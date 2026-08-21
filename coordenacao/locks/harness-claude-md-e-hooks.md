---
dono: revisor2
superficie: CLAUDE.md, AGENTS.md (gerado), .claude/settings.json, scripts/hooks/
motivo: "ordem direta do autor (2026-08-21): implementar @-imports no CLAUDE.md + hooks PreToolUse e SessionStart"
criada_em: 2026-08-21T03:45:00Z
renovado_em: 2026-08-21T03:45:00Z
ttl_min: 45
---
Trabalho em branch própria (`harness/claude-md-imports-e-hooks`); a main recebe
só o lock e o aviso de entrega. NÃO toco em conteúdo de capítulo, em fichamento
nem em `docs/records/`. O `AGENTS.md` é regenerado por `scripts/sync-agents-md.sh`,
não editado à mão.

ATENÇÃO a quem for mexer em harness em paralelo: um hook `PreToolUse` mal
formado bloqueia TODOS os agentes. Testei os meus antes de entregar e eles
falham em aberto (qualquer erro interno = permitir); só as três proibições
duras retornam bloqueio.
