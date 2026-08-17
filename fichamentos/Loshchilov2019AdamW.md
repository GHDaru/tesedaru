---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Loshchilov2019AdamW
title: "Decoupled Weight Decay Regularization"
authors: ["Loshchilov, Ilya", "Hutter, Frank"]
year: 2019
venue: "International Conference on Learning Representations (ICLR)"
doi: ""
pdf: referencias-pdf/Loshchilov2019AdamW.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: metodo
pillars: [P4]
status: fichado

# ===== ENTIDADES =====
proposes: [adamw, decaimento-de-peso-desacoplado]
uses_methods: [fine-tuning]
datasets: []
metrics: []
tasks: []
models: []

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "é a referência do otimizador do ajuste fino do BERTimbau no Cap. 3; a escolha de AdamW com decaimento de peso 0,01 só faz sentido sob a formulação desacoplada que este artigo propõe"
---

# Decoupled Weight Decay Regularization

**Lida na fonte** (ICLR 2019, 19 pp.), identidade conferida na folha de rosto.

## O que a tese usa desta obra

O Cap. 3 declara: ajuste fino do BERTimbau com a biblioteca `transformers`,
**otimizador AdamW**, taxa de aprendizado $3\times10^{-5}$, lote 32 e
**decaimento de peso $0{,}01$**. Esta obra é a que dá sentido a esses dois
últimos números juntos.

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Regularização $L_2$ e decaimento de peso são equivalentes no SGD padrão, mas **não** em algoritmos de gradiente adaptativo como o Adam | Resumo, p. 1 | Cap. 3 — justifica escrever "AdamW" e não "Adam com $L_2$" |
| C2 | A correção proposta é **desacoplar** o decaimento de peso do passo de gradiente, recuperando a formulação original | Resumo (p. 1) e Algoritmo 2 (p. 3) | Cap. 3 — é o algoritmo efetivamente executado pela `transformers` |
| C3 | Com o desacoplamento, taxa de aprendizado e decaimento de peso deixam de ser hiperparâmetros acoplados e podem ser ajustados de forma independente | §Introdução e §2, p. 1-3 | Cap. 3 — sustenta reportar $3\times10^{-5}$ e $0{,}01$ como escolhas separadas, e não como um par arbitrário |

## Citação direta (com página)

> "L2 regularization and weight decay regularization are equivalent for standard
> stochastic gradient descent (when rescaled by the learning rate), but as we
> demonstrate this is not the case for adaptive gradient algorithms, such as
> Adam. … we propose a simple modification to recover the original formulation of
> weight decay regularization by decoupling [it from the gradient update]"
> (Resumo, p. 1)

## Números que posso citar

Nenhum. Os números do ajuste fino desta tese ($3\times10^{-5}$, lote 32,
decaimento $0{,}01$) são **escolha da tese**, não resultado desta obra — o
artigo fundamenta o **método**, e não os valores. Registro explicitamente para
que ninguém atribua os hiperparâmetros da tese a esta referência.

## Crítica / limitações (minha leitura)

O artigo avalia principalmente visão computacional (CIFAR, ImageNet) e modelos
de linguagem recorrentes; **não** avalia ajuste fino de \textit{transformers}
pré-treinados, que é o nosso caso. Isso não enfraquece o uso — a correção é
sobre o otimizador, não sobre a tarefa —, mas significa que a evidência empírica
de superioridade não vem daqui para o nosso regime. O que a tese pode afirmar
com esta fonte é **por que o AdamW existe e o que ele faz**, não que ele seja
melhor para BERTimbau em português.

## Ideias que gera para a tese

O C3 é útil ao Cap. 3 e à reprodutibilidade: como decaimento e taxa são
independentes sob AdamW, os dois valores podem ser reportados (e reexecutados)
sem que um exija reinterpretar o outro. É argumento de método, e cabe em uma
linha ao lado dos hiperparâmetros.
