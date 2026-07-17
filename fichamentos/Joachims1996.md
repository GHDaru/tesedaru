---
id: Joachims1996
title: "A Probabilistic Analysis of the Rocchio Algorithm with TFIDF for Text Categorization"
authors: ["Joachims, Thorsten"]
year: 1996
venue: "Technical Report CMU-CS-96-118, Carnegie Mellon University"
doi: ""
pdf: referencias-pdf/Joachims1996.pdf
paper_type: teoria
pillars: [geral]
status: fichado
proposes: [probtfidf, analise-probabilistica-do-rocchio]
uses_methods: [rocchio, tfidf, naive-bayes]
datasets: []
metrics: [acuracia]
tasks: [classificacao-de-texto]
models: []
extends: [Salton1988]
compares_with: []
contradicts: []
builds_on: [Salton1988]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Explicação probabilística do TF-IDF/Rocchio: o ancestral formal da
           família de classificadores por protótipo — a MESMA família dos métodos
           argmax de Darú (2022/2024) e do PVBin. Dá profundidade teórica à
           linhagem do nosso baseline."
---

# A Probabilistic Analysis of the Rocchio Algorithm with TFIDF

## Resumo
TR CMU 1996: análise probabilística do algoritmo de relevance feedback de Rocchio
em categorização de texto, derivando uma versão probabilística do classificador e
oferecendo explicação formal para a heurística TF-IDF; compara Rocchio, variante
probabilística e Naive Bayes em três tarefas.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | TF-IDF/Rocchio admite fundamentação probabilística | Abstract | Cap.2: os métodos argmax por protótipo (Daru2022/2024, PVBin) têm linhagem formal — não são apenas heurística de RI |

## Números que posso citar
- (Teórico/experimentos da época.)

## Crítica / limitações (minha leitura)
- Técnico e antigo; citar apenas na frase de linhagem do protótipo.

## Ideias que gera para a tese
- Frase no Cap.3 ao apresentar o PVBin: protótipo por classe = Rocchio binário
  normalizado; Joachims1996 dá o lastro.
