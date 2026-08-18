---
id: Donmez2008
title: "Proactive Learning: Cost-Sensitive Active Learning with Multiple Imperfect Oracles"
authors: ["Donmez, Pinar", "Carbonell, Jaime G."]
year: 2008
venue: "CIKM 2008, pp. 619-628"
doi: "10.1145/1458082.1458165"
pdf: referencias-pdf/Donmez2008.pdf
paper_type: metodo
pillars: [p3-oraculo]
status: fichado
proposes: [aprendizado-proativo, selecao-conjunta-instancia-oraculo, restricao-de-orcamento, oraculo-relutante, oraculo-falivel, custo-nao-uniforme]
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, agrupamento-por-k-medias]
datasets: [face, spambase, adult, uci-letter]
metrics: [erro-de-classificacao, custo-total]
tasks: [classificacao-binaria]
models: [regressao-logistica]
falco_relation:
  - type: fundamenta
    target: oraculo-progressivo
    note: "É a formulação de origem do problema que o FALCO instancia: quando
           existem VÁRIOS oráculos com custos e confiabilidades diferentes, a
           decisão do laço deixa de ser 'qual instância rotular' e passa a ser
           o PAR 'qual instância, com qual oráculo', sob restrição de
           orçamento e não de número de rótulos. É o antecedente formal da
           progressão de fases (LLM barata → LLM cara → humano) e do orçamento
           como unidade de comparação no lugar da contagem de rótulos."
  - type: fundamenta
    target: multiplos-oraculos
    note: "Nomeia as quatro suposições que o oráculo clássico carrega —
           infalível, incansável, individual e insensível a custo — e relaxa as
           quatro. A Seção 2.2.3 da tese trata as três primeiras com
           Sheng2008/Snow2008/Donmez2009/Yan2011; ESTA é a que sustenta a
           quarta (custo distinto por oráculo), hoje sem lastro no texto."
---

# Proactive Learning: Cost-Sensitive Active Learning with Multiple Imperfect Oracles (Donmez & Carbonell, CIKM 2008)

## Resumo
Generaliza o aprendizado ativo relaxando de uma vez as quatro suposições que o
oráculo clássico esconde: que ele nunca erra, sempre responde, é único e cobra
sempre o mesmo (ou nada). No lugar delas, propõe o *aprendizado proativo*:
existem vários oráculos, cada um com sua confiabilidade e seu preço, e a
decisão de cada rodada é conjunta — qual instância consultar **e** a quem
perguntar — por maximização de utilidade esperada sob um **envelope de
orçamento**, não sob um número fixo de instâncias. A formulação exata é
intratável (a maximização é sobre todas as sequências possíveis de amostragem),
e o artigo adota a aproximação gulosa por rodada. Três cenários instanciam a
ideia: oráculo relutante, oráculo falível e oráculo de custo não uniforme.
Avaliação em quatro conjuntos binários pequenos, com oráculos simulados.

Páginas: o PDF aberto na página do co-autor (CMU) tem 10 páginas; a paginação
dos anais é 619-628 (Crossref), consistente com as 10. As citações abaixo usam
a página **do PDF**.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O oráculo do AA clássico é suposto "infalível (nunca erra), incansável (sempre responde), individual (só um) e insensível a custos (sempre grátis ou sempre o mesmo preço)"; o proativo relaxa as quatro | Abstract, p. 1 | 2.2.3 — é a enumeração que organiza a seção; hoje o texto trata só as três primeiras |
| C2 | A decisão do laço é o PAR instância-oráculo: $(x^*,k^*) = \arg\max_{x \in U, k \in K} (P(\text{ans}\mid x,k)\,V(x) - C_k)$ | §3, eq. (2), p. 3 | 2.2.3 e Cap. 3 — antecedente formal da escolha de oráculo por fase |
| C3 | O laço proativo fixa um **envelope de orçamento** em vez de um número de instâncias a amostrar, "já que instâncias e oráculos podem ter custos variáveis" | §3, p. 3 | Cap. 3 — sustenta comparar por custo, não por contagem de rótulos |
| C4 | Três cenários, um por propriedade: (1) confiável × relutante, (2) confiável × falível, (3) custo uniforme × custo não uniforme; cada um analisa **uma só** propriedade por vez | §3, pp. 3-5 | 2.2.3 — o FALCO combina custo e falibilidade ao mesmo tempo; o artigo separa |
| C5 | A formulação conjunta exata é intratável (maximização sobre um número exponencial de sequências de amostragem); usa-se aproximação **gulosa** por rodada | §3, p. 3 | Cap. 3 — justifica por que a progressão de fases é uma heurística, e não uma política ótima |
| C6 | Avaliação em 4 conjuntos **binários** e pequenos: Face (2.500), Spambase (4.601), Adult (4.147), VY-letter (1.550) | Tab. 2, p. 6 | limite de escopo — ver "o que NÃO sustenta" |
| C7 | Os oráculos são **simulados**: o confiável é um classificador treinado em todos os dados; o imperfeito, um treinado num subconjunto pequeno; o custo é atribuído pelo desenho experimental | §4.1, p. 6 | limite de escopo — nenhum custo monetário real é medido |

