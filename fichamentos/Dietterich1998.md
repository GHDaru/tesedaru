---
id: Dietterich1998
title: "Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms"
authors: ["Dietterich, Thomas G."]
year: 1998
venue: "Neural Computation 10(7):1895-1923"
doi: "10.1162/089976698300017197"
pdf: referencias-pdf/Dietterich1998.pdf
paper_type: periodico
pillars: [transversal]
status: fichado
proposes: [taxonomia-de-testes-para-classificadores, 5x2cv]
falco_relation:
  - type: fundamenta
    target: instrumentacao-estatistica
    note: "Clássico que examina 5 testes para comparar classificadores e mede
           erro tipo I/poder: recomenda McNEMAR quando só há UMA execução de
           treino (nosso caso E0: oráculos fixos sobre a mesma amostra) e o
           5x2cv quando re-treino é viável. Fundamenta a escolha do McNemar na
           subseção 2.1.4 do plano."
---

# Approximate Statistical Tests (Dietterich, 1998)

## Resumo
Avalia cinco testes estatísticos para comparar algoritmos de classificação
(t-teste re-amostrado, validação cruzada, McNemar, 5x2cv...), medindo erro
tipo I e poder empiricamente. Conclusões: o t-teste re-amostrado infla erro
tipo I; McNemar é adequado quando o classificador é treinado uma única vez;
5x2cv quando múltiplos re-treinos são possíveis.

## Relação com a tese
Referência APLICADA do McNemar no E0 (oráculos avaliados uma única vez sobre
amostras pareadas) — par com McNemar 1947 na 2.1.4.
