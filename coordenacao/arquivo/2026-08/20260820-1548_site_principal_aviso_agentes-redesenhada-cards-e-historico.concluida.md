---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma — ciência; publicado direto (ADR 0010, site dispensa gate)
criada_em: 2026-08-20T15:48:00Z
referencia: ciclo 011 · specs/011-agentes-cards-e-historico-recolhido/ · commit 7e45e8a
---
O autor achou a página Agentes do ciclo 010 (mapa de nós/arcos) "visualmente
carregada e congestionada" e propôs duas direções sem decidir entre elas,
pedindo que 3 especialistas avaliassem. Convoquei 3 pareceres independentes
(visualização de redes/grafos, dashboards/big numbers, UX operacional) — os
três convergiram, por caminhos diferentes, em abandonar o grafo em anel como
visão principal: a topologia é 100% imposta pelo protocolo (principal
concentra 90,6% do tráfego histórico), não é um achado que pague o custo
visual.

Redesenho publicado:
- **Topo (sempre visível)**: quantas tarefas estão abertas agora, quantos
  agentes têm pendência, e um card por agente com trabalho — só quem tem
  tarefa aberta ganha card (evita o "ruído de zeros"); o `principal` ganhou
  uma faixa-resumo própria, separada dos satélites, porque não é comparável
  a eles.
- **Histórico (dentro de um "recolhido por padrão", como o arquivo da
  Coordenação)**: aqui implementei o pedido literal do autor — um arco por
  par de agente↔principal, sem seta, rótulo `[in]`/`[out]`, num leque reto
  (não anel) que não cruza nenhuma linha. A tabela de dados exatos, que já
  existia, continua abaixo.

Testado (Playwright): claro/escuro, mobile 390px, 8 páginas, 0 erros de
console reais, todos os números conferidos manualmente contra
`mensagens.json`. Decisões e os 3 pareceres resumidos em
`specs/011-agentes-cards-e-historico-recolhido/{ux-design.md,qa-report.md}`.
