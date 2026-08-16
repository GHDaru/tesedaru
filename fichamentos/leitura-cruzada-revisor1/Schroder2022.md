---
id: Schroder2022
title: "Revisiting Uncertainty-based Query Strategies for Active Learning with Transformers"
authors: ["Schröder, Christopher", "Niekler, Andreas", "Potthast, Martin"]
year: 2022
venue: "Findings of the Association for Computational Linguistics: ACL 2022, p. 2194-2203"
doi: "10.18653/v1/2022.findings-acl.172"
pdf: referencias-pdf/Schroder2022.pdf
paper_type: avaliacao
pillars: [P2]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, entropia, menor-confianca, menor-margem, fine-tuning]
datasets: [agnews, trec]
metrics: [acuracia]
tasks: [classificacao-de-texto]
models: [bert, distilroberta]
extends: []
compares_with: [Margatina2021, EinDor2020]
contradicts: []
builds_on: [Lewis1994, Devlin2019, Schroder2021SmallText]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Base empírica da escolha do FALCO de usar amostragem por incerteza no
           laço com transformers (E5/E6): mostra que estratégias de incerteza,
           computacionalmente baratas, são altamente eficazes com fine-tuning de
           transformers — acurácia próxima do estado da arte com 0,4%-14% dos
           dados — enquanto gradientes/ensembles têm custo proibitivo."
  - type: motiva
    target: FALCO
    note: "Desafia a entropia de predição como baseline default: breaking ties
           (menor margem) obtém os melhores ranks médios de acurácia/AUC em
           multi-classe. Como o E5/E6 usa entropia, isso motiva discutir (Cap. 5)
           a menor margem como variante para as 714 classes desbalanceadas; o
           seed class-balanced que usam no TREC-6 dialoga com o papel do DRI-SL
           no cold start desbalanceado."
---

# Revisiting Uncertainty-based Query Strategies for Active Learning with Transformers

## Resumo (5-8 linhas)
Reavalia sistematicamente as estratégias de consulta por incerteza — entropia de
predição (PE), breaking ties/menor margem (BT), menor confiança (LC) — contra
contrastive active learning (CA) e amostragem aleatória (RS), agora no regime de
fine-tuning de transformers (BERT-large e DistilRoBERTa), em cinco benchmarks de
classificação de sentenças (AGN, CR, MR, SUBJ, TREC-6). Com apenas 525 instâncias
rotuladas (25 iniciais + 20 iterações × 25), os modelos chegam perto (ou acima)
do estado da arte com 0,4%-14% dos dados. Contrariando a prática corrente, PE é
superada por outras estratégias de incerteza, em particular BT — desafiando seu
status de baseline padrão. Incerteza volta a ser competitiva porque é barata
frente a gradientes/ensembles, proibitivos com transformers.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Estratégias de incerteza + fine-tuning de transformers são "highly effective as well as efficient"; estratégias SOTA (gradientes, ensembles) têm custo proibitivo com transformers | §1-2, p. 2194-2195; tempos de consulta na Tab. 8, p. 2203 | Cap. 2 fundamentação; Cap. 3 justificativa do E5/E6 |
| C2 | BT (menor margem) supera PE em rank médio de acurácia e AUC com transformers ("the PE baseline is outperformed by BT") | Tab. 2, p. 2196; §4, p. 2198 | Cap. 2; Cap. 5 discussão da escolha da entropia |
| C3 | Com AL, os modelos ficam próximos ou acima do estado da arte usando só 0,4%-14% dos dados de treino | Tab. 3, p. 2197; §4, p. 2198 | Cap. 2 — economia de rótulos alcançável com incerteza |
| C4 | RS é forte nas primeiras iterações, mas é superada depois; em dados desbalanceados (TREC-6) RS é menos eficaz, confirmando Ein-Dor et al. 2020 | §4, p. 2197-2198 | Cap. 2/Cap. 5 — papel do desbalanceamento (714 classes) |
| C5 | PE tende à superconfiança em redes profundas (motivo teórico da fraqueza da entropia como critério) | §2, p. 2195 (com Guo et al. 2017) | Cap. 5 discussão — limites da entropia no E5/E6 |
| C6 | DistilRoBERTa, com <25% dos parâmetros do BERT, chega notavelmente perto do BERT a uma fração do custo | §4-5, p. 2198 | Cap. 5 — trade-off custo/desempenho do classificador |
| C7 | Para TREC-6 (desbalanceado), o conjunto inicial foi CLASS-BALANCED, senão a classe mais rara raramente entraria por amostragem aleatória | Apêndice C, p. 2201 | Cap. 3 — motivação do DRI-SL para cold start desbalanceado |

## Números que posso citar
- Protocolo: 25 instâncias iniciais + 20 iterações × 25 consultas = 525 rótulos;
  5 execuções por configuração; parada antecipada por 98% de acurácia de
  validação ou 5 épocas sem melhora (§4, p. 2197).
- Acurácia final (média±dp, 5 runs, Tab. 5, p. 2201): AGN BERT+BT 0,904±0,002;
  CR BERT+LC 0,919±0,009; MR BERT+BT 0,857±0,009; SUBJ BERT+LC 0,958±0,005;
  TREC-6 BERT+CA 0,968±0,004.
- Uso de dados (Tab. 3, p. 2197): AGN 0,4% (525 de 120.000); CR 15,45%;
  MR 0,547%; SUBJ 5,83%; TREC-6 9,55%.
- Modelos: BERT-large (24 camadas, 336M parâmetros) vs DistilRoBERTa (6 camadas,
  82M) (§3, p. 2196).
- Tempo de consulta em AGN com BERT (Tab. 8, p. 2203): LC 480,4s, BT 503,5s,
  PE 528,9s vs CA 1476,0s por passo — incerteza ~3× mais barata que CA.

## Citações diretas (com página)
> "Several other uncertainty-based approaches outperform the well-known prediction entropy query strategy, thereby challenging its status as most popular uncertainty baseline in active learning for text classification." (Abstract, p. 2194)

> "This invalidates the common practice of solely relying on prediction entropy as baseline, and shows that uncertainty-based strategies demand renewed attention especially in the context of transformer-based active learning." (§5, p. 2198)

## Crítica / limitações (minha leitura)
- Datasets pequenos e de poucas classes (2-6); quatro dos cinco são balanceados.
  Nada garante que BT > PE se mantenha em 714 classes fortemente desbalanceadas
  em PT-BR — no FALCO isso é hipótese a discutir, não fato importado.
- Avaliação por acurácia e AUC da curva de aprendizado; sem métricas macro
  (Macro F1), que são as relevantes sob desbalanceamento severo.
- Oráculo perfeito (rótulos gold dos benchmarks); não considera oráculo ruidoso
  como o LLM do FALCO, nem custo de rótulo heterogêneo (LCE).
- Textos em inglês; sem PT-BR nem domínio de e-commerce.

## Ideias que gera para a tese
- Citar C1/C3 no Cap. 3 como base da escolha de incerteza (barata) no laço
  E5/E6 com transformers, alinhada à restrição de custo do FALCO.
- Cap. 5: registrar a menor margem (breaking ties) como variante promissora à
  entropia para multi-classe desbalanceada — trabalho futuro direto do E6.
- C7 fortalece o argumento do DRI-SL: em desbalanceamento severo, o arranque
  aleatório perde classes raras; seleção estruturada de seed importa.
- Comparação de custo computacional por consulta (Tab. 8) é um análogo, no eixo
  de computação, do que a LCE mede no eixo de custo de rótulo.
