---
de: banca
para: principal
tipo: entrega
acao_esperada: LER O §0 ANTES DE TUDO e levá-lo ao autor: o reenunciado FLIPA o veredito central da tese (de refutada para sustentada), e isso precisa de decisão consciente dele sobre o enquadramento, não de aplicação silenciosa; com o enquadramento aprovado, as 6 edições de antes/depois do §2 estão prontas para aplicar
referencia: tarefa 20260818-0145 · decisão do autor pela opção (b), valor absoluto · proveniência entregue em 0210 (Settles 2009 e Schröder 2022 conferidos na fonte)
criada_em: 2026-08-18T02:45:00Z
---

# 0. O QUE NINGUÉM MEDIU AINDA: o reenunciado inverte o veredito

Aritmética, toda conferida contra a base de 231.490 textos únicos:

| Marco | Rótulos | % da base | % do pool |
|---|---|---|---|
| Braço (A), pipeline real executado | ~9.000 | ~3,9% | ~18% |
| Orçamento pré-registrado e executado | 15.000 | **6,5%** | 30% |
| Piso do critério em acurácia | 20.000 | 8,6% | 40% |
| **Piso do critério em Macro F1** | **25.000** | **10,8%** | 50% |
| **TETO NOVO (15% da base)** | **34.724** | **15,0%** | 69% |
| Braço E35 | 35.000 | 15,1% | 70% |

**O piso da métrica da hipótese (25 mil, 10,8% da base) fica ABAIXO do teto
novo (34.724, 15%).** Com o denominador e o teto reenunciados, a hipótese
central deixa de ser refutada e passa a ser sustentada.

Isso é exatamente o que o autor previu ("se conseguimos mais, ótimo"), mas é
também a definição de trave móvel, se enunciado sem cuidado: o teto foi
reenunciado DEPOIS de o resultado ser conhecido. A banca não recomenda
esconder nem recuar; recomenda a LEITURA DUPLA, que é defensável e mais
honesta que qualquer das duas leituras isoladas:

1. contra o orçamento fixado no documento (30% do pool, 15 mil), o critério
   NÃO foi atingido e a causa está diagnosticada (política de parada);
2. contra o teto ancorado na literatura (15% da base, 34.724), o critério é
   atingido com 25 mil rótulos, e a varredura que mostra isso é POST HOC;
3. a tese declara as duas coisas e diz qual é qual.

Uma precisão que reforça o cuidado: o braço E35, o que supera a supervisão
completa em Macro F1, usa 35.000 rótulos, ou 15,1% da base. Ele fica
LIGEIRAMENTE ACIMA do teto novo. Ou seja, o teto de 15% não é generoso a
ponto de absorver tudo: ele acomoda o piso (10,8%) e deixa o E35 de fora por
uma fração de ponto percentual. Isso é bom para a defesa e precisa ser dito,
não escondido.

# 1. O que NÃO muda (guarda do princípio III)

Experimento executado, números medidos, diagnóstico da causa e o estatuto
post hoc da varredura. Reenunciar não é reinterpretar.

# 2. As 6 edições, antes/depois

## (1) 1-intro, enunciado do critério

ANTES: "O critério: treinado com no máximo $30\%$ dos exemplos do
\textit{pool}, rotulados pelo oráculo, o framework deve alcançar pelo menos
$95\%$ do Macro F1-Score que o mesmo classificador obtém com o \textit{pool}
inteiro rotulado, superando com significância estatística a seleção
aleatória e a seleção por incerteza sob o mesmo orçamento."

DEPOIS: "O critério: treinado com no máximo \textbf{34.724 rótulos}
fornecidos pelo oráculo, ou $15\%$ da base deduplicada de 231.490 textos
únicos, o framework deve alcançar pelo menos $95\%$ do Macro F1-Score que o
mesmo classificador obtém com o \textit{pool} de referência inteiramente
rotulado, superando com significância estatística a seleção aleatória e a
seleção por incerteza sob o mesmo orçamento. O teto tem lastro na literatura
de aprendizado ativo, que reporta desempenho equivalente ao da supervisão
passiva com frações dessa ordem: menos de $10\%$ dos dados na ilustração
canônica de \citet{Settles2009} e entre $0{,}4\%$ e $14\%$ nos benchmarks
com transformers de \citet{Schroder2022Uncertainty}."

## (2) 3-metodo, papel do pool (o ponto que a arguição ataca hoje)

ANTES: "O tamanho de 50 mil resulta de viabilidade computacional: cada braço
do E3$'$ é um ajuste fino completo do BERTimbau, e o programa executa cinco
braços mais a varredura de orçamento em uma única GPU, mantendo ainda uma
média de 70 exemplos por classe no \textit{pool}."

