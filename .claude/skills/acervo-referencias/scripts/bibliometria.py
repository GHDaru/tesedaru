#!/usr/bin/env python
"""Estagio 5 — bibliometria do acervo, toda ela derivada de arquivo.

Dono: agente `local` (skill acervo-referencias).
Uso:  uv run --with pyyaml python bibliometria.py --acervo .

Constituicao da tese, principio V: nenhum numero sem artefato rastreavel.
Por isso cada contagem sai daqui em CSV, e o relatorio em markdown so aponta
para os CSVs. Numero digitado a mao em relatorio nao e' bibliometria, e' chute
com formatacao.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml


def ler_front(p: Path) -> dict:
    txt = p.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return {}
    _, bloco, _ = txt.split("---", 2)
    return yaml.safe_load(bloco) or {}


def chaves_bib(acervo: Path) -> set[str]:
    bib = acervo / "referencias.bib"
    if not bib.exists():
        return set()
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,",
                          bib.read_text(encoding="utf-8", errors="replace")))


def escrever(destino: Path, cabecalho: list[str], linhas) -> int:
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cabecalho)
        n = 0
        for ln in linhas:
            w.writerow(ln)
            n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--acervo", type=Path,
                    default=Path(os.environ.get("ACERVO", ".")))
    a = ap.parse_args()
    acervo, saida = a.acervo, a.acervo / "bibliometria"

    fichas = {p.stem: ler_front(p)
              for p in sorted((acervo / "fichas").glob("*.md"))
              if not p.stem.startswith("_")}
    bib = chaves_bib(acervo)
    pdfs = {p.stem for p in (acervo / "pdf").glob("*.pdf")}

    # --- cobertura: a pergunta que a banca faz -------------------------------
    todas = sorted(bib | set(fichas))
    escrever(saida / "cobertura.csv",
             ["chave", "na_bib", "tem_ficha", "tem_pdf", "canonica", "status"],
             ([k, k in bib, k in fichas, k in pdfs,
               bool(fichas.get(k, {}).get("canonica")),
               fichas.get(k, {}).get("status", "")] for k in todas))

    # --- autoria -------------------------------------------------------------
    autores = Counter()
    muitos = []
    for k, f in fichas.items():
        aut = f.get("authors") or []
        for nome in aut:
            autores[str(nome)] += 1
        if len(aut) >= 5:
            muitos.append([k, len(aut), "; ".join(str(x) for x in aut)])
    escrever(saida / "autores.csv", ["autor", "obras"], autores.most_common())
    escrever(saida / "autoria-5-ou-mais.csv", ["chave", "n_autores", "autores"],
             sorted(muitos, key=lambda r: -r[1]))

    # --- ano, veiculo, tipo --------------------------------------------------
    escrever(saida / "por-ano.csv", ["ano", "obras"],
             sorted(Counter(f.get("year") for f in fichas.values()).items(),
                    key=lambda kv: (kv[0] is None, kv[0])))
    escrever(saida / "por-veiculo.csv", ["veiculo", "obras"],
             Counter(f.get("venue") or "(sem veiculo)"
                     for f in fichas.values()).most_common())
    escrever(saida / "por-tipo.csv", ["paper_type", "obras"],
             Counter(f.get("paper_type") or "(sem tipo)"
                     for f in fichas.values()).most_common())

    # --- DOIs: presenca e duplicidade ---------------------------------------
    por_doi = defaultdict(list)
    for k, f in fichas.items():
        d = (f.get("doi") or "").strip().lower()
        if d:
            por_doi[d].append(k)
    dups = {d: ks for d, ks in por_doi.items() if len(ks) > 1}
    escrever(saida / "dois.csv", ["doi", "chaves"],
             ((d, "; ".join(ks)) for d, ks in sorted(por_doi.items())))

    # --- mapa chave x capitulo da tese --------------------------------------
    linhas_mapa = []
    for k, f in sorted(fichas.items()):
        for cap in f.get("cited_in") or []:
            linhas_mapa.append([k, cap])
    escrever(saida / "mapa-citacao-por-capitulo.csv", ["chave", "capitulo"], linhas_mapa)

    # --- relatorio: so aponta para os CSVs -----------------------------------
    sem_ficha = sorted(bib - set(fichas))
    sem_pdf = sorted(k for k, f in fichas.items()
                     if k not in pdfs and not f.get("canonica"))
    nunca_citada = sorted(k for k, f in fichas.items() if not (f.get("cited_in") or []))

    rel = [
        "# Bibliometria do acervo",
        "",
        "> Gerado por `scripts/bibliometria.py`. **Nao editar a mao**: todo numero",
        "> aqui resolve para um CSV desta pasta (constituicao da tese, principio V).",
        "",
        "| grandeza | valor | artefato |",
        "|---|---|---|",
        f"| entradas no referencias.bib | {len(bib)} | `referencias.bib` |",
        f"| fichas | {len(fichas)} | `fichas/` |",
        f"| PDFs no acervo | {len(pdfs)} | `pdf/` |",
        f"| chaves na bib sem ficha | {len(sem_ficha)} | `cobertura.csv` |",
        f"| fichas sem PDF e sem `canonica` | {len(sem_pdf)} | `cobertura.csv` |",
        f"| autores distintos | {len(autores)} | `autores.csv` |",
        f"| obras com 5+ autores | {len(muitos)} | `autoria-5-ou-mais.csv` |",
        f"| DOIs distintos | {len(por_doi)} | `dois.csv` |",
        f"| DOIs duplicados | {len(dups)} | `dois.csv` |",
        f"| fichas sem capitulo que as cite | {len(nunca_citada)} | `mapa-citacao-por-capitulo.csv` |",
        "",
    ]
    if dups:
        rel += ["## DOIs duplicados (cada um e' uma fusao de chaves pendente)", ""]
        rel += [f"- `{d}` → {', '.join(ks)}" for d, ks in sorted(dups.items())]
        rel.append("")
    if sem_pdf:
        rel += ["## Fichas sem PDF e sem justificativa canonica (ADR 0012)", "",
                "Cada uma exige uma das duas: o PDF, ou `canonica: true` com a",
                "justificativa (livro ou obra pre-2010 por definicao consagrada).", ""]
        rel += [f"- {k}" for k in sem_pdf[:50]]
        if len(sem_pdf) > 50:
            rel.append(f"- ... e mais {len(sem_pdf) - 50}")
        rel.append("")

    saida.mkdir(parents=True, exist_ok=True)
    (saida / "RELATORIO.md").write_text("\n".join(rel) + "\n", encoding="utf-8")

    print(f"bib={len(bib)} fichas={len(fichas)} pdfs={len(pdfs)} "
          f"sem_ficha={len(sem_ficha)} sem_pdf={len(sem_pdf)} dois_dup={len(dups)}")
    print(f"[ok] {saida}/RELATORIO.md + 8 CSVs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
