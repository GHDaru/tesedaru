---
id: Pennington2014
title: "GloVe: Global Vectors for Word Representation"
authors: ["Pennington, Jeffrey", "Socher, Richard", "Manning, Christopher D."]
year: 2014
venue: "EMNLP 2014, pp. 1532–1543"
doi: "10.3115/v1/D14-1162"
pdf: referencias-pdf/Pennington2014.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [glove]
uses_methods: [fatoracao-de-coocorrencia, regressao-log-bilinear]
datasets: []
metrics: [analogia-de-palavras]
tasks: [representacao-de-palavras]
models: [glove]
extends: [Mikolov2013, Deerwester1990]
compares_with: [Mikolov2013]
contradicts: []
builds_on: [Deerwester1990, Mikolov2013]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "GloVe unifica as duas famílias de representação (fatoração global à la
           LSA + janelas locais à la word2vec) — fecha o elo denso-estático da
           linha de representação do Cap.2."
---

# GloVe: Global Vectors for Word Representation

## Resumo
Modelo log-bilinear global que explica POR QUE regularidades semânticas emergem
como aritmética vetorial e combina as vantagens das duas famílias da literatura:
fatoração global de matriz (estatísticas de coocorrência do corpus inteiro) e
métodos de janela de contexto local. Estado da arte em analogia de palavras na
época.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Fatoração global + contexto local são unificáveis num único modelo | Abstract | Cap.2: fecha a discussão de embeddings estáticos com as duas linhagens explícitas |

## Números que posso citar
- (Clássico conceitual.)

## Crítica / limitações (minha leitura)
- Estático como word2vec; mesma insuficiência para o nosso domínio.

## Ideias que gera para a tese
- Compõe o parágrafo-linha-do-tempo do Cap.2.
