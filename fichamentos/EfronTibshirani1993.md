---
id: EfronTibshirani1993
title: "An Introduction to the Bootstrap"
authors: ["Efron, Bradley", "Tibshirani, Robert J."]
year: 1993
venue: "Chapman & Hall/CRC"

paper_type: canonica
status: ficha-minima
ficha_minima_motivo: "ADR 0012, adendo das estatísticas — obra canônica que a banca argui"

falco_relation:
  - type: fundamenta
    target: LCE
    note: "Intervalo de confiança bootstrap percentil para funcional sem
           distribuição conhecida — é como a tese põe barra de erro na
           diferença de LCE (E3)."
---

# Efron e Tibshirani (1993) — ficha mínima

**O que a tese usa:** o intervalo de confiança bootstrap por percentil, aplicado
a um funcional cuja distribuição amostral não é conhecida em forma fechada.

**Onde:** `2-fundam/texto.tex:184` (definição do bootstrap como estimador do
intervalo) e `2-fundam/texto.tex:202` (linha da tabela de decisão: funcional sem
distribuição conhecida → IC bootstrap percentil, aplicado à diferença de LCE
no E3).

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Reamostrando com reposição é possível estimar a distribuição amostral de um funcional arbitrário e daí extrair intervalo de confiança, sem forma fechada | Efron e Tibshirani (1993), livro-texto | Sustenta o IC da diferença de LCE (E3) |

**Por que basta uma linha:** livro-texto citado para método consagrado — é
exatamente o caso que a ADR 0012 desobriga de fichamento integral (ler 436
páginas para sustentar uma definição seria desproporcional).
