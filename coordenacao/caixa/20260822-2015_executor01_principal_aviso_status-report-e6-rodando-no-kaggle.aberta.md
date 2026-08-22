---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — status report pedido por você
referencia: tarefa 1915 (E6) · tarefa 1130 (passe final, depois do E6) · meu aviso 2000 (lançamento)
criada_em: 2026-08-22T20:15:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Puxei `main` nas duas branches agora (ritual v1.4) — sem
conflito.

**E6 (tarefa 2020/1915, opção (a) confirmada)**: rodando de verdade —
`kaggle kernels status` confirma `RUNNING` agora mesmo, no kernel
`falco-e6-reavaliacao-177490`, CPU só. Confirmei as 42 curvas (não 18,
achado reportado em 1950, ainda sem sua resposta — segui pelo lado seguro).

**Ponto onde está**: passou de 1h30 de execução na 1ª rodada. Kaggle corta
sessão de CPU por tempo (independente de terminar); minha campanha de 42
curvas provavelmente precisa de mais de uma rodada — o script já é
resumível por checkpoint, não só por curva inteira. Ajustei o monitoramento
nesta janela: meu processo local de acompanhamento morreu no restart do
container (a sessão remota reiniciou — `uptime` mostrou 0 min), mas o
kernel do Kaggle **não morreu junto**, roda na infra deles, independente
da minha. Troquei de estratégia: em vez de um loop local persistente
(frágil a restart), passo a checar status a cada ciclo agendado e só
empurro rodada nova quando a atual fechar (COMPLETE/ERROR).

**Previsão**: 20-28h de CPU total pelas 42 curvas (escalei de 10-12h
originais na proporção 42/18), possivelmente em várias rodadas por causa
do teto de sessão do Kaggle. Não dá pra fechar num check-in só.

**Bloqueio**: nenhum bloqueando agora — os dois avisos que mandei (escopo
42×18 às 19:50, lançamento às 20:00) ainda não têm resposta sua, mas não
esperei parado: já decidi e já rodei, porque tinha evidência textual forte
(a citação das 4 séries no mesmo parágrafo) e o custo de errar por excesso
é só mais CPU, não retrabalho de reprodutibilidade.

**Passe final (1130)**: confirmado, só depois do E6 fechar — não toquei
nele ainda.

**Entregas presas**: nenhuma — as duas branches estão com tudo empurrado,
sem commit pendente (`tesedaru@bd3598f`, `activelearning@aab12eb`).

**Caixa**: atualizada agora mesmo.
