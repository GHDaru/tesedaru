# QA Report 011 — Agentes: cards + histórico recolhido

- **Lane**: light — feedback direto do autor sobre a página do ciclo 010,
  com consulta a 3 especialistas antes de decidir (ver `ux-design.md`).

## Verificação (Playwright/Chromium, dados reais — 287 mensagens, plano v61)

- **0 erros de console reais** nas 8 páginas do site (Controle, Plano,
  Coordenação, Resultados, Referências, Grafo, Bibliometria, Agentes) — o
  único erro capturado é o 404 de `/favicon.ico`, já investigado em ciclos
  anteriores.
- **KPI "agora"**: `16` tarefas abertas, `5 de 10 nós com pendência` —
  bate com a soma manual sobre `mensagens.json` (`principal 5, executor02
  5, executor01 4, revisor2 1, todos 1`).
- **Faixa do hub**: `principal` mostra `enviou 97 · recebeu 163` — conferido
  somando manualmente todas as arestas `principal>*` (97) e `*>principal`
  (163) no JSON real.
- **Cards**: 3 agentes com pendência (`executor02` 5, `executor01` 4,
  `revisor2` 1) + card de difusão (`todos` 1), ordenados por volume desc —
  bate com os dados. `revisor2` mostra sinal de vida ("sem sinal recente há
  3 dias", dado do ciclo 009); os demais cards não mostram essa linha
  porque `atividade` só existe para os 4 agentes de coordenação — conferido
  que não há fabricação de dado ausente.
- **Linha de zerados**: "Sem pendências agora: revisor1, banca, site,
  local, autor" — os 5 agentes restantes, nenhum card vazio renderizado.
- **Difusão**: "42 no histórico, 1 tarefa ainda aberta" — 42 confirmado
  somando todas as arestas `*>todos`.
- **Histórico (dentro do `<details>`, fechado por padrão — conferido
  `details.open === false` no carregamento)**: 6 linhas retas
  `agente ⇄ principal`, sem seta, com `[in N] [out M]` — os 6 rótulos
  batem exatamente com os 6 pares reais (`revisor1 [in 27][out 61]`,
  `revisor2 [in 20][out 44]`, `banca [in 7][out 36]`, `site [in 9][out
  11]`, `executor02 [in 10][out 5]`, `executor01 [in 6][out 6]`),
  ordenados por volume do par desc. Nota de exceções lista as 3 trocas
  peer-to-peer fora do hub; nota separada lista `local` e `autor` (sem
  troca direta com o principal). A tabela "Dados exatos" (23 arcos, já
  existente) segue abaixo, inalterada.
- **Claro/escuro**: conferido nos dois — cores de agente, faixa do hub,
  cards, leque do histórico e tabelas sem regressão de contraste.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` antes E depois de
  abrir o `<details>` do histórico (o SVG do leque encolhe
  proporcionalmente, sem forçar rolagem horizontal).
- **Regressão**: as 7 páginas não tocadas por este ciclo seguem com 0 erros
  de console — mudança ficou contida em `build_agentes()`.

## Closing tail

- `TAIL:review` — n/a: lane light, mas com um passo de verificação
  equivalente a revisão — 3 pareceres técnicos independentes revisaram a
  decisão de design antes da implementação (registrado em `ux-design.md`
  §1-2), o que substitui a revisão de código pós-implementação para uma
  mudança puramente de apresentação (sem lógica de negócio nova).
- `TAIL:security` — nenhuma superfície nova de rede; todo texto injetado
  segue passando por `esc()`. n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
