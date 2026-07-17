---
id: Santos2016Vies
title: "Seleção e controle do viés de aprendizado ativo"
authors: ["Santos, Davi Pereira dos"]
year: 2016
venue: "Tese de doutorado, ICMC-USP (orient. André C. P. L. F. de Carvalho)"
doi: ""
pdf: referencias-pdf/Santos2016Vies.pdf
paper_type: tese
pillars: [geral, P2]
status: fichado
proposes: [controle-de-vies-de-al]
uses_methods: [aprendizado-ativo, meta-aprendizado]
datasets: []
metrics: []
tasks: [classificacao]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Settles2012]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Tese ICMC-USP sobre o VIÉS que a amostragem ativa introduz (a amostra
           rotulada deixa de ser i.i.d.): fundamento para discutir por que curvas
           de aprendizado com AL exigem avaliação em conjunto de teste
           independente e aleatório — como fazemos nos E1–E3."
---

# Seleção e controle do viés de aprendizado ativo (Santos, 2016)

## Resumo
Tese de doutorado (ICMC-USP, 2016) dedicada à seleção e controle do **viés do
aprendizado ativo**: como a amostragem guiada distorce a distribuição do conjunto
rotulado em relação à população, afetando o classificador final, e como
selecionar/controlar estratégias considerando esse viés.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A amostragem ativa introduz viés distribucional no conjunto rotulado (não-i.i.d.) | Escopo | Cap.2/Cap.3: por que o teste dos E1–E3 é particionado ANTES e nunca tocado pela seleção ativa |
| C2 | O viés interage com a escolha da estratégia — controlá-lo é problema próprio | Escopo | Discussão do Cap.5 se curvas de estratégias divergirem de forma inesperada |

## Números que posso citar
- (Uso conceitual.)

## Crítica / limitações (minha leitura)
- Pré-DL, classificadores rasos; mas o argumento do viés é independente de época
  e raramente citado — bom diferencial de profundidade no Cap.2.

## Ideias que gera para a tese
- Citar C1 explicitamente na metodologia (desenho do split) — antecipa pergunta
  clássica de banca sobre validade estatística das curvas de AL.
