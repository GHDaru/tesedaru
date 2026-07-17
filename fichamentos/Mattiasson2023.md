---
id: Mattiasson2023
title: "Active Learning applied on text classification"
authors: ["Mattiasson, Malin"]
year: 2023
venue: "Dissertação de mestrado em Estatística, Stockholm University"
doi: ""
pdf: referencias-pdf/Mattiasson2023.pdf
paper_type: dissertacao
pillars: [P2]
status: fichado
proposes: []
uses_methods: [amostragem-por-incerteza, least-confident, margin, entropia]
datasets: []
metrics: [acuracia]
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994, Settles2012]
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Comparação recente (2023) das TRÊS estratégias de incerteza que
           implementamos (least-confident, margin, entropy) em classificação de
           texto — referência de sanidade para os resultados do E1."
---

# Active Learning applied on text classification (Mattiasson, 2023)

## Resumo
Dissertação de estatística (Stockholm University, 2023) examinando o efeito do
AL — especificamente uncertainty sampling — em classificação de texto, comparando
as três estratégias clássicas: least confident, margin e entropia.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | As três estratégias de incerteza seguem sendo o baseline padrão comparado em 2023 | Abstract | Valida o conjunto de estratégias do E1 como o trio canônico |

## Números que posso citar
- (Extrair se necessário para comparação com E1.)

## Crítica / limitações (minha leitura)
- Escopo de mestrado, datasets padrão; citar como referência de sanidade apenas.

## Ideias que gera para a tese
- Comparar o ranking das 3 estratégias no nosso E1 com o dela — convergência
  reforça validade; divergência rende discussão sobre efeito do domínio.