## Números que posso citar
- Datasets (Tab. 2, p. 6): Face 2.500 instâncias / 400 dimensões; Spambase
  4.601 / 57; Adult 4.147 / 48; VY-letter 1.550 / 16 — todos **binários**.
- Razões de custo entre oráculo confiável e imperfeito (Tab. 1, p. 6):
  1:3 a 1:5 no cenário relutante e 1:5 a 1:7 no falível — o artigo justifica a
  razão maior no falível: "receber um rótulo ruidoso deve ser penalizado mais
  do que não receber resposta alguma".
- Orçamento total B = 300 nos cenários 1 e 2; orçamento de agrupamento
  B_C ∈ {20, 30, 50} (Tab. 1, p. 6).
- Custo não uniforme (cenário 3, p. 5):
  $C_{\text{non-unif}}(x) = \dfrac{1 - \max_y P(y\mid x) - 1/|Y|}{1 - 1/|Y|}$
  — o oráculo cobra mais pela instância mais próxima da fronteira, isto é,
  **cobra pelo que a instância vale para o aprendiz**.

## Citações diretas (com página)
> "the oracle is assumed to be infallible (never wrong), indefatigable (always
> answers), individual (only one oracle), and insensitive to costs (always free
> or always charges the same). Proactive learning relaxes all four of these
> assumptions" (p. 1)

> "Rather than fixing the number of instances to sample, as in standard active
> learning, proactive learning fixes a maximum budget envelope since instances
> and oracles may have variable costs." (p. 3)

## O que esta obra NÃO sustenta
Registro explícito para o R5 não herdar atribuição indevida:
1. **Não fala de LLM.** É de 2008; os oráculos são classificadores simulados
   (C7). Citar como antecedente do custo por oráculo é correto; citar como
   evidência sobre oráculo-LLM, não.
2. **Não fala de texto curto nem de espaço amplo de classes.** As quatro bases
   são binárias e pequenas (C6) — o oposto do cenário da tese (714 classes,
   descrição de produto). Nada aqui mede o que acontece quando o espaço de
   rótulos cresce.
3. **Não mede custo real.** O custo é parâmetro do desenho, com razões fixadas
   à mão (Tab. 1). A tese, essa sim, mede custo em dinheiro por mil rótulos.
4. **Não trata custo e falibilidade juntos.** Cada cenário isola uma
   propriedade (C4); o próprio artigo diz que a extensão para mais de dois
   oráculos "é direta" (nota 1, p. 3) — mas não a executa.

## Crítica / limitações (minha leitura)
A força da obra é a formulação, não a evidência: a equação (2) é o que fica, e
ela é anterior a qualquer resultado. A evidência empírica é o elo fraco —
oráculos simulados, custos por decreto, quatro bases binárias pequenas — e por
isso a obra deve entrar na tese sustentando **o problema e a formulação**, não
um resultado. A separação de cenários (uma propriedade por vez) é
metodologicamente limpa e, ao mesmo tempo, a distância exata entre 2008 e o
caso do FALCO: uma LLM barata é falível **e** barata **e** incansável ao mesmo
tempo, e é a combinação que produz a decisão difícil.

## Ideias que gera para a tese
1. **Orçamento como unidade, não contagem de rótulos** (C3): a comparação
   FALCO × baselines por custo já está no espírito de 2008; vale dizer isso
   explicitamente, porque dá antecedente formal a uma escolha que hoje parece
   só pragmática.
2. **A quarta suposição tem dono agora.** Sugestão de local para o principal
   (superfície dele; ancoro por trecho, não por linha — ver meu aviso 1935):
   Cap. 2, na frase que hoje termina "…roteamento entre anotadores de custos
   distintos \cite{Sheng2008, Snow2008, Donmez2009, Yan2011}". É o ponto exato
   do "custo distinto"; hoje as quatro chaves citadas cobrem repetição,
   qualidade e roteamento — nenhuma delas formula o custo por oráculo.
3. **Nota de honestidade que a tese pode fazer**: o FALCO usa uma progressão de
   fases fixa, e não a otimização conjunta de (2). Dizer isso citando 2008
   transforma uma limitação em posição consciente.
