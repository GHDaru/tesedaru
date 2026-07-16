---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: ChaveBibtex            # = chave em referencias.bib (ID do nó)
title: ""
authors: []                # ["Sobrenome, Nome", ...]
year: 2026
venue: ""                  # periódico/conferência/arXiv
doi: ""
pdf: referencias-pdf/arquivo.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo         # metodo | survey | dataset | avaliacao | posicao
pillars: [P3]              # pilares da tese que toca: P1..P4, LCE, geral
status: fichado            # a-ler | lido | fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: []               # métodos/algoritmos/métricas PROPOSTOS aqui
uses_methods: []           # métodos usados (não propostos)
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []                 # LLMs/classificadores empregados

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: compara          # compara | fundamenta | motiva | ameaca | complementa
    target: ""             # ex.: DRI-SL, oraculo-progressivo, LCE, FALCO
    note: ""
---

# {title}

## Resumo (5-8 linhas, com as MINHAS palavras)

## Claims relevantes
<!-- Cada claim = potencial nó do grafo e potencial citação na tese.
     evidencia = onde está no paper (seção/tabela/página). -->
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 |  | §, Tab., p. | cap./seção |

## Números que posso citar
<!-- resultados quantitativos exatos, com condições -->

## Citações diretas (com página)
> "" (p. )

## Crítica / limitações (minha leitura)

## Ideias que gera para a tese
