---
id: Javed2018
title: "Normalization of Unstructured and Informal Text in Sentiment Analysis"
authors: ["Javed, Muhammad", "Kamal, Shahid"]
year: 2018
venue: "IJACSA, 9(10)"
doi: ""
pdf: referencias-pdf/Javed2018.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [normalizacao-de-texto-informal]
uses_methods: [normalizacao-lexical]
datasets: [microblogs]
metrics: []
tasks: [analise-de-sentimento, normalizacao]
models: []
extends: []
compares_with: [Bard2019Normalizador]
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Normalização de texto informal como etapa prévia: paralela ao nosso
           problema de abreviações de varejo (CERV→cerveja). No FALCO essa
           normalização é DELEGADA ao LLM (expanded_description) em vez de a um
           módulo dedicado. (Arquivo veio rotulado como Han 2011; identidade
           corrigida no saneamento.)"
---

# Normalization of Unstructured and Informal Text in Sentiment Analysis

## Resumo
Trata a normalização de texto informal/não-estruturado (microblogs) como etapa
que precede o processamento usual em análise de sentimento, convertendo a
escrita do usuário para formato padrão. O problema (texto fora da norma quebra
os pipelines) é o mesmo das descrições abreviadas de varejo.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Texto informal exige normalização prévia para o restante do pipeline funcionar | Abstract | Cap.2: motivação da linha de normalização; contraste com a delegação ao LLM no FALCO |

## Números que posso citar
- (Qualitativo.)

## Crítica / limitações (minha leitura)
- Sentimento/microblog em inglês/urdu; periférico — citar em bloco.

## Ideias que gera para a tese
- Par com Bard2019Normalizador: normalização dedicada (clássica) vs implícita no
  oráculo (nossa) — meia página no Cap.2.
