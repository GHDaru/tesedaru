---
id: Hafez2021
title: "Classification of Retail Products: From Probabilistic Ranking to Neural Networks"
authors: ["Hafez, Manar Mohamed", "Fernández Vilas, Ana", "Díaz Redondo, Rebeca P.", "Olivera Pazó, Héctor"]
year: 2021
venue: "Applied Sciences, 11(9), 4117 (MDPI)"
doi: "10.3390/app11094117"
pdf: referencias-pdf/Hafez2021.pdf
paper_type: avaliacao
pillars: [geral]
status: fichado
proposes: []
uses_methods: [ranking-probabilistico, redes-neurais]
datasets: [catalogo-varejo]
metrics: [acuracia]
tasks: [classificacao-de-produtos-e-servicos, classificacao-de-texto-curto]
models: []
extends: []
compares_with: [Paulucio2020, Pawlowski2022]
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Espectro probabilístico→neural no MESMO problema de varejo: espelha a
           progressão de classificadores da tese (PVBin probabilístico →
           BERTimbau neural) em literatura independente."
---

# Classification of Retail Products: From Probabilistic Ranking to Neural Networks

## Resumo
Estudo (Applied Sciences 2021, grupo AtlanTTic/Vigo) de classificação de produtos
de varejo comparando o espectro de abordagens **de ranking probabilístico a redes
neurais** sobre dados de catálogo. Relevante pela paridade estrutural com a tese:
a mesma progressão leve→neural que adotamos (PVBin → BERTimbau), aplicada ao
mesmo tipo de dado (descrições de produtos de varejo).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O espectro probabilístico→neural é o eixo natural de comparação em classificação de produtos de varejo | Título/escopo | Justifica o par de classificadores da tese (PVBin probabilístico vs BERTimbau) como desenho padrão do domínio |

## Números que posso citar
- (Extrair se necessário; uso principal estrutural/contextual.)

## Crítica / limitações (minha leitura)
- Supervisão completa, sem custo de rotulagem; não português.

## Ideias que gera para a tese
- No Cap.3, ao justificar os DOIS classificadores (leve+neural), citar Hafez como
  precedente do espectro no varejo.
