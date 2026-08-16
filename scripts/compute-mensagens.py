#!/usr/bin/env python3
"""Varre coordenacao/ e grava docs/records/mensagens.json para o painel.

Nome de arquivo é a fonte da triagem (protocolo ADR 0008); o front matter só
complementa (acao_esperada, prazo). Locks: estado vivo/vencido pelo timestamp
do último commit que tocou o arquivo (TTL 45 min), nunca pelo YAML.

Uso: python3 scripts/compute-mensagens.py
"""
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAIXA = ROOT / "coordenacao/caixa"
LOCKS = ROOT / "coordenacao/locks"
TTL_MIN = 45

RE_NOME = re.compile(
    r"^(?P<ts>\d{8}-\d{4})_(?P<de>[a-z0-9]+)_(?P<para>[a-z0-9]+)"
    r"_(?P<tipo>aviso|tarefa|pergunta)_(?P<slug>[a-z0-9-]+)"
    r"\.(?P<estado>aberta|em-andamento|concluida)\.md$")


def front_matter(texto: str) -> dict:
    m = re.match(r"---\n(.*?)\n---", texto, re.S)
    fm = {}
    if m:
        for linha in m.group(1).splitlines():
            if ":" in linha:
                k, v = linha.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def idade_horas(ts: str) -> float:
    dt = datetime.strptime(ts, "%Y%m%d-%H%M").replace(tzinfo=timezone.utc)
    return round((datetime.now(timezone.utc) - dt).total_seconds() / 3600, 1)


def ultimo_commit_iso(path: Path) -> str | None:
    r = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cI",
                        "--", str(path.relative_to(ROOT))],
                       capture_output=True, text=True)
    return r.stdout.strip() or None


def main():
    mensagens = []
    fontes = [(CAIXA, False)] + [(d, True) for d in sorted((ROOT / "coordenacao/arquivo").glob("*/"))]
    for pasta, arquivada in fontes:
      for f in sorted(pasta.glob("*.md")):
        m = RE_NOME.match(f.name)
        if not m:
            continue
        fm = front_matter(f.read_text(errors="replace"))
        mensagens.append({
            "arquivo": f.name, **m.groupdict(), "arquivada": arquivada,
            "idade_horas": idade_horas(m.group("ts")),
            "acao_esperada": fm.get("acao_esperada", ""),
            "referencia": fm.get("referencia", ""),
            "prazo": fm.get("prazo") or None,
        })
    locks = []
    agora = datetime.now(timezone.utc)
    for f in sorted(LOCKS.glob("*.md")):
        fm = front_matter(f.read_text(errors="replace"))
        iso = ultimo_commit_iso(f)
        mins = None
        if iso:
            mins = round((agora - datetime.fromisoformat(iso)).total_seconds() / 60)
        locks.append({
            "superficie": f.stem, "dono": fm.get("dono", "?"),
            "renovado_ha_min": mins,
            "vencido": (mins is None) or (mins > TTL_MIN),
        })
    ativas = [x for x in mensagens if x["estado"] != "concluida"]
    bloqueios = [x for x in ativas if x["tipo"] == "tarefa" and "bloque" in x["slug"]]
    saude = {
        "mensagens_ativas": len(ativas),
        "para_autor_abertas": sum(1 for x in ativas
                                  if x["para"] == "autor" and x["estado"] == "aberta"),
        "bloqueio_mais_antigo_h": max((x["idade_horas"] for x in bloqueios), default=0),
        "locks_ativos": sum(1 for l in locks if not l["vencido"]),
        "locks_vencidos": sum(1 for l in locks if l["vencido"]),
    }
    out = ROOT / "docs/records/mensagens.json"
    out.write_text(json.dumps({
        "schema": "mensagens/v1",
        "computado_em": agora.isoformat(timespec="seconds"),
        "ttl_min": TTL_MIN, "mensagens": mensagens, "locks": locks, "saude": saude,
    }, ensure_ascii=False, indent=1) + "\n")
    print(f"ok: {out}  ativas={len(ativas)} locks={len(locks)} "
          f"para_autor={saude['para_autor_abertas']}")


if __name__ == "__main__":
    main()
