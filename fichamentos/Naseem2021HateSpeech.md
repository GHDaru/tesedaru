---
id: Naseem2021HateSpeech
title: "A survey of pre-processing techniques to improve short-text quality: a case study on hate speech detection on Twitter"
authors: ["Naseem, Usman", "Razzak, Imran", "Eklund, Peter W."]
year: 2021
venue: "Multimedia Tools and Applications, 80, pp. 35239–35266"
doi: "10.1007/s11042-020-10082-6"
pdf: referencias-pdf/Naseem2021HateSpeech.pdf
paper_type: survey
pillars: [geral]
status: fichado
proposes: []
uses_methods: [pre-processamento, avaliacao-de-12-tecnicas]
datasets: [twitter-hate-speech]
metrics: [acuracia, f1]
tasks: [classificacao-de-texto-curto]
models: []
extends: [song2014shorttext]
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Evidência de que o pré-processamento tem impacto considerável e é
           SUBEXPLORADO em texto curto — sustenta a seção de pré-processamento do
           Cap.2 e a decisão de pipeline mínimo e documentado da tese."
---

# A survey of pre-processing techniques to improve short-text quality

## Resumo
Análise de **doze técnicas de pré-processamento** para texto curto (estudo de
caso: detecção de discurso de ódio no Twitter). Tese central: o pré-processamento
é essencial para desambiguar texto curto e tem impacto considerável no
desempenho, mas é menos explorado que extração de atributos e classificação.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Pré-processamento tem impacto considerável e é subexplorado em texto curto | Abstract | Cap.2 (pré-processamento em STC); justifica documentarmos o pipeline mínimo (minúsculas+acentos) como decisão, não default |

## Números que posso citar
- 12 técnicas avaliadas em 3 classificadores (detalhar só se necessário).

## Crítica / limitações (minha leitura)
- Twitter/inglês; várias técnicas (correção ortográfica, emojis) não se aplicam
  a descrições de produto em caixa alta.

## Ideias que gera para a tese
- Citar ao lado de Uysal & Gunal (2014) — cuja versão em PDF ainda falta —
  como o par de referências de impacto de pré-processamento.
