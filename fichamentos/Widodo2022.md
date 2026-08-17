---
id: Widodo2022
title: "Stratified K-fold cross validation optimization on machine learning for prediction"
authors: ["Widodo, Slamet", "Brawijaya, Herlambang", "Samudi"]
year: 2022
venue: "Sinkron: Jurnal dan Penelitian Teknik Informatika, v. 7, n. 4, pp. 2407--2414"
doi: "10.33395/sinkron.v7i4.11792"
pdf: referencias-pdf/Widodo2022.pdf

paper_type: empirico
status: fichado

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Sustenta a afirmação do Cap. 2 de que a estratificação das dobras é
           essencial sob desbalanceamento: no estudo, é exatamente o recurso
           adotado para lidar com classe-alvo desbalanceada."
---

# Widodo, Brawijaya e Samudi (2022)

## O que a tese cita, e a obra sustenta?

**Sim.** O Cap. 2 cita esta obra para "validação cruzada $k$-fold
**estratificada** [...] essencial sob desbalanceamento". A obra faz precisamente
esse movimento: declara que "the data used has an imbalance in the distribution
of the target class, namely more negative samples than positive ones" e que
"**to overcome this**, a technique called Stratified K-Fold Cross-Validation
(SKCV) is used" (Resumo, p. 1).

Ou seja, a estratificação aparece na fonte como **remédio declarado para o
desbalanceamento**, que é o uso exato que a tese faz da citação.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Diante de classe-alvo desbalanceada, a validação cruzada estratificada é adotada como o recurso para contornar o problema | Resumo, p. 1 | Cap. 2: sustenta "estratificada — essencial sob desbalanceamento" |
| C2 | A avaliação usa matriz de confusão para determinar o desempenho de cada modelo | Resumo, p. 1 | Cap. 2: coerente com o uso da matriz de confusão como instrumento |
| C3 | Melhor desempenho entre os cinco algoritmos: 96\% (Random Forest), 94\% (regressão logística), 92\% (XGBoost) | Resumo, p. 1 | Não usado na tese; registrado para contexto |
| C4 | O trabalho de referência anterior avaliava com 10-fold, medindo acurácia, precisão e revocação | p. 2 | Cap. 2: apoia "k tipicamente 5 ou 10" |

## DOIS ACHADOS DE BIBLIOGRAFIA — para o revisor1, dono do `referencias.bib`

**1. Grafia do título (já reportado, segue aberto).** O título real diz
"optimi**z**ation"; a entrada do `.bib` diz "optim**a**tion". Confirmado tanto
na Crossref quanto na primeira página do PDF.

**2. Página final (já reportado, segue aberto).** A entrada diz `2407--2413`;
a Crossref e a paginação do PDF (que abre em 2407 e tem 8 páginas) indicam
**2414**.

**3. NOVO — o próprio PDF tem o volume errado no cabeçalho.** O cabeçalho de
todas as páginas diz "Volume **6**, Number 4, October 2022", enquanto o DOI da
mesma página é `10.33395/sinkron.v**7**i4.11792` e a Crossref registra
**volume 7**. É erro do periódico, não da tese. Registro para que ninguém
"corrija" a entrada do `.bib` para 6 achando que está seguindo a fonte: o
volume correto é **7**, e a evidência é o DOI e o registro da Crossref, não o
cabeçalho do PDF.
