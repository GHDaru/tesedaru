---
id: Mikolov2013
title: "Efficient Estimation of Word Representations in Vector Space"
authors: ["Mikolov, Tomas", "Chen, Kai", "Corrado, Greg", "Dean, Jeffrey"]
year: 2013
venue: "ICLR 2013 Workshop (arXiv:1301.3781)"
doi: ""
pdf: referencias-pdf/Mikolov2013.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [word2vec, cbow, skip-gram]
uses_methods: [redes-neurais-rasas]
datasets: [google-news-1.6b]
metrics: [analogia-de-palavras]
tasks: [representacao-de-palavras]
models: [word2vec]
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "word2vec: o marco dos embeddings densos eficientes (CBOW/Skip-gram),
           treináveis em bilhões de palavras em horas. Elo da linha de
           representação do Cap.2 rumo a BERT/BERTimbau."
---

# Efficient Estimation of Word Representations in Vector Space

## Resumo
Propõe CBOW e Skip-gram: arquiteturas rasas para aprender representações
vetoriais contínuas de palavras em corpora massivos, com grandes ganhos de
acurácia a custo computacional muito menor que as redes anteriores (menos de um
dia para 1,6 bilhão de palavras) e estado da arte em similaridade
sintática/semântica (analogias vetoriais).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Embeddings densos de qualidade podem ser aprendidos eficientemente em escala | Abstract | Cap.2 (linha esparso→denso); pré-requisito histórico do BERTimbau |

## Números que posso citar
- 1,6 bilhão de palavras em <1 dia (na época).

## Crítica / limitações (minha leitura)
- Embedding ESTÁTICO: um vetor por palavra — insuficiente para abreviações
  polissêmicas de varejo; só embeddings contextuais resolvem (BERT).

## Ideias que gera para a tese
- Compõe o parágrafo-linha-do-tempo do Cap.2 (ver Deerwester1990).
