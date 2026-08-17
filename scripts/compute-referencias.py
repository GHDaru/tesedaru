#!/usr/bin/env python3
"""Gera docs/records/referencias.json: cada entrada de referencias.bib,
cruzada com onde é citada no livro (ordem real de \\include no principal.tex),
se está fichada (fichamentos/<chave>.md) e se o PDF existe no repositório.

Uso:  python3 scripts/compute-referencias.py

Sem dependências além de PyYAML (já usada por fichamentos/build_kg.py) e da
biblioteca padrão. Nenhum parser de BibTeX/Markdown de terceiros: os dois
são pequenos e específicos o bastante para não justificar uma dependência
nova. Única exceção à regra de "sem rede no build": a resolução da ficha no
Semantic Scholar (pedido do autor, tarefa 20260817-0055/0110) — com cache
persistente em docs/records/s2-cache.json e degradação graciosa total: sem
rede, sem chave de API válida ou com a API fora do ar, o build segue e só
não preenche o link direto do S2 (cai no link de busca, nunca quebra).
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "referencias.bib"
PRINCIPAL_TEX = ROOT / "principal.tex"
FICHAMENTOS_DIR = ROOT / "fichamentos"
PDF_DIR = ROOT / "referencias-pdf"
OUT_PATH = ROOT / "docs/records/referencias.json"
S2_CACHE_PATH = ROOT / "docs/records/s2-cache.json"
S2_API_BASE = "https://api.semanticscholar.org/graph/v1/paper"
S2_MAX_LOOKUPS_PER_RUN = int(__import__("os").environ.get("S2_MAX_LOOKUPS", "50"))
S2_TIMEOUT_S = 6
S2_DELAY_S = 1.05  # API pública sem chave: ~1 req/s é o limite documentado
S2_MAX_CONSECUTIVE_TRANSIENT_FAILURES = 3  # rede fora do ar: desiste cedo, não trava o build


# --------------------------------------------------------------------------
# 1. LaTeX -> texto legível (acentos, escapes comuns) — não é um parser TeX
#    completo, cobre o que este repositório realmente usa.
# --------------------------------------------------------------------------
_ACCENTS = {
    "'": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "y": "ý", "c": "ć", "n": "ń",
          "A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú"},
    "`": {"a": "à", "e": "è", "i": "ì", "o": "ò", "u": "ù", "A": "À"},
    "^": {"a": "â", "e": "ê", "i": "î", "o": "ô", "u": "û", "A": "Â", "E": "Ê", "O": "Ô"},
    '"': {"a": "ä", "e": "ë", "i": "ï", "o": "ö", "u": "ü", "A": "Ä", "O": "Ö", "U": "Ü"},
    "~": {"a": "ã", "o": "õ", "n": "ñ", "A": "Ã", "O": "Õ", "N": "Ñ"},
    "v": {"s": "š", "n": "ň", "c": "č", "z": "ž", "r": "ř", "e": "ě",
          "S": "Š", "N": "Ň", "C": "Č", "Z": "Ž", "R": "Ř"},
    "k": {"a": "ą", "e": "ę", "A": "Ą", "E": "Ę"},
}
# símbolos sem argumento (não combinam com uma letra seguinte)
_BARE_SYMBOLS = {r"\l": "ł", r"\L": "Ł", r"\o": "ø", r"\O": "Ø", r"\aa": "å", r"\AA": "Å"}


def tex_to_text(s: str) -> str:
    if not s:
        return s
    # {\'a} ou \'a ou \'{a}  ->  á  (para cada família de acento conhecida)
    for mark, table in _ACCENTS.items():
        pat = re.compile(r"\{?\\" + re.escape(mark) + r"\s*\{?([a-zA-Z])\}?\}?")
        s = pat.sub(lambda m: table.get(m.group(1), m.group(1)), s)
    # cedilha: \c{c}, \c c ou \c{C} -> ç/Ç (este .bib usa a forma com espaço)
    s = re.sub(r"\{?\\c\s*\{?([a-zA-Z])\}?\}?", lambda m: "ç" if m.group(1) == "c" else "Ç", s)
    # símbolos sem argumento: {\l}owski -> łowski (ordem importa: depois dos
    # acentos combinantes, para não confundir \l com um prefixo de comando)
    for cmd, ch in _BARE_SYMBOLS.items():
        s = s.replace("{" + cmd + "}", ch).replace(cmd + " ", ch + " ").replace(cmd + "}", ch + "}")
    s = s.replace(r"\ss", "ß").replace(r"\&", "&").replace(r"\%", "%")
    s = s.replace("---", "—").replace("--", "–")
    s = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", s)
    s = re.sub(r"\\(?:textit|emph|textbf)\{([^{}]*)\}", r"\1", s)
    s = s.replace("{", "").replace("}", "")
    return s.strip()


# --------------------------------------------------------------------------
# 2. Parser de referencias.bib (brace-balanced, sem dependência externa)
# --------------------------------------------------------------------------
_VENUE_FIELDS = ["journal", "booktitle", "publisher", "school", "institution", "organization"]


def _split_top_level(body: str) -> list[str]:
    """Divide 'campo = {valor}, campo2 = "valor, com vírgula"' respeitando
    chaves aninhadas E aspas duplas — BibTeX aceita os dois delimitadores de
    valor, e uma vírgula dentro de "..." (comum em 'Sobrenome, Nome and
    Sobrenome2, Nome2') não é separador de campo. Ignorar aspas foi um bug
    real: quebrava o campo author em pedaços (achado durante o QA)."""
    parts, depth, start, in_quotes = [], 0, 0, False
    for i, ch in enumerate(body):
        if ch == '"' and depth == 0:
            in_quotes = not in_quotes
        elif in_quotes:
            continue
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(body[start:i])
            start = i + 1
    parts.append(body[start:])
    return [p for p in (p.strip() for p in parts) if p]


def parse_bib(path: Path) -> dict[str, dict]:
    text = path.read_text(encoding="utf-8")
    entries: dict[str, dict] = {}
    for m in re.finditer(r"@(\w+)\s*\{", text):
        open_brace = m.end() - 1
        depth, i = 0, open_brace
        while i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        body = text[open_brace + 1 : i]
        comma = body.find(",")
        if comma == -1:
            continue
        key = body[:comma].strip()
        fields: dict[str, str] = {}
        for part in _split_top_level(body[comma + 1 :]):
            if "=" not in part:
                continue
            fname, fval = part.split("=", 1)
            fname = fname.strip().lower()
            fval = fval.strip().rstrip(",").strip()
            if fval.startswith("{") and fval.endswith("}"):
                fval = fval[1:-1]
            elif fval.startswith('"') and fval.endswith('"'):
                fval = fval[1:-1]
            fields[fname] = tex_to_text(fval)
        venue = next((fields[f] for f in _VENUE_FIELDS if fields.get(f)), "")
        doi = fields.get("doi", "")
        eprint = fields.get("eprint", "")
        url = fields.get("url", "")
        arxiv_id = eprint
        if not arxiv_id and "arxiv.org" in url.lower():
            m_arxiv = re.search(r"arxiv\.org/abs/([\w.]+)", url, re.I)
            arxiv_id = m_arxiv.group(1) if m_arxiv else ""
        link, link_tipo = None, None
        if doi:
            link, link_tipo = f"https://doi.org/{doi}", "doi"
        elif arxiv_id:
            link, link_tipo = f"https://arxiv.org/abs/{arxiv_id}", "arxiv"
        elif url:
            link, link_tipo = url, "url"
        entries[key] = {
            "titulo": fields.get("title", key),
            "autores": _authors(fields.get("author", "")),
            "autores_completos": _authors_full(fields.get("author", "")),
            "ano": fields.get("year", ""),
            "venue": venue,
            "volume": fields.get("volume", ""),
            "numero": fields.get("number", ""),
            "paginas": fields.get("pages", ""),
            "doi": doi,
            "arxiv_id": arxiv_id,
            "link": link,
            "link_tipo": link_tipo,
        }
    return entries


def _authors(raw: str) -> list[str]:
    if not raw:
        return []
    out = []
    for piece in raw.split(" and "):
        piece = piece.strip()
        if not piece or piece.lower() == "others":
            continue
        surname = piece.split(",")[0].strip() if "," in piece else piece.split()[-1]
        out.append(surname)
    return out


def _authors_full(raw: str) -> list[str]:
    """Nome por extenso (não só sobrenome) — usado na ficha básica das
    obras sem fichamento, onde o pedido do autor foi 'autores por extenso'."""
    if not raw:
        return []
    out = []
    for piece in raw.split(" and "):
        piece = piece.strip()
        if not piece or piece.lower() == "others":
            continue
        if "," in piece:
            last, first = piece.split(",", 1)
            out.append(f"{first.strip()} {last.strip()}".strip())
        else:
            out.append(piece)
    return out


# --------------------------------------------------------------------------
# 3. Ordem do livro: \include do principal.tex, na ordem real, e dentro de
#    cada arquivo a citação mais próxima de qual \section/\subsection.
# --------------------------------------------------------------------------
_CITE_RE = re.compile(
    r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|textcite|parencite)[a-zA-Z]*\*?"
    r"(?:\[[^\]]*\])*\{([^}]*)\}"
)
_CHAPTER_RE = re.compile(r"^\\chapter\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", re.MULTILINE)
_SECTION_RE = re.compile(r"^\\(?:sub)?section\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", re.MULTILINE)


def include_order() -> list[Path]:
    text = PRINCIPAL_TEX.read_text(encoding="utf-8")
    order = []
    for m in re.finditer(r"\\include\{([^}]+)\}", text):
        tex = ROOT / f"{m.group(1)}.tex"
        if tex.exists():
            order.append(tex)
    return order


def chapter_label(dirname: str) -> str:
    """'3-metodo' -> 'Cap. 3' · 'a2-ag' -> 'Apêndice A2' · '0-iniciais' -> ''
    (pré-textuais não têm numeração de capítulo e, na prática, não citam)."""
    m = re.match(r"^(\d+)-", dirname)
    if m:
        return f"Cap. {m.group(1)}"
    m = re.match(r"^a(\d+)-", dirname)
    if m:
        return f"Apêndice A{m.group(1)}"
    return ""


def scan_citations() -> dict[str, dict]:
    """chave -> {ocorrencias: [{capitulo, secao}], ordem: (arquivo_idx, linha)}"""
    result: dict[str, dict] = {}
    for file_idx, tex in enumerate(include_order()):
        text = tex.read_text(encoding="utf-8", errors="replace")
        chapter_m = _CHAPTER_RE.search(text)
        titulo_cap = tex_to_text(chapter_m.group(1)) if chapter_m else tex.parent.name
        label = chapter_label(tex.parent.name)
        capitulo = f"{label} — {titulo_cap}" if label else titulo_cap

        # mapa: offset -> título da seção vigente naquele ponto do arquivo
        sections = sorted(
            ((m.start(), tex_to_text(m.group(1))) for m in _SECTION_RE.finditer(text)),
            key=lambda t: t[0],
        )

        def secao_em(offset: int) -> str | None:
            atual = None
            for pos, titulo in sections:
                if pos > offset:
                    break
                atual = titulo
            return atual

        for m in _CITE_RE.finditer(text):
            linha = text.count("\n", 0, m.start()) + 1
            secao = secao_em(m.start())
            for key in m.group(1).split(","):
                key = key.strip()
                if not key:
                    continue
                info = result.setdefault(key, {"ocorrencias": [], "ordem": None})
                ocorrencia = {"capitulo": capitulo, "secao": secao}
                info["ocorrencias"].append(ocorrencia)
                sort_key = (file_idx, linha)
                if info["ordem"] is None or sort_key < info["ordem"]:
                    info["ordem"] = sort_key
    return result


# --------------------------------------------------------------------------
# 4. Fichamentos: status (fichado sim/não) + PDF físico (sim/não) + corpo
#    em HTML (conversor Markdown mínimo, só o que os fichamentos usam:
#    títulos, tabelas, negrito, itálico, código inline, listas, parágrafos).
# --------------------------------------------------------------------------
def parse_front_matter(path: Path) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.index("\n---", 3)
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4 :].lstrip("\n")
    return meta, body


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _inline_md(s: str) -> str:
    s = _esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


_RE_BULLET = re.compile(r"^[-*]\s+")
_RE_NUM = re.compile(r"^\d+\.\s+")


def _is_block_start(s: str) -> bool:
    """Mesma régua usada no despacho E no corte de parágrafo — as duas NUNCA
    podem divergir, senão uma linha como '**negrito** no início' (começa com
    '*' mas não é item de lista, falta o espaço logo depois) faz o loop de
    parágrafo não avançar (achado real: fichamentos/Bengar2022ClassBalanced.md
    travava o build inteiro nisso)."""
    return bool(s) and (s.startswith("#") or s.startswith("|") or bool(_RE_BULLET.match(s)) or bool(_RE_NUM.match(s)))


def markdown_to_html(md: str) -> str:
    lines = md.split("\n")
    html: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        i_antes = i  # trava de segurança: nenhum ramo pode deixar de avançar
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("#"):
            level = min(len(stripped) - len(stripped.lstrip("#")), 6)
            html.append(f"<h{level+1}>{_inline_md(stripped.lstrip('#').strip())}</h{level+1}>")
            i += 1
        elif stripped.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            if len(rows) >= 2 and re.match(r"^:?-+:?$", rows[1][0]):
                rows.pop(1)
            if rows:
                head, *body = rows
                html.append("<table><thead><tr>" +
                             "".join(f"<th>{_inline_md(c)}</th>" for c in head) +
                             "</tr></thead><tbody>" +
                             "".join("<tr>" + "".join(f"<td>{_inline_md(c)}</td>" for c in r) + "</tr>" for r in body) +
                             "</tbody></table>")
        elif _RE_BULLET.match(stripped):
            items = []
            while i < n and _RE_BULLET.match(lines[i].strip()):
                items.append(_RE_BULLET.sub("", lines[i].strip()))
                i += 1
            html.append("<ul>" + "".join(f"<li>{_inline_md(it)}</li>" for it in items) + "</ul>")
        elif _RE_NUM.match(stripped):
            items = []
            while i < n and _RE_NUM.match(lines[i].strip()):
                items.append(_RE_NUM.sub("", lines[i].strip()))
                i += 1
            html.append("<ol>" + "".join(f"<li>{_inline_md(it)}</li>" for it in items) + "</ol>")
        else:
            para = []
            while i < n and lines[i].strip() and not _is_block_start(lines[i].strip()):
                para.append(lines[i].strip())
                i += 1
            html.append(f"<p>{_inline_md(' '.join(para))}</p>")
        if i == i_antes:  # nenhum ramo avançou — não trava o build, pula a linha
            i += 1
    return "\n".join(html)


def load_fichamentos() -> dict[str, dict]:
    out = {}
    for path in sorted(FICHAMENTOS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        parsed = parse_front_matter(path)
        if not parsed:
            continue
        meta, body = parsed
        key = meta.get("id") or path.stem
        pdf_rel = (meta.get("pdf") or "").strip()
        out[key] = {
            "meta": meta,
            "pdf_existe": bool(pdf_rel) and (ROOT / pdf_rel).exists(),
            "detalhes_html": markdown_to_html(body),
        }
    return out


# --------------------------------------------------------------------------
# 5. Link de busca pronta — fallback honesto para quem não tem DOI/arXiv/URL
#    (pedido do autor: nunca um botão/link morto; tarefa 20260817-0055).
# --------------------------------------------------------------------------
def busca_fallback_link(titulo: str, autores: list[str]) -> str:
    partes = [f'"{titulo}"'] if titulo else []
    if autores:
        partes.append(autores[0])
    query = " ".join(partes) or titulo or ""
    return f"https://scholar.google.com/scholar?q={urllib.parse.quote(query)}"


# --------------------------------------------------------------------------
# 6. Ficha básica — gerada dos metadados do bib para obras SEM fichamento,
#    para que o botão "Detalhes" nunca fique morto (tarefa 20260817-0055).
# --------------------------------------------------------------------------
def ficha_basica_html(b: dict | None, autores_completos: list[str], ocorrencias: list[dict], chave: str) -> str:
    b = b or {}
    partes = [
        '<p class="vazia">📄 Ficha básica gerada a partir dos metadados da '
        "bibliografia — esta obra ainda não foi fichada academicamente.</p>",
        f"<p><strong>Título</strong>: {_esc(b.get('titulo') or chave)}</p>",
    ]
    if autores_completos:
        partes.append(f"<p><strong>Autores</strong>: {_esc(', '.join(autores_completos))}</p>")
    if b.get("venue"):
        partes.append(f"<p><strong>Veículo</strong>: {_esc(b['venue'])}</p>")
    if b.get("ano"):
        partes.append(f"<p><strong>Ano</strong>: {_esc(str(b['ano']))}</p>")
    vol_pag = []
    if b.get("volume"):
        vol_pag.append(f"vol. {b['volume']}")
    if b.get("numero"):
        vol_pag.append(f"n. {b['numero']}")
    if b.get("paginas"):
        vol_pag.append(f"p. {b['paginas']}")
    if vol_pag:
        partes.append(f"<p><strong>Volume/Páginas</strong>: {_esc(', '.join(vol_pag))}</p>")
    if b.get("doi"):
        partes.append(f"<p><strong>DOI</strong>: {_esc(b['doi'])}</p>")
    elif b.get("arxiv_id"):
        partes.append(f"<p><strong>arXiv</strong>: {_esc(b['arxiv_id'])}</p>")
    if ocorrencias:
        rotulos: list[str] = []
        for o in ocorrencias:
            rotulo = o["capitulo"] + (f" § {o['secao']}" if o.get("secao") else "")
            if rotulo not in rotulos:
                rotulos.append(rotulo)
        partes.append(f"<p><strong>Citada em</strong>: {_esc('; '.join(rotulos))}</p>")
    else:
        partes.append('<p class="vazia">Não citada no texto da tese.</p>')
    return "\n".join(partes)


# --------------------------------------------------------------------------
# 7. Ficha no Semantic Scholar — resolvida via API pública por DOI/arXiv,
#    com cache persistente (a API tem limite de taxa; cada build só resolve
#    entradas novas, pedido do principal na tarefa 20260817-0110). Falha de
#    rede/timeout NUNCA vira "não encontrado" permanente — só uma resposta
#    real da API (achou ou 404) é definitiva e vai para o cache.
# --------------------------------------------------------------------------
def load_s2_cache() -> dict:
    if S2_CACHE_PATH.exists():
        try:
            data = json.loads(S2_CACHE_PATH.read_text(encoding="utf-8"))
            if isinstance(data.get("resolvidos"), dict):
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return {"schema": "s2-cache/v1", "resolvidos": {}}


def save_s2_cache(cache: dict) -> None:
    S2_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    S2_CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8"
    )


def _s2_fetch(identifier: str) -> tuple[str | None, bool]:
    """Retorna (paper_id, definitivo). definitivo=True só quando a API de
    fato respondeu (achou ou 404) — nesse caso, e só nesse caso, o
    resultado pode ser cacheado para sempre."""
    url = f"{S2_API_BASE}/{identifier}?fields=paperId"
    req = urllib.request.Request(url, headers={"User-Agent": "tesedaru-site-build (github.com/GHDaru/tesedaru)"})
    try:
        with urllib.request.urlopen(req, timeout=S2_TIMEOUT_S) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("paperId"), True
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, True
        return None, False
    except Exception:
        return None, False


def resolve_s2(bib: dict[str, dict]) -> dict[str, dict]:
    cache = load_s2_cache()
    resolvidos = cache["resolvidos"]
    budget = S2_MAX_LOOKUPS_PER_RUN
    consecutive_failures = 0
    changed = False
    for chave, b in bib.items():
        if chave in resolvidos or budget <= 0:
            continue
        doi, arxiv_id = b.get("doi"), b.get("arxiv_id")
        if not (doi or arxiv_id):
            continue
        ident = f"DOI:{doi}" if doi else f"ARXIV:{arxiv_id}"
        paper_id, definitivo = _s2_fetch(ident)
        budget -= 1
        if definitivo:
            consecutive_failures = 0
            changed = True
            resolvidos[chave] = {
                "paper_id": paper_id,
                "metodo": ("doi" if doi else "arxiv") if paper_id else "nao-encontrado",
            }
        else:
            consecutive_failures += 1
            if consecutive_failures >= S2_MAX_CONSECUTIVE_TRANSIENT_FAILURES:
                break  # rede indisponível nesta rodada — tenta de novo no próximo build
        time.sleep(S2_DELAY_S)
    if changed:
        save_s2_cache(cache)
    return resolvidos


# --------------------------------------------------------------------------
# 8. Monta o JSON final
# --------------------------------------------------------------------------
def main() -> None:
    bib = parse_bib(BIB_PATH)
    citacoes = scan_citations()
    fichamentos = load_fichamentos()
    s2_resolvidos = resolve_s2(bib)

    chaves = set(bib) | set(citacoes)
    referencias = []
    for chave in chaves:
        b = bib.get(chave)
        cit = citacoes.get(chave, {"ocorrencias": [], "ordem": None})
        fic = fichamentos.get(chave)
        pdf_existe = fic["pdf_existe"] if fic else (PDF_DIR / f"{chave}.pdf").exists()
        # ocorrencias[0] já é a primeira em ordem de livro: scan_citations()
        # percorre os arquivos na ordem real do \include e, dentro de cada
        # um, da primeira à última linha — a lista nasce ordenada.
        primeira = cit["ocorrencias"][0] if cit["ocorrencias"] else None

        titulo = (b or {}).get("titulo") or (fic["meta"].get("title") if fic else None) or chave
        autores = (b or {}).get("autores") or (fic["meta"].get("authors") if fic else None) or []
        autores_completos = (b or {}).get("autores_completos") or autores

        # link direto (DOI > arXiv > URL); se nenhum, busca pronta — nunca
        # um link morto (tarefa 20260817-0055, pedido literal do autor)
        link = (b or {}).get("link")
        link_tipo = (b or {}).get("link_tipo")
        doi_fic = fic["meta"].get("doi") if fic else ""
        if not link and doi_fic:
            link, link_tipo = f"https://doi.org/{doi_fic}", "doi"
        if not link:
            link, link_tipo = busca_fallback_link(titulo, autores), "busca"

        # ficha no Semantic Scholar: link direto se resolvido, senão busca
        # pronta no próprio site do S2 (tarefa 20260817-0110)
        s2 = s2_resolvidos.get(chave)
        if s2 and s2.get("paper_id"):
            link_s2, link_s2_tipo = f"https://www.semanticscholar.org/paper/{s2['paper_id']}", "direto"
        else:
            link_s2 = f"https://www.semanticscholar.org/search?q={urllib.parse.quote(titulo)}&sort=relevance"
            link_s2_tipo = "busca"

        referencias.append({
            "chave": chave,
            "sort_key": list(cit["ordem"]) if cit["ordem"] else None,
            "titulo": titulo,
            "autores": autores,
            "ano": (b or {}).get("ano") or (fic["meta"].get("year") if fic else None) or "",
            "venue": (b or {}).get("venue") or (fic["meta"].get("venue") if fic else None) or "",
            "link": link,
            "link_tipo": link_tipo,
            "link_s2": link_s2,
            "link_s2_tipo": link_s2_tipo,
            "sem_entrada_bib": b is None,
            "primeira_aparicao": primeira,
            "ocorrencias": cit["ocorrencias"],
            "total_ocorrencias": len(cit["ocorrencias"]),
            "pdf": pdf_existe,
            "fichado": fic is not None,
            "detalhes_html": fic["detalhes_html"] if fic else ficha_basica_html(b, autores_completos, cit["ocorrencias"], chave),
        })

    # ordem do livro: quem foi citado primeiro, na ordem real; não citadas por último
    referencias.sort(key=lambda r: (r["sort_key"] is None, r["sort_key"] or [0, 0], r["chave"]))
    for i, r in enumerate(referencias, start=1):
        r["ordem"] = i if r["sort_key"] is not None else None
        del r["sort_key"]

    out = {
        "schema": "referencias.v1",
        "computado_em": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "total": len(referencias),
        "citadas": sum(1 for r in referencias if r["ordem"] is not None),
        "com_link_direto": sum(1 for r in referencias if r["link_tipo"] != "busca"),
        "com_ficha_s2": sum(1 for r in referencias if r["link_s2_tipo"] == "direto"),
        "referencias": referencias,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ok: {OUT_PATH}  {out['total']} referências ({out['citadas']} citadas · "
          f"{out['com_link_direto']} com link direto · {out['com_ficha_s2']} com ficha S2)")


if __name__ == "__main__":
    sys.exit(main())
