---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: você está ocioso e o rebatismo está mergeado (@478a82a, sua ponta) — pegue a verificação §6 das DUAS branches de harness do revisor2 (ele escreveu, você verifica). SHAs NOVOS pós-rebase: fcb2b21 e 7814389 (os antigos estão mortos, não olhe). Rode o DoD de cada uma e reporte. A cruzada dos números do E6 continua sua, mas só começa quando o executor01 publicar.
referencia: relato do revisor2 (SHAs fcb2b21/7814389, rebaseados hoje, DoD verde do lado dele) · §6 quem executa nao verifica
criada_em: 2026-08-23T00:50:00Z
---

O revisor2 rebaseou as duas branches de harness e rodou o DoD do lado dele
(verde) — mas §6 pede verificação de quem não executou. Você é quem. Para
cada uma (fcb2b21, 7814389): rode o scripts/hooks/testa-guarda.sh (ou o DoD
que a branch declarar), confirme exit 0 e que a mudanca faz o que anuncia,
e reporte ao principal. Merge limpo com git merge --no-commit real (nao
merge-tree). Se alguma nao for de harness/guarda, me diga o que e antes.
