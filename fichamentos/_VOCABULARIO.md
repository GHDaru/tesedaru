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
classificacao-de-texto  <!-- Xiao2023FreeAL -->
regressao  <!-- Farquhar2021Bias -->
classificacao-de-imagens  <!-- Hacohen2022TypiClust -->

### Modelos (fichar-vizinhos)
gpt-2, gpt-j, gpt-neox, opt, sentence-bert  <!-- Margatina2023 -->
biomed-roberta-base, gpt-3.5-turbo, roberta-base  <!-- Xiao2023FreeAL -->
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
