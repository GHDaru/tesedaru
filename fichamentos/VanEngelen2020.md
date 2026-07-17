---
id: VanEngelen2020
title: "A survey on semi-supervised learning"
authors: ["van Engelen, Jesper E.", "Hoos, Holger H."]
year: 2020
venue: "Machine Learning, 109, pp. 373–440"
doi: "10.1007/s10994-019-05855-6"
pdf: referencias-pdf/VanEngelen2020.pdf
paper_type: survey
pillars: [geral]
status: fichado
proposes: [taxonomia-ssl]
uses_methods: [semi-supervisao]
datasets: []
metrics: []
tasks: []
models: []
extends: []
compares_with: [Persello2014]
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "O survey de referência de semi-supervisão (Machine Learning 2020):
           a citação certa para definir SSL no Cap.2 e para o contraste AL vs SSL
           (por que escolhemos AL: temos oráculo barato)."
---

# A survey on semi-supervised learning (van Engelen & Hoos, 2020)

## Resumo
Survey de referência de SSL (68 pp.): situa a semi-supervisão entre supervisão e
não-supervisão, taxonomiza métodos (indutivos/transdutivos; wrapper, ensemble,
grafos, perturbação) e discute suposições necessárias (smoothness, cluster,
manifold) para o não-rotulado ajudar.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | SSL depende de suposições estruturais sobre os dados para funcionar | Corpo (assumptions) | Cap.2: contraste com AL — AL não exige essas suposições, exige oráculo; com LLM barato, AL domina |
| C2 | Taxonomia moderna do SSL | Escopo | Citação única para toda a subseção de semi-supervisão |

## Números que posso citar
- (Survey.)

## Crítica / limitações (minha leitura)
- Nada específico de texto curto.

## Ideias que gera para a tese
- Condensar a subseção SSL do Cap.2 para 1 parágrafo apoiado neste survey
  (mesma tática das demais condensações).
