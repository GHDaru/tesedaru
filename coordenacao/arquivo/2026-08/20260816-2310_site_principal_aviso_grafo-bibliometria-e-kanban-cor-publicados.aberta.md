# Aviso: páginas Grafo + Bibliometria publicadas; kanban com cor por agente

**De**: site · **Para**: principal · **Tipo**: aviso
**Quando**: 2026-08-16 23:10 UTC

## O que foi publicado (direto na main, ADR 0010 — site/painel dispensa gate)

Dois pedidos do autor, executados como dois ciclos separados:

### 1. Ciclo 004-grafo-bibliometria (commit `96ada9f`)

Pedido do autor: "inclua o grafo semântico... mais um item no menu" + "temos
bibliometria... podemos fazer algo similar" ao `bibliometrix` de R.
Instrução explícita: consultar ≥3 especialistas (UX/UI + bibliometria
acadêmica), consolidar, registrar a decisão, implementar. Consolidação
completa em `specs/004-grafo-bibliometria/{ux-design.md,qa-report.md}`.

- **Grafo** (https://ghdaru.github.io/tesedaru/grafo.html) — janela
  `<iframe>` para o instrumento já existente (`fichamentos/kg.html`, 526 nós
  · 1048 arestas), moldura explicitamente honesta sobre ser outro sistema
  (sem duplicar cartão, altura relativa ao viewport, rompe a largura de
  leitura do resto do site, link "abrir em nova aba" sempre visível).
  Chamado **"mapa de argumentação"**, nunca "rede de co-citação" — decisão
  do especialista de bibliometria: é julgamento humano registrado no
  fichamento, categoria diferente de inferência estatística automática.
- **Bibliometria** (https://ghdaru.github.io/tesedaru/bibliometria.html) —
  composição/atualidade/distribuição da bibliografia da tese (378
  referências), nunca confundida com "o que a pesquisa descobriu" (isso
  continua em Resultados). **Decisão deliberada e registrada**: lei de
  Lotka, lei de Bradford, h-index/proxy e mapa temático por co-ocorrência
  ficaram **fora** deste ciclo — todos pressupõem levantamento sistemático
  de um campo científico inteiro, e 378 itens curados por um único autor
  não são essa amostra; aplicar essas técnicas emprestaria autoridade
  estatística que os dados não sustentam. Todo gráfico carrega o rótulo do
  próprio escopo no texto visível (nunca só em tooltip). A distribuição por
  pilar (P1–P4) é computada das arestas já existentes em `kg.json`, sem
  inventar campo novo em `compute-referencias.py`.
- `painel.yml` passou a rodar `fichamentos/build_kg.py` a cada deploy e
  publicar `kg.html` como `grafo-embed.html` — sempre regenerado no
  momento do build, nunca depende da cópia commitada de `kg.json`/`kg.html`
  estar em dia (essas continuam sendo conteúdo de fichamento, fora da
  superfície do site).

### 2. Kanban — cor por agente + fonte menor (commit `99fabfe`)

Pedido do autor, direto e já especificado: "reduzir um pouco a fonte e
colocar uma cor para cada agente... pode ser o card inteiro, ou uma tag -
um ux pode decidir". Decisão de UX tomada e registrada em comentário no
próprio CSS: **tag pequena** (pontinho colorido de 8px + nome do agente por
extenso ao lado), não o cartão inteiro pintado — pintar o cartão inteiro
competiria com o sinal âmbar de "para você"/"atrasado", que precisa
continuar sendo o mais saliente da tela do quadro. O mesmo pontinho entra
nas pílulas do filtro por agente, funcionando como legenda sem precisar de
elemento novo. Título do cartão caiu de 15px para 13px.

## Verificação (Playwright/Chromium, dados reais, nos dois ciclos)

0 erros de console nas 7 páginas do site, tema claro/escuro e mobile
(390px, sem rolagem horizontal do body) checados para as 3 telas tocadas
(Grafo, Bibliometria, Coordenação). Deploys confirmados verdes via GitHub
Actions (`run 131` e `run 132`) e as URLs ao vivo retornam 200.

## Nada pendente do meu lado

Site com 7 páginas (Controle, Plano, Coordenação, Resultados, Referências,
Grafo, Bibliometria). Sem bloqueios, sem gate pendente (site dispensa gate
por ADR 0010) — só este aviso para o registro da coordenação.
