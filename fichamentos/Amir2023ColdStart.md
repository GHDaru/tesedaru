---
id: Amir2023ColdStart
title: "Cold-start Active Learning for Text Classification of Business Documents"
authors: ["Amir, Bachir Kaddis Beshay"]
year: 2023
venue: "Dissertação de mestrado (MSc Interaction Technology), University of Twente"
doi: ""
pdf: referencias-pdf/Amir2023ColdStart.pdf
paper_type: dissertacao
pillars: [P1]
status: fichado
proposes: [construcao-de-pool-inicial]
uses_methods: [cold-start, selecao-de-seed, aprendizado-ativo]
datasets: [documentos-de-negocio]
metrics: []
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [zhang2022surveyAL]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Confirma, em contexto industrial de 2023, que o cold start segue
           subexplorado em classificação de texto — exatamente a lacuna que o P1
           (otimização do L0 via AG) e a fase 0 do FALCO atacam. Uso principal:
           evidência de atualidade da lacuna no Cap.1/Cap.2."
---

# Cold-start Active Learning for Text Classification of Business Documents

## Resumo
Dissertação (105 pp., contexto industrial com parceiro de negócio) focada na fase
de **cold start** do AL para classificação de documentos de negócio: como
construir judiciosamente o pool inicial rotulado quando não há rótulo algum.
Motivação declarada: a qualidade do pool inicial ("cold start") influencia
significativamente a eficiência e a acurácia das iterações seguintes, mas essa
fase crítica permanece **subexplorada, particularmente em classificação de
texto**. O trabalho estuda técnicas de construção do pool inicial que habilitam
decisões de amostragem melhores nas iterações posteriores ("warm start"),
otimizando o processo de AL como um todo.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O cold start influencia fortemente a eficiência/acurácia das iterações seguintes de AL | Abstract | Cap.1: motivação do P1; converge com zhang2022surveyAL §5.1 |
| C2 | A fase de cold start permanece subexplorada em classificação de texto (2023) | Abstract | Cap.2: sustenta a atualidade da lacuna que o L0-ótimo via AG preenche |
| C3 | Cenário industrial: não-rotulados abundantes, anotação cara — o caso de uso é real, não acadêmico | Abstract | Cap.1: paralelo com nosso cenário de varejo |

## Números que posso citar
- (Dissertação aplicada; extrair números específicos das seções de resultados se
  algum for citado — uso principal é qualitativo/motivacional.)

## Crítica / limitações (minha leitura)
- Oráculo humano clássico; não considera LLM nem custo por token.
- Domínio de documentos de negócio (textos mais longos que os nossos ~32 chars);
  as técnicas de seed por representatividade podem se comportar diferente em
  texto curto esparso.
- Sem otimização evolutiva do seed — abordagens heurísticas; o P1 da tese formula
  o L0 como problema de otimização com AG, que é mais forte metodologicamente.

## Ideias que gera para a tese
- Citar C1+C2 em par com o survey de Zhang (2022) para mostrar que a lacuna do
  cold start atravessa do meio acadêmico (survey) ao industrial (esta dissertação).
