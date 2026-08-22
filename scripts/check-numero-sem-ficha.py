#!/usr/bin/env python3
"""Número atribuído a obra cujo FICHAMENTO não tem número para dar.

Dono: revisor2. Quarto da família de guardas (check-largura-tabela,
check-travessao-titulo, check-bib).

O PROBLEMA QUE ISTO RESOLVE
---------------------------
A constituição da tese exige "referência validada contra fichamento" e
"nenhum número sem artefato rastreável". Os dois se encontram num ponto que
nenhuma checagem cobria: uma frase que atribui um NÚMERO a uma obra cujo
fichamento, na seção "Números que posso citar", não traz número nenhum — e
às vezes diz textualmente que a obra não serve para isso ("Livro conceitual;
usar como fonte de definições, não de números").

O caso que motivou o guarda, achado à mão em 2026-08-22:

    "menos de $10\\%$ na ilustração canônica de \\citet{Settles2009}"

O fichamento `Settles2009.md` remete a `Settles2012.md`, e este diz
"(Livro conceitual; usar como fonte de definições, não de números.)". O
número não é necessariamente falso — é NÃO VALIDADO, e a banca pergunta
"onde, no Settles, está esse 10%?".

Na mesma frase, "até $15{,}45\\%$ em \\citet[Tab.~3]{Schroder2022Uncertainty}"
está impecável: o fichamento traz o valor, a tabela de origem e a quebra por
conjunto. Esses dois formam o par positivo/negativo do DoD.

COMO CLASSIFICA UM FICHAMENTO
-----------------------------
Lê a seção `## Números que posso citar`. Antes de procurar dígito, REMOVE
chaves de citação (`Settles2012`) e anos soltos — sem isso, uma ficha que
apenas remete a outra ("Ver fichamento Settles2012") passaria por ter número,
que foi exatamente o erro da primeira versão desta checagem.

  - sobra dígito           -> a obra TEM número citável  (não sinaliza)
  - não sobra dígito       -> a obra NÃO tem número      (sinaliza)
  - seção ausente          -> DESCONHECIDO               (não sinaliza)

A seção ausente não sinaliza de propósito: o guarda acusa o que sabe estar
sem lastro, não o que não sabe. Guarda que grita no escuro é desligado.

COMO ATRIBUI UM NÚMERO A UMA CITAÇÃO
------------------------------------
Por SENTENÇA, nunca por linha. A primeira versão trabalhava por linha e
falhou dos dois lados: deu falso positivo (o 15,45% da linha 114 do Cap.1 foi
atribuído ao Settings citado na mesma linha) e perdeu o caso real (o "<10%"
está na linha 113 e a citação fecha na 114).

Para cada número, procura a citação mais próxima SEM cruzar fim de sentença,
primeiro para a frente (convenção `X\\% \\citep{k}`) e depois para trás
(convenção `\\citet{k} reporta X\\%`). Se a citação mais próxima tiver várias
chaves, só sinaliza quando TODAS estão sem número: qualquer uma com número
pode ser a fonte, e acusar nesse caso seria chutar.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# --------------------------------------------------------------- fichamentos
SECAO = re.compile(r"^## Números que posso citar\s*$(.*?)(?=^## |\Z)", re.M | re.S)
CHAVE_BIB = re.compile(r"\b[A-Z][A-Za-z]*\d{4}[A-Za-z]*\b")
ANO = re.compile(r"\b(?:19|20)\d{2}\b")

TEM, NAO_TEM, DESCONHECIDO = "tem", "nao-tem", "desconhecido"


def classifica_fichamentos(raiz: str) -> dict:
    """chave -> TEM | NAO_TEM (a seção existe mas não sobrou dígito)."""
    dir_f = os.path.join(raiz, "fichamentos")
    estado = {}
    if not os.path.isdir(dir_f):
        return estado
    for nome in sorted(os.listdir(dir_f)):
        if not nome.endswith(".md") or nome.startswith("_"):
            continue
        caminho = os.path.join(dir_f, nome)
        try:
            with open(caminho, encoding="utf-8") as fh:
                texto = fh.read()
        except Exception:
            continue
        m = SECAO.search(texto)
        if not m:
            continue                      # sem a seção -> desconhecido
        limpo = ANO.sub(" ", CHAVE_BIB.sub(" ", m.group(1)))
        estado[nome[:-3]] = TEM if re.search(r"\d", limpo) else NAO_TEM
    return estado


# ------------------------------------------------------------------ o .tex
CITE = re.compile(r"\\(?:cite|citet|citep|citealp|citeauthor|citeyear)[a-z]*\*?"
                  r"(?:\[[^\]]*\])*\{([^}]*)\}")
ESTRUTURAL = re.compile(r"\\(?:ref|autoref|pageref|eqref|label|cite[a-z]*\*?"
                        r"(?:\[[^\]]*\])*)\{[^{}]*\}")
# "Tabela~2", "Seção 3.1", "Capítulo 4", "(i)", "Fase 2", "Tab. 3"
CONTEXTO_ESTRUTURAL = re.compile(
    r"(?:tabela|tab\.|se[çc][ãa]o|sec\.|cap[íi]tulo|cap\.|figura|fig\.|"
    r"algoritmo|equa[çc][ãa]o|fase|princ[íi]pio|item)\s*~?\s*$", re.I)
# ESCOPO DELIBERADAMENTE ESTREITO: só PERCENTUAL. A primeira versão pegava
# qualquer número e acertava 1 em 7 — os outros 6 eram parâmetros do próprio
# método (b_0 = 0,01·B) que dividiam sentença com uma citação de definição.
# Guarda com 1/7 de precisão é desligado no primeiro dia. Percentual é onde
# mora a comparação com a literatura, que é o que se quer validar contra a
# ficha; o preço declarado é não cobrir número absoluto.
NUMERO = re.compile(r"\d+(?:[.,]|\{,\})?\d*\s*\\?%")
JANELA = 120   # caracteres entre o número e a citação (o caso real tem 37)
FIM_SENTENCA = re.compile(r"(?<![A-Z])\.(?=\s+[A-ZÀ-Ý])|\.\s*$|\n\s*\n")


def _sentencas(texto: str):
    """(inicio, fim) de cada sentença, com o parágrafo em branco também
    fechando sentença — em LaTeX o ponto final costuma faltar antes de um
    ambiente, e sem isso um número atravessaria meia página."""
    inicio, limites = 0, []
    for m in FIM_SENTENCA.finditer(texto):
        limites.append((inicio, m.end()))
        inicio = m.end()
    if inicio < len(texto):
        limites.append((inicio, len(texto)))
    return limites


def _chaves_das_citacoes(texto: str):
    """[(inicio, fim, [chaves])] de cada comando de citação."""
    saida = []
    for m in CITE.finditer(texto):
        chaves = [c.strip() for c in m.group(1).split(",") if c.strip()]
        if chaves:
            saida.append((m.start(), m.end(), chaves))
    return saida


def _mascara_estrutural(texto: str) -> str:
    """Troca por espaço o que tem número mas não é dado: \\ref{}, \\label{},
    e o miolo das próprias citações (senão o ano da chave vira 'número')."""
    return ESTRUTURAL.sub(lambda m: " " * len(m.group(0)), texto)


def analisa(caminho: str, estado: dict):
    with open(caminho, encoding="utf-8") as fh:
        bruto = fh.read()
    mascarado = _mascara_estrutural(bruto)
    citacoes = _chaves_das_citacoes(bruto)      # posições valem nos dois
    achados = []
    for ini, fim in _sentencas(mascarado):
        trecho = mascarado[ini:fim]
        locais = [(a, b, k) for a, b, k in citacoes if ini <= a < fim]
        if not locais:
            continue
        for mn in NUMERO.finditer(trecho):
            pos = ini + mn.start()
            antes = mascarado[max(ini, pos - 40):pos]
            if CONTEXTO_ESTRUTURAL.search(antes.strip()):
                continue                        # "Tabela 3", "Seção 2"
            fim_num = ini + mn.end()
            frente = [c for c in locais if c[0] >= fim_num and c[0] - fim_num <= JANELA]
            atras = [c for c in locais if c[1] <= pos and pos - c[1] <= JANELA]
            alvo = frente[0] if frente else (atras[-1] if atras else None)
            if alvo is None:
                continue                        # citação longe demais: não é atribuição
            chaves = alvo[2]
            conhecidas = [k for k in chaves if k in estado]
            if not conhecidas:
                continue                        # nenhuma ficha conhecida
            if any(estado[k] == TEM for k in conhecidas):
                continue                        # alguma pode sustentar
            achados.append({
                "linha": bruto.count("\n", 0, pos) + 1,
                "numero": mn.group(0).strip(),
                "chaves": chaves,
                "sentenca": re.sub(r"\s+", " ", bruto[ini:fim]).strip()[:160],
            })
    return achados


# Superficies onde um numero pode ser atribuido a uma citacao. Nao e' "todo
# .tex do repositorio" de proposito: preambulo, folhas de rosto e arquivos
# gerados nao tem prosa com citacao, e varrer o que nao interessa so gera
# ruido. A defesa e os artigos entram porque numero errado ali chega a banca
# e a revisores externos antes de chegar a tese.
PADROES_PADRAO = (
    "[0-9]-*/texto.tex",
    "a4-biblioteca/texto.tex",
    "apresentacao/*.tex",
    "artigos/*/main.tex",
)


def superficies_padrao():
    import glob
    achados = []
    for padrao in PADROES_PADRAO:
        achados.extend(glob.glob(padrao))
    return sorted(set(achados))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("arquivos", nargs="*", help="padrão: os capítulos N-*/texto.tex")
    p.add_argument("--raiz", default=None, help="raiz do repositório")
    args = p.parse_args()

    raiz = args.raiz
    if raiz is None:
        try:
            raiz = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                  capture_output=True, text=True, timeout=5,
                                  cwd=os.path.dirname(os.path.abspath(__file__))
                                  ).stdout.strip() or os.getcwd()
        except Exception:
            raiz = os.getcwd()
    os.chdir(raiz)

    estado = classifica_fichamentos(raiz)
    if not estado:
        print("check-numero-sem-ficha: nenhum fichamento legível — nada a checar.")
        return 0

    alvos = args.arquivos
    if not alvos:
        alvos = superficies_padrao()

    total = 0
    for arq in alvos:
        if not os.path.exists(arq):
            continue
        for a in analisa(arq, estado):
            total += 1
            print(f"{arq}:{a['linha']}: número {a['numero']!r} atribuído a "
                  f"{'/'.join(a['chaves'])}, cujo fichamento não declara número citável")
            print(f"    {a['sentenca']}")
    n_sem = sum(1 for v in estado.values() if v == NAO_TEM)
    if total:
        print(f"\ncheck-numero-sem-ficha: {total} atribuição(ões) sem lastro "
              f"({n_sem} fichas sem número citável, de {len(estado)} com a seção).")
        print("Conserte de um dos dois lados: registre o número (com página/tabela) "
              "na seção 'Números que posso citar' da ficha, ou cite obra que o tenha.")
        return 1
    print(f"check-numero-sem-ficha: nenhuma atribuição sem lastro "
          f"({n_sem} fichas sem número citável, de {len(estado)} com a seção).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