DEPOIS: idem, e acrescentar ao fim do período: "O \textit{pool} é, portanto,
\emph{referência de comparação} e não o universo do problema: o orçamento da
hipótese é medido contra a base deduplicada
(Seção~\ref{sec:intro-hipotese}), e os 50 mil respondem a quanto seria
preciso rotular por escolha aleatória para cobrir o mesmo espaço."

## (3) 3-metodo, critério de aceitação do E3'

ANTES: "O critério de aceitação da hipótese central torna-se direto:
$F1(A) \ge 0{,}95 \cdot F1(D)$, com $|A|/|D| \approx 18\%$ dos rótulos."

DEPOIS: "O critério de aceitação da hipótese central torna-se direto:
$F1(A) \ge 0{,}95 \cdot F1(D)$, com $|A|$ limitado a 34.724 rótulos ($15\%$
da base). O braço (A) executado usa $\approx 18\%$ do \textit{pool}, cerca
de $3{,}9\%$ da base, portanto muito abaixo do teto: a execução foi mais
restritiva que o critério."

## (4) 5-resultados, leitura (i) do fecho do pilar

ANTES: "o orçamento pré-registrado de $\le 30\%$ era, portanto, apertado
demais para o objetivo macro do classificador forte, mas o piso correto é
modesto e conhecido."

DEPOIS: "o piso do critério em Macro F1, 25 mil rótulos, equivale a
$10{,}8\%$ da base e fica dentro do teto de $15\%$ adotado como critério
(Seção~\ref{sec:intro-hipotese}); o orçamento efetivamente executado, 15 mil
rótulos ou $6{,}5\%$ da base, era mais restritivo que o teto e apertado
demais para o objetivo macro do classificador forte. O piso, portanto, é
modesto, conhecido e cabe no critério."

## (5) 6-conclusao, o veredito (AQUI mora a leitura dupla)

ANTES: "A hipótese quantitativa central ($\ge 95\%$ do Macro F1 de
supervisão completa com $\le 30\%$ dos rótulos via oráculo LLM) foi
submetida ao teste pré-registrado (E3$'$): \textbf{refutada no orçamento de
$30\%$ originalmente fixado, tornando-se alcançável a partir de $50\%$ do
\textit{pool} em varredura \textit{post hoc} com rótulos de gabarito}"

DEPOIS: "A hipótese quantitativa central ($\ge 95\%$ do Macro F1 da
supervisão completa do \textit{pool} de referência, com no máximo 34.724
rótulos, ou $15\%$ da base) foi submetida ao teste (E3$'$) com duas leituras
declaradas. \textbf{No orçamento efetivamente executado, 15 mil rótulos
($6{,}5\%$ da base, $30\%$ do \textit{pool}), o critério não foi atingido};
a varredura \textit{post hoc} com rótulos de gabarito localiza o piso em 25
mil rótulos ($10{,}8\%$ da base), \textbf{dentro do teto de $15\%$}. A
distinção importa e é declarada: o orçamento de $30\%$ do \textit{pool} era
o valor fixado no protocolo executado, mais restritivo que o teto de $15\%$
da base que a literatura sustenta e que esta tese adota como critério"

## (6) resumo.tex, a mesma leitura dupla em uma frase

ANTES: "respondeu à hipótese central pré-registrada --- $\ge 95\%$ do Macro
F1 da supervisão completa do \textit{pool} com $\le 30\%$ dos rótulos ---,
que foi \textbf{refutada no orçamento de 30\% pré-registrado, tornando-se
alcançável a partir de $\approx$50\% do \textit{pool}}"

DEPOIS: "respondeu à hipótese central --- $\ge 95\%$ do Macro F1 da
supervisão completa do \textit{pool} de referência com no máximo 34.724
rótulos, $15\%$ da base --- com duas leituras: \textbf{no orçamento
executado de 15 mil rótulos ($6{,}5\%$ da base) o critério não foi atingido,
e a varredura \textit{post hoc} localiza o piso em 25 mil ($10{,}8\%$ da
base), dentro do teto}"

O abstract em inglês espelha (6) e vai no mesmo lote.

# 3. Dependências que este pacote CRIA

1. `Schroder2022Uncertainty` passa a ser CITADA (hoje é órfã com ficha). A
   ficha existe; o claim C3 dela precisa da correção 15% -> 14% ANTES de a
   citação entrar, senão a prosa nasce citando número que a fonte não tem.
2. As três ocorrências antigas de "15% dos rótulos" com denominador de POOL
   (resumo e 5-resultados:246 e :277) precisam ganhar o denominador
   explícito, senão a tese passa a ter dois 15% distintos. Sem isso, a
   opção (b) não elimina a ambiguidade que ela existe para eliminar.
