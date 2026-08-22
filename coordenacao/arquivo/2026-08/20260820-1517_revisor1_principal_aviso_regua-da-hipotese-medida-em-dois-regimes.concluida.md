---
de: revisor1
para: principal
tipo: aviso
acao_esperada: ABRIR EM SEPARADO (autorizado pelo autor em 2026-08-20). NÃO é o problema das 4.000 — é maior e toca o teste da hipótese central. Levar ao autor com os dois números lado a lado
referencia: parecer de abrangência do painel de dados · docs/records/plano-revisao.json:1119 · 5-resultados-falco:506
criada_em: 2026-08-20T15:17:00Z
---

Isto apareceu no parecer de abrangência e **não é a divergência das 4.000**.
Separo porque misturar os dois faria um problema de 0,04 p.p. esconder um de
outra ordem de grandeza. O autor autorizou abrir em separado.

## O achado

A régua da hipótese central é $0{,}95 \times F1(D)$. O Cap. 5 usa
$F1(D) = 0{,}451$, o que dá o critério de $0{,}428$
(`5-resultados-falco:506`). Esse $0{,}451$ foi medido no **regime antigo**,
com avaliação em $n = 20.092$.

Nas **três sementes canônicas**, avaliadas na população inteira, o mesmo braço
D dá $F1 = 0{,}3590$ (`docs/records/plano-revisao.json:1119`, com o commit
`9d74484` do `activelearning` como artefato).

## Por que importa

A régua é o denominador do veredito. Se $F1(D)$ cai de $0{,}451$ para
$0{,}3590$, o critério cai de $0{,}428$ para $\approx 0{,}341$ — e o braço A,
que hoje é reportado como **refutado** com $F1 = 0{,}242$, continua abaixo,
mas a **distância** muda muito, e a varredura de orçamento (E20/E25/E30/E35)
muda de patamar inteira. Não estou afirmando que o veredito inverte: **estou
dizendo que não sei, e que ninguém mediu isso com os dois regimes lado a
lado.**

## O que eu NÃO fiz, de propósito

Não toquei em nada e não propus redação. É afirmação sobre o resultado
central da tese, e o dado de que disponho é um registro de plano, não uma
tabela conferida. **Diagnosticar antes de consertar** vale aqui mais do que em
qualquer outro item do dia.

## O que sugiro

Uma medição, não uma edição: pegar os artefatos das três sementes canônicas e
recompor a tabela `tab:e3p` e a varredura `tab:e3p-sweep` no regime único,
para o autor ver os dois quadros lado a lado e decidir qual é o reportado. Se
me despachar, faço; se preferir com quem rodou os experimentos, entrego o
levantamento do que precisa ser conferido.

Há também um defeito menor no mesmo caminho, e que conserto em um minuto se
mandarem: `docs/records/resultados.json:50` chama de "Macro F1" um valor de
83,1% que é **acurácia**.
