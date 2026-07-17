---
id: Zhao2017DeepALShortText
title: "Deep Active Learning for Short-Text Classification"
authors: ["Zhao, Wenquan"]
year: 2017
venue: "Dissertação de mestrado, KTH Royal Institute of Technology, Estocolmo"
doi: ""
pdf: referencias-pdf/Zhao2017DeepALShortText.pdf
paper_type: dissertacao
pillars: [geral, P2]
status: fichado
proposes: []
uses_methods: [deep-active-learning, cnn, amostragem-por-incerteza]
datasets: []
metrics: [acuracia]
tasks: [classificacao-de-texto-curto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Precedente direto da COMBINAÇÃO da tese: deep AL aplicado
           especificamente a texto curto (2017, era CNN). Mostra que a interseção
           já era reconhecida como problema próprio antes dos transformers — o
           FALCO a revisita com BERTimbau e oráculo LLM."
---

# Deep Active Learning for Short-Text Classification (Zhao, 2017)

## Resumo
Dissertação de mestrado (KTH, 2017, 42 pp.) que aplica aprendizado ativo profundo
à classificação de **texto curto** — a mesma interseção de domínio da tese, na
era pré-transformer (classificadores convolucionais/recorrentes). Investiga
estratégias de seleção sobre redes profundas para reduzir a necessidade de
anotação em textos curtos, atacando simultaneamente a esparsidade do texto curto
e o apetite por dados das redes profundas.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL profundo aplicado a texto curto já era objeto de estudo dedicado em 2017 | Título/escopo | Cap.2: a interseção AL×STC não é vazia — nossa lacuna específica é AL×STC×LLM-oráculo×português, e este trabalho ajuda a delimitá-la com precisão |

## Números que posso citar
- (Extrair números específicos das seções de resultados se a comparação for
  citada; uso principal é posicionamento de lacuna.)

## Crítica / limitações (minha leitura)
- Era CNN: sem pré-treinados, sem LLM, inglês; oráculo humano implícito.
- Dissertação de mestrado com escopo limitado — citar como precedente da
  interseção, não como estado da arte.

## Ideias que gera para a tese
- Na tabela de lacunas do Cap.2 (Seção da revisão sistemática), incluir linha
  Zhao 2017: AL✓ STC✓ LLM✗ PT✗ — evidencia visualmente o que só o FALCO cobre.
