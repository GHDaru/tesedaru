# Relatório de convergência — reexecuções independentes × resultados originais

Tarefa C3 do checklist. Artefatos-fonte:
`activelearning/experiments/p1/results/replay_l0.jsonl` e `replay_ga.jsonl`
(biblioteca nova, DDD/hexagonal), comparados aos números originais do draft
(`Tese-Vers-o-Draft/capitulo_04_resultados`). Tabelas completas na tese:
Cap. 4 (Seção "Reexecução independente e circularidade") e Apêndice A6.

## C1 — Sensibilidade de L0 (P1-replay)

- Desenho do replay: grade reduzida de 15 tamanhos × 10 repetições
  (racional em D-002), PVBin da biblioteca nova, mesmas partições.
- Convergência: divergência máxima de **0,7 p.p.** de acurácia média em
  relação ao original (47 tamanhos × 30 repetições) em TODOS os tamanhos
  comparáveis — de 6,6% vs 6,7% em |L0|=10 até 88,8% vs 89,1% em 200k.
- Conclusão: o fenômeno de sensibilidade (amplitude 6,4 p.p. em |L0|=100,
  decaindo à irrelevância em |L0|≥10^5) reproduz-se de forma independente.

## C2 — Envelope evolutivo (AG-replay, protocolo anticircularidade)

- Desenho: 2 tamanhos (I=50, I=500) × max/min, pop. 30, 40 gerações,
  aptidão em partição de aferição separada; reavaliação final em teste
  intocado (correção A3/R1).
- Mecanismo reproduzido: +5,2 p.p. do max_f1 sobre a média aleatória em I=50.
- Achado novo: **inflação de circularidade quantificada** — max_f1 I=500
  atinge 19,4% na partição de aptidão, mas 13,1% no teste intocado
  (−6,3 p.p.). O envelope original, avaliado na própria partição de
  aptidão, está portanto inflacionado; a comparação DRI-SL × AG da tese
  usa o envelope corrigido (e mesmo contra o inflacionado o DRI-SL vence
  em 100..5000).

## Veredito

Reexecução independente CONVERGE com os resultados originais dentro de
0,7 p.p.; única divergência sistemática é explicada e virou achado
metodológico (circularidade), incorporado ao Cap. 4.
