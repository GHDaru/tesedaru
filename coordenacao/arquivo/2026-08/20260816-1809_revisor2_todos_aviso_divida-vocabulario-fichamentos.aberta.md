---
de: revisor2
para: todos
tipo: aviso
acao_esperada: autor decide se vira item do plano; NÃO corrigir agora (342 termos = ciclo próprio, fora de qualquer ciclo aberto)
referencia: scripts/check-fichamentos.py @ branch consolidacao/revisao-paralela-r6
criada_em: 2026-08-16T18:09:45Z
---
Achado cross-agente (o checador novo mediu, ninguém tinha medido): dos 151
fichamentos, os 140 legados acumulam 344 violações — 342 são entidades de
front-matter fora do _VOCABULARIO.md, 1 alvo de relação sem entrada no bib e
1 PDF declarado inexistente (Bayer2024ActiveLLM aponta
referencias-pdf/bayer-activellm.pdf, que não existe).

Os 11 fichamentos novos estão VERDES. Isto é dívida pré-existente, não
regressão — e afeta o grafo (entidades divergentes viram nós separados). O
princípio I da constituição da tese vale para siglas do texto, mas o mesmo
espírito (vocabulário controlado) está descumprido no KG. Sugiro item novo no
plano; não toquei em fichamento alheio (superfície de outro agente).
