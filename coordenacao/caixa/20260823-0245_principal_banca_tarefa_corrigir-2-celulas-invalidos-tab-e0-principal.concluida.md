---
de: principal
para: banca
tipo: tarefa
acao_esperada: corrigir 2 células da coluna "Inválidos" da tab:e0-principal (Cap.5) que nao batem com o artefato (achado do revisor2 0807). Valores exatos abaixo. Conferir que a prosa da RQ3 (l.127) continua coerente apos a correcao. Branch (pode ser junto do lote-2100 ou nova), cruzada do revisor2, gate do autor.
referencia: revisor2 0807 · artefato e0_table.json (invalid_label_rate) · 5-resultados-falco tab:e0-principal · RQ3 l.127
criada_em: 2026-08-23T02:45:00Z
---

Duas celulas erradas (as outras 10 da coluna batem — nao e arredondamento):
- **glm-5.2, S-rand**: 0,0\% -> **0,7\%** (invalid_label_rate = 0,0070)
- **deepseek-v4-pro, S-strat**: 0,0\% -> **0,2\%** (invalid_label_rate = 0,0021)

Cuidado de coerencia: a RQ3 (l.127) diz sobre o v4-pro na S-strat que
"~2% envolvem raro ou rotulo invalido". Com a celula agora em 0,2% de
invalido, confira que o ~2% (raro + invalido) continua de pe — provavelmente
sim (o grosso e "raro"), mas confirme contra o ANALISE_ERROS.md para a tabela
e a prosa nao se contradizerem. Nenhum outro numero muda. Use exatamente
0,7% e 0,2%; cruzada do revisor2 (achado dele).

## Resultado (banca, 2026-08-23)

Entregue em `banca/celulas-invalidos-e-metade` @11770fc (1 arquivo, junto com
o adendo 0300). Celulas: glm-5.2 S-rand 0,0%->0,7% e v4-pro S-strat
0,0%->0,2%, exatamente os valores do artefato. Coerencia da RQ3 conferida: o
"~2%" e a soma _rare_ ~1% + invalido ~1% dos 324 erros (0,0021 x 1.863 = 3,91
-> os 4 casos do ANALISE_ERROS.md); tabela e prosa agora concordam. Adendo
0300 no mesmo commit: "metade ou um quarto" -> "cerca de metade do que a
selecao aleatoria exige nos dois classificadores" (tab:e6: SGD 2,06x, PVBin
2,11x). Proximo passo: cruzada do revisor2 (achados dele) e gate via principal.
