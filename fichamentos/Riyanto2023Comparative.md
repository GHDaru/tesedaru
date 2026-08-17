---
id: Riyanto2023Comparative
title: "Comparative Analysis using Various Performance Metrics in Imbalanced Data for Multi-class Text Classification"
authors: ["Riyanto, Slamet", "Sitanggang, Imas Sukaesih", "Djatna, Taufik", "Atikah, Tika Dewi"]
year: 2023
venue: "International Journal of Advanced Computer Science and Applications (IJACSA), v. 14, n. 6, pp. 1082--1090"
pdf: referencias-pdf/Riyanto2023Comparative.pdf

paper_type: empirico
status: fichado

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Vizinho direto da decisão métrica da tese: compara métricas em dados
           desbalanceados de classificação de texto MULTICLASSE e conclui que o
           F1 é a métrica que importa nesse regime."
---

# Riyanto, Sitanggang, Djatna e Atikah (2023)

## O que a tese cita, e a obra sustenta?

**Sim, e é a citação mais alinhada das quatro.** O Cap. 2 cita esta obra ao lado
de Grandini2020 para as alternativas de métrica; a obra é um estudo comparativo
de métricas **em dados desbalanceados de classificação de texto multiclasse** —
exatamente o regime da tese.

A tese sustenta o Macro F1 como métrica principal. O resumo desta obra diz:
"Precision and Recall are very important to consider when the data is balanced,
but **in the case of unbalanced data the F1-score is the most important
metric**". É apoio direto, não tangencial.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Em dados desbalanceados, o F1 é a métrica mais importante; precisão e revocação isoladas servem ao caso balanceado | Resumo, p. 1 | Cap. 2: apoio direto à escolha do Macro F1 como métrica principal |
| C2 | O micro-F1 pode ficar **acima** do macro porque o modelo prevê melhor a classe dominante | §I, p. 2 | Cap. 2: é a razão técnica de a tese reportar macro, e não micro |
| C3 | Estudos anteriores analisaram apenas o equilíbrio entre macro-F1 e micro-F1 | §I, p. 2 | Cap. 2: situa a lacuna que a obra ocupa |
| C4 | Cinco classificadores comparados (Naive Bayes multinomial, kNN, SVM, floresta aleatória e LSTM), com abordagens de nível de dados e de algoritmo | Resumo, p. 1 | Cap. 2: dá lastro empírico à comparação de métricas |
| C5 | Corpus PDR com **quatro** classes e forte desbalanceamento: Association (34), Cause of Disease (183), Treatment of Disease (507), Negative (583) | §II.A, p. 2 | Ver ressalva de escala abaixo |

## Ressalva de escala, que a tese precisa respeitar

O desbalanceamento aqui é de **quatro** classes, com a menor tendo 34 registros
e a maior 583 — razão de cerca de 17 para 1. A tese opera com **621 rótulos** e
cauda longa. A conclusão qualitativa (F1 é o que importa sob desbalanceamento)
transfere-se bem; qualquer número desta obra, não. Registro para que a citação
permaneça no papel de apoio conceitual, que é como o Cap. 2 a usa hoje.

## Sobre a ausência de DOI

O periódico não declara DOI para o artigo; a URL do volume 14, n. 6, abre e
responde. Pelo vocabulário de três vereditos da verificação das clássicas, o
caso é `nao-indexada-declarada`: propriedade do veículo, não defeito da entrada.
