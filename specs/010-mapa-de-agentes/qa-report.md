# QA Report 010 — Mapa de Agentes (nova página)

- **Lane**: light — pedido direto do autor, sem spec/plan/tasks separados;
  `ux-design.md` cobre as 6 decisões (quem entra como nó, layout hub,
  semântica do número no nó, semântica das arestas, fonte de dados, cores
  novas).

## Verificação (Playwright/Chromium, dados reais — 282 mensagens)

- **Nós**: 10 renderizados (`principal` + 9 do anel) — bate com o desenho
  (8 pedidos pelo autor + `autor` + `todos`, ambos justificados no
  ux-design.md). Número dentro de cada nó conferido contra o cálculo Python
  independente: `principal` 4, `executor01` 4, `executor02` 4, os outros 6
  em 0 — bate exatamente.
- **Arestas**: 23 arcos renderizados, mesma contagem do agregado Python
  (`Counter((de,para))` sobre as 282 mensagens). Amostra conferida:
  `revisor1→principal` 61 (a mais grossa do desenho, visualmente a mais
  grossa de fato).
- **Achado de bug ANTES de publicar**: a primeira versão da seta
  (`marker`) usava o `markerUnits` padrão (`strokeWidth`), que escala o
  tamanho da seta junto com a espessura da linha — nas arestas mais
  grossas (até 9px) a seta virava um triângulo gigante que engolia os nós
  vizinhos. Corrigido com `markerUnits="userSpaceOnUse"` (tamanho fixo,
  independente da espessura). Achado por inspeção visual do screenshot, não
  por teste automatizado — o Playwright não pega "feio", só erro/dado
  errado.
- **Achado de bug ANTES de publicar (2)**: rótulo do nome do agente sempre
  posicionado "abaixo" do nó — para os nós da metade de cima do anel
  (`revisor1`, `revisor2`, `site`, `banca`), "abaixo" aponta para o centro,
  onde as arestas convergem, e o texto ficava atrás das linhas. Corrigido
  posicionando o rótulo na direção radial de cada nó (para fora do anel,
  não sempre para baixo).
- **Tabelas de dados exatos**: 23 linhas em "Arcos" (ordenadas por volume,
  maior primeiro) e 10 linhas em "Tarefas abertas" — conferidas contra o
  mesmo cálculo Python, valores idênticos.
- **0 erros de console reais** nas 8 páginas (as 7 existentes + Agentes) —
  único erro capturado é o 404 de `/favicon.ico`, já investigado, não é da
  aplicação.
- **Claro/escuro**: grafo, cores por agente e rótulos conferidos nos dois
  temas — sem regressão de contraste.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` — sem rolagem
  horizontal; o SVG encolhe proporcionalmente (`width:100%`), rótulos
  ficam pequenos mas legíveis, e a tabela de dados exatos abaixo cobre o
  caso de quem precisa do número preciso sem depender do desenho.
- **Regressão**: as 7 páginas existentes (Controle, Plano, Coordenação,
  Resultados, Referências, Grafo, Bibliometria) seguem com 0 erros de
  console — mudança ficou contida em `build_agentes()` (função nova),
  4 tokens de cor novos (aditivos) e 2 entradas em `NAV`/`pages` (aditivas).
  Nenhum arquivo de dados novo, nenhuma mudança em `painel.yml`
  (`mensagens.json` já era copiado para `_site/`).

## Closing tail

- `TAIL:review` — n/a: lane light, página nova mas 100% derivada de dados
  já existentes (nenhum compute novo, nenhuma superfície de escrita nova).
- `TAIL:security` — nenhuma superfície de rede nova; todo texto (nomes de
  agente, rótulos) passa por `esc()` antes de entrar no HTML/SVG, mesmo
  padrão do resto do site.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
