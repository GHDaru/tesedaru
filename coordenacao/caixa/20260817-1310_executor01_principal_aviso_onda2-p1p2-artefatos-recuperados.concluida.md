---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir se vale investigar a divergência de magnitude do AG (item novo); nenhuma outra ação — sigo para a Onda 3a
referencia: activelearning@b512d3d notebooks/auditoria/conjunto-inicial.ipynb · experiments/p1/results/{replay_l0,replay_ga}.jsonl · docs/records/rastreabilidade.json (72 itens)
criada_em: 2026-08-17T13:10:00Z
---
**Onda 2 concluída.** Os dois artefatos que estavam perdidos desde sempre
(`replay_l0.jsonl`, `replay_ga.jsonl` — achado das 04:00) **existem agora**,
gerados de verdade e commitados com `git add -f`.

## P1 (sensibilidade de L0): confere em todos os 5 pontos publicados

|L0|=10, 100, 1.000, 10.000, 200.000 — divergência máxima de 0,7 p.p., dentro
da folga de 1,0 p.p. que usei (o relatório original, sem artefato, declarava
0,7 p.p.). A amplitude em |L0|=100 é 4,8 p.p. no replay (10 reps) contra 6,4
p.p. no publicado (30 reps) — esperado por ter menos repetições, não é
refutação do fenômeno.

## P2 (AG): um número reproduz exatamente, outro diverge de verdade

**A inflação de circularidade bate igual**: max_f1 em |L0|=500 dá **+6,3
p.p.** no replay — os mesmos 19,4% (partição de aptidão) vs. 13,1% (teste
intocado) que só existiam em texto até hoje.

**O mecanismo do AG diverge em magnitude.** O relatório original dizia que o
AG ganha +5,2 p.p. sobre a média aleatória em |L0|=50. O replay dá **+1,3
p.p.** — mesma direção (o AG vence), mas ~4× menor. Não é arredondamento nem
erro meu que eu tenha encontrado: reportando com precisão, não escondendo
atrás do "mesma direção".

Hipótese não verificada, para o senhor avaliar se vale investigar: o replay
usa grade reduzida (30 gerações × pop 30, um `FITNESS_SET` de 5.000) contra o
desenho original — pode ser só perda de poder da otimização em escala menor,
ou pode ser algo mais. Não fui atrás porque não é a minha missão decidir isso.

## Placar

`rastreabilidade.json`: **72 itens · 59 rastreados · 10 divergentes · 2 sem
evidência · 1 legado**. As 9 divergências anteriores continuam abertas.

## Próximo

**Onda 3a**: reanálise gratuita do E0/E0-P a partir das anotações já
versionadas — sem chave de API, sem custo. É onde a divergência mais grave
(o McNemar do E0/RQ1 com `b=43,c=16` inexistente) pode ganhar mais contexto,
recalculando outras métricas do mesmo artefato bruto.
