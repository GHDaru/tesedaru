---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: FreeAL2023
title: "FreeAL: Towards Human-Free Active Learning in the Era of Large Language Models"
authors: ["Xiao, Ruixuan", "Dong, Yiwen", "Zhao, Junbo", "Wu, Runze", "Lin, Minmin", "Chen, Gang", "Wang, Haobo"]
year: 2023
venue: "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 14520-14535"
doi: "10.18653/v1/2023.emnlp-main.896"
pdf: referencias-pdf/FreeAL2023.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P3]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: []               # método proposto: FreeAL (termo ausente do vocabulário; ver relatório)
uses_methods: [aprendizado-ativo, llm-como-oraculo, destilacao-ativa, few-shot, zero-shot, entropia, cold-start]
datasets: [trec]           # também: SST-2, MR, SUBJ, CoNLL03, Medical Abstract, BC5CDR (fora do vocabulário)
metrics: [acuracia, custo-por-rotulo]  # também: F1 (micro) nos NER (fora do vocabulário)
tasks: [classificacao-de-texto]
models: [gpt-3.5-turbo, roberta-base, biomed-roberta-base]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: []          # baselines empíricos (Random/Entropy/CAL) sem chave no repositório
contradicts: []
builds_on: []
falco_relation:
  - type: compara
    target: FALCO
    note: "Vizinho direto exigido pelo parecer R6 (Bloco C, item 9 / Dom-M1) na
           tabela de lacunas. FreeAL elimina o humano do laço via colaboração
           LLM(anotador)-SLM(filtro) com refinamento iterativo de rótulos; FALCO
           difere em: progressão de oráculos com gate de custo, espaço FECHADO de
           714 classes (FreeAL: 2-6 classes + NER), texto curto PT-BR de varejo,
           saída estruturada (CategorySchema) e contabilidade de custo por rótulo
           (FreeAL não reporta custo de API). Confronto central do Cap. 2."
---

# FreeAL: Towards Human-Free Active Learning in the Era of Large Language Models

## Resumo (5-8 linhas, com as MINHAS palavras)
Reformula o aprendizado ativo sem NENHUM anotador humano: o LLM (GPT-3.5-Turbo)
atua como anotador ativo e um SLM (RoBERTa) como aluno/filtro. No round inicial,
o LLM gera suas próprias demonstrações ("self-generated demonstration") imitando
amostras não rotuladas; anota o corpus por ICL; o SLM treina com robustez a ruído
(seleção por GMM sobre a perda + regularização de consistência), filtra um pool
limpo por menor perda + k-medoids e o devolve como demonstrações para o LLM
re-anotar os casos ruidosos. Em 8 benchmarks, o laço colaborativo melhora tanto o
LLM quanto o SLM sem supervisão humana, aproximando-se do desempenho supervisionado
em tarefas simples e superando AL tradicional com 20-50% de rótulos humanos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL "human-free": LLM como anotador ativo + SLM como filtro supera zero-shot ICL do próprio LLM (+3,44 SST-2; +34,6 SUBJ; +23,1 BC5-D) | §5.2, Tab. 3, p. 14526 | Cap. 2 (tabela de lacunas): vizinho a confrontar; Cap. 5: contraste com oráculo progressivo |
| C2 | FreeAL supera AL tradicional (Random/Entropy/CAL) mesmo quando estes usam 20-50% de anotação humana | §5.3.1, Tab. 5 e Fig. 1, p. 14527 | Cap. 2: evidência de que o LLM-oráculo desloca a fronteira custo-desempenho do AL |
| C3 | A qualidade do laço depende de demonstrações filtradas: seleção por menor perda supera seleção por entropia e aleatória no papel de feedback ao LLM | §5.3.2, Tab. 6, p. 14527 | Cap. 2/5: discussão de acoplamento seletor-oráculo (paralelo com DRI-SL) |
| C4 | Sem rótulo humano o método fica refém da competência do LLM no domínio: em tarefas difíceis/eccêntricas a anotação inicial pode falhar | Limitations, p. 14528 | Cap. 5: justifica o gate E0 do FALCO (validar o oráculo antes de confiar nele) |
| C5 | 4 rounds de interação bastam empiricamente; mais rounds melhoram com mais custo | §5.2, p. 14526 | Cap. 5: contraste com a política de parada do FALCO |
| C6 | O refino iterativo melhora os pseudo-rótulos rodada a rodada: no conjunto de treino (transdutivo) o SST-2 sai de 88,93 (zero-shot, round 0) para 95,49 (RoBERTa anotado pelo round 3, round 4) | §5.2, Tab. 1, p. 14525 | Cap. 5: contraste com o FALCO, que rotula cada item uma única vez, sem realimentação |
| C7 | O custo de anotação por exemplo do LLM fica ~2 ordens de grandeza abaixo do humano (SST-2: US$ 1,2e-3 vs US$ 0,11) | Apêndice A.2, Tab. 7, p. 14532 | Cap. 2: fundamenta a métrica custo-por-rotulo e o orçamento do FALCO; corrige a leitura de que o paper não mede custo |
| C8 | Estratégia multi-rodada que anota apenas 10% do pool por rodada chega perto do FreeAL completo (SST-2 93,76 vs 94,66; MR 88,95 vs 90,20) com fração do custo | Apêndice A.2, Tab. 8, p. 14532 | Cap. 5: paralelo com o caráter progressivo/orçado do oráculo do FALCO |

