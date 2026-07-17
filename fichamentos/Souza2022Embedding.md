---
id: Souza2022Embedding
title: "Embedding generation for text classification of Brazilian Portuguese user reviews: from bag-of-words to transformers"
authors: ["Souza, Frederico Dias", "Souza Filho, João Baptista de Oliveira e"]
year: 2023
venue: "Neural Computing and Applications, 35, pp. 9393–9406"
doi: "10.1007/s00521-022-08068-6"
pdf: referencias-pdf/Souza2022Embedding.pdf
paper_type: avaliacao
pillars: [geral, P4]
status: fichado
proposes: []
uses_methods: [bag-of-words, embeddings, transformers, avaliacao-comparativa]
datasets: [reviews-em-portugues]
metrics: [f1]
tasks: [classificacao-de-texto]
models: [bertimbau]
extends: []
compares_with: [Karl2023]
contradicts: []
builds_on: [Souza2020BERTimbau]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Compara BoW→transformers PARA PORTUGUÊS (reviews de e-commerce):
           versão nacional do achado de Karl2023 (transformers vencem) e ponte
           direta para a escolha do BERTimbau nos E2/E3."
---

# Embedding generation for text classification of Brazilian Portuguese user reviews

## Resumo
Avaliação sistemática (UFRJ) de representações para classificação de texto em
português brasileiro — reviews de usuários de e-commerce — cobrindo o espectro
completo de bag-of-words a transformers. Relevância dupla: idioma (PT-BR) e
domínio adjacente ao nosso (texto de e-commerce).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O espectro BoW→transformers avaliado em PT-BR confirma a vantagem dos contextuais | Escopo/Abstract | Cap.2: versão em português do Karl2023-C1; fecha a justificativa do BERTimbau |

## Números que posso citar
- (Extrair da seção de resultados se precisar de números; qualitativo por ora.)

## Crítica / limitações (minha leitura)
- Reviews (frases completas) ≠ descrições telegráficas; supervisão completa.

## Ideias que gera para a tese
- Par com Karl2023 no Cap.2: "transformers vencem em texto curto (inglês) e em
  PT-BR (reviews)" → a combinação exata (texto curto + PT-BR) fica para a tese
  demonstrar no E2.
