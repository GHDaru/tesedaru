# QA Report 013 — Resultados: cards de experimento, pilares vazios, sumário

- **Lane**: light — pedido direto do autor, com consulta a 3 especialistas
  antes de decidir (ver `ux-design.md` §1-2).

## Verificação (Playwright/Chromium, dados reais)

- **0 erros de console reais** nas 8 páginas do site — o único erro
  capturado é o 404 de `/favicon.ico`, já investigado em ciclos anteriores.
- **Zero rolagem horizontal na seção de experimentos**: `scrollWidth <=
  clientWidth` no `documentElement` em 1280px (desktop) E em 390px
  (mobile) — o problema que motivou a consulta aos especialistas
  desapareceu por completo, não foi só mitigado.
- **7 cards renderizados** (`document.querySelectorAll('.experimento-card')
  .length === 7`), cada um com o selo do notebook sempre visível:
  - E0, E0-P, E1, E4, E5 → `pill pendente`, texto "— sem notebook" (visível
    sem hover, sem depender de `title`).
  - E6 → `pill feito`, "✓ notebook ↗", `href` =
    `https://www.kaggle.com/code/ghdaru/falco-auditoria-escala-populacional`,
    `aria-label="abrir notebook Kaggle do experimento E6"`.
  - E3′ → `pill feito`, "✓ notebook ↗", `href` =
    `https://www.kaggle.com/code/ghdaru/falco-auditoria-classificador-forte`,
    `aria-label="abrir notebook Kaggle do experimento E3′"` — conferido que
    o `aria-label` carrega o ID certo mesmo com o apóstrofo curvo (′) do
    id.
- **Pilares vazios**: 2 de 4 (`document.querySelectorAll('.pilar-vazio')
  .length === 2`) — P1 e P2, os únicos sem achado registrado no JSON.
- **Sumário de âncoras**: texto conferido —
  `Achados (2 de 4 pilares) · Entregas (8) · Experimentos (7)`, batendo com
  a contagem real do JSON. Clique em `#sec-experimentos` rola a seção para
  perto do topo da viewport (`getBoundingClientRect().top` entre 0 e 200px
  após o clique) — o `scroll-margin-top` funciona.
- **Claro/escuro**: página inteira conferida nos dois temas — cards,
  selos (`pill feito`/`pill pendente`), pilares tracejados e sumário sem
  regressão de contraste.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` — sem rolagem
  horizontal em lugar nenhum da página.
- **Regressão**: as 7 páginas não tocadas por este ciclo seguem com 0 erros
  de console — mudança ficou contida em `build_resultados()`.
- **Tamanho da página**: caiu de ~3537px para ~2643px de altura total
  (mesmos dados, mesma viewport 1280×900) — efeito colateral positivo de
  colapsar os pilares vazios e de cards mais compactos que a tabela
  anterior (que tinha células de 10+ linhas de texto espremidas em colunas
  estreitas).

## Closing tail

- `TAIL:review` — n/a: lane light, mas com um passo equivalente a revisão —
  3 pareceres técnicos independentes (ciclo 013) avaliaram a decisão de
  design antes da implementação, registrado em `ux-design.md` §1-2, que
  substitui a revisão de código pós-implementação para uma mudança
  puramente de apresentação.
- `TAIL:security` — nenhuma superfície nova de rede; todo texto injetado
  segue passando por `esc()`. Link do notebook mantém
  `target="_blank" rel="noopener"` (mesmo padrão do site inteiro). n/a
  como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
