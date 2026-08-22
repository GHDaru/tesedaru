#!/usr/bin/env python
"""Estado do pipeline por chave — o que permite parar e retomar sem refazer.

Dono: agente `local` (skill acervo-referencias).
Uso:
    estado.py proximo                 # proxima chave pendente e em que estagio
    estado.py marcar <Chave> <1-5> ok # registra estagio concluido
    estado.py marcar <Chave> 4 pulado --motivo "insumo da tese ausente"
    estado.py painel                  # quantas chaves em cada estagio

Formato: `_estado/pipeline.jsonl`, append-only. Uma linha por evento, nunca
sobrescrita — o historico de quem processou o que fica junto com o estado.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import sys
from pathlib import Path

ESTAGIOS = {1: "converter", 2: "metadados", 3: "resumo", 4: "citacoes", 5: "grafo"}
POR_ARTIGO = [1, 2, 3, 4]


def caminho(acervo: Path) -> Path:
    p = acervo / "_estado" / "pipeline.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def eventos(acervo: Path) -> list[dict]:
    p = caminho(acervo)
    if not p.exists():
        return []
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln:
            try:
                out.append(json.loads(ln))
            except json.JSONDecodeError:
                print(f"[aviso] linha ilegivel no estado, ignorada: {ln[:60]}",
                      file=sys.stderr)
    return out


def concluidos(acervo: Path) -> dict[str, set[int]]:
    """chave -> conjunto de estagios com resultado ok/pulado."""
    mapa: dict[str, set[int]] = {}
    for e in eventos(acervo):
        if e.get("resultado") in ("ok", "pulado"):
            mapa.setdefault(e["chave"], set()).add(int(e["estagio"]))
    return mapa


def chaves_do_acervo(acervo: Path) -> list[str]:
    """Fila = PDFs em _entrada/ (ainda sem chave) + PDFs ja em pdf/."""
    return sorted({p.stem for p in (acervo / "pdf").glob("*.pdf")})


def cmd_proximo(acervo: Path) -> int:
    feito = concluidos(acervo)
    for chave in chaves_do_acervo(acervo):
        for est in POR_ARTIGO:
            if est not in feito.get(chave, set()):
                print(f"{chave}\t{est}\t{ESTAGIOS[est]}")
                return 0
    entrada = sorted((acervo / "_entrada").glob("*.pdf"))
    if entrada:
        print(f"[_entrada] {len(entrada)} PDF(s) sem chave BibTeX ainda — "
              f"proximo: {entrada[0].name}")
        return 0
    print("nada pendente nos estagios 1-4; o estagio 5 (grafo) pode rodar")
    return 0


def cmd_marcar(acervo: Path, chave: str, estagio: int, resultado: str,
               motivo: str | None) -> int:
    if resultado not in ("ok", "pulado", "falhou"):
        print("[erro] resultado deve ser ok | pulado | falhou", file=sys.stderr)
        return 2
    if resultado == "pulado" and not motivo:
        print("[erro] 'pulado' exige --motivo: pular sem registrar por que "
              "e' como o trabalho se perde", file=sys.stderr)
        return 2
    reg = {
        "quando": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "chave": chave,
        "estagio": estagio,
        "nome": ESTAGIOS[estagio],
        "resultado": resultado,
    }
    if motivo:
        reg["motivo"] = motivo
    with caminho(acervo).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
    print(f"[ok] {chave} estagio {estagio} ({ESTAGIOS[estagio]}) = {resultado}")
    return 0


def cmd_painel(acervo: Path) -> int:
    feito = concluidos(acervo)
    chaves = chaves_do_acervo(acervo)
    print(f"chaves no acervo: {len(chaves)}")
    for est in POR_ARTIGO:
        n = sum(1 for c in chaves if est in feito.get(c, set()))
        print(f"  estagio {est} ({ESTAGIOS[est]:<10}): {n:>4}/{len(chaves)}")
    faltam = [c for c in chaves if set(POR_ARTIGO) - feito.get(c, set())]
    print(f"pendentes: {len(faltam)}")
    if faltam[:5]:
        print("  proximas:", ", ".join(faltam[:5]))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--acervo", type=Path,
                    default=Path(os.environ.get("ACERVO", ".")))
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("proximo")
    sub.add_parser("painel")
    m = sub.add_parser("marcar")
    m.add_argument("chave")
    m.add_argument("estagio", type=int, choices=[1, 2, 3, 4, 5])
    m.add_argument("resultado", nargs="?", default="ok")
    m.add_argument("--motivo")
    a = ap.parse_args()

    if a.cmd == "proximo":
        return cmd_proximo(a.acervo)
    if a.cmd == "painel":
        return cmd_painel(a.acervo)
    return cmd_marcar(a.acervo, a.chave, a.estagio, a.resultado, a.motivo)


if __name__ == "__main__":
    raise SystemExit(main())
