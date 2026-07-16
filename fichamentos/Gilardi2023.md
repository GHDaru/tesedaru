---
id: Gilardi2023
title: "ChatGPT outperforms crowd-workers for text-annotation tasks"
authors: ["Gilardi, Fabrizio", "Alizadeh, Meysam", "Kubli, Maël"]
year: 2023
venue: "Proceedings of the National Academy of Sciences (PNAS)"
doi: "10.1073/pnas.2305016120"
pdf: referencias-pdf/Gilardi2023.pdf
paper_type: avaliacao
pillars: [P3]
status: fichado
proposes: []
uses_methods: [llm-como-oraculo, zero-shot]
datasets: []
metrics: [acuracia, custo-por-rotulo]
tasks: [anotacao-de-texto]
models: [chatgpt]
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Evidência seminal de que LLMs superam crowd-workers em custo e acurácia
           de anotação — premissa do oráculo LLM do FALCO. Mas avalia tarefas com
           poucas classes (relevância/postura/tópicos), não 621 categorias."
---

# ChatGPT outperforms crowd-workers for text-annotation tasks

## Resumo
Compara ChatGPT zero-shot com crowd-workers (MTurk) e anotadores treinados em quatro
amostras de tweets e notícias (n=6.183), nas tarefas de relevância, postura
(stance), tópicos e enquadramento. ChatGPT supera crowd-workers em acurácia (~25
pontos percentuais em média) e supera ambos em concordância intercodificador, a um
custo por anotação ~30x menor que o MTurk. Conclui que LLMs podem aumentar
drasticamente a eficiência da rotulagem de texto.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Zero-shot do ChatGPT excede crowd-workers em ~25 p.p. de acurácia média | Abstract; §Resultados (n=6.183) | Cap.2 (LLM como oráculo); motivação P3 |
| C2 | Custo por anotação < US$0,003, ~30x mais barato que MTurk | Abstract | Cap.5 análise de custo (comparar com nossos custos/1k) |
| C3 | Concordância intercodificador do LLM excede a de anotadores treinados | Abstract | Discussão sobre consistência do oráculo (temp=0) |

## Números que posso citar
- n = 6.183 (tweets + notícias, 4 amostras); +25 p.p. vs crowd-workers (média);
  < US$0,003/anotação (~30x mais barato que MTurk).

## Crítica / limitações (minha leitura)
- Tarefas com POUCAS classes; nada comparável ao nosso espaço de 621 categorias —
  nossos pilotos mostram acurácias bem menores nesse regime, o que delimita a
  generalização do claim C1.
- Zero-shot sem saída estruturada; sem análise de efeito do instrumento (nosso RQ4).

## Ideias que gera para a tese
- Usar C2 como âncora de comparação de custo: nosso custo/1k rótulos (com cache e
  lote) vs MTurk vs anotador especializado — tabela do Cap.5.
