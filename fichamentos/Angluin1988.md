---
id: Angluin1988
title: "Queries and Concept Learning"
authors: ["Angluin, Dana"]
year: 1988
venue: "Machine Learning, 2, pp. 319–342, Kluwer"
doi: "10.1023/A:1022821128753"
pdf: referencias-pdf/Angluin1988.pdf
paper_type: teoria
pillars: [geral]
status: fichado
proposes: [tipologia-de-consultas, membership-query, equivalence-query]
uses_methods: [analise-formal]
datasets: []
metrics: []
tasks: [aprendizado-de-conceito]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Origem formal da noção de ORÁCULO em aprendizado: o aprendiz tem acesso
           a oráculos que respondem tipos específicos de consulta. O FALCO instancia
           a membership query com um LLM como oráculo falível."
---

# Queries and Concept Learning

## Resumo
Artigo teórico fundador: estuda formalmente o problema de identificar um conceito
desconhecido L* usando **consultas a oráculos** em vez de (ou além de) exemplos
gerados passivamente. Define e analisa seis tipos de consulta — membership,
equivalence, subset, superset, disjointness e exhaustiveness — e dá métodos
eficientes de aprendizado usando subconjuntos desses tipos para domínios formais
(linguagens regulares, subclasses de livres-de-contexto, pattern languages,
fórmulas proposicionais restritas), além de técnicas gerais de cota inferior.
Compara equivalence queries com o critério PAC de Valiant sob amostragem aleatória.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O aprendiz pode ter acesso a um conjunto fixo de oráculos que respondem tipos específicos de consulta sobre o conceito-alvo | Abstract/§1 | Cap.2: definição formal de oráculo; o FALCO usa membership queries ("qual a classe deste x?") |
| C2 | Diferentes tipos de consulta têm poderes distintos; há cotas inferiores | Abstract | Observação de que a escolha do TIPO de interação com o oráculo importa — paralelo com nossos modos de instrumentação (enum/json/free, RQ4) |

## Números que posso citar
- (Teórico; citar apenas definições e a tipologia de consultas.)

## Crítica / limitações (minha leitura)
- Oráculos assumidos CORRETOS por definição; domínios formais. Serve para ancorar
  terminologia, não para prever comportamento de oráculo LLM estatístico.

## Ideias que gera para a tese
- Nota histórica no Cap.2: "oráculo" não é metáfora nossa — é o termo técnico
  desde Angluin (1988); a novidade do FALCO é o oráculo ser um modelo generativo
  com taxa de erro mensurável e custo por token.
