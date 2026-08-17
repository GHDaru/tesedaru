---
de: banca
para: principal
tipo: tarefa
acao_esperada: aplicar na zona t1 (2-fundam/texto.tex, subseção 2.1.4) a substituição integral dos 4 parágrafos de inferência + 1 linha da tabela, LaTeX verbatim abaixo; gate em bloco ao autor
referencia: leitura do autor na 2.1.4 (aprovação da opção b — 4 fórmulas em display) · ciclo completo R3/R4/R5/R6/R1 rodado pela banca · ficha Guyon2011ALC criada em d82f00c (DoD do R3 cumprida)
criada_em: 2026-08-17T08:15:00Z
---
PACOTE T1 — INFERÊNCIA ESTATÍSTICA COM AS 4 FÓRMULAS (aprovação do autor
condicionada à aplicação deste texto exato; ele pediu o ciclo completo antes,
e o ciclo rodou: R3 achou e sanou a ficha faltante do Guyon; R4 conferiu
Dietterich contra a ficha; R5 conferiu a aritmética; R6 acrescentou glosas de
z, semente e réplicas; R1 removeu os padrões de IA da minha própria proposta).

Rótulos eq:wilson, eq:mcnemar, eq:wilcoxon, eq:bootstrap verificados livres
em toda a tese. Zero travessões. Substituir os 4 parágrafos atuais
(2-fundam/texto.tex:155-194) por:

%%% INÍCIO DO BLOCO %%%
\textbf{Intervalo de confiança para proporções (Wilson).} Toda acurácia é uma
proporção estimada em $n$ instâncias. Um intervalo de confiança de 95\% deve
conter o valor verdadeiro em 95\% das repetições do experimento; a fração em
que isso de fato ocorre é a \emph{cobertura} do intervalo, e os 95\%
declarados são o seu \emph{nível nominal}. O intervalo usual de Wald
($\hat{p} \pm z\sqrt{\hat{p}(1-\hat{p})/n}$, com $z$ o quantil da normal
padrão associado ao nível: $1{,}96$ para 95\%) fica aquém do que declara: sua
cobertura real cai abaixo do nível nominal e varia de forma imprevisível
conforme $n$ e $p$ mudam, mesmo com amostras grandes. O intervalo de
\citet{Wilson1927} evita o defeito partindo da desigualdade do teste,
$|\hat{p}-p| \le z\sqrt{p(1-p)/n}$, cuja variância usa o parâmetro
desconhecido $p$ e não a estimativa $\hat{p}$, e resolvendo-a para $p$ como
equação de segundo grau. As raízes delimitam o intervalo
\begin{equation}
\frac{\hat{p} + \frac{z^2}{2n} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}},
\label{eq:wilson}
\end{equation}
cujo centro desloca $\hat{p}$ levemente em direção a $1/2$ e cuja largura
ganha o termo de correção $z^2/4n^2$; é isso que mantém a cobertura próxima
do nível nominal em toda a faixa de $p$. A análise sistemática de
\citet{Brown2001} o recomenda como escolha padrão. Por isso toda acurácia de
oráculo desta tese é reportada com IC de Wilson a 95\%
(Capítulo~\ref{ch:resultados-falco}).

\textbf{Comparação pareada na mesma amostra (McNemar).} Quando dois oráculos
rotulam \emph{as mesmas} instâncias, seus acertos não são independentes, e a
comparação correta olha apenas os pares discordantes: as $b$ instâncias em
que só o primeiro acerta e as $c$ em que só o segundo. Sob a hipótese nula de
desempenhos iguais, cada discordância tem probabilidade $1/2$ de cair para
cada lado, e o teste de \citet{McNemar1947} verifica se a assimetria
observada excede o que esse sorteio produziria, pela estatística
\begin{equation}
\chi^2 = \frac{(b-c)^2}{b+c},
\label{eq:mcnemar}
\end{equation}
comparada à distribuição qui-quadrado com um grau de liberdade. Quando
$b+c<25$, a aproximação deixa de ser confiável e usa-se a versão binomial
exata: sob a nula, $b \sim \mathrm{Binomial}(b+c,\,1/2)$, e o $p$-valor
bicaudal é $2\,P(X \le \min(b,c))$. A escolha segue \citet{Dietterich1998},
que comparou empiricamente cinco testes e concluiu que o McNemar é o adequado
quando cada modelo é avaliado uma única vez sobre um conjunto comum, o regime
desta tese; nos experimentos daquele estudo, os demais testes apontaram
diferença onde não existia com frequência maior do que o nível de
significância prometia.