## Números que posso citar
- Test set, GPT-3.5-Turbo, m=10 exemplos in-context, média de 3 execuções (Tab. 3, p. 14526):
  FreeAL 95,91 (SST-2), 93,10 (MR), 90,27 (SUBJ), 79,80 (TREC) vs zero-shot ICL
  92,47 / 90,05 / 55,65 / 77,20; ganhos de +12,9 (BC5CDR-Chemical) e +23,1 (BC5CDR-Disease) em F1.
- SLM (RoBERTa) FreeAL vs fine-tuning supervisionado (Tab. 3): 94,66 vs 94,89 (SST-2);
  94,45 vs 95,95 (SUBJ); mas 76,12 vs 88,11 (CoNLL03) e 58,90 vs 75,38 (BC5-D) — gap grande em tarefas difíceis.
- Tab. 5 (p. 14527), SST-2/MR: FreeAL 94,66/90,20 sem humano vs Entropy com 50% de
  rótulos humanos 94,29/90,00 e CAL 50% 94,56/89,75.
- Ablação (Tab. 6, p. 14527): sem robust self-training o SLM cai de 94,66→89,18 (SST-2).
- Datasets: 4-6 classes nas tarefas de classificação; MA com 5 classes (Tab. 4, p. 14526).

## Citações diretas (com página)
> "FreeAL surpasses all the active learning rivals and achieves near-supervised performance without human annotation." (legenda da Fig. 1, p. 14520)

> "the effectiveness of FreeAL largely hinges on the strong ability of LLMs. For some domains that are extremely challenging or eccentric, the commonly adopted GPT-3.5-Turbo nowadays may fail to provide a qualified initial annotation" (Limitations, p. 14528)

## Crítica / limitações (minha leitura)
- Sem contabilidade de custo: nenhum número de tokens, chamadas ou dólares — o
  "free" refere-se ao humano, não ao orçamento de API. O FALCO instrumenta
  exatamente o que FreeAL omite (custo por rótulo, cache).
- Espaço de rótulos pequeno (2-6 classes); nada indica que a autogeração de
  demonstrações escale para 714 classes de varejo — o prompt teria de cobrir o
  esquema inteiro.
- Sem saída estruturada validável: o parsing da resposta do LLM não é tratado
  (nosso achado de taxa de inválidos não tem correspondente aqui).
- A transdução exige re-anotar todo o corpus por rounds — em ~231k textos isso
  multiplica o custo, enquanto o FALCO anota apenas o que o seletor pede.
- Inglês e benchmarks públicos (risco de contaminação do LLM não discutido).

## Ideias que gera para a tese
- Par com Zhang2023LLMaAA na tabela de lacunas: FreeAL = eixo "sem humano,
  transdutivo, sem custo medido"; FALCO = "orçamento explícito, espaço fechado
  gigante, custo instrumentado".
- C4 é munição direta para justificar o E0-como-gate: até o paper "human-free"
  admite que sem validação o laço desaba em domínios difíceis.
- A seleção de demonstrações por menor perda + k-medoids ecoa a lógica de
  representatividade do DRI-SL — citar em 2.3 ao discutir acoplamento
  seletor-oráculo.
