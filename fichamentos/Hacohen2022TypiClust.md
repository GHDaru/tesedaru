---
id: Hacohen2022TypiClust
title: "Active Learning on a Budget: Opposite Strategies Suit High and Low Budgets"
authors: ["Hacohen, Guy", "Dekel, Avihu", "Weinshall, Daphna"]
year: 2022
venue: "ICML 2022 (PMLR 162)"
doi: ""
pdf: referencias-pdf/Hacohen2022TypiClust.pdf
paper_type: metodo
pillars: [P1, P2]
status: fichado
proposes: [typiclust, tipicidade, transicao-de-fase-de-orcamento]
uses_methods: [aprendizado-ativo, pool-based, cold-start, auto-supervisao,
               k-means, selecao-por-diversidade, amostragem-por-incerteza]
datasets: [cifar-10, cifar-100, tiny-imagenet, imagenet-subconjuntos]
metrics: [acuracia]
tasks: [classificacao-de-imagens]
models: [simclr, dino, scan, flexmatch]
extends: []
compares_with: [Sener2018]
contradicts: []
builds_on: [Hacohen2019]
falco_relation:
  - type: compara
    target: DRI-SL
    note: "Fundamento teórico do regime de orçamento baixo: no cold start,
           selecionar exemplos TÍPICOS (densos) e diversos vence incerteza e
           coreset — mesmo princípio de representatividade da etapa 1 do DRI-SL
           (k-médias + cota proporcional). Diferenças: TypiClust exige
           representação auto-supervisionada treinada no pool (cara) e mede
           tipicidade por densidade k-NN, que em texto curto com 7,7% de
           duplicatas tende a escolher quase-duplicatas; o DRI-SL não usa
           encoder treinado na tarefa, tem custo linear e adiciona a variedade
           LEXICAL intragrupo que a tipicidade pura não garante (o próprio paper
           mostra que tipicidade sem diversidade falha, TPC_NoClust, §4.3.3)."
  - type: fundamenta
    target: FALCO
    note: "Dá base teórica (modelo de mistura + transição de fase, §2) para a
           escolha do FALCO de usar estratégia de representatividade — e não
           incerteza — na fase de orçamento baixo: até incerteza de oráculo
           perfeito perde de random nesse regime (§4.3.4)."
---

# Active Learning on a Budget: Opposite Strategies Suit High and Low Budgets

## Resumo (5-8 linhas, com as MINHAS palavras)
Analisa teoricamente (modelo de mistura de dois aprendizes) e empiricamente a
relação entre tamanho do orçamento de rotulagem e estratégia ótima de AL,
identificando uma transição de fase: com orçamento baixo convém superamostrar
exemplos típicos (regiões densas, "fáceis"); com orçamento alto, exemplos
atípicos/incertos. Disso deriva o TypiClust: aprende representação
auto-supervisionada do pool, agrupa em |L|+B clusters e consulta o exemplo mais
típico (inverso da distância média aos K=20 vizinhos) de cada um dos B maiores
clusters não cobertos. No regime de orçamento baixo (1–10 exemplos/classe por
rodada), supera todas as estratégias clássicas — que empatam com ou perdem de
random — em CIFAR-10/100, TinyImageNet e subconjuntos do ImageNet, com ganho
máximo no semi-supervisionado (93,2% em CIFAR-10 com 10 rótulos).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Transição de fase: típicos são a melhor consulta em orçamento baixo; atípicos/incertos em orçamento alto | Abstract; §2 (Thm. 1–3); Fig. 1, pp. 1–5 | Cap. 2 (posicionamento do DRI-SL); justifica representatividade no cold start |
| C2 | Em orçamento baixo, TODAS as baselines clássicas (incerteza, margem, entropia, BADGE, BALD, DBAL e CoreSet) empatam com random ou pioram | §4.2.1, Fig. 4, p. 7 | Confronto DRI-SL × coreset: coreset não é competidor forte no nosso regime |
| C3 | TypiClust = representação auto-supervisionada + k-means em \|L\|+B clusters + exemplo mais típico dos B maiores clusters não cobertos | §3.2, Alg. 1, pp. 5–6 | Cap. 2: descrição do competidor conceitual mais próximo do DRI-SL |
| C4 | Tipicidade sem diversidade falha (TPC_NoClust) e clustering sem tipicidade também (TPC_Rand) — os dois componentes são cruciais | §4.3.3, Fig. 7c, pp. 7–8 | Defesa da arquitetura em 2 etapas do DRI-SL (densidade + variedade) |
| C5 | Mesmo incerteza calculada por um "oráculo" treinado no dataset inteiro perde de random no orçamento baixo | §4.3.4, Fig. 8, p. 8 | Cap. 2/5: o problema do cold start não é só má estimação de incerteza — é o princípio |
| C6 | TypiClust produz conjuntos rotulados com melhor balanceamento de classes (menor distância TV à distribuição real) sem acesso a rótulos | §4.3.2, Fig. 7b, p. 7 | Paralelo com a cota proporcional por cluster do DRI-SL |
| C7 | Métodos de representação auto-supervisionada assumem classes balanceadas; em CIFAR-10 desbalanceado TypiClust ainda vence no orçamento baixo, mas os autores admitem risco de falha | §4.3.5, p. 8 (Fig. 17, App. G.1) | Limitação frente ao nosso desbalanceamento severo (714 classes) |
| C8 | Seleção não aleatória do pool inicial (L0=∅) traz ganho adicional vs. dar pool inicial random ao TypiClust | §4.3.1, Fig. 7a, p. 7 | Sustenta o P1 (o L0 importa) com evidência independente |

