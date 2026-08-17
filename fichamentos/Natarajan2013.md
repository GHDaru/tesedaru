---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Natarajan2013
title: "Learning with Noisy Labels"
authors: ["Natarajan, Nagarajan", "Dhillon, Inderjit S.", "Ravikumar, Pradeep", "Tewari, Ambuj"]
year: 2013
venue: "Advances in Neural Information Processing Systems 26 (NIPS), pp. 1196-1204"
doi: ""
pdf: referencias-pdf/Natarajan2013.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P4]
status: fichado

# ===== ENTIDADES =====
proposes: [estimador-nao-viesado-de-perda, perda-corrigida]
uses_methods: [minimizacao-de-risco-empirico, ruido-dependente-de-classe]
datasets: []
metrics: [acuracia]
tasks: [classificacao-binaria]
models: [svm]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: oraculo-progressivo
    note: "sustenta a frase da §2.3 de que há garantias de aprendizado sob ruído com funções de perda corrigidas — é o alicerce teórico de treinar com rótulos de oráculo imperfeito"
  - type: fundamenta
    target: FALCO
    note: "citado no Cap. 6 junto a Frenay2014 e Song2023NoisyLabels para sustentar que erro estruturado é o cenário benigno da literatura de ruído"
---

# Learning with Noisy Labels

## Resumo (5-8 linhas, com as MINHAS palavras)

O artigo trata o caso em que os rótulos de treino chegam corrompidos por ruído
aleatório dependente da classe: um exemplo positivo virá negativo com
probabilidade $\rho_{+1}$, e o inverso com $\rho_{-1}$. A pergunta é se ainda se
pode minimizar risco com garantia, e a resposta é sim, por dois caminhos. O
primeiro constrói, a partir das taxas de ruído, um **estimador não viesado** de
qualquer função de perda, e obtém limites de desempenho para a minimização de
risco empírico sobre os dados ruidosos; uma condição simples de simetria
garante que a perda substituta continue convexa. O segundo atribui **custos
dependentes do rótulo** e mostra que o classificador de Bayes da distribuição
ruidosa é o mesmo, apenas com limiar deslocado. É teoria com algoritmo, não
apenas teorema.

## Claims relevantes

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Existe estimador **não viesado** de qualquer função de perda sob ruído, com limites de desempenho para minimização de risco empírico em dados ruidosos | Resumo (p. 1) e §3 "Method of Unbiased Estimators" (p. 3) | §2.3 — sustenta "garantias de aprendizado sob ruído com funções de perda corrigidas" (l. 664) |
| C2 | Sob condição simples de simetria, a perda substituta permanece **convexa** — vale para Huber, logística e quadrática; a \textit{hinge} não satisfaz | §2 (p. 2) | §2.3 e Cap. 3 — justifica por que a correção é operacional, não só teórica |
| C3 | O minimizador empírico calculado sobre a distribuição **ruidosa** tem risco de classificação que se aproxima do risco de Bayes da distribuição **verdadeira** | §3, discussão do Teorema (p. 4) | Cap. 6 — o argumento de que treinar com rótulo de oráculo imperfeito não condena o resultado |
| C4 | Método alternativo por custos dependentes do rótulo: quando $\rho_{+1} \neq \rho_{-1}$, o classificador de Bayes da distribuição ruidosa usa apenas um **limiar diferente de 1/2** | §4 (p. 5) e Teorema 11 (p. 6) | Cap. 2 — mostra que ruído assimétrico é tratável por reponderação |

## Números que posso citar

- Em dados sintéticos 2D linearmente separáveis, os métodos propostos mantêm
  **mais de 90% de acurácia mesmo com $\rho_{+1} = \rho_{-1} = 0{,}4$** (§5.1,
  p. 7). Condição: dado sintético, separável, ruído simétrico e **taxas de ruído
  conhecidas**.
- O paper também estuda a **má especificação** das taxas de ruído (§5 e Apêndice
  C, p. 8) — relevante para nós, porque no nosso caso a taxa de ruído do oráculo
  é estimada, não dada.

## Citações diretas (com página)

> "we provide a simple unbiased estimator of any loss, and obtain performance
> bounds for empirical risk minimization in the presence of iid data with noisy
> labels." (p. 1)

> "we give a simple symmetry condition on the loss (enjoyed, for instance, by the
> Huber, logistic, and squared losses) to ensure that the proxy loss is also
> convex. Hinge loss does not satisfy..." (p. 2)

## Crítica / limitações (minha leitura)

Três limites que a tese deve respeitar ao citar. **Primeiro**, o cenário é
**binário** — a nossa tarefa é multiclasse com centenas de classes, e a extensão
não é imediata. **Segundo**, as garantias supõem ruído **aleatório dependente da
classe** (CCN); o erro do nosso oráculo LLM é dependente da **instância**
(confusões concentradas em pares vizinhos), que é justamente o caso que
`Frenay2014` classifica como mais difícil. **Terceiro**, a correção precisa das
**taxas de ruído**; no nosso regime elas são estimadas a partir de amostra
auditada, e o paper mostra que má especificação degrada o resultado.

Isso não invalida o uso na tese: a frase da §2.3 afirma apenas que existem
garantias sob ruído com perdas corrigidas, e isso é exatamente o que o paper
estabelece. Mas o Cap. 6, que cita a obra para dizer que erro estruturado é
"cenário benigno", pede cautela — o benigno da literatura CCN é o ruído
**aleatório**, e o nosso é estruturado por vizinhança semântica. Estruturado é
mais fácil de *interpretar*, não necessariamente o caso coberto por estas
garantias.

## Ideias que gera para a tese

Se em algum momento quisermos treinar com correção de perda usando a taxa de
ruído medida do oráculo, este é o alicerce, e a condição de simetria (C2) diz
quais perdas podem ser usadas — logística sim, \textit{hinge} não. É decisão de
método, não de fundamentação, e fica registrada aqui para quando o Cap. 3
precisar dela.
