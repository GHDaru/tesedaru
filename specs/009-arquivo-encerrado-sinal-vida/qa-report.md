# QA Report 009 — arquivo no kanban, capítulo encerrado, sinal de vida

- **Lane**: light — tarefa direta do `principal`, sem spec/plan/tasks
  separados; `ux-design.md` cobre as três decisões (inclusive o diagnóstico
  que descartou o pedido literal do item 3).

## Verificação (Playwright/Chromium, dados reais — 281 mensagens, 336
referências, plano v61)

- **Item 1 (arquivo)**: já resolvido antes deste ciclo — nenhuma mudança de
  código. Confirmado com dados reais pós-limpeza: `Arquivadas (252)` no
  `<details>` recolhido de Coordenação, 29 mensagens ativas nas colunas do
  quadro. `compute-mensagens.py` já varria `coordenacao/arquivo/*/` desde o
  commit `ec2bf01`.
- **Item 2 (capítulo encerrado)**: 2 linhas (`1 · Introdução`,
  `2 · Fundamentação`) na matriz "Capítulos × rodadas" mostram o selo
  `✓ encerrado` + fundo destacado (`--st-feito-bg`); `title` do selo carrega
  a justificativa completa do campo `capitulos[].encerrado` do plano
  (conferido: texto bate com o JSON fonte). Capítulos 3-6, apêndices e
  pré-textuais seguem sem selo/sem destaque (nenhum tem `encerrado` no
  plano) — sem falso positivo.
- **Item 3 (sinal de vida)**: 4 chips renderizados (`principal`, `banca`,
  `revisor1`, `revisor2`), cada um com `k-ag-dot` na cor certa do agente.
  Dado real: `banca` ativo há 6 min (postou mensagem recentemente), os
  outros 3 "há 3 dias" e marcados `vida-inativo` (opacidade reduzida) —
  bate com `atividade` em `mensagens.json` (`ativos=1/4`). `title` de cada
  chip explica a metodologia (mensagem OU lock, janela de 120 min) por
  extenso.
- **0 erros de console reais** nas 7 páginas (Controle, Plano, Coordenação,
  Resultados, Referências, Grafo, Bibliometria) — o único console error
  capturado é o 404 de `/favicon.ico`, já investigado e é do servidor local
  de teste, não da aplicação (confirmado no log do `http.server`).
- **Claro/escuro**: sinal de vida e selo de capítulo conferidos nos dois
  temas — sem regressão de contraste ou de token de cor (reuso de
  `--st-feito-bg`/`.k-ag-dot`, nenhuma cor nova).
- **Mobile (390×844)**: `scrollWidth <= clientWidth` em Plano e Coordenação
  — sem rolagem horizontal.
- **Regressão**: as 4 páginas não tocadas por este ciclo (Controle,
  Resultados, Referências, Grafo, Bibliometria) seguem com 0 erros de
  console — mudança ficou contida em `build_plano()`/`build_coordenacao()`
  de `render-plano-revisao.py` e em `compute-mensagens.py`.

## Desvio do pedido original (item 3) — registrado para o principal

O pedido era "derivar do git (último commit por autor)". Verificação
(`git log --format='%an' -300 | sort | uniq -c`): 295/300 commits recentes
têm autor git `Claude`, só 4 têm `revisor2` — o autor do commit não
distingue agente nenhum na prática (quase todos os agentes commitam pela
mesma identidade de ferramenta, não pelo papel que estão assumindo).
Implementado com o sinal real disponível: timestamp da mensagem postada em
`coordenacao/` (campo `de`) combinado com a renovação de lock (`dono` +
`renovado_ha_min`), ambos já commitados a cada ação do protocolo e já
presentes no `mensagens.json`. Mesmo espírito do pedido (git como fonte,
janela de 2h), sem o método que não funcionaria.

## Closing tail

- `TAIL:review` — n/a: lane light, mudança aditiva e pequena (3 ajustes
  independentes, cada um com fallback gracioso quando o dado não existe).
- `TAIL:security` — nenhuma superfície nova de rede; todo texto injetado
  (justificativa do `encerrado`, agente, timestamps) passa por `esc()`
  como qualquer outro campo do site. n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
