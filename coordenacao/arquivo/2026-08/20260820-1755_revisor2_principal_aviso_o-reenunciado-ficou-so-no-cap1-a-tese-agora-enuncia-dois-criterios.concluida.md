---
de: revisor2
para: principal
tipo: aviso
assunto: o reenunciado ficou só no Cap.1 — a tese agora enuncia DOIS critérios (34.724 e 15.000) e o Cap.5 ainda refuta com a régua antiga
criada_em: 2026-08-20T17:55
ref: commit 2aa0b4f (cap1: reenunciado, v2 da banca, aprovado pelo autor) · meu gatilho 8
urgencia: alta — está na main e o Cap.5 vai herdar
---

O gatilho 8 disparou no 2aa0b4f. Dos três itens que ele mandava conferir, **dois
passam** e vou dizê-los primeiro, porque são trabalho bem feito: o caráter *post hoc*
da varredura está declarado (Cap.5, linha 552, em negrito), e o valor absoluto aparece
na primeira ocorrência, resolvendo a colisão com os "15% do pool". O terceiro item — a
âncora do Schröder — foi acolhido: a frase cita a Tab. 3, não a prosa. Obrigado.

O que segue são dois achados novos. O primeiro é objetivo e mecânico; o segundo é meu e
eu preciso assumi-lo, porque a âncora que ele questiona fui eu que forneci.

## Achado 1 — o reenunciado ficou preso no Cap.1

O commit mexeu em **um arquivo só** (`1-intro/texto.tex`, 10 inserções / 6 remoções).
O Cap.3 e o Cap.5 não foram tocados, e ambos continuam carregando a régua anterior,
literalmente:

| onde | o que está escrito hoje na main | orçamento |
|---|---|---|
| `1-intro/texto.tex:96` (NOVO) | "no máximo **34.724 rótulos**, ou 15% da base deduplicada de 231.490" | **34.724** |
| `3-metodo/texto.tex:203-204` | "os orçamentos passam a ser medidos como fração do *pool* de 50 mil (**30% = 15 mil rótulos**), e não de $\|U_0\|$" | **15.000** |
| `3-metodo/texto.tex:651-653` | "o orçamento pré-registrado ($B=30\%$ de $\|U_0\|$) foi re-baseado para fração do *pool* de 50 mil; os percentuais reportados no Capítulo 5 **referem-se sempre ao denominador de 50 mil**" | pool |
| `5-resultados-falco/texto.tex:574,586` | "E25 & 25.000 & **50\%**" e "em 25 mil (50%); o orçamento pré-registrado de $\le 30\%$ era, portanto, ..." | pool |

Consequências, em ordem de gravidade:

1. **A tese enuncia dois critérios incompatíveis**, com fator 2,3× entre eles: 34.724
   rótulos (Cap.1) e 15.000 rótulos (Cap.3). Uma banca que ler os dois capítulos na
   mesma tarde pergunta qual vale.
2. **O Cap.5 continua concluindo pela refutação com a régua antiga.** Ele mede o piso em
   "25 mil (50%)" contra o "orçamento pré-registrado de ≤30%" — exatamente o argumento
   que o reenunciado se propôs a corrigir. Hoje o Cap.1 diz uma coisa e o Cap.5 conclui
   a oposta.
3. O número **34.724 não aparece em nenhum outro lugar da tese** (conferido por `grep`
   em 1-intro, 3-metodo, 5-resultados e 7-*). Ele está órfão no Cap.1.
4. O Cap.3 trata a re-baseação para o *pool* como **decisão metodológica declarada**,
   com consequências discutidas nas limitações (linha 651-653). O Cap.1 agora trata a
   mesma re-baseação como o erro que está sendo corrigido. Os dois capítulos discordam
   sobre o que é o erro.

## Achado 2 — a frase de lastro compara frações com denominadores diferentes (a âncora é minha)

A frase nova diz que o teto "tem lastro na literatura ... que reporta desempenho
equivalente ao da supervisão passiva com **frações dessa ordem**", citando Settles
(<10%) e Schröder (15,45%, Tab. 3). Fui eu que forneci o 15,45%, e o número está certo
para aquela fonte. O problema não é o número: é o denominador dele.

A legenda da Tab. 3 do Schröder diz textualmente: *"Data Use indicates proportion of
**training data** used"* — a fração é sobre o conjunto de treino de onde o aprendizado
ativo seleciona. Confere na aritmética da própria fonte: o orçamento é fixo em 525
rótulos (25 iniciais + 20×25) e 525/0,1545 = 3.398, que é o tamanho do treino do CR;
em AGN, 525/120.000 = 0,4%. O denominador é sempre o conjunto selecionável.

O análogo disso na tese é o ***pool* de 50 mil**, não a base de 231.490 — o aprendizado
ativo só pode rotular o que está no *pool*. Então:

| medida | valor |
|---|---|
| critério novo, medido como o Schröder mede | 34.724 / 50.000 = **69,4%** |
| âncora do Schröder (Tab. 3, CR) traduzida para o *pool* | 15,45% = **7.725 rótulos** |
| âncora do Settles traduzida para o *pool* | 10% = **5.000 rótulos** |

Medido da maneira como as fontes citadas medem, o critério é 69,4%, e não 15%. A frase
"frações dessa ordem" compara 15% (da base) com 15,45% (do treino) como se fossem a
mesma grandeza. São 34.724 rótulos contra 7.725.

Isto **não** diz que o autor escolheu o denominador errado — a economia real sobre o
universo operacional de 231.490 textos é um enunciado legítimo, e é o dele. Diz que
esse enunciado não pode ser lastreado em números que usam o outro denominador, sob pena
de a banca fazer a divisão em trinta segundos.

## Saída barata, independente de qual denominador vencer

Declarar o número **nos dois denominadores na primeira ocorrência**: "34.724 rótulos —
15% da base deduplicada de 231.490 e 69,4% do *pool* de referência de 50 mil". Custa uma
oração, mata a ambiguidade em definitivo e é honesto nas duas direções. Com os dois
números à vista, a frase de lastro pode então dizer o que é verdade: que a literatura
reporta frações **do conjunto selecionável** de até ~15%, e que o critério desta tese é
mais generoso nessa régua e mais econômico na régua da base.

E, seja qual for a decisão: **Cap.3 (linhas 203-204 e 651-653) e Cap.5 (linhas 574 e
586) precisam ser re-baseados no mesmo commit que o Cap.1**, senão a tese fica com dois
critérios e uma refutação órfã. Não é minha superfície — o Cap.3 está com o executor e
o Cap.5 está na fila do reenunciado — por isso mando para você em vez de mexer.

Evidência: `git show 2aa0b4f --stat` (1 arquivo); linhas citadas conferidas em
`origin/main @ c76e901`; legenda da Tab. 3 e a conta 525/0,1545 conferidas em
`referencias-pdf/Schroder2022Uncertainty.pdf` (pág. 4 do arquivo = p. 2197 impressa).
