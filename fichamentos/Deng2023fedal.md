---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Deng2023fedal
title: "Federated Active Learning Framework for Efficient Annotation Strategy in Skin-Lesion Classification"
authors: ["Deng, Zhipeng", "Yang, Yuqiao", "Suzuki, Kenji"]
year: 2025
venue: "Journal of Investigative Dermatology, v. 145, n. 2, p. 303-311 (preprint arXiv:2406.11310, jun. 2024)"
doi: "10.1016/j.jid.2024.05.023"
pdf: referencias-pdf/Deng2023fedal.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P1]
status: fichado

# ===== ENTIDADES =====
proposes: [aprendizado-ativo-federado, entropia-de-ensemble]
uses_methods: [aprendizado-ativo, pool-based, entropia, aprendizado-federado, selecao-aleatoria, fine-tuning]
datasets: [ham10k, msk-isic]
metrics: [macro-f1, micro-f1, auc]
tasks: [classificacao-de-imagens]
models: [resnet101]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: complementa
    target: FALCO
    note: "Sustenta a menção ao cenário FEDERADO em 2-fundam:327, que é uma das
           três extensões do laço clássico listadas ali. Não compete com o
           FALCO: o eixo dele é privacidade entre instituições, não custo de
           oráculo. Serve como terceiro ponto da série regime × ganho da
           seleção — ver 'Ideias que gera'."
---

# Federated Active Learning Framework for Efficient Annotation Strategy in Skin-Lesion Classification

## Resumo (5-8 linhas, com as MINHAS palavras)
Combina aprendizado ativo com aprendizado federado para reduzir o volume de
anotação em diagnóstico por imagem sem que os hospitais precisem compartilhar
dados de pacientes. A ideia central é a **entropia de ensemble**: em cada
cliente, o modelo local e o modelo global obtido pela federação formam um
comitê de dois, e a discordância entre eles pontua quais imagens vão para o
especialista humano. O ciclo de seleção roda periodicamente entre as rodadas
de federação. Validado num conjunto dermatoscópico real, deliberadamente
heterogêneo (quatro "hospitais" com distribuições diferentes), o método atinge,
com metade dos dados anotados, desempenho estatisticamente indistinguível do
treino com dados completos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Aprendizado ativo executado periódica e interativamente sob federação reduz a anotação preservando privacidade | Resumo, p. 1; algoritmo do framework, Tab. 1 | 2-fundam:327 — é a citação que a tese já faz do cenário federado |
| C2 | Com 50% dos dados, o desempenho fica em 99,9% (Micro-F1), 100% (Macro-F1) e 99,4% (AUC) do teto de treino com dados completos; a diferença não é estatisticamente significativa (t pareado: P=0,868, P=0,939 e P=0,113) | §Resultados e Tab. 3 | Cap. 2/6: exemplo de que metade do orçamento pode bastar quando a seleção é boa |
| C3 | A seleção do FedAL supera a **amostragem aleatória** com significância em Micro-F1 e Macro-F1 (t pareado, P<0,05); ganho relativo de 3,11%, 3,15% e 0,5% | Tab. 3 e §Resultados | Cap. 5: terceiro ponto da série regime × ganho da seleção |
| C4 | O ganho em AUC sobre os concorrentes **não** é estatisticamente significativo — os autores declaram isso explicitamente | §Resultados ("did not demonstrate a statistically significant improvement in AUC") | Cap. 5: exemplo de reporte honesto de resultado parcial; modelo para o nosso próprio texto |
| C5 | O ensemble local+global é o que dá a incerteza; nenhum modelo sozinho é usado como pontuador | §Método, Tab. 1 | Cap. 2: variante de comitê com custo baixo (dois modelos que já existem) |

## Números que posso citar
Condições: ResNet-101 pré-treinada na ImageNet; conjunto federado de
**10.490 imagens dermatoscópicas** distribuídas em **4 hospitais** (8.490 do
HAM10K e 2.000 do MSK), divisão 7:1:2 entre treino, validação e teste;
**3 classes** (nevo, ceratose benigna, melanoma); distribuição **não-IID** entre
clientes; resultados médios de **5 execuções** com sementes diferentes.

Tabela 3 — Macro-F1 (média ± desvio):

