---
id: Sener2018
title: "Active Learning for Convolutional Neural Networks: A Core-Set Approach"
authors: ["Sener, Ozan", "Savarese, Silvio"]
year: 2018
venue: "ICLR 2018"
doi: ""
pdf: referencias-pdf/Sener2018.pdf
paper_type: metodo
pillars: [P2]
status: fichado
proposes: [core-set-selection, k-center-greedy, robust-k-center]
uses_methods: [aprendizado-ativo, pool-based, rotulagem-em-lote,
               selecao-por-diversidade]
datasets: [cifar-10, cifar-100, svhn]
metrics: [acuracia]
tasks: [classificacao-de-imagens]
models: [vgg-16]
extends: []
compares_with: [Gal2016]
contradicts: []
builds_on: []
falco_relation:
  - type: compara
    target: DRI-SL
    note: "Clássico da seleção por diversidade geométrica: AL em lote como
           cobertura minimax (k-Center) no espaço de ativações do próprio
           modelo. Três diferenças que o confronto do Cap. 2 explora: (i)
           coreset NÃO é cold start — a distância usa ativações de uma rede já
           treinada no pool inicial rotulado, enquanto o DRI-SL parte de
           rótulo zero; (ii) o próprio bound dos autores escala com o número de
           classes (pior com muitas classes — nós temos 714); (iii) cobertura
           minimax privilegia pontos extremos/outliers, frágil em texto curto
           esparso e ruidoso, enquanto o DRI-SL aloca por densidade
           proporcional + novidade lexical. Em orçamento baixo, coreset empata
           com random (Hacohen2022TypiClust, Fig. 4) e fica abaixo até de
           random em cold start textual (Yu2023Patron, Tab. 1)."
---

# Active Learning for Convolutional Neural Networks: A Core-Set Approach

## Resumo (5-8 linhas, com as MINHAS palavras)
Mostra empiricamente que heurísticas clássicas de incerteza são ineficazes para
CNNs no cenário de lote (consultas correlacionadas) e reformula o AL em lote
como seleção de core-set: escolher o subconjunto tal que o modelo nele treinado
seja competitivo no restante do pool. O Teorema 1 limita a "perda de core-set"
pelo raio de cobertura δ do subconjunto (mais um termo O(√(1/n))), sem depender
do número de rótulos; minimizar o raio equivale ao problema k-Center (NP-difícil),
resolvido por guloso 2-OPT (k-Center-Greedy) e refinado por um MIP robusto a
outliers. A distância é a l2 entre ativações da última camada densa de uma
VGG-16 treinada. Supera as baselines (incerteza, DBAL, BMDR, CEAL, k-Median)
em CIFAR-10/100 e SVHN, com margem maior no regime fracamente supervisionado.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Heurísticas de incerteza são ineficazes para CNNs em lote: amostras correlacionadas; random as supera | Abstract; §1; §5 e Figs. 3–4, pp. 7–8 | Cap. 2: linhagem do argumento anti-US em lote (que o FALCO herda no cold start) |
| C2 | AL em lote ≡ seleção de core-set; perda de core-set limitada pelo raio de cobertura δ, independente do nº de rótulos | §4.1–4.2, Eq. 3, Thm. 1, pp. 4–5 | Cap. 2: formalização canônica da seleção por diversidade/cobertura |
| C3 | Minimizar o bound ≡ k-Center (minimax facility location), NP-difícil; guloso dá 2-OPT; MIP robusto com cota de outliers Ξ | §4.3, Alg. 1–2, Eq. 5–6, pp. 6–7 | Contraste com DRI-SL: cota proporcional por cluster ≠ cobertura minimax |
| C4 | O bound escala com o nº de classes: o método é menos eficaz em CIFAR-100 que em CIFAR-10/SVHN | §5, p. 8 ("it is better to have fewer classes") | Confronto direto: com 714 classes, a garantia do coreset degrada — argumento pró-DRI-SL |
| C5 | Clustering puro (k-Median/k-Medoids) também não é eficaz: os centros já são bem cobertos por amostra iid; falha em amostrar as caudas | §5, p. 8 | Antecipa a crítica "por que k-médias sozinho não basta" — DRI-SL responde com a etapa lexical |
| C6 | A distância usa ativações da última camada densa do modelo treinado (VGG-16) | §4.4, p. 7 | Mostra que coreset pressupõe modelo treinado — não resolve cold start puro |

## Números que posso citar
- Runtime para b=5k consultas com \|s0\|=10k: greedy 2 s; MIP total 244 s;
  total 360 s (Tab. 1, p. 9; Intel i7-5930K, 64 GB).
- Experimentos com pool inicial UNIFORME e lotes grandes (frações de 10% do
  dataset por rodada nas Figs. 3–4) — regime de orçamento ALTO, não baixo
  (Figs. 3–4, pp. 8).
- Robustez a outliers: cota Ξ = 1e-4·n (§4.4, p. 7).

## Citações diretas (com página)
> "many of the active learning heuristics in the literature are not effective
> when applied to CNNs in batch setting" (Abstract, p. 1)

> "Our bound over the core-set loss scales with the number of classes, hence
> it is better to have fewer classes" (§5, p. 8)

## Crítica / limitações (minha leitura)
- Não é cold start: precisa de pool inicial rotulado uniforme + rede treinada
  para obter o espaço de ativações onde a geometria é medida. No rótulo-zero do
  P2, coreset só roda sobre um embedding genérico — configuração que TypiClust
  e PATRON testaram e na qual ele empata com ou perde de random.
- Regime experimental de orçamento alto (frações de 10% do dataset); nada diz
  sobre o regime 100..5000 do nosso envelope.
- C4 é a limitação mais grave para o nosso caso: garantia degrada com C classes
  (714 no domínio de varejo).
- Cobertura minimax é atraída por outliers (o MIP mitiga, mas com hiperparâmetro
  Ξ); em texto curto ruidoso (títulos truncados, códigos), os "pontos extremos"
  tendem a ser lixo, não informação.
- Só imagens/CNNs; distância l2 em ativações não transfere diretamente para
  TF-IDF esparso.

## Ideias que gera para a tese
- Par com Hacohen2022TypiClust no confronto do R6 item 11: coreset é o
  representante canônico de diversidade minimax; DRI-SL difere em (a) alocação
  proporcional à densidade (não minimax), (b) novidade lexical intragrupo,
  (c) rótulo-zero de verdade, (d) sem dependência do nº de classes.
- C1 reforça, por linhagem independente (2018, visão), o mesmo fenômeno que
  Hacohen 2022 teoriza e que motiva o FALCO a não usar US no início.
- C5 serve para responder à banca "por que não só k-médias?": até os autores do
  coreset mostram que clustering puro falha nas caudas.

## Nota de duplicata no referencias.bib (reportar, não editar)
`Sener2018` (@inproceedings, ICLR 2018, url OpenReview H1aIuk-RW, linha 573) e
`Sener2017` (@misc, arXiv 1708.00489, linha 2171) são o MESMO trabalho. Este
fichamento usa **Sener2018** (versão publicada; venue correto). Dedupe fica
para o ciclo próprio.
