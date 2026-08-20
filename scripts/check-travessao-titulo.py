#!/usr/bin/env python3
"""Trava a regra de compilação de 2026-08-17: nada de `—` em TÍTULO.

Dono: revisor1.

POR QUE ISTO EXISTE
-------------------
A classe da UFPR maiusculiza títulos ao escrevê-los no sumário. A maiusculização
parte o caractere multibyte `—` (U+2014) e grava um byte solto (U+0080) no
`.toc`, e o PDF inteiro deixa de compilar. Foram **6 builds vermelhos** em
2026-08-17 (02:35 a 06:25 UTC) por causa de UM título convertido na unificação
tipográfica do R1.

A regra virou prosa em `docs/criterio-humanizacao.md`. Esta é a forma
executável dela, pelo princípio IX e pela skill `verifiable-dod`: critério que
depende de alguém lembrar é critério que falha na terceira ocorrência.

POR QUE NÃO BASTA O BUILD COMO CANÁRIO
--------------------------------------
O `tese-pdf.yml` só roda no push da `main`. Uma branch de revisão carrega o
defeito até o merge, e aí quem quebra a `main` é o merge — que é exatamente o
que aconteceu. Esta checagem roda em qualquer branch, em menos de um segundo,
antes do push.

REGRA (com a exceção aprovada pelo autor em 2026-08-17)
-------------------------------------------------------
Em `\\chapter`, `\\section`, `\\subsection`, `\\subsubsection`, `\\paragraph`
e `\\title`, o travessão é a ligadura ASCII `---` — violação REPROVA (exit 1).

`\\caption` é EXCEÇÃO registrada (`docs/criterio-humanizacao.md`): as listas
de figuras e tabelas não maiusculizam, e builds com `—` em legenda saem
verdes (comprovado em 2026-08-17). Legenda com `—` vira AVISO, nunca
reprovação — o DoD de fatia não pode ser bloqueado por ela.

No CORPO do texto a unificação `---` → `—` continua valendo: a exceção é só
de título (proibição) e caption (aviso).

LIMITES DECLARADOS
------------------
1. Detecta o comando e o `—` na MESMA linha. Um título quebrado em duas linhas
   com o travessão na segunda escapa. É conservador: subconta, nunca acusa
   falso.
2. Não valida chaves balanceadas — não distingue o `—` que está dentro do
   argumento do título daquele que viesse depois do `}` na mesma linha. Na
   prática do repositório os títulos ocupam a linha inteira.

Saída: lista os casos; exit 1 só se houver violação em TÍTULO.
"""
from __future__ import annotations

import glob
import re
import sys

COMANDOS_TITULO = ("chapter", "section", "subsection", "subsubsection",
                   "paragraph", "title")
COMANDOS_AVISO = ("caption",)

_PADRAO = re.compile(
    r"\\(" + "|".join(COMANDOS_TITULO + COMANDOS_AVISO) + r")\*?\s*(?:\[[^\]]*\])?\s*\{"
)

TRAVESSAO = "—"  # —


def varrer(arquivos: list[str]) -> list[dict]:
    achados: list[dict] = []
    for caminho in arquivos:
        try:
            linhas = open(caminho, encoding="utf-8").read().split("\n")
        except (OSError, UnicodeDecodeError):
            continue
        for numero, linha in enumerate(linhas, 1):
            m = _PADRAO.search(linha)
            if m and TRAVESSAO in linha[m.start():]:
                achados.append({
                    "arquivo": caminho,
                    "linha": numero,
                    "comando": m.group(1),
                    "severidade": ("aviso" if m.group(1) in COMANDOS_AVISO
                                   else "erro"),
                    "texto": linha.strip(),
                })
    return achados


def main() -> int:
    alvos = sys.argv[1:] or sorted(glob.glob("*/texto.tex") + glob.glob("*.tex"))
    achados = varrer(alvos)
    erros = [a for a in achados if a["severidade"] == "erro"]
    avisos = [a for a in achados if a["severidade"] == "aviso"]
    if not achados:
        print(f"travessão em título/caption: nenhum ({len(alvos)} arquivos)")
        return 0
    if erros:
        print(f"PROBLEMAS ({len(erros)}) — use '---' no lugar de '{TRAVESSAO}':")
        for a in erros:
            print(f"  {a['arquivo']}:{a['linha']}  \\{a['comando']}")
            print(f"     {a['texto'][:100]}")
    if avisos:
        print(f"AVISOS ({len(avisos)}) — legenda com '{TRAVESSAO}' compila, "
              "mas a unificação é bem-vinda (exceção registrada):")
        for a in avisos:
            print(f"  {a['arquivo']}:{a['linha']}  \\{a['comando']}")
            print(f"     {a['texto'][:100]}")
    return 1 if erros else 0


if __name__ == "__main__":
    raise SystemExit(main())
