---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Schick2023
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
authors: ["Schick, Timo", "Dwivedi-Yu, Jane", "Dessì, Roberto", "Raileanu, Roberta", "Lomeli, Maria", "Zettlemoyer, Luke", "Cancedda, Nicola", "Scialom, Thomas"]
year: 2023
venue: "arXiv preprint arXiv:2302.04761"
doi: ""
pdf: referencias-pdf/Schick2023.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P3]
status: fichado

# ===== ENTIDADES =====
proposes: [uso-de-ferramentas]
uses_methods: [auto-supervisao, few-shot, zero-shot, fine-tuning]
datasets: []
metrics: [acuracia]
tasks: [resposta-a-perguntas]
models: [gpt-j, gpt-3]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: complementa
    target: llm-como-oraculo
    note: "mostra que um LLM pode aprender, por auto-supervisão, a decidir QUAIS ferramentas chamar, quando e com que argumentos — é a família dos sistemas compostos discutida na §2.3, não a seleção ativa de prompts"
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

## Resumo (5-8 linhas, com as MINHAS palavras)

O Toolformer treina um modelo de linguagem para intercalar, no próprio texto que
gera, chamadas a ferramentas externas — calculadora, busca, tradutor, calendário,
sistema de perguntas e respostas. O que há de novo é o modo de obter os dados de
treino: em vez de anotação humana, o próprio modelo propõe chamadas candidatas a
partir de poucas demonstrações por API, executa-as, e **mantém apenas as que
reduzem a perplexidade** da continuação do texto. O treinamento final é o mesmo
objetivo de modelagem de linguagem, sobre esse corpus enriquecido, o que preserva
a generalidade do modelo. Com 6,7 bilhões de parâmetros, o resultado supera uma
GPT-3 muito maior em várias tarefas de tiro zero.

## Claims relevantes

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Um LLM pode ser treinado para decidir **quais APIs chamar, quando chamá-las, quais argumentos passar** e como incorporar o resultado — de forma auto-supervisionada, com poucas demonstrações por API | Resumo, p. 1 | §2.3 — família dos sistemas compostos (LLM que orquestra recursos externos) |
| C2 | O critério de seleção dos exemplos de treino é utilitário e automático: mantém-se a chamada que **reduz a perplexidade** da continuação | §2 (abordagem), p. 2-3 | Cap. 3 — exemplo de sinal automático substituindo anotação humana |
| C3 | Toolformer com 6,7B supera "um modelo GPT-3 muito maior" em tiro zero em várias tarefas | §1, p. 2 (e Tabelas de resultados) | Cap. 2 — capacidade não é só escala; o instrumento importa |

## Números que posso citar

- Modelo base **GPT-J, 6,7 bilhões** de parâmetros; comparação declarada contra
  **GPT-3 (175B)** (p. 2 e tabela da p. ~7). Condição: avaliação em tiro zero,
  tarefas onde a ferramenta é útil.
- **Não** transcrevo aqui as taxas por tarefa: o ganho é fortemente dependente da
  tarefa e da ferramenta, e um número único seria enganoso.

## Citações diretas (com página)

> "Toolformer, a model trained to decide which APIs to call, when to call them,
> what arguments to pass, and how to best incorporate the results into future
> token prediction. This is done in a self-supervised way, requiring nothing more
> than a handful of demonstrations for each API." (p. 1)

## Crítica / limitações (minha leitura)

**Achado de citação, verificado.** A §2.3 cita esta obra ao lado de `Diao2023`
para sustentar que "a própria escolha de \textit{prompts} pode ser ativa"
(l. 611). Medi: a expressão "active learning" aparece **zero** vezes neste
paper. O que o Toolformer decide ativamente é **qual ferramenta chamar**, não
qual \textit{prompt} ou qual exemplo anotar; e o critério é auto-supervisão por
perplexidade, não incerteza de aprendizado ativo. `Diao2023` sustenta a frase
com precisão; `Schick2023` sustenta **outra** afirmação, verdadeira e útil, que a
própria §2.3 já faz alguns parágrafos antes: a dos sistemas compostos, em que o
LLM orquestra recursos externos.

Portanto a recomendação **não** é remover a obra — é movê-la para a afirmação que
ela sustenta. Levado ao principal; não editei prosa.

Limite adicional: é pré-impressão de 2023 sem DOI, e a `paper_type` foi marcada
como `metodo` porque é o que descreve — mas cabe registrar que não passou por
revisão por pares na forma citada.

## Ideias que gera para a tese

O C2 é o que mais interessa ao nosso método: o Toolformer troca anotação humana
por um **sinal automático de utilidade** (perplexidade da continuação). É o mesmo
movimento que fazemos ao usar o oráculo LLM em lugar do anotador — e nomear essa
semelhança fortalece a §2.3, que hoje trata as duas coisas em parágrafos
separados sem ligá-las.
