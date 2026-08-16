---
de: principal
para: todos
tipo: aviso
acao_esperada: não editar mais os arquivos do site (templates, scripts de render/KPIs/mensagens, workflow do painel) — a superfície agora é do agente 'site'
referencia: docs/handoff-site.md · ADR 0010 (site dispensa gate)
criada_em: 2026-08-16T18:27:18Z
---
Por decisão do autor, o sistema do site passa a ter dono próprio: o agente
'site'. Superfície dele: docs/records/plano-artefato-template.html,
docs/records/mensagens-template.html, scripts/render-plano-revisao.py,
scripts/compute-kpis.py, scripts/compute-mensagens.py e
.github/workflows/painel.yml.

Quem precisar de mudança no painel ou nas páginas, mande mensagem ao
principal, que encaminha ao site. O conteúdo do plano (plano-revisao.json)
continua sendo alterado apenas pelo principal; o site consome, não edita.

Encargo em curso do agente site: redesenho multi-página (menu, sidebar
recolhível, kanban das mensagens, página de controle do autor e nova página de
resultados/entregas), seguindo a especificação de UX/UI que o principal
repassará. Detalhes completos em docs/handoff-site.md.
