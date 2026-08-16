---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma ação obrigatória — registro de conclusão; ITEM QUE PRECISA DE VOCÊ: decidir o que fazer com a citação "ADR 0006" incorreta nos artefatos deste ciclo (ver abaixo)
referencia: tesedaru branch main (863b257) · specs/002-kanban-visual/ · pedido direto do autor na sessão
criada_em: 2026-08-16T20:15:00Z
---
Ciclo Maestro completo (spec → plan → tasks → implement → DoD → review
independente) para corrigir um defeito real no board kanban da Coordenação:
a coluna "Aberta" crescia sem limite (38 cartões numa sessão real do autor),
produzindo uma página gigante e desequilibrada. Pedido veio direto do autor
na sessão, com screenshot, pedindo explicitamente o rito completo — 3
especialistas em paralelo, consolidação, e o ciclo formal.

Artefatos completos em `specs/002-kanban-visual/` (spec.md, ux-design.md,
plan.md, tasks.md, qa-report.md) — primeiro ciclo do agente `site` seguindo
o método Maestro por inteiro, não só a convenção de commit.

## O que mudou
- Coluna do kanban virou uma "raia limitada": altura ~constante entre as 3
  colunas, rolagem própria (nunca a página inteira crescendo com N
  cartões).
- Removido um mecanismo de corte que estava quebrado desde a Fatia 2 (media
  o total do board, não por coluna — por isso nunca disparava com uma
  coluna sozinha grande).
- Cartões ordenados por prioridade dentro da coluna (atrasado+para-você >
  para-você > atrasado > recência) — o essencial fica visível sem rolar.
- Densidade reduzida (título com 2 linhas + reticências), breakpoint novo
  para telas médias (601-1099px, rolagem horizontal em vez de espremer),
  acessibilidade básica (regiões navegáveis, contagem anunciada por leitor
  de tela).

## Achado real durante o próprio ciclo (não previsto pelos 3 especialistas)
Um bug de CSS clássico (overflow em flex/grid aninhado por falta de
`min-width:0`) apareceu no primeiro teste visual e foi corrigido antes de
publicar — documentado no qa-report.md.

## ITEM QUE PRECISA DE VOCÊ: citação de ADR incorreta
A revisão independente (TAIL:review, agente `review`, contexto fresco)
conferiu o texto real de `docs/adr/0006-camada-de-kpis-e-dashboard-de-
evolucao.md` e confirmou que ele cobre só a página Controle/KPIs — não
menciona `mensagens.html` nem o cartão "para você" do kanban. Mas a
citação "ADR 0006 — regras de design vinculantes" para essas mesmas regras
(fila do autor é o único grito visual, estado nunca só por cor) veio
LITERALMENTE da sua própria tarefa 20260816-1836 ("Regras de design
vinculantes (ADR 0006 — não revogue)"), então não inventei essa citação —
só a propaguei. O princípio em si está correto e é bom (reusei e apliquei
no kanban sem violar nada), só a referência ao número do ADR está
desalinhada com o texto real desse ADR. Sugiro: emendar o ADR 0006 para
declarar explicitamente que o princípio vale para o site inteiro, ou abrir
um registro em `docs/records/decisoes.jsonl` apontando a fonte correta. Não
é decisão minha — fica com você.

## Nota de processo (não é sobre o código, é sobre como rodei a revisão)
O agente de revisão (TAIL:review) rodou sem isolamento próprio (sem
`isolation:worktree`), compartilhando o mesmo diretório de trabalho desta
sessão — que seguiu commitando/rebaseando/dando push DURANTE a revisão
dele. Ele viu o chão se mexer (git status mudando, um system-reminder sobre
CLAUDE.md) e levantou isso corretamente como possível manipulação — apurei
e é um falso alarme (CLAUDE.md mudou de verdade, por outro agente da
coordenação, `git log -S` confirma). Mas é uma lição real: revisões
independentes futuras (minhas ou de qualquer agente) deveriam rodar em
worktree isolado, ou eu deveria parar de mutar o repo enquanto uma roda.
Registrado no qa-report.md para não se perder.

## Evidência
Testado com até 72 mensagens sintéticas (38 numa coluna): altura das 3
colunas idêntica e dentro do teto definido, rolagem interna funcional,
ordem de prioridade correta, 0 erros de console em claro/escuro/mobile/
breakpoint intermediário, atributos de acessibilidade presentes e
alcançáveis por teclado. Revisão independente confirmou tudo isso de novo,
de forma cega, gerando o site real e testando no navegador — não confiou só
no meu relatório.

- https://ghdaru.github.io/tesedaru/mensagens.html (board kanban)

## Também nesta sessão
Encontrei, ao consultar `docs/declaracao-uso-ia.md` por outro motivo, que o
experimento **E5** (que eu tinha marcado como "não localizado" no ciclo
anterior) é real e foi executado — "E5 (ciclo real)", citado nesse
documento. Só falta a seção dele no Capítulo 5; atualizei
`docs/records/resultados.json` para registrar isso com precisão em vez de
manter a pendência genérica.
