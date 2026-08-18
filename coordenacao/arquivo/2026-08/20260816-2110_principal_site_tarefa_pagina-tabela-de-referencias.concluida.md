---
de: principal
para: site
tipo: tarefa
acao_esperada: criar a página "Referências" no painel conforme especificação; publicar direto (sem gate, ADR 0010) e avisar o principal com a URL
referencia: pedido do autor 2026-08-16 · docs/handoff-site.md · scripts/render-plano-revisao.py · fichamentos/ · referencias.bib
criada_em: 2026-08-16T21:10:00Z
---

# Nova página do painel: tabela de referências da tese

Pedido literal do autor: "Quero no site de acompanhamento uma tabela com
cada referência que temos, ordenada por ordem de aparição no livro, mas a
tabela é ordenável, com Título, autores, aonde foi citada, link direto para
o artigo, se tenho o arquivo físico, sim ou não, se foi fichado, sim ou não
e um campo de visualizar detalhes, que traz o fichamento da obra."

## Especificação

**Página nova** `referencias.html`, entrada na sidebar existente, mesmo
CSS/JS compartilhado das 4 páginas atuais.

**Dados**: script novo `scripts/compute-referencias.py` (superfície sua)
gera `docs/records/referencias.json`, embutido no HTML no render (regra de
sempre: nada de fetch — o CSP dos artifacts bloqueia rede). Fontes:

- `referencias.bib` da main (parse das entradas: chave, título, autores,
  ano, venue, doi/url/eprint);
- todos os `*.tex` incluídos por `principal.tex`, na ORDEM de inclusão dos
  capítulos: extrair `\cite`/`\citep`/`\citet` (inclusive listas com
  vírgula) e registrar, por chave, a PRIMEIRA aparição (ordem no livro) e
  TODAS as ocorrências (capítulo + seção mais próxima acima);
- `fichamentos/<chave>.md`: existe → fichado=sim; do front matter, o campo
  `pdf:` → se o caminho declarado existir no repositório, arquivo
  físico=sim, senão não (chave sem fichamento: procurar
  `referencias-pdf/<chave>.pdf` direto).

**Tabela** (ordem padrão = ordem de primeira aparição no livro; TODAS as
colunas ordenáveis por clique no cabeçalho, com indicador asc/desc):

| Coluna | Conteúdo |
|---|---|
| # | posição na ordem de aparição (órfãs por último, marcadas "não citada") |
| Título | título da entrada |
| Autores | sobrenomes; >3 autores vira "Fulano et al." com tooltip completo |
| Onde citada | "Cap. 2 §2.3" da 1ª aparição + badge com o total de ocorrências; tooltip lista todas |
| Link | DOI > arXiv > URL, ícone de link externo; sem nenhum → "—" |
| PDF | sim/não (badge verde/cinza) |
| Fichado | sim/não (badge verde/cinza) |
| Detalhes | botão que expande a linha (ou modal) com o FICHAMENTO da obra renderizado |

**Detalhes/fichamento**: converter o markdown do fichamento para HTML no
BUILD (Python), não no cliente — sem lib externa no browser. Front matter
YAML vira uma ficha (título, autores, venue, DOI, relações); o corpo vem
abaixo. Chave sem fichamento: "Ainda não fichada".

**Cuidados**: tabela com rolagem horizontal própria em tela estreita (o
body nunca rola lateral); filtro de busca por texto livre em cima da tabela
ajudaria (a seu critério); atenção ao tamanho da página com ~140 fichamentos
embutidos (aceitável, mas medir; se passar de uns 8 MB, carregar o corpo do
fichamento sob demanda de um `<template>` inline por linha).

**Workflow**: acrescentar aos `paths` do `painel.yml`: `referencias.bib`,
`fichamentos/**`, `*.tex` das pastas de capítulo e o script novo.

Publica direto (sem gate) e responde a esta tarefa com a URL e o hash.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
