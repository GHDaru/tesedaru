#!/usr/bin/env python
"""Portoes 1..5 do pipeline do acervo. Exit 0 = pode seguir; 1 = lista o que falta.

Dono: agente `local` (skill acervo-referencias).
Uso:  uv run --with pymupdf --with pyyaml python gate.py <estagio> [Chave]
      gate.py 1 Xiao2023FreeAL     # portoes 1..4 sao por chave
      gate.py 5                    # portao 5 e' do acervo inteiro

Existe porque criterio de aceite julgado por leitura vira teatro. Aqui e'
grep, contagem e parse: a maquina reprova sem negociar.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

MARCADOR = "DESCRICAO PENDENTE"
OBRIG_ID = ["id", "title", "authors", "year", "pdf", "paginas"]
ENTIDADES = ["proposes", "uses_methods", "datasets", "metrics", "tasks", "models"]
TIPOS_FALCO = {"compara", "fundamenta", "motiva", "ameaca", "complementa"}


class Falhas(list):
    def erro(self, msg: str) -> None:
        self.append(msg)


def ler_front(caminho: Path) -> tuple[dict, str]:
    txt = caminho.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        raise ValueError("arquivo sem front-matter YAML")
    _, bloco, corpo = txt.split("---", 2)
    return yaml.safe_load(bloco) or {}, corpo


def termos_canonicos(acervo: Path) -> set[str]:
    voc = acervo / "vocabulario" / "_VOCABULARIO.md"
    if not voc.exists():
        return set()
    texto = re.sub(r"<!--.*?-->", " ", voc.read_text(encoding="utf-8"), flags=re.S)
    termos: set[str] = set()
    for linha in texto.splitlines():
        if linha.startswith(("#", "|", ">")):
            continue
        for t in re.split(r"[,\s]+", linha):
            t = t.strip().strip(".")
            if t and re.fullmatch(r"[A-Za-z0-9][\w\-\.]*", t):
                termos.add(t)
    return termos


def chaves_bib(acervo: Path) -> dict[str, str]:
    """chave -> doi (minusculo, vazio se nao houver)."""
    bib = acervo / "referencias.bib"
    if not bib.exists():
        return {}
    texto = bib.read_text(encoding="utf-8", errors="replace")
    saida: dict[str, str] = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", texto, re.S):
        chave, corpo = m.group(1), m.group(2)
        doi = re.search(r"doi\s*=\s*[{\"]([^}\"]+)", corpo, re.I)
        saida[chave] = doi.group(1).strip().lower() if doi else ""
    return saida


# ---------------------------------------------------------------- portao 1
def portao1(acervo: Path, chave: str, f: Falhas) -> None:
    doc = acervo / "documentos" / f"{chave}.md"
    if not doc.exists():
        f.erro(f"documentos/{chave}.md nao existe — rode o pdf2md.py")
        return
    front, corpo = ler_front(doc)
    texto = doc.read_text(encoding="utf-8")

    pend = texto.count(MARCADOR)
    if pend:
        f.erro(f"{pend} figura(s) com '{MARCADOR}' — descreva olhando os PNGs")

    marcas = len(re.findall(r"<!-- p\.\d+ -->", texto))
    declaradas = int(front.get("paginas") or 0)
    if declaradas and marcas != declaradas:
        f.erro(f"marcas de pagina ({marcas}) != paginas do PDF ({declaradas})")

    try:
        try:
            import pymupdf as fitz
        except ImportError:
            import fitz
        pdf = acervo / "pdf" / f"{chave}.pdf"
        if pdf.exists():
            with fitz.open(pdf) as d:
                if d.page_count != declaradas:
                    f.erro(f"front-matter diz {declaradas} paginas; o PDF tem "
                           f"{d.page_count}")
    except ImportError:
        pass

    dir_fig = acervo / "documentos" / "figuras" / chave
    if dir_fig.exists():
        for png in sorted(dir_fig.glob("*.png")):
            if png.name not in texto:
                f.erro(f"figura exportada nao referenciada no .md: {png.name}")

    chars = int(front.get("caracteres") or 0)
    if declaradas and chars / declaradas < 200:
        f.erro(f"densidade de texto {chars/declaradas:.0f} char/pag — provavel "
               "PDF so-imagem; veja references/conversao-pdf.md")


# ---------------------------------------------------------------- portao 2
def portao2(acervo: Path, chave: str, f: Falhas) -> None:
    ficha = acervo / "fichas" / f"{chave}.md"
    if not ficha.exists():
        f.erro(f"fichas/{chave}.md nao existe")
        return
    try:
        front, _ = ler_front(ficha)
    except Exception as e:
        f.erro(f"front-matter nao parseia: {e}")
        return

    if front.get("id") != chave:
        f.erro(f"id '{front.get('id')}' != nome do arquivo '{chave}'")
    for campo in OBRIG_ID:
        v = front.get(campo)
        if v in (None, "", [], 0) and campo != "doi":
            f.erro(f"campo obrigatorio vazio: {campo}")

    fonte = front.get("_fonte") or {}
    for campo in ("title", "authors", "year"):
        if front.get(campo) and not fonte.get(campo):
            f.erro(f"_fonte.{campo} ausente — todo metadado declara de que pagina veio")

    autores = front.get("authors") or []
    if any("et al" in str(a).lower() for a in autores):
        f.erro("authors contem 'et al.' — liste todos os autores")

    pdf_rel = front.get("pdf") or ""
    if pdf_rel and not (acervo / pdf_rel).exists():
        f.erro(f"pdf: aponta para arquivo inexistente: {pdf_rel}")

    bib = chaves_bib(acervo)
    if bib and chave not in bib:
        f.erro(f"chave '{chave}' ausente do referencias.bib do acervo")

    doi = (front.get("doi") or "").strip().lower()
    if doi.startswith("http"):
        f.erro("doi deve ser so o sufixo 10.xxxx/..., sem URL")
    if doi:
        for outra, d in bib.items():
            if outra != chave and d and d == doi:
                f.erro(f"DOI duplicado: mesma obra tambem em '{outra}' — funda as chaves")

    canon = termos_canonicos(acervo)
    if canon:
        for campo in ENTIDADES:
            for termo in front.get(campo) or []:
                if str(termo) not in canon:
                    f.erro(f"{campo}: '{termo}' fora do vocabulario controlado")


# ---------------------------------------------------------------- portao 3
def _secao(corpo: str, titulo_re: str) -> str:
    m = re.search(rf"^##\s+{titulo_re}.*?$(.*?)(?=^##\s|\Z)", corpo,
                  re.S | re.M | re.I)
    return m.group(1) if m else ""


def _ngramas(texto: str, n: int = 8) -> set[tuple[str, ...]]:
    pal = re.findall(r"\w+", texto.lower())
    return {tuple(pal[i:i + n]) for i in range(max(len(pal) - n + 1, 0))}


def portao3(acervo: Path, chave: str, f: Falhas) -> None:
    ficha = acervo / "fichas" / f"{chave}.md"
    if not ficha.exists():
        f.erro(f"fichas/{chave}.md nao existe")
        return
    _, corpo = ler_front(ficha)

    resumo = _secao(corpo, r"Resumo")
    linhas = [ln for ln in resumo.splitlines()
              if ln.strip() and not ln.strip().startswith("<!--")]
    if not (5 <= len(linhas) <= 8):
        f.erro(f"resumo com {len(linhas)} linhas — o pedido e' 5 a 8")

    doc = acervo / "documentos" / f"{chave}.md"
    if resumo.strip() and doc.exists():
        cabeca = doc.read_text(encoding="utf-8")[:6000]
        a, b = _ngramas(resumo), _ngramas(cabeca)
        if a and len(a & b) / len(a) > 0.30:
            f.erro("resumo sobrepoe >30% de 8-gramas com a 1a pagina do artigo "
                   "— parece copiado do abstract; reescreva com suas palavras")

    for titulo, col, nome in (
        (r"Claims", 3, "evidencia"),
        (r"N[uú]meros", 3, "condicoes"),
    ):
        for ln in _secao(corpo, titulo).splitlines():
            ln = ln.strip()
            if not ln.startswith("|") or re.fullmatch(r"\|[\s\-\|]+\|", ln):
                continue
            cels = [c.strip() for c in ln.strip("|").split("|")]
            if len(cels) < col or cels[0].lower() in ("#", "valor", "claim"):
                continue
            if not cels[0]:
                continue
            if not cels[col - 1]:
                f.erro(f"secao {nome}: linha '{cels[0][:40]}' sem {nome} preenchida")


# ---------------------------------------------------------------- portao 4
def portao4(acervo: Path, chave: str, f: Falhas) -> None:
    ficha = acervo / "fichas" / f"{chave}.md"
    front, corpo = ler_front(ficha)

    rels = front.get("falco_relation") or []
    if not rels:
        f.erro("falco_relation vazia — se o artigo nao toca a tese, declare isso "
               "explicitamente em vez de deixar em branco")
    alvos_validos = set()
    nos = acervo / "_insumos" / "tese" / "nos.txt"
    if nos.exists():
        alvos_validos = {l.strip() for l in nos.read_text(encoding="utf-8").splitlines()
                         if l.strip()}
    for r in rels:
        if (r.get("type") or "") not in TIPOS_FALCO:
            f.erro(f"falco_relation.type invalido: {r.get('type')}")
        alvo = r.get("target") or ""
        if not alvo:
            f.erro("falco_relation sem target")
        elif alvos_validos and alvo not in alvos_validos:
            f.erro(f"falco_relation.target '{alvo}' nao esta em _insumos/tese/nos.txt")

    sumario = acervo / "_insumos" / "tese" / "sumario.txt"
    if sumario.exists():
        secoes = sumario.read_text(encoding="utf-8")
        for ln in _secao(corpo, r"Claims").splitlines():
            cels = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cels) >= 4 and cels[0] and cels[0] != "#" and cels[3]:
                alvo = cels[3].split()[0]
                if alvo and alvo not in secoes:
                    f.erro(f"'Uso na tese' aponta para '{cels[3]}', ausente do sumario")


# ---------------------------------------------------------------- portao 5
def portao5(acervo: Path, f: Falhas) -> None:
    fichas = sorted((acervo / "fichas").glob("*.md"))
    if not fichas:
        f.erro("nenhuma ficha em fichas/")
        return
    chaves = {p.stem for p in fichas}
    dois: dict[str, str] = {}

    for p in fichas:
        try:
            front, _ = ler_front(p)
        except Exception as e:
            f.erro(f"{p.name}: front-matter nao parseia ({e})")
            continue
        k = p.stem
        for campo in ("extends", "compares_with", "contradicts", "builds_on"):
            for alvo in front.get(campo) or []:
                alvo_k = alvo.get("target") if isinstance(alvo, dict) else alvo
                if alvo_k not in chaves:
                    f.erro(f"{k}.{campo}: aresta orfa para '{alvo_k}' (sem ficha)")
        doi = (front.get("doi") or "").strip().lower()
        if doi:
            if doi in dois:
                f.erro(f"DOI repetido em '{k}' e '{dois[doi]}'")
            dois[doi] = k
        if not front.get("canonica"):
            pdf_rel = front.get("pdf") or ""
            if not pdf_rel or not (acervo / pdf_rel).exists():
                f.erro(f"{k}: sem PDF e sem canonica:true (ADR 0012) — declare um dos dois")

    pdfs = {q.stem for q in (acervo / "pdf").glob("*.pdf")}
    sem_ficha = sorted(pdfs - chaves)
    if sem_ficha:
        f.erro(f"{len(sem_ficha)} PDF(s) no acervo sem ficha — o grafo fecharia "
               f"com o acervo pela metade (ex.: {sem_ficha[:3]})")

    kg = acervo / "grafo" / "kg.json"
    if not kg.exists():
        f.erro("grafo/kg.json ausente — rode o build_kg.py")
    else:
        dados = json.loads(kg.read_text(encoding="utf-8"))
        papers = {n["id"] for n in dados.get("nodes", []) if n.get("type") == "Paper"}
        faltando = chaves - papers
        if faltando:
            f.erro(f"grafo desatualizado: {len(faltando)} ficha(s) fora do kg.json "
                   f"(ex.: {sorted(faltando)[:3]}) — regenere")


PORTOES = {1: portao1, 2: portao2, 3: portao3, 4: portao4}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("estagio", type=int, choices=[1, 2, 3, 4, 5])
    ap.add_argument("chave", nargs="?")
    ap.add_argument("--acervo", type=Path,
                    default=Path(os.environ.get("ACERVO", ".")))
    a = ap.parse_args()

    f = Falhas()
    if a.estagio == 5:
        portao5(a.acervo, f)
        rotulo = "acervo"
    else:
        if not a.chave:
            print("[erro] portoes 1..4 exigem a chave", file=sys.stderr)
            return 2
        PORTOES[a.estagio](a.acervo, a.chave, f)
        rotulo = a.chave

    if f:
        print(f"PORTAO {a.estagio} REPROVADO — {rotulo} ({len(f)} problema(s)):")
        for m in f:
            print(f"  - {m}")
        return 1
    print(f"PORTAO {a.estagio} ok — {rotulo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
