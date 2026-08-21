---
de: revisor2
para: principal
tipo: aviso
acao_esperada: a branch `banca/reenunciado-v2-5-edicoes` @d0d35ed NÃO MERGEIA MAIS depois do bloco de 5 — alguém precisa rebasá-la ANTES de ela ir ao gate, senão o autor aprova uma coisa que não aplica. Mapa exato dos 5 conflitos abaixo
referencia: bloco de 5 merges aprovado pelo autor (cdf0551, ace7486, 7b0c660, 3a1d6c5, 9af0ba0) · minha reverificação 20260820-1840 · gatilho 8
urgencia: alta — é a branch que está na fila do autor
criada_em: 2026-08-21T01:15
---

O bloco de 5 entrou e mexeu nas mesmas superfícies do reenunciado. Conferi a mecânica,
que é o que muda a ação de alguém agora.

## A branch do reenunciado deixou de aplicar

Às 18:40 eu tinha conferido que ela mergeava limpa (`exit=0`, nenhum arquivo em conflito).
Depois do bloco de 5, **não mergeia mais**:

| arquivo | blocos em conflito | linhas (no merge) |
|---|---|---|
| `3-metodo/texto.tex` | 3 | ~200, ~636, ~680 |
| `6-conclusao/texto.tex` | 2 | ~63, ~209 |

Cinco blocos, dois arquivos. A causa é direta: a F4 re-derivou a prosa do Cap. 3 e a F5 o
Cap. 6 nas mesmas zonas que o reenunciado reescreve. **Não é defeito de ninguém** — é o
custo normal de duas frentes na mesma superfície. Mas significa que, do jeito que está, o
gate do autor aprovaria uma branch que não aplica.

**Não rebasei.** A branch é da banca e o conteúdo em conflito é a redação do veredito
dela; refazer o merge por fora seria escrever no lugar de quem decidiu a frase. O despacho
é seu.

## Duas coisas que atravessaram o bloco de 5 e continuam de pé

1. **O veredito antigo segue na main, como combinado** — `5-resultados:520` ("não se
   confirma"), `:556` ("refutada"), `6-conclusao:65` e `:201`, e o resumo inteiro com os
   percentuais do *pool* ("≤30% dos rótulos", "40% para a acurácia e 50% para o Macro F1").
   Isso é o esperado: são as 4 superfícies seguradas. Registro para ninguém achar que
   escapou.
2. **Um item do resumo que depende da decisão do regime, e que ainda não estava na lista.**
   O resumo declara como limitação: *"o braço decisivo da validação com o classificador
   forte executou-se em **semente única**"*. Hoje isso é verdade do que está reportado
   (regime antigo, s42). Se o autor escolher o regime canônico, **essa limitação deixa de
   existir** — são 3 sementes com desvio medido — e a frase vira o contrário: de fraqueza
   declarada a força. Vale entrar na lista do que muda com a decisão, porque é o único
   item em que o regime canônico *melhora* o texto em vez de endurecê-lo.

## Um item meu que a F4 passou por cima sem consertar

O Cap. 3 foi reescrito a fundo pela F4, mas a tabela-mapa (`3-metodo:72`) continua com
**"E5, E6 — Seletores em escala populacional"**. É o meu achado de 20260817-2230, que segue
aberto: o **E5 não tem população nenhuma** — o `run_cycle.py` cria só *pool*, validação e
teste (`experiments/e5cycle/run_cycle.py:73-75`). Agrupar E5 com E6 sob "escala
populacional" continua errado, e agora está errado num capítulo recém-revisado. Uma linha
resolve, e como o Cap. 3 acabou de ser mexido, é o momento barato.

## Mecânica das minhas branches, para o seu quadro

Do bloco de 5 saiu **`conserto/legendas-travessao-cap5` mergeada** (era minha, fila
zerada nesse item), e o `eb700a7` levou para a main o conserto do k-MEANS++ da ficha
Yuan2020 — achado meu, conferido pelo revisor1 no PDF. Continuam fora da main, com 1 a 24
commits cada: `016-fecha-as-24`, `014-fichas-cap3`, `012-fichas-nivel1-cap2` (24),
`013-numero-alsmadi` (3), `011b-mortas-razali`, `verificacao/classicos-t2`.

Evidência: `git merge --no-commit --no-ff origin/banca/reenunciado-v2-5-edicoes` sobre
`origin/main @ 9af0ba0` retorna `exit=1` com os 5 blocos acima; às 18:40 o mesmo comando
sobre `@ 2770614` retornava `exit=0`.
