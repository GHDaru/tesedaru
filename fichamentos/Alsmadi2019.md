---
id: Alsmadi2019
title: "Review of short-text classification"
authors: ["Alsmadi, Issa", "Gan, Keng Hoon"]
year: 2019
venue: "International Journal of Web Information Systems"
doi: "10.1108/IJWIS-12-2017-0083"
pdf: referencias-pdf/Alsmadi2019.pdf
paper_type: survey
pillars: [geral, P1]
status: fichado
proposes: [revisao-por-estagios-do-pipeline]
uses_methods: [selecao-de-atributos, algoritmos-geneticos, soft-computing]
datasets: []
metrics: []
tasks: [classificacao-de-texto-curto]
models: []
extends: [Song2014]
compares_with: []
contradicts: []
builds_on: [Song2014]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Revisão de STC organizada por estágio do pipeline; aponta algoritmos
           genéticos como solução promissora para otimização em texto curto — eco
           direto do nosso P1 (otimização do L0 via AG)."
---

# Review of short-text classification

## Resumo
Revisão de classificação de texto curto (STC) estruturada pelos estágios da tarefa
de classificação (pré-processamento, representação/seleção de atributos,
classificação, avaliação), com as técnicas de cada estágio e tendências. Motivação:
explosão de documentos eletrônicos curtos (redes sociais) e aplicações como
filtragem de spam, análise de sentimento e revisão de clientes. Findings
declarados: as soluções correntes ainda têm desempenho baixo; problemas de baixo
desempenho podem ser atacados com soluções otimizadas, como **algoritmos
genéticos** ("poderosos para melhorar a qualidade dos atributos selecionados") e
soft computing/lógica fuzzy.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | STC é etapa essencial de muitas aplicações, mas revisões dedicadas são escassas | Abstract (Purpose) | Cap.1: relevância do recorte em texto curto |
| C2 | Desempenho corrente em STC é baixo; há espaço para otimização | Abstract (Findings/Value) | Justificativa de pesquisa (Cap.1) |
| C3 | Algoritmos genéticos são apontados como solução poderosa de otimização em STC | Abstract (Findings) | Respaldo bibliográfico do P1 (AG para otimizar o conjunto inicial L0) — a literatura de STC já apontava AG como direção |

## Números que posso citar
- (Revisão qualitativa; 89 referências.)

## Crítica / limitações (minha leitura)
- Foco em redes sociais/microblogs, não em descrições de produto; pré-BERT (2019,
  mas sem transformers).
- O endosso a AG (C3) é genérico (seleção de atributos), não idêntico ao nosso uso
  (seleção de instâncias iniciais) — citar com essa distinção explícita.

## Ideias que gera para a tese
- Usar a organização por estágios como checklist da seção de STC do Cap.2 e
  posicionar onde o FALCO intervém (rotulagem, não representação).