\textbf{Comparação pareada por semente (Wilcoxon).} Quando duas estratégias
são executadas com as mesmas sementes de aleatorização (o valor que fixa o
gerador pseudoaleatório e torna cada execução repetível), cada semente gera
um par de resultados e uma diferença $d_i$. O teste de postos sinalizados de
\citet{Wilcoxon1945} ordena os valores absolutos $|d_i|$, atribui-lhes postos
$1,\dots,n$ e soma os postos das diferenças positivas,
\begin{equation}
W^{+} = \sum_{i:\; d_i>0} \operatorname{posto}(|d_i|).
\label{eq:wilcoxon}
\end{equation}
Sob a hipótese nula, cada sinal é positivo ou negativo com probabilidade
$1/2$, o que dá a $W^{+}$ distribuição conhecida sem supor normalidade,
suposição difícil de sustentar para métricas limitadas ao intervalo $[0,1]$,
como o Macro F1; é a recomendação de \citet{Demsar2006} para comparar dois
algoritmos sobre múltiplas condições. Um limite aritmético importa ao
desenho: o caso mais extremo, todos os $n$ sinais para o mesmo lado, tem
probabilidade $1/2^{n}$ por cauda, logo o menor $p$-valor bicaudal é
$2/2^{n}$. Seis sementes são o mínimo que alcança significância a 5\%
($p=0{,}031$); esta tese adota oito, cujo piso de $p=0{,}0078$ mantém a
significância alcançável mesmo sob correção para comparações múltiplas sobre
as mesmas sementes.

\textbf{Intervalos por reamostragem (\textit{bootstrap}).} Para uma proporção
existe fórmula fechada de intervalo; para estatísticas que resumem uma curva
inteira em um único número, como a área sob uma curva de aprendizado
\citep{Guyon2011ALC}, a distribuição amostral não é conhecida e não há
fórmula. O \textit{bootstrap} \citep{EfronTibshirani1993} contorna a ausência
com um procedimento: dos $n$ pares observados, sorteiam-se $n$ com reposição;
calcula-se a estatística de interesse na reamostra; repete-se o sorteio $B$
vezes, obtendo as réplicas $\theta^{*}_{1},\dots,\theta^{*}_{B}$; e o
intervalo de confiança toma os percentis empíricos dessas réplicas,
\begin{equation}
\mathrm{IC}_{95\%} = \left[\theta^{*}_{(2{,}5\%)},\; \theta^{*}_{(97{,}5\%)}\right],
\label{eq:bootstrap}
\end{equation}
o chamado método do percentil. Sem conhecer a distribuição populacional, o
procedimento usa a própria amostra como o melhor retrato disponível dela e
mede quanto a estatística flutua ao repetir o experimento dentro desse
retrato.
%%% FIM DO BLOCO %%%

E na tabela tab:inferencia-mapa, a linha do bootstrap:
"Funcional sem distribuição conhecida" -> "Estatística de resumo sem
distribuição conhecida".

DoD para o gate: (i) bloco aplicado verbatim; (ii) linha da tabela trocada;
(iii) grep confirma eq:wilson/eq:mcnemar/eq:wilcoxon/eq:bootstrap únicos;
(iv) ficha Guyon2011ALC existe (d82f00c, já na main); (v) zero "—" no bloco.

## Resultado (principal, 2026-08-17T13:50Z)
Aplicado na main: bloco verbatim (155-194) + célula da tabela. DoD verde nos 5 itens.
