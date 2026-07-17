---
id: Bard2019Normalizador
title: "Normalizador de Texto para Língua Portuguesa baseado em Modelo de Linguagem"
authors: ["Bard, Patrick Thiago", "Lopes Luis, Renan", "Moraes, Silvia Maria Wanderley"]
year: 2019
venue: "STIL (Symposium in Information and Human Language Technology) — edição a confirmar"
doi: ""
pdf: referencias-pdf/Bard2019Normalizador.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [normalizador-portugues-por-lm]
uses_methods: [modelo-de-linguagem, normalizacao]
datasets: []
metrics: []
tasks: [normalizacao]
models: []
extends: []
compares_with: [Javed2018]
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Normalização de texto informal PARA PORTUGUÊS via modelo de linguagem
           (PUCRS): precedente nacional da ideia de usar LM para padronizar texto
           fora da norma — que o FALCO leva ao extremo com o expanded_description
           do oráculo LLM."
---

# Normalizador de Texto para Língua Portuguesa baseado em Modelo de Linguagem

## Resumo
Protótipo de normalizador para português (PUCRS) que converte texto informal
gerado por usuários em escrita padrão usando modelo de linguagem — etapa prévia
ao processamento usual. Interessa como precedente em português da normalização
baseada em LM.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | LM pode padronizar texto informal em português | Abstract | Cap.2: elo nacional entre normalização clássica e a expansão de abreviações via LLM do prompt v3 |

## Números que posso citar
- (Protótipo; qualitativo.)

## Crítica / limitações (minha leitura)
- LM pré-transformer, protótipo; ano/edição do STIL a confirmar (metadado
  incompleto no PDF — anotado no .bib).

## Ideias que gera para a tese
- Meia página do Cap.2 sobre normalização em português: Branco2012 (contexto),
  Bard (LM dedicado), FALCO (LLM embutido no oráculo).
