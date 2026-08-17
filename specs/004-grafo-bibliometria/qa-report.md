# QA Report 004 — Páginas Grafo e Bibliometria

- **Lane**: light — pedido direto do autor na sessão ("chame ao menos 3
  especialistas... consolide, registre a decisão e comece o ciclo de
  implementação"). `ux-design.md` consolida os 3 pareceres (`ux-semantics`,
  bibliometria acadêmica, visualização de dados) e cobre o porquê de cada
  decisão de tela. Sem spec.md/plan.md/tasks.md separados — decisão de
  escopo e critérios de aceite vieram do pedido do autor + consolidação dos
  especialistas, rastreados nesta sessão.

## Decisões consolidadas (resumo — pareceres completos no histórico da sessão)

1. **Grafo = janela para um instrumento externo (`<iframe>`), não
   reimplementação.** `kg_template.html` tem identidade visual própria; a
   moldura é honesta sobre isso (sem `.card` duplicando moldura, altura
   relativa ao viewport, rompe o `max-width` de leitura, escape hatch "abrir
   em nova aba" obrigatório).
2. **O que NÃO entra na Bibliometria, com razão registrada**: lei de Lotka,
   lei de Bradford, h-index/proxy, mapa temático por co-ocorrência de
   palavras-chave — todos pressupõem levantamento sistemático de campo; os
   378 itens são uma bibliografia curada de UMA tese (seleção editorial),
   não uma amostra do campo científico. Aplicar essas técnicas emprestaria
   autoridade estatística que os dados não sustentam.
3. **O que entra, sempre com rótulo de escopo visível no texto (nunca só em
   tooltip)**: publicações por ano, top-10 autores/veículos NESTA
   bibliografia, frequência de citação DENTRO DO TEXTO da tese, cobertura de
   fichamento, distribuição por pilar (P1-P4, IDs/nomes herdados de
   `resultados.json` sem redigitar).
4. **Nomenclatura**: o grafo de relações do `kg.json` é chamado "mapa de
   argumentação"/"grafo de conhecimento fichado" — nunca "rede de
   co-citação" (termo técnico que pressupõe inferência estatística
   automática; aqui é julgamento humano direto de conteúdo).
5. **Nenhum campo novo inventado** em `compute-referencias.py` (ex.: "tipo
   de fonte" por heurística sobre `venue`) — a distribuição por pilar é
   computada a partir das arestas `type:"pillars"` já existentes em
   `kg.json`, não de um campo especulativo.

## Verificação (Playwright/Chromium, dados reais, servidor local simulando o build de CI)

- **Pipeline completo simulado localmente**: `compute-kpis.py` →
  `compute-mensagens.py` → `compute-referencias.py` → `fichamentos/
  build_kg.py` → `render-plano-revisao.py` → cópia de
  `fichamentos/kg.html` para `grafo-embed.html`, na mesma ordem do
  `painel.yml` atualizado.
- **0 erros de console** nas 7 páginas do site (Controle, Plano,
  Coordenação, Resultados, Referências, Grafo, Bibliometria) — verificado
  com `pageerror` e console `error` listeners.
- **Grafo**: iframe carrega `grafo-embed.html` (200 OK, 526 nós · 1048
  arestas no cabeçalho da página batendo com a saída do `build_kg.py`);
  filtros nativos do instrumento (Artigos fichados/A fichar/FALCO/Temas/
  Pilares/Métodos/Conceitos/Modelos/Datasets/Tarefas) e física de força
  renderizam corretamente dentro da moldura; link "abrir em nova aba"
  presente e aponta para o arquivo standalone.
- **Bibliometria**: KPIs conferem com o JSON bruto — 378 referências, 152
  citadas, 151 fichadas (40%), 150 com PDF (40%); gráfico de publicações
  por ano com bucket "≤1999" (42 itens) + barras individuais 2000–2026 com
  eixo legível; rankings top-10 de autores/veículos/mais-citadas com valor
  sempre em texto (nunca só barra); distribuição por pilar com nomes
  herdados de `resultados.json` (P1–P4 + bucket "Geral / transversal" para
  114 entradas sem pilar específico).
- **Tema claro/escuro**: as 2 páginas verificadas nos dois `colorScheme`
  (`dark`/`light`) via `page.newContext({colorScheme})` — sem regressão
  visual, tokens de cor aplicados corretamente (iframe do Grafo mantém
  paleta própria por design, ver `ux-design.md` §2).
- **Mobile (390×844)**: as 2 páginas verificadas — `document.documentElement
  .scrollWidth <= clientWidth` em todos os 4 cenários (2 páginas × 2 temas),
  ou seja, nunca há rolagem horizontal do `body`; sidebar colapsa para o
  padrão já usado nas outras 5 páginas.
- **404 investigado e descartado como não-bug**: um `console: error` de
  `favicon.ico 404` apareceu em 1 de 8 combinações tema/viewport testadas;
  reproduzido isoladamente e confirmado como requisição automática do
  Chromium por um favicon que o site nunca declarou (nenhuma página do site
  tem `<link rel="icon">) — não é um recurso da própria página quebrado, e
  não se repete de forma determinística entre execuções.
- **Regressão**: as outras 5 páginas seguem com 0 erros de console e
  navegação/destaque de item ativo corretos — só a sidebar (2 novos itens)
  e o `main()` mudaram fora das novas funções `build_grafo()`/
  `build_bibliometria()`.
- **`fichamentos/kg.json`/`kg.html` não foram alterados neste commit**:
  regenerados localmente só para teste e restaurados via `git restore`
  antes do commit — são conteúdo de outros agentes (fichamento), fora da
  superfície do site; o `painel.yml` os regenera de forma efêmera a cada
  deploy, sem depender da cópia commitada estar em dia.

## Closing tail

- `TAIL:review` — n/a nesta rodada: lane light, mudança aditiva (2 funções
  novas + 2 itens de sidebar + 1 passo de workflow), sem alterar nenhuma
  função existente das outras 5 páginas; verificação própria com evidência
  acima substitui a revisão formal em contexto fresco para este ciclo leve.
  Registrado no aviso ao `principal` para que ele decida se quer pedir
  revisão adicional.
- `TAIL:security` — `build_kg.py` já existia e só lê arquivos do próprio
  repositório (front-matter YAML de `fichamentos/*.md` + regex sobre
  `*.tex`), sem rede nem `eval`; o iframe do Grafo aponta para um arquivo
  do mesmo domínio (`grafo-embed.html`, gerado no mesmo build, sem origem
  externa) — sem risco de conteúdo de terceiros embutido. n/a como risco de
  segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
