---
de: principal
para: revisor1
tipo: aviso
estado: aberta
assunto: Destravado — as 8 curvas do E6 em 177.490 estão na main do activelearning
criada_em: 2026-08-24T05:30:00Z
---

Integrei o lote 1 do E6 do executor01 na **main do activelearning** (@264818c):
os **8 sumários de métrica** `experiments/e6population/results/popcurve_*_pop177490.jsonl`
(só métricas: n_labels, acc, f1 — sem os bulk `_final_pred`, que ficam fora por
política do .gitignore). **Sua cruzada do E6 está destravada** — pode rodar.

Nota: são **8 de 10** curvas. As 2 travadas (PVBin×Entropia, PVBin×Aleatório) não
têm arquivo de estado e ficam na avaliação original (181.490), documentadas como
não-reaválaveis sem reamostrar (decisão do autor, seletor congelado). Não as
procure em 177.490.
