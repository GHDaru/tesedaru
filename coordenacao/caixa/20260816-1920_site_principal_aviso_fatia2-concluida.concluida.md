---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma ação obrigatória — registro de conclusão da Fatia 2; leia se quiser repassar ao autor
referencia: tesedaru branch main (1f3a04b) · tarefa 20260816-1837
criada_em: 2026-08-16T19:20:00Z
---
Fatia 2 concluída e publicada direto na main (ADR 0010), commit 1f3a04b —
depois de a Fatia 1 já estar publicada e funcionando, como instruído.

## Coordenação (mensagens.html) — virou board kanban
- 3 colunas (Aberta ○ · Em andamento ◐ · Concluída ●); Arquivadas não é
  coluna, fica recolhida abaixo do board.
- Card: título = ação esperada (não o slug) → rota "de → para" + tipo →
  idade em linguagem natural + prazo (vencido = palavra "atrasado", nunca só
  cor) → referência truncada.
- Único destaque forte: card dirigido ao autor tem borda âmbar + rótulo
  "para você" — nada mais compete (ADR 0006 preservado).
- Filtros por agente e por tipo, client-side, contadores refletindo o
  filtro ativo.
- Volume: acima de 50 cards, cada coluna limita a 20 + "+N mais" sem
  paginação — testei com 72 mensagens sintéticas antes de publicar.
- Somente-leitura explícito no cabeçalho do board; cursor padrão nos cards;
  sem draggable — arrastar não faz nada.
- Locks + linha de saúde da coordenação abaixo do board.

## Resultados (resultados.html) — conteúdo real, não mais stub
- docs/records/resultados.json criado com schema documentado no topo
  (achados/entregas/experimentos/convenção de evidência) e os exemplos
  reais pedidos:
  - P3 — platô de 77–83% de acurácia entre oráculos LLM, US$0,035–0,92/mil
    rótulos, conferido contra 5-resultados-falco/texto.tex (Tabela
    tab:e0-custo) antes de escrever;
  - P4 — veredito de paridade a 30% do orçamento refutado, McNemar p=0,10 e
    IC bootstrap [0,002;0,018], conferido contra
    experiments/e2e3/results/mcnemar_s42.json e bootstrap_f1_s42.json (já
    citados em docs/records/plano-revisao.json).
- Achado (afirmação + número + evidência, por pilar P1–P4) e Entrega (nome +
  descrição + link) são cartões visualmente diferentes, como pedido. P1/P2
  aparecem honestamente vazios — não escondidos, não inventados.
- Tabela de experimentos executados (E0, E0-P, E1, E4, E6, E3′) com dados
  conferidos contra o texto do Capítulo 5. Um detalhe que vale seu
  conhecimento: **não encontrei E5 como seção própria no Cap. 5** — o
  capítulo tem E0, E0-P, E1, E4, E6, E3′, mas nenhum E5;
  docs/inventario-prontidao-2026-08-16.md cita o intervalo "E0–E6/E3′" de
  forma agregada, sem seção E5 individual. Registrei isso explicitamente na
  página e no JSON como pendente de confirmação, em vez de inventar um
  resultado. Se E5 for um experimento real que falta escrever, ou um erro
  de numeração, quem souber pode corrigir direto no JSON.

## Evidência
Testado no Chromium (Playwright) local antes E depois do deploy: 0 erros de
console nas 4 páginas, filtro do kanban recalcula contagem em tempo real,
tema claro/escuro corretos, mobile empilha o board numa coluna. Confirmado
ao vivo após o deploy do GitHub Actions (run 31967080084, sucesso):
- https://ghdaru.github.io/tesedaru/mensagens.html (board kanban)
- https://ghdaru.github.io/tesedaru/resultados.html (achados/entregas/experimentos)
- https://ghdaru.github.io/tesedaru/resultados.json servindo os 2 achados

## Estado
As duas fatias da tarefa de redesenho estão completas e publicadas. Sigo
disponível na superfície do site para o que vier a seguir (por exemplo, se
alguém confirmar o que é E5, ou quando houver mais achados/entregas para
adicionar a resultados.json).
