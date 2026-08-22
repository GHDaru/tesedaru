---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: INVESTIGAR (não corrigir ainda) as 2 divergências da R4 do Cap.3 que exigem decisão, medir contra os artefatos e propor a saída ao principal. É diagnóstico com evidência, no seu estilo. Depois das suas 2 cruzadas em curso (axb + rebatismo).
referencia: R4 do revisor1 20260822-1345 (itens 2 e 3) · 5-resultados:281-290 · Apêndice A7 · 3-metodo (afirmação da Fase 2)
criada_em: 2026-08-22T17:00:00Z
---

Duas divergências que o revisor1 declarou na R4 e não corrigiu:

**(2) Fase 2 usa entropia, mas o E1 elege menor margem/menor confiança.**
O Cap.3 afirma que a Fase 2 seleciona por entropia; o E1 (5-resultados:281-290)
mede as estratégias e o vencedor não é a entropia. Investigue: qual estratégia
o framework REALMENTE executou (olhe o artefato/código do ciclo real, E5)? Três
saídas possíveis, diga qual os dados sustentam: (a) o método usou entropia e o
texto deve explicar por que a manteve apesar do E1; (b) usou o vencedor do E1 e
o Cap.3 está com a palavra errada; (c) as duas medem coisas diferentes
(ranking global x por lote) e falta essa distinção no texto. Traga a evidência.

**(3) epsilon = 1e-3 x 1/sqrt(nV) = 0,0224 (fator ~22).**
Há uma tolerância de parada citada como 1e-3 num lugar e o A7 a justifica pelo
limite 1/sqrt(n_V) que, com n_V=2.000, dá 0,0224. Investigue: são a MESMA
constante com valores incompatíveis, ou duas coisas distintas (uma tolerância
de convergência x um piso de significância) que o texto confunde? Meça de onde
cada número vem no código/artefato e proponha a redação que reconcilia — ou,
se forem a mesma e uma estiver errada, qual é a certa.

NÃO edite texto: entregue o diagnóstico + proposta ao principal, que leva ao
autor. A (2) toca o argumento central da seleção ativa, então diagnostique
antes de qualquer conserto.
