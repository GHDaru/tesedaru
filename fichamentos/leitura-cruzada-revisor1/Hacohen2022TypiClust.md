---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Hacohen2022TypiClust
title: "Active Learning on a Budget: Opposite Strategies Suit High and Low Budgets"
authors: ["Hacohen, Guy", "Dekel, Avihu", "Weinshall, Daphna"]
year: 2022
venue: "Proceedings of the 39th International Conference on Machine Learning (ICML), PMLR 162"
doi: ""                      # PMLR não expõe DOI; URL oficial: https://proceedings.mlr.press/v162/hacohen22a.html
pdf: referencias-pdf/Hacohen2022TypiClust.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P1, P2]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: [amostragem-por-tipicidade]   # TypiClust: tipicidade (densidade k-NN) + cluster
uses_methods: [aprendizado-ativo, pool-based, cold-start, amostragem-por-incerteza,
               entropia, menor-margem, clusterizacao, aprendizado-auto-supervisionado]
datasets: [cifar-10, cifar-100, tinyimagenet, imagenet]
metrics: [acuracia]
tasks: [classificacao-de-imagens]
models: [resnet-18, simclr]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: [Sener2018, Gal2017, Kirsch2019, Ash2020]
contradicts: []
builds_on: [Attenberg2010]

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: fundamenta
    target: DRI-SL
    note: "Mesmo princípio do DRI-SL: no cold start (L0=∅), selecionar exemplos
           TÍPICOS (alta densidade em espaço semântico) com diversidade forçada por
           clusterização, sem rótulos e sem modelo treinado. Valida teoricamente a
           escolha de densidade+diversidade contra incerteza no orçamento baixo."
  - type: fundamenta
    target: FALCO
    note: "A transição de fase (tipicidade no orçamento baixo → incerteza no alto)
           justifica a arquitetura em fases do FALCO: DRI-SL no início, estratégias
           de incerteza quando o classificador já está informativo."
  - type: complementa
    target: FALCO
    note: "Mostra (Fig. 2b e Fig. 7b, distância TV) que a seleção por tipicidade+cluster
           produz conjunto aproximadamente balanceado por classe SEM acesso a rótulos
           — argumento direto para o desbalanceamento de 714 classes do FALCO."
---

# Active Learning on a Budget: Opposite Strategies Suit High and Low Budgets (TypiClust)

## Resumo (5-8 linhas, com as MINHAS palavras)

Analisa a relação entre tamanho do orçamento de rotulagem e a estratégia de consulta
adequada, mostrando teórica e empiricamente um fenômeno tipo "transição de fase":
com orçamento baixo convém consultar exemplos típicos (alta densidade), com orçamento
alto convém consultar exemplos atípicos/incertos. Disso deriva o TypiClust: aprende
representação auto-supervisionada do pool não rotulado, particiona em |L|+B clusters
e seleciona o exemplo mais típico (inverso da distância média aos K=20 vizinhos) de
cada um dos B maiores clusters não cobertos. No regime de baixo orçamento supera
todas as estratégias clássicas (que empatam ou perdem para o aleatório) e dá ganho
grande em semi-supervisão (93,2% no CIFAR-10 com 10 rótulos).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Regimes de baixo e alto orçamento exigem estratégias OPOSTAS: típicos no baixo, incertos/atípicos no alto (transição de fase) | Abstract; §2 (Thm. 1–3); Fig. 1, p. 1 (PMLR 8175) | Cap. 2 fundamentação do cold start; justifica fases do FALCO |
| C2 | No orçamento baixo, estratégias clássicas de AL (CoreSet, BALD, BADGE, entropia, margem, DBAL) empatam com aleatório ou pioram | §4.2.1, Fig. 4, p. 5–6 | Cap. 2; motivação do DRI-SL (P2) |
| C3 | Tipicidade = inverso da distância média aos K vizinhos em espaço auto-supervisionado; diversidade via K-means com |L|+B clusters, 1 exemplo por cluster não coberto | §3.1 Eq. (4); §3.2 Passos 1–3; Alg. 1, p. 4–5 | Cap. 2/3: paralelo formal com o DRI-SL (densidade semântica + cobertura) |
| C4 | A seleção típica+cluster gera conjunto rotulado aproximadamente balanceado por classe sem usar rótulos (menor distância TV à distribuição real) | Fig. 2b (legenda), p. 2; §4.3.2, Fig. 7b, p. 7 | Cap. 5 discussão: balanceamento emergente do L0 sob 714 classes |
| C5 | Ablação: tipicidade sem cluster e cluster sem tipicidade são ambos insuficientes — os dois componentes são cruciais | §4.3.3, Fig. 7c, p. 7 | Cap. 5: defende os dois componentes do DRI-SL |
| C6 | Cold start explicado pela má estimativa de incerteza de redes treinadas com poucos rótulos | §1, p. 1–2 (citando Nguyen et al. 2015; Gal & Ghahramani 2016) | Cap. 2 revisão de cold start |

## Números que posso citar
- CIFAR-10 semi-supervisionado (FlexMatch), 10 rótulos selecionados por TypiClust:
  **93,2% de acurácia, +39,4 p.p. sobre seleção aleatória** (Abstract; §4.2.3, Fig. 6a).
- Regime avaliado como "baixo orçamento": **1–10 exemplos rotulados por classe por
  rodada**; orçamentos B = M ou B = 5M (M = nº de classes) com L0 = ∅ (§4.2, §4.2.1).
- Tipicidade calculada com **K = 20** vizinhos mais próximos (nota 1, §3.1); outros
  valores dão resultados similares.
- Semi-supervisão avaliada no regime extremo com **0,02%–1% dos dados rotulados**
  (§4.2.3).
- Variantes: TPC(DC) usa SCAN; TPC(RP) usa SimCLR (CIFAR/Tiny) ou DINO (ImageNet)
  + K-means (§3.2).

## Citações diretas (com página)
> "typical examples are best queried when the budget is low, while unrepresentative
> examples are best queried when the budget is large" (Abstract, p. 1 / PMLR 8175)

> "Note that the ensuing labeled set is approximately class-balanced, even though
> the queries are chosen without access to class labels." (legenda da Fig. 2, p. 2 /
> PMLR 8176)

## Crítica / limitações (minha leitura)
- Toda a validação é em imagens (CIFAR, ImageNet, SVHN ausente); nada em texto,
  nada em português — a transferência para descrições curtas de varejo é hipótese
  que o FALCO testa, não resultado deles.
- Datasets quase balanceados e com poucas classes (10–200); não há evidência no
  regime de 714 classes com cauda longa — o balanceamento emergente (C4) pode não
  se sustentar quando classes raras têm densidade baixíssima.
- Exige treinar representação auto-supervisionada sobre o pool (SimCLR/DINO), custo
  que o paper não contabiliza no orçamento; DRI-SL usa embeddings prontos.
- A fronteira entre "orçamento baixo" e "alto" não é operacionalizada — o ponto de
  troca de estratégia fica empírico e dependente do dataset.

## Ideias que gera para a tese
- Citar a transição de fase como fundamento teórico para o desenho em fases do
  FALCO (DRI-SL no cold start → incerteza depois) no Cap. 2.
- Usar a distância TV entre distribuição do L0 e distribuição real de classes
  (§4.3.2) como métrica auxiliar para avaliar o L0 do DRI-SL vs AG/aleatório (P1/P2).
- Replicar a ablação C5 (densidade sem cluster / cluster sem densidade) para os
  componentes do DRI-SL (cluster semântico vs variedade lexical).
