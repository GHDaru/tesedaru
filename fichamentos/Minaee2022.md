---
id: Minaee2022
title: "Deep Learning–based Text Classification: A Comprehensive Review"
authors: ["Minaee, Shervin", "Kalchbrenner, Nal", "Cambria, Erik", "Nikzad, Narjes", "Chenaghlu, Meysam", "Gao, Jianfeng"]
year: 2022
venue: "ACM Computing Surveys, 54(3), pp. 1–40"
doi: "10.1145/3439726"
pdf: referencias-pdf/Minaee2022.pdf
paper_type: survey
pillars: [geral, P4]
status: fichado
proposes: []
uses_methods: [deep-learning]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: [transformers]
extends: [Kowsari2019]
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "O survey moderno (CSUR 2022, 150+ modelos) da classificação de texto
           por deep learning: citação-síntese para 'DL superou o clássico' no
           Cap.2, liberando espaço textual (mesma tática do Kowsari p/ clássico)."
---

# Deep Learning–based Text Classification: A Comprehensive Review

## Resumo
ACM CSUR 2022: revisão de mais de 150 modelos de deep learning para classificação
de texto (sentimento, categorização de notícias, QA, NLI), com comparação em 40+
benchmarks. Constata que modelos profundos superaram as abordagens clássicas de
ML nas tarefas de classificação de texto.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | DL superou ML clássico em classificação de texto (150+ modelos, 40+ benchmarks) | Abstract | Cap.2: a frase-síntese da transição clássico→profundo com uma única citação |

## Números que posso citar
- 150+ modelos revisados; 40+ benchmarks.

## Crítica / limitações (minha leitura)
- Não cobre o regime rotulagem-cara (nosso foco); benchmarks com rótulos fartos.

## Ideias que gera para a tese
- Par com Karl2023: Minaee (geral) + Karl (texto curto) fecham a justificativa do
  BERTimbau em duas citações.
