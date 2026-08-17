---
id: Grandini2020
title: "Metrics for Multi-Class Classification: an Overview"
authors: ["Grandini, Margherita", "Bagli, Enrico", "Visani, Giorgio"]
year: 2020
venue: "White paper, arXiv:2008.05756 (CRIF S.p.A. e Universidade de Bolonha)"
pdf: referencias-pdf/Grandini2020.pdf

paper_type: survey
status: fichado

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "É a fonte que descreve as métricas multiclasse alternativas
           (acurácia balanceada, coeficiente de Matthews, Kappa de Cohen) que a
           tese cita para, em seguida, dispensar de forma justificada."
---

# Grandini, Bagli e Visani (2020)

## O que a tese cita, e a obra sustenta?

**Sim.** O Cap. 2 usa esta obra em dois pontos, e os dois conferem:

1. a inadequação da acurácia como métrica única sob desbalanceamento;
2. a existência e a descrição das alternativas — acurácia balanceada,
   coeficiente de correlação de Matthews e Kappa de Cohen — que a tese menciona
   antes de dispensar.

Confirmei os dois na fonte: a acurácia balanceada é tratada a partir da p. 4,
com a afirmação de que ela "is insensitive to imbalanced class"; Matthews e
Kappa aparecem na p. 9, apresentados como as duas últimas métricas do texto,
construídas a partir da matriz de confusão.

**Natureza da obra, declarada:** é um *white paper* corporativo (CRIF S.p.A.,
com coautoria da Universidade de Bolonha), não artigo com revisão por pares. Não
compromete o uso que a tese faz — a obra é citada para descrever métricas
consagradas, não para sustentar resultado empírico — mas registro porque é
informação que a banca pode perguntar.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A matriz de confusão contém toda a informação relevante sobre o desempenho, e a maioria das métricas multiclasse deriva dela | §1.1, p. 2 | Cap. 2: sustenta a matriz de confusão como instrumento de diagnóstico |
| C2 | A acurácia balanceada é **insensível ao desbalanceamento** de classes, porque dá influência proporcional às classes menores | p. 4 | Cap. 2: é a alternativa nº 1 que a tese cita e dispensa |
| C3 | Coeficiente de Matthews e Kappa de Cohen partem da matriz de confusão e de dois conceitos estatísticos distintos (coeficiente Phi e concordância entre avaliadores) | p. 9 | Cap. 2: alternativas nº 2 e nº 3 citadas e dispensadas |
| C4 | As métricas são úteis em momentos diferentes do desenvolvimento: comparar dois modelos, ou analisar o mesmo modelo variando parâmetros | Resumo, p. 1 | Cap. 2: reforça que a escolha de métrica é decisão de projeto |

## Por que a dispensa da tese continua defensável

A obra descreve as alternativas, mas **não demonstra** que elas separem
fenômenos que o par Macro F1 + acurácia global não separe. A justificativa da
tese (aprovada pelo autor na leitura do t1) é de separação operacional: as duas
métricas escolhidas chegam a divergir em sinal, e uma métrica única mascararia
o contraste. Nada nesta fonte contradiz esse argumento.
