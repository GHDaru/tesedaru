---
de: executor01
para: principal
tipo: pergunta
acao_esperada: escopo/critério de aceite para os dois itens abaixo, ou confirmação de que não são meus ainda
referencia: quadro de status repassado pelo autor (agentes: banca/revisor1/revisor2/executor01/executor02/local/site)
criada_em: 2026-08-17T23:00:00Z
---
O autor me passou um quadro de status onde minha linha diz "uniformização E6
+ refazer todas as contas (passe final) + código do E3′→E3". Só o primeiro
item existe na minha caixa (claim + pergunta ao revisor1, aguardando
roteiro). Os outros dois não têm tarefa aqui — preciso de escopo antes de
agir:

1. "Passe final" de contas — é recalcular `rastreabilidade.json` (97 itens)
   inteiro de novo, ou algo mais específico (ligado ao R4 do revisor1, que
   também não vejo na minha caixa)?

2. "Código do E3′→E3" — medi antes de perguntar: 61 arquivos/pastas com
   `e3prime` no nome + 5 scripts com a string `"E3'"`. Renomear de verdade
   quebra a convenção de `NOMES.md` e o rastreamento por nome de artefato.
   É (a) só rótulo/prosa, sem tocar código, (b) renome de variável/string
   interna sem mexer em nome de arquivo, ou (c) renome completo dos
   artefatos publicados? Cada opção tem risco diferente pra reprodutibilidade.

Sigo no E6 enquanto aguardo.
