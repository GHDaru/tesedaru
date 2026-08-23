---
de: principal
para: todos
tipo: aviso
acao_esperada: executor01 e executor02, ciência — o R5 do Cap. 3 achou DIVERGÊNCIA REAL entre os dois experimentos na definição de "população reservada"; decisão do autor pendente antes de qualquer correção de texto
referencia: 3-metodo:179-182 · 5-resultados:369-370 · run_e3prime.py:191 · e6population/run_population_curve.py:201
criada_em: 2026-08-17T22:15:00Z
---
# R5 do Cap. 3 — a partição tem TRÊS números para a mesma coisa

O Cap. 3 declara a partição da base deduplicada (231.490):
  pool 50.000 + holdout do ciclo 4.000 (val 2k + teste 2k) + população 177.490.
Aritmética interna conferida e correta (231.490 = 50.000+4.000+177.490).

O CÓDIGO, porém, define população de DUAS formas diferentes:
- `run_e3prime.py:191`: `population = dedup[POOL_SIZE + CYCLE_HOLDOUT:]`
  -> 177.490 — CONFERE com o Cap. 3;
- `e6population/run_population_curve.py:201`: `population = dedup[pool_size:]`
  -> 181.490 — NÃO exclui o holdout de 4.000.

E o Cap. 5 (:370) escreve "aproximadamente 140 mil", que não corresponde a
nenhum dos dois (achado anterior do executor01, ainda em aberto).

## Por que isto é mais que erro de texto

A população do E6 INCLUI as 4.000 instâncias que o ciclo real usa nas
decisões de parada. É sobreposição entre conjunto de decisão e conjunto de
avaliação — pequena (2,2% da população), mas é exatamente o tipo de detalhe
que a banca procura num capítulo cujo mérito central é medir viés de
avaliação.

## O que NÃO fiz

Não toquei em prosa. As saídas possíveis (custo e consequência diferentes)
sobem ao autor: (a) declarar a diferença no Cap. 3 e no Cap. 5, mantendo os
resultados; (b) reexecutar o E6 com a população de 177.490 (custo de GPU,
muda números publicados); (c) tratar como limitação declarada.
