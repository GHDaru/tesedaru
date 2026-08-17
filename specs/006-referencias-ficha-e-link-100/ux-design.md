# ux-design.md — Referências: ficha e link para toda entrada

- **Ciclo**: 006-referencias-ficha-e-link-100 · **Lane**: light (tarefa já
  veio totalmente especificada pelo `principal`, mensagens `20260817-0055`
  e `20260817-0110` — pedido literal do autor, sem necessidade de consulta
  a especialistas).

## 1. Princípio central: nenhum botão morto

O pedido do autor foi direto: "importante a ficha e todos deveriam ter" +
"colocar também o link no site". A decisão de desenho segue disso sem
ambiguidade — **toda** entrada da tabela (fichada ou não, com ou sem DOI)
precisa ter um botão "Detalhes" que abre conteúdo real e um link que
realmente vai a algum lugar. Nunca um placeholder vazio, nunca um `href`
ausente.

## 2. Três estados de link, nunca confundidos entre si

O autor pediu explicitamente honestidade visual entre link direto e busca.
Solução: o **rótulo de texto já diz qual é qual** (`doi ↗` / `arxiv ↗` /
`link ↗` vs. `buscar ↗`) — reforçado por um sublinhado tracejado
(`.ref-link-busca`) só nos links de busca, nunca a única pista (mesma
régua do site inteiro: nunca estado só por cor). Os três estados:

1. **Link direto** — DOI > arXiv > URL, na mesma ordem de hierarquia já
   existente.
2. **Busca pronta** — quando não há identificador nenhum, um link de busca
   no Google Scholar (título entre aspas + primeiro autor) já com a
   consulta pronta. Racional do autor: ele quer clicar e cair direto numa
   busca útil, não digitar tudo de novo.
3. **Fichada / não fichada** — eixo INDEPENDENTE do link (uma obra pode
   ter DOI e não estar fichada, ou estar fichada sem DOI nenhum). Continua
   representado pela coluna "Fichado" já existente, sem mudança.

## 3. Ficha básica: o que aparece quando não há fichamento

Antes desta rodada, uma obra sem fichamento mostrava só "Ainda não
fichada." — um beco sem saída. Agora o detalhe sempre tem conteúdo:
título completo, autores por extenso (não só sobrenome — diferença
proposital do resto da tabela, que usa sobrenome para caber na coluna),
veículo, ano, volume/número/páginas quando existem no `.bib`,
identificador (DOI ou arXiv), e onde a obra é citada no texto — tudo
precedido de um selo "📄 Ficha básica... ainda não foi fichada
academicamente", para nunca confundir com um fichamento de verdade.

## 4. Ficha no Semantic Scholar — pedido à parte, mesmo padrão

O adendo do autor (mensagem 0110) esclareceu que ele usa a página da obra
no Semantic Scholar como uma **ficha externa própria** de conferência —
por isso ela entra dentro do painel de Detalhes (não na coluna Link
principal, que seria uma terceira coluna competindo por atenção). Mesma
lógica de honestidade: `Ficha S2 ↗` quando resolvido de verdade via API
(por DOI/arXiv), `Ficha S2 (buscar) ↗` quando cai no fallback de busca no
próprio site do S2.

## 5. Decisão de arquitetura: resolução por API, cache persistente, sem rede no cliente

Only o `compute-referencias.py` (build) toca a rede — o HTML/JS que roda
no navegador do leitor nunca faz `fetch`, mantendo o princípio "nenhuma
dependência de rede em tempo de execução" que vale para o resto do site.
A API pública do Semantic Scholar tem limite de taxa sem chave (confirmado
na prática: `429 Too Many Requests` já apareceu durante o desenvolvimento
desta própria rodada) — por isso:

- **Cache persistente** em `docs/records/s2-cache.json`, chave por chave
  do `.bib`. Cada build só tenta resolver entradas AINDA não cacheadas
  (até um orçamento de 50 por rodada), exatamente como pedido.
- **Falha de rede/timeout nunca vira "não encontrado" permanente** — só
  uma resposta real da API (achou o paper, ou 404 de verdade) é definitiva
  e vai para o cache. Um 429 ou timeout fica pendente para a próxima
  rodada. Depois de 3 falhas transientes seguidas, a rodada desiste cedo
  (assume rede fora do ar) em vez de gastar o orçamento inteiro em
  timeouts.
- **Nada quebra o build**: sem rede nenhuma, `resolve_s2()` simplesmente
  não resolve nada nesta rodada — toda referência cai no link de busca do
  S2, que sempre funciona sem depender de API nenhuma.

**Nota de arquitetura sobre persistência entre deploys**: o workflow
`painel.yml` não commita de volta o `s2-cache.json` que ele mesmo regera
durante o build (nenhum script deste site faz isso hoje — o mesmo vale
para `kpis.json`/`mensagens.json`). Ou seja, o progresso de resolução via
API feito DENTRO de um deploy de CI não persiste para o próximo deploy
sozinho; quem faz o cache crescer de fato é uma sessão de agente rodando
`compute-referencias.py` localmente e commitando o resultado — o mesmo
ritual já usado para os outros JSONs de `docs/records/`. Registrado aqui
para não parecer um comportamento diferente do resto do site por acidente;
é a mesma arquitetura, aplicada de forma consistente.

## 6. Reuso (nada disto é papel novo)

`.pill`/badge sim-não, `.ref-det-btn`/`.ref-det-row` (painel de detalhe já
existente), `<details>` não é usado aqui — o padrão já era expandir a
linha da tabela, mantido. Papel novo pequeno: `.ref-link-busca` (sublinhado
tracejado + cor `--muted`, reforço visual de "isto é busca, não link
direto") — reutilizável em qualquer outro link de fallback que o site
venha a precisar no futuro.
