#!/usr/bin/env python3
"""Computa os 6 KPIs do dashboard a partir do plano + histórico git.

Camada de indicadores definida em ADR 0006 (especialista em indicadores):
moeda única = pontos de esforço (célula ponderada pelas dimensões reais do
capítulo), nunca contagem de células. Grava docs/records/kpis.json — o front
só formata; zero lógica no HTML.

Uso: python3 scripts/compute-kpis.py
"""
import json
import re
import subprocess
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REL = "docs/records/plano-revisao.json"

CREDITO = {"feito": 1.0, "gate": 0.9, "andamento": 0.5, "pendente": 0.0}
GRUPOS_BLOQUEANTES = {"experimentos", "defesa", "governanca"}
PESO_ITEM_ARTEFATO = 10


def pontos_celula(cap: dict, rid: str) -> float:
    """Tabela de pesos por rodada (minutos-equivalentes por unidade do driver)."""
    dim = cap.get("dimensoes", {})
    calc = {
        "R1": 1.0 * dim.get("travessoes", 59),
        "R2": 15.0,
        "R3": 2.5 * dim.get("citacoes", 0),
        "R4": 20.0,
        "R5": 0.4 * dim.get("tokens", 40),
        "R6": 10.0,
        "R7": 10.0 if cap["id"] in ("pre-resumo", "pre-abstract") else 20.0,
    }[rid]
    return max(5.0, calc)


def status_itens(plano: dict) -> dict:
    return {i["id"]: i.get("status") or i.get("estado", "pendente")
            for g in plano.get("artefatos", []) for i in g["itens"]} | {
            i["id"]: i.get("estado", "pendente")
            for i in plano.get("execucoes", {}).get("itens", [])}


def bloqueada(cell: dict, itens: dict) -> bool:
    return any(itens.get(b) not in ("feito", "concluido")
               for b in cell.get("bloqueado_por", []))


def credito(cell: dict, itens: dict) -> float:
    if bloqueada(cell, itens):
        return 0.0  # progresso fantasma: célula bloqueada nunca pontua
    if "progresso" in cell:
        return float(cell["progresso"])
    return CREDITO.get(cell.get("status", "pendente"), 0.0)


def prontidao(plano: dict):
    itens = status_itens(plano)
    tot = feito = 0.0
    por_rodada, por_capitulo = Counter(), Counter()
    fr, fc = Counter(), Counter()
    for c in plano["capitulos"]:
        for rid, cell in c["rodadas"].items():
            if cell.get("status") == "na":
                continue
            pts = pontos_celula(c, rid)
            ganho = pts * credito(cell, itens)
            tot += pts; feito += ganho
            por_rodada[rid] += pts; fr[rid] += ganho
            por_capitulo[c["id"]] += pts; fc[c["id"]] += ganho
    at = af = 0.0
    for g in plano.get("artefatos", []):
        if g["id"] not in GRUPOS_BLOQUEANTES:
            continue
        for i in g["itens"]:
            at += PESO_ITEM_ARTEFATO
            af += PESO_ITEM_ARTEFATO * (1.0 if i.get("status") == "feito" else 0.0)
    p_txt = feito / tot if tot else 0.0
    p_art = af / at if at else 0.0
    return {
        "global_pct": round(100 * (0.85 * p_txt + 0.15 * p_art), 1),
        "texto_pct": round(100 * p_txt, 1),
        "artefatos_pct": round(100 * p_art, 1),
        "pontos_totais": round(tot), "pontos_feitos": round(feito),
        "por_rodada": [{"id": r, "pontos": round(por_rodada[r]), "feitos": round(fr[r])}
                       for r in sorted(por_rodada)],
        "por_capitulo": [{"id": c, "pontos": round(por_capitulo[c]), "feitos": round(fc[c])}
                         for c in por_capitulo],
    }, tot


