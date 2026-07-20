"""Gera o Knowledge Graph dos fichamentos a partir do front-matter YAML.

Saídas (na pasta fichamentos/):
- kg.json : nós + arestas tipadas (consumível por Neo4j/vis.js/etc.)
- kg.html : visualização autocontida (abre em qualquer navegador, sem internet)

Uso:  uv run --with pyyaml python fichamentos/build_kg.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent

# Arestas artigo→artigo e artigo→FALCO extraídas do front-matter
PAPER_RELATIONS = ["extends", "compares_with", "contradicts", "builds_on"]
# Atributos que viram nós-conceito ligados ao artigo
CONCEPT_FIELDS = {
    "pillars": "pilar",
    "proposes": "conceito",
    "uses_methods": "metodo",
    "models": "modelo",
    "datasets": "dataset",
    "tasks": "tarefa",
}


def parse_front_matter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.index("\n---", 3)
    return yaml.safe_load(text[3:end])


# Diretórios de capítulo da tese -> nome legível (para "citado na tese em ...")
CHAPTER_NAMES = {
    "1-intro": "Cap. 1 — Introdução",
    "2-fundam": "Cap. 2 — Fundamentação",
    "3-metodo": "Cap. 3 — Metodologia",
    "4-resultados-l0": "Cap. 4 — Resultados (L0)",
    "5-resultados-falco": "Cap. 5 — Resultados (FALCO)",
    "6-conclusao": "Cap. 6 — Conclusão",
}
_CITE_RE = re.compile(
    r"\\(?:cite|citep|citet|citeauthor|citeyear|textcite|parencite)[a-zA-Z]*\*?"
    r"(?:\[[^\]]*\])*\{([^}]*)\}"
)


def _citations_by_key() -> dict[str, list[str]]:
    """Mapeia chave BibTeX -> capítulos da tese que a citam."""
    root = HERE.parent
    cited: dict[str, set[str]] = {}
    for chdir, label in CHAPTER_NAMES.items():
        for tex in (root / chdir).glob("*.tex"):
            for m in _CITE_RE.finditer(tex.read_text(encoding="utf-8", errors="replace")):
                for key in m.group(1).split(","):
                    cited.setdefault(key.strip(), set()).add(label)
    return {k: sorted(v, key=lambda s: list(CHAPTER_NAMES.values()).index(s))
            for k, v in cited.items()}


def build() -> dict:
    nodes: dict[str, dict] = {
        "FALCO": {"id": "FALCO", "type": "framework", "label": "FALCO"}
    }
    edges: list[dict] = []
    cited_in = _citations_by_key()

    for path in sorted(HERE.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = parse_front_matter(path)
        if not meta or "id" not in meta:
            continue
        pid = meta["id"]
        doi = (meta.get("doi") or "").strip()
        nodes[pid] = {
            "id": pid,
            "type": "artigo",
            "label": pid,
            "title": meta.get("title", ""),
            "year": meta.get("year"),
            "venue": meta.get("venue", ""),
            "paper_type": meta.get("paper_type", ""),
            "status": meta.get("status", ""),
            "pdf": (meta.get("pdf") or "").strip(),
            "doi": doi,
            "url": f"https://doi.org/{doi}" if doi else "",
            "cited_in": cited_in.get(pid, []),
        }
        for relation in PAPER_RELATIONS:
            for target in meta.get(relation) or []:
                edges.append({"source": pid, "target": str(target), "type": relation})
        for field, node_type in CONCEPT_FIELDS.items():
            for value in meta.get(field) or []:
                cid = f"{node_type}:{value}"
                nodes.setdefault(
                    cid, {"id": cid, "type": node_type, "label": str(value)}
                )
                edges.append({"source": pid, "target": cid, "type": field})
        for rel in meta.get("falco_relation") or []:
            edges.append(
                {
                    "source": pid,
                    "target": str(rel.get("target", "FALCO")),
                    "type": rel.get("type", "relaciona"),
                    "note": rel.get("note", ""),
                }
            )

    # Alvos ainda não declarados como nó:
    #  - se vieram de uma relação artigo→artigo (PAPER_RELATIONS), são artigos
    #    ainda não fichados → "artigo-pendente";
    #  - se vieram de falco_relation, são entidades internas do FALCO (fases,
    #    experimentos, algoritmos, afirmações, temas) → "tema-falco".
    paper_targets = {e["target"] for e in edges if e["type"] in PAPER_RELATIONS}
    for edge in edges:
        if edge["target"] not in nodes:
            is_paper = edge["target"] in paper_targets
            nodes[edge["target"]] = {
                "id": edge["target"],
                "type": "artigo-pendente" if is_paper else "tema-falco",
                "label": edge["target"],
            }
    return {"nodes": list(nodes.values()), "edges": edges}


def render_html(graph: dict) -> str:
    template = (HERE / "kg_template.html").read_text(encoding="utf-8")
    return template.replace("/*__GRAPH_JSON__*/", json.dumps(graph, ensure_ascii=False))


if __name__ == "__main__":
    graph = build()
    (HERE / "kg.json").write_text(
        json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (HERE / "kg.html").write_text(render_html(graph), encoding="utf-8")
    print(
        f"kg.json/kg.html: {len(graph['nodes'])} nós, {len(graph['edges'])} arestas"
    )
