---
de: revisor2
para: principal
tipo: entrega
acao_esperada: levar ao autor a decisao dec-cap4-L0-100-valor-canonico CORRIGIDA — o valor canonico do executor02 esta certo, mas a linha tem 4 celulas a trocar, nao 1. Aprovar so a troca 38,76->36,71 deixa a linha MISTURADA entre duas geracoes de artefato (pior que hoje).
referencia: tarefa 1800 (executor02) · plano v85 dec-cap4-L0-100-valor-canonico · meu achado 0744 · main @8ee6778 · activetextclassification @b540533
criada_em: 2026-08-22T19:30:00Z
---

# Veredito: APROVADO no merito, com correcao de escopo

O canonico do executor02 esta CERTO: `_100old` e a geracao valida. Reproduzi os
numeros com parser de CSV real (nao `cut`, que quebra em campo com virgula
entre aspas — `"CHOC BARRA GAROTO 90G, CORES"` me deu NA falso na 1a passada).

Mas a recomendacao escrita na decisao — "aprovar a troca 38,76->36,71 e
despachar a correcao de 1 linha" — nomeia UM valor. A linha tem QUATRO celulas
vindas da geracao errada. Executada ao pe da letra, a linha fica misturada
entre `_100oldold` (3 celulas) e `_100old` (1 celula) — internamente pior que
hoje, que ao menos e consistente com uma unica geracao.

## A linha inteira (`4-resultados-l0/texto.tex`, tab:drisl-vs-ag, l.117)

HOJE:      `100 & 41,23\% & 6,85\% & 38,76\% & 6,51\% & 5,75\%  & 1,81\% \\`
CORRIGIDA: `100 & 41,23\% & 6,85\% & 36,71\% & 5,39\% & 10,86\% & 1,19\% \\`

| celula | hoje (`_100oldold`) | canonico (`_100old`) | direcao |
|---|---|---|---|
| AG melhor Acc | 38,76% | **36,71%** | cai |
| AG melhor Macro F1 | 6,51% | **5,39%** | cai |
| AG pior Acc | 5,75% | **10,86%** | **SOBE** |
| AG pior Macro F1 | 1,81% | **1,19%** | cai |

A coluna do PIOR anda no sentido CONTRARIO ao do melhor. Nao da para descrever
a correcao como "o AG cai": o envelope ESTREITA dos dois lados.

## A alegacao central sobrevive e melhora nas DUAS metricas

DRI-SL vs AG-melhor em I=100: acuracia 41,23 vs 36,71 = **+4,52 p.p.** (era
+2,47); Macro F1 6,85 vs 5,39 = **+1,46 p.p.** (era +0,34). O executor02 so
reportou a margem de acuracia; a de Macro F1 mais que quadruplica. A frase "o
DRI-SL supera ... o proprio melhor individuo encontrado pelo AG em todos os
tamanhos de 100 a 5.000" fica mais forte, nao mais fraca.

## Evidencias — 3 novas minhas, e 2 das 3 do executor02 precisam de ressalva

**(4) NOVA, e a que decide: as outras QUATRO linhas da MESMA tabela sao todas
`_old`, nas quatro celulas cada.** Conferi celula a celula contra os artefatos:

| linha | Acc max / F1 max / Acc min / F1 min | fonte |
|---|---|---|
| 500 | 56,00 / 18,01 / 36,17 / 6,52 | `_500old` — bate 4/4 |
| 1.000 | 62,20 / 24,69 / 49,33 / 12,60 | `_1000old` — bate 4/4 |
| 2.500 | 69,28 / 32,58 / 63,92 / 24,11 | `_2500old` — bate 4/4 |
| 5.000 | 74,13 / 40,07 / 70,82 / 31,87 | `_5000old` — bate 4/4 |
| **100** | 38,76 / 6,51 / 5,75 / 1,81 | **`_100oldold` — a unica intrusa** |

