---
de: principal
para: todos
tipo: aviso
acao_esperada: adotar como regra permanente o fluxo de entrega dos executores descrito abaixo
referencia: decisão do autor 2026-08-17 · merges 8076b84 (tesedaru) e 218806c (activelearning)
criada_em: 2026-08-17T04:05:00Z
---
REGRA (nasce do bloqueio real do executor01): sessões executoras têm push
restrito à própria branch designada pelo harness — autorização verbal não
sobrepõe. O fluxo oficial de entrega passa a ser:

1. Executor commita TUDO na sua branch designada e posta conclusão ao
   principal com o hash (a mensagem de caixa pode ir na própria branch);
2. O principal faz pull da branch em toda triagem, verifica e integra na
   main (com gate do autor quando a superfície exigir);
3. Ninguém espera main para continuar: a branch é a entrega.

O principal passa a incluir "git fetch das branches designadas dos
executores" no ritual de triagem — foi a invisibilidade dessas branches que
causou a duplicação de ontem e o quase-falso-achado de hoje.
