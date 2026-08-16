---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Yu2023Patron
title: "Cold-Start Data Selection for Better Few-shot Language Model Fine-tuning: A Prompt-based Uncertainty Propagation Approach"
authors: ["Yu, Yue", "Zhang, Rongzhi", "Xu, Ran", "Zhang, Jieyu", "Shen, Jiaming", "Zhang, Chao"]
year: 2023
venue: "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL), Volume 1: Long Papers"
doi: "10.18653/v1/2023.acl-long.141"
pdf: referencias-pdf/Yu2023Patron.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P2, P3]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: [propagacao-de-incerteza-por-prompt]   # PATRON: incerteza via prompt + PTR
uses_methods: [aprendizado-ativo, cold-start, few-shot, zero-shot, fine-tuning,
               amostragem-por-incerteza, entropia, clusterizacao]
datasets: [imdb, agnews, trec, yelp-full, yahoo-answers, dbpedia]
metrics: [acuracia, macro-f1]
tasks: [classificacao-de-texto]
models: [roberta-base, simcse]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: [Hacohen2022TypiClust, Sener2018, Yuan2020, Margatina2021]
contradicts: []
builds_on: [Lewis1994, Hacohen2022TypiClust]

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: compara
    target: DRI-SL
    note: "Mesmo problema do DRI-SL (seleção cold-start sem nenhum rótulo para
           classificação de texto), solução oposta: PATRON consulta um PLM com
           prompts zero-shot no pool INTEIRO para estimar incerteza; DRI-SL usa só
           estrutura do pool (cluster semântico + variedade lexical), reservando o
           LLM para rotular os itens já selecionados — diferença central de custo."
  - type: complementa
    target: oraculo-progressivo
    note: "Usa pseudo-rótulos de prompt calibrados por prior contextualizado para
           guiar a seleção; evidencia que o sinal zero-shot de um LM é utilizável
           antes de existir rótulo humano — mesmo insumo que o oráculo progressivo
           explora, mas no papel de seletor, não de rotulador."
  - type: motiva
    target: FALCO
    note: "Confirma em TEXTO (seis datasets) o achado de TypiClust: incerteza pura
           falha no cold start e ganhos crescem com o número de classes — cenário
           que o FALCO leva ao extremo (714 classes, orçamentos muito maiores)."
---

# PATRON — Cold-Start Data Selection for Better Few-shot Language Model Fine-tuning

## Resumo (5-8 linhas, com as MINHAS palavras)

Ataca a seleção de dados em cold start (zero rótulos iniciais) para fine-tuning
few-shot de PLMs. Estima a incerteza de cada exemplo com prompts (cloze) em
RoBERTa-base, calibrando os pseudo-rótulos com um prior contextualizado dos label
words; depois propaga essa incerteza pelos K vizinhos (kernel RBF sobre embeddings
SimCSE) para penalizar outliers. A diversidade vem da estratégia partition-then-
rewrite (PTR): K-means com k = orçamento B, seleção regularizada dentro de cada
cluster e reescrita iterativa que afasta escolhas de clusters vizinhos. Em seis
datasets de classificação de texto, com orçamentos de 32–128 rótulos, supera os
melhores baselines cold-start (incl. TypiClust e ALPS) em 3,4–6,9% em média, e com
128 rótulos recupera 91,0% (fine-tuning) e 92,1% (prompt-based) do desempenho
totalmente supervisionado.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Em cold start, a incerteza estimada pelo PLM é enviesada entre classes; métodos de incerteza pura chegam a perder do aleatório | §1, p. 2499–2500; Tabela 1 (coluna Uncertainty), p. 2503 | Cap. 2 fundamentação do cold start em texto; motiva DRI-SL |
| C2 | Incerteza via prompt zero-shot + calibração por prior contextualizado + propagação por vizinhança dá sinal de utilidade sem nenhum rótulo | §4.1 Eqs. (2)–(5); §4.2 Eqs. (6)–(7), p. 2502 | Cap. 2; ponte com o uso de confiança do LLM no oráculo progressivo (P3) |
| C3 | Diversidade por partição K-means (k = B) + reescrita entre clusters (PTR) evita redundância da consulta em lote | §4.3, Eqs. (8)–(10), Alg. 1, p. 2502–2503 | Cap. 2: família de seleção cluster-based a que o DRI-SL pertence |
| C4 | PATRON supera os melhores baselines cold-start em 3,4–6,9% em média (10 execuções, t-test 0,05/0,01) | Tabela 1, p. 2503; Abstract | Cap. 2/5 trabalhos relacionados |
| C5 | Ganhos maiores em datasets com mais classes (TREC, Yahoo!), onde cada classe recebe menos rótulos do orçamento fixo | §5.3 obs. (2), p. 2503 | Cap. 5 discussão: extrapolação para 714 classes |
| C6 | Variância entre execuções cai com seleção estratégica (vs amostragem aleatória few-shot que varia até 10%) | Fig. 1, p. 2499; §5.3 obs. (1) | Cap. 2: estabilidade como critério de qualidade do L0 |

