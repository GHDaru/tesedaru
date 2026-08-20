# QA Report 008 — Kanban: desmarcar todos + parte da tarefa

- **Lane**: light — pedido direto do autor, sem spec/plan/tasks
  separados; `ux-design.md` cobre as duas decisões.

## Verificação (Playwright/Chromium, dados reais)

- **0 erros de console reais** (só o 404 de favicon, já investigado em
  ciclos anteriores).
- **Nenhum/Todos**: clique em "nenhum" (grupo Agente) zera as 5 pílulas
  (`afterNenhum: 0`); clicar em uma pílula depois liga só ela
  (`oneOn: 1`); clique em "todos" restaura as 5 (`afterTodos: 5`).
  Board atualiza em tempo real a cada clique (`board-status` reflete a
  contagem filtrada).
- **Parte detectada**: 33 badges renderizados na tela, batendo com a
  contagem calculada em `compute-mensagens.py` contra os 121 registros
  reais (33/121 ≈ 27%). Amostra conferida: primeiro badge = "Cap. 2",
  batendo com a mensagem real (referência cita `2-fundam/texto.tex`).
- **Claro/escuro**: sem regressão visual nos dois temas.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` — sem rolagem
  horizontal do body.
- **Regressão**: as outras 6 páginas não tocadas por este ciclo (mudança
  ficou contida em `renderFiltros()`/`card()` de `build_coordenacao()` e
  em `compute-mensagens.py`).

## Closing tail

- `TAIL:review` — n/a: lane light, mudança aditiva e pequena (dois
  botões de ação + um campo calculado, opcional em cada cartão).
- `TAIL:security` — nenhuma superfície nova de rede; `parte_detectada`
  passa por `esc()` como qualquer outro texto antes de entrar no HTML.
  n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
