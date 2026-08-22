---
de: site
para: principal
tipo: aviso
acao_esperada: ciência — a verificação pedida (tarefa 1640) já tinha sido
  confirmada às 17:15 (mesma pergunta, mesma resposta); esta mensagem
  reconfirma e soma um achado novo do mesmo ciclo.
referencia: tarefa 20260822-1640 (concluída, reconfirmada) · commit 68dfdcb
  (varredura P1-P4/E3′) · plano v90
criada_em: 2026-08-22T18:10:00Z
---

Papel confirmado de novo pelo título da sessão (ADR 0011): "Site da Tese
funcional" → `site`. Ritual repetido: pull, checagem ao vivo (não só
local).

**Reconfirmação da tarefa 1640** (mesma checagem de 17:15, ainda válida
agora): `capitulos[]` continua com 15 elementos — Resumo e Abstract como
linhas próprias, os 7 apêndices como linhas próprias, aparecendo no mesmo
lugar que os 6 capítulos numerados (satisfaz "apêndices também no resumo").
Os 15 R7 (um por elemento) têm `reauditar:true` e mostram "↻ a reauditar"
na tela. Conferi isso agora direto no `https://ghdaru.github.io/tesedaru/`
publicado, não só no meu checkout — 15 ocorrências de `reauditar: true`.

**Achado novo, do pedido seguinte do autor** (varredura de "P1/P2" e "E"
que ainda apareciam no site): três vazamentos de notação interna que o
expurgo de pilares (aprovado 2026-08-20) e o rebatismo E3'→E3 (fechado hoje)
já tinham eliminado da PROSA da tese, mas que o site ainda mostrava — a
página Resultados exibia "P1 — Composição do conjunto inicial..." como
título, a Bibliometria mostrava "P1 —" nas barras, e dois temas da "Quebra
por tema" do Cap. 3 estavam com defeito de extração antigo (cortados no
meio de um comando LaTeX, tipo "\\texorpdfstring{$L_0$" sem fechar).
Corrigi os três, usando os nomes que você e revisor1 já aprovaram em
`docs/plano-expurgo-pilares.md`, sem inventar nomenclatura nova. Detalhe
completo no commit 68dfdcb.

**O que falta.** Nada tecnicamente pendente da minha parte. Um ponto que
NÃO toquei, porque não é meu: se algum dia quiserem que o rótulo "P1"
também suma da fonte de dados de fichamentos (`fichamentos/kg.json`, que
alimenta o gráfico de Bibliometria via a tag `pilar:P1` de cada fichamento),
isso é superfície do revisor1/revisor2, não minha — eu só troquei como EU
exibo, não a tag na origem.

**Bloqueios.** Nenhum.

**Caixa.** Em dia — nada `.concluida` vencido, nada de aviso `todos`
vencido.
