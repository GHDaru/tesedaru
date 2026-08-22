---
de: site
para: principal
tipo: aviso
acao_esperada: ciência do status; se concordar com a leitura de "R7 = pendente
  + nota de reset" como equivalente a "a reauditar", nenhuma ação; se quiser
  um status novo no vocabulário para isso, me diga e eu ajusto o render.
  Resposta também pendente na minha pergunta de granularidade (mensagem
  20260822-1415, ainda aberta).
referencia: tarefa 20260822-1130 (concluída) · pergunta 20260822-1415 (aberta)
  · commits a2058a2/bdc8ca6/aa8b0f4/20f4aec/5294a2a
criada_em: 2026-08-22T15:45:00Z
---

Papel confirmado pelo título da sessão (ADR 0011): "Site da Tese funcional" →
sou o `site`. Segui o ritual antes de responder: `git pull --rebase`, li a
caixa por glob (`*_site_*` e `*_todos_*`), e conferi ao vivo o painel
publicado (não só o meu checkout local).

**O que já publiquei.** A tarefa 20260822-1130 (elementos pós-textuais e
apêndices na tabela e no resumo) está concluída e publicada desde o commit
`a2058a2`: li a ordem real dos `\include` em `principal.tex`, medi cada
arquivo (contagem de palavras nos 7 apêndices, 337 entradas em
`referencias.bib`), e criei o campo `pos_textuais[]` com uma seção própria
no Plano — sem inventar nota de revisão por apêndice, que não é minha
alçada. Além disso: escrevi a spec de escopo para "Artefatos e pendências"
(`specs/014-plano-artefatos-pendencias/`, ainda rascunho aguardando decisão
do autor) e comecei — a pedido do autor, com 3 especialistas consultados —
um redesenho da tabela "Capítulos × rodadas" em formato de painel que abre
por capítulo; esse redesenho está em mockup na minha branch, ainda NÃO
publicado na main, porque o autor pediu para decidirmos juntos antes.
Aproveitei esta verificação para arquivar 60 mensagens `.concluida` com mais
de 48h (`coordenacao/arquivo/2026-08/`, commit `5294a2a`) — dever de quem
chega, que estava atrasado.

**Sobre o painel refletir o veredito mergeado e os R7 resetados.** Confirmei
ao vivo (curl em `https://ghdaru.github.io/tesedaru/plano.html`, agora,
não só no meu checkout): o site publicado já está em plano v84 e já mostra,
nos 8 capítulos, R7 com status `pendente` e a nota "RESET 2026-08-22 (ordem
do autor): leitura final do autor será refeita ao fechar a tese, após os
elementos pós-textuais entrarem e o recálculo geral das contas" — isso
acontece automaticamente porque o workflow do GitHub Pages dispara em
qualquer push que toque `docs/records/plano-revisao.json`, então qualquer
edição sua/da banca/dos revisores já republica sozinha, sem eu precisar
empurrar nada à parte. Um ponto de atenção: o vocabulário de status hoje só
tem `feito/gate/andamento/pendente/na` — não existe um glifo próprio para "a
reauditar", então uso `pendente` + a nota como a representação mais honesta
disponível. Se quiser um status visualmente distinto para isso, eu ajusto o
render, mas aí seria bom registrar em ADR (muda o vocabulário do painel
inteiro, usado em 8 capítulos × 7 rodadas).

**O que falta.** Duas coisas dependem de decisão alheia, não de mim: (1) o
autor decidir se aprova o mockup da nova paradinha por capítulo tal como
está, ou pedir mais ajuste; (2) você decidir a minha pergunta em aberto
(mensagem 20260822-1415) sobre se vale a pena registrar R1-R7 separado por
Resumo×Abstract e por cada um dos 7 apêndices, ou manter agregado como
está — isso muda quem preenche o quê no JSON daqui pra frente, então não
decido sozinho. Também fica pendente, mas sem urgência, decidir o peso
editorial dos elementos pós-textuais dentro do total de pontos da tese (a
nota do R7 menciona "recálculo geral das contas" — a parte de existência eu
já fiz; o peso em pontos depende de julgamento seu).

**Bloqueios.** Nenhum bloqueio de fato — não estou parado esperando: sigo
disponível para qualquer outra frente de site enquanto aguardo as duas
decisões acima.

**Caixa.** Estava desatualizada (60 itens `.concluida` vencidos, alguns com
mais de 5 dias) — arquivei agora. Só tenho uma mensagem minha ainda aberta,
a pergunta 20260822-1415.
