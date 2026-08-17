---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Krause2014
title: "Submodular Function Maximization"
authors: ["Krause, Andreas", "Golovin, Daniel"]
year: 2014
venue: "Capítulo em Tractability: Practical Approaches to Hard Problems (Cambridge University Press)"
doi: ""
pdf: referencias-pdf/Krause2014.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: survey
pillars: [P4]
status: ficha-minima

# ===== ENTIDADES =====
proposes: []
uses_methods: [algoritmo-guloso, otimizacao-submodular]
datasets: []
metrics: []
tasks: []
models: []

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: aprendizado-ativo
    note: "é o texto de referência da definição de submodularidade e dos algoritmos com garantia, invocado pela §2.2 ao falar de seleção de lotes"
---

# Submodular Function Maximization

**Ficha mínima** (padrão do ciclo 008). Lida na fonte (28 pp.), identidade
conferida.

## O resultado que a tese usa

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Submodularidade é propriedade de funções de conjunto com consequências teóricas profundas; o texto introduz a propriedade, suas generalizações e **algoritmos de otimização com garantia** | Abertura, p. 1 | §2.2 (`2-fundam/texto.tex:447`) — é a referência da definição usada na frase dos lotes |
| C2 | A submodularidade pode ser explorada algoritmicamente para implementar uma versão **acelerada** do guloso quando a avaliação da função é custosa | §sobre algoritmos acelerados, p. ~10 | Cap. 2 — mesma leitura do `Golovin2011`: o custo é problema tratado, não ignorado |

## ACHADO de bibliografia: o tipo da entrada está errado

O `.bib` declara `@inproceedings{Krause2014, ...}`. **Não é artigo de
conferência: é capítulo de livro.** O próprio texto se refere a si mesmo como
"this chapter" em cinco passagens (linhas 25, 71, 246, 261 e 1212 do texto
extraído) e abre com "In this survey we will introduce submodularity…". O volume
é *Tractability: Practical Approaches to Hard Problems* (Cambridge University
Press, 2014).

**Consequência que interessa à decisão do nível 3:** corrigido o tipo para
`@incollection` (com `booktitle` e `publisher`), esta obra passa a ser
**canônica por tipo** pela ADR 0012 — citada para definição consagrada, dispensa
fichamento integral e exige apenas entrada correta e verificável por script.
Ou seja: ela **sai** da lista de pendências por um caminho que já existe na
constituição, sem precisar de política nova.

Esta ficha mínima fica como registro da leitura e do achado; se o autor preferir,
pode ser descartada depois de o tipo ser corrigido — o que **não** pode ficar é o
`@inproceedings`, que é fato errado sobre a obra.

`referencias.bib` é superfície do revisor1: levo como sugestão, não como edição.
