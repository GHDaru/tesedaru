---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar a entrega parcial da seed123; encaminhar a re-execução das estatísticas (McNemar/bootstrap) para o dono delas quando a s42 canônica fechar; e manter viva a pendência do cache do oráculo (A/B/C ×3 sementes)
referencia: activelearning@9d74484 (resultados s123) · activelearning@176f703 (legacy s42) · plano v17 (e3p-seed123, e3p-seed42-canonico)
criada_em: 2026-08-16T21:18:00Z
---
CONCLUSÃO PARCIAL da `e3p-seed123` + decisão do autor executada.

## Entregue: semente 123, regime canônico, 6 de 9 braços

Kernel `ghdaru/falco-e3prime-s123`, GPU T4, 75 min. Avaliação na população
inteira (177.490 itens). Commit `activelearning@9d74484` na main:

| braço | n_train | Macro F1 | acurácia | Wilson95 |
|---|---|---|---|---|
| D (régua) | 50.000 | 0,3590 | 0,8652 | [0,8636; 0,8668] |
| E35 | 35.000 | 0,3461 | 0,8582 | [0,8566; 0,8598] |
| E30 | 30.000 | 0,3228 | 0,8479 | [0,8463; 0,8496] |
| E25 | 25.000 | 0,3136 | 0,8305 | [0,8288; 0,8323] |
| E20 | 20.000 | 0,2416 | 0,7715 | [0,7695; 0,7734] |
| E | 15.000 | 0,1909 | 0,6895 | [0,6873; 0,6916] |

Varredura vs 0,95×D (F1 ≥ 0,3410; acc ≥ 0,8219): **E35 cruza os dois
critérios; E30 e E25 cruzam só acurácia; E20 e E ficam abaixo.**

A, B e C não rodaram: continuam presos ao `annotation_cache_nemotron.jsonl`
(mensagem de 19:30). Quando o cache virar dataset do Kaggle, uma reexecução
pula os 6 prontos e completa só esses três — vale para as TRÊS sementes.

## Decisão do autor, executada: s42 refeita em canônico

O autor decidiu (em sessão comigo, 2026-08-16): **refazer a semente 42 em
regime canônico**, em vez de refazer 7 e 123 em pareado — 1 sessão de GPU
contra 2, agora que as duas sementes novas já saíram canônicas. Consequências
já materializadas:

1. Os `e3prime_*_s42.json` antigos (bs=16, avaliação em 20.092) foram movidos
   por `git mv` para `results/legacy_s42_bs16_eval20k/`, com README —
   `activelearning@176f703`. Nada foi apagado.
2. `mcnemar_s42.json` e `bootstrap_f1_s42.json` ficaram onde estão (os links do
   plano continuam válidos), mas **referem-se ao regime antigo**: precisarão
   ser refeitos sobre as predições canônicas. O dono desses itens no plano é
   "agente" — encaminhe a quem for assumir.
3. Kernel `ghdaru/falco-e3prime-s42` **rodando agora** numa T4 (~1,3 h). Aviso
   quando fechar; aí as três sementes ficam comparáveis e o média ± desvio da
   banca sai dos 6 braços existentes.

A comparação entre regimes confirma que a decisão era necessária: E35 na
semente 123 canônica dá F1 0,3461 contra 0,4627 no s42 antigo — a população
inteira expõe classes raras que a amostra de 20k sub-representava. Números dos
dois regimes NÃO se misturam.

## Estado dos executores

Observei `ghdaru/falco-e3-semente-7` (executor01) com status COMPLETE no
Kaggle — a colheita e o commit são dele. Minha tarefa segue `.em-andamento`
até A/B/C saírem. Cota da conta hoje: ~2,7 h de GPU gastas nas duas sementes;
a s42 leva a ~4 h das 30 h semanais.
