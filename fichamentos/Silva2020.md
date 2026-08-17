---
id: Silva2020
title: "Towards automatically filtering fake news in Portuguese"
authors: ["Silva, Renato M.", "Santos, Roney L. S.", "Almeida, Tiago A.", "Pardo, Thiago A. S."]
year: 2020
venue: "Expert Systems With Applications, 146, 113199"
doi: "10.1016/j.eswa.2020.113199"
pdf: referencias-pdf/Silva2020.pdf
paper_type: avaliacao
pillars: [geral]
status: fichado
proposes: [corpus-fakebr]
uses_methods: [classificadores-classicos, avaliacao-comparativa]
datasets: [fake-br-corpus]
metrics: [f1]
tasks: [classificacao-de-texto, deteccao-de-fake-news]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Classificação de texto EM PORTUGUÊS com construção de corpus (UFSCar/
           NILC-USP): exemplo de referência nacional de pipeline completo
           corpus→classificação — espelho do par dataset (Daru2022) + tese."
---

# Towards automatically filtering fake news in Portuguese

## Resumo
Trabalho NILC/UFSCar (ESWA 2020) sobre filtragem automática de fake news em
português, incluindo construção de corpus e avaliação comparativa de métodos de
categorização de texto. Interessa como caso nacional de classificação de texto
com corpus próprio.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Classificação de texto em português com corpus dedicado é linha ativa nacional | Escopo | Cap.2: bloco de PLN em português (com Souza2020BERTimbau, Souza2023, Bard) |

## Números que posso citar
- (Fora do nosso domínio; qualitativo.)

## Crítica / limitações (minha leitura)
- Domínio distinto (notícias, texto longo); citar só no bloco de português.

## Ideias que gera para a tese
- Compõe o parágrafo "classificação de texto em português" do Cap.2.
