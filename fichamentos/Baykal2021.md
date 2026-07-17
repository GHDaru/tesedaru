---
id: Baykal2021
title: "Low-Regret Active Learning"
authors: ["Baykal, Cenk", "Liebenwein, Lucas", "Gal, Oren", "Feldman, Dan", "Rus, Daniela"]
year: 2021
venue: "arXiv:2104.02822"
doi: ""
pdf: referencias-pdf/Baykal2021.pdf
paper_type: metodo
pillars: [P2]
status: fichado
proposes: [al-como-sleeping-experts]
uses_methods: [minimizacao-de-regret, online-learning, ensembles]
datasets: []
metrics: [regret, acuracia]
tasks: [classificacao]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [BlumMansour2007]
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Formula a seleção de instâncias como problema de regret (sleeping
           experts), agnóstica à definição de informatividade: moldura teórica
           alternativa às heurísticas de incerteza que usamos — citar como linha
           formal e como base do trabalho futuro de seleção de oráculo."
---

# Low-Regret Active Learning

## Resumo
MIT/Haifa (2021): formula AL como *prediction with sleeping experts*, obtendo um
framework de minimização de regret para identificar dados informativos sob
QUALQUER definição de informatividade, com regret medido contra um algoritmo
onipotente. Motivado pelo sucesso de ensembles em AL.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Seleção ativa admite formulação de regret agnóstica à medida de informatividade | Abstract | Cap.2: registrar a linha formal (vs heurísticas); Cap.6: base do futuro seletor de oráculo por bandit |

## Números que posso citar
- (Qualitativo.)

## Crítica / limitações (minha leitura)
- Custo computacional do framework em pools grandes; sem noção de custo
  monetário por consulta (nosso caso com LLM) — extensão natural.

## Ideias que gera para a tese
- Par com BlumMansour2007 no trabalho futuro de seleção de oráculo com custo.
