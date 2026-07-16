---
id: Kowsari2019
title: "Text Classification Algorithms: A Survey"
authors: ["Kowsari, Kamran", "Jafari Meimandi, Kiana", "Heidarysafa, Mojtaba", "Mendu, Sanjana", "Barnes, Laura", "Brown, Donald"]
year: 2019
venue: "Information, 10(4), 150 (MDPI)"
doi: "10.3390/info10040150"
pdf: referencias-pdf/Kowsari2019.pdf
paper_type: survey
pillars: [geral]
status: fichado
proposes: [pipeline-de-4-fases-da-classificacao-de-texto]
uses_methods: [extracao-de-atributos, reducao-de-dimensionalidade]
datasets: []
metrics: [acuracia, f1, matriz-de-confusao]
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Survey-guarda-chuva da classificação de texto: fornece o vocabulário do
           pipeline (extração de atributos → redução → classificador → avaliação)
           usado na fundamentação, e as métricas de avaliação padrão."
---

# Text Classification Algorithms: A Survey

## Resumo
Survey amplo (68 páginas) de algoritmos de classificação de texto. Estrutura o
campo decompondo os sistemas em **quatro fases**: extração de atributos, redução
de dimensionalidade, seleção do algoritmo de classificação e avaliação. Cobre
representações (BoW, TF-IDF, embeddings), famílias de classificadores (de Rocchio
e Naive Bayes a deep learning) e métodos de avaliação, discutindo limitações de
cada técnica e aplicações reais. Posição no tempo: captura a transição
pré-transformers (2019), com deep learning já dominante mas BERT ainda recente.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Sistemas de classificação de texto decompõem-se em 4 fases padronizadas | Abstract/§1 | Organização da seção de fundamentos do Cap.2 (já portada do draft — conferir consistência terminológica) |
| C2 | O sucesso dos algoritmos depende da capacidade de capturar relações não-lineares complexas | Abstract | Transição argumentativa para representações profundas no Cap.2 |

## Números que posso citar
- (Survey; fonte de definições e taxonomia, não de números.)

## Crítica / limitações (minha leitura)
- Pré-BERT na prática; várias seções (redução de dimensionalidade clássica) hoje
  têm peso menor — no rework do Cap.2 (condensação de ~75% da parte de ML), este
  é o tipo de material a resumir agressivamente, mantendo só o que ancora o
  pipeline e as métricas.

## Ideias que gera para a tese
- Usar C1 como espinha da (curta) seção de fundamentos de classificação do Cap.2
  reescrito, citando este survey uma vez em vez de detalhar algoritmo a algoritmo.
