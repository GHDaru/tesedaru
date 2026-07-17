---
id: MaslejKresnakova2020
title: "Comparison of Deep Learning Models and Various Text Pre-Processing Techniques for the Toxic Comments Classification"
authors: ["Maslej-Krešňáková, Viera", "Sarnovský, Martin", "Butka, Peter", "Machová, Kristína"]
year: 2020
venue: "Applied Sciences, 10(23), 8631"
doi: "10.3390/app10238631"
pdf: referencias-pdf/MaslejKresnakova2020.pdf
paper_type: avaliacao
pillars: [geral]
status: fichado
proposes: []
uses_methods: [deep-learning, pre-processamento]
datasets: [toxic-comments]
metrics: [f1]
tasks: [classificacao-de-texto-curto]
models: []
extends: []
compares_with: [Naseem2021HateSpeech]
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Cruza modelos DL × técnicas de pré-processamento em comentários
           (texto curto informal): evidência de que a INTERAÇÃO representação ×
           pré-processamento importa. (Arquivo veio rotulado como 'Torfi 2020';
           identidade corrigida no saneamento.)"
---

# Comparison of DL Models and Text Pre-Processing for Toxic Comments

## Resumo
Applied Sciences 2020 (TU Košice): compara modelos de deep learning combinados a
diferentes técnicas de pré-processamento na classificação de comentários tóxicos
— texto curto informal. Mostra que a escolha de pré-processamento interage com a
arquitetura (o que é ótimo para um modelo não é para outro).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Pré-processamento e arquitetura interagem em texto curto informal | Escopo | Cap.2: apoio à decisão de pipeline mínimo + validação empírica própria (E2) em vez de receita universal |

## Números que posso citar
- (Qualitativo.)

## Crítica / limitações (minha leitura)
- Comentários tóxicos ≠ descrições de produto; inglês.

## Ideias que gera para a tese
- Citar com Naseem2021HateSpeech no par "pré-processamento em texto curto".
