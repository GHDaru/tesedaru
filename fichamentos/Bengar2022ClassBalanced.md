---
id: Bengar2022ClassBalanced
title: "Class-Balanced Active Learning for Image Classification"
authors: ["Zolfaghari Bengar, Javad", "van de Weijer, Joost", "Lopez Fuentes, Laura", "Raducanu, Bogdan"]
year: 2022
venue: "IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2022), pp. 1536–1545"
doi: "10.1109/WACV51458.2022.00376"
pdf: referencias-pdf/Bengar2022ClassBalanced.pdf
paper_type: metodo
pillars: [P2, P4]
status: fichado
proposes: [aprendizado-ativo-balanceado-por-classe]
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, entropia,
               rotulagem-em-lote, otimizacao-binaria]
datasets: [cifar-10, cifar-100, tiny-imagenet]
metrics: [acuracia, l1-score-balanceamento]
tasks: [classificacao-de-imagens]
models: [resnet18, resnet101]
extends: []
compares_with: []
contradicts: []
builds_on: [Settles2012]
falco_relation:
  - type: motiva
    target: FALCO
    note: "Demonstra (Fig. 2) que estratégias de AL — inclusive entropia, nosso
           baseline — reproduzem e AMPLIFICAM ao longo dos ciclos o
           desbalanceamento do pool. Com 714 classes em cauda longa, este é o
           risco central do nosso laço; citar no Cap.2 (lacuna) e na discussão
           dos resultados do P4."
  - type: complementa
    target: DRI-SL
    note: "Ataca o mesmo problema (seleção balanceada sem rótulos) em fase
           diferente: CBAL balanceia DURANTE os ciclos usando pseudo-rótulos do
           modelo; DRI-SL balanceia o L0 ANTES de existir modelo, via densidade
           semântica + variedade lexical. Par natural de confronto no Cap.2."
---

# Class-Balanced Active Learning for Image Classification

## Resumo (5-8 linhas)
Artigo de método (WACV 2022) que ataca o AL sob desbalanceamento de classes
(distribuição em cauda longa), cenário dominante no mundo real e quase ausente
dos benchmarks. Constata que os métodos de AL — informativos (entropia, BALD,
VAAL) e representativos (KCenterGreedy) — selecionam amostras que seguem a
distribuição desbalanceada do pool, e que esse viés cresce a cada ciclo. Propõe
CBAL: um problema de programação binária que soma ao critério de aquisição um
termo de balanceamento λ·‖Ω(c) − Pᵀz‖₁, no qual a distribuição de classes dos
não-rotulados é estimada pelas probabilidades preditas (pseudo-rótulos), sem
acesso a rótulos reais. Genérico (acopla a métodos informativos e
representativos, inclusive versão gulosa), melhora todos os baselines nos
datasets desbalanceados (CIFAR10/100, Tiny ImageNet com IF∈{0.1, 0.3}) e até nos
balanceados, ao neutralizar o viés amostral do próprio AL.
NOTA de identidade: obra distinta de "When Deep Learners Change Their Mind"
(CAIP 2021, arXiv:2107.14707), do mesmo primeiro autor, citada aqui como ref.
[4]; a fonte primária (CVF/IEEE, DOI conferido no Crossref) confirma que ESTE é
o paper de desbalanceamento — o correto para a tese.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL é estudado quase só em datasets balanceados, mas dados reais seguem cauda longa, o que degrada o processo | Abstract; §1, p. 1536 | Cap.2: lacuna "AL × desbalanceamento"; espelha nossas 714 classes em cauda longa |
| C2 | Amostras selecionadas por AL (informativo E representativo) seguem a distribuição desbalanceada do pool, e o desbalanceamento da seleção CRESCE ao longo dos ciclos | Fig. 2 e §3.2, p. 1538–1539 (CIFAR10, IF=0.3) | Cap.5/Cap.6: risco estrutural do nosso laço com entropia; motiva monitorar distribuição de classes por fase |
| C3 | Balanceamento pode ser imposto sem rótulos, estimando a distribuição de classes pelas probabilidades preditas e resolvendo um problema de programação binária (relaxação LP + branch-and-bound) | §3.3–4.1, Eq. 8, p. 1540 | Cap.2: alternativa formal ao DRI-SL na fase quente; nosso caso usaria pseudo-rótulos do LLM |
| C4 | O método é genérico: acopla a entropia, VAAL, BALD e (versão gulosa) KCenterGreedy | §4, Eq. 8–9, Alg. 2, p. 1540–1541 | Cap.2: balanceamento como camada ortogonal à estratégia — mesmo desenho em fases do FALCO |
| C5 | Ganhos consistentes nos desbalanceados; em CIFAR100, Entropy-CB ganha ≥1% sobre entropia após 4 ciclos em qualquer IF, e VAAL-CB chega a +3,29% | Tab. 2, p. 1543; §5.2, p. 1542 | Cap.2: ordem de grandeza do ganho de balancear a seleção |
| C6 | Mesmo em datasets balanceados o balanceamento tende a ajudar, por conter o viés amostral do próprio AL | Abstract; Tab. 1–2 (IF=1), p. 1543 | Cap.6: viés amostral do AL como fenômeno separável do desbalanceamento do pool |
| C7 | Há um trade-off entre balanceamento e informatividade, regulado por λ (mais balanceado ⇒ menor entropia média da seleção) | Fig. 4 e §4.1, p. 1539–1540 | Cap.6: enquadra por que maximizar só incerteza pode ser subótimo no nosso domínio |

