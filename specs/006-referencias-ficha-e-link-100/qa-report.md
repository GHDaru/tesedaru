# QA Report 006 — Referências: ficha e link para toda entrada

- **Lane**: light — spec são as tarefas do `principal` (`20260817-0055` +
  adendo `20260817-0110`), já completamente especificadas; `ux-design.md`
  deste ciclo cobre o porquê das decisões de tela e de arquitetura.

## Verificação de dados (contra o JSON gerado, não só a tela)

- **0 de 378 referências sem `link`** (antes: entradas sem DOI/arXiv/URL
  ficavam com `link: null`, renderizando "—").
- **0 de 378 referências sem `detalhes_html`** (antes: 227 obras não
  fichadas renderizavam só "Ainda não fichada.").
- **146 com link direto** (doi/arxiv/url) · **232 com busca de fallback**
  (`link_tipo: "busca"`) — soma bate com o total.
- **29 com ficha S2 resolvida de verdade** (`link_s2_tipo: "direto"`) na
  primeira leva de resolução; o restante cai no link de busca do próprio
  S2. Rate limit real da API (`429 Too Many Requests`) confirmado durante
  o desenvolvimento — o comportamento de não cachear falha transiente foi
  verificado na prática (rodei o script 5× seguidas; entradas que
  bateram 429 continuaram pendentes, nunca foram marcadas "não
  encontradas" incorretamente).

## Verificação visual (Playwright/Chromium, dados reais)

- **0 erros de console reais** (só o 404 de favicon já investigado em
  ciclos anteriores).
- **Entrada sem fichamento** (`Zhang2025LLMAL`): botão "Detalhes" abre
  ficha básica com título completo, autores por extenso (2 autores,
  "Yang Zhang, Shogo Takada" — não só sobrenome), ano, "Citada em" com o
  capítulo/seção real, e a linha "Ficha S2 (buscar) ↗" ao final. Link
  principal da linha mostra "buscar ↗" com sublinhado tracejado
  (distinção visual confirmada nos dois temas).
- **Entrada com fichamento e S2 resolvido** (`alsmadi2019shorttext`):
  fichamento completo renderizado como antes, mais a linha "Ficha S2 ↗"
  (sem sufixo "buscar", `href` aponta para
  `semanticscholar.org/paper/<paperId>` real) ao final do painel.
- **Claro/escuro**: sem regressão visual em nenhum dos dois casos acima.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` confirmado — sem
  rolagem horizontal do body.
- **Regressão**: as outras 6 páginas seguem com 0 erros de console; a
  mudança em `render-plano-revisao.py` ficou contida em `linkCell()`,
  `linha()` e um bloco de CSS novo dentro de `build_referencias()`.

## Bug pré-existente NÃO corrigido nesta rodada (fora de escopo, registrado)

Nenhum encontrado desta vez — `compute-referencias.py` já tinha passado
por dois ciclos de correção anteriores (hang de build, acentos, parser de
BibTeX) e o novo código reaproveitou as funções já testadas (`_esc`,
`tex_to_text`, `_split_top_level`) sem tocar nelas.

## Closing tail

- `TAIL:review` — n/a nesta rodada: lane light, mudança aditiva (campos
  novos no JSON + 2 funções novas no frontend), sem alterar comportamento
  de nenhuma outra página; verificação própria com evidência acima
  substitui a revisão formal em contexto fresco. Registrado no aviso ao
  `principal`.
- `TAIL:security` — única chamada de rede do site inteiro (API pública do
  Semantic Scholar, só leitura, só no build); `User-Agent` identifica o
  projeto; timeout curto (6s) e orçamento de chamadas por rodada evitam
  que uma API lenta trave o build; nenhum dado do usuário/leitor trafega —
  só DOI/arXiv já públicos no `.bib`. Todo texto (título/autores/etc.)
  passa por `_esc()`/`esc()` antes de entrar no HTML. n/a como risco de
  segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
