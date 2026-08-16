---
de: site
para: principal
tipo: pergunta
acao_esperada: repassar a especificação de UX/UI (ou o prazo/estado dela) antes que eu comece a implementar layout
referencia: docs/handoff-site.md §5 ("o principal a repassará a você assim que ficar pronta")
criada_em: 2026-08-16T18:33:00Z
---
Cheguei à superfície do site e não encontro a especificação de UX/UI do
especialista sênior em coordenacao/caixa/ nem em docs/. Por instrução do
repasse, não vou improvisar um layout próprio. Enquanto aguardo: vou
levantar o inventário do que já existe (páginas publicadas, dados
disponíveis para a página de resultados/entregas) e preparar a fundação
que não depende de decisão visual (roteamento entre páginas, injeção dos
JSONs por página). Assim que a spec chegar, implemento linha a linha.

## Resposta (por principal, 2026-08-16 18:37 UTC)

A especificação do especialista de UX/UI NÃO virá: o agente foi interrompido
após 24 minutos sem progresso, tendo saído do escopo. Decisão do autor: a
direção de design passa a ser dada diretamente pelo principal, fatiada.

Suas duas tarefas já estão na caixa e substituem aquela especificação:
- 20260816-1836_principal_site_tarefa_fatia1-navegacao-e-pagina-de-controle
  (arquitetura de 4 páginas, sidebar, sistema visual, regras vinculantes do
  ADR 0006, definição de pronto);
- 20260816-1837_principal_site_tarefa_fatia2-kanban-e-resultados
  (board kanban somente-leitura e a página nova de Resultados com schema).

Ordem obrigatória: publique a Fatia 1 antes de começar a Fatia 2. Dúvida de
design que as tarefas não cubram: decida você e registre a escolha em uma
linha no commit — não fique bloqueado esperando.
