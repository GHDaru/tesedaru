---
id: Joachims1998
title: "Text Categorization with Support Vector Machines: Learning with Many Relevant Features"
authors: ["Joachims, Thorsten"]
year: 1998
venue: "ECML 1998, pp. 137–142, Springer"
doi: "10.1007/BFb0026683"
pdf: referencias-pdf/Joachims1998.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [svm-para-texto]
uses_methods: [svm]
datasets: [reuters]
metrics: []
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Salton1988]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "O artigo que explica POR QUE texto favorece classificadores de margem:
           alta dimensão com muitos atributos relevantes e vetores esparsos.
           Fundamenta a discussão de propriedades do espaço textual no Cap.2."
---

# Text Categorization with Support Vector Machines (Joachims, 1998)

## Resumo
ECML 1998: analisa as propriedades particulares do aprendizado com texto — alta
dimensionalidade, muitos atributos RELEVANTES (pouca redundância descartável),
vetores esparsos — e mostra teórica e empiricamente por que SVMs são adequadas,
com melhoras substanciais sobre os melhores métodos da época, de forma robusta e
sem ajuste manual.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O espaço textual tem alta dimensão E muitos atributos relevantes; margens lidam bem com isso | Abstract | Cap.2: caracterização do espaço de atributos textual (vale para nosso BoW/PVBin) |

## Números que posso citar
- (Reuters da época; usar o argumento, não os números.)

## Crítica / limitações (minha leitura)
- Documentos longos; em texto curto a esparsidade é mais extrema ainda — o
  argumento se intensifica.

## Ideias que gera para a tese
- Par com Daru2022 (SVM sigmoid competitivo no nosso domínio) — coerência entre a
  teoria de 1998 e o resultado empírico de 2022.
