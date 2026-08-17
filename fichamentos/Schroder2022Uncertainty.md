---
id: Schroder2022Uncertainty
title: "Revisiting Uncertainty-based Query Strategies for Active Learning with Transformers"
authors: ["Schröder, Christopher", "Niekler, Andreas", "Potthast, Martin"]
year: 2022
venue: "Findings of the Association for Computational Linguistics: ACL 2022, pp. 2194–2203"
doi: "10.18653/v1/2022.findings-acl.172"
pdf: referencias-pdf/Schroder2022Uncertainty.pdf
paper_type: avaliacao
pillars: [P4, geral]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, entropia,
               menor-margem, menor-confianca, fine-tuning]
datasets: [agnews, trec, movie-reviews, customer-reviews, subjectivity]
metrics: [acuracia, auc-curva-de-aprendizado]
tasks: [classificacao-de-texto]
models: [bert, distilroberta, svm, kimcnn]
extends: []
compares_with: [Margatina2021, EinDor2020]
contradicts: []
builds_on: [Schroder2020DNNSurvey, Schroder2021SmallText, Lewis1994, Devlin2019]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Valida empiricamente a escolha central do FALCO: com transformers,
           estratégias de incerteza (baratas) são eficazes E eficientes, enquanto
           as estratégias 'estado-da-arte' impõem overhead proibitivo no laço —
           mesmo argumento de custo que justifica nosso classificador leve no
           laço e BERTimbau fora dele (E3')."
  - type: ameaca
    target: FALCO
    note: "Desafia o status da entropia (PE) como baseline default: com
           transformers, breaking ties (menor-margem) supera PE em média nos
           multiclasse. Como nosso baseline de incerteza é entropia num problema
           de 714 classes, precisamos ou justificar a escolha ou reportar BT —
           citar ao definir os baselines do P4."
  - type: complementa
    target: LCE
    note: "Usa AUC da curva de aprendizado como métrica-resumo de eficiência —
           antecedente direto da LCE; citar como prática corrente que a LCE
           refina."
---

# Revisiting Uncertainty-based Query Strategies for Active Learning with Transformers

## Resumo (5-8 linhas)
Avaliação sistemática (Findings of ACL 2022) de estratégias de consulta baseadas
em incerteza combinadas com transformers (BERT-large e DistilRoBERTa) em cinco
benchmarks de classificação de sentenças. Motivação: as estratégias
estado-da-arte (gradientes, ensembles, contrastivas) têm custo computacional
proibitivo com transformers, anulando a economia de rotulagem; as de incerteza,
"ultrapassadas" na era pré-transformer, voltam a ser competitivas. Resultado
central: breaking ties (menor-margem) supera em média a entropia de predição
(PE) — o baseline mais usado da área — nos datasets multiclasse, e o AL atinge
resultados próximos do estado-da-arte passivo usando 0,4%–15% dos dados. Obra
DISTINTA do survey (Schroder2020DNNSurvey) e da biblioteca (Schroder2021SmallText)
dos mesmos autores; usa a small-text como infraestrutura dos experimentos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Estratégias de consulta estado-da-arte (gradiente, ensemble, contrastiva) induzem overhead de execução proibitivo com transformers, anulando ou superando a economia de rotulagem | Abstract; §2, p. 2195; Tab. 8, p. 2203 | Cap.2/Cap.3: justifica classificador leve no laço (custo do ciclo de consulta) |
| C2 | Com transformers, breaking ties (menor-margem) supera a entropia de predição em média (melhor rank de AUC e, com frequência, de acurácia), desafiando a entropia como baseline default | §4, Tab. 2, p. 2196–2197; Conclusões, p. 2198 | Cap.3: discussão da escolha do baseline de incerteza do P4 (nosso problema é multiclasse extremo) |
| C3 | AL com BERT alcança resultados próximos ou acima do estado-da-arte passivo usando entre 0,4% e ~15% dos dados de treino | Tab. 3, p. 2197 | Cap.2: evidência quantitativa de que AL+transformer preserva desempenho com fração mínima de rótulos |
| C4 | Amostragem aleatória é competitiva nas iterações iniciais mas é superada depois; em dataset desbalanceado (TREC-6) é menos eficaz | §4 Results, p. 2197 (confirmando Ein-Dor et al. 2020) | Cap.5: interpreta por que aleatória compete no início das nossas curvas e por que degrada sob desbalanceamento |
| C5 | DistilRoBERTa (<25% dos parâmetros do BERT) chega muito perto do BERT a uma fração do custo — do ponto de vista do praticante, o modelo menor é preferível | Tab. 2, p. 2196; §4, p. 2198; Tab. 8, p. 2203 | Cap.3/Cap.6: precedente do trade-off "modelo menor no laço"; paralelo com nosso par leve/BERTimbau |
| C6 | Para o TREC-6 (desbalanceado), o conjunto inicial foi balanceado por classe, senão a classe mais rara "raramente seria encontrada" por amostragem aleatória | Apêndice C, p. 2201 | P1/P2: até o benchmark padrão precisa intervir na composição do L0 sob desbalanceamento — motiva DRI-SL |
| C7 | Razão teórica declarada para a fraqueza da entropia: em redes profundas atuais a entropia de predição "has been observed to be overconfident" (Guo et al. 2017; Lakshminarayanan et al. 2017); ensembles, a alternativa calibrada, são caros demais | §2, p. 2195 | Cap. 5: fundamenta POR QUE a entropia pode falhar como critério de incerteza no E5/E6, além do resultado empírico do C2 |

## Números que posso citar
- Protocolo: L0 de 25 instâncias + 20 iterações × 25 instâncias/consulta; 5
  execuções por configuração; early stopping (acurácia >98% em validação de 10%
  ou 5 épocas sem melhora de loss) (§4, p. 2197).
- AGN com BERT+BT: acurácia 0,904 usando 0,4% do treino (passivo próprio: 0,946
  com 100%) (Tab. 3, p. 2197).
- TREC-6 com BERT+CA: 0,968 com 9,55% dos dados — acima do passivo próprio
  (0,958) (Tab. 3, p. 2197).
- Ranks médios de AUC (BERT): BT 1,60 < PE 2,40 < CA 2,60 < LC 3,80 < RS 4,00
  (Tab. 2, p. 2196).
- Tempo de consulta em AGN com BERT: CA 1476s ± 392 vs PE 529s ± 118 vs RS
  ~0,002s (Tab. 8, p. 2203) — o custo do ciclo é dominado pela estratégia.
- Condições exatas: BERT-large (336M par.) e DistilRoBERTa (82M); 5 datasets
  (AGN, CR, MR, SUBJ, TREC-6), todos balanceados exceto TREC-6; small-text
  1.0.0a8 como framework (Apêndices A–C, p. 2200–2201).
- Orçamento total de rótulos: **525** instâncias por execução (25 iniciais +
  20 × 25), o teto de todas as curvas da Fig. 1 (§4, p. 2197).
- Faixa declarada pelos autores: modelos ficam próximos ou acima do estado da
  arte usando "only between **0,4% and 14%** of the data" (§4, p. 2198); o maior
  percentual da Tab. 3 é **15,45%** (CR), donde a leitura "~15%" acima.
- Uso de dados por dataset (Tab. 3, p. 2197): AGN **0,4%** (525 de 120.000);
  CR **15,45%**; MR **0,547%**; SUBJ **5,83%**; TREC-6 **9,55%**.
- Acurácia final do BERT (média±dp sobre 5 execuções, Tab. 5, p. 2201):
  AGN+BT **0,904±0,002**; CR+LC **0,919±0,009**; MR+PE/BT **0,857±0,009**;
  SUBJ+LC **0,958±0,005**; TREC-6+CA **0,968±0,004** (nos três datasets
  binários — CR, MR, SUBJ — PE e BT compartilham a mesma célula porque
  selecionam as mesmas instâncias).
- Arquiteturas: BERT-large com 24 camadas e estados ocultos de 1024;
  DistilRoBERTa com 6 camadas e 768 (§3, p. 2196).
- Tempo de consulta em AGN com BERT, série completa (Tab. 8, p. 2203):
  LC **480,4s ± 107,4** < BT **503,5s ± 112,6** < PE **528,9s ± 118,3** <<
  CA **1476,0s ± 391,6**; RS 0,002s — as três estratégias de incerteza custam
  praticamente o mesmo entre si e ~3× menos que a contrastiva.

## Citações diretas (com página)
> "This invalidates the common practice of solely relying on prediction entropy
> as baseline, and shows that uncertainty-based strategies demand renewed
> attention especially in the context of transformer-based active learning."
> (p. 2198)

> "using state-of-the-art query strategies for transformers induces a
> prohibitive runtime overhead, which effectively nullifies, or even outweighs
> the desired cost savings." (p. 2194)

> "For active learning with transformers, several other uncertainty-based
> approaches outperform the well-known prediction entropy query strategy,
> thereby challenging its status as most popular uncertainty baseline in active
> learning for text classification." (Resumo, p. 2194)

> "prediction entropy has been observed to be overconfident" (p. 2195, §2)

## Crítica / limitações (minha leitura)
- Sentenças em inglês, 2–6 classes, datasets quase todos balanceados: a
  generalização para 714 classes com cauda longa em PT-BR não é automática — no
  binário BT≡PE, e é justamente no multiclasse que BT ganha, o que TORNA o
  resultado mais relevante para nós, mas ninguém testou c≫10.
- Oráculo = gabarito dos benchmarks (perfeito e gratuito); nenhuma noção de
  custo por rótulo ou ruído de oráculo — exatamente o eixo que o P3 adiciona.
- Transformer DENTRO do laço (re-treino a cada 25 rótulos): o custo reportado na
  Tab. 8 reforça nossa decisão de mantê-lo fora do laço; a comparação leve
  vs. transformer no laço não é feita por eles.
- 5 sementes e IC não reportado como teste formal; conclusões por rank médio
  sobre 5 datasets — padrão da área, mas abaixo do nosso protocolo (Wilson,
  McNemar).

## Ideias que gera para a tese
- Reportar breaking ties (menor-margem) ao lado de entropia no P4, ou ao menos
  justificar a entropia citando este resultado como limitação conhecida.
- Usar a Tab. 8 (tempo de consulta) como analogia para a nossa decomposição de
  custo: eles medem segundos de GPU; nós medimos tokens/custo do oráculo.
- Na Tabela de lacunas: este paper cobre "incerteza × transformer" mas não
  toca oráculo LLM, custo por rótulo, nem desbalanceamento extremo — tripla
  lacuna que o FALCO ocupa.
