---
id: Ahmed2022
title: "Short Text Clustering Algorithms, Application and Challenges: A Survey"
authors: ["Ahmed, Majid Hameed", "Tiun, Sabrina", "Omar, Nazlia", "Sani, Nor Samsiah"]
year: 2023
venue: "Applied Sciences 13(1):342 (MDPI), 38 pp."
doi: "10.3390/app13010342"
pdf: referencias-pdf/Ahmed2022.pdf
paper_type: survey
pillars: [p2-texto-curto]
status: fichado
uses_methods: [agrupamento-de-texto-curto, reducao-de-dimensionalidade, medida-de-similaridade, expansao-de-corpus]
tasks: [agrupamento-de-texto]
falco_relation:
  - type: fundamenta
    target: texto-curto
    note: "Fonte de revisão para os desafios do regime de texto curto que o Cap. 2
           enumera: escassez de informação/contexto, esparsidade de representação e
           alta dimensionalidade, ruído e informalidade. O survey trata o problema
           do lado do AGRUPAMENTO, mas os desafios que enumera são da natureza do
           texto curto, não da tarefa — ver a ressalva abaixo."
---

# Short Text Clustering Algorithms, Application and Challenges: A Survey (Ahmed et al., Appl. Sci. 2023)

## Nota de identidade — chave `Ahmed2022`, obra de **2023**
O PDF traz na primeira página: *"Appl. Sci. **2023**, 13, 342"*, recebido em
19/10/2022, publicado em **27/12/2022**, com volume datado de 2023. A entrada
do `.bib` já diz `year={2023}`; a **chave** `Ahmed2022` permanece, porque chave
é identificador interno e renomear obrigaria a mexer no `.tex`. Fica
registrado para ninguém "corrigir" o ano de volta.

## Resumo
Revisão de algoritmos de **agrupamento** (clustering) de texto curto: por que o
regime é difícil, como representar o documento, como reduzir dimensionalidade,
como medir similaridade e como avaliar. O fio condutor é que o texto curto
"sofre de falta de informação e esparsidade", e que as técnicas de agrupamento
tradicionais ficam insatisfatórias nesse regime. Levanta a literatura em cinco
bases (IEEE Xplore, Web of Science, ScienceDirect, Scopus, Google Scholar).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Texto curto "sofre de **falta de informação e esparsidade**" e precisa de análise própria | Resumo, p. 1 | 2.4 — sustenta "escassez de contexto" e "esparsidade lexical" |
| C2 | A comunidade se concentrou em superar "os problemas de **esparsidade, dimensionalidade e falta de informação**" | Resumo, p. 1 | 2.4 — os três desafios, na palavra da fonte |
| C3 | O texto curto "normalmente contém **ruído, gíria, emojis, erros de grafia, abreviações e erros gramaticais**" | §1, p. 2 | 2.4 — sustenta "ruído e informalidade" |
| C4 | A esparsidade decorre de cada documento curto conter poucas palavras, e é agravada pelo pequeno número de co-ocorrências entre palavras | §2, p. 4 | 2.4 — dá o MECANISMO da esparsidade, não só o rótulo |
| C5 | Aplicações listadas: personalização no Twitter, **análise de sentimento**, filtragem de spam, avaliações de clientes | Resumo, p. 1 | 2.4 — ver ressalva |

## Números que posso citar
- **38 páginas**; revisão sobre cinco bases bibliográficas (Resumo, p. 1).
- Escala do fenômeno, citada pelos autores: Twitter gera **500 milhões de
  tuítes por dia** (§1, p. 2).

## Citações diretas (com página)
> "short text suffers from lack of information and sparsity" (p. 1)

> "which typically contains noise, slang, emojis, misspellings, abbreviations
> and grammatical errors" (p. 2)

## RESSALVA: é um survey de AGRUPAMENTO, e a tese o cita ao falar de classificação
Medido no texto completo das 38 páginas:
- **"classification" aparece 2 vezes** (pp. 18 e 25). O objeto do artigo é
  *short text clustering* (STC) — tarefa **não supervisionada**.
- "sentiment analysis" aparece 4 vezes (pp. 1, 35, 38); **"categorização de
  catálogos" não aparece** em forma alguma.
- **"curse of dimensionality" aparece 0 vezes**; o que há é o tratamento de
  *dimensionality* (32 ocorrências) e um capítulo de redução de
  dimensionalidade.

Onde isso toca a tese, com as duas citações medidas:
1. Cap. 2: *"sua **classificação** sustenta aplicações de análise de sentimento
   a categorização de catálogos \cite{Ahmed2022, Song2014}"* — o Ahmed sustenta
   **análise de sentimento** (literal) e as aplicações de texto curto em geral,
   mas **não** trata de classificação e **não** menciona catálogos. Conserto
   barato, sem remover ninguém: falar de *processamento* de texto curto, ou
   deixar o `Song2014` responder pela parte de classificação.
2. Cap. 2: os quatro desafios do regime — **batem** (C1-C4), com uma exceção de
   vocabulário: "maldição da dimensionalidade" é expressão da tese, não da
   fonte. A alta dimensionalidade está lá; o nome consagrado, não. Se a banca
   for literal, a expressão precisa de outra referência (ou de nenhuma: é termo
   clássico e dispensável de citação).

**Não é caso de retirar a citação.** É caso de ajustar uma palavra, e a decisão
é do principal — a prosa é dele.

## O que esta obra NÃO sustenta
1. **Não sustenta afirmação sobre classificação supervisionada** (ver ressalva).
2. **Não mede nada em português.** Os conjuntos e exemplos são de inglês e de
   redes sociais.
3. **Não tem experimento próprio.** É revisão: reporta o que outros mediram.

## Ideias que gera para a tese
1. O survey é a fonte natural para a frase "o regime é difícil" **do lado da
   representação**, que é onde o DRI-SL atua: se a esparsidade vem de poucas
   palavras e poucas co-ocorrências (C4), então usar embeddings pré-treinados
   é resposta direta ao mecanismo, e não só uma escolha de conveniência.
