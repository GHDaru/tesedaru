#!/usr/bin/env python3
"""Trava a regra de compilação de 2026-08-17: nada de `—` em título ou caption.

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

REGRA
-----
Em `\\chapter`, `\\section`, `\\subsection`, `\\subsubsection`, `\\paragraph`,
`\\caption` e `\\title`, o travessão é a ligadura ASCII `---`. No CORPO do
texto a unificação `---` → `—` continua valendo: a exceção é só de título e
caption.

LIMITES DECLARADOS
------------------
1. Detecta o comando e o `—` na MESMA linha. Um título quebrado em duas linhas
   com o travessão na segunda escapa. É conservador: subconta, nunca acusa
   falso.
2. Não valida chaves balanceadas — não distingue o `—` que está dentro do
   argumento do título daquele que viesse depois do `}` na mesma linha. Na
   prática do repositório os títulos ocupam a linha inteira.
3. `\\caption` foi verificado empiricamente como NÃO quebrando o build hoje
   (o build ficou verde com dois deles presentes). Está na checagem porque a
   regra publicada o inclui e porque o comportamento depende da classe listar
   ou não figuras e tabelas — é risco latente, não falha ativa.

Saída: lista os casos e devolve exit 1 se houver algum.
"""
from __future__ import annotations

import glob
import re
import sys

COMANDOS = ("chapter", "section", "subsection", "subsubsection",
            "paragraph", "caption", "title")

_PADRAO = re.compile(
    r"\\(" + "|".join(COMANDOS) + r")\*?\s*(?:\[[^\]]*\])?\s*\{"
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
                    "texto": linha.strip(),
                })
    return achados


def main() -> int:
    alvos = sys.argv[1:] or sorted(glob.glob("*/texto.tex") + glob.glob("*.tex"))
    achados = varrer(alvos)
    if not achados:
        print(f"travessão em título/caption: nenhum ({len(alvos)} arquivos)")
        return 0
    print(f"PROBLEMAS ({len(achados)}) — use '---' no lugar de '{TRAVESSAO}':")
    for a in achados:
        print(f"  {a['arquivo']}:{a['linha']}  \\{a['comando']}")
        print(f"     {a['texto'][:100]}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
