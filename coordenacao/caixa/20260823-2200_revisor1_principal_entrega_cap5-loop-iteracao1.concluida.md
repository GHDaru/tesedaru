---
de: revisor1
para: principal
tipo: aviso
acao_esperada: cruzar a iteração 1 e re-kickar para a iteração 2 (falta chegar a 20–26 e fechar R1–R6/humanizer)
referencia: branch fluidez/cap5-r1-loop @ 8e6cdcd
criada_em: 2026-08-23T22:00:00Z
---

Identidade: **Revisor 01** (ADR 0011). Ritual v1.8 feito. Parti da main atual
(@12194fe), não do fork antigo.

## Iteração 1 — medido

| | média pal./frase | frase mais longa | frases >40 pal. |
|---|---|---|---|
| main @12194fe | 45,2 | 195 | 49 |
| **iteração 1** | **28,6** | **76** | **31** |

30 passagens reescritas nas 8 seções mais densas (RQ1–RQ4, E1, E4, E6, E3,
gate). **Ainda NÃO cheguei ao goal (b)**: falta descer de 28,6 para 20–26 e
fechar a auditoria humanizer completa. Peço re-kick.

## Freeze — no critério que você pediu

735 números, 48 `\ref`, 22 `\label`, 41 `\emph`, 70 `\textbf` **IDÊNTICOS**.
Única exceção, declarada e autorizada pelo critério (d): **+1**
`\cite{DaruActiveLearning}`.

## Restrições respeitadas, e medidas

- **P-01 CONGELADA**: conferi por diff que os números do gate (`p<0,001`,
  `85%`, `78,3%`, `0,76`) saem idênticos. Só a FORMA da seção mudou.
- **tab:e3p / tab:e6**: legendas e agregações intocadas; `_bs16v2` preservado.
- Títulos RQ1–RQ4 no padrão gateado.
- **Travessões**: os 4 continuam sendo os 4 de TABELA; zero em prosa.
- Caminhos internos: 0 (já estavam limpos antes de mim).

## Critério (d) — o ponteiro órfão se repetiu no Cap.5

A abertura dizia que os números são rastreáveis a *"artefatos versionados que
acompanham o repositório de código da tese"*, **sem dizer qual repositório** —
exatamente o problema que achei no Cap.3. Ancorei em `\texttt{activelearning}
\cite{DaruActiveLearning}`, que é a rota que você mesmo pôs no critério (d).

## TRÊS bugs de medição corrigidos (todos davam número BOM por engano)

1. **`\$` escapado não é delimitador de matemática.** O Cap.5 tem 4 deles; o
   stripper tratava cada um como abre/fecha, deslocava a paridade e engolia
   parágrafos inteiros. Sintoma: o Cap.5 media **"11 frases" num arquivo de 714
   linhas**. Se eu tivesse confiado, teria reportado o capítulo como quase
   pronto. O baseline real era 45,2.
2. **O `mede-freeze-tex.py` que está na main estava sem a linha de `import`** e
   quebrava ao ser chamado — o DoD de freeze não era executável (princípio IX).
   Eu já havia corrigido em `dc4f4b7`, mas o commit único não levou a correção.
   Vai de novo aqui.
3. O freeze passa a cobrir **`\emph` e `\textbf`**, como você pediu.

## DoD

pdflatex+bibtex limpos: 0 erro, 0 citação indefinida, 0 referência indefinida,
104 páginas.

## Não verificado por mim

Princípio VI. Não mergeei na main (gate do autor).
