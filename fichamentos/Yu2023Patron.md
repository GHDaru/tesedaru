---
id: Yu2023Patron
title: "Cold-Start Data Selection for Better Few-shot Language Model Fine-tuning: A Prompt-based Uncertainty Propagation Approach"
authors: ["Yu, Yue", "Zhang, Rongzhi", "Xu, Ran", "Zhang, Jieyu",
          "Shen, Jiaming", "Zhang, Chao"]
year: 2023
venue: "ACL 2023 (Long Papers), pp. 2499-2521"
doi: "10.18653/v1/2023.acl-long.141"
pdf: referencias-pdf/Yu2023Patron.pdf
paper_type: metodo
pillars: [P2]
status: fichado
proposes: [patron, propagacao-de-incerteza, partition-then-rewrite]
uses_methods: [aprendizado-ativo, pool-based, cold-start, few-shot, zero-shot,
               amostragem-por-incerteza, entropia, k-means, fine-tuning,
               selecao-por-diversidade]
datasets: [imdb, agnews, trec, yelp-full, yahoo-answers, dbpedia]
metrics: [acuracia, f1]
tasks: [classificacao-de-texto]
models: [roberta-base, simcse]
extends: []
compares_with: [Sener2018, Hacohen2022TypiClust, Yuan2020]
contradicts: []
builds_on: []
falco_relation:
  - type: compara
    target: DRI-SL
    note: "Estado da arte de cold start textual que USA o conhecimento do PLM
           na seleção: pseudo-rótulos por prompt cloze + calibração + entropia,
           propagados por kernel RBF a vizinhos k-NN (SimCSE), e diversidade
           via K-Means + reescrita com regularização entre clusters. O DRI-SL
           difere em três eixos: (i) custo — PATRON roda inferência do PLM em
           TODO o pool não rotulado; DRI-SL usa encoder congelado + operações
           esparsas, sem nenhum modelo na malha de seleção; (ii) engenharia —
           PATRON exige template e verbalizador manuais por tarefa (mapear as
           714 classes do varejo a palavras-rótulo de [MASK] é impraticável;
           experimentos param em c=14); (iii) sinal — PATRON mistura incerteza
           pseudo-rotulada com diversidade; DRI-SL é 100% representatividade +
           novidade lexical, coerente com a evidência de que incerteza é
           enviesada no cold start (o próprio PATRON, §1 e obs. 3 do §5.3)."
  - type: compara
    target: FALCO
    note: "Como o ActiveLLM (Bayer2024ActiveLLM), põe o modelo de linguagem na
           fase de SELEÇÃO; o FALCO faz a separação oposta — seleção local
           barata (DRI-SL) e LLM só na ROTULAGEM — reduzindo chamadas na fase
           cara e eliminando template/verbalizador por classe."
---

# Cold-Start Data Selection for Better Few-shot Language Model Fine-tuning: A Prompt-based Uncertainty Propagation Approach (PATRON)