## Números que posso citar
- CIFAR-10, semi-supervisionado (FlexMatch), 10 rótulos escolhidos por
  TypiClust(DC): **93,2%** de acurácia vs. **53,8%** random — ganho de
  **+39,4 p.p.** (Abstract; Fig. 6a, p. 7; 3 repetições).
- CIFAR-100, semi-supervisionado, 300 rótulos: TPC_RP **58,6%** vs. random
  **38,3%** (Fig. 6b, p. 7).
- Regime avaliado: 1–10 exemplos/classe por rodada; orçamentos B = M ou 5M
  (M = nº de classes) com L0 = ∅ (§4.2.1, p. 7).
- Tipicidade: inverso da distância euclidiana média aos K = 20 vizinhos mais
  próximos (Eq. 4 e nota 1, p. 6).

## Citações diretas (com página)
> "typical examples are best queried when the budget is low, while
> unrepresentative examples are best queried when the budget is large"
> (Abstract, p. 1)

> "all other baseline AL methods perform on par with random selection or worse"
> (§4.2.1, p. 7)

## Crítica / limitações (minha leitura)
- Só visão computacional (CIFAR/ImageNet); nada de texto — a transferência do
  princípio para texto curto esparso é plausível, mas não demonstrada aqui.
- Exige treinar representação auto-supervisionada (SimCLR/DINO/SCAN) no próprio
  pool: custo computacional alto que o DRI-SL evita (SBERT congelado + k-médias).
- Tipicidade por densidade k-NN em domínio com 7,7% de duplicatas exatas
  selecionaria quase-duplicatas como "mais típicas" de cada cluster — exatamente
  a redundância que a etapa lexical do DRI-SL suprime.
- Assume datasets balanceados na representação (§4.3.5, admitido pelos autores);
  o teste de desbalanceamento é modesto perto das 714 classes com cauda longa
  do nosso domínio.
- k-means com |L|+B clusters cresce com a iteração; para b0 de centenas o
  agrupamento fica caro — DRI-SL fixa N_c = √I.
- "O que torna um orçamento 'baixo' depende da tarefa" fica em aberto (§5) —
  na tese, o regime é definido empiricamente pelo envelope 100..5000.

## Ideias que gera para a tese
- Usar C1+C5 como fundamento teórico do Cap. 2 para explicar POR QUE US falha
  no cold start do FALCO (não é defeito de implementação, é o regime).
- C4 é o argumento pró-arquitetura em duas etapas do DRI-SL: densidade sozinha
  não basta, diversidade sozinha não basta.
- C6 dialoga com a variante DRI-SL-C (class-aware) do E6 e com o DEUCE
  (Guo2025Deuce): balanceamento emergente sem rótulos.
- Confronto R6 item 11: DRI-SL compartilha o princípio "denso e diverso" do
  TypiClust, mas o operacionaliza sem treinar encoder e com novidade lexical
  explícita — adequado a texto curto, orçamento e CPU.
