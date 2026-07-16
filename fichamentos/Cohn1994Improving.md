---
id: Cohn1994Improving
title: "Improving Generalization with Active Learning"
authors: ["Cohn, David", "Atlas, Les", "Ladner, Richard"]
year: 1994
venue: "Machine Learning, 15, pp. 201–221, Kluwer"
doi: "10.1007/BF00993277"
pdf: referencias-pdf/Cohn1994Improving.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [selective-sampling, sg-network]
uses_methods: [version-space, redes-neurais]
datasets: [tres-dominios-sinteticos]
metrics: [generalizacao]
tasks: [aprendizado-de-conceito-binario]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Angluin1988]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Formaliza o selective sampling (consultar um oráculo apenas nas regiões
           'úteis' do domínio) e prova que aprendizado ativo pode ser mais poderoso
           que aprendizado passivo — a garantia conceitual por trás do laço do FALCO."
---

# Improving Generalization with Active Learning

## Resumo
Um dos artigos fundadores do AL moderno. Distingue aprendizado ativo de "learning
from examples": o algoritmo assume ao menos algum controle sobre QUAL parte do
domínio de entrada recebe informação. Mostra que, em algumas situações, AL é
**provadamente mais poderoso** que aprender apenas com exemplos aleatórios, dando
melhor generalização para um número fixo de exemplos. No problema de aprender um
conceito binário sem ruído, formaliza o **selective sampling**: o aprendiz recebe
informação de distribuição do ambiente e consulta um oráculo nas partes do domínio
que considera "úteis" (região de incerteza derivada do version space). Implementa
aproximadamente a ideia com uma rede neural (SG-network) e observa melhora
significativa de generalização em três domínios.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL é provadamente mais poderoso que amostragem aleatória em certas condições | Abstract | Cap.2: fundamento teórico; tempera as expectativas (condições: sem ruído, conceito binário) |
| C2 | Selective sampling = consultar oráculo só na região de incerteza | Abstract/§1 | Ancestral direto do uncertainty sampling usado nas fases do FALCO |
| C3 | A região de incerteza deriva do version space (conjunto de hipóteses consistentes) | Abstract | Ponte teórica para query-by-committee no Cap.2 |

## Números que posso citar
- (Domínios sintéticos; usar como fonte teórica, não de números aplicados.)

## Crítica / limitações (minha leitura)
- Cenário sem ruído e conceito binário — o oposto do regime FALCO (oráculo ruidoso,
  621 classes). A garantia de superioridade NÃO se transfere; por isso a tese
  precisa de validação empírica (E1–E4) em vez de apelo teórico.

## Ideias que gera para a tese
- Usar C1 com a ressalva explícita das hipóteses (sem ruído) para motivar E4:
  o que resta da vantagem do AL quando o oráculo erra com taxa ε?
