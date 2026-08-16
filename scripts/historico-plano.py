#!/usr/bin/env python3
"""Extrai a série temporal do plano de revisão a partir do histórico git.

Cada commit que tocou docs/records/plano-revisao.json é um snapshot datado.
Emite JSON em stdout: [{data, commit, contagens por status da matriz,
contagens dos artefatos}] — insumo da série de evolução do dashboard.
Requer clone com histórico (fetch-depth: 0 no CI).
"""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = "docs/records/plano-revisao.json"


def snapshots():
    log = subprocess.run(
        ["git", "-C", str(ROOT), "log", "--follow", "--format=%H %cI", "--", REL],
        capture_output=True, text=True, check=True).stdout.split()
    pares = list(zip(log[::2], log[1::2]))  # (hash, data ISO), mais novo primeiro
    out = []
    for h, data in reversed(pares):
        try:
            raw = subprocess.run(["git", "-C", str(ROOT), "show", f"{h}:{REL}"],
                                 capture_output=True, text=True, check=True).stdout
            d = json.loads(raw)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            continue
        matriz = Counter()
        for c in d.get("capitulos", []):
            for cell in c.get("rodadas", {}).values():
                matriz[cell.get("status", "pendente")] += 1
        itens = Counter()
        for g in d.get("artefatos", []):
            for i in g.get("itens", []):
                itens[i.get("status", "pendente")] += 1
        out.append({
            "data": data[:10], "commit": h[:7], "versao": d.get("versao"),
            "matriz": dict(matriz), "artefatos": dict(itens),
        })
    return out


if __name__ == "__main__":
    json.dump(snapshots(), sys.stdout, ensure_ascii=False, indent=1)
    print()
