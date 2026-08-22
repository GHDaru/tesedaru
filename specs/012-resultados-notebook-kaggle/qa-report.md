# QA Report 012 — Resultados: notebook Kaggle por experimento

- **Lane**: light — pedido direto do autor, sem spec/plan/tasks separados;
  `ux-design.md` cobre a investigação de proveniência (por que só 2 dos 7
  experimentos têm link) e a decisão de não adivinhar os demais.

## Verificação (Playwright/Chromium, dados reais)

- **0 erros de console reais** nas 8 páginas do site — o único erro
  capturado é o 404 de `/favicon.ico`, já investigado em ciclos anteriores.
- **Coluna "Notebook Kaggle"**: 7 linhas conferidas via DOM
  (`document.querySelectorAll('#experimentos tbody tr')`) — E0, E0-P, E1,
  E4, E5 mostram `—`; E6 mostra
  `https://www.kaggle.com/code/ghdaru/falco-auditoria-escala-populacional`;
  E3′ mostra
  `https://www.kaggle.com/code/ghdaru/falco-auditoria-classificador-forte`.
  Os dois links batem, byte a byte, com os slugs citados em
  `docs/records/rastreabilidade.json` (branch
  `origin/claude/e3prime-seed-7-bx08ks`, não mergeada) e na mensagem
  `20260817-0330_executor01_..._tres-sementes-canonicas-contrariam-o-cap5`.
- **Mapeamento experimento↔notebook conferido por conteúdo, não só por
  nome**: os números que o notebook `escala-populacional` audita
  ("saturação SGD/PVBin", "viés de autoavaliação") são os mesmos números do
  achado E6 já registrado em `resultados.json`; os que `classificador-forte`
  audita ("Tabela e3p A/B/C/E/D", "McNemar") são os mesmos do E3′.
- **Verificação de rede descartada como sinal**: `curl` contra
  `kaggle.com` (inclusive contra um slug já confirmado por prosa,
  `falco-e3-semente-7`) devolve 404 genérico do proxy deste ambiente para
  qualquer caminho — não serve para confirmar nem para descartar um slug
  adivinhado, então nenhum dos outros 5 experimentos recebeu link por essa
  via.
- **Claro/escuro**: coluna nova conferida nos dois temas, sem regressão de
  contraste (reuso do padrão de link externo já usado em Referências/
  Entregas).
- **Mobile (390×844)**: `scrollWidth <= clientWidth` no body — a tabela mais
  larga rola dentro do próprio `<div class="scroll">`, sem vazar para a
  página (mesmo padrão já usado nas outras tabelas largas do site).
- **Regressão**: as 7 páginas não tocadas por este ciclo seguem com 0 erros
  de console — mudança ficou contida em `build_resultados()` e no JSON de
  dados.

## Closing tail

- `TAIL:review` — n/a: lane light, mudança aditiva (1 coluna, 1 campo por
  item). O passo que substitui revisão de código aqui foi a investigação de
  proveniência de cada link antes de publicar (registrada em
  `ux-design.md`), já que o risco real deste ciclo era inventar uma URL, não
  quebrar a UI.
- `TAIL:security` — link externo com `target="_blank" rel="noopener"`
  (mesmo padrão já usado no site inteiro); nenhuma superfície nova de rede
  no cliente. n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
