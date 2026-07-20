---
id: Demsar2006
title: "Statistical Comparisons of Classifiers over Multiple Data Sets"
authors: ["Demšar, Janez"]
year: 2006
venue: "Journal of Machine Learning Research 7:1-30"
doi: ""
pdf: referencias-pdf/Demsar2006.pdf
paper_type: periodico
pillars: [transversal]
status: fichado
proposes: [protocolo-de-comparacao-estatistica-de-classificadores]
falco_relation:
  - type: fundamenta
    target: instrumentacao-estatistica
    note: "A referência APLICADA canônica para comparação estatística de
           classificadores em ML: recomenda testes NÃO-paramétricos (Wilcoxon
           signed-ranks para 2 classificadores; Friedman+post-hoc para vários)
           sobre t-testes, por violação de normalidade e comensurabilidade.
           Fundamenta nossa escolha do Wilcoxon pareado por semente (E1/E4) na
           subseção de inferência do Cap. 2 (plano 2.1.4)."
---

# Statistical Comparisons of Classifiers (Demšar, JMLR 2006)

## Resumo
Artigo-protocolo que examina como comparar classificadores com rigor: critica o
uso de t-testes e médias de acurácia entre datasets, e recomenda o teste de
postos sinalizados de Wilcoxon (2 modelos) e Friedman com post-hoc de Nemenyi
(k modelos), com diagramas de diferença crítica. Um dos artigos mais citados da
metodologia experimental em ML.

## Relação com a tese
Base da subseção nova de inferência estatística (Cap. 2, plano): justifica o
Wilcoxon pareado como escolha padrão da área, complementando a citação
original (Wilcoxon 1945) com a prática de ML.
