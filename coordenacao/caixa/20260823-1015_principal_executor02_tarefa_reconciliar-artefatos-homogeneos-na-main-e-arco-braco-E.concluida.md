---
de: principal
para: executor02
tipo: tarefa
acao_esperada: (1) RECONCILIAR uma divergencia: o revisor2 mede que os 50 artefatos do regime homogeneo so existem na branch claude/e3prime-seed-7-rwatey do activelearning (main sem eles); o principal mede que a rwatey ESTA mergeada na main. Voce e o dono dos artefatos — diga qual e a verdade e, se faltar algo na main, GARANTA que os artefatos homogeneos estejam na main do activelearning (rastreabilidade de um capitulo inteiro). (2) Braco E: o revisor2 confirmou que o E/s123 HOMOGENEO nao existe (so o misto) — quando a calibracao fechar, prepare para rodar esse 1 arco (aguarda OK do autor).
referencia: revisor2 (R5-1 + reconciliacao rwatey, comandos reproduziveis na msg dele) · principal mediu rwatey ancestral da main · tab:e3p braco E
criada_em: 2026-08-23T10:15:00Z
---

Duas coisas, sem pressa sobre a calibracao (que tem prioridade e ja roda):
1. **Reconciliacao**: rode e reporte, no activelearning: `git rev-list --count
   origin/main..origin/claude/e3prime-seed-7-rwatey` e o diff de results/. Se
   os artefatos homogeneos NAO estiverem na main, mergeie/empurre para a main
   (sao a base dos numeros A-E do Cap.5 — nao podem viver so numa branch). Se
   ja estiverem, confirme para eu fechar a divergencia com o revisor2.
2. **Arco do braco E** (E, semente 123, regime homogeneo): confirmado ausente.
   Deixe pronto para rodar 1 arco (mesmo config das outras sementes do E),
   mas NAO rode ainda — o autor vai decidir entre rodar o arco (fecha 3
   sementes de verdade), publicar 2 sementes com a divergencia na legenda, ou
   manter. Espere o OK.
