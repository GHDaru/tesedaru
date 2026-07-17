---
id: Goudjil2018
title: "A Novel Active Learning Method Using SVM for Text Classification"
authors: ["Goudjil, Mohamed", "Koudil, Mouloud", "Bedda, Mouldi", "Ghoggali, Noureddine"]
year: 2018
venue: "International Journal of Automation and Computing, 15(3), pp. 290–298"
doi: "10.1007/s11633-015-0912-z"
pdf: referencias-pdf/Goudjil2018.pdf
paper_type: metodo
pillars: [P2]
status: fichado
proposes: [selecao-em-lote-por-probabilidade-svm]
uses_methods: [svm, aprendizado-ativo, selecao-em-lote]
datasets: []
metrics: [acuracia]
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: [Hoi2006]
contradicts: []
builds_on: [Lewis1994, Hoi2006]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Já citado no formalismo do Cap.2 (arcabouço do ciclo de AL). Exemplo
           canônico de AL+SVM com seleção em LOTE guiada por probabilidades —
           antecedente direto do QueryBatch por incerteza do FALCO."
---

# A Novel Active Learning Method Using SVM for Text Classification

## Resumo
Método de AL para categorização de texto que seleciona um **lote de amostras
informativas por iteração** usando as saídas probabilísticas de SVMs
(posterior de pertencimento), reduzindo o esforço de rotulagem manual sem
comprometer a acurácia. Motivação clássica: rotular manualmente é demorado e
sujeito a erro; não-rotulados abundam na internet. O artigo já é usado no Cap.2
da tese como uma das formulações-base do ciclo de AL (junto com Settles).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Seleção em lote via probabilidades do classificador reduz esforço de rotulagem mantendo acurácia | Abstract | Cap.2 (formalismo, já citado); antecedente do QueryBatch por incerteza |
| C2 | Rotulagem manual é demorada E sujeita a erro | Abstract | Raro reconhecimento pré-LLM de que o oráculo humano erra — ponte para o oráculo ruidoso do FALCO (E4) |

## Números que posso citar
- (Resultados em benchmarks de texto clássicos; citar qualitativamente.)

## Crítica / limitações (minha leitura)
- SVM com BoW, benchmarks em inglês; probabilidades de SVM exigem calibração
  (Platt) — fragilidade análoga à incerteza mal calibrada de DNNs.

## Ideias que gera para a tese
- A citação já existente no Cap.2 ganha lastro: manter e referenciar C2 na
  motivação do E4 (ruído de oráculo não é exclusividade de LLM).
