---
id: Kossen2021
title: "Active Testing: Sample-Efficient Model Evaluation"
authors: ["Kossen, Jannik", "Farquhar, Sebastian", "Gal, Yarin", "Rainforth, Tom"]
year: 2021
venue: "ICML 2021 (PMLR 139:5753-5763)"
doi: ""
pdf: referencias-pdf/Kossen2021.pdf
paper_type: metodo
pillars: [transversal]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, entropia]
datasets: []
metrics: [acuracia, custo-por-rotulo]
tasks: []
models: []
extends: [Farquhar2021]
compares_with: []
contradicts: []
builds_on: [Houlsby2011]
falco_relation:
  - type: fundamenta
    target: instrumentacao-estatistica
    note: "Formaliza que rotular dados de TESTE também custa e que selecionar
           pontos de teste por incerteza SUPERESTIMA a perda se não houver correção
           (LURE). Sustenta duas decisões do FALCO: (i) nunca reaproveitar pontos
           selecionados pelo laço ativo para avaliação; (ii) avaliar na população
           reservada de 177.490 por amostragem uniforme, que dispensa correção."
  - type: complementa
    target: FALCO
    note: "Caminho futuro: se a população reservada não tivesse rótulos de
           referência, o teste ativo com LURE permitiria estimar Macro F1/perda com
           fração dos rótulos (custo relativo ~0,25 em CIFAR-10/Fashion-MNIST) —
           relevante para replicar o FALCO em domínios de varejo sem ground truth."
---

# Active Testing: Sample-Efficient Model Evaluation

## Resumo (5-8 linhas)
Introduz o "teste ativo": seleção ativa de quais pontos de TESTE rotular para
avaliar um modelo com poucos rótulos, área ignorada pela literatura de AL, que
assume conjuntos de teste grandes e gratuitos. Como a seleção ativa enviesa o
estimador ingênuo (pontos incertos são mais difíceis que a média), aplica o
estimador não-viesado R̂_LURE de Farquhar2021 e deriva funções de aquisição
próprias para teste (proporcionais à perda esperada, aproximada por um modelo
substituto/surrogate). Mostra que as aquisições boas para AL (ex.: informação
mútua/BALD) não servem para teste ativo, e que ensembles profundos como
surrogate dão estimativas precisas com 2-4× menos rótulos que amostragem i.i.d.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A literatura de AL "largely ignores the cost of labeling test data, typically unrealistically assuming large test sets" | Abstract + §1, p. 1 | Cap. 2 fundamentação — motivação da LCE/custo total (treino E teste) |
| C2 | Selecionar teste por incerteza sem correção superestima a perda: "the least certain points will tend to be harder than average"; efeito pior em modelos superconfiantes | §1, p. 2 | Cap. 3 — por que a avaliação do FALCO é disjunta do laço ativo |
| C3 | R̂_LURE (pesos v_m, Eq. 3-4) remove o viés da seleção ativa e, com proposta adequada, reduz (drasticamente) a variância vs R̂_iid | §2.2, Eqs. (3)-(4), p. 3 | Cap. 2 fundamentação |
| C4 | A proposta ótima amostra proporcionalmente à perda esperada: q*(i_m) ∝ E_{p(y|x)}[L(f(x),y)]; para classificação vira entropia-cruzada entre surrogate e modelo | §3.1 Eq. (5), §3.3 Eqs. (10)-(12), pp. 3-4 | Cap. 2 fundamentação |
| C5 | Ganho empírico: custo relativo de rotulagem ~0,25 (4× menos rótulos) em CIFAR-10 e Fashion-MNIST e ~0,5 (2×) em CIFAR-100 para igualar a precisão do i.i.d.; ganhos similares ao estimar ACURÁCIA | §5.3, Fig. 6(b), p. 7 | Cap. 5 discussão — avaliação eficiente |
| C6 | Aquisição de AL não transfere para teste: informação mútua (BALD) rende pior que entropia preditiva no teste ativo, pois foca incerteza epistêmica e ignora a aleatória, que importa para avaliação | §5.6, Fig. 8(b), p. 8 | Cap. 5 discussão |
| C7 | Estratégia ingênua (o próprio modelo como surrogate, sem ensemble) só é aceitável como último recurso, se as incertezas do modelo forem confiáveis | §3.4/§5.7, pp. 5 e 8 | Cap. 5 discussão |

## Números que posso citar
- Custo relativo de rotulagem de teste (fração de rótulos ativos para igualar a
  precisão do i.i.d.): ~0,25 em CIFAR-10 e Fashion-MNIST; ~0,5 em CIFAR-100
  (WideResNet/ResNet-18; medianas sobre 1000 conjuntos de teste; Fig. 6b, p. 7).
- Sintético (GP regressão): com 5 pontos de teste ativos o desvio-padrão do
  estimador já iguala o do i.i.d. com 40 pontos — quase o conjunto inteiro
  (§5.1, Fig. 3a, p. 6).
- Estudo de surrogate: ResNet-18 em CIFAR-10 com treino restrito a 250 pontos;
  ensemble de 5 ResNet-18 supera um único ResNet-50 (§5.4, Fig. 7, pp. 7-8).
- Pesos LURE: v_m = 1 + (N-M)/(N-m) · [1/((N-m+1)·q(i_m)) - 1] (Eq. 4, p. 3).

## Citações diretas (com página)
> "Whenever labels are expensive enough that we need to carefully pick training data, we cannot afford to be wasteful with test data either." (p. 1, §1)

> "Acquiring points where the model is least certain (Houlsby et al., 2011) will likely overestimate the test loss: the least certain points will tend to be harder than average." (p. 2, §1)

> "This is just one way active testing needs special examination and cannot just re-use results from active learning." (p. 8, §5.6)

## Crítica / limitações (minha leitura)
- Exige um surrogate de qualidade (idealmente ensemble retreinado), o que
  adiciona custo computacional O(M·|D_train| + M·N) — no FALCO, onde o gargalo
  é o custo de rótulo LLM e a população reservada JÁ tem rótulos de referência,
  o teste ativo não é necessário no desenho atual, só em replicações sem gold.
- Avaliado em visão (MNIST/CIFAR/Fashion-MNIST) e regressão sintética; nada em
  NLP nem em multi-classe extrema/desbalanceada como as 714 classes do FALCO —
  estimar perda esperada com surrogate em 714 classes desbalanceadas é questão
  aberta.
- Estima perda/acurácia agregada; não cobre métricas macro (Macro F1) nem testes
  pareados (McNemar) — a transposição para essas estatísticas não é dada.

## Ideias que gera para a tese
- Citar C1-C2 no Cap. 3 para justificar a separação estrita: pool ativo para
  treinar, população reservada uniforme (177.490) para avaliar — o FALCO evita
  por construção o viés que o teste ativo precisa corrigir.
- Cap. 5 (trabalhos futuros): FALCO + teste ativo com oráculo LLM também na
  avaliação, para domínios sem ground truth — o custo por rótulo LLM da LCE se
  aplicaria aos dois lados (treino e teste).
- C6 reforça que decisões do laço de AL (entropia no E5/E6) não devem ser
  reaproveitadas acriticamente em avaliação.
