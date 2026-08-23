#!/usr/bin/env python3
"""Cruzada dos números do E6 reavaliados em 177.490 contra os originais.

Dono: revisor1. §6 do protocolo: quem executa não verifica. O executor01
reavaliou; isto confere.

O QUE CONFERE
-------------
1. a curva INTEIRA foi reavaliada (não só o ponto final);
2. as métricas INTERNAS foram transportadas sem recálculo (só as externas
   mudam — o pool não foi tocado);
3. o tamanho do efeito, contra a dispersão entre sementes já medida;
4. os quatro números que a Tabela do Cap. 5 reporta (teto, saturação,
   F1@10k, F1@20k).

USO
---
    python3 scripts/cruza-e6-177490.py [--repo CAMINHO]
"""
import argparse, glob, json, os, statistics as st, sys

# tab:e6 do Cap. 5: (teto F1, saturação, F1@10k, F1@20k)
TESE = {"sgd_entropy": (0.591, 8000, 0.565, 0.574),
        "sgd_drisl-cs": (0.555, 10000, 0.533, 0.543),
        "sgd_drisl-c": (0.491, 15500, 0.412, 0.486),
        "sgd_random": (0.459, 16500, 0.391, 0.449),
        "sgd_drisl": (0.441, 41500, 0.310, 0.365),
        "pvbin_drisl-cs": (0.528, 18000, 0.444, 0.498),
        "pvbin_drisl-c": (0.525, 39500, 0.349, 0.453),
        "pvbin_drisl": (0.527, 45500, 0.284, 0.356)}
SD_SEMENTE_ACC, SD_SEMENTE_F1 = 0.075, 0.354   # p.p., medidos nas 9 execuções


def quatro(pontos, chave):
    d = {p["n_labels"]: p[chave] for p in pontos}
    teto = max(d.values())
    sat = min(n for n in sorted(d) if d[n] >= 0.95 * teto)
    return teto, sat, d.get(10000), d.get(20000)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--repo", default=None)
    args = p.parse_args()
    raiz = args.repo or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "..", "activelearning")
    res = os.path.abspath(os.path.join(raiz, "experiments/e6population/results"))
    if not os.path.isdir(res):
        print(f"ERRO: não achei {res}; use --repo")
        return 2

    arqs = sorted(glob.glob(os.path.join(res, "*_pop177490.jsonl")))
    print(f"curvas reavaliadas: {len(arqs)} (as 2 PVBin travadas ficam em 181.490)\n")

    falhas, das, dfs = [], [], []
    print(f"{'célula':16s} {'pts':>4s} {'int?':>5s} {'Δacc pp':>8s} {'Δf1 pp':>8s}")
    for f in arqs:
        base = f.replace("_pop177490", "")
        novo = [json.loads(l) for l in open(f)]
        orig = {}
        for l in open(base):
            x = json.loads(l)
            orig.setdefault(x["n_labels"], []).append(x)
        interno_ok = all(abs(n["acc_int"] - orig[n["n_labels"]][0]["acc_int"]) < 1e-9
                         for n in novo if n["n_labels"] in orig)
        if not interno_ok:
            falhas.append(f"{base}: métrica interna alterada")
        d = [(n["acc_ext_177490"] - n["acc_ext_181490_original"]) * 100 for n in novo]
        e = [(n["f1_ext_177490"] - n["f1_ext_181490_original"]) * 100 for n in novo]
        das += d
        dfs += e
        k = os.path.basename(base).replace("popcurve_", "").replace(".jsonl", "")
        print(f"{k:16s} {len(novo):4d} {'sim' if interno_ok else 'NÃO':>5s} "
              f"{st.mean(d):+8.3f} {st.mean(e):+8.3f}")

    print(f"\nΔ em {len(das)} pontos: acurácia média {st.mean(das):+.4f} pp "
          f"(máx |Δ| {max(map(abs, das)):.4f}); "
          f"Macro F1 média {st.mean(dfs):+.4f} pp (máx |Δ| {max(map(abs, dfs)):.4f})")
    print(f"dispersão entre sementes já medida: {SD_SEMENTE_ACC} pp (acc) · "
          f"{SD_SEMENTE_F1} pp (F1) — o efeito fica abaixo dela")

    print(f"\n{'célula':16s} {'teto':>14s} {'saturação':>16s} {'F1@10k':>14s} {'F1@20k':>14s}")
    mudou = 0
    for f in arqs:
        k = os.path.basename(f).replace("popcurve_", "").replace("_pop177490.jsonl", "")
        if k not in TESE:
            continue
        t, s, a, b = quatro([json.loads(l) for l in open(f)], "f1_ext_177490")
        T, S, A, B = TESE[k]
        m = lambda x, y, n=3: f"{x:.{n}f}->{y:.{n}f}" if round(x, n) != round(y, n) else f"{x:.{n}f} ="
        ms = f"{S}->{s}" if S != s else f"{S} ="
        if round(T, 3) != round(t, 3) or S != s or round(A, 3) != round(a, 3) or round(B, 3) != round(b, 3):
            mudou += 1
        print(f"{k:16s} {m(T,t):>14s} {ms:>16s} {m(A,a):>14s} {m(B,b):>14s}")
    print(f"\ncélulas com algum valor a atualizar: {mudou} de {len(TESE)}")

    if falhas:
        print("\nFALHA:", "; ".join(falhas))
        return 1
    print("\nPASS — curva inteira reavaliada, métricas internas preservadas, "
          "efeito abaixo da dispersão entre sementes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
