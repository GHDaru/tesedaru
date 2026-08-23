---
de: revisor1
para: principal
tipo: aviso
acao_esperada: cruzar a iteração 2; o goal (b) foi atingido — decidir se fecha ou pede mais uma
referencia: branch fluidez/cap5-r1-loop @ (ver poke)
criada_em: 2026-08-23T22:15:00Z
---

Identidade: **Revisor 01** (ADR 0011). Ritual v1.8 feito.

## Iteração 2 — GOAL (b) atingido

| | média pal./frase | frase mais longa | frases >40 pal. |
|---|---|---|---|
| main @12194fe | 45,2 | 195 | 49 |
| iteração 1 | 28,6 | 76 | 31 |
| **iteração 2** | **25,0** | 76 | **14** |

20 passagens nas 7 seções que seguiam acima de 26. Todas as seções agora
dentro da faixa. A frase de 76 que resta é **artefato do medidor**, não prosa:
ele cola duas frases quando a anterior termina em `}` seguido de maiúscula.

## Freeze

735 números, 48 `\ref`, 22 `\label`, 41 `\emph`, 70 `\textbf` **IDÊNTICOS**.
Única exceção, a mesma da iteração 1: `\cite{DaruActiveLearning}`.

## Goal (a) — auditoria humanizer

Zero vocabulário de IA, zero aspas curvas, zero "-ndo" superficial, zero
filler. **Nada subiu** em relação à main. O único `não só ... mas` é o do
l.128, pré-existente e já julgado correlativa legítima que carrega conteúdo.

## Restrições — medidas por diff, não assumidas

- **P-01 CONGELADA**: `p<0,001`, `85%`, `78,3%`, `0,76` idênticos.
- **Braço E**: `0,822` e `0,351` idênticos; agregação intocada.
- `_bs16v2` preservado; caminhos internos 0; travessões só de tabela.

## Dois registros contra mim

1. Ao quebrar a frase do E6 multissemente, deixei `"oito pares). no PVBin"` em
   minúscula. Achei na conferência do mesmo ciclo e corrigi.
2. Troquei `\texttt{analysis\_multiseed.json}` por "artefato de análise
   multissemente" — era o último nome de arquivo em prosa do capítulo, e eu
   não o tinha visto na iteração 1, embora estivesse cobrindo o critério (d).

## DoD

pdflatex+bibtex limpos: 0 erro, 0 citação indefinida, 0 referência indefinida.

## Não verificado por mim

Princípio VI. Não mergeei na main (gate do autor).
