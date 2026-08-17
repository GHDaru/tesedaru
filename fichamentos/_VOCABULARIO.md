# Vocabulário controlado do grafo de conhecimento

IDs de paper = chave BibTeX. Entidades abaixo usam SEMPRE o nome canônico.

## Métodos/conceitos canônicos
aprendizado-ativo, pool-based, cold-start, amostragem-por-incerteza, entropia,
menor-confianca, menor-margem, query-by-committee, llm-como-oraculo,
llm-como-seletor, saida-estruturada, prompt-caching, rotulagem-em-lote,
destilacao-ativa, fine-tuning, DRI-SL, FALCO, LCE, algoritmo-genetico,
mixture-of-llms, few-shot, zero-shot

## Datasets canônicos
retail-product-description-ptbr, agnews, trec, imdb, ...

## Métricas canônicas
acuracia, macro-f1, lce, custo-por-rotulo, ic-wilson, mcnemar, wilcoxon

## Relações (arestas)
| Aresta | Semântica |
|---|---|
| proposes | paper → método/métrica que introduz |
| uses_methods / datasets / metrics / models | paper → entidade empregada |
| extends | paper → paper que ele estende |
| compares_with | paper ↔ paper comparado empiricamente |
| contradicts | paper → paper/claim que contesta |
| builds_on | paper → fundamento conceitual |
| falco_relation.compara/fundamenta/motiva/ameaca/complementa | paper → nó da tese |

