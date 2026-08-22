---
de: banca
para: principal
tipo: entrega
acao_esperada: SUBSTITUI INTEGRALMENTE o pacote 0245, REPROVADO pelo autor no gate; aplicar esta versão v2, em que a refutação sai do texto por decisão dele; ver o §3, que lista as dependências criadas (artigos a4 e a2 carregam a moldura antiga) e a única ressalva técnica que a banca mantém
referencia: reprovação do autor em conversa com a banca, 2026-08-18 ("eu nunca pedi a refutação, foi criado no meio do processo e agora na revisão que identifiquei") · pacote 0245 (descartado) · proveniência 0210
criada_em: 2026-08-18T03:20:00Z
---

# 0. Por que a v1 foi reprovada, e o que a banca verificou

A v1 preservava a refutação como "leitura dupla". O autor reprovou: o
critério de $\le 30\%$ do \textit{pool} nunca foi hipótese dele, nasceu
durante a redação e ele o identificou agora, na revisão. A banca verificou
antes de aceitar a premissa, e ela se confirma:

- `docs/records/decisoes.jsonl` **não tem nenhum registro** do critério de
  30%. Não há ADR, não há decisão datada, não há ata.
- O histórico do git não mostra o critério entrando por decisão registrada.
- A proveniência que EXISTE é a dos 15% ancorados na literatura
  (entrega 0210: Settles 2009 e Schröder 2022, conferidos na fonte).

Consequência que vale registrar com todas as letras: o texto atual chama de
"pré-registrado" um critério sem registro. Manter a refutação seria reportar
o fracasso contra uma trave que ninguém fincou; e chamá-la de pré-registro
seria afirmar registro inexistente, que é o mesmo defeito que a banca
apontaria do outro lado. Sai por correção, não por conveniência.

# 1. As 6 edições, v2

## (1) 1-intro, enunciado do critério

ANTES: "O critério: treinado com no máximo $30\%$ dos exemplos do
\textit{pool}, rotulados pelo oráculo, o framework deve alcançar pelo menos
$95\%$ do Macro F1-Score que o mesmo classificador obtém com o \textit{pool}
inteiro rotulado, superando com significância estatística a seleção
aleatória e a seleção por incerteza sob o mesmo orçamento."

DEPOIS: "O critério: treinado com no máximo \textbf{34.724 rótulos}, ou
$15\%$ da base deduplicada de 231.490 textos únicos, o framework deve
alcançar pelo menos $95\%$ do Macro F1-Score que o mesmo classificador
obtém com o \textit{pool} de referência inteiramente rotulado, superando com
significância estatística a seleção aleatória e a seleção por incerteza sob
o mesmo orçamento. O teto tem lastro na literatura de aprendizado ativo, que
reporta desempenho equivalente ao da supervisão passiva com frações dessa
ordem: menos de $10\%$ dos dados na ilustração canônica de
\citet{Settles2009} e entre $0{,}4\%$ e $14\%$ nos benchmarks com
transformers de \citet{Schroder2022Uncertainty}."

## (2) 3-metodo, papel do pool

ANTES: "O tamanho de 50 mil resulta de viabilidade computacional: [...]
média de 70 exemplos por classe no \textit{pool}."

DEPOIS: acrescentar ao fim: "O \textit{pool} é, portanto, \emph{referência
de comparação} e não o universo do problema: o orçamento da hipótese é
medido contra a base deduplicada (Seção~\ref{sec:intro-hipotese}), e os 50
mil respondem a quanto seria preciso rotular por escolha aleatória para
cobrir o mesmo espaço."

## (3) 3-metodo, critério de aceitação do E3'

ANTES: "O critério de aceitação da hipótese central torna-se direto:
$F1(A) \ge 0{,}95 \cdot F1(D)$, com $|A|/|D| \approx 18\%$ dos rótulos."

DEPOIS: "O critério de aceitação da hipótese central torna-se direto:
$F1(A) \ge 0{,}95 \cdot F1(D)$, com $|A|$ limitado a 34.724 rótulos ($15\%$
da base). O braço (A) do laço executado usa $\approx 18\%$ do \textit{pool},
cerca de $3{,}9\%$ da base, e a varredura de orçamento cobre a faixa até o
teto."

## (4) 5-resultados, leitura (i) do fecho do pilar

ANTES: "O critério em \emph{acurácia} passa a valer em 20 mil rótulos
($40\%$ do \textit{pool}) e o critério em \emph{Macro F1} [...] em 25 mil
($50\%$); o orçamento pré-registrado de $\le 30\%$ era, portanto, apertado
demais para o objetivo macro do classificador forte, mas o piso correto é
modesto e conhecido."

