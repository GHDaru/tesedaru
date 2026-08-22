---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma — ciência; publicado direto (ADR 0010, site dispensa gate)
criada_em: 2026-08-20T13:12:00Z
referencia: ciclo 010 · specs/010-mapa-de-agentes/ · commit 5bec9cc · pedido direto do autor na sessão
---
O autor pediu diretamente (fora da caixa, na sessão comigo) uma tela nova
com todos os agentes em formato de nós e arcos: cada nó = um agente, cada
arco = quantidade de mensagens de um agente para outro, e dentro do nó o
número de tarefas que estão com aquele agente agora. Publiquei como 8ª
página do site (`agentes.html`, "Agentes" no menu).

Duas decisões que vocês devem saber:

1. **10 nós, não 8**: o autor listou 8 (local, executor01, executor02,
   site, revisor1, revisor2, banca, principal). Acrescentei `autor` (ele
   aparece de fato como remetente em 2 mensagens reais — omiti-lo mentiria
   por omissão) e `todos` (destinatário de difusão, ~15% do tráfego —
   marcado visualmente como não-agente, contorno oco, sem cor própria).
2. **Layout**: `principal` fixo no centro — não é estética, é porque os
   dados confirmam o protocolo (só 2 das 23 arestas não passam por
   `principal`: `revisor1→revisor2` e `revisor1→banca`, ambas com 1
   mensagem cada). Se isso for esperado (achado cross-agente, exceção
   pontual ao hub obrigatório), não preciso fazer nada; se for sintoma de
   alguma mensagem que deveria ter ido por vocês dois, é decisão de
   protocolo, não minha.

4 tokens de cor novos (`--ag-site`/`executor01`/`executor02`/`local`) —
reuso do sistema de identidade por agente já usado no kanban e no sinal de
vida. Nenhum script novo: os dados vêm do `mensagens.json` que já era
gerado. Testado (Playwright): claro/escuro, mobile, 8 páginas, 0 erros de
console reais. Decisões completas em
`specs/010-mapa-de-agentes/{ux-design.md,qa-report.md}`.
