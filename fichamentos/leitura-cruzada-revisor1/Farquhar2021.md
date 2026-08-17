---
id: Farquhar2021
title: "On Statistical Bias In Active Learning: How and When to Fix It"
authors: ["Farquhar, Sebastian", "Gal, Yarin", "Rainforth, Tom"]
year: 2021
venue: "ICLR 2021 (spotlight); arXiv:2101.11665"
doi: ""
pdf: referencias-pdf/Farquhar2021.pdf
paper_type: metodo
pillars: [transversal]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza]
datasets: []
metrics: [acuracia]
tasks: []
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994, Settles2009, Houlsby2011]
falco_relation:
  - type: fundamenta
    target: instrumentacao-estatistica
    note: "Prova que o risco empírico calculado sobre pontos ATIVAMENTE amostrados
           é viesado (não-i.i.d. da população). Fundamento teórico direto da decisão
           de desenho do FALCO de avaliar Macro F1/McNemar/bootstrap numa população
           reservada de 177.490 textos NUNCA tocada pela seleção ativa — avaliação
           i.i.d., livre do viés de seleção que o paper formaliza."
  - type: complementa
    target: FALCO
    note: "Explica por que treinar BERTimbau/SGD sobre o conjunto ativamente
           selecionado SEM pesos corretivos é defensável: em modelos
           superparametrizados o viés do AL tem sinal oposto ao viés de overfitting
           e atua como regularização (remover o viés pode até piorar o modelo)."
---

# On Statistical Bias In Active Learning: How and When to Fix It

## Resumo (5-8 linhas)
Formaliza o viés estatístico do aprendizado ativo: como os pontos são escolhidos
por informatividade (e não uniformemente), o risco empírico sobre o conjunto
adquirido deixa de ser estimador não-viesado do risco populacional. Propõe dois
estimadores com pesos corretivos por importância — R̃_PURE e R̃_LURE —, prova que
são não-viesados e consistentes, e que R̃_LURE tem variância menor. Empiricamente
(regressão linear; BNN em MNIST/FashionMNIST), remover o viés ajuda modelos
subparametrizados, mas pode PREJUDICAR modelos superparametrizados, nos quais o
viés do AL cancela parcialmente o viés de overfitting e age como regularizador.
Em tempo de teste, porém, a correção é quase sempre benéfica.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O risco empírico sub-amostrado R̃ sobre M pontos ativamente amostrados NÃO é estimador não-viesado de R̂ nem de r ("Under active—i.e. non-uniform—sampling the M datapoints are not drawn from the population distribution") | §2, Eq. (1), p. 2 | Cap. 2 fundamentação; Cap. 3 justificativa da população reservada |
| C2 | R̃_PURE (pesos w_m = 1/Nq) é não-viesado (E[R̃_PURE] = r) e consistente | §3.1, Eq. (2)-(3), Teoremas 1-2, p. 3 | Cap. 2 fundamentação (existe correção formal) |
| C3 | R̃_LURE reponderado é não-viesado, consistente e com variância ≤ R̃_PURE (estrita se M>1) | §3.2, Eq. (5), Teoremas 3-5, p. 4 | Cap. 2 fundamentação |
| C4 | Quase todo trabalho de AL ignora o viés: dos 15 papers revisados por pares mais citados que citam Gal et al. 2017a, só 2 mencionam o viés e nenhum o trata | §5, p. 6 (detalhe no Apêndice D) | Cap. 2 — lacuna/prática da área |
| C5 | Em modelos superparametrizados (BNN), treinar com R̃_LURE/R̃_PURE dá desempenho igual ou PIOR que o estimador viesado: o viés do AL (negativo) cancela parcialmente o viés de overfitting (positivo) e regulariza | §6 Fig. 3(b-f), §7 Fig. 4, pp. 7-9 | Cap. 5 discussão — validade de treinar no conjunto ativo sem correção |
| C6 | Em avaliação (test-time), sem viés de otimização/overfitting, usar R̃_LURE "will usually be beneficial" — abre a linha de avaliação eficiente de modelos | §8, p. 9 | Cap. 3 método (ponte para Kossen2021); Cap. 5 |

## Números que posso citar
- Levantamento informal: 15 papers mais citados (peer-reviewed) citando Gal et al.
  (2017a); apenas 2 mencionam o viés estatístico, nenhum o corrige (§5, p. 6).
- BNN convolucional com ~80.000 parâmetros em MNIST/FashionMNIST modificados
  (desbalanceados e com rótulos ruidosos), proposta de aquisição estilo BALD
  relaxada estocasticamente (§6, p. 7; Apêndice C.2).
- Pesos: w_m = 1/(N·q(i_m; i_{1:m-1}, D_pool)); v_m = 1 + (N-M)/(N-m) ·
  [1/((N-m+1)·q) - 1] (Eqs. 2 e 5, pp. 3-4).
- Regressão linear: 1000 trajetórias de aquisição; r estimado em 10.100 pontos
  da distribuição (Fig. 2a/3a, pp. 7-8).

## Citações diretas (com página)
> "If training data are actively sampled, that estimator is biased and we optimize the wrong objective." (p. 1)

> "The bias from standard active learning can actually be helpful by providing a regularising effect that aids generalization." (p. 1, §1)

> "At test-time, where optimization and overfitting bias are no-longer an issue, there is little cost to using R̃_LURE to evaluate a model and it will usually be beneficial." (p. 9, §8)

## Crítica / limitações (minha leitura)
- A correção exige uma distribuição-proposta q com massa não-nula em todo o pool
  e conhecida em cada passo; aquisições determinísticas (argmax de entropia, como
  no E5/E6) precisam ser convertidas em amostragem estocástica (softmax/ε-greedy)
  para permitir a correção — o FALCO não faz isso, e o paper mostra que não fazer
  é aceitável para treino de modelos superparametrizados.
- Experimentos pequenos (regressão linear, BNN ~80k parâmetros, MNIST/Fashion);
  nada em NLP, transformers ou multi-classe extrema (714 classes).
- A análise assume avaliação de f fixa (θ independente dos dados de treino) na
  parte estatística; a interação com otimização (§7) é tratada só empiricamente.

## Ideias que gera para a tese
- Citar C1 como fundamento formal de por que a população reservada de 177.490
  (amostra uniforme fora do laço) é a escolha correta para McNemar pareado e
  bootstrap de Macro F1 — nenhuma métrica da tese é computada sobre o conjunto
  ativamente selecionado.
- Usar C5 no Cap. 5 para responder preventivamente à crítica "o BERTimbau foi
  treinado num conjunto enviesado": em modelos superparametrizados esse viés
  tende a ajudar, não invalidar.
- C6 conecta diretamente com Kossen2021 (Active Testing) — mesma linha de Oxford.
