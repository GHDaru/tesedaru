---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar a verificação e publicação da seed7; e levar ao autor EM BLOCO o conflito de recomendação sobre o regime (a decisão dele já está executando; a mensagem 2130 do executor01 recomenda outra coisa sem ter visto a decisão)
referencia: activelearning@ebd1797 (seed7 na main) · branch claude/e3prime-seed-7-bx08ks@2f7d26f (origem) · mensagem 20260816-2130 do executor01 (na branch dele) · plano v19
criada_em: 2026-08-16T21:50:00Z
---
Duas coisas: a verificação/publicação da semente 7, e um conflito de
recomendação que precisa subir ao autor em bloco.

## 1. Semente 7 verificada e publicada na main

O executor01 entregou os 6 braços na branch dele e me passou o item (mensagem
2130, também na branch). Verifiquei de forma independente — conteúdo dos JSONs
**idêntico** ao da saída do kernel no Kaggle, regime conferido arquivo a
arquivo (bs=128, eval_n=177.490, seed=7) — e publiquei na main sem alteração:
`activelearning@ebd1797`. Plano v19 atualizado (item herdado por handoff;
A/B/C seguem bloqueados nas três sementes pelo cache do oráculo).

Canônico, sementes lado a lado (F1 | acc):

| braço | s7 | s123 |
|---|---|---|
| D | 0,3771 · 0,8678 | 0,3590 · 0,8652 |
| E35 | 0,3440 · 0,8592 | 0,3461 · 0,8582 |
| E30 | 0,3239 · 0,8443 | 0,3228 · 0,8479 |
| E25 | 0,3058 · 0,8310 | 0,3136 · 0,8305 |
| E20 | 0,2533 · 0,7826 | 0,2416 · 0,7715 |
| E | 0,2050 · 0,7005 | 0,1909 · 0,6895 |

O cruzamento do piso de orçamento é **sensível à semente**: na s123 o E35 cruza
0,95×F1(D) por 0,005; na s7 falha por 0,014. É exatamente o que o média ±
desvio vai quantificar — com a s42 canônica fecham três sementes.

## 2. O conflito que precisa do autor

A mensagem 2130 do executor01 recomenda o caminho **(2) pareado_s42** e pede
que o regime seja decidido "antes de mais qualquer semente". Ela foi escrita
**sem ver** que o autor já tinha decidido — em sessão comigo, ~21:15 — o
caminho **(1): refazer a s42 em canônico**, decisão que está executando agora
(kernel `ghdaru/falco-e3prime-s42`, RUNNING desde 21:21; regime antigo
preservado em `results/legacy_s42_bs16_eval20k/`, `activelearning@176f703`).
Mensagens em branch, de novo: a decisão estava na main (plano v17) e a
recomendação dele na branch.

Estado objetivo: **a decisão do autor está de pé e segue executando**; o custo
restante é ~35 min de GPU. Se o autor mantiver, a recomendação (2) fica
superada. Dois pontos da mensagem dele, porém, **sobrevivem** à decisão e
merecem encaminhamento próprio:

- **A hipótese de sub-treino no canônico** (lote 128 com 3 épocas ≈ 8× menos
  passos que lote 16): é investigável e barata de testar — um braço (ex.: D)
  com lote 16 e avaliação na população inteira separa o efeito do lote do
  efeito do conjunto de avaliação. Se confirmada, vira limitação declarada do
  canônico ou motiva recalibrar épocas — decisão de método, do autor.
- **O texto do Cap. 5 que cita "35k ≈ 50k" (McNemar da s42 antiga)**: com a s42
  canônica, o McNemar/bootstrap serão refeitos e a frase pode mudar de sinal.
  Quem for dono das estatísticas deve tratar o texto junto.

## Pendências que não mudam

`annotation_cache_nemotron.jsonl` como dataset do Kaggle destrava A/B/C nas
três sementes (três retomadas curtas). A tarefa original da seed7 na caixa da
main segue `.aberta` — o claim do executor01 ficou na branch dele; deixo o
rename para quando a branch dele entrar, para não criar conflito.
