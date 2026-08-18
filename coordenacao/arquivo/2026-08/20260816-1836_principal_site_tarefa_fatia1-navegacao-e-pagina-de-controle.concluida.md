---
de: principal
para: site
tipo: tarefa
acao_esperada: implementar a Fatia 1 (estrutura de navegação, sidebar e página de Controle) e publicar; avisar o principal ao concluir
referencia: docs/handoff-site.md · ADR 0006 (decisões de UX vinculantes) · sem gate (ADR 0010)
criada_em: 2026-08-16T18:36:37Z
---
FATIA 1 de 2 — estrutura, navegação e a página de Controle.
(A Fatia 2, com o kanban e a página de Resultados, chega em mensagem separada;
não a implemente agora — entregue e publique a Fatia 1 primeiro.)

Contexto: o autor não consegue usar o painel atual porque tudo está empilhado
numa página só. O problema a resolver é FOCO, não estética.

## 1. Arquitetura de informação — 4 páginas

| Arquivo | Nome no menu | A pergunta que responde |
|---|---|---|
| index.html | Controle | "O que preciso decidir agora?" (HOME) |
| plano.html | Plano | "Onde está o trabalho e quanto falta?" |
| mensagens.html | Coordenação | "O que os agentes estão fazendo?" |
| resultados.html | Resultados | "O que a tese já produziu?" |

A home é Controle, não o plano: o autor abre o site para decidir, não para
admirar progresso. Quem quer o detalhe navega.

Distribuição do conteúdo que hoje está empilhado:
- Controle: hero de prontidão + fila "Aguardando você" (gates, decisões,
  mensagens dirigidas a ele, processo doente) + próximo passo do agente +
  atalhos para as outras três páginas com um número cada
  ("Plano · 3,5%", "Coordenação · N ativas", "Resultados · N entregas").
- Plano: os 6 KPIs, burn-up, matriz 8x7 + glossário das rodadas, aberturas por
  capítulo, execuções, artefatos e pendências.
- Coordenação: kanban (Fatia 2) + locks + linha de saúde.
- Resultados: Fatia 2.

## 2. Sidebar

- Expandida 220px, recolhida 60px; botão de recolher no topo; estado
  persistido em localStorage (chave `falco.sidebar`).
- Expandida: glifo + rótulo. Recolhida: só o glifo, com `title` e
  `aria-label` (sem biblioteca de ícones — use glifos unicode simples ou SVG
  inline: por exemplo ◎ Controle, ▤ Plano, ✉ Coordenação, ★ Resultados).
- Página ativa: fundo levemente destacado + barra de 3px na borda esquerda +
  `aria-current="page"`.
- Abaixo do menu, um rodapé discreto: "atualizado em <data> · plano v<N>".
- Mobile (<768px): sidebar vira barra superior com botão que abre um painel
  deslizante; nunca sobrepõe conteúdo sem permitir fechar.
- A sidebar é gerada por UMA função compartilhada no gerador, não copiada em
  cada template (evita divergência).

## 3. Sistema visual (mantenha os tokens atuais e formalize)

- Paleta clara: fundo #FAFAF8 · cartão #FFFFFF · tinta #20261F · secundária
  #68705F · acento (verde UFPR) #1E6B3C · atenção (âmbar) #8A5A00 sobre
  #FBF1DC · borda #E2E5DF.
- Escura: fundo #131714 · cartão #1B211C · tinta #E6EAE4 · secundária #9AA294 ·
  acento #6FC492 · atenção #E8BE6A sobre #33290F · borda #2A302B.
- Três estados de tema obrigatórios (ver docs/handoff-site.md §4).
- Tipografia: fontes de sistema; títulos em Georgia/serif; escala 12/13/15/
  20/28/44px; números sempre com `font-variant-numeric: tabular-nums`.
- Espaçamento em múltiplos de 4px; largura máxima de conteúdo 1080px.
- Componentes reutilizáveis (um CSS só, compartilhado pelas 4 páginas):
  cartão, pílula de estado, item de lista com dono, tabela com rolagem
  horizontal própria, barra de progresso, tile de KPI.

## 4. Regras de design vinculantes (ADR 0006 — não revogue)

- UM único grito visual na interface, e ele pertence ao autor: a fila
  "Aguardando você" em âmbar. Telemetria de agente jamais compete com ela.
- Estado nunca só por cor: glifo + palavra (✓ feito · 🔒 em gate · ◐ andamento
  · ○ pendente · – n/a · ⛓ bloqueado).
- Nada que espere o autor pode nascer dentro de um bloco recolhido.
- Burn-up: eixo Y fixo de 0 a 100%, eixo X em datas reais.

## 5. Definição de pronto

Quatro páginas geradas pelo mesmo script, navegação funcionando entre elas,
sidebar recolhendo e lembrando o estado, temas claro/escuro corretos nos três
estados, sem erro de console, publicado no Pages. Ao concluir, poste conclusão
ao principal com hash e URLs.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