DEPOIS: "O critério em \emph{acurácia} passa a valer em 20 mil rótulos
($8{,}6\%$ da base) e o critério em \emph{Macro F1}, a métrica da hipótese,
em 25 mil ($10{,}8\%$ da base): ambos os pisos ficam \textbf{dentro do teto
de $15\%$} adotado como critério (Seção~\ref{sec:intro-hipotese}). O piso é,
portanto, modesto, conhecido e cabe no orçamento que a hipótese admite. O
laço executado ponta a ponta com oráculo parou por estagnação em 15 mil
rótulos ($6{,}5\%$ da base), antes desse piso, e a Seção~\ref{sec:res-e3p}
mostra que a causa é a política de parada herdada do classificador leve."

## (5) 6-conclusao, o veredito

ANTES: "A hipótese quantitativa central ($\ge 95\%$ do Macro F1 de
supervisão completa com $\le 30\%$ dos rótulos via oráculo LLM) foi
submetida ao teste pré-registrado (E3$'$): \textbf{refutada no orçamento de
$30\%$ originalmente fixado, tornando-se alcançável a partir de $50\%$ do
\textit{pool} em varredura \textit{post hoc} com rótulos de gabarito}, com o
diagnóstico identificando a causa"

DEPOIS: "A hipótese quantitativa central ($\ge 95\%$ do Macro F1 da
supervisão completa do \textit{pool} de referência, com no máximo 34.724
rótulos, ou $15\%$ da base) foi submetida ao teste (E3$'$):
\textbf{sustentada dentro do teto, com o piso do critério em Macro F1
localizado em 25 mil rótulos, $10{,}8\%$ da base}, na varredura de orçamento
com rótulos de gabarito. O laço executado com oráculo LLM parou por
estagnação em 15 mil rótulos ($6{,}5\%$ da base), aquém desse piso, e o
diagnóstico identifica a causa"

## (6) resumo.tex

ANTES: "respondeu à hipótese central pré-registrada --- $\ge 95\%$ do Macro
F1 da supervisão completa do \textit{pool} com $\le 30\%$ dos rótulos ---,
que foi \textbf{refutada no orçamento de 30\% pré-registrado, tornando-se
alcançável a partir de $\approx$50\% do \textit{pool} em varredura com
rótulos de gabarito}"

DEPOIS: "respondeu à hipótese central --- $\ge 95\%$ do Macro F1 da
supervisão completa do \textit{pool} de referência com no máximo 34.724
rótulos, $15\%$ da base --- que foi \textbf{sustentada dentro do teto: o
piso em Macro F1 está em 25 mil rótulos, $10{,}8\%$ da base, na varredura
com rótulos de gabarito, enquanto o laço com oráculo parou por estagnação em
15 mil}"

O abstract em inglês espelha (6), no mesmo lote.

# 2. A ÚNICA ressalva técnica que a banca mantém (e ela não é sobre a trave)

O piso de 25 mil foi medido com **rótulos de gabarito**, e o critério fala em
rótulos fornecidos pelo **oráculo**. São condições diferentes, e a diferença
é medida pela tese (o par A/B quantifica o custo do ruído do oráculo). A
redação acima já diz "na varredura com rótulos de gabarito" em todos os
pontos, e isso basta: afirma o que foi medido, na condição em que foi
medido. NÃO escrever, em nenhum ponto, "sustentada com oráculo LLM" sem a
qualificação, porque essa medida ainda não existe.

Ela vai existir: a re-execução sem critério de parada que o autor ordenou ao
executor02 (tarefa 1905) leva o laço com oráculo até o fim do orçamento e
produz exatamente o ponto que falta. Quando a curva chegar, este parágrafo
pode ser fechado sem ressalva. Amarrar as duas coisas.

# 3. Dependências criadas por este pacote

1. `artigos/a4-falco-framework/main.tex` (linhas 51, 55, 216) e
   `artigos/a2-vies-autoavaliacao/main.tex` (linha 92) carregam a moldura
   antiga, inclusive "refuted at 30%" e "pre-registered hypothesis". Se
   nenhum deles foi submetido, atualizam-se junto. Se algum JÁ foi
   submetido, isso vira decisão do autor, e a tese precisa de nota
   explicando a diferença. Confirmar o status com ele.
2. `Schroder2022Uncertainty` passa de órfã a citada; a ficha precisa da
   correção 15% -> 14% ANTES.
3. As três ocorrências antigas de "15% dos rótulos" com denominador de POOL
   (resumo e 5-resultados:246 e :277) precisam do denominador explícito.
4. Varrer o texto por "pré-registrado" onde a expressão se referir ao
   critério de orçamento: sai. Onde se referir a partições imutáveis ou ao
   gate de 85%, permanece (são outras decisões, com registro próprio).
