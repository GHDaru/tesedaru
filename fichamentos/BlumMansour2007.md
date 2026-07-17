---
id: BlumMansour2007
title: "Learning, Regret Minimization, and Equilibria (cap. 4 de Algorithmic Game Theory)"
authors: ["Blum, Avrim", "Mansour, Yishay"]
year: 2007
venue: "Algorithmic Game Theory (Nisan et al., eds.), Cambridge University Press"
doi: "10.1017/CBO9780511800481.006"
pdf: referencias-pdf/BlumMansour2007.pdf
paper_type: livro
pillars: [geral]
status: fichado
proposes: []
uses_methods: [minimizacao-de-regret, online-learning]
datasets: []
metrics: [regret]
tasks: [aprendizado-online]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Fundamento de regret/online learning: vocabulário para formular a
           escolha sequencial de estratégia/oráculo do FALCO como decisão online
           (cada fase 'aposta' num braço). Uso apenas conceitual."
---

# Learning, Regret Minimization, and Equilibria

## Resumo
Capítulo 4 do livro Algorithmic Game Theory: algoritmos de decisão repetida sob
incerteza com garantias de regret (desempenho próximo da melhor ação fixa em
retrospecto) e conexões com equilíbrios quando todos os jogadores se adaptam.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Decisões sequenciais sob incerteza admitem garantias de regret vs melhor ação fixa | Abstract | Cap.2 (nota) ou Cap.6: enquadrar a progressão de fases do FALCO como problema de decisão online (trabalho futuro: seleção de oráculo por bandits) |

## Números que posso citar
- (Teórico.)

## Crítica / limitações (minha leitura)
- Distante do núcleo da tese; útil só se formularmos a seleção de oráculo como
  bandit — hoje é heurística de fases. Não forçar a citação.

## Ideias que gera para a tese
- Trabalho futuro concreto: escolher o oráculo por fase via bandit com custo
  (regret em US$) em vez de cronograma fixo — cita este capítulo + Baykal2021.
