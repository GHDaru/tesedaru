---
id: Olsson2009
title: "A literature survey of active machine learning in the context of natural language processing"
authors: ["Olsson, Fredrik"]
year: 2009
venue: "SICS Technical Report T2009:06, Swedish Institute of Computer Science"
doi: ""
pdf: referencias-pdf/Olsson2009.pdf
paper_type: survey
pillars: [geral]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo]
datasets: []
metrics: []
tasks: [classificacao-de-texto, ner, extracao-de-informacao, pos-tagging]
models: []
extends: []
compares_with: [Settles2012]
contradicts: []
builds_on: [Lewis1994, Cohn1994Improving]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Um dos dois surveys clássicos de AL para PLN (com Settles 2009/2012).
           Define o oráculo como 'tipicamente um humano com conhecimento extenso
           do domínio' — a formulação que a era LLM (e o FALCO) revisita."
---

# A literature survey of active machine learning in the context of NLP

## Resumo
Survey técnico (59 pp., SICS 2009) de aprendizado ativo aplicado a PLN. Define AL
como técnica supervisionada em que **o aprendiz controla os dados de treino**,
consultando um oráculo ("tipicamente um humano com conhecimento extenso do
domínio") sobre as classes das instâncias em que o modelo corrente é pouco
confiável. Entrada: poucos rotulados + muitos não-rotulados; saída: um
classificador e um conjunto pequeno de dados recém-rotulados. Objetivo declarado:
manter o esforço humano de anotação no mínimo, consultando apenas onde a
utilidade de treino é alta. Cobre aplicações em extração de informação, NER,
categorização de texto, POS tagging, parsing e desambiguação de sentido.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL bem-sucedido em várias tarefas de PLN já em 2009, incluindo categorização de texto | Abstract | Cap.2: historicidade do AL em PLN antes do deep learning |
| C2 | Oráculo = humano especialista; o objetivo é minimizar esforço HUMANO | Abstract | Contraste com FALCO: quando o oráculo vira LLM, o objetivo muda de esforço para custo monetário/token — reformulação explícita no Cap.3 |

## Números que posso citar
- (Survey qualitativo; usar como marco histórico junto de Settles.)

## Crítica / limitações (minha leitura)
- Pré-deep learning (2009): estratégias sobre modelos rasos; committee-based
  ganha destaque que hoje é menor. Citar apenas como fundamento histórico —
  zhang-etal-2022-survey já constata que esses surveys têm mais de uma década.

## Ideias que gera para a tese
- Par de citações de abertura da seção de AL do Cap.2: Settles (2009/2012) +
  Olsson (2009) como os dois surveys canônicos pré-DL, seguidos por Ren (2021,
  DeepAL) e Zhang et al. (2022, NLP) — a linha do tempo completa dos surveys.
