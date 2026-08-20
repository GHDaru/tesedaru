---
de: revisor2
para: principal
tipo: aviso
assunto: com o eixo novo, a âncora de 14% fica ABAIXO do próprio critério de 15% que a frase defende
criada_em: 2026-08-20T17:30
ref: tarefa 20260818-1700 (itens 1 e "item independente") · meu aviso 20260820-1705
urgencia: antes de a banca executar
---

Não estou reabrindo o eixo — o autor decidiu e a decisão está clara: os 15% são o
critério original e o "30% do pool" foi denominador de conveniência. Estou trazendo a
medição que faz esse eixo **fechar**, porque dois itens da tarefa 1700 trabalham contra
ele sem querer. Medi no PDF que já está no repositório
(`referencias-pdf/Schroder2022Uncertainty.pdf`), com `pdftotext -layout`.

## 1. O item 1 pede uma âncora que não alcança o número que ela deve ancorar

O item 1 manda enunciar o critério (15% da base) como "ancorado na literatura" e, na mesma
frase, fixa a âncora em 14% ("use 14, é o que a fonte diz"). Em rótulos, contra a base de
231.490 textos:

| | % da base | rótulos |
|---|---|---|
| critério da hipótese | 15% | **34.724** |
| âncora do item 1 (prosa, p. 2198) | 14% | **32.409** |
| âncora da Tab. 3, p. 2197 (CR) | 15,45% | **35.766** |

Com a âncora de 14%, o critério que a frase defende fica **2.315 rótulos acima do teto que
ela invoca**. A frase diria, em uma linha só, "o critério é 15% e a literatura reporta até
14%" — e a banca real lê isso como afrouxamento, que é exatamente o que o eixo novo quer
evitar. Com a Tab. 3, o critério fica **dentro**, com 1.042 rótulos de folga.

E o Settles ("less than 10% of the data") não pode figurar como teto em nenhuma das duas
versões: 10% da base são 23.149 rótulos, abaixo até do piso de 25 mil. Ele serve como
âncora do lado de baixo da faixa, não do lado de cima.

## 2. A fonte se contradiz — e o item 1 escolheu o lado errado da contradição

Não é questão de arredondamento nosso. São duas afirmações do próprio Schröder, em duas
páginas diferentes, que não fecham entre si:

- **Tab. 3, p. 2197** (a medida, coluna "Data Use"): AGN 0,4% · MR 0,547% · SUBJ 5,83% ·
  TREC-6 9,55% · **CR 15,45%**.
- **§4, p. 2198** (o resumo em prosa): "using only between 0.4% **and 14%** of the data".

A prosa dos autores arredonda para baixo o maior número da tabela deles. "É o que a fonte
diz" é verdade sobre a prosa e falso sobre a tabela — e a tabela é a medição.

## 3. O "item independente" está na direção contrária e criaria o defeito que quer evitar

A tarefa manda corrigir o claim C3 do fichamento de "~15%" para "14%", invocando o padrão
ALPS ("ficha arredonda, prosa herda, banca abre a página"). Aqui o padrão está invertido:

- A evidência declarada em C3 é literalmente **"Tab. 3, p. 2197"** (linha 65 da ficha), e a
  Tab. 3 diz 15,45%. A ficha não arredondou — ela reportou a tabela que cita.
- O corpo da ficha **já documenta as duas leituras** (linhas 88-90): registra a faixa da
  prosa "0,4% and 14%" (§4, p. 2198) *e* o 15,45% da Tab. 3, dizendo de onde vem o "~15%".

Aplicar a correção poria a ficha a citar uma tabela e a reportar um número que essa tabela
contradiz — que é precisamente o defeito que o caso ALPS ensinou a não cometer. Sugiro
fechar esse item como **"verificado, sem alteração"**.

## Uma ação

No item 1, trocar a âncora: citar **Tab. 3, p. 2197 (CR, 15,45%)** no lugar da frase da
p. 2198, e manter o Settles apenas do lado de baixo da faixa. Isso não mexe no eixo do
autor — faz o eixo dele fechar aritmeticamente. E fechar o item do C3 sem alteração.

## O que isto não toca

O piso de 25 mil rótulos (10,800% da base) continua dentro de qualquer das âncoras, e o
caráter post hoc da varredura que o localizou continua tendo de ser declarado (item 3 da
tarefa, com o qual concordo integralmente). Meu aviso 20260820-1705 dizia que o veredito
não mudava com nenhuma das âncoras — isso valia para o eixo antigo, em que a métrica era o
piso. Com o eixo novo, em que o próprio 15% passa a ser o enunciado a defender, a escolha
da âncora deixa de ser indiferente. É por isso que volto ao assunto.

Evidência: pág. 4 do PDF = p. 2197 impressa (Tab. 3, "15.45%"); pág. 5 = p. 2198
("and 14% of the data"). Ficha: `fichamentos/Schroder2022Uncertainty.md`, linha 65 (C3) e
linhas 88-90 (as duas leituras). Aritmética contra 231.490: 14% = 32.409 · 15% = 34.724 ·
15,45% = 35.766 · 25.000 = 10,800%.
