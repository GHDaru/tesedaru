#!/usr/bin/env python3
"""Confere qual configuração do AG produziu a tabela de envelope do Cap. 4.

Dono: revisor1. Criado para a cruzada do lote A2 (achado do revisor2: o A2
documenta a configuração ABANDONADA do algoritmo genético).

O QUE ISTO DECIDE
-----------------
O apêndice A2 declara população 50 e elitismo N_elite=5. As corridas canônicas
usam população 20. A pergunta que decide o tamanho do estrago é outra:
**os números REPORTADOS no Cap. 4 vêm de qual das duas?**

O teste é direto: para os tamanhos de L0 que têm as duas gerações de artefato
(`_old` = pop 20 e `_oldold` = pop 50), comparar o melhor indivíduo das
gerações 1 e 100 com o que a Tabela do Cap. 4 reporta.

USO
---
    python3 scripts/confere-config-ag.py [--repo CAMINHO]

Espera `activetextclassification` como irmão deste repositório.
"""
import argparse, csv, os, sys

# Tabela tab:ag-evolucao do Cap. 4 (maximização de acurácia), em %
TESE = {"10": (13.06, 18.82), "50": (22.12, 33.83), "100": (26.65, 36.71),
        "30000": (85.07, 85.88)}
TOL = 0.01


def melhor(pasta, geracao, goal="ACCURACY_MAXIMIZE"):
    f = os.path.join(pasta, f"ag_detailed_fitness{goal}.csv")
    if not os.path.exists(f):
        return None
    with open(f, encoding="utf-8") as fh:
        linhas = [x for x in csv.DictReader(fh) if int(x["generation"]) == geracao]
    return max(float(x["accuracy_on_full"]) for x in linhas) if linhas else None


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--repo", default=None)
    args = p.parse_args()
    raiz = args.repo or os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "..", "activetextclassification")
    ex = os.path.abspath(os.path.join(raiz, "examples"))
    if not os.path.isdir(ex):
        print(f"ERRO: não achei {ex}; use --repo")
        return 2

    falhas = []
    print(f"{'L0':>7s} {'tese g1/g100':>15s} {'_old (pop 20)':>16s} "
          f"{'_oldold (pop 50)':>17s}  veredito")
    for k, (t1, t100) in TESE.items():
        o = [melhor(os.path.join(ex, f"ag_optimization_results_L0_{k}old"), g)
             for g in (1, 100)]
        oo = [melhor(os.path.join(ex, f"ag_optimization_results_L0_{k}oldold"), g)
              for g in (1, 100)]
        fo = f"{o[0]*100:.2f}/{o[1]*100:.2f}" if o[0] else "-"
        foo = f"{oo[0]*100:.2f}/{oo[1]*100:.2f}" if oo[0] else "(não existe)"
        bate20 = o[0] and abs(o[0]*100 - t1) < TOL and abs(o[1]*100 - t100) < TOL
        bate50 = oo[0] and abs(oo[0]*100 - t1) < TOL and abs(oo[1]*100 - t100) < TOL
        v = "pop 20" if bate20 else ("pop 50" if bate50 else "NENHUM")
        if not bate20:
            falhas.append(k)
        print(f"{k:>7s} {f'{t1}/{t100}':>15s} {fo:>16s} {foo:>17s}  {v}")

    # população e nº de avaliações das corridas canônicas
    print()
    d = os.path.join(ex, "ag_optimization_results_L0_100old")
    with open(os.path.join(d, "ag_detailed_fitnessACCURACY_MAXIMIZE.csv"),
              encoding="utf-8") as fh:
        r = list(csv.DictReader(fh))
    ind = len({int(x["individual_id"]) for x in r})
    ger = len({int(x["generation"]) for x in r})
    print(f"corrida canônica (L0=100): população {ind} · {ger} gerações · "
          f"{len(r)} avaliações · elitismo 10% => N_elite {ind//10}")

    if falhas:
        print(f"\nFALHA: {len(falhas)} tamanho(s) não casam com pop 20: {falhas}")
        return 1
    print("\nPASS — a tabela do Cap. 4 vem das corridas de POPULAÇÃO 20. "
          "O defeito está confinado à descrição do A2; os resultados não são afetados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
