---
id: Pawlowski2022
title: "Machine Learning Based Product Classification for eCommerce"
authors: ["Pawłowski, Mieczysław"]
year: 2022
venue: "Journal of Computer Information Systems, 62(4), pp. 730–739"
doi: "10.1080/08874417.2021.1910880"
pdf: referencias-pdf/Pawlowski2022.pdf
paper_type: avaliacao
pillars: [geral]
status: fichado
proposes: []
uses_methods: [classificadores-classicos, avaliacao-comparativa]
datasets: [catalogo-e-commerce]
metrics: [acuracia]
tasks: [classificacao-de-produtos-e-servicos]
models: []
extends: []
compares_with: [Paulucio2020, Hafez2021]
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Mais uma confirmação (sistemas de informação, 2022) de que classificar
           produtos de e-commerce por texto é problema industrial ativo — compõe
           o bloco de relevância aplicada do Cap.1 com Paulucio, Hafez e Tan."
---

# Machine Learning Based Product Classification for eCommerce

## Resumo
Artigo de sistemas de informação (JCIS) avaliando abordagens de aprendizado de
máquina para classificação de produtos em e-commerce a partir de informação
textual do catálogo. Compõe, com Paulucio (2020), Hafez (2021) e Tan (2020), o
conjunto de evidências de que a categorização automática de produtos é demanda
industrial recorrente, atacada com pipelines supervisionados clássicos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Classificação de produto em e-commerce é problema industrial ativo tratado com ML supervisionado | Título/escopo | Cap.1 (relevância aplicada), citação em bloco com os demais do domínio |

## Números que posso citar
- (Extrair da seção de resultados apenas se necessário; uso em bloco qualitativo.)

## Crítica / limitações (minha leitura)
- Supervisionado clássico com rótulos dados; sem custo de anotação, sem
  português, sem texto curto extremo — utilidade limitada a contexto.

## Ideias que gera para a tese
- Citar em bloco no Cap.1: \citep{Paulucio2020, Hafez2021, Tan2020, Pawlowski2022}
  para relevância industrial, sem gastar mais de um parágrafo.
