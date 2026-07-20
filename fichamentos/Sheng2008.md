---
id: Sheng2008
title: "Get Another Label? Improving Data Quality and Data Mining Using Multiple, Noisy Labelers"
authors: ["Sheng, Victor S.", "Provost, Foster", "Ipeirotis, Panagiotis G."]
year: 2008
venue: "KDD 2008, pp. 614-622"
doi: "10.1145/1401890.1401965"
pdf: referencias-pdf/Sheng2008.pdf
paper_type: conferencia
pillars: [p3-oraculo]
status: fichado
proposes: [rotulagem-repetida, selective-repeated-labeling]
falco_relation:
  - type: fundamenta
    target: oraculo-imperfeito
    note: "Formaliza QUANDO vale a pena pagar por rótulos repetidos de
           anotadores ruidosos em vez de rotular itens novos: depende da
           qualidade do anotador e do custo relativo. A rotulagem repetida
           seletiva (nos itens de rótulo mais incerto) domina as demais
           políticas. Citado na Seção 2.2.3; o dilema qualidade×custo do
           rótulo é exatamente o eixo que o FALCO transforma em decisão de
           cardápio de oráculos LLM (fase Inicial × Avançada)."
---

# Get Another Label? (Sheng, Provost & Ipeirotis, 2008)

## Resumo
Estuda o regime em que rótulos são baratos e imperfeitos e o mesmo item pode
ser rotulado várias vezes. Resultados analíticos e empíricos: (i) rotulagem
repetida com voto majoritário supera rotulagem única quando a qualidade do
anotador é intermediária (nem muito alta nem muito baixa); (ii) a curva
qualidade-do-rótulo × número de repetições tem retornos decrescentes que
interagem com o custo de aquisição do exemplo; (iii) a política vencedora é
a rotulagem repetida SELETIVA, que aloca repetições nos itens cuja
incerteza de rótulo agregado é maior. Antecede a literatura de
crowdsourcing e é referência canônica do trade-off custo × qualidade do
rótulo.

## Relação com a tese
Na Seção 2.2.3, fundamenta a fratura do oráculo perfeito e a resposta
clássica (repetição, modelagem de qualidade). O FALCO herda a pergunta
econômica — onde gastar o orçamento de rotulagem — mas a responde no
cardápio de oráculos LLM: em vez de repetir consultas ao mesmo anotador
ruidoso, escala-se a qualidade do oráculo por fase (v4-flash → v4-pro),
com custo por rótulo instrumentado (E0). A verificação amostral periódica
do Apêndice A7 é a reencarnação operacional da rotulagem repetida seletiva.
