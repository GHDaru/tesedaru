---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma decisão nova — fecha com confiança máxima o achado das 04:30; o Cap. 5/RQ1 precisa de correção de prosa
referencia: activelearning notebooks/auditoria/escolha-do-oraculo.ipynb · experiments/e0/analyze_e0.py
criada_em: 2026-08-17T13:35:00Z
---
**Onda 3a concluída** — E0, reanálise sem custo (as anotações cruas já
estavam versionadas). Não recomputei um número isolado: rodei o **script real
de produção** (`analyze_e0.py`) sobre os dados brutos, do zero.

## Resultado: zero divergências no pipeline inteiro

13 de 13 linhas da tabela e **43 de 43 pares de McNemar** idênticos ao
artefato commitado. Isso muda a categoria do achado das 04:30: não é
possível mais atribuí-lo a artefato desatualizado ou script que mudou depois.
**O `e0_mcnemar.json` é exatamente o que o código de hoje produz a partir das
respostas reais do LLM.**

Recomputado agora, do zero: v4-pro × v4-flash na S-strat dá **b=73, c=91,
p=0,1844 — não significativo**. Procurei `b=43/c=16` nos 43 pares
recomputados: **não existe**, igual ao artefato. A frase do Cap. 5, RQ1 —
"significativamente superior... b=43, c=16, p<0,001" — não tem lastro em
nenhuma versão do dado, publicada ou recém-calculada.

## O que isso pede

Como pedi às 04:30: é decisão sua e do autor, mas agora com o grau mais alto
de confiança que eu consigo dar. Ou os números vieram de uma execução que
nunca existiu neste repositório, ou há um erro de transcrição no texto. Nos
dois casos, a leitura (i) do Cap. 5 — que há hierarquia dentro do platô de
oráculos — perde o único suporte estatístico que a diferenciava de um empate
quádruplo.

## Próximo

Onda 3a continua com o **E0-P**, que também tem anotação crua versionada.
Depois, Onda 4 (E1/E4 — já rastreados, falta notebook próprio e o
`sweeps.jsonl`) e Onda 5 (índice).
