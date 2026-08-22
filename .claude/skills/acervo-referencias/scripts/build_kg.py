#!/usr/bin/env python
"""Estagio 5 — projeta as fichas em grafo: wikilinks, kg.json e kg.ttl.

Dono: agente `local` (skill acervo-referencias).
Uso:  uv run --with pyyaml python build_kg.py --acervo .

A FONTE DE VERDADE e' o front-matter das fichas. Este script so PROJETA.
Corrigir a projecao em vez da ficha cria a segunda verdade que o padrao
(references/padrao-grafo.md) existe para impedir.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from pathlib import Path

import yaml

ARESTAS_PAPER = ["extends", "compares_with", "contradicts", "builds_on"]
ENTIDADES = {
    "proposes": "Method", "uses_methods": "Method", "datasets": "Dataset",
    "metrics": "Metric", "tasks": "Task", "models": "Model",
}
NS = "https://ghdaru.github.io/falco/acervo/"


def ler_front(p: Path) -> tuple[dict, str]:
    txt = p.read_text(encoding="utf-8")
    _, bloco, corpo = txt.split("---", 2)
    return yaml.safe_load(bloco) or {}, corpo


def montar(acervo: Path) -> dict:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    def no(nid: str, tipo: str, **extra) -> None:
        if nid not in nodes:
            nodes[nid] = {"id": nid, "type": tipo, **extra}
        else:
            nodes[nid].update({k: v for k, v in extra.items() if v})

    for ficha in sorted((acervo / "fichas").glob("*.md")):
        if ficha.stem.startswith("_"):
            continue
        front, corpo = ler_front(ficha)
        k = ficha.stem
        no(k, "Paper",
           title=front.get("title") or "",
           year=front.get("year"),
           venue=front.get("venue"),
           doi=front.get("doi"),
           pdf=front.get("pdf"),
           paper_type=front.get("paper_type"),
           canonica=bool(front.get("canonica")),
           cited_in=front.get("cited_in") or [])

        for campo in ARESTAS_PAPER:
            for alvo in front.get(campo) or []:
                if isinstance(alvo, dict):
                    alvo_id, nota = alvo.get("target"), alvo.get("note", "")
                else:
                    alvo_id, nota = alvo, ""
                edges.append({"from": k, "to": alvo_id, "type": campo, "note": nota})

        for campo, tipo in ENTIDADES.items():
            for termo in front.get(campo) or []:
                no(str(termo), tipo)
                edges.append({"from": k, "to": str(termo), "type": campo})

        for rel in front.get("falco_relation") or []:
            alvo = rel.get("target")
            if alvo:
                no(alvo, "ThesisNode")
                edges.append({"from": k, "to": alvo,
                              "type": f"falco:{rel.get('type')}",
                              "note": rel.get("note", "")})

        # claims da tabela viram nos com evidencia localizavel
        m = re.search(r"^##\s+Claims.*?$(.*?)(?=^##\s|\Z)", corpo, re.S | re.M)
        if m:
            for ln in m.group(1).splitlines():
                cels = [c.strip() for c in ln.strip().strip("|").split("|")]
                if len(cels) >= 3 and re.fullmatch(r"C\d+", cels[0]) and cels[1]:
                    cid = f"{k}#{cels[0]}"
                    no(cid, "Claim", text=cels[1], evidence=cels[2])
                    edges.append({"from": k, "to": cid, "type": "asserts"})

    return {"nodes": list(nodes.values()), "edges": edges}


def secao_relacoes(kg: dict, acervo: Path) -> None:
    """Reescreve a secao '## Relacoes' de cada ficha com wikilinks Obsidian."""
    por_origem: dict[str, list[dict]] = {}
    for e in kg["edges"]:
        if e["type"] in ARESTAS_PAPER or e["type"].startswith("falco:"):
            por_origem.setdefault(e["from"], []).append(e)

    for ficha in sorted((acervo / "fichas").glob("*.md")):
        k = ficha.stem
        txt = ficha.read_text(encoding="utf-8")
        linhas = ["## Relações",
                  "<!-- GERADO pelo build_kg.py — nao editar; a fonte e' o YAML acima. -->"]
        for e in por_origem.get(k, []):
            nota = f" — {e['note']}" if e.get("note") else ""
            linhas.append(f"- `{e['type']}` [[{e['to']}]]{nota}")
        if len(linhas) == 2:
            linhas.append("- *(sem relações declaradas)*")
        nova = "\n".join(linhas) + "\n"
        if re.search(r"^##\s+Relações", txt, re.M):
            txt = re.sub(r"^##\s+Relações.*?(?=^##\s|\Z)", nova, txt, flags=re.S | re.M)
        else:
            txt = txt.rstrip() + "\n\n" + nova
        ficha.write_text(txt, encoding="utf-8")


def escrever_ttl(kg: dict, destino: Path) -> None:
    """RDF em Turtle. Os IRIs de CiTO estao MARCADOS como pendentes de
    conferencia contra a especificacao — ver references/padrao-grafo.md."""
    def iri(s: str) -> str:
        return f"<{NS}{re.sub(r'[^A-Za-z0-9_#.-]', '_', s)}>"

    linhas = [
        "@prefix falco: <%s> ." % NS,
        "@prefix schema: <https://schema.org/> .",
        "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
        "",
        "# ATENCAO: o mapeamento para CiTO ainda NAO foi conferido IRI a IRI",
        "# contra a especificacao oficial. Ate la, as arestas paper->paper saem",
        "# no namespace falco:. Ver references/padrao-grafo.md.",
        "",
    ]
    for n in kg["nodes"]:
        if n["type"] == "Paper":
            linhas.append(f"{iri(n['id'])} a schema:ScholarlyArticle ;")
            linhas.append(f'    schema:name "{(n.get("title") or "").replace(chr(34), "")}" ;')
            if n.get("year"):
                linhas.append(f'    schema:datePublished "{n["year"]}" ;')
            if n.get("doi"):
                linhas.append(f'    schema:identifier "{n["doi"]}" ;')
            linhas[-1] = linhas[-1].rstrip(" ;") + " ."
        elif n["type"] in ("Method", "Dataset", "Metric", "Task", "Model"):
            linhas.append(f'{iri(n["id"])} a skos:Concept ; skos:prefLabel "{n["id"]}" .')
    linhas.append("")
    for e in kg["edges"]:
        pred = e["type"].replace("falco:", "")
        linhas.append(f"{iri(e['from'])} falco:{pred} {iri(e['to'])} .")
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--acervo", type=Path,
                    default=Path(os.environ.get("ACERVO", ".")))
    ap.add_argument("--sem-wikilinks", action="store_true",
                    help="nao reescreve a secao '## Relacoes' das fichas")
    a = ap.parse_args()

    kg = montar(a.acervo)
    saida = a.acervo / "grafo"
    saida.mkdir(parents=True, exist_ok=True)
    (saida / "kg.json").write_text(
        json.dumps(kg, ensure_ascii=False, indent=2), encoding="utf-8")
    escrever_ttl(kg, saida / "kg.ttl")
    if not a.sem_wikilinks:
        secao_relacoes(kg, a.acervo)

    tipos = Counter(n["type"] for n in kg["nodes"])
    arestas = Counter(e["type"] for e in kg["edges"])
    ids = {n["id"] for n in kg["nodes"]}
    orfas = [e for e in kg["edges"] if e["to"] not in ids]

    print(f"nos: {len(kg['nodes'])}  " + " ".join(f"{t}={c}" for t, c in tipos.most_common()))
    print(f"arestas: {len(kg['edges'])}  " + " ".join(f"{t}={c}" for t, c in arestas.most_common()))
    if orfas:
        print(f"[ATENCAO] {len(orfas)} aresta(s) orfa(s) — o portao 5 vai reprovar:")
        for e in orfas[:10]:
            print(f"  {e['from']} -{e['type']}-> {e['to']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
