#!/usr/bin/env python
"""Estagio 1 — converte um PDF inteiro em markdown, com as figuras exportadas.

Dono: agente `local` (skill acervo-referencias).
Uso:  uv run --with pymupdf python pdf2md.py --pdf pdf/Chave.pdf --chave Chave --acervo .

O script NAO descreve figura: exporta a imagem e deixa o marcador
`DESCRICAO PENDENTE`, que o agente substitui olhando o PNG. O portao 1 falha
enquanto sobrar marcador — e essa falha e' o ponto, nao um incomodo.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

try:
    import pymupdf as fitz          # nome novo (>=1.24)
except ImportError:  # pragma: no cover
    import fitz                       # nome antigo, ainda em uso

MARCADOR = "DESCRICAO PENDENTE"
MIN_AREA = 10_000       # px^2: abaixo disto e' ornamento/icone, nao figura
MIN_LADO = 80           # px: descarta filetes e linhas


def desifenar(texto: str) -> str:
    """Junta palavra quebrada por hifen no fim da linha: 'aprendiza-\\ndo'."""
    return re.sub(r"(\w)-\n(\w)", r"\1\2", texto)


def limpar(texto: str) -> str:
    texto = desifenar(texto)
    texto = re.sub(r"[ \t]+\n", "\n", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def tabelas_da_pagina(pagina) -> list[str]:
    """Tabelas detectadas, em markdown. Falha silenciosa: nem todo PDF tem
    estrutura de tabela recuperavel, e forcar produz lixo pior que a ausencia."""
    saida: list[str] = []
    try:
        achadas = pagina.find_tables()
    except Exception:
        return saida
    for i, tab in enumerate(getattr(achadas, "tables", []), start=1):
        try:
            linhas = tab.extract()
        except Exception:
            continue
        if not linhas or len(linhas) < 2:
            continue
        def celula(c):
            return (c or "").replace("\n", " ").replace("|", "\\|").strip()
        cab = [celula(c) for c in linhas[0]]
        corpo = ["| " + " | ".join(celula(c) for c in ln) + " |" for ln in linhas[1:]]
        saida.append(
            f"<!-- TAB-{i:02d} (p.{pagina.number + 1}) -->\n"
            + "| " + " | ".join(cab) + " |\n"
            + "|" + "---|" * len(cab) + "\n"
            + "\n".join(corpo)
        )
    return saida


def exportar_figuras(doc, pagina, dir_fig: Path, chave: str) -> list[str]:
    """Exporta as imagens da pagina e devolve os blocos markdown com marcador."""
    blocos: list[str] = []
    n = pagina.number + 1
    for i, info in enumerate(pagina.get_images(full=True), start=1):
        xref = info[0]
        try:
            pix = fitz.Pixmap(doc, xref)
        except Exception:
            continue
        if pix.width < MIN_LADO or pix.height < MIN_LADO:
            continue
        if pix.width * pix.height < MIN_AREA:
            continue
        if pix.n - pix.alpha >= 4:          # CMYK nao grava em PNG direto
            pix = fitz.Pixmap(fitz.csRGB, pix)
        nome = f"p{n:02d}-fig{i:02d}.png"
        dir_fig.mkdir(parents=True, exist_ok=True)
        pix.save(dir_fig / nome)
        blocos.append(
            f"![](figuras/{chave}/{nome})\n"
            f"> **FIG-{n:02d}{i:02d} (p.{n})** — {MARCADOR}"
        )
    return blocos


def converter(pdf: Path, chave: str, acervo: Path) -> Path:
    doc = fitz.open(pdf)
    dir_doc = acervo / "documentos"
    dir_fig = dir_doc / "figuras" / chave
    partes: list[str] = []
    total_chars = 0

    for pagina in doc:
        n = pagina.number + 1
        texto = limpar(pagina.get_text("text"))
        total_chars += len(texto)
        partes.append(f"<!-- p.{n} -->")
        if texto:
            partes.append(texto)
        for tab in tabelas_da_pagina(pagina):
            partes.append(tab)
        for fig in exportar_figuras(doc, pagina, dir_fig, chave):
            partes.append(fig)

    npag = doc.page_count
    doc.close()

    frente = (
        "---\n"
        f"chave: {chave}\n"
        f"pdf: pdf/{chave}.pdf\n"
        f"paginas: {npag}\n"
        f"caracteres: {total_chars}\n"
        f"convertido_em: {_dt.date.today().isoformat()}\n"
        f"conversor: pdf2md.py v1 (pymupdf {getattr(fitz, 'VersionBind', '?')})\n"
        "---\n"
    )
    dir_doc.mkdir(parents=True, exist_ok=True)
    destino = dir_doc / f"{chave}.md"
    destino.write_text(frente + "\n" + "\n\n".join(partes) + "\n", encoding="utf-8")

    por_pag = total_chars / max(npag, 1)
    print(f"[ok] {destino}  {npag} paginas  {total_chars} chars  ({por_pag:.0f}/pag)")
    if por_pag < 200:
        print(
            "[ATENCAO] densidade de texto baixa: provavel PDF so-imagem. "
            "Veja references/conversao-pdf.md, secao 'PDF que e' so imagem'.",
            file=sys.stderr,
        )
    pendentes = (frente + "\n".join(partes)).count(MARCADOR)
    if pendentes:
        print(f"[proximo passo] {pendentes} figura(s) a descrever — abra os PNGs "
              f"em documentos/figuras/{chave}/ e substitua '{MARCADOR}'.")
    return destino


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf", required=True, type=Path)
    ap.add_argument("--chave", required=True)
    ap.add_argument("--acervo", required=True, type=Path)
    a = ap.parse_args()
    if not a.pdf.exists():
        print(f"[erro] PDF inexistente: {a.pdf}", file=sys.stderr)
        return 2
    converter(a.pdf, a.chave, a.acervo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
