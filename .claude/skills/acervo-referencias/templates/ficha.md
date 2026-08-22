---
# ===== IDENTIDADE (nó Paper) — estágio 2 =====
id: ChaveBibtex
title: ""
authors: []
year: 0
venue: null
doi: null
pdf: pdf/ChaveBibtex.pdf
paginas: 0
idioma: en

# prova de que cada campo acima foi transcrito, não inventado
_fonte:
  title: null
  authors: null
  year: null
  venue: null
  doi: null

# ===== CLASSIFICAÇÃO — estágio 2 =====
paper_type: metodo        # metodo|survey|dataset|avaliacao|posicao|livro|tese
pillars: []               # P1..P4 | LCE | geral
status: a-ler             # a-ler|convertido|metadados|resumido|aguarda-tese|fichado
canonica: false           # ADR 0012 — livro ou obra pré-2010 por definição consagrada

# ===== ENTIDADES (só termos do _VOCABULARIO.md) — estágio 2 =====
proposes: []
uses_methods: []
datasets: []
metrics: []
tasks: []
models: []

# ===== RELAÇÕES PAPER→PAPER — preenchidas no estágio 5 =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE — estágio 4 =====
falco_relation: []
#  - type: compara        # compara|fundamenta|motiva|ameaca|complementa
#    target: FALCO
#    note: ""
cited_in: []              # capítulos da tese que já citam esta chave (vem do insumo)
---

# {title}

## Resumo (5–8 linhas, minhas palavras) — estágio 3

<!-- problema · o que o trabalho faz · resultado principal · sob que condição.
     Copiar o abstract reprova no portão 3, e com razão. -->

## Claims relevantes — estágio 3 (evidência) + estágio 4 (uso)

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 |  | §, Tab., FIG-NN, p. | cap./seção |

## Números que posso citar — estágio 3

<!-- valor exato COM as condições: dataset, métrica, orçamento, semente.
     Ex.: 0,884 macro-F1 · AG News · 500 rótulos · média de 5 sementes (Tab. 2) -->

| Valor | Métrica | Condições | Onde |
|---|---|---|---|
|  |  |  | Tab. , p.  |

## Citações diretas (com página)

> "" (p. )

## Crítica / limitações (minha leitura)

<!-- marcada como minha: é interpretação, não achado do artigo -->

## Ideias que gera para a tese

## Relações
<!-- GERADO pelo build_kg.py a partir do front-matter. NÃO editar à mão:
     a fonte de verdade é o YAML acima. -->
