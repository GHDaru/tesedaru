---
id: Zhang2025
title: "Applying LLMs to Active Learning: Towards Cost-Efficient Cross-Task Text Classification without Manually Labeled Data"
authors: ["Zhang (et al.; ver PDF)"]
year: 2025
venue: "International Journal of Intelligent Systems (Wiley)"
doi: "10.1155/int/6472544"
pdf: referencias-pdf/Zhang2025.pdf
paper_type: periodico
pillars: [P3, P4]
status: fichado
uses_methods: [llm-como-oraculo, amostragem-por-incerteza, diversidade]
falco_relation:
  - type: compete
    target: FALCO
    note: "Linha direta 'LLM rotula o que o AL seleciona': GPT como oráculo das
           instâncias escolhidas por incerteza/diversidade, treinando modelo
           pequeno cross-task com custo muito menor que rotular tudo com o LLM.
           FALCO difere: fases com PROGRESSÃO de oráculos, espaço fechado de
           621 classes, gate pré-registrado e instrumentação de custo/medição."
---

# Applying LLMs to Active Learning (Zhang et al., 2025)

## Resumo
Framework em que o LLM substitui o anotador humano no laço de AL: estratégias
de seleção clássicas escolhem instâncias; o GPT as rotula; um modelo compacto
treina. Demonstra alta performance cross-task com custo monetário/computacional
bem inferior ao de classificar todo o dataset com o LLM.

## Relação com a tese
Já citado no Cap. 2 (linha de LLM-oráculo); com o PDF fichado, sobe para a
posição de baseline conceitual mais próximo do FALCO na frente "anotador".
