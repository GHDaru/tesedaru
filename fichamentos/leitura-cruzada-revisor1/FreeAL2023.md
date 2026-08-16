---
id: FreeAL2023
title: "FreeAL: Towards Human-Free Active Learning in the Era of Large Language Models"
authors: ["Xiao, Ruixuan", "Dong, Yiwen", "Zhao, Junbo", "Wu, Runze",
          "Lin, Minmin", "Chen, Gang", "Wang, Haobo"]
year: 2023
venue: "EMNLP 2023 (main)"
doi: "10.18653/v1/2023.emnlp-main.896"
pdf: referencias-pdf/FreeAL2023.pdf
paper_type: metodo
pillars: [P2, P3, P4]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, llm-como-oraculo, destilacao-ativa, few-shot,
               zero-shot, entropia, cold-start]
datasets: [trec]
metrics: [acuracia, custo-por-rotulo]
tasks: [classificacao-de-texto]
models: [gpt-3.5-turbo, roberta]
extends: []
compares_with: []
contradicts: []
builds_on: [Wang2021GPT3]
falco_relation:
  - type: compara
    target: oraculo-progressivo
    note: "FreeAL fecha um LAÇO LLM↔SLM: o SLM filtra amostras limpas (small-loss
           + k-medoids) que voltam como demonstrações para o LLM RE-rotular os itens
           ruidosos. O oráculo do FALCO rotula uma única vez os itens escolhidos pelo
           DRI-SL, sem realimentação — comparação direta de arquitetura no Cap. 5."
  - type: compara
    target: DRI-SL
    note: "FreeAL resolve o cold start COM o LLM (demonstrações auto-geradas por
           imitação de amostras não rotuladas); DRI-SL resolve o mesmo cold start
           SEM LLM (cluster semântico + variedade lexical), poupando chamadas."
  - type: motiva
    target: FALCO
    note: "Evidência de viabilidade da rotulagem 100% via LLM: custo por rótulo ~2
           ordens de grandeza menor que humano e desempenho quase-supervisionado
           em benchmarks — justifica o braço A do E3'."
---

# FreeAL: Towards Human-Free Active Learning in the Era of LLMs

## Resumo (5-8 linhas, com as MINHAS palavras)
Inverte o aprendizado ativo tradicional: em vez de pedir rótulos a um humano, o LLM
(GPT-3.5-Turbo) atua como anotador e um SLM (RoBERTa) atua como filtro. Na rodada
inicial o LLM gera as próprias demonstrações imitando amostras não rotuladas
(cold start via LLM) e rotula todo o conjunto; o SLM treina com esses rótulos
ruidosos usando seleção small-loss (GMM sobre a perda) + regularização de
consistência, filtra um pool de demonstrações limpo (k-medoids por classe) e o
devolve ao LLM, que re-rotula só os itens ruidosos. Em 8 benchmarks (sentimento,
tópico, NER, domínio biomédico), 4 rodadas aproximam o desempenho supervisionado
sem nenhum rótulo humano, superando AL clássico com 20-50% de anotação humana.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Colaboração LLM-anotador + SLM-filtro atinge desempenho quase-supervisionado sem rótulo humano (SST-2: 94,66 vs 94,89 do fine-tuning supervisionado) | §5.2, Tab. 3, p. 14526 | Cap. 2 (AL na era dos LLMs); Cap. 5 trabalhos relacionados |
| C2 | O refino iterativo melhora os pseudo-rótulos rodada a rodada (SST-2 transdutivo: 88,93 no zero-shot → 95,49 na rodada 4) | §5.2, Tab. 1, p. 14525 | Cap. 5: contraste com FALCO, que rotula uma única vez |
| C3 | Custo por rótulo do LLM é ~2 ordens de grandeza menor que o humano (SST-2: $1,2e-3 vs $0,11) | Apêndice A.2, Tab. 7, p. 14532 | Cap. 2: fundamenta custo-por-rotulo e o orçamento do FALCO |
| C4 | Seleção small-loss para demonstrações supera seleção por entropia e aleatória | §5.3.2, Tab. 6, p. 14527 | Cap. 5: sinal de perda do aluno como detector de ruído do oráculo |
| C5 | Ganhos maiores justamente em domínio especializado (BC5CDR-Disease: +23,1 pontos sobre zero-shot), mas o método depende de o LLM dar anotação inicial minimamente boa | §5.2 p. 14526; Limitations p. 14528 | Cap. 5: limite para 714 classes raras do varejo |
| C6 | Variante multi-rodada rotulando só 10% por vez chega perto do FreeAL completo com fração do custo | Apêndice A.2, Tab. 8, p. 14532 | Cap. 5: paralelo com o caráter progressivo do oráculo FALCO |

## Números que posso citar
- SST-2 (teste, indutivo): RoBERTa treinado por FreeAL 94,66% vs 94,89% do
  fine-tuning supervisionado completo; GPT-3.5-Turbo zero-shot 92,47% → 95,91%
  com FreeAL (Tab. 3, p. 14526).
- SUBJ: ganho absoluto de +34,6 pontos do LLM sobre zero-shot (55,65 → 90,27) —
  tarefa em que o LLM sozinho não se adapta (Tab. 3, p. 14526).
- Custo por rótulo (GPT-3.5-Turbo, ICL m=10, preço 2023): SST-2 $1,2e-3, MR
  $1,3e-3, TREC $8,5e-4 vs $0,11 do humano ($0,11 por 50 tokens, seguindo
  Wang2021GPT3) (Tab. 7, p. 14532).
- FreeAL sem rótulo humano supera Random/Entropy/CAL com 20% e 50% de anotação
  humana em SST-2 e MR (Tab. 5, p. 14527).

## Citações diretas (com página)
> "FreeAL surpasses all the active learning rivals and achieves near-supervised
> performance without human annotation." (legenda da Fig. 1, p. 14520)

> "the effectiveness of FreeAL largely hinges on the strong ability of LLMs. For
> some domains that are extremely challenging or eccentric, the commonly adopted
> GPT-3.5-Turbo nowadays may fail to provide a qualified initial annotation, even
> with self-generated demonstrations." (Limitations, p. 14528)

## Crítica / limitações (minha leitura)
- Benchmarks com 2-6 classes balanceadas em inglês; nada indica que o refino
  colaborativo escale para 714 classes com cauda longa em PT-BR — a seleção
  small-loss por classe (R% menores perdas POR classe) exige classes populosas.
- Cada rodada de refino re-rotula os itens ruidosos: o custo total cresce com o
  número de rodadas (ICL é feito "at most twice" por amostra), enquanto o FALCO
  paga uma chamada por item selecionado.
- Avaliação transdutiva usa o próprio treino; o ganho indutivo é menor e oscila
  (Tab. 2, p. 14525).
- Sem saída estruturada: predições fora do espaço de rótulos são tratadas como
  rótulo aleatório (Apêndice B.2, p. 14534) — problema que o CategorySchema do
  FALCO elimina por construção.

## Ideias que gera para a tese
- Usar a perda do BERTimbau (small-loss) como detector barato de ruído do oráculo
  no braço A do E3' — diagnóstico post-hoc sem novas chamadas de LLM.
- Discutir no Cap. 5: FreeAL elimina o humano fechando o laço LLM↔SLM; FALCO
  elimina o LLM da SELEÇÃO (DRI-SL) e o mantém só na rotulagem — dois cortes de
  custo ortogonais.
- A autoria alucinada desta referência no bib (ver retorno da rodada R3) é em si
  um exemplo útil de por que a constituição exige validação contra fichamento.