## Resumo (5-8 linhas, com as MINHAS palavras)
Ataca a seleção de dados em cold start (zero rótulos iniciais) para fine-tuning
few-shot de PLMs, onde o desempenho varia até 10 p.p. conforme o subconjunto
rotulado. O PATRON gera pseudo-rótulos zero-shot via prompt cloze com
verbalizador, calibra com prior contextualizado, mede incerteza por entropia e
a propaga aos k-NN via kernel RBF sobre embeddings SimCSE — só há incerteza
alta se o ponto E sua vizinhança são incertos. A seleção usa
partition-then-rewrite: K-Means com k=B, escolha por cluster equilibrando
incerteza propagada e proximidade ao centroide, e reescrita iterativa com
penalidade que afasta seleções de clusters adjacentes. Em 6 datasets ingleses
(c=2..14), supera as melhores baselines em 3,4-6,9 p.p. em média e atinge
91,0%/92,1% do desempenho totalmente supervisionado com só 128 rótulos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Em cold start, a incerteza estimada pelo PLM é enviesada/mal calibrada; métodos puros de incerteza (ex.: CAL, entropia) perdem até de random | §1, pp. 2499-2500; §5.3 obs. (3), pp. 2504-2505 | Cap. 2: terceira fonte independente (após Hacohen 2022 e Sener 2018) de que US falha no cold start |
| C2 | Poucos rótulos → alta variância: fine-tuning de RoBERTa-base em AG News com 32 rótulos varia até 10 p.p. entre amostragens | §1, Fig. 1, p. 2499 | Cap. 1/2: motivação do P1-P2 (a composição do L0 importa) em texto, não só em visão |
| C3 | PATRON = pseudo-rótulos por prompt (Eq. 1) + calibração (Eqs. 2-4) + entropia (Eq. 5) + propagação k-NN/RBF (Eqs. 6-7) + PTR (Eqs. 8-10) | §4, Alg. 1, pp. 2501-2503 | Cap. 2: descrição do competidor SOTA textual do DRI-SL |
| C4 | Com 128 rótulos (<0,5% dos dados), PATRON atinge 91,0% (fine-tuning) e 92,1% (prompt-based) do totalmente supervisionado, média de 6 datasets | Abstract; §5.3 obs. (1); Tabs. 1-2, pp. 2504-2505 | Referência de teto para "quanto dá para extrair de 128 rótulos" em inglês |
| C5 | Coreset em cold start textual fica ABAIXO de random (53,2 vs. 57,2 de média com B=32) | Tab. 1, p. 2504 | Confronto R6 item 11: coreset não é páreo no nosso regime; DRI-SL só precisa vencer random e as diversidade-based |
| C6 | K-Means simples (BERT-KM) supera métodos mais elaborados (TypiClust, ALPS) em datasets com mais classes | §5.3 obs. (4), p. 2505 | Sustenta a escolha do DRI-SL por k-médias como espinha + refino lexical |
| C7 | Ganhos maiores em datasets com mais classes (TREC, Yahoo!): menos rótulos por classe sob orçamento fixo | §5.3 obs. (2), p. 2504 | Extrapolação favorável ao nosso caso (714 classes), com a ressalva c≤14 |
| C8 | Em AL multi-rodada, quando o orçamento passa de ~256 (IMDB), métodos de incerteza voltam a vencer — o cold start é regime, não dogma | §5.4, p. 2505 | Converge com a transição de fase de Hacohen 2022; justifica o desenho por fases do FALCO |
| C9 | Seleção estratégica reduz a VARIÂNCIA, não só a média: PATRON tem desvio-padrão menor que as baselines em 14 dos 18 cenários (6 datasets × 3 orçamentos) | §5.3 obs. (1), p. 2504 | Cap. 4/5: estabilidade do L0 como critério de qualidade além da acurácia média — métrica que o DRI-SL também pode reivindicar |

## Números que posso citar
- Média de 6 datasets, fine-tuning, 10 execuções: PATRON **68,4 / 75,2 / 80,2**
  para B=32/64/128 vs. random 57,2/68,9/76,6; ganho de **+6,9/+5,0/+3,4 p.p.**
  sobre a MELHOR baseline por orçamento (Tab. 1, p. 2504).
- Coreset (Sener2018) na média com B=32: **53,2** — abaixo de random (57,2);
  TypiClust (TPC): 58,9 (Tab. 1, p. 2504).
- Com 128 rótulos: **91,0%** do fully-supervised (fine-tuning) e **92,1%**
  (prompt-based) (Abstract; Tabs. 1-2).
- Eficiência de rótulos: PATRON com 128 rótulos ≥ random com 2× rótulos; com
  512 (multi-rodada) ≈ 95% do supervisionado ≈ random com 3× (§5.5, Fig. 4).
- Setup: RoBERTa-base; budgets {32, 64, 128}; c = 2..14 classes; seleção
  one-round no experimento principal; T=2 iterações de PTR (§5.1; Alg. 1) — o
  texto de §4.3 (p. 2503) registra que a reescrita converge em **2-3 iterações**
  ("the selected samples do not change anymore"), então T=2 é o valor fixado no
  trabalho, não um limite do método.