def serie_historica(pontos_totais: float):
    """Um ponto por commit do plano: (data, pontos concluídos, evento de merge)."""
    log = subprocess.run(
        ["git", "-C", str(ROOT), "log", "--follow", "--format=%H|%cI|%s", "--", REL],
        capture_output=True, text=True, check=True).stdout.strip().splitlines()
    serie = []
    for linha in reversed(log):
        sha, data, msg = linha.split("|", 2)
        try:
            snap = json.loads(subprocess.run(
                ["git", "-C", str(ROOT), "show", f"{sha}:{REL}"],
                capture_output=True, text=True, check=True).stdout)
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            continue
        # dimensões atuais valem para snapshots antigos (chave = id do capítulo)
        dims = {c["id"]: c.get("dimensoes") for c in snap["capitulos"]}
        atuais = {c["id"]: c.get("dimensoes", {}) for c in
                  json.loads((ROOT / REL).read_text())["capitulos"]}
        for c in snap["capitulos"]:
            c.setdefault("dimensoes", atuais.get(c["id"], {}))
        p, _ = prontidao(snap)
        serie.append({"data": data[:10], "commit": sha[:7],
                      "pontos": p["pontos_feitos"],
                      "pct": round(100 * p["pontos_feitos"] / pontos_totais, 1),
                      "evento": msg.split(" — ")[0][:40] if msg.lower().startswith("merge") else None})
    # um ponto por dia (o último do dia)
    por_dia = {}
    for s in serie:
        por_dia[s["data"]] = s if not (por_dia.get(s["data"], {}).get("evento")) or s["evento"] else \
            {**s, "evento": por_dia[s["data"]]["evento"]}
    dias = sorted(por_dia.values(), key=lambda s: s["data"])
    if not dias:
        return dias
    # gráfico por dia de verdade: preenche dias sem commit no plano com o
    # último valor conhecido (carregado=True), em vez de pular direto para
    # o próximo dia com commit — sem isso um hiato de dias parados aparece
    # como um segmento de reta igual a qualquer outro, escondendo a pausa
    completa = []
    cursor = date.fromisoformat(dias[0]["data"])
    fim = date.fromisoformat(dias[-1]["data"])
    idx = {d["data"]: d for d in dias}
    ultimo = None
    while cursor <= fim:
        chave = cursor.isoformat()
        if chave in idx:
            ultimo = idx[chave]
            completa.append(ultimo)
        else:
            completa.append({**ultimo, "data": chave, "evento": None, "carregado": True})
        cursor += timedelta(days=1)
    return completa


def ritmo(serie, pontos_totais):
    if len(serie) < 2:
        return {"velocidade_pontos_semana": None, "janela_dias": 14,
                "eta_semanas": None, "eta_data": None, "eta_confiavel": False,
                "serie": serie}
    hoje = date.fromisoformat(serie[-1]["data"])
    alvo = hoje - timedelta(days=14)
    base = next((s for s in serie if date.fromisoformat(s["data"]) >= alvo), serie[0])
    dias = max(1, (hoje - date.fromisoformat(base["data"])).days)
    vel = (serie[-1]["pontos"] - base["pontos"]) / dias * 7
    restante = pontos_totais - serie[-1]["pontos"]
    ok = vel >= 10
    return {"velocidade_pontos_semana": round(vel, 1), "janela_dias": dias,
            "eta_semanas": round(restante / vel, 1) if ok else None,
            "eta_data": (hoje + timedelta(weeks=restante / vel)).isoformat() if ok else None,
            "eta_confiavel": ok, "serie": serie}


