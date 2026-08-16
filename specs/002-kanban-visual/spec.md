# Spec 002 — Board kanban da Coordenação: caber na tela

- **Status**: Em implementação · **Lane**: light · **Date**: 2026-08-16
- **Origin**: pedido direto do autor na sessão, com screenshot do board ao vivo
  (`mensagens.html`): a coluna "Aberta" com 38 cartões cresce sem limite,
  produzindo uma página gigante e desequilibrada frente às colunas vizinhas
  ("Em andamento", "Concluída", poucos cartões). Pedido: "deve caber na
  tela". O autor pediu explicitamente o rito completo — consulta a três
  especialistas, consolidação, e um ciclo especificando → planejando →
  tasqueando → implementando.

## What and why

O board kanban (entregue na Fatia 2, ciclo anterior sem spec formal) tem um
defeito de layout real: a coluna `.k-cards` não tem limite de altura nem
rolagem própria, então ela cresce linearmente com o número de cartões. Um
segundo defeito, encontrado pelos especialistas na leitura do código (não
relatado pelo autor, mas correlato), agrava o primeiro: o mecanismo de corte
por volume (`CAP_ENABLED`) mede o TOTAL de mensagens do board inteiro
(`ativas.length > 50`), não o tamanho de cada coluna — então uma coluna
isolada com 38 cartões nunca aciona o corte se o total do board ficar
abaixo de 50.

Três especialistas foram consultados em paralelo, cada um lendo a
implementação real (`scripts/render-plano-revisao.py`, função
`build_coordenacao()`) antes de opinar:

1. **ux-semantics** (papel semântico, Princípio VII do método): produziu
   `ux-design.md` — decisão de que a coluna deve ser uma "raia limitada"
   (altura ~constante, definida pelo board, não pelo conteúdo) com rolagem
   interna própria, e que os cartões devem ser ordenados por prioridade
   dentro da raia.
2. **especialista em dashboards kanban enterprise** (mecânica concreta,
   padrão Trello/Linear/Jira): confirmou a causa raiz, propôs CSS concreto
   (`max-height` + `overflow-y:auto` em `.k-cards`, não em `.k-col`),
   recomendou aposentar o mecanismo de corte quebrado, e identificou um
   terceiro problema real (zona de largura 900–1099px onde 3 colunas fixas
   ficam espremidas).
3. **especialista em acessibilidade/legibilidade sob pressão**: confirmou a
   mesma causa raiz de forma independente, encontrou que "atrasado" fica
   perdido no fim de uma linha de 12px, que a truncagem por `title` é
   inacessível por teclado, e que faltam landmarks de região nas colunas.

Os três convergiram, sem coordenação entre si, na mesma causa raiz e na
mesma direção de solução — sinal forte para agir.

## Functional requirements

- **FR1**: cada coluna do board (`.k-cards`) tem altura máxima previsível
  (~constante entre as 3 colunas do mesmo board, via `clamp()`) com rolagem
  vertical própria quando o conteúdo excede essa altura — nunca a rolagem
  da página inteira. O cabeçalho da coluna (glifo + nome + contagem) fica
  fora do container que rola, sempre visível.
- **FR2**: dentro de cada coluna, os cartões são ordenados por prioridade:
  (atrasado E para-você) → para-você → atrasado → demais por recência —
  para que o essencial apareça no topo mesmo sem rolar.
- **FR3**: o mecanismo de corte por DOM (`CAP_ENABLED`/`CAP`/botão "+N
  mais", hoje quebrado por medir o total do board) é removido — a rolagem
  interna resolve exibição sem esconder nenhum cartão real atrás de um
  clique, o que também cumpre a regra do produto "sem paginação nem
  rolagem infinita" com mais fidelidade do que o mecanismo anterior.
- **FR4**: densidade do cartão reduzida sem sair da escala de tokens
  existente (`--fs-*`/`--sp-*`): título truncado a 2 linhas (texto
  completo via `title`, mesmo padrão já usado em `k-ref`), `line-height`
  mais compacto, padding/gap internos reduzidos.
- **FR5**: "atrasado" ganha mais peso visual (negrito + glifo de atenção)
  sem introduzir um segundo destaque forte que compita com a borda âmbar
  de "para você" — ADR 0006 continua valendo ("nada mais compete").
- **FR6**: largura das colunas em viewports médios (601–1099px): o board
  passa a rolar na horizontal com largura mínima por coluna, em vez de
  espremer 3 colunas fixas até o texto quebrar mal. Breakpoints: ≥1100px
  grid de 3 colunas fixas · 601–1099px flex com scroll horizontal ·
  ≤600px empilhado (1 coluna).
- **FR7**: acessibilidade mínima e barata: cada coluna como região
  navegável (`role="region"` + `aria-labelledby` apontando pro `h2`
  existente), container de rolagem alcançável por teclado (`tabindex="0"`
  + `aria-label`), região `aria-live="polite"` anunciando a contagem após
  mudança de filtro.
- **FR8**: distinguir "coluna vazia de verdade" de "vazia só por causa do
  filtro ativo" (hoje as duas mostram o mesmo texto "Nada aqui").

## Out of scope (decisão registrada, não esquecida)

- **Truncagem do título/referência por `title` nativo continua
  mouse-only** (gap de acessibilidade real, achado pelo especialista de
  legibilidade) — corrigir isso direito exige um widget de disclosure
  focável (ex.: `&lt;details&gt;`), uma mudança de interação maior que o
  escopo "caber na tela" deste ciclo. Registrado como follow-up.
- **Estado explícito para `mensagens.json` ausente/corrompido** (hoje
  indistinguível de "coordenação sem pendências", achado pelo
  especialista de semântica) — fica para um ciclo de robustez de dados,
  não de layout.
- **Se "para você" deveria cobrir broadcasts `para: "todos"`** — achado do
  especialista de acessibilidade de que, nos dados reais, `para: "autor"`
  nunca ocorre, então o único destaque forte do produto pode nunca
  disparar. É uma pergunta de modelo de dados/regra de negócio da
  coordenação, não de estilo visual — não decido isso sozinho neste
  ciclo; registro para o `principal` avaliar.
- Type do cartão (tarefa/pergunta/aviso) como borda colorida — descartado
  nesta rodada por risco de competir visualmente com a borda âmbar de
  "para você" (ADR 0006 proíbe qualquer segundo destaque forte); mantido
  como texto pequeno, só com espaçamento mais compacto (FR4).

## Acceptance criteria (executável — verificado no qa-report.md)

- AC1: com 72 mensagens sintéticas (38 numa única coluna), a altura de
  `.k-cards` não excede o teto definido (`clamp(320px,58vh,640px)`) em
  nenhuma das 3 colunas — medido via Playwright (`boundingBox().height`).
- AC2: a rolagem interna da coluna funciona (scrollTop muda ao rolar) e a
  rolagem da página não é acionada pelo volume de cartões (altura da
  página com 72 mensagens sintéticas comparável à altura com os dados
  reais atuais, não proporcional a N).
- AC3: dentro de uma coluna com cartões "para você" e "atrasado"
  misturados a cartões comuns, os primeiros aparecem nas primeiras
  posições do DOM.
- AC4: 0 erros de console nas 4 páginas do site, tema claro/escuro
  corretos, breakpoint de 600px e 900-1099px verificados visualmente.
- AC5: `role="region"`/`aria-labelledby`/`tabindex` presentes nas 3
  colunas; navegação por Tab alcança o container de rolagem.