- Linha de Yahoo! Answers (c=10), B=32, para citar a hierarquia completa das
  baselines: PATRON **56,8 ± 1,0** > ALPS 47,7 > BERT-KM 46,8 > aleatório 43,5 >
  TPC 36,9 > Margin-KM 34,0 > CAL 26,6 > incerteza 23,0 > **Coreset 22,0**
  (Tab. 1, p. 2504) — o dataset com mais classes é onde a ordem
  representatividade > incerteza > geometria fica mais nítida.
- Todos os resultados da Tab. 1 são média de **10 execuções**, com
  significância por teste t de Student aos níveis **0,05 e 0,01** (legenda da
  Tab. 1, p. 2504).
- Estabilidade: desvio-padrão menor que o das baselines em **14 de 18** casos
  (§5.3 obs. (1), p. 2504).
- TREC é desbalanceado — reportado em F1 no apêndice G.2 (legenda da Tab. 1).

## Citações diretas (com página)
> "the estimated uncertainty for unlabeled data from the PLM can be biased over
> classes. As a result, uncertainty-based approaches can underperform even the
> random selection strategy" (§1, pp. 2499-2500)

> "we do not claim PATRON outperforms AL methods under high-budget scenarios"
> (§6, p. 2507)

> "In PATRON, we design (1) a prompt-based uncertainty propagation approach to
> estimate the importance of data points and (2) a partition-then-rewrite (PTR)
> strategy to promote sample diversity when querying for annotations."
> (Abstract, p. 2499)

## Crítica / limitações (minha leitura)
- Template e verbalizador MANUAIS por tarefa (nota 3, p. 2501): cada classe
  precisa virar palavra(s) de vocabulário previstas em [MASK]. Com 714 classes
  hierárquicas de produto em PT-BR, construir e calibrar esse verbalizador é um
  projeto em si; os experimentos param em c=14.
- Custo: inferência do PLM (prompting) sobre TODO o pool + embeddings SimCSE +
  K-Means com k=B + grafos k-NN em duas escalas. A "seleção" consome o tipo de
  chamada cara que o FALCO reserva para a rotulagem.
- Tudo em inglês, com RoBERTa-base e SimCSE en; nada garante que pseudo-rótulos
  cloze funcionem em títulos de varejo PT-BR de ~32 caracteres (texto
  telegráfico, abreviações, sem sintaxe para o template ancorar).
- Desbalanceamento tratado superficialmente (TREC via F1 em apêndice); nenhum
  estudo de cauda longa severa.
- Três hiperparâmetros novos (ρ, β, γ) — robustos nos ablations (§5.7), mas
  ajustados com acesso a conjuntos de validação rotulados, o que contradiz um
  pouco o espírito rótulo-zero. Some-se o limiar de distância m da regularização
  entre clusters adjacentes (§4.3, p. 2503): são quatro botões numa fase que,
  por definição, não tem rótulo para calibrá-los.
- Orçamentos de 32-128 rótulos em uma rodada: duas ordens de grandeza abaixo dos
  braços de 15k-35k do FALCO; a evidência não cobre AL progressivo em escala.

## Ideias que gera para a tese
- Fecha o triângulo do R6 item 11: TypiClust (visão, tipicidade), coreset
  (geometria minimax, orçamento alto) e PATRON (texto, PLM na seleção) — DRI-SL
  se posiciona como o único dos quatro sem modelo treinado/consultado na malha
  de seleção, com custo linear e diversidade lexical explícita para texto curto.
- C5+C6 dão números citáveis para desarmar "por que não coreset?" e "por que
  k-médias basta como base?".
- C8 + Hacohen C1: par de evidências (visão + texto) para o argumento de regime
  do FALCO — representatividade primeiro, incerteza depois (se houver orçamento).
- Comparação futura (trabalhos futuros do Cap. 6): PATRON com verbalizador
  automático seria o competidor textual a bater se o custo de prompting cair.
- A calibração por prior contextualizado (Eqs. 3-4) é candidata a corrigir a
  confiança que o oráculo LLM do FALCO reporta em classes raras — é o mesmo
  problema (viés de classe na saída do PLM), mas aplicado à rotulagem (P3) em vez
  da seleção.
- C9 sugere reportar desvio-padrão entre sementes como resultado, e não como
  ruído: se o DRI-SL estabilizar o L0, isso é um ganho vendável mesmo onde a
  média empatar.
