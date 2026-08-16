# Tasks 002 — Board kanban da Coordenação: caber na tela

## Verification first

- [x] **T0** — DoD executável definido em `spec.md` (AC1–AC5, Playwright)
  antes de qualquer mudança de CSS/JS.

## Implementation

- [ ] **T1** — `.k-cards`: `max-height:clamp(320px,58vh,640px)` +
  `overflow-y:auto` + `overscroll-behavior:contain`; `.k-col-h` fora do
  container que rola. (FR1)
- [ ] **T2** — Remover `CAP_ENABLED`/`CAP`/lógica de `mostrar`/`resto` e o
  botão "+N mais" (mecanismo de corte quebrado — media o total do board,
  não por coluna). (FR3)
- [ ] **T3** — Função de ordenação por prioridade dentro de cada coluna:
  `(atrasado && paraVoce) → paraVoce → atrasado → recência`. (FR2)
- [ ] **T4** — `.k-titulo` com `-webkit-line-clamp:2` + `title` com texto
  completo; `.k-card` com `line-height:1.3` e padding/gap reduzidos dentro
  da escala `--sp-*` existente. (FR4)
- [ ] **T5** — "Atrasado": glifo `⚠` + negrito, mantido inline no rodapé
  (sem virar destaque forte novo). (FR5)
- [ ] **T6** — Breakpoint intermediário 601–1099px (`.k-board` flex +
  `overflow-x:auto`, `.k-col{min-width:260px}`); ajustar breakpoint mobile
  de 900px para 600px. (FR6)
- [ ] **T7** — Acessibilidade: `role="region"` + `aria-labelledby` por
  coluna; `tabindex="0"` + `aria-label` no container de rolagem; região
  `aria-live="polite"` para a contagem após filtro. (FR7)
- [ ] **T8** — Estado vazio diferenciado: "Nada aqui" (vazio real) vs.
  "Nada aqui com os filtros atuais" (vazio só por filtro). (FR8)

## Verification (DoD)

- [ ] **T9** — Rodar as 4 páginas no Chromium (Playwright): 0 erros de
  console; medir altura de `.k-cards` com 72 mensagens sintéticas (AC1);
  testar rolagem interna vs. altura da página (AC2); verificar ordem do
  DOM por prioridade (AC3); tema claro/escuro + breakpoints 600px/900-
  1099px/1100px (AC4); atributos ARIA presentes + navegação por Tab (AC5).
- [ ] **T10** — Screenshots antes/depois (coluna com 38 cartões sintéticos)
  anexados ao `qa-report.md`.

## Living documentation (same cycle)

- [ ] **T11** — `spec.md`/`plan.md`/`ux-design.md`/`tasks.md` já
  commitados junto com a implementação (não depois) — mesmo commit.

## Closing tail — MANDATORY, one line each, never delete

- [ ] `TAIL:review` — revisão independente em contexto fresco do diff
  (agente `review`, não o executor) — evidência no qa-report.
- [ ] `TAIL:security` — n/a: mudança é só CSS/JS de apresentação num script
  gerador estático — sem entrada de usuário, sem rede nova, sem segredo
  tocado; varredura rápida de diff ainda roda por hábito, evidência no
  qa-report.
- [x] `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR
  0010) — publicação direta na main após DoD + review independente.
