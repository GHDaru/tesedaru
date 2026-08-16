---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Sener2018
title: "Active Learning for Convolutional Neural Networks: A Core-Set Approach"
authors: ["Sener, Ozan", "Savarese, Silvio"]
year: 2018
venue: "International Conference on Learning Representations (ICLR)"
doi: ""                      # OpenReview: https://openreview.net/forum?id=H1aIuk-RW ; arXiv:1708.00489
pdf: referencias-pdf/Sener2018.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P1, P2]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: [core-set, k-center-greedy]
uses_methods: [aprendizado-ativo, pool-based, rotulagem-em-lote, entropia,
               amostragem-por-incerteza, clusterizacao]
datasets: [cifar-10, cifar-100, svhn]
metrics: [acuracia]
tasks: [classificacao-de-imagens]
models: [vgg-16]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: [Gal2017]
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: fundamenta
    target: DRI-SL
    note: "Formaliza a seleção em lote SEM rótulos como problema de cobertura
           geométrica (k-Center) no espaço de características — é o fundamento da
           família 'representatividade/diversidade' da qual o cluster semântico do
           DRI-SL descende."
  - type: motiva
    target: FALCO
    note: "Mostra que heurísticas de incerteza ponto-a-ponto degradam na aquisição
           em lote por correlação entre amostras — o FALCO rotula em lote com LLM,
           logo precisa de seleção que gerencie redundância, não só incerteza."
  - type: ameaca
    target: DRI-SL
    note: "O próprio bound do core-set cresce com o número de classes e o método
           perde eficácia já no CIFAR-100 (100 classes); com as 714 classes do
           FALCO, cobertura geométrica pura tende a degradar — limite que o DRI-SL
           precisa discutir (e que a variedade lexical tenta mitigar)."
---

# Active Learning for Convolutional Neural Networks: A Core-Set Approach

## Resumo (5-8 linhas, com as MINHAS palavras)

Reformula o aprendizado ativo em lote para CNNs como seleção de core-set: escolher o
subconjunto de pontos tal que o modelo treinado nele seja competitivo no restante dos
dados. Como os rótulos do pool não estão disponíveis, deriva (Teorema 1) um limite
superior para a perda média que depende só da geometria: o raio δ de cobertura do
conjunto selecionado. Minimizar esse limite equivale ao problema k-Center, resolvido
por um algoritmo guloso 2-aproximado (k-Center-Greedy) e refinado por um programa
inteiro misto robusto a outliers. Nos experimentos (CIFAR-10/100, SVHN, VGG-16),
supera aleatório, incerteza (softmax), DBAL, BMDR, CEAL e k-Median, especialmente no
cenário fracamente supervisionado; observa que o argumento das heurísticas clássicas
falha porque a aquisição em lote gera amostras correlacionadas.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Heurísticas clássicas de AL (incerteza etc.) são ineficazes para CNNs em regime de LOTE, por correlação entre as amostras adquiridas | Abstract; §1, p. 1–2 | Cap. 2 fundamentação; motiva rotulagem-em-lote do FALCO |
| C2 | AL sem rótulos pode ser formulado como core-set: perda no pool limitada pelo raio de cobertura δ do conjunto selecionado (mais termo O(1/√n)) | §4.2, Thm. 1, p. 5; Fig. 1, p. 5 | Cap. 2: base teórica da seleção por diversidade/representatividade |
| C3 | Minimizar o bound equivale ao problema k-Center; o guloso dá solução 2-OPT, refinável por MIP robusto (outliers Ξ) | §4.3, Alg. 1 e 2, p. 6; Eq. (6) | Cap. 2 descrição do baseline core-set |
| C4 | O método é menos eficaz no CIFAR-100 que no CIFAR-10/SVHN porque o bound escala com o número de classes | §5, p. 8 | Cap. 5 discussão: limite de core-set com 714 classes |
| C5 | Ganho é maior no cenário fracamente supervisionado, pois espaços de características melhores dão geometria mais fiel — método puramente geométrico depende da qualidade do embedding | §5, p. 8 | Cap. 5: dependência do DRI-SL da qualidade do embedding |

## Números que posso citar
- Algoritmo guloso k-Center-Greedy é **2-aproximado** (2-OPT); o MIP busca melhorar
  entre OPT e 2·OPT, com limite de outliers **Ξ = 1e-4·n** (§4.3, p. 6–7).
- Experimentos: CIFAR-10 (10 classes), CIFAR-100 (100 classes), SVHN; 5 inicializações
  aleatórias do pool inicial; VGG-16 como classificador (§5, p. 7; App.).
- Supera todos os baselines (Random, melhor incerteza empírica, incerteza-oráculo,
  DBAL, BMDR, CEAL, k-Median) em todos os experimentos; margem maior no
  fracamente supervisionado (Figs. 3–4, p. 8).

## Citações diretas (com página)
> "we define the problem of active learning as core-set selection, i.e. choosing set
> of points such that a model learned over the selected subset is competitive for the
> remaining data points" (Abstract, p. 1)

> "We also observed that our algorithm is less effective in CIFAR-100 when compared
> with CIFAR-10 and SVHN. [...] Our bound over the core-set loss scales with the
> number of classes, hence it is better to have fewer classes." (§5, p. 8)

## Crítica / limitações (minha leitura)
- Assume erro de treino zero no subconjunto e perda Lipschitz — razoável para CNNs
  superparametrizadas, mas o próprio bound fica frouxo com muitas classes (C4), o
  caso exatamente oposto ao do FALCO (714 classes).
- Distâncias L2 em espaço de ativações de alta dimensão sofrem de concentração de
  distâncias; trabalhos posteriores (inclusive Hacohen2022TypiClust e Yu2023Patron)
  mostram core-set perdendo até para aleatório no orçamento baixo/cold start.
- Precisa de um modelo treinado para extrair o espaço de características — no
  cold start estrito (L0 = ∅) o método nem se aplica sem embedding externo.
- Só imagens, datasets balanceados; nenhuma consideração de desbalanceamento.
- O MIP com Gurobi não escala trivialmente para pools grandes; na prática
  usa-se quase sempre só a versão gulosa.

## Ideias que gera para a tese
- Usar C1 (correlação em lote) para justificar por que o FALCO não usa incerteza
  pura na fase de aquisição em lote com oráculo LLM.
- Citar C4 explicitamente na discussão (Cap. 5) ao explicar por que baselines de
  diversidade geométrica pura não são adequados a 714 classes.
- k-Center-Greedy sobre embeddings do BERTimbau é um baseline barato e defensável
  para comparação com DRI-SL em trabalho futuro.
