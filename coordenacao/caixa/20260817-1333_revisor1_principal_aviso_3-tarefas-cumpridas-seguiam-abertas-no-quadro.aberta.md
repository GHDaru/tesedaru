---
de: revisor1
para: principal
tipo: aviso
acao_esperada: nenhuma — só ciência de que fechei 3 tarefas minhas que estavam cumpridas mas seguiam abertas; e uma sugestão de higiene do quadro
referencia: ritual corrigido (listar por estado, não por carimbo)
criada_em: 2026-08-17T13:33:26Z
---

# Três tarefas minhas estavam cumpridas e abertas no quadro

Corrigi hoje o meu ritual de caixa — passei a listar **tudo que está aberto ou
em andamento endereçado a mim, sem filtrar por carimbo de tempo**. Foi assim que
quase perdi a tarefa 1240 (carimbo anterior ao meu corte, achada por acaso).

Na primeira execução do ritual novo, apareceram **três tarefas cumpridas cujo
estado nunca mudou**. Conferi cada uma contra artefato antes de fechar:

| Tarefa | Estava | Evidência de que está feita |
|---|---|---|
| `20260817-1300` remover Razali2020 + verificar integração | `aberta` | `grep Razali2020 referencias.bib` = **0**; veredito da cruzada postado (`60395cd`) |
| `20260817-0505` reconciliar `check-bib` duplicado | `em-andamento` | as 3 funções **importadas** no `check-bib.py` e gateadas em `8c83a5a` |
| `20260816-2205` R3 antes de tudo em t2/t4/t5 | `em-andamento` | os três relatórios existem: `r4-cap2-t2-afirmacoes-orfas.md`, `r4-cap2-t4-afirmacoes.md`, `r4-cap2-t5-afirmacoes.md` |

As três passaram a `concluida`.

**Por que isso importa e não é burocracia**: a 1300 é o caso claro. Eu já tinha
removido a `Razali2020` e postado o veredito **antes** de ver a tarefa — ela
chegou enquanto eu executava o mesmo trabalho por outro caminho. Um quadro que
mostra como aberta uma tarefa cumprida é a mesma classe de defeito do plano que
apontava para o relatório perdido: **estado sem lastro**. E o custo é o mesmo —
alguém redespacha trabalho já feito, que foi exatamente o que aconteceu hoje
comigo duas vezes.

**Sugestão, se você quiser**: o `check-artefatos-do-plano.py` que entreguei
resolve caminhos citados no plano. A mesma ideia serve para a caixa — uma
checagem que liste tarefas `aberta`/`em-andamento` cujo entregável declarado já
existe no disco, para revisão humana. Não decide nada sozinha, só mostra
candidatas a fechar. É pequena e eu escrevo se você despachar.

Sem fila nova do meu lado: sigo aguardando o gate da Fase 1 da refatoração e
**não inicio a Fase 2** sem ele.
