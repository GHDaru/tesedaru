---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Wang2021GPT3Labeling
title: "Want To Reduce Labeling Cost? GPT-3 Can Help"
authors: ["Wang, Shuohang", "Liu, Yang", "Xu, Yichong", "Zhu, Chenguang", "Zeng, Michael"]
year: 2021
venue: "Findings of the Association for Computational Linguistics: EMNLP 2021, pp. 4195-4205"
doi: "10.18653/v1/2021.findings-emnlp.354"
pdf: referencias-pdf/Wang2021GPT3Labeling.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P3]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: []               # rotulagem-ativa-gpt3-humano (termo ausente do vocabulário; ver relatório)
uses_methods: [llm-como-oraculo, few-shot, menor-confianca, aprendizado-ativo, fine-tuning]
datasets: [agnews, trec]   # também: SST-2, CB, RTE, DBPedia, Gigaword, XSum, SQuAD (fora do vocabulário)
metrics: [acuracia, custo-por-rotulo]  # também: ROUGE-L (fora do vocabulário)
tasks: [classificacao-de-texto]        # também NLG (sumarização, geração de pergunta)
models: [gpt-3-davinci, roberta-large, pegasus-large]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Primeiro trabalho (auto-declarado) a ANALISAR O CUSTO do LLM como
           rotulador e o mix LLM+humano sob orçamento fixo — é o ancestral direto
           do eixo custo-por-rótulo do P3. A 'active labeling' deles (humano
           re-rotula os casos de menor confiança do GPT-3) é o dual do FALCO
           (LLM anota o que o seletor pede). Fundamenta a moldura de AL como
           alocação de recursos sob orçamento (ancoragem PPGMNE) e a tabela de
           custo do Cap. 5."
---

# Want To Reduce Labeling Cost? GPT-3 Can Help

## Resumo (5-8 linhas, com as MINHAS palavras)
Usa o GPT-3 (Davinci, few-shot) como rotulador barato para treinar modelos
menores implantáveis (RoBERTa-large para NLU, PEGASUS para NLG) e mede TUDO em
dólares: para atingir o mesmo desempenho do rótulo humano, o rótulo GPT-3 custa
50% a 96% menos, especialmente em orçamento baixo. Propõe ainda o mix
GPT-3+humano sob orçamento fixo (dual supervision) e a "active labeling": o
humano re-rotula apenas os casos em que o logit do GPT-3 (confiança) é mais
baixo. Mostra também, com justificativa teórica via self-training, que o modelo
treinado nos rótulos do GPT-3 pode superar o próprio GPT-3 few-shot. Com
orçamento amplo, porém, o rótulo humano volta a dominar pela qualidade.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Rotular com GPT-3 custa ~50x menos que humano (SST-2: $0,002 vs $0,11 por rótulo) e 50-96% menos para desempenho igual | §1 e §2.1, Tab. 1, p. 4196; §3.3.1, p. 4200-4201 | Cap. 1/5: número-âncora da motivação de custo do oráculo LLM |
| C2 | Modelo pequeno treinado nos rótulos do LLM supera o próprio LLM few-shot (com limite teórico via expansão/self-training) | §2.3, Teor. 2, p. 4198; §3.3.2, Fig. 4, p. 4201 | Cap. 2/5: fundamenta destilar o oráculo em classificador implantável |
| C3 | A confiança (logit) do GPT-3 correlaciona com a acurácia do rótulo: top-10% logits têm 90-95% de acurácia | §3.3.3, Fig. 5, p. 4201 | Cap. 5: precedente do uso da confiança do oráculo como sinal de qualidade |
| C4 | "Active labeling": humano re-rotula os casos de menor confiança do LLM e ganha desempenho sob o mesmo orçamento (TREC 77→80% com $2,2) | §2.4 e §3.3.3, Fig. 5, p. 4201 | Cap. 2 (lacunas) e futuros: papel humano remanescente (item 16 do parecer R6) |
| C5 | Com orçamento amplo/ilimitado o rótulo humano domina pela qualidade; LLM vence no regime de orçamento restrito | §3.3.1, p. 4201 | Cap. 5: condição de contorno honesta para a claim de custo do FALCO |
| C6 | Mais shots melhoram qualidade mas encarecem linearmente o rótulo (custo = #tok x 4e-5 x (n+1)); menos shots rotulam mais sob o mesmo orçamento | Tab. 1, p. 4196; §3.3.2, p. 4201 | Cap. 5: análogo de 2021 do nosso trade-off tokens-por-rótulo (decomposição pedida no item 15 do R6) |

## Números que posso citar
- Tab. 1 (p. 4196): custo por rótulo GPT-3 (API 2021, $4e-5/token): SST-2 2-shot
  $0,0012; AGNews 2-shot $0,0038; TREC 2-shot $0,0023 — vs humano $0,11 por 50
  tokens (Google Cloud, média Tier 1&2).
- SST-2: mesmo desempenho com $1,1 de rótulos GPT-3 vs $27,5 de rótulos humanos
  (96% de economia); Gigaword: $4,4 vs $70,4 (93,8%) (§3.3.1, p. 4201).
- Active labeling: TREC de 77% para 80% de acurácia sob mesmo orçamento de $2,2
  (§3.3.3, p. 4201).
- Protocolo: até 5.120 instâncias rotuladas por dataset; 3 seeds; shots {2,4,8}
  NLU e {1,2,3} NLG; mix de orçamento {0,25,50,75,100}% (§3.2, p. 4200).

## Citações diretas (com página)
> "to make the downstream model achieve the same performance on a variety of NLU and NLG tasks, it costs 50% to 96% less to use labels from GPT-3 than using labels from humans" (Abstract, p. 4195)

> "when the budget is ample or unlimited, fully human labeling will dominate in performance due to higher quality. However, when the budget is limited, GPT-3 labeling is a more cost-effective choice." (§3.3.1, p. 4201)

> "GPT-3 is not reliable enough yet at labeling 'high-stakes' cases [...] but is more suitable for low-stakes labeling" (§5, p. 4202)

## Crítica / limitações (minha leitura)
- Rotulagem em massa aleatória/completa: o GPT-3 não escolhe o que rotular — a
  "active labeling" seleciona para o HUMANO, não para o LLM; o laço de AL
  clássico (seletor→oráculo) fica de fora. É exatamente a composição que o FALCO
  (e depois LLMaAA) fazem.
- Custos de 2021 (Davinci $4e-5/token; humano via Google Cloud) — usar como
  ordem de grandeza histórica, nunca como número corrente; a tese recalcula com
  preços NIM/atuais.
- "Rótulo humano" simulado pelos gabaritos dos datasets — o custo humano é
  estimado, não medido (mesma fragilidade que apontei em Kholodna2024).
- Tarefas com poucas classes (2-14); confiança = logit do primeiro token, sem
  saída estruturada nem espaço de 714 classes.
- Contaminação: benchmarks públicos possivelmente vistos no pré-treino do GPT-3
  não são discutidos.

## Ideias que gera para a tese
- C1+C6 abrem a linhagem do argumento de custo: Wang21 (2021, custo por rótulo)
  → Kholodna2024 (amortização em lote) → FALCO (custo instrumentado por anotação
  com cache). Contar essa progressão na 2.3.4.
- C3 sustenta discutir a confiança do oráculo como subproduto útil; contrastar
  com viés de autoavaliação (item 10 do parecer R6 — Farquhar/Kossen): a
  correlação existe, mas é enviesada quando o mesmo modelo seleciona.
- C5 vira frase de honestidade no Cap. 5: o ganho de custo do FALCO vale no
  regime de orçamento restrito, como já era verdade em 2021.