def fila_e_represados(plano):
    itens = status_itens(plano)
    # pontos que cada id destrava (fecho transitivo simples de bloqueado_por)
    dependentes = {}
    for c in plano["capitulos"]:
        for rid, cell in c["rodadas"].items():
            for b in cell.get("bloqueado_por", []):
                dependentes.setdefault(b, []).append(("cel", c, rid))
    for g in plano.get("artefatos", []):
        for i in g["itens"]:
            for b in i.get("bloqueado_por", []):
                dependentes.setdefault(b, []).append(("item", i, None))

    def destrava(idem, visto=None):
        visto = visto or set()
        pts = 0.0
        for tipo, obj, rid in dependentes.get(idem, []):
            chave = (tipo, obj["id"] if tipo == "item" else obj["id"] + rid)
            if chave in visto:
                continue
            visto.add(chave)
            if tipo == "cel":
                pts += pontos_celula(obj, rid)
            else:
                pts += PESO_ITEM_ARTEFATO + destrava(obj["id"], visto)
        return pts

    fila = []
    for c in plano["capitulos"]:
        for rid, cell in c["rodadas"].items():
            if cell.get("status") == "gate":
                # rodada de capítulo é sempre revisão de texto — trilha implícita
                fila.append({"id": f"{c['id']}.{rid}", "tipo": "gate", "trilha": "texto",
                             "titulo": f"Aprovar {c['titulo']} · rodada {rid}",
                             "pontos_destravados": round(pontos_celula(c, rid))})
    for i in plano.get("execucoes", {}).get("itens", []):
        if i.get("dono") == "autor" and i.get("estado") == "aguardando_inicio":
            fila.append({"id": i["id"], "tipo": "execucao", "trilha": i.get("trilha"),
                         "titulo": i["o_que"], "pontos_destravados": round(destrava(i["id"]))})
        elif i.get("estado") == "gate":
            # execução em gate espera aprovação do autor independente do dono
            # do item (plano v29 — pedido do autor: fila agrupada por trilha)
            fila.append({"id": i["id"], "tipo": "gate", "trilha": i.get("trilha"),
                         "titulo": i.get("o_que") or i.get("descricao") or i["id"],
                         "pontos_destravados": 0})
    for g in plano.get("artefatos", []):
        for i in g["itens"]:
            if (i.get("dono") == "autor" and i.get("status") == "pendente"
                    and not bloqueada(i, itens)):
                fila.append({"id": i["id"], "tipo": "acao", "trilha": i.get("trilha"),
                             "titulo": i["titulo"], "pontos_destravados": round(destrava(i["id"]))})
    for dp in plano.get("decisoes_pendentes", []):
        fila.append({"id": dp["id"], "tipo": "decisao", "trilha": dp.get("trilha"),
                     "titulo": dp["titulo"], "pontos_destravados": 0})
    fila.sort(key=lambda x: -x["pontos_destravados"])
    return {"total": len(fila), "itens": fila}, \
           {"pontos": round(max((f["pontos_destravados"] for f in fila), default=0))}


def divida(plano):
    cit = sum(c["dimensoes"].get("citacoes", 0) for c in plano["capitulos"]
              if c["rodadas"].get("R3", {}).get("status") not in ("feito", "na"))
    chaves = set()
    for tex in ROOT.glob("*/texto.tex"):
        for m in re.finditer(r"\\cite[tp]?\*?(?:\[[^\]]*\])?\{([^}]*)\}", tex.read_text()):
            chaves.update(k.strip() for k in m.group(1).split(","))
    fich = len(list((ROOT / "fichamentos").glob("*.md")))
    return {"citacoes_pendentes": cit,
            "chaves_citadas": len(chaves), "fichamentos": fich,
            "chaves_sem_fichamento": max(0, len(chaves) - fich)}


def main():
    plano = json.loads((ROOT / REL).read_text())
    sha = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                         capture_output=True, text=True).stdout.strip()
    pront, tot = prontidao(plano)
    serie = serie_historica(tot)
    fila, repr_ = fila_e_represados(plano)
    kpis = {
        "schema": "kpis/v1",
        "computado_em": date.today().isoformat(), "git_sha": sha,
        "prontidao": pront, "ritmo": ritmo(serie, tot),
        "fila_autor": fila, "represados": repr_, "divida_fundamentacao": divida(plano),
        "meta_saida": {"parecer_ars": 83.6, "alvo": "reavaliar após R7"},
    }
    out = ROOT / "docs/records/kpis.json"
    out.write_text(json.dumps(kpis, ensure_ascii=False, indent=1) + "\n")
    print(f"ok: {out}  PGP={pront['global_pct']}%  fila={fila['total']}  "
          f"vel={kpis['ritmo']['velocidade_pontos_semana']}")


if __name__ == "__main__":
    main()
