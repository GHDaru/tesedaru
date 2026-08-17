---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Golovin2011
title: "Adaptive Submodularity: Theory and Applications in Active Learning and Stochastic Optimization"
authors: ["Golovin, Daniel", "Krause, Andreas"]
year: 2011
venue: "Journal of Artificial Intelligence Research (JAIR)"
doi: ""
pdf: referencias-pdf/Golovin2011.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: metodo
pillars: [P4]
status: ficha-minima

# ===== ENTIDADES =====
proposes: [submodularidade-adaptativa]
uses_methods: [aprendizado-ativo, algoritmo-guloso, otimizacao-estocastica]
datasets: []
metrics: []
tasks: []
models: []

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Krause2014]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: aprendizado-ativo
    note: "sustenta a frase da §2.2 sobre tratamento de lotes por otimização submodular: a submodularidade adaptativa garante que o guloso é competitivo com a política ótima, e o aprendizado ativo é uma das três aplicações que o próprio artigo desenvolve"
---

# Adaptive Submodularity

**Ficha mínima** (padrão do ciclo 008). Lida na fonte (60 pp.), identidade
conferida na folha de rosto. Sobe de nível pela análise do nível 3: **sustenta
afirmação**, não é citada por existência.

## O resultado que a tese usa

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Se o problema satisfaz **submodularidade adaptativa**, um algoritmo guloso adaptativo simples é **garantidamente competitivo com a política ótima** | Resumo, p. 1 | § "Aprendizado ativo" — sustenta "tratamento natural de lotes via otimização submodular" |
| C2 | **Aprendizado ativo é uma das três aplicações** que o artigo desenvolve (ao lado de gestão de sensores e marketing viral); a §1 dedica um bloco a ela | Resumo (p. 1) e §1, terceira aplicação (p. ~4) | §2.2 — mostra que a ponte submodularidade → aprendizado ativo é do próprio artigo, não nossa |
| C3 | A propriedade permite acelerar drasticamente o guloso por **avaliações preguiçosas** | Resumo, p. 1 | §2.2 e Cap. 3 — relevante ao custo computacional, que é o motivo declarado pelo qual esta tese **não** adota a família |

## Citação direta (com página)

> "we introduce the concept of adaptive submodularity, generalizing submodular set
> functions to adaptive policies. We prove that if a problem satisfies this
> property, a simple adaptive greedy algorithm is guaranteed to be competitive
> with the optimal policy." (p. 1)

## Leitura crítica em uma linha

A tese cita esta família para em seguida **dispensá-la** por custo computacional
proibitivo no nosso regime — e o C3 mostra que os próprios autores tratam o custo
como problema a atacar (avaliações preguiçosas). A dispensa continua defensável,
mas o argumento honesto é sobre o **nosso** regime (re-treinamento por par
candidato-rótulo em centenas de classes), não sobre a família ser lenta em geral.
Vale ao Cap. 2 dizer isso nessa ordem.
