---
id: Schroder2021SmallText
title: "Small-Text: Active Learning for Text Classification in Python"
authors: ["Schröder, Christopher", "Müller, Lydia", "Niekler, Andreas", "Potthast, Martin"]
year: 2021
venue: "arXiv:2107.10314 (posteriormente EACL 2023 System Demonstrations)"
doi: ""
pdf: referencias-pdf/Schroder2021SmallText.pdf
paper_type: ferramenta
pillars: [P4, geral]
status: fichado
proposes: [biblioteca-small-text]
uses_methods: [pool-based, estrategias-de-consulta, criterio-de-parada]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: [transformers]
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994, zhang2022surveyAL]
falco_relation:
  - type: compara-ferramenta
    target: FALCO
    note: "Referência de engenharia para a biblioteca activelearning da tese:
           mesma decomposição (classificador × estratégia × critério de parada
           com interfaces padronizadas). Nossa biblioteca difere ao elevar o
           ORÁCULO a porta de primeira classe (custo, cache, modos de saída) —
           ausente no small-text, que assume rótulos dados."
---

# Small-Text: Active Learning for Text Classification in Python

## Resumo
Artigo de sistema (7 pp.) apresentando **small-text**, biblioteca Python de AL
pool-based para classificação de texto mono e multi-rótulo. Oferece estratégias
de consulta estado-da-arte pré-implementadas (algumas com GPU), e **interfaces
padronizadas que permitem combinar classificadores, estratégias de consulta e
critérios de parada** ("mix and match"), integrando scikit-learn, PyTorch e
HuggingFace transformers como extensões opcionais. MIT, público no GitHub
(webis-de/small-text). Motivação: rotular é caro; AL seleciona repetidamente os
não-rotulados mais informativos segundo uma query strategy.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A tríade (classificador, estratégia, critério de parada) com interfaces padronizadas é a decomposição correta de um sistema de AL | Abstract | Valida a arquitetura de ports do activelearning (QueryStrategy/Trainer/StoppingCriterion); citar no Cap.3 e no apêndice da biblioteca |
| C2 | Integração transformers+AL pronta para uso, GPU opcional | Abstract | Precedente para o par small-text↔BERTimbau; nosso E2 se apoia na mesma pilha HF |

## Números que posso citar
- (Artigo de sistema, sem resultados empíricos; citar como ferramenta/arquitetura.)

## Crítica / limitações (minha leitura)
- O oráculo é implícito (rótulos simplesmente aparecem): sem custo por consulta,
  sem ruído, sem lote de anotação, sem observabilidade — as abstrações centrais
  do FALCO (OracleUsage, Annotation com invalid_label, Budget) não têm análogo.
- Por que não usamos small-text direto: a tese exige exatamente o que falta nele
  (instrumentação do oráculo LLM); argumentar isso no apêndice a4 evita a
  pergunta óbvia da banca ("por que reinventar?").

## Ideias que gera para a tese
- Apêndice a4 (biblioteca): tabela small-text vs activelearning por porta —
  o delta é a camada de oráculo instrumentado, não as estratégias.
