---
id: Zhang2016ShortText
title: "Improving short text classification by learning vector representations of both words and hidden topics"
authors: ["Zhang, Heng", "Zhong, Guoqiang"]
year: 2016
venue: "Knowledge-Based Systems, 102, pp. 76–86"
doi: "10.1016/j.knosys.2016.03.027"
pdf: referencias-pdf/Zhang2016ShortText.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [vetores-conjuntos-palavra-topico]
uses_methods: [topic-models, embeddings, enriquecimento-com-corpus-externo]
datasets: []
metrics: [acuracia]
tasks: [classificacao-de-texto-curto]
models: []
extends: []
compares_with: [Song2014]
contradicts: []
builds_on: [Song2014, Mikolov2013]
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Linha de enriquecimento para texto curto (vetores de palavras + tópicos
           ocultos aprendidos com coleção externa): a resposta pré-LLM à
           esparsidade. O expanded_description do nosso prompt é o herdeiro dessa
           linha com conhecimento paramétrico."
---

# Improving short text classification by learning word and hidden-topic vectors

## Resumo
Framework para classificação de texto curto que aprende conjuntamente
representações vetoriais de palavras E de tópicos ocultos, usando coleção externa
de larga escala para enriquecer o sinal — ataque direto à esparsidade do texto
curto via semântica auxiliar (Knowledge-Based Systems, 2016).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Enriquecer texto curto com tópicos aprendidos de corpus externo melhora a classificação | Abstract | Cap.2 (STC, linha de enriquecimento): elo entre enriquecimento por ontologia (Song 2014) e por LLM (nosso prompt v3) |

## Números que posso citar
- (Benchmarks de STC da época; qualitativo.)

## Crítica / limitações (minha leitura)
- Pré-transformer; pipeline de tópicos frágil comparado a embeddings contextuais.

## Ideias que gera para a tese
- Na seção de STC do Cap.2, apresentar a linha de enriquecimento em 3 gerações:
  ontologias (2014) → tópicos/vetores (2016) → conhecimento paramétrico de LLM
  (2023+, nosso expanded_description).