## Pipeline para o KG
fichamentos/*.md → (script: front-matter → triplas) → JSON-LD/CSV de arestas →
Neo4j ou RDF. O corpo markdown NÃO entra no grafo; claims da tabela entram como
nós `Claim` ligados por `asserts` (paper→claim) e `evidences` (claim→localização).

## Adições da rodada fichar-vizinhos (2026-08-16)

Termos entrados pelos fichamentos dos 11 vizinhos (parecer R6, Bloco C); mesmo commit do fichamento que os introduz.

### Tarefas (fichar-vizinhos)
classificacao-de-texto  <!-- FreeAL2023 -->
regressao  <!-- Farquhar2021Bias -->
classificacao-de-imagens  <!-- Hacohen2022TypiClust -->

### Modelos (fichar-vizinhos)
gpt-2, gpt-j, gpt-neox, opt, sentence-bert  <!-- Margatina2023 -->
gpt-4o  <!-- Zhang2025 -->
biomed-roberta-base, gpt-3.5-turbo, roberta-base  <!-- FreeAL2023 -->
resnet101, resnet18  <!-- Bengar2022ClassBalanced -->
distilroberta, kimcnn, svm  <!-- Schroder2022Uncertainty -->
processo-gaussiano, random-forest, resnet, wideresnet  <!-- Kossen2021ActiveTesting -->
rede-neural-bayesiana, regressao-linear  <!-- Farquhar2021Bias -->
simcse  <!-- Yu2023Patron -->
vgg-16  <!-- Sener2018 -->
dino, flexmatch, scan, simclr  <!-- Hacohen2022TypiClust -->
gpt-3-davinci, pegasus-large, roberta-large  <!-- Wang2021GPT3Labeling -->
gpt-3, gpt-4  <!-- Zhang2023LLMaAA (gpt-3 = família, quando o paper não fixa a variante) -->
bert  <!-- Zhang2023LLMaAA, Schroder2022Uncertainty (família; use a variante exata quando o paper a fixar) -->

### Métodos (fichar-vizinhos)
aprendizado-em-contexto, selecao-de-demonstracoes, selecao-por-similaridade  <!-- Margatina2023 -->
auto-supervisao, k-means, selecao-por-diversidade, tipicidade, transicao-de-fase-de-orcamento, typiclust  <!-- Hacohen2022TypiClust -->
aprendizado-ativo-balanceado-por-classe, otimizacao-binaria  <!-- Bengar2022ClassBalanced -->
teste-ativo  <!-- Kossen2021ActiveTesting -->
estimador-lure, estimador-pure  <!-- Farquhar2021Bias -->
partition-then-rewrite, patron, propagacao-de-incerteza  <!-- Yu2023Patron -->
core-set-selection, k-center-greedy, robust-k-center  <!-- Sener2018 -->

### Datasets (fichar-vizinhos)
crossfit  <!-- Margatina2023 -->
glue, jigsaw-toxic, sst-2  <!-- Bayer2024ActiveLLM, Zhang2025 -->
cifar-10, cifar-100, imagenet-subconjuntos, tiny-imagenet  <!-- Hacohen2022TypiClust -->
customer-reviews, movie-reviews, subjectivity  <!-- Schroder2022Uncertainty -->
fashion-mnist, mnist  <!-- Farquhar2021Bias -->
dbpedia, yahoo-answers, yelp-full  <!-- Yu2023Patron -->
svhn  <!-- Sener2018 -->

### Métricas (fichar-vizinhos)
perplexidade  <!-- Margatina2023 -->
auc-curva-de-aprendizado  <!-- Schroder2022Uncertainty -->
l1-score-balanceamento  <!-- Bengar2022ClassBalanced -->
f1  <!-- Yu2023Patron: o paper reporta "F1 score" sem especificar macro/micro; não normalizar para macro-f1 -->

## Adições da rodada R3 do t2 — pós-2022 do Cap. 2 (2026-08-17)

Termos entrados pelos fichamentos dos artigos pós-2022 citados no bloco t2 do
Cap. 2; mesmo commit do fichamento que os introduz.

### Métodos (R3 t2)
anotacao-hibrida-humano-llm, confidence-scoring, proxy-validation-set, roteamento-por-limiar-de-confianca  <!-- Rouzegar2024 (os dois primeiros já em uso por Rouzegar2024Thesis, aqui registrados) -->

### Datasets (R3 t2)
fake-news, movie-genres  <!-- Rouzegar2024: nomes como o artigo os chama; "Movie Genres" é tarefa de 4 classes apesar de o resumo dizer multirrótulo -->

### Modelos (R3 t2)
gpt-3.5, regressao-logistica  <!-- Rouzegar2024: gpt-3.5 já em uso por Rouzegar2024Thesis, aqui registrado; a regressão logística é o classificador que gera a incerteza -->

### Métodos (R3 t2 — rótulo extremo)
alps, cvirs, discriminative-active-learning, amostragem-por-subpalavras, selecao-aleatoria, limiar-variavel-multirrotulo, cnn-como-cabeca-de-classificacao  <!-- Fromme2022 -->

### Tarefas (R3 t2)
classificacao-multirrotulo-extrema  <!-- Fromme2022: XMTC, centenas a milhões de classes com vários rótulos por texto -->

### Datasets (R3 t2 — rótulo extremo)
eurlex, arxiv-xmtc, nyt, rcv1, yelp-xmtc, toxic  <!-- Fromme2022: compilados PELOS AUTORES a partir de tarefas hierárquicas; yelp-xmtc (580 classes) NÃO é o yelp-full (5 estrelas) de Yu2023Patron -->

### Métricas (R3 t2)
micro-f1  <!-- Fromme2022: reportado lado a lado com macro-f1; não são intercambiáveis em rótulo desbalanceado -->

### Modelos (R3 t2 — rótulo extremo)
bert-base-uncased  <!-- Fromme2022: variante exata; usar em vez do genérico bert quando o paper a fixa -->
## Adições da rodada do ruído estruturado (2026-08-17)

Termos entrados pelo fichamento do survey de ruído de rótulo (tarefa 20260817-0215).

### Métodos (ruído de rótulo)
ruido-simetrico, ruido-assimetrico, ruido-de-par, ruido-dependente-da-instancia, matriz-de-transicao-de-ruido, efeito-de-memorizacao, small-loss-trick, selecao-de-amostras, correcao-de-perda, co-teaching, aprendizado-multi-rodada  <!-- Song2023NoisyLabels: a taxonomia simetrico/assimetrico/dependente-da-instancia e a que a tese deve usar para nomear o ruido do oraculo LLM (o nosso e assimetrico) -->

### Datasets (ruído de rótulo)
clothing1m, animal-10n, food-101n, webvision, cifar-10n, cifar-100n, imagenet  <!-- Song2023NoisyLabels: conjuntos com ruido REAL (taxas de 8% a 40%), distintos dos conjuntos limpos corrompidos artificialmente -->

### Métricas (ruído de rótulo)
precisao-de-rotulo, revocacao-de-rotulo  <!-- Song2023NoisyLabels: metricas especificas da familia "selecao de amostras" -->

### Modelos (ruído de rótulo)
wideresnet  <!-- Song2023NoisyLabels: ja registrado por Kossen2021ActiveTesting; repetido aqui so como referencia cruzada -->

### Métodos (R3 t2 — federado)
aprendizado-ativo-federado, entropia-de-ensemble, aprendizado-federado  <!-- Deng2023fedal: o comitê é o par modelo local + modelo global, que já existem no laço federado — incerteza sem custo extra -->

### Datasets (R3 t2 — federado)
ham10k, msk-isic  <!-- Deng2023fedal: 10.490 imagens dermatoscópicas repartidas em 4 hospitais com distribuição não-IID -->

### Métricas (R3 t2 — federado)
auc  <!-- Deng2023fedal: reportada ao lado de micro-f1 e macro-f1 -->
