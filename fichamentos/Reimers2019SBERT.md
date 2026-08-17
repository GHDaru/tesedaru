---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Reimers2019SBERT
title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
authors: ["Reimers, Nils", "Gurevych, Iryna"]
year: 2019
venue: "EMNLP-IJCNLP 2019"
doi: "10.18653/v1/D19-1410"
pdf: referencias-pdf/Reimers2019SBERT.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: metodo
pillars: [P1, P2]
status: fichado

# ===== ENTIDADES =====
proposes: [sentence-bert]
uses_methods: [fine-tuning, selecao-por-similaridade]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: [sentence-bert, bert, roberta]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Devlin2019]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: DRI-SL
    note: "é o codificador de sentenças da densidade semântica: o DRI-SL projeta as instâncias com SBERT e agrupa por k-médias, o que só é viável porque este artigo torna a similaridade de sentenças comparável por cosseno"
---

# Sentence-BERT

**Lida na fonte** (EMNLP 2019, 11 pp.), identidade conferida.

## O que a tese usa desta obra

O Cap. 3 projeta as instâncias com "um codificador de sentenças
\citep{Reimers2019SBERT}" e agrupa por $k$-médias — é o primeiro dos dois
espaços de representação do DRI-SL.

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A construção do BERT o torna **inadequado** para busca por similaridade semântica e para tarefas não supervisionadas como agrupamento | Resumo, p. 1 | Cap. 3 — é a razão de existir um codificador de sentenças no DRI-SL, em vez de usar o BERT direto |
| C2 | O SBERT produz \textit{embeddings} de sentença **comparáveis por cosseno**, mantendo a acurácia do BERT | Resumo, p. 1 | Cap. 3 e Apêndice do DRI-SL — sustenta agrupar por $k$-médias no espaço do codificador |
| C3 | O custo de achar o par mais similar cai de **~65 horas** (BERT/RoBERTa) para **~5 segundos** (SBERT) | Resumo, p. 1 | Cap. 3 — número citável para justificar a viabilidade computacional da fase 1 |

## Números que posso citar

- **65 horas → ~5 segundos** para encontrar o par mais similar em uma coleção,
  mantendo a acurácia do BERT (Resumo, p. 1). Condição: é o experimento de
  busca de par mais similar do próprio artigo, em inglês; a ordem de grandeza é
  o que transfere, não o tempo absoluto.

## Citação direta (com página)

> "The construction of BERT makes it unsuitable for semantic similarity search as
> well as for unsupervised tasks like clustering. … [SBERT] reduces the effort
> for finding the most similar pair from 65 hours with BERT / RoBERTa to about 5
> seconds with SBERT, while maintaining the accuracy from BERT." (p. 1)

## ACHADO de citação: "SBERT multilíngue" não é esta obra

O Apêndice do DRI-SL diz "SBERT **multilíngue** \citep{Reimers2019SBERT}".
**Medi: a palavra "multilingual" aparece ZERO vezes neste artigo.** O SBERT de
2019 é treinado e avaliado em **inglês** (SNLI, MultiNLI, STS).

O modelo multilíngue vem de **outra obra dos mesmos autores** — Reimers &
Gurevych, *Making Monolingual Sentence Embeddings Multilingual using Knowledge
Distillation*, EMNLP 2020 —, que é quem introduz a destilação entre línguas e os
modelos `paraphrase-multilingual-*`. **Essa entrada não está no nosso
`referencias.bib`** (conferi).

Isso não é preciosismo: a tese roda em **português**, e a propriedade que
sustenta a fase 1 do DRI-SL é justamente a multilinguidade. Atribuí-la ao artigo
de 2019 deixa a decisão de método sem lastro exatamente no ponto em que a banca
vai olhar. **Recomendação:** acrescentar a obra de 2020 ao `.bib` (superfície do
revisor1) e citá-la onde se fala em "SBERT multilíngue", mantendo o `2019` onde
se fala do codificador e do cosseno. Fico com o fichamento dela assim que a
entrada existir.

## Crítica / limitações (minha leitura)

Além do ponto acima, o artigo avalia similaridade semântica e transferência, não
**seleção de conjunto inicial** — o uso da tese é uma aplicação legítima do
espaço de representação, mas a evidência de que esse espaço serve para escolher
$L_0$ é **nossa**, medida no P1, e não herdada daqui.
