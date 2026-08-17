---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Rouzegar2024
title: "Enhancing Text Classification through LLM-Driven Active Learning and Human Annotation"
authors: ["Rouzegar, Hamidreza", "Makrehchi, Masoud"]
year: 2024
venue: "arXiv:2406.12114v1 [cs.CL], 17 jun. 2024 (6 pp. + apêndice)"
doi: "10.48550/arXiv.2406.12114"
pdf: referencias-pdf/Rouzegar2024.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P3, P4]
status: fichado

# ===== ENTIDADES =====
proposes: [anotacao-hibrida-humano-llm, proxy-validation-set, roteamento-por-limiar-de-confianca]
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, menor-confianca, llm-como-oraculo, confidence-scoring, few-shot, zero-shot]
datasets: [imdb, fake-news, movie-genres]
metrics: [f1, custo-por-rotulo]
tasks: [classificacao-de-texto]
models: [gpt-3.5, regressao-logistica]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994, Seung1992, Settles2009, Gilardi2023, Yu2023Patron]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: compara
    target: FALCO
    note: "Versão de conferência (6 pp.) da dissertação já fichada em
           Rouzegar2024Thesis — é ESTA que o texto da tese cita (5 ocorrências
           no Cap. 2 e 1 no Cap. 6). Mesmo problema do FALCO (custo de rótulo
           em AL com oráculo LLM), topologia diferente: roteia por CONFIANÇA
           entre humano e LLM dentro da mesma iteração, enquanto o FALCO faz o
           oráculo EVOLUIR entre fases. Espaço de rótulos de 2 a 4 classes
           contra as 621 do FALCO."
  - type: fundamenta
    target: DRI-SL
    note: "Fornece a medida externa que faltava para o ruído do oráculo LLM:
           11% de anotações incorretas em tarefa binária e 33% em tarefa de
           4 classes (§5). É evidência publicada de que a taxa de erro cresce
           com o número de classes — exatamente a premissa que motiva o
           DRI-SL e a decomposição A−B do Cap. 5."
---

# Enhancing Text Classification through LLM-Driven Active Learning and Human Annotation

## Resumo (5-8 linhas, com as MINHAS palavras)
Propõe um pipeline de aprendizado ativo em que a anotação é dividida entre o
GPT-3.5 e um anotador humano segundo a **confiança auto-reportada pelo LLM**:
acima do limiar vale o rótulo da máquina, abaixo dele o item vai para o humano
(ou para reanotação em *few-shot*). A seleção é a clássica amostragem por
incerteza sobre as probabilidades de uma regressão logística; a novidade de
processo é o **proxy-validation set**, um subconjunto que espelha a distribuição
do pool e permite estimar o desempenho a cada iteração sem gastar rótulos de
teste. Avalia em três conjuntos públicos (IMDB, Fake News, Movie Genres),
reportando F1 e custo em dólares lado a lado. A conclusão é de compromisso:
com o limiar certo, chega-se perto da acurácia do humano por uma fração do
custo — mas o "limiar certo" muda de conjunto para conjunto.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A confiança auto-reportada do GPT-3.5 correlaciona-se com o erro de anotação: abaixo do limiar a taxa de erro chega a ~50% | §5 (Analysis and Results), parágrafo "The study also delved into the analysis of GPT-3.5's output confidence scores" | Cap. 2 §2.x (oráculo LLM): sustenta tratar confiança como medida de incerteza — e sustenta também a ressalva de calibração |
| C2 | A taxa de erro global do oráculo LLM cresce com o número de classes: 11% (IMDB, 2 classes), 27% (Fake News, 2 classes), 33% (Movie Genres, 4 classes) | §5, mesmo parágrafo | Cap. 5: referência externa para o ruído do oráculo medido no braço A−B; é o dado que projeta o problema para as 621 classes do FALCO |
| C3 | Todos os métodos de anotação superam amostragem aleatória de forma consistente na faixa de 2% a 52% de dados de treino | §5 + Figura 1 (Fake News) | Cap. 2: contraponto ao achado inverso de Wertz2022 em rótulo extremo — a vantagem sobre o aleatório depende do número de classes |
| C4 | O proxy-validation set estima o desempenho no pool sem consumir rótulos de teste | §3.2 (Proxy-Validation Set) | Cap. 3/Cap. 6: alternativa de validação sob orçamento; candidata a trabalho futuro |
| C5 | O limiar de confiança é ajustado por conjunto (70% no IMDB, 80% nos outros dois) para atingir de 10 a 15% do IMDB e do Movie Genres e ~4% do Fake News | §3.3 e §4 (Confidence Thresholds) | Cap. 2 e Cap. 6: evidência de que o roteamento por confiança tem hiperparâmetro dependente de domínio — custo escondido do método |

