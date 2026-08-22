#!/usr/bin/env python3
"""Composição por classe da amostra ATIVA contra a distribuição NATURAL do pool.

Dono: revisor1. Criado para a R4 do Cap. 5 (tarefa 20260823-0330 do principal).

O QUE ISTO MEDE E POR QUÊ
------------------------
O Capítulo 5 sustenta DUAS afirmações de destaque na MESMA proposição:

  (a) "rotular tudo pode piorar ... PORQUE a amostra ativa é mais balanceada
      por classe que a distribuição natural";
  (b) o Macro F1 interno superestima o populacional "PORQUE a amostra ativa
      sobre-representa classes raras".

Os EFEITOS estavam medidos; a PROPOSIÇÃO, não. Este script a mede, sem
re-executar nada: reconstrói o pool pela receita da biblioteca e lê os
`labeled_idx` já salvos nos `*_state.json` do E6.

O braço ALEATÓRIO é o controle: se o efeito viesse do subamostrar (e não do
selecionar), ele apareceria lá também. Não aparece.

USO
---
    python3 scripts/mede-composicao-amostra-ativa.py [--activelearning CAMINHO] [-k 15000]

Espera o repositório `activelearning` como irmão deste, ou em --activelearning.
"""
import argparse, csv, json, math, os, random, sys
from collections import Counter

POOL_SIZE, DATA_SEED = 50_000, 42


def constroi_pool(raiz_al):
    """Réplica exata da receita de notebooks/auditoria/build_escala-populacional.py."""
    sys.path.insert(0, os.path.join(raiz_al, "src"))
    from activelearning.domain.instances import normalize_label
    csv_path = os.path.join(raiz_al, "data/dataset.csv")
    with open(csv_path, encoding="utf-8") as fh:
        linhas = [(r["nm_item"], normalize_label(r["nm_product"]))
                  for r in csv.DictReader(fh)]
    cont = Counter(l for _, l in linhas)
    filtradas = [(t, l) for t, l in linhas if cont[l] >= 2]
    vistos, dedup = set(), []
    for t, l in filtradas:
        k = t.strip().lower()
        if k not in vistos:
            vistos.add(k)
            dedup.append((t, l))
    random.Random(DATA_SEED).shuffle(dedup)
    return [l for _, l in dedup[:POOL_SIZE]], len({l for _, l in dedup})


def perfil(rotulos, raras):
    c = Counter(rotulos)
    n = len(rotulos)
    p = [v / n for v in c.values()]
    H = -sum(x * math.log(x) for x in p)
    massa_raras = sum(v for k, v in c.items() if k in raras) / n
    return {
        "n": n, "classes": len(c),
        "n_efetivo": math.exp(H),          # exp(entropia de Shannon)
        "top1": max(c.values()) / n,
        "classes_raras": len({k for k in c if k in raras}),
        "massa_raras": massa_raras,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--activelearning", default=None)
    p.add_argument("-k", type=int, default=15_000,
                   help="prefixo da trajetória a analisar (padrão 15000)")
    args = p.parse_args()

    raiz_al = args.activelearning or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "activelearning")
    raiz_al = os.path.abspath(raiz_al)
    if not os.path.isdir(raiz_al):
        print(f"ERRO: não achei o activelearning em {raiz_al}; use --activelearning")
        return 2

    pool, n_classes_base = constroi_pool(raiz_al)
    cp = Counter(pool)
    raras = {c for c, v in cp.items() if v < 5}

    print(f"pool reconstruído: {len(pool)} textos, {len(cp)} classes presentes "
          f"(de {n_classes_base} na base)")
    print(f"classes ausentes do pool: {n_classes_base - len(cp)} | "
          f"classes com <5 exemplos: {len(raras)}\n")

    res = os.path.join(raiz_al, "experiments/e6population/results")
    alvos = [("POOL INTEIRO (natural)", None),
             ("SGD entropia", "popcurve_sgd_entropy_state.json"),
             ("SGD aleatório (controle)", "popcurve_sgd_random_state.json"),
             ("PVBin entropia", "popcurve_pvbin_entropy_s43_state.json"),
             ("PVBin aleatório (controle)", "popcurve_pvbin_random_s43_state.json")]

    base = perfil(pool, raras)
    cab = f"{'amostra':30s} {'n':>6s} {'classes':>8s} {'nº efet.':>9s} {'top-1':>7s} {'raras':>6s} {'massa raras':>12s} {'razão':>7s}"
    print(cab)
    print("-" * len(cab))
    for nome, arq in alvos:
        if arq is None:
            d = base
        else:
            caminho = os.path.join(res, arq)
            if not os.path.exists(caminho):
                print(f"{nome:30s} (ausente: {arq})")
                continue
            idx = json.load(open(caminho))["labeled_idx"][:args.k]
            d = perfil([pool[i] for i in idx], raras)
        print(f"{nome:30s} {d['n']:6d} {d['classes']:8d} {d['n_efetivo']:9.1f} "
              f"{d['top1']*100:6.2f}% {d['classes_raras']:6d} {d['massa_raras']*100:11.3f}% "
              f"{d['massa_raras']/base['massa_raras']:6.2f}x")
    print("\nnº efetivo = exp(entropia de Shannon): quantas classes equiprováveis "
          "produziriam a mesma dispersão.\nMaior = mais balanceado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
