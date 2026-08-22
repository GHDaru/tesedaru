# ux-design.md — Resultados: cards de experimento, pilares vazios e sumário

- **Ciclo**: 013-resultados-ux-cards-e-sumario · **Lane**: light — pedido
  direto do autor ("Chame especialista de uxui ao menos três para melhorar
  a entrega visual e a usabilidade"), logo após o ciclo 012 (link do
  notebook Kaggle). Consultei 3 especialistas independentes antes de
  decidir — este documento cobre a consolidação, não só o resultado.

## 0. Por que 3 especialistas de novo

Mesmo ritual do ciclo 011 (mapa de agentes): 3 pareceres em background, sem
se verem uns aos outros, mesmo material real (código de `build_resultados()`
+ screenshots claro/escuro da página publicada no ciclo 012) — um
especialista em tabelas/design de informação, um em visual/tipografia, um
em usabilidade/interação. A própria tabela de experimentos (recém-ampliada
com a coluna de notebook) era o gatilho óbvio: eu mesmo já tinha notado, ao
testar o ciclo 012, que a coluna nova só aparecia rolando a tabela para a
direita.

## 1. O que os três disseram (resumo)

- **Tabelas/dados**: diagnóstico duro — o problema não é "falta espaço para
  a coluna nova", é que a seção nunca deveria ter sido uma tabela. As 7
  linhas têm células de tamanho radicalmente desigual (um ID de 2
  caracteres ao lado de um parágrafo de 400) — isso É o que força a
  rolagem. Recomenda cartão por experimento (mesmo padrão de "Entregas" já
  na página), e argumenta explicitamente contra o padrão
  resumo+`<details>` de Referências aqui: com 300+ referências, esconder o
  detalhe por padrão compensa; com 7 experimentos, forçar um clique extra
  em cada um para ver o que 99% dos visitantes vieram ler é fricção sem
  retorno.
- **Visual/tipografia**: concorda que a tabela é o formato errado (propõe
  o padrão accordion de Referências como alternativa, mas sem confrontar o
  argumento de escala acima). Levanta dois problemas independentes e reais:
  (1) os cards de pilar sem achado (P1, P2) usam a mesma classe `.card` e o
  mesmo peso visual dos pilares com achado real (P3, P4) — dois blocos
  vazios na frente de dados reais atrasam a leitura de quem abre a página;
  (2) a página não tem nenhum sumário/âncora, e vai crescer (mais achados,
  mais experimentos). Recomenda contra espalhar a cor `--accent` para os
  links do notebook — o verde já tem um significado único ("o número que a
  tese prova"); resolver isolando estruturalmente o link é melhor que
  disputar a mesma cor para dois significados.
- **Usabilidade/interação**: foco na coluna escondida como defeito real
  (não estético) — bloquearia a entrega, principalmente porque é
  justamente a rastreabilidade que a banca mais cobra ficando invisível.
  Recomenda sombra de rolagem em CSS puro no `.scroll` compartilhado (sem
  JS, beneficia todas as tabelas do site) + `aria-label` no link do
  notebook (hoje "abrir ↗" repetido em 7 linhas seria ambíguo para leitor
  de tela em modo de navegação por links). Explicitamente contra
  reestruturar para cards — considera isso além do que foi pedido.

## 2. Decisão consolidada

Dois dos três especialistas (o de tabelas/dados e o de tipografia), por
caminhos diferentes, chegaram à mesma conclusão: a tabela é a estrutura
errada para 7 itens com esse formato de conteúdo. O de tabelas/dados deu o
argumento mais completo (a comparação direta com Referências — por que
`<details>` se paga a partir de dezenas de itens, não com 7) e a
implementação mais concreta. Fui com **cards de experimento**, não com o
accordion nem com o remendo de sombra:

- **Cards resolvem a causa, não só o sintoma**: zero rolagem horizontal na
  seção inteira (testado: `scrollWidth <= clientWidth` em 1280px E em
  390px), então a "correção" do especialista de usabilidade (sombra +
  aria-label) deixa de ser necessária ali — o problema que ele descreveu
  como bloqueante simplesmente some.
- O selo do notebook (reaproveitando `.pill.feito`/`.pill.pendente`, já
  usado em Referências para o mesmo tipo de indicador sim/não — sugestão
  minha, não de nenhum parecer, mas seguindo a recomendação do especialista
  de tipografia de "não inventar semântica nova, reusar convenção") fica
  sempre visível no topo do card, nunca atrás de scroll nem de hover — isso
  também resolve o ponto 3 do especialista de tabelas/dados (o antigo "—"
  só explicava a ausência em `title`, invisível em touch) e o `aria-label`
  do especialista de usabilidade (mantive: `aria-label="abrir notebook
  Kaggle do experimento E6"`).
- **Não usei `--accent` no selo** — seguindo a recomendação do especialista
  de tipografia, `.pill.feito` usa o token de status `--st-feito` (verde
  diferente, já reservado para "está feito"), não o verde de "número
  provado". Os dois significados continuam separados.
- **Pilares vazios** (P1, P2) ganharam tratamento diferente: uma linha
  tracejada compacta (`.pilar-vazio`) em vez de `.card` cheio — exatamente
  a correção que o especialista de tipografia propôs, mudança pequena e
  isolada da decisão dos cards.
- **Sumário de âncoras** no topo (`Achados (2 de 4 pilares) · Entregas (8)
  · Experimentos (7)`), contagens calculadas a partir do próprio JSON, sem
  hardcode. `scroll-margin-top` nas 3 seções para o salto de âncora não
  colar o título na borda da tela.

**Deixei de fora, por ora**: a sombra de rolagem em CSS no `.scroll`
compartilhado (recomendação do especialista de usabilidade). Ela ainda
beneficiaria a tabela de Referências (que continua sendo tabela de
verdade — 337 linhas, ali o formato está certo), mas essa página não foi
tocada neste ciclo e o pedido do autor mirava a entrega que acabou de
subir. Registrado aqui para retomar se algum dia vier reclamação parecida
em Referências.

## 3. Reuso

`.pill.feito`/`.pill.pendente` (Referências, ciclo 006) para o selo do
notebook — nenhuma classe nova de badge. `.entrega`/`.entregas` (mesma
página, bloco "Entregas") como modelo direto para `.experimento-card`/
`.experimentos-grid` — mesma receita de borda + `border-radius` + padding +
fundo `--ground`, só com mais campos internos. `--st-feito`/`--st-feito-bg`
e `--st-gate`/pendente (tokens já existentes, usados em Plano/Coordenação)
para o par disponível/ausente do selo.
