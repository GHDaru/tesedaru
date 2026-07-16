---
id: zhang2022surveyAL
title: "A Survey of Active Learning for Natural Language Processing"
authors: ["Zhang, Zhisong", "Strubell, Emma", "Hovy, Eduard"]
year: 2022
venue: "Proceedings of EMNLP 2022, pp. 6166–6190"
doi: "10.18653/v1/2022.emnlp-main.414"
pdf: referencias-pdf/zhang2022surveyAL.pdf
paper_type: survey
pillars: [geral, P2, P4]
status: fichado
proposes: [taxonomia-de-estrategias-de-consulta]
uses_methods: [amostragem-por-incerteza, representatividade, cold-start, criterio-de-parada]
datasets: []
metrics: []
tasks: [classificacao-de-texto, predicao-estruturada]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Settles2012, Ren2021, Lewis1994, Cohn1994Improving]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Survey-espinha-dorsal do Cap.2: organiza estratégias de consulta
           (informatividade vs representatividade), cold-start e parada — exatamente
           os eixos das fases do FALCO. Anterior à era dos LLMs-como-oráculo, o que
           demarca a lacuna que a tese ocupa."
---

# A Survey of Active Learning for Natural Language Processing

## Resumo
Revisão de literatura de aprendizado ativo (AL) aplicada a PLN, centrada no cenário
pool-based (Lewis e Gale, 1994). Formaliza o laço típico de AL (seed → train →
query → annotate → retrain, Algoritmo 1) e propõe categorização fina das
estratégias de consulta em **informatividade** (incerteza de saída — entropia,
least-confidence, margin; divergência local; comprimento esperado de gradiente;
predição de desempenho), **representatividade** (evitar viés amostral e outliers)
e combinações. Cobre ainda temas pouco tratados nos surveys anteriores: AL para
predição estruturada, custo real de anotação, casamento consulta↔modelo sucessor,
combinação com transferência/supervisão fraca/augmentação, e os problemas de
**início (cold-start)** e **parada** do AL. Motivação declarada: os surveys
clássicos de PLN (Settles 2009; Olsson 2009) têm mais de uma década e antecedem o
aprendizado profundo.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Uncertainty sampling é a estratégia mais simples e mais usada; entropia, least-confidence e margin são as três formas típicas | §2.1.1 | Cap.2 taxonomia; justifica as três funções de escore implementadas no `activelearning` |
| C2 | Informatividade isolada sofre de viés amostral e seleção de outliers; representatividade corrige | §2.2 (cita Dasgupta 2011; Roy & McCallum 2001) | Motivação da fase híbrida do FALCO e do DRI-SL (densidade) |
| C3 | Cold-start: seleção da semente influencia fortemente o desempenho inicial; aleatória preserva a distribuição, centroides de clusters dão diversidade | §5.1 | Fundamenta a fase 0 do FALCO (P1: otimização do L0 via AG como alternativa) |
| C4 | Parada: métricas sobre conjunto separado não-rotulado, limiar sobre a *variação* do critério é mais estável que valor absoluto | §5.2 | Critério de parada do FALCO; comparar com nosso orçamento fixo (30% do pool) |
| C5 | É um survey puro, sem experimentos comparativos entre estratégias | Limitations | Posiciona nossa contribuição empírica (E1–E3 comparam estratégias no mesmo dataset) |

## Números que posso citar
- Cobertura: EMNLP 2022, 25 páginas (6166–6190); consolida ~2 décadas de AL
  (desde Lewis & Gale 1994; Cohn et al. 1994).

## Crítica / limitações (minha leitura)
- **Anterior aos LLMs-como-oráculo**: todo o laço assume anotador humano; o custo de
  anotação (§3.2) é modelado como esforço humano. A tese substitui o anotador por
  oráculo LLM ruidoso e instrumentado — lacuna explícita que este survey não cobre.
- Sem resultados empíricos próprios (admitido em Limitations) — não serve como
  fonte de números de desempenho, apenas de organização conceitual.
- Foco em inglês/tarefas gerais de PLN; nada sobre textos curtos ruidosos em
  português nem espaços de rótulos na casa das centenas.

## Ideias que gera para a tese
- Estruturar a seção 2.x de AL do Cap.2 espelhando a taxonomia
  informatividade/representatividade/combinação — e mapear cada fase do FALCO a uma
  célula dessa taxonomia (tabela).
- Usar C4 para discutir por que adotamos orçamento fixo + LCE em vez de critério de
  parada adaptativo (simplicidade experimental; comparabilidade entre estratégias).
- O laço do Algoritmo 1 é o mesmo diagrama-base do hexágono do `activelearning`
  (ports: QueryStrategy, Oracle, Trainer) — citar ao apresentar a arquitetura.