## Números que posso citar
- Protocolo: L0 = 10% do treino (uniforme por classe); orçamento de 5% por
  ciclo; 4–5 ciclos; 3 execuções por experimento; ResNet18 do zero
  (CIFAR10/100) e ResNet101 pré-treinada (Tiny ImageNet) (§5.1, p. 1541–1542).
- Cauda longa sintética: IF∈{0.1, 0.3} aplicado a metade das classes, removendo
  exemplos do treino (protocolo de Cui et al. 2019) (§5.1, p. 1542).
- CIFAR10 IF=0.3: Entropy-CB atinge 86% de acurácia; aleatória precisa de ~10%
  a mais de anotação (~5 mil imagens) para o mesmo desempenho (§5.2, p. 1542).
- CIFAR100 IF=0.3: VAAL-CB +3,23% e +3,29% sobre VAAL nos ciclos 3–4; IF=0.1:
  Entropy-CB +2,23% no ciclo 2 (Tab. 2, p. 1543).
- Tiny ImageNet (200 classes): ganhos menores porém positivos — Entropy-CB até
  +0,74% (IF=1, ciclo 4); métodos representativos declarados inviáveis em
  datasets grandes (Tab. 3 e nota 2, p. 1543).

## Citações diretas (com página)
> "Active learning is generally studied on balanced datasets where an equal
> amount of images per class is available. However, real-world datasets suffer
> from severe imbalanced classes, the so called long-tail distribution."
> (p. 1536)

> "AL methods tend to sample more from frequent classes and less from minority
> classes which consequently leads to biased predictions and a performance
> drop." (p. 1538)

## Crítica / limitações (minha leitura)
- Visão computacional, C ≤ 200 classes e IF ≥ 0.1: nosso problema tem 714
  classes com cauda mais severa e texto curto; a programação binária N×C pode
  não escalar no nosso pool (~10⁵ itens × 714 classes) — e os ganhos já
  encolhem de CIFAR10 para Tiny ImageNet.
- O alvo é a distribuição UNIFORME porque o teste deles é balanceado; nosso
  teste é cauda longa real — o Ω(c) teria de mirar a distribuição do domínio,
  não a uniforme (adaptação não trivial, boa discussão para trabalhos futuros).
- Confia nos pseudo-rótulos do próprio classificador para estimar classes dos
  não-rotulados: nas classes raras (onde o modelo é pior) a estimativa é
  justamente menos confiável — o paper não quantifica esse erro circular.
- Oráculo perfeito e gratuito (gabarito); sem noção de custo por rótulo nem
  ruído — com LLM-oráculo, o erro de rotulagem interage com o balanceamento
  (rótulo errado em classe rara é duplamente danoso), interação que o P3+P4
  medem e este paper não.
- Métrica só acurácia em teste balanceado; sem macro-F1 — nossa métrica
  principal para cauda longa.

## Ideias que gera para a tese
- Usar C2 (viés amostral crescente por ciclo) como argumento de que o laço do
  FALCO precisa de diagnóstico de distribuição por fase — temos os artefatos
  JSONL para plotar o equivalente da Fig. 2 no nosso domínio.
- Confronto DRI-SL × CBAL na revisão: balancear antes (frio, sem modelo) vs.
  durante (quente, pseudo-rótulos); FALCO poderia compor os dois.
- O L1-score deles (distância à uniforme) sugere uma métrica análoga de
  "aderência à distribuição-alvo" para as fases do FALCO.
