# ux-design.md — Página Referências (referencias.html)

- **Ciclo**: 003-pagina-referencias · **Lane**: light (tarefa já veio
  totalmente especificada pelo `principal`, mensagem `20260816-2110` — sem
  necessidade de consulta a especialistas desta vez).
- **Consome**: tarefa do `principal`, pedido literal do autor citado nela.

Artefato obrigatório deste ciclo (toca uma tela). Curto, porque a jornada e
a anatomia já vieram fechadas na tarefa — este documento fixa só o que ela
deixou implícito.

## 1. Jornada

O autor abre esta página para responder duas perguntas diferentes, na
mesma tela: **"o que já tenho fichado e com PDF, e o que ainda falta?"**
(varredura rápida, sim/não) e **"o que exatamente esta obra sustenta na
tese, e onde?"** (aprofundamento pontual em UMA linha por vez, via
Detalhes). A tabela serve a primeira pergunta; o Detalhes expansível serve
a segunda — são dois ritmos de leitura diferentes na mesma tela, e a
página não pode forçar o segundo ritmo sobre todo mundo (por isso Detalhes
é expansível sob demanda, nunca aberto por padrão).

## 2. Papel de cada coluna (por que existe, não só o que mostra)

- **#** — não é um índice arbitrário: é a ordem real de leitura do livro.
  Serve para o autor achar rápido "o que vem primeiro" e para auditar se a
  bibliografia acompanha a narrativa. Órfãs (nunca citadas) não têm
  posição — aparecem por último, marcadas, nunca misturadas silenciosamente
  entre as citadas.
- **Onde citada** — não é só "em que capítulo": o badge de contagem
  responde "isso é citado uma vez de passagem ou é uma referência
  estrutural?" sem o autor precisar abrir nada.
- **PDF / Fichado** — dois badges sim/não INDEPENDENTES um do outro
  (ter o PDF não implica estar fichado, e vice-versa é raro mas o dado não
  assume). Cada um responde uma pergunta de prontidão diferente: "posso
  reler a fonte primária?" vs. "já processei academicamente esta fonte?".
- **Detalhes** — não é uma pré-visualização, é o fichamento inteiro. Uma
  chave sem fichamento mostra "Ainda não fichada" — nunca uma linha vazia
  ou escondida, porque a ausência de fichamento é, ela mesma, informação
  de prontidão que a tabela já anuncia na coluna Fichado.

## 3. Estado nunca só por cor (regra já vigente no site inteiro)

Badges PDF/Fichado usam glifo+palavra (✓/✕ + "sim"/"não"), nunca só a cor
de fundo — mesma régua do kanban (ADR 0006, achado do ciclo 002: a
citação correta do princípio é comportamental, não o número do ADR).

## 4. Ordenação

Todas as colunas ordenáveis por clique no cabeçalho (pedido explícito do
autor). Papel do clique: alterna asc → desc → volta à ordem padrão (ordem
do livro) na terceira clicada — nunca fica "preso" numa ordenação
secundária sem uma saída óbvia de volta à leitura natural.

## 5. Volume (~150 fichamentos embutidos)

Medido: ~527KB de JSON com todos os corpos de fichamento já renderizados
em HTML no build — bem abaixo do teto de 8MB que a tarefa citou como
gatilho para carregamento sob demanda. Decisão: **tudo embutido de uma
vez**, sem `<template>`/lazy-load — YAGNI (Princípio VII): a complexidade
de carregamento sob demanda não se paga para 527KB.

## 6. Reuso (nada disto é papel novo)

`.card`, `.pilula` (mesma pílula de filtro do kanban, reusada para busca
por texto livre — ver §7), badges sim/não (mesmo padrão visual de
`.k-badge`/glifo+palavra), `.scroll` (rolagem horizontal própria de
tabela, já usada em "Arquivadas"), tokens de tipografia/espaço
(`--fs-*`/`--sp-*`). Papel novo: **cabeçalho de coluna clicável com
indicador de direção** (▲/▼) — não existe ainda no site, é infraestrutura
de navegação (como N01–N05 do catálogo do harness, não um entregável de
conteúdo).

## 7. Adição além da spec literal (decisão registrada, não escondida)

A tarefa sugeriu "filtro de busca por texto livre... a seu critério".
Decisão: incluir — com ~150 linhas, encontrar uma referência por título
sem rolar é a mesma necessidade que já resolvemos no kanban com pílulas de
filtro; aqui o equivalente é busca textual (título/autor/chave), porque a
variável relevante não é categórica (agente/tipo) e sim texto livre.
