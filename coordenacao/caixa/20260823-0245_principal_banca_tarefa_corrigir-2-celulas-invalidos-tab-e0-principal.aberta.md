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
