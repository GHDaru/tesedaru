---
id: Persello2014
title: "Active and Semisupervised Learning for the Classification of Remote Sensing Images"
authors: ["Persello, Claudio", "Bruzzone, Lorenzo"]
year: 2014
venue: "IEEE TGRS, 52(11), pp. 6937–6956"
doi: "10.1109/TGRS.2014.2305805"
pdf: referencias-pdf/Persello2014.pdf
paper_type: avaliacao
pillars: [geral]
status: fichado
proposes: [comparacao-al-vs-ssl]
uses_methods: [aprendizado-ativo, semi-supervisao]
datasets: [imagens-sensoriamento-remoto]
metrics: [acuracia]
tasks: [classificacao-de-imagens]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Comparação teórica+experimental AL vs SSL sob poucos rótulos e viés de
           seleção amostral: a referência para a pergunta 'por que AL e não
           semi-supervisão?' no Cap.2 — os dois paradigmas atacam o mesmo gargalo."
---

# Active and Semisupervised Learning for Remote Sensing Classification

## Resumo
IEEE TGRS 2014: revisão + comparação teórica e experimental de AL e
semi-supervisão (SSL) em classificação com poucas amostras de treino e viés de
seleção amostral, destacando semelhanças, diferenças e um framework conceitual
comum. Domínio é sensoriamento remoto, mas a análise AL-vs-SSL é geral.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL e SSL são comparáveis sob um framework comum; a escolha depende do custo/disponibilidade do oráculo | Abstract | Cap.2: responder "por que não SSL?" — porque temos oráculo barato (LLM), o que muda a economia a favor do AL |

## Números que posso citar
- (Domínio distinto; qualitativo.)

## Crítica / limitações (minha leitura)
- Imagens, não texto; pré-DL. Vale pela moldura conceitual apenas.

## Ideias que gera para a tese
- Parágrafo AL-vs-SSL no Cap.2 fechando com o argumento do custo do oráculo LLM.
