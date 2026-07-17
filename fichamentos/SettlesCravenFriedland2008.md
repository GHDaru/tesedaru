---
id: SettlesCravenFriedland2008
title: "Active Learning with Real Annotation Costs"
authors: ["Settles, Burr", "Craven, Mark", "Friedland, Lewis"]
year: 2008
venue: "NIPS Workshop on Cost-Sensitive Learning"
doi: ""
pdf: referencias-pdf/SettlesCravenFriedland2008.pdf
paper_type: avaliacao
pillars: [P3]
status: fichado
proposes: [al-sensivel-a-custo]
uses_methods: [aprendizado-ativo, medicao-de-custo-real]
datasets: [quatro-dominios-com-custo-real]
metrics: [custo-de-anotacao]
tasks: [anotacao]
models: []
extends: [Settles2012]
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "O artigo que quebra a suposição 'todo rótulo custa igual' com custos
           REAIS de anotação: fundamento direto da contabilidade de custo por
           consulta do FALCO (OracleUsage em US$/token) — reduzir número de
           rótulos não garante reduzir CUSTO."
---

# Active Learning with Real Annotation Costs

## Resumo
Settles, Craven e Friedland (NIPS WS 2008) estudam AL com **custos reais de
anotação** medidos com anotadores humanos em quatro domínios. Diagnóstico
central: quase toda a pesquisa em AL assume custo uniforme por rótulo; onde os
custos variam, **reduzir o número de instâncias rotuladas não garante reduzir o
custo total de treinamento**. Analisam a variabilidade empírica dos custos e
abordagens de AL sensíveis a custo.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Menos rótulos ≠ menos custo quando o custo por rótulo varia | Abstract | Pedra angular do P3: o FALCO otimiza CUSTO (US$), não contagem de rótulos — LCE + custo/1k como par de métricas |
| C2 | Custos reais de anotação variam substancialmente entre instâncias e anotadores | Corpo (4 domínios) | Cap.2: com LLM o custo também varia por instância (tokens de entrada/saída, cache) — mesma lógica, nova moeda |

## Números que posso citar
- (Custos dos 4 domínios se necessário; o argumento conceitual basta.)

## Crítica / limitações (minha leitura)
- Custo humano em tempo; nossa moeda é token/US$ com estrutura diferente (cache
  compartilhado entre instâncias do lote — não previsto em 2008).

## Ideias que gera para a tese
- Citar C1 na definição da métrica de custo do Cap.3 — legitima medir US$/1k
  rótulos como objetivo primário, com linhagem desde 2008.