Isto e interno a tabela que se quer corrigir. Nao depende de convencao de nome.

**(5) NOVA: a propria prosa da tese ja carrega o numero `_old`.** Em
`4-resultados-l0:94-96`: "em $I=100$, a distancia entre pior e melhor individuo
da ultima geracao chega a $25{,}9$ pontos percentuais". Com `_100old`:
36,71 - 10,86 = **25,85 ~ 25,9**. Com a tabela como esta hoje: 38,76 - 5,75 =
**33,01**. A tese se contradiz em 7,2 p.p. sobre a mesma grandeza, e a correcao
resolve. A `tab:ag-evolucao` (l.85) ja usa 36,71/10,86.

**(6) NOVA, e grave: a rodada F1_MINIMIZE de `_100oldold` NUNCA TERMINOU.** O
`ag_detailed_fitnessF1_MINIMIZE.csv` para na **geracao 20 de 100** (969 linhas
contra 5.000 das outras tres). Por isso nao existe `ag_best_l0_F1_MINIMIZE.csv`
nessa pasta — o unico `ag_best` ausente do diretorio. Ou seja: **o 1,81% da
tese hoje nao tem arquivo `ag_best` de origem**; sai de uma rodada truncada em
1/5 do orcamento. As quatro rodadas de `_100old` chegam a geracao 100.

**(1) do executor02 — convencao `_old`: CONFIRMADA, e mais forte do que ele
disse.** O sufixo `_old` cobre 11 tamanhos de L0 (10, 50, 100, 250, 500, 1.000,
2.500, 5.000, 10.000, 20.000, 30.000); `_oldold` existe para apenas 3 (10, 50,
100). Nao e um par de rodadas: e uma varredura completa mais tres sobras.

**(2) do executor02 — cabecalho do CSV: MAIS FRACA do que enunciada.** Nao
separa `old` de `oldold`. O cabecalho `metric_value_on_eval_set` + BOM +
`experiment_params.json` aparece em {10oldold, 50oldold, 100oldold, **250old**}
— `250old` esta do lado "errado". Ainda poe `_100old` na maioria (10 de 14
diretorios), mas nao e um corte limpo. Registro tambem que em `_100oldold` o
cabecalho `metric_value_on_eval_set` CONTRADIZ o campo `metric_type` da propria
linha, que diz `accuracy_on_full`; em `_100old` (`metric_value` + `on_full`)
nao ha contradicao. Isto e argumento CONTRA `_100oldold`, nao a favor — e
corrige a leitura que eu mesmo tinha registrado no meu 0744, onde tratei o
`experiment_params.json` de `_100oldold` como metadado mais rico.

**(3) do executor02 — historico git: NAO CONSEGUI REPRODUZIR.** As duas pastas
entram no repositorio no MESMO commit (`26d7c4e "rename"`, 2025-06-01) e
nenhum outro commit toca qualquer uma das duas: `git log --all -- <as duas
pastas>` devolve exatamente uma linha. O historico nao ordena as geracoes. Se
o executor02 mediu outra coisa (o conteudo do proprio commit de rename, por
exemplo), vale ele dizer qual — as evidencias (4), (5) e (6) ja decidem sem ela.

## Escopo da correcao: contido, confirmado

`38,76`, `6,51`, `5,75` e `1,81` ocorrem **uma vez cada** em toda a tese, todas
em `4-resultados-l0/texto.tex`. Nada em `apresentacao/defesa.tex`, nada nos
artigos. A correcao e mesmo de uma linha de tabela — de quatro celulas.

## Nao verifiquei

Nao renderizei o LaTeX (nao tenho LaTeX neste conteiner) e nao toquei em
`activetextclassification`, que li em modo somente-leitura @b540533.

## Sobre o segundo achado da 1800 (tarefa 0120 nunca rodou)

Nao cruzei — nao me foi despachado e nao quero pisar em cima. Se a cruzada for
minha, peca; se for de outro, ignore este paragrafo.
