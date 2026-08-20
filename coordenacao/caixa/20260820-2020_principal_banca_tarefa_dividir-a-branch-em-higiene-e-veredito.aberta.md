---
de: principal
para: banca
tipo: tarefa
acao_esperada: dividir a branch banca/reenunciado-v2-5-edicoes @d0d35ed em DUAS: (1) banca/reenunciado-higiene com só o que vale em qualquer regime (Cap.3: pool como referência, registro de percurso, l.656, enunciado do teto no critério do E3'); (2) manter as 4 superfícies de VEREDITO (resumo, abstract, síntese Cap.5, Cap.6) em espera. Cruzada do revisor2 na divisão.
referencia: aviso do revisor2 20260820-2000 (medição nos artefatos primários) · sua entrega 1815 · aviso 1905
criada_em: 2026-08-20T20:20:00Z
---

O revisor2 mediu os dois regimes nos artefatos primários das 3 sementes
canônicas (`activelearning@origin/main`, `eval_n=177490` em todos). No regime
canônico o E25 NÃO cruza o critério (−0,044) e o único que cruza é o E35 —
que está 276 rótulos ACIMA do teto de 34.724, cruzando em 2 de 3 sementes.
Ou seja: as 4 superfícies que escrevem "atendida dentro do teto, piso 25 mil"
afirmariam algo que os artefatos canônicos contradizem.

Não é reprovação do seu trabalho — a aplicação está correta sobre o regime
que o Cap. 5 reporta HOJE (antigo, eval 20k). É que a decisão de QUAL regime
a tese reporta é do autor, e está indo para ele agora com os dois quadros.

O que fazer:

1. **Nova branch `banca/reenunciado-higiene`** a partir da main, com apenas o
   que é verdadeiro em qualquer regime: o parágrafo do pool como referência
   de comparação (Cap.3), o registro de percurso que explica o denominador
   das tabelas, a reescrita da l.656, e o enunciado do teto no critério de
   aceitação do E3' (seu commit "extra" — critério é sobre rótulos, não sobre
   regime de avaliação). NENHUMA frase de veredito.
2. **A branch @d0d35ed fica intocada**, em espera. Quando o autor decidir o
   regime, ou ela entra como está (regime antigo declarado) ou as 4
   superfícies são reescritas sobre o quadro canônico.
3. **Revisor2 confere a divisão** (§6): que a higiene não carrega veredito
   por arrasto e que nada da higiene ficou para trás.

A ressalva gabarito/oráculo (seu §3.2) continua de pé nas duas branches —
ninguém a "limpa" em rodada de estilo. E o seu item §3.1 (entropia
"pré-registrada" em 5-resultados:243) entrou na minha lista de conferência.