## Números que posso citar
Todos de tabelas com condições completas (Tabelas 1-3; custo em USD; "porção" =
fração dos dados usada em treino).

- **IMDB (Tab. 1, porção 50%)**: GPT only F1 **0,9629** a **US$ 2,30**;
  Human only F1 **0,9796** a **US$ 2.116,22**. Ou seja, **-1,7 ponto de F1 por
  ~1/920 do custo**.
- **IMDB (Tab. 1, porção 10%)**: GPT only F1 0,8201 / US$ 0,46 · Human only
  F1 0,8597 / US$ 423,24.
- **Fake News (Tab. 2, porção 50%)**: GPT only F1 0,9041 / US$ 7,66 ·
  GPT conf > 90 F1 **0,9871** / US$ 2.156,90 · Human only F1 0,9791 /
  US$ 7.045,11. Aqui o híbrido **supera** o humano puro.
- **Movie Genres (Tab. 3, porção 50%)**: GPT only F1 **0,4337** / US$ 4,05 ·
  Human only F1 **0,8443** / US$ 3.724,61. Com 4 classes o LLM sozinho perde
  **41 pontos** de F1 — o colapso que o IMDB binário esconde.
- **Erro de anotação do GPT-3.5 (§5)**: IMDB 11% global, subindo para ~50%
  abaixo de 70% de confiança; Movie Genres 33% global, ~50% abaixo de 80%;
  Fake News 27% global, ~50% abaixo de 80%.

## Citações diretas (com página)
> "In the IMDB dataset, 11% of the annotations were found to be incorrect
> overall. However, in instances where GPT-3.5's confidence was below 70%, the
> rate of incorrect annotations rose to nearly 50%." (§5, p. 5)

> "These findings suggest that the model's confidence score can be a reliable
> indicator of uncertainty and the likelihood of annotation errors." (§5, p. 5)

## Crítica / limitações (minha leitura)
- **Inconsistência interna sobre o Movie Genres**: o resumo o chama de
  "multi-label classification" e a §5 o descreve como "a more intricate
  four-class classification". Ao citar, descrever como tarefa de 4 classes
  (é o que as métricas da Tab. 3 comportam) e não afirmar multirrótulo.
- **F1 sem qualificação**: o artigo reporta "F1" sem dizer se é macro ou micro.
  Não normalizar para `macro-f1` na tese; citar como "F1" e explicitar a
  ambiguidade se o número for usado em comparação.
- **O custo humano é preço de tabela, não medição**: vem da lista de preços do
  Google AI Platform Data Labeling, não de anotadores contratados. Os fatores
  de ~920× no IMDB comparam um custo real de API com um custo hipotético de
  humano — a ordem de grandeza é defensável, o número exato não.
- **Classificador raso**: a seleção usa regressão logística, não o transformer.
  A incerteza medida é a de um modelo fraco; nada garante que a ordenação
  sobreviva a um classificador forte.
- **Limiar ajustado a posteriori** por inspeção dos dados (§3.3), sem conjunto
  de validação separado para essa escolha — otimismo embutido nos resultados.
- **Escala do rótulo**: 2 a 4 classes. O próprio artigo mostra a degradação de
  2 para 4 classes; extrapolar para 621 é o salto que o FALCO tem de justificar
  com dados próprios, não por herança.

## Ideias que gera para a tese
- **Curva erro-do-oráculo × número de classes**: juntar os três pontos deste
  artigo (2 → 11%, 2 → 27%, 4 → 33%) com o nosso ponto em 621 classes vira
  uma figura de motivação do Cap. 1/2, e transforma "LLM erra mais com muitas
  classes" de intuição em série de dados citável.
- **Contraste C3 × Wertz2022**: aqui todos os métodos batem o aleatório
  (2-4 classes); em rótulo extremo (100-739 classes) nenhuma estratégia bate o
  aleatório de forma consistente. Os dois achados juntos delimitam a região em
  que a seleção ativa compensa — argumento direto para a discussão do Cap. 5.
- **Distinguir as duas entradas de Rouzegar**: `Rouzegar2024` (este, arXiv,
  6 pp., com Makrehchi) é a obra citada na tese; `Rouzegar2024Thesis` (99 pp.,
  Ontario Tech) a estende com o critério de parada PICR e o *role-based
  prompting*. Se a tese quiser citar o PICR, tem de citar a dissertação —
  o PICR **não** aparece nesta versão.
