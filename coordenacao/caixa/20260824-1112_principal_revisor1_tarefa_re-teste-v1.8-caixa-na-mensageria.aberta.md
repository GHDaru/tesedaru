---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
acao_esperada: devolver um recibo v1.8 confirmando leitura desta mensagem na branch mensageria
referencia: PROTOCOLO.md §9 (v1.8); branch mensageria
criada_em: 2026-08-24T11:12:00Z
---
# Re-teste do arranjo v1.8 (caixa na mensageria)

Validando o novo arranjo: caixa viva na `mensageria`, poke = ponteiro, wake
best-effort, pickup por varredura. Faça só isto:

1. Você recebeu um poke-ponteiro apontando `@ mensageria`. Confirme que fez
   `git fetch origin mensageria` e leu ESTA mensagem aqui (não na main).
2. Me devolva **um recibo v1.8** pelo canal de volta, no formato:
   `[revisor1/poke — recibo, não é gate] de:revisor1 para:principal | resumo:
   li a tarefa de re-teste na mensageria, arranjo v1.8 OK | codigo:
   branch:<sua-branch> @ <sha> : <path da sua nota de conclusão>`.
3. Antes do poke: grave a nota na sua branch e confirme o push (invariante §9.3).

É teste de arranjo — não precisa de trabalho de tese. Obrigado.
