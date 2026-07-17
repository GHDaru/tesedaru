---
id: Deerwester1990
title: "Indexing by Latent Semantic Analysis"
authors: ["Deerwester, Scott", "Dumais, Susan T.", "Furnas, George W.", "Landauer, Thomas K.", "Harshman, Richard"]
year: 1990
venue: "Journal of the American Society for Information Science, 41(6), pp. 391–407"
doi: "10.1002/(SICI)1097-4571(199009)41:6<391::AID-ASI1>3.0.CO;2-9"
pdf: referencias-pdf/Deerwester1990.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [lsa, indexacao-semantica-latente]
uses_methods: [svd, fatoracao-matricial]
datasets: []
metrics: []
tasks: [recuperacao-de-informacao]
models: []
extends: [Salton1988]
compares_with: []
contradicts: []
builds_on: [Salton1988]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Primeiro passo esparso→denso (SVD sobre termo-documento): ancestral
           conceitual dos embeddings; na linha do Cap.2 fica entre TF-IDF e
           word2vec. Ataca sinonímia/polissemia — os problemas centrais do texto
           curto de varejo (CERV vs cerveja)."
---

# Indexing by Latent Semantic Analysis

## Resumo
Artigo fundador da LSA: decompõe a matriz termo-documento por SVD truncada,
projetando termos e documentos num espaço latente de menor dimensão em que a
similaridade captura relações semânticas indiretas (documentos podem ser
similares sem compartilhar termos). Mitiga sinonímia e, parcialmente, polissemia
— as duas fraquezas estruturais da correspondência lexical exata.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Projeção em espaço latente captura similaridade sem sobreposição lexical | Escopo | Cap.2: motivação histórica de representações densas; o problema (CERV≠cerveja lexicalmente) é o nosso |

## Números que posso citar
- (Clássico conceitual.)

## Crítica / limitações (minha leitura)
- Linear e global; superado por embeddings contextuais — citar só como elo
  histórico esparso→denso.

## Ideias que gera para a tese
- Um parágrafo-linha-do-tempo no Cap.2: Salton (1988, pesos) → Deerwester (1990,
  latente) → Mikolov/Pennington (2013-14, embeddings) → Vaswani (2017, atenção) →
  Devlin (2019, BERT) → Souza (2020, BERTimbau). Seis citações, um parágrafo.
