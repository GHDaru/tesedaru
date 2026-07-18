---
id: Gholamian2024
title: "LLM-Based Robust Product Classification in Commerce and Compliance"
authors: ["Gholamian, Sina", "Romani, Gianfranco", "Rudnikowicz, Bartosz", "Skylaki, Stavroula"]
year: 2024
venue: "CustomNLP4U @ EMNLP 2024 (arXiv:2408.05874)"
doi: "10.48550/arXiv.2408.05874"
pdf: referencias-pdf/Gholamian2024.pdf
paper_type: workshop
pillars: [P3]
status: fichado
datasets: [Icecat-370, WDC-222]
metrics: [acuracia, robustez-a-abreviacao]
tasks: [classificacao-de-produtos]
falco_relation:
  - type: suporta
    target: claim-granularidade
    note: "Maior espaço fechado da linha LLM-produto que encontramos: 370 folhas
           (Icecat, 490k treino). LLMs com ICL superam supervisionados sob
           ABREVIAÇÃO e truncamento — exatamente a degradação do nosso domínio
           (cupom fiscal). Ancora o claim de que 621 classes excede a literatura."
---

# LLM-Based Robust Product Classification (Gholamian et al., 2024)

## Resumo
Avalia LLMs vs. supervisionados em classificação de produtos com taxonomias
fechadas (Icecat 370 folhas; WDC 222), sob ataques realistas de abreviação e
amputação de atributos. LLMs com few-shot/ICL mantêm robustez onde os
supervisionados degradam — recomendando o LLM como oráculo forte para títulos
pobres.

## Relação com a tese
Citado no Cap. 6 (contribuições) para ancorar a granularidade do E0; apoia a
tese de reservar o oráculo LLM para onde o classificador leve falha por
pobreza descritiva.

## Limitações
Inglês; sem laço de AL; sem custo instrumentado.
