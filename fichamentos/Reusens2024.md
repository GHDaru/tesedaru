---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Reusens2024
title: "Evaluating text classification: A benchmark study"
authors: ["Reusens, Manon", "Stevens, Alexander", "Tonglet, Jonathan", "De Smedt, Johannes", "Verbeke, Wouter", "vanden Broucke, Seppe", "Baesens, Bart"]
year: 2024
venue: "Expert Systems with Applications, v. 254, p. 124302"
doi: "10.1016/j.eswa.2024.124302"
pdf: referencias-pdf/Reusens2024.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: avaliacao
pillars: [P4]
status: ficha-minima

# ===== ENTIDADES =====
proposes: []
uses_methods: [fine-tuning]
datasets: []
metrics: [acuracia, macro-f1]
tasks: [classificacao-de-texto]
models: [bert, roberta-base]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "benchmark imparcial que mostra que os maiores modelos do estado da arte NÃO são sempre preferíveis e que métodos simples competem em vários casos — sustenta a escolha desta tese de usar um classificador de porte médio (BERTimbau) em vez do maior LLM disponível"
---

# Evaluating text classification: A benchmark study

**Ficha mínima** (padrão do ciclo 008): registra o resultado que a tese usa e
onde. Lida na versão de acesso aberto do repositório institucional da KU Leuven
(48 pp.), com autoria conferida contra o `.bib`.

## O resultado que a tese pode usar

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Benchmark imparcial de classificação de texto com **5 tarefas, 20 conjuntos de dados, 11 arquiteturas e 42.800 execuções**; a hipótese testada é que os maiores modelos do estado da arte não são sempre necessários, e o objetivo é achar os casos em que métodos simples competem | Resumo, p. 1 | Cap. 2 e Cap. 3 — sustenta a decisão de instrumento desta tese (classificador de porte médio, não o maior modelo) |

## ACHADO: a citação atual não é sustentada por esta obra

A §2.1 (`2-fundam/texto.tex:134`) cita esta obra ao lado de `Nti2021` para
afirmar "com $k$ tipicamente 5 ou 10, equilíbrio entre viés, variância e custo".
**Medi no PDF: a palavra "fold" aparece uma única vez em todo o artigo, dentro da
expressão "threefold"** (uso retórico, p. ~28), e a seção 3 (Metodologia) trata
de **seleção de conjuntos de dados**, não de validação cruzada. O artigo não
discute escolha de $k$, nem o compromisso viés-variância-custo do $k$-fold.

`Nti2021` sustenta a afirmação com precisão — conferi no PDF em ciclo anterior:
diz literalmente "$k$ tipicamente 5 ou 10" e admite que "there is no formal
rule". Portanto a frase **não fica órfã** se esta chave sair dela.

**Recomendação: mover, não remover.** A obra sustenta uma afirmação diferente e
muito pertinente à tese — que o maior modelo não é sempre o melhor —, que é
exatamente o argumento de instrumento do Cap. 3. Levado ao principal; não editei
prosa.

## Nota de bibliografia (já corrigida no gate do bib)

Esta entrada era a que declarava o DOI `10.1016/j.eswa.2024.124168`, que abria
outro artigo ("DeepPepPI"). O DOI correto — `10.1016/j.eswa.2024.124302`, v. 254,
p. 124302 — e o autor faltante (Verbeke) já entraram no gate `7f8e2b2`.
Confirmei os sete autores contra a folha de rosto do PDF: batem.
