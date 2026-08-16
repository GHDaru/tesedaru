---
id: Bayer2024ActiveLLM
title: "ActiveLLM: Large Language Model-based Active Learning for Textual Few-Shot Scenarios"
authors: ["Bayer, Markus", "Reuter, Christian"]
year: 2026
venue: "Transactions of the ACL"
doi: "10.1162/TACL.a.63"
pdf: referencias-pdf/Bayer2024ActiveLLM.pdf
paper_type: metodo
pillars: [P2, P3]
status: fichado
proposes: [llm-como-seletor]
uses_methods: [aprendizado-ativo, few-shot, cold-start]
datasets: []
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
| C1 | Estratégias clássicas de AL falham no cold start few-shot | (preencher c/ PDF final) | Cap.2 revisão; motivação P2 |
| C2 | LLM seleciona instâncias úteis sem modelo inicial treinado | idem | Cap.5 trabalhos relacionados |
| C3 | Prompting importa: CoT e recap de seleções anteriores | idem | Discussão de prompt v3 |

## Números que posso citar
(preencher com a versão TACL final — P1 da lista de PDFs)

## Crítica / limitações
- Selecionar via LLM exige apresentar o pool ao LLM: custo cresce com |U|; FALCO
  evita isso usando o LLM apenas nos itens já selecionados.
- Avaliado em benchmarks em inglês; nada em português/e-commerce.

## Ideias que gera para a tese
- Comparação de custo: seleção-via-LLM vs seleção-local+rotulagem-via-LLM (FALCO).