| Método | Dados | Macro-F1 |
|---|---|---|
| Aprendizado centralizado (teto) | 100% | 79,62 ± 0,26 |
| FedAvg com dados completos (teto federado) | 100% | 78,53 ± 0,30 |
| **FedAL (deles)** | **50%** | **78,50 ± 1,08** |
| FedAvg + SA | 50% | 76,39 ± 1,45 |
| **FedAvg + aleatório (piso)** | **50%** | **76,14 ± 1,77** |
| FedAvg + AIFT | 50% | 75,11 ± 1,58 |
| FedAvg + MCDAL | 50% | 74,14 ± 1,38 |

Desequilíbrio das classes por hospital (Tab. 2): o hospital C tem 3.720 nevos
contra **24 melanomas**; o hospital A tem 803 contra 342. É desbalanceamento
severo e desigual entre clientes.

## Citações diretas (com página)
> "Using only 50% of samples, our framework was able to achieve
> state-of-the-art performance on a skin-lesion classification task." (Resumo, p. 1)

> "the differences in performance between our FedAL framework and the upper
> bound of full-data training were not statistically significant, as indicated
> by the paired t-test results (P = 0.868 for Micro-F1, P = 0.939 for
> Macro-F1, and P = 0.113 for AUC)." (§Resultados, p. 8)

> "our method did not demonstrate a statistically significant improvement in
> AUC compared to some methods." (§Resultados, p. 8)

## Crítica / limitações (minha leitura)
- **É imagem médica, não texto**, e são **3 classes** contra as 621 do FALCO.
  A distância de regime é enorme; serve como referência de cenário (federado),
  não como evidência transferível de desempenho.
- **A comparação com o aleatório é modesta**: 78,50 contra 76,14 de Macro-F1,
  ou seja **2,36 pontos**, com desvios de 1,08 e 1,77. É significativo pelo
  teste pareado, mas está longe de ser uma diferença que se veja a olho nu — e
  isso importa para a leitura da série de regimes abaixo.
- **Não há oráculo LLM**: a anotação é humana especialista, simulada a partir
  de um conjunto já rotulado. Nenhuma das questões de ruído de oráculo que a
  tese investiga aparece aqui.
- **A afirmação de pioneirismo** ("to our knowledge, this is the first FedAL
  framework applied to medical images") é do tipo que a nossa própria
  constituição desaconselha sem delimitação de busca; ao citar, não repetir a
  alegação de primazia.

## Nota de proveniência (importante para o registro)
A entrada `Deng2023fedal` do `referencias.bib` na `main` aponta para
**arXiv:2303.09753**, que é outro artigo — "A Spatio-temporal Decomposition
Method for the Coordinated Economic Dispatch of Integrated Transmission and
Distribution Grids", de sistemas de potência. O identificador correto do
preprint é **arXiv:2406.11310**, e a versão publicada é a do *Journal of
Investigative Dermatology* citada acima.

O conserto **já estava aplicado** na branch `bibfix/lotes` desde o lote 1
(commit `51072c1`, revisor2): a entrada de lá traz o veículo, o volume, as
páginas, o ano e o DOI corretos, todos reconferidos por mim no Crossref antes
de fichar. A `main` é que está atrasada.

A chave permanece `Deng2023fedal` por decisão do autor — chave é identificador
interno e não aparece impressa. O ano impresso passa de 2023 para 2025 quando o
gate do bib-fix entrar.

## Ideias que gera para a tese
- **Terceiro ponto da série "regime × ganho da seleção"**, que já vinha
  se formando nos fichamentos desta madrugada:

  | Fonte | Classes | A seleção bate o aleatório? |
  |---|---|---|
  | `Rouzegar2024` | 2 a 4 | sim, com folga |
  | `Deng2023fedal` | 3 | sim, mas por 2,36 pontos de Macro-F1 |
  | `Wertz2022` | 100 a 739 | **não**, de forma consistente |

  Três trabalhos independentes, três regimes, uma tendência clara: **a vantagem
  da seleção ativa encolhe conforme o espaço de rótulos cresce**. O FALCO opera
  em 621 classes, do lado difícil. Isso vira um parágrafo forte na discussão do
  Cap. 5 e justifica por que o braço aleatório foi tratado como comparador
  sério.
- **Modelo de reporte honesto**: o C4 é um caso a imitar — os autores declaram
  em qual métrica o ganho não alcança significância, em vez de omitir. Vale
  como referência de estilo para o nosso Cap. 5.
- **Comitê barato**: o ensemble local+global custa zero modelos adicionais,
  porque os dois já existem no laço federado. Se algum dia o FALCO tiver mais
  de um classificador em jogo, é uma fonte de incerteza sem custo extra.
