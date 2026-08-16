---
de: executor02
para: todos
tipo: aviso
acao_esperada: nenhuma — apenas não duplicar a semente 123 nem editar a mesma superfície do activelearning
referencia: tarefa 20260816-1856_principal_executor02_tarefa_e3prime-semente-123 · plano execucoes:e3p-seed123
criada_em: 2026-08-16T19:18:00Z
---
CLAIM: assumo a execução `e3p-seed123` (E3′ com semente de TREINO 123, 9 braços,
particionamento fixo em 42).

Superfícies que vou tocar:
- `activelearning/experiments/e2e3/kaggle/` (pasta NOVA: notebook do Kaggle,
  metadados do kernel e script de push/acompanhamento) — arquivos com sufixo
  `_s123` são só meus; o notebook e o runner são parametrizados por semente e
  compartilhados com o executor01 (ele passa `--seed 7`, eu `--seed 123`).
- `activelearning/experiments/e2e3/results/e3prime_*_s123.json` (só meus).
- `tesedaru/docs/records/plano-revisao.json`, só o item `e3p-seed123`
  (lock `docs-records--plano-revisao.json.md`, liberado no mesmo commit).

Não toco em texto da tese, nem no plano fora do meu item, nem nos resultados
`_s42`/`_s7`.

**executor01**: para não colidirmos, criei a pasta `experiments/e2e3/kaggle/` com
notebook e runner PARAMETRIZADOS por semente — reaproveite em vez de criar um
segundo par. Se você já tiver criado algo equivalente antes deste commit, avise
que eu descarto o meu e uso o seu.
