---
id: McNemar1947
title: "Note on the sampling error of the difference between correlated proportions or percentages"
authors: ["McNemar, Quinn"]
year: 1947
venue: "Psychometrika, v. 12, n. 2, pp. 153--157"

paper_type: canonica
status: ficha-minima
ficha_minima_motivo: "ADR 0012, adendo das estatísticas — obra canônica que a banca argui"

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Teste pareado que opera SÓ sobre os pares discordantes (b e c), usado
           em toda comparação entre dois oráculos sobre as mesmas instâncias."
---

# McNemar (1947) — ficha mínima

**O que a tese usa:** o teste de McNemar para duas proporções correlacionadas —
dois classificadores avaliados nas MESMAS instâncias.

**Onde:** `2-fundam/texto.tex:164` (definição, com a observação de que o teste
correto opera sobre os pares discordantes), `2-fundam/texto.tex:200` (tabela de
decisão, com a regra do binomial exato quando b+c < 25) e
`3-metodo/texto.tex:250` (aplicação nos pareamentos E0/E0-P).

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Com amostras pareadas, o erro amostral da diferença entre proporções correlacionadas depende apenas das discordâncias; ignorar o pareamento infla o erro | McNemar (1947), pp. 153--157 | Sustenta o uso do teste pareado nas comparações de oráculos |

**Por que basta uma linha:** resultado consagrado, citado como definição.
ADR 0012 item 3 devolve a obra à regra cheia se alguma afirmação passar a
depender do conteúdo específico do artigo.
