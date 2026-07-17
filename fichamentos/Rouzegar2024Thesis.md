---
id: Rouzegar2024Thesis
title: "LLM-Powered Active Learning for Cost-Effective Text Classification"
authors: ["Rouzegar, Hamidreza"]
year: 2024
venue: "Dissertação de mestrado, Ontario Tech University (expande arXiv:2406.12114 com Makrehchi)"
doi: ""
pdf: referencias-pdf/Rouzegar2024Thesis.pdf
paper_type: dissertacao
pillars: [P3, P4]
status: fichado
proposes: [picr-criterio-de-parada, anotacao-hibrida-humano-llm, role-based-prompting]
uses_methods: [llm-como-oraculo, amostragem-por-incerteza, confidence-scoring]
datasets: []
metrics: [acuracia, custo-por-rotulo]
tasks: [classificacao-de-texto]
models: [gpt-3.5, gpt-4]
extends: []
compares_with: [Gilardi2023]
contradicts: []
builds_on: [Lewis1994, Gilardi2023]
falco_relation:
  - type: compete
    target: FALCO
    note: "Trabalho mais próximo do FALCO na literatura fichada: AL + oráculo LLM +
           foco explícito em custo. Diferenças-chave: roteia por CONFIANÇA entre
           humano e LLM no mesmo estágio (FALCO faz o oráculo EVOLUIR entre fases);
           tarefas com poucas classes vs nossas 621; sem saída estruturada
           instrumentada nem análise de efeito do instrumento."
---

# LLM-Powered Active Learning for Cost-Effective Text Classification

## Resumo
Dissertação (99 pp.) que propõe um framework de AL com oráculo LLM para
classificação de texto com custo controlado, atacando diretamente o problema dos
**erros de anotação do LLM**. Mecânica: parte de um seed rotulado pequeno; a cada
iteração, uncertainty sampling seleciona os pontos mais informativos; a anotação é
**híbrida humano+LLM mediada por confidence scoring** (o LLM anota quando confia;
casos difíceis vão ao humano). Um *proxy validation set* dinamicamente atualizado
espelha a distribuição do pool não-rotulado para estimar desempenho sem gastar
rótulos de teste. Introduz o **PICR (Performance Improvement Cost Ratio)** como
critério de parada objetivo que equilibra custo × ganho de acurácia, e usa
**role-based prompting** para melhorar a qualidade da anotação. Resultados:
desempenho comparável ao humano com custos reduzidos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Roteamento por confiança entre LLM e humano equilibra qualidade e custo | Abstract | Cap.2 (AL+LLM); contraste direto com a progressão de oráculo do FALCO — citar como alternativa de desenho |
| C2 | PICR como critério de parada custo-consciente | Abstract | Cap.2/Cap.5: comparar com nosso orçamento fixo + LCE; PICR é candidato a trabalho futuro do FALCO |
| C3 | Proxy validation set dinâmico evita gastar rótulos em validação | Abstract | Ideia aproveitável no E3 (validação sem consumir orçamento de oráculo) |
| C4 | Role-based prompting melhora qualidade de anotação | Abstract | Conecta com nosso prompt v3 (contexto de domínio + persona) |

## Números que posso citar
- (Extrair da seção de resultados quando citada numericamente — a tese usa
  GPT-3.5/GPT-4 em benchmarks de classificação com poucas classes.)

## Crítica / limitações (minha leitura)
- Espaço de rótulos pequeno (benchmarks padrão); nada no regime de centenas de
  classes com enum estruturado — nosso E0 mostra que é outro problema.
- A confiança auto-reportada de LLMs é mal calibrada (nosso RQ na instrumentação);
  o roteamento por confiança herda esse risco sem quantificá-lo.
- Ainda depende de humano no laço; o FALCO investiga o extremo 100% LLM com
  robustez a ruído (E4).

## Ideias que gera para a tese
- Tabela comparativa no Cap.2: Rouzegar (paralelo humano+LLM por confiança) vs
  Qi 2026 (mixture-of-LLMs paralelo) vs FALCO (progressão sequencial de oráculo) —
  três topologias de composição de oráculo.
- PICR como métrica secundária reportável nos E3 (barato de calcular a posteriori).