## Números que posso citar
- Orçamentos avaliados: **|B| ∈ {32, 64, 128}** rótulos, seleção em uma rodada,
  RoBERTa-base, 10 execuções (§5.1, p. 2503).
- Ganho médio sobre o melhor baseline: **+6,9% (B=32), +5,0% (B=64), +3,4% (B=128)**
  — média de acurácia em 6 datasets (Tabela 1, p. 2503).
- Com **128 rótulos (<0,5% dos dados)**: **91,0%** do desempenho totalmente
  supervisionado com fine-tuning e **92,1%** com prompt-based learning (Abstract;
  §5.3).
- Exemplo em muitas classes: Yahoo! Answers (10 classes), B=32: PATRON **56,8 ± 1,0**
  vs 47,7 (ALPS), 46,8 (BERT-KM), 43,5 (aleatório), 22,0 (Coreset) (Tabela 1).
- TREC é desbalanceado — acurácia na Tabela 1 e F1 no Apêndice G.2 (nota da Tabela 1).
- PTR converge em **2–3 iterações** de reescrita (§4.3, p. 2503).

## Citações diretas (com página)
> "In PATRON, we design (1) a prompt-based uncertainty propagation approach to
> estimate the importance of data points and (2) a partition-then-rewrite (PTR)
> strategy to promote sample diversity when querying for annotations." (Abstract,
> p. 2499)

## Crítica / limitações (minha leitura)
- Estimar incerteza exige rodar o PLM com prompt sobre TODO o pool não rotulado —
  no pool de 50k do FALCO isso significa dezenas de milhares de inferências antes
  de rotular qualquer coisa; o DRI-SL evita exatamente esse custo.
- Depende de template e verbalizer manuais por dataset (nota 3, §3): com 714
  categorias de varejo, construir verbalizer é impraticável sem o CategorySchema —
  e aí o problema já vira o do oráculo FALCO.
- Orçamentos minúsculos (32–128) e uma rodada: regime muito distante dos braços de
  15k–35k do FALCO; a evidência não cobre AL progressivo em escala.
- Tudo em inglês; SimCSE e RoBERTa-base não têm equivalente direto avaliado para
  PT-BR (BERTimbau/embeddings próprios exigiriam revalidação).
- Sensível a hiperparâmetros (ρ, β, γ, m) fixados por validação que, a rigor, não
  existe em cold start real.

## Ideias que gera para a tese
- Posicionar DRI-SL vs PATRON no Cap. 2 como as duas rotas do cold start textual:
  estrutura-do-pool (sem LLM) vs sinal-zero-shot-do-LM (com LLM no pool inteiro);
  comparar custo de inferência por item selecionado.
- A calibração por prior contextualizado (Eq. 3–4) é candidata a melhorar a
  confiança reportada pelo oráculo LLM do FALCO sob classes raras.
- Usar C5 como argumento de que o benefício de seleção estratégica CRESCE com o
  número de classes — extrapolação favorável ao cenário de 714 classes.
