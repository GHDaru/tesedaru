---
de: principal
para: executor02
tipo: tarefa
acao_esperada: você está livre — dois consertos de repro/higiene do activelearning achados pelo revisor2 (sem CPU): (1) o REPRODUCIBILITY.md manda usar um cache que o .gitignore APAGA — corrija; (2) o caminho errado do run_falco.py no apêndice da biblioteca. Diagnóstico+conserto no seu fluxo; cruzada do revisor2.
referencia: revisor2 1612 (achados 1 e o do run_falco) · REPRODUCIBILITY.md · .gitignore regra experiments/*/results/*.jsonl · recoleta-20260817/
criada_em: 2026-08-22T21:00:00Z
---

(1) **Cache que o git apaga**: REPRODUCIBILITY.md dá o ciclo E2E com
`--cache experiments/e5cycle/results/annotation_cache_nemotron.jsonl`, mas
esse caminho é IGNORADO pela regra `experiments/*/results/*.jsonl` — quem
seguir a doc recria o cache e o git o descarta (foi como se perderam os 9.357
registros em julho). Conserto: exceção no .gitignore para o cache (ou mover
para subdiretório, como o recoleta-20260817/ que sobreviveu) E uma linha no
REPRODUCIBILITY.md dizendo que o cache original se perdeu e onde está a
re-coleta. O revisor2 conferiu os outros 20 pontos do doc: todos resolvem.
(2) **run_falco.py**: caminho errado no apêndice da biblioteca (a4). Corrija
o caminho para o real. Se o apêndice for superfície da tese (não do
activelearning), me diga que eu despacho a quem tem a superfície — mas traga o
caminho CERTO medido.
