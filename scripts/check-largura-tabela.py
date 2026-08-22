#!/usr/bin/env python3
"""Avisa quando uma tabela cresce a ponto de provavelmente estourar a mancha.

Dono: revisor2.

POR QUE ISTO EXISTE
-------------------
Em 2026-08-21 a Fase 2 do expurgo de pilares trocou tokens curtos (`P1`) por
nomes longos (`conjunto inicial / partida a frio`) dentro da Tabela 3.1, que
usa `\\begin{tabular}{llll}`. Passou por TRÊS verificações de conteúdo — a
minha cruzada (números como multiconjunto, refs/cites, coluna Id byte a byte,
siglas, três validadores em exit 0), o DoD do revisor1 e o gate do autor — e
o autor encontrou o defeito lendo o PDF: a última coluna cortada, "Resultado
em" virando "Resultad".

Nenhuma daquelas verificações olha para o CONTÊINER. E o agente que fez a
cruzada não tem motor LaTeX no contêiner dele (`pdflatex`, `xelatex`,
`lualatex`, `latexmk` e `tectonic` todos ausentes), então não podia renderizar
nem que quisesse. Isto aqui é o substituto barato: não diz se a tabela estoura
— diz que alguém precisa OLHAR o PDF antes do merge.

Medido contra aquele caso por esta própria ferramenta: a soma das colunas
livres foi de 90 para 127 caracteres (+41%), com a coluna "Pilar" indo de 16
para 33 (x2,1) e a "Resultado em" de 12 para 30 (x2,5). São exatamente as duas
que saíram cortadas no PDF.

O QUE É MEDIDO, E POR QUE ESTA MEDIDA
-------------------------------------
Só colunas de largura LIVRE (`l`, `c`, `r`) entram na conta. Colunas com
largura declarada (`p{}`, `m{}`, `b{}`, `X` de `tabularx`) QUEBRAM a linha:
podem ficar feias, mas não empurram a tabela para fora da página. O que
estoura a mancha é a soma das colunas livres, cada uma tão larga quanto a sua
célula mais longa.

Comandos LaTeX são removidos antes de contar (`\\textbf{Id}` conta 2, não 13),
porque o que ocupa espaço é o texto composto, não a marcação.

DOIS MODOS
----------
1. ABSOLUTO (padrão): reprova tabela cuja soma de colunas livres passe do
   orçamento. Pega tabela nova nascida larga.
2. REGRESSÃO (`--base REF`): compara com outra revisão do git e reprova
   crescimento — na soma ou em qualquer coluna isolada. Pega o caso de 21/08,
   em que a tabela já era larga e a mudança a empurrou para fora.

Os dois modos podem rodar juntos.

LIMITES DECLARADOS — leia antes de confiar
------------------------------------------
1. **É proxy, não tipografia.** Conta CARACTERES. Não conhece fonte, kerning,
   `\\tabcolsep`, nem se a tabela está em `\\small` ou dentro de um
   `\\resizebox`. Uma tabela pode passar aqui e estourar no PDF, e o inverso
   também. Verde aqui NÃO substitui olhar a página.
2. **O orçamento é empírico, de UM caso só.** O padrão (110) está entre os
   dois únicos pontos que existem: **90 cabia** (a Tabela 3.1 viveu meses
   assim sem ninguém reclamar) e **127 não coube** (o autor viu cortado, em
   `\\small`). Não é derivado de largura de mancha nem de métrica de fonte —
   é um valor espremido entre um acerto e um erro observados, e o "90 cabia"
   é inferido de ausência de reclamação, não de medição. Ajuste com
   `--orcamento` assim que houver mais casos.
3. **`\\multicolumn` é ignorado**: uma célula que atravessa colunas não define
   a largura de nenhuma delas isoladamente.
4. **Tabela gerada por script** (a partir de JSON, por exemplo) é medida como
   está no `.tex` no momento da checagem.
5. **Sem coluna livre, a tabela é pulada** — tudo `p{}`/`X` não estoura por
   este mecanismo.

USO
---
    python3 scripts/check-largura-tabela.py                    # absoluto, todos os .tex
    python3 scripts/check-largura-tabela.py --base origin/main # + regressão
    python3 scripts/check-largura-tabela.py 3-metodo/texto.tex # só um arquivo

Exit 0 = nada a relatar. Exit 1 = alguém precisa olhar o PDF.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

# Ambientes que compõem uma grade de colunas.
AMBIENTES = ("tabular", "tabularx", "tabulary", "longtable", "tabular*")

ORCAMENTO_PADRAO = 110     # ver LIMITE 2: espremido entre 90 (coube) e 127 (nao)
CRESC_SOMA = 0.20          # +20% na soma das colunas livres
CRESC_COLUNA = 2.0         # qualquer coluna livre dobrando


# Comandos cujo ARGUMENTO não é composto como está: o PDF põe outra coisa no
# lugar. `\ref{sec:res-l0-sens}` sai como "4.1"; contar o rótulo inteiro
# inflaria a coluna em vinte caracteres que não existem na página.
REFERENCIA = ("ref", "autoref", "pageref", "eqref", "cite", "citep", "citet",
              "citealp", "label", "tnote", "footnote")
LARGURA_REF = 3        # "4.1", "2.7" — a largura típica de uma referência composta


def _sem_latex(celula: str) -> str:
    """Texto como ele SAI COMPOSTO, não como está escrito.

    Duas famílias de comando, tratadas de formas opostas — e a distinção é o
    ponto todo desta função:

    - `\\textbf{Id}`, `\\emph{...}`, `\\texttt{...}` carregam o texto no
      argumento: some o comando, FICA o argumento;
    - `\\ref{sec:res-l0-sens}` NÃO carrega: o PDF imprime um número curto.
      Some comando e argumento, entra um marcador de largura típica.

    Tratar os dois igual foi o erro do meu primeiro protótipo: contando o
    rótulo do `\\ref` inteiro, a última coluna da Tabela 3.1 media 22 em vez
    dos ~9 que a página mostra.
    """
    s = celula
    for cmd in REFERENCIA:                          # \ref{...} -> "###"
        s = re.sub(r"\\" + cmd + r"\*?\s*(\[[^\]]*\])?\{[^{}]*\}",
                   "#" * LARGURA_REF, s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)            # \textbf, \small… (fica o arg.)
    s = re.sub(r"[{}$]", "", s)
    s = s.replace("~", " ").replace(r"\\", "")
    return re.sub(r"\s+", " ", s).strip()


def _colunas_livres(spec: str):
    """Índices das colunas de largura livre (l/c/r) na especificação.

    `p{3cm}`, `m{2cm}`, `b{1cm}` e `X` declaram largura e quebram linha, então
    não empurram a tabela para fora — não entram na conta.
    """
    livres, i, idx = [], 0, 0
    while i < len(spec):
        ch = spec[i]
        if ch in "lcr":
            livres.append(idx); idx += 1
        elif ch in "pmb" and i + 1 < len(spec) and spec[i + 1] == "{":
            prof, j = 0, i + 1
            while j < len(spec):                    # pula o argumento inteiro
                if spec[j] == "{": prof += 1
                elif spec[j] == "}":
                    prof -= 1
                    if prof == 0: break
                j += 1
            i = j; idx += 1
        elif ch == "X":
            idx += 1
        elif ch == "@" and i + 1 < len(spec) and spec[i + 1] == "{":
            prof, j = 0, i + 1                      # @{...} não é coluna
            while j < len(spec):
                if spec[j] == "{": prof += 1
                elif spec[j] == "}":
                    prof -= 1
                    if prof == 0: break
                j += 1
            i = j
        i += 1
    return livres


def tabelas(texto: str, arquivo: str):
    """Cada tabela do arquivo: (rótulo, spec, larguras por coluna, linha)."""
    padrao = re.compile(
        r"\\begin\{(" + "|".join(re.escape(a) for a in AMBIENTES) + r")\}"
        r"\s*(?:\[[^\]]*\])?\s*(?:\{[^{}]*\}\s*)??\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}"
        r"(.*?)\\end\{\1\}", re.S)
    for m in padrao.finditer(texto):
        spec, corpo = m.group(2), m.group(3)
        linha = texto[: m.start()].count("\n") + 1
        larg = {}
        for ln in corpo.splitlines():
            ln = ln.strip()
            if "&" not in ln or ln.startswith("%") or "\\multicolumn" in ln:
                continue
            for i, cel in enumerate(ln.rstrip("\\ ").split("&")):
                t = _sem_latex(cel)
                if len(t) > larg.get(i, 0):
                    larg[i] = len(t)
        # rótulo: o \label mais próximo antes do \begin
        antes = texto[max(0, m.start() - 700): m.start()]
        rot = re.findall(r"\\label\{([^}]*)\}", antes)
        yield (rot[-1] if rot else f"{os.path.basename(arquivo)}:{linha}",
               spec, larg, linha)


def medir(texto: str, arquivo: str):
    """{rótulo: (soma das colunas livres, {coluna: largura}, linha)}."""
    out = {}
    for rot, spec, larg, linha in tabelas(texto, arquivo):
        livres = _colunas_livres(spec)
        if not livres:
            continue
        so_livres = {i: larg.get(i, 0) for i in livres}
        out[rot] = (sum(so_livres.values()), so_livres, linha)
    return out


def _do_git(ref: str, caminho: str):
    r = subprocess.run(["git", "show", f"{ref}:{caminho}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("arquivos", nargs="*", help="padrão .tex (padrão: todos)")
    ap.add_argument("--base", help="revisão git para comparar (modo regressão)")
    ap.add_argument("--orcamento", type=int, default=ORCAMENTO_PADRAO,
                    help=f"limite absoluto por tabela (padrão {ORCAMENTO_PADRAO})")
    a = ap.parse_args()

    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(raiz)
    alvos = a.arquivos or sorted(
        p for p in glob.glob("**/*.tex", recursive=True)
        if not p.startswith((".", "build/")))

    problemas, vistas = [], 0
    for arq in alvos:
        try:
            with open(arq, encoding="utf-8") as fh:
                agora = medir(fh.read(), arq)
        except (OSError, UnicodeDecodeError):
            continue
        vistas += len(agora)

        for rot, (soma, cols, linha) in sorted(agora.items()):
            if soma > a.orcamento:
                det = " ".join(f"c{i+1}={w}" for i, w in sorted(cols.items()))
                problemas.append(
                    f"{arq}:{linha}: {rot} — colunas livres somam {soma} "
                    f"caracteres, acima do orcamento {a.orcamento} ({det})")

        if not a.base:
            continue
        bruto = _do_git(a.base, arq)
        if bruto is None:
            continue
        antes = medir(bruto, arq)
        for rot, (soma, cols, linha) in sorted(agora.items()):
            if rot not in antes:
                continue
            soma0, cols0, _ = antes[rot]
            if soma0 and soma > soma0 * (1 + CRESC_SOMA):
                problemas.append(
                    f"{arq}:{linha}: {rot} — soma das colunas livres foi de "
                    f"{soma0} para {soma} ({100*(soma-soma0)/soma0:+.0f}%) "
                    f"contra {a.base}")
            for i, w in sorted(cols.items()):
                w0 = cols0.get(i, 0)
                if w0 and w >= w0 * CRESC_COLUNA:
                    problemas.append(
                        f"{arq}:{linha}: {rot} — coluna {i+1} foi de {w0} para "
                        f"{w} caracteres (x{w/w0:.1f}) contra {a.base}")

    if problemas:
        print(f"largura de tabela: {len(problemas)} sinal(is) — "
              f"ALGUEM PRECISA OLHAR O PDF", file=sys.stderr)
        for p in problemas:
            print(f"  {p}", file=sys.stderr)
        print("\nIsto e proxy de caracteres, nao tipografia: confirme na pagina "
              "antes de mexer, e ajuste --orcamento se o alarme for falso.",
              file=sys.stderr)
        return 1

    print(f"largura de tabela: nada a relatar ({vistas} tabela(s) com coluna livre)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
