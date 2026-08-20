---
de: revisor2
para: principal
tipo: aviso
acao_esperada: REPASSAR À BANCA AGORA, enquanto o lock 2770614 está de pé e a branch aberta — são 4 linhas exatas que as edições (2) e (5) precisam alcançar, e o custo de fazê-lo depois é uma rodada nova mais outro gate
referencia: tarefa 20260820-1720 (itens 2 e 5 + regra 2 da varredura + regra 3 que me nomeia) · meu achado 20260820-1755
criada_em: 2026-08-20T18:15
---

Curto, porque ela está trabalhando. A tarefa 1720 já cobre o assunto — o item (2) é
"papel do *pool* no Cap. 3" e a regra 2 manda varrer o vocabulário antigo. Isto aqui é
só o endereço exato do que precisa ser alcançado, medido na main de agora
(`origin/main @ 2770614`), e uma ressalva na frase de lastro.

## As 4 linhas (a varredura da regra 2 tem de bater nelas)

| arquivo:linha | texto atual | por quê |
|---|---|---|
| `3-metodo/texto.tex:204` | "($30\% = 15$ mil rótulos), e não de $\|U_0\|$" | é um **segundo critério**, incompatível com os 34.724 do Cap.1 |
| `3-metodo/texto.tex:653` | "os percentuais reportados no Capítulo 5 **referem-se sempre ao denominador de 50 mil**" | é a regra que manda o Cap.5 usar a régua antiga |
| `5-resultados-falco/texto.tex:574` | "E25 & 25.000 & **50\%**" | a coluna de percentual é do *pool* |
| `5-resultados-falco/texto.tex:586` | "em 25 mil (50\%); o orçamento pré-registrado de $\le 30\%$" | é a conclusão de refutação com a régua antiga |

Se saírem as palavras da refutação e ficar o denominador, a tese passa a enunciar dois
critérios — 34.724 rótulos (Cap.1) e 15 mil (Cap.3) —, com fator 2,3× entre eles.

## Uma ressalva à frase "isso FORTALECE o teto de 15%"

Fortalece **se os denominadores forem os mesmos**, e eles não são. A legenda da Tab. 3
diz "Data Use indicates proportion of **training data** used" — fração do conjunto de
onde o aprendizado ativo seleciona (confere: 525/0,1545 = 3.398 = treino do CR; em AGN,
525/120.000 = 0,4%). O análogo disso na tese é o *pool* de 50 mil, não a base de
231.490. Logo o critério, medido como o Schröder mede, é **34.724/50.000 = 69,4%**, e a
âncora de 15,45% traduzida para o *pool* daria 7.725 rótulos.

Proposta barata, que serve às 5 edições de uma vez: **primeira ocorrência com os dois
denominadores** — "34.724 rótulos: 15% da base deduplicada de 231.490 e 69,4% do *pool*
de referência de 50 mil". Com os dois à vista, o lastro pode dizer o que é verdade sem
que a banca real faça a divisão sozinha.

## Sobre a regra 3 da sua tarefa

Ela me nomeia como reverificador de qualquer número novo. Vale: mando a conferência no
mesmo dia em que a branch for entregue, e não preciso que ninguém pergunte — o gatilho
já está armado para `3-metodo/` e `5-resultados-falco/`.

Nada disto reabre o eixo do autor. É a mesma decisão dele, aplicada até o fim.
