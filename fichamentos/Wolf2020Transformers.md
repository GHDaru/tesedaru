---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Wolf2020Transformers
title: "Transformers: State-of-the-Art Natural Language Processing"
authors: ["Wolf, Thomas", "Debut, Lysandre", "Sanh, Victor", "Chaumond, Julien", "Delangue, Clement", "Moi, Anthony", "Cistac, Pierric", "Rault, Tim", "Louf, Rémi", "Funtowicz, Morgan", "Davison, Joe", "Shleifer, Sam", "von Platen, Patrick", "Ma, Clara", "Jernite, Yacine", "Plu, Julien", "Xu, Canwen", "Le Scao, Teven", "Gugger, Sylvain", "Drame, Mariama", "Lhoest, Quentin", "Rush, Alexander M."]
year: 2020
venue: "EMNLP 2020 (System Demonstrations)"
doi: "10.18653/v1/2020.emnlp-demos.6"
pdf: referencias-pdf/Wolf2020Transformers.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: dataset
pillars: [P4]
status: ficha-minima

# ===== ENTIDADES =====
proposes: []
uses_methods: [fine-tuning]
datasets: []
metrics: []
tasks: []
models: [bert]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "é a implementação declarada do ajuste fino do BERTimbau no Cap. 3 — citação de ferramenta, que sustenta reprodutibilidade e não afirmação sobre a literatura"
---

# Transformers: State-of-the-Art Natural Language Processing

**Ficha mínima**, porque o papel desta obra na tese é de **ferramenta**, não de
argumento. Lida na fonte (EMNLP 2020, demonstrações de sistema, 8 pp.),
identidade conferida.

## O que a tese usa desta obra

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | *Transformers* é uma **biblioteca de código aberto** que reúne arquiteturas \textit{transformer} e modelos pré-treinados sob interface unificada | §1, p. 1 | Cap. 3 — é a implementação declarada do ajuste fino do BERTimbau (com AdamW, lr $3\times10^{-5}$, lote 32, decaimento $0{,}01$) |

## Por que a citação está correta como está

É **citação de ferramenta**: a tese não afirma nada sobre a literatura com esta
referência, apenas declara **com que implementação** os resultados foram
produzidos. Para o R5 e para a reprodutibilidade, é isso que importa — e é o que
falta em muitos trabalhos que dizem "usamos BERT" sem dizer com qual código.

**Registro para o Cap. 3, se o autor quiser fortalecer:** a citação de
biblioteca ganha valor quando vem com a **versão** usada. Hoje o texto cita a
biblioteca sem versão; o apêndice de reprodutibilidade é o lugar natural para
isso, e o dado não vem desta obra — vem do nosso ambiente de execução.

## Números que posso citar

Nenhum. Artigo de demonstração de sistema; os números que ele traz (contagem de
modelos e de tarefas suportadas à época) envelheceram e não sustentam afirmação
da tese.
