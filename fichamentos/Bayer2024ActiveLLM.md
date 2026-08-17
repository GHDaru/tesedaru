---
id: Bayer2024ActiveLLM
title: "ActiveLLM: Large Language Model-based Active Learning for Textual Few-Shot Scenarios"
authors: ["Bayer, Markus", "Lutz, Justin", "Reuter, Christian"]
year: 2026
venue: "Transactions of the Association for Computational Linguistics, vol. 14, pp. 1--22 (publicado 1/2026)"
doi: "10.1162/TACL.a.63"
pdf: referencias-pdf/Bayer2024ActiveLLM.pdf
paper_type: metodo
pillars: [P2, P3]
status: fichado
proposes: [llm-como-seletor]
uses_methods: [aprendizado-ativo, few-shot, cold-start]
datasets: [agnews, glue, sst-2]
metrics: [acuracia, macro-f1]
tasks: [classificacao-de-texto]
models: [gpt-4, bert]
extends: []
compares_with: [Yuan2020]   # ALPS = Yuan, Lin & Boyd-Graber (EMNLP 2020); chave correta no bib
contradicts: []
builds_on: [Settles2012]
falco_relation:
  - type: compara
    target: DRI-SL
    note: "ActiveLLM usa o LLM para SELECIONAR instâncias iniciais; DRI-SL seleciona
           sem LLM (cluster semântico + variedade lexical) e usa LLM só para ROTULAR
           — separação que reduz chamadas na fase cara."
  - type: motiva
    target: FALCO
    note: "Demonstra que o cold start é o gargalo das estratégias clássicas em few-shot."
---

# ActiveLLM

## Resumo
Propõe usar LLMs (GPT-4) como agente de SELEÇÃO de instâncias em cenários few-shot,
contornando o cold start: o LLM recebe lotes de instâncias não rotuladas + descrição
da tarefa e escolhe as mais informativas para treinar um modelo menor (BERT).
Reporta superar estratégias clássicas de AL e o SetFit em few-shot.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Estratégias clássicas de AL falham no cold start: sem semente rotulada suficiente, o sistema não consegue estimar incerteza nem diversidade de forma informada | §2.1.3, p. 4 (também no Resumo, p. 1) | Cap. 2 revisão; motivação do P2 |
| C2 | O LLM seleciona instâncias úteis SEM modelo inicial treinado e sem treino durante a anotação; o modelo sucessor é independente do modelo consultor | Resumo, p. 1; §3, p. 5; lacuna declarada em §2.1.3, p. 4 | Cap. 5, trabalhos relacionados |
| C3 | O desenho do prompt é decisivo: os autores parametrizam guidelines, número de instâncias, "advice" e três modos de raciocínio (sem CoT, CoT normal "pense passo a passo", explicação instância a instância) | §3.1 e Fig. 2, p. 5 | Discussão do prompt v3 |
| C4 | No modo de consulta iterada, o histórico entra por três variantes — sem recapitulação, recapitulação direta e recapitulação só dos índices (para poupar contexto); os rótulos anotados NÃO entram, porque os modelos tendiam a ignorá-los | §3.2, p. 6 | Cap. 3: desenho do prompt em lote e limite de contexto |
| C5 | O problema do descasamento de modelos (consultor × sucessor) é conhecido e costuma degradar o ganho do AL — o trabalho o assume de propósito, usando LLM grande para consultar e BERT pequeno para servir | §2.1.2 e Tab. 1, p. 3 | Cap. 2: fundamenta a separação de papéis que o FALCO também faz |

## Números que posso citar
- Cenário few-shot padrão do trabalho: **32 instâncias por tarefa**, selecionadas
  por AL ou por amostragem aleatória (linha de base) — §4.1.1, p. 6.
- Robustez do protocolo: **5 aleatorizações do conjunto × 5 sementes de treino
  do modelo sucessor = 25 execuções**, e o valor reportado é a média (§4.1.1, p. 6).
- Conjuntos usados: CTI especializado (para reduzir vazamento de dados no LLM),
  GLUE, AGNews e SST-2 (§4.1.1, p. 6).
- Referência completa da versão publicada: TACL, vol. 14, pp. 1--22, DOI
  10.1162/TACL.a.63, publicado em 1/2026 (rodapé da p. 1).

## Crítica / limitações
- Selecionar via LLM exige apresentar o pool ao LLM: custo cresce com |U|; FALCO
  evita isso usando o LLM apenas nos itens já selecionados.
- Avaliado em benchmarks em inglês; nada em português nem em comércio eletrônico.
- O próprio desenho admite o descasamento consultor × sucessor (§2.1.2, p. 3), que
  a literatura ali resenhada associa a ganho reduzido — é escolha consciente, não
  descuido, mas continua sendo um risco declarado.
- A anotação é simulada: as instâncias selecionadas recebem o rótulo verdadeiro
  "como se tivessem sido anotadas por um anotador perfeito" (§4.1, p. 6). Ou seja,
  o trabalho NÃO mede erro de oráculo — exatamente o que a tese mede.

## Ideias que gera para a tese
- Comparação de custo: seleção-via-LLM vs seleção-local+rotulagem-via-LLM (FALCO).
