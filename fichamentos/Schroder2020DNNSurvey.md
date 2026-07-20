---
id: Schroder2020DNNSurvey
title: "A Survey of Active Learning for Text Classification using Deep Neural Networks"
authors: ["Schröder, Christopher", "Niekler, Andreas"]
year: 2020
venue: "arXiv:2008.07267"
doi: ""
pdf: referencias-pdf/Schroder2020DNNSurvey.pdf
paper_type: survey
pillars: [geral, P2, P4]
status: fichado
proposes: [taxonomia-data-model-prediction-based]
uses_methods: [deep-active-learning, embeddings, modelo-de-linguagem]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []
extends: [Olsson2009]
compares_with: [Ren2021, zhang2022surveyAL]
contradicts: []
builds_on: [Olsson2009, Lewis1994]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Survey específico da NOSSA interseção (AL × classificação de texto ×
           DNNs). Nomeia os dois bloqueios históricos — incerteza mal calibrada
           de NNs e treino com poucos dados — que o FALCO contorna com
           pré-treinados (BERTimbau) e fases guiadas por estratégia."
---

# A Survey of Active Learning for Text Classification using DNNs

## Resumo
Survey (arXiv 2020) da interseção exata AL × classificação de texto × redes
profundas. Diagnóstico de por que NNs eram pouco usadas em AL apesar da
popularidade: **(a) incapacidade de fornecer estimativas de incerteza confiáveis**
(das quais as estratégias de consulta mais comuns dependem) e **(b) dificuldade
de treinar DNNs com poucos dados**. Constrói uma taxonomia de estratégias de
consulta em **data-based, model-based e prediction-based**, revisa avanços de PLN
(word embeddings, modelos de linguagem) no contexto de AL e analisa lacunas dos
trabalhos recentes.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Dois bloqueios históricos de AL+DNN: incerteza não confiável e treino em small data | Abstract | Cap.2: por que o par (pré-treinado + fine-tuning) destravou o DeepAL; motiva BERTimbau no E2 |
| C2 | Taxonomia data/model/prediction-based complementa a de informatividade/representatividade | Abstract | Cap.2: usar como segunda dimensão da tabela de estratégias (cruzar com a taxonomia de Zhang et al. 2022) |
| C3 | Com AL+NN: mais desempenho com os mesmos dados, ou mesmos resultados com menos anotação | Abstract | Formulação exata do objetivo de eficiência que a LCE quantifica |

## Números que posso citar
- (Survey; taxonomia e diagnóstico, sem números próprios.)

## Crítica / limitações (minha leitura)
- 2020: anterior aos LLMs-como-oráculo; incerteza tratada só do lado do
  classificador — a incerteza/confiabilidade DO ORÁCULO (nosso E0/E4) não aparece.
- Dos mesmos autores do small-text (Schroder2021SmallText): a dupla
  survey+biblioteca é o espelho metodológico do nosso par tese+activelearning.

## Ideias que gera para a tese
- Citar C1 ao justificar por que as fases iniciais do FALCO não confiam em
  incerteza pura do classificador recém-treinado (cold start + incerteza mal
  calibrada) e usam densidade/aleatório antes de migrar para incerteza.
