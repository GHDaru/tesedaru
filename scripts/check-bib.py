#!/usr/bin/env python3
"""Checagem executável do referencias.bib (princípios II e IX da constituição).

Dono: revisor2 (ciclo bib-fix, lotes 1 e 3 — tarefa do principal 2026-08-16).

Transforma o DoD do parecer de auditoria em comandos. Verifica:

  1. toda chave citada em `\\cite*{...}` nos capítulos e apêndices existe no
     `referencias.bib` (evita "citação indefinida" na compilação);
  2. nenhuma chave duplicada no arquivo;
  3. nenhuma chave morta pelo ciclo bib-fix reaparece citada (lista abaixo);
  4. nenhum campo `note` com resíduo de conversa de modelo de linguagem
     (o parecer achou 2 vazando para o PDF);
  5. nenhum campo `key = {...}` residual (artefato que confunde o BibTeX);
  6. toda entrada citada com `year >= 2020` tem `doi` ou `url`.

O item 6 é o critério do DoD §5 do parecer. Entradas não citadas ficam de fora
dele de propósito: o que não é citado não entra no PDF.

Uso:  python3 scripts/check-bib.py
Exit 0 = verde; exit 1 = imprime cada violação. Sem dependências externas.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "referencias.bib"

# Chaves removidas pelo ciclo bib-fix — nenhuma pode voltar a ser citada.
MORTAS = {
    "Su2023", "FreeAL2023",        # -> Xiao2023FreeAL
    "Bayer2024", "activellm2024",  # -> Bayer2024ActiveLLM
    "Zhang2025LLMAL",              # -> Zhang2025
    "Yusuf2023",                   # obra fabricada; a real é Riyanto2023Comparative
    "Jung2021",                    # obra fabricada; a real é Nti2021
}

def fontes_tex() -> list[Path]:
    """Capítulos, pré-textuais e apêndices — não inclui artigos/ (bib próprio)."""
    return [p for p in ROOT.glob("*/texto.tex")] + list((ROOT / "0-iniciais").glob("*.tex"))

def main() -> int:
    texto = BIB.read_text(encoding="utf-8", errors="replace")
    problemas: list[str] = []

    chaves = re.findall(r"^@\w+\{\s*([^,\s]+)\s*,", texto, flags=re.M)
    vistas: set[str] = set()
    for c in chaves:
        if c in vistas:
            problemas.append(f"chave duplicada no bib: {c}")
        vistas.add(c)

    # Chaves ancoradas por fichamento: são nós do grafo de conhecimento e
    # NÃO são órfãs, mesmo sem \cite na prosa — remover uma quebraria o KG e
    # o check-fichamentos.py. (Achado do ciclo bib-fix: a regra "matar órfã"
    # do parecer, aplicada cegamente, mataria Sener2018 e Shen2018.)
    ancoradas = {p.stem for p in (ROOT / "fichamentos").glob("*.md")
                 if not p.name.startswith("_")}
    for chave in sorted(ancoradas - vistas):
        problemas.append(f"fichamento sem entrada no bib: {chave}")

    citadas: dict[str, list[str]] = {}
    for path in fontes_tex():
        conteudo = path.read_text(encoding="utf-8", errors="replace")
        for grupo in re.findall(r"\\[a-zA-Z]*cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", conteudo):
            for chave in (k.strip() for k in grupo.split(",")):
                if chave:
                    citadas.setdefault(chave, []).append(path.name)

    for chave, onde in sorted(citadas.items()):
        if chave not in vistas:
            problemas.append(f"citada mas ausente do bib: {chave} (em {', '.join(sorted(set(onde)))})")
        if chave in MORTAS:
            problemas.append(f"chave morta pelo bib-fix voltou a ser citada: {chave}")

    if re.search(r"note\s*=\s*\{[^}]*(?:as an AI|language model|I cannot|Não posso|As an AI)", texto, re.I):
        problemas.append("campo note com resíduo de conversa de modelo de linguagem")
    for m in re.finditer(r"^\s*key\s*=\s*\{", texto, flags=re.M):
        problemas.append(f"campo 'key = {{...}}' residual na posição {m.start()}")

    for m in re.finditer(r"^@\w+\{\s*([^,\s]+)\s*,", texto, flags=re.M):
        chave = m.group(1)
        if chave not in citadas:
            continue
        i = m.start(); j = texto.index("{", i); d = 0
        for k in range(j, len(texto)):
            if texto[k] == "{": d += 1
            elif texto[k] == "}":
                d -= 1
                if d == 0:
                    corpo = texto[i:k + 1]; break
        ano = re.search(r"year\s*=\s*\{?\s*(\d{4})", corpo)
        if ano and int(ano.group(1)) >= 2020:
            if not re.search(r"^\s*(doi|url)\s*=", corpo, flags=re.M | re.I):
                problemas.append(f"citada, year={ano.group(1)}, sem doi nem url: {chave}")

    print(f"entradas no bib: {len(chaves)} · chaves citadas nos .tex: {len(citadas)}")
    if problemas:
        print(f"PROBLEMAS ({len(problemas)}):")
        for p in problemas:
            print(f"  - {p}")
        return 1
    print("PROBLEMAS: nenhum")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
