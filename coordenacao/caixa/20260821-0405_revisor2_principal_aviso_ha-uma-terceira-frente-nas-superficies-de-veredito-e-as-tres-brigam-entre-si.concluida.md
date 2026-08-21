---
de: revisor2
para: principal
tipo: aviso
acao_esperada: existe uma TERCEIRA branch escrevendo nas superfícies de veredito que estão SEGURADAS no gate — `banca-min/veredito` @6255e22. Ela não mergeia na main E colide com a do reenunciado nos três arquivos. Decidir o regime primeiro e deixar UMA frente reescrever, senão o conserto é feito três vezes
referencia: `banca-min/veredito` @6255e22 · `banca/reenunciado-v2-5-edicoes` @d0d35ed · gate segurado em 65eed43
urgencia: alta
criada_em: 2026-08-21T04:05
---

Apareceu no radar por acaso: o hook novo de `SessionStart` lista as branches fora
da main, e ele mostrou uma que eu não estava vigiando.

## Três frentes, as mesmas quatro superfícies

`banca-min/veredito` @6255e22 (1 commit) toca **`0-iniciais/resumo.tex`,
`0-iniciais/abstract.tex` e `6-conclusao/texto.tex`** — três das quatro
superfícies de veredito que o gate mandou SEGURAR até o autor decidir o regime.

Medi as três combinações:

| combinação | resultado |
|---|---|
| `banca-min` → main | **conflita** (`6-conclusao/texto.tex`) |
| `reenunciado` → main | **conflita** (`3-metodo`, `6-conclusao`) |
| `banca-min` + `reenunciado` | **conflita nos TRÊS** (abstract, resumo, Cap. 6) |

Ou seja: as duas branches são mutuamente incompatíveis na redação do veredito, e
nenhuma das duas aplica na main de hoje.

## O conteúdo dela é bom — e é isso que torna a colisão cara

Não estou pedindo para descartar. O que a `banca-min` faz é **apertar a
afirmação**, e aperta bem:

- troca "refutada …, **mas sustentada** a partir de ≈50% do *pool*" por
  "refutada …, **tornando-se alcançável** a partir de ≈50% do *pool* **em
  varredura com rótulos de gabarito**" — acrescenta a qualificação que faltava
  (a varredura usou gabarito, não oráculo);
- conserta uma contagem errada no resumo ("Quatro resultados principais" →
  "Cinco", e são cinco mesmo);
- acrescenta a estatística pareada ao resumo (IC *bootstrap* e McNemar).

Perder isso num descarte seria desperdício.

## O problema comum às três frentes, que ninguém resolve escrevendo

**Todas escrevem um piso que o regime canônico falsifica.** Elas dizem "a partir
de ≈50% do *pool*" (E25). No regime canônico, o E25 **não cruza** o critério de
Macro F1 — quem cruza é o E35, 70% do *pool*, e ainda assim em 2 de 3 sementes.
Está medido no meu quadro de `fbf7489`.

Então, hoje, qualquer uma das três que entre põe no resumo, no abstract e no
Cap. 6 um número que depende de uma decisão que o autor ainda não tomou.

## O que sugiro, em uma frase

**Decidir o regime primeiro; depois UMA frente reescreve as quatro superfícies
de uma vez**, absorvendo o aperto de redação da `banca-min` (que é bom e é
independente do regime) e o valor absoluto do reenunciado. Fazer na ordem
inversa custa três rebases e três gates para chegar ao mesmo lugar.

Não toquei em nenhuma das duas branches: são da banca e o conteúdo em conflito é
a redação do veredito dela.
