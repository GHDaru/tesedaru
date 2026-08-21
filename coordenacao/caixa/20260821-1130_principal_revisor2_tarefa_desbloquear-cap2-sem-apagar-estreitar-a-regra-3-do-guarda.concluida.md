---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: o AUTOR AUTORIZOU a sua saída 2 (aviso 0440): estreitar a regra 3 do guarda para destravar o Cap.2 SEM apagar as branches humanize/cap2-*. Implementar, estender o testa-guarda.sh com casos positivo e negativo, entregar em branch para gate.
referencia: pergunta do autor 2026-08-21 ("não dá para desbloquear sem deletar as branches?") · seu aviso 20260821-0440 · merge do harness 904c7ca
criada_em: 2026-08-21T11:30:00Z
---

Resposta do autor à sua alternativa: ele prefere desbloquear sem deletar.
Autorização dada — a escolha de MECANISMO é sua, com duas balizas:

1. Nada de heurística cara ou frágil dentro do hook (comparar diff completo a
   cada chamada de ferramenta, não). Sugestão aceitável: uma lista versionada
   de branches DECLARADAS SUPERADAS pelo autor (com o SHA da ponta registrado
   para restauração), que a regra 3 passa a ignorar. Entrar na lista exige
   decisão do autor — a de hoje já cobre humanize/cap2-t2 @2438c68 e
   humanize/cap2-t3 @dc7247e (resgate do que valia já feito por você em
   5218ccd).
2. O guarda continua falhando em aberto e o DoD continua sendo o
   testa-guarda.sh em exit 0, agora com pelo menos: (a) branch na lista →
   edição PERMITIDA; (b) branch fora da lista → edição BLOQUEADA como hoje.

Quem confere a entrega: revisor1 ou banca (§6 — você escreveu o harness e
esta mudança). Se o autor um dia apagar as duas branches, a lista esvazia e
nada quebra.
