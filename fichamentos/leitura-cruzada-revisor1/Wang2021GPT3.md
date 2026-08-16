---
id: Wang2021GPT3
title: "Want To Reduce Labeling Cost? GPT-3 Can Help"
authors: ["Wang, Shuohang", "Liu, Yang", "Xu, Yichong", "Zhu, Chenguang",
          "Zeng, Michael"]
year: 2021
venue: "Findings of EMNLP 2021"
doi: "10.18653/v1/2021.findings-emnlp.354"
pdf: referencias-pdf/Wang2021GPT3.pdf
paper_type: metodo
pillars: [P3, LCE]
status: fichado
proposes: []
uses_methods: [llm-como-oraculo, few-shot, fine-tuning, menor-confianca,
               aprendizado-ativo]
datasets: [trec, agnews]
metrics: [acuracia, custo-por-rotulo]
tasks: [classificacao-de-texto]
models: [gpt-3, roberta, pegasus]
extends: []
compares_with: []
contradicts: []
builds_on: [Settles2009]
falco_relation:
  - type: fundamenta
    target: oraculo-progressivo
    note: "Primeiro trabalho a tratar explicitamente o LLM como ROTULADOR de
           baixo custo com contabilidade de custo por rótulo (API vs
           crowdsourcing) — é a origem da linha que o oráculo LLM do FALCO
           continua, e a referência de custo humano ($0,11/50 tokens) reusada
           por FreeAL2023."
  - type: fundamenta
    target: LCE
    note: "As curvas desempenho × custo em dólares (Fig. 3) são o precedente
           direto de avaliar rotulagem pelo par (qualidade, custo) — a
           motivação de uma métrica integrada como a LCE."
  - type: complementa
    target: FALCO
    note: "A rotulagem ativa (humano re-rotula os itens de MENOR confiança do
           GPT-3) é um desenho híbrido humano+LLM sob orçamento fixo que o
           FALCO não explora — extensão natural para trabalhos futuros."
---

# Want To Reduce Labeling Cost? GPT-3 Can Help

## Resumo (5-8 linhas, com as MINHAS palavras)
Propõe usar o GPT-3 (Davinci, few-shot) como rotulador barato de dados não
anotados para treinar modelos menores implantáveis (RoBERTa para NLU, PEGASUS
para NLG), com análise explícita de custo: a API custava ~$0,002 por rótulo
contra $0,11 do crowdsourcing. Em 9 tarefas, atingir o mesmo desempenho
downstream custa 50-96% menos com rótulos do GPT-3 do que com rótulos humanos em
regime de orçamento baixo; os modelos treinados com esses rótulos ruidosos ainda
superam o próprio GPT-3 few-shot (justificado como self-training, com limite
teórico de erro). Propõe ainda misturar rótulos humanos e de GPT-3 sob orçamento
fixo e uma rotulagem ativa em que humanos re-anotam os itens em que o logit do
GPT-3 indica menor confiança — melhor que a mistura aleatória.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Rotular com GPT-3 economiza 50-96% do custo para o mesmo desempenho downstream (orçamento baixo) | Abstract p. 4195; §3.3.1, Fig. 3, p. 4199-4201 | Cap. 2: fundamento econômico do oráculo LLM |
| C2 | Modelos in-house treinados com rótulos do GPT-3 superam o GPT-3 few-shot em inferência direta (efeito self-training, Teorema 2) | §2.3, p. 4198; §3.3.2, Fig. 4, p. 4200-4201 | Cap. 2/Cap. 5: por que treinar BERTimbau em vez de servir o LLM |
| C3 | O logit do primeiro token gerado funciona como escore de confiança: top 10% dos logits têm 90-95% de acurácia | §3.3.3, Fig. 5, p. 4201 | Cap. 5: sinal de confiança do oráculo (aplicável ao FALCO?) |
| C4 | Rotulagem ativa (humano re-rotula a menor confiança) supera mistura aleatória humano+GPT-3 | §3.3.3, Fig. 5, p. 4201 | Cap. 5: híbrido humano+oráculo como trabalho futuro |
| C5 | Com orçamento amplo o rótulo humano domina (qualidade); com orçamento restrito o GPT-3 é mais custo-efetivo | §3.3.1, p. 4201 | Cap. 5: condição de contorno do argumento de custo do FALCO |
| C6 | Menos shots = prompt mais barato = mais rótulos sob o mesmo orçamento; qualidade vs quantidade é um trade-off por orçamento | §2.2 p. 4197-4198; §3.3.2 p. 4201 | Cap. 3: análogo ao dimensionamento de prompt do oráculo |

## Números que posso citar
- Custo por rótulo SST-2 (preços OpenAI 2021, quote $400/10M tokens): GPT-3
  2-shot $2,3e-3 vs humano $0,11 (mínimo $0,11 por 50 tokens, Google Cloud
  Tiers 1-2) (Tab. 1, p. 4196).
- SST-2: RoBERTa-large com rótulos GPT-3 de $1,1 empata com rótulos humanos de
  $27,5 → economia de 96% (§3.3.1, p. 4201).
- Gigaword (sumarização): PEGASUS com rótulos GPT-3 de $4,4 empata com humanos
  de $70,4 → economia de 93,8% (§3.3.1, p. 4201).
- TREC: rotulagem ativa eleva a acurácia de 77% para 80% sob o mesmo orçamento
  de $2,2 (§3.3.3, p. 4201).
- Escala: até 5.120 instâncias rotuladas por tarefa; resultados = média de 3
  execuções (Fig. 3, p. 4199).

## Citações diretas (com página)
> "to make the downstream model achieve the same performance on a variety of
> NLU and NLG tasks, it costs 50% to 96% less to use labels from GPT-3 than
> using labels from humans" (Abstract, p. 4195)

> "GPT-3 is not reliable enough yet at labeling 'high-stakes' cases, e.g.
> identifying toxic language, but is more suitable for low-stakes labeling"
> (§5, p. 4202)

## Crítica / limitações (minha leitura)
- Os rótulos "humanos" são simulados pelos gold labels dos datasets — o custo
  humano é estimado de tabela de preços, não medido; a comparação de qualidade
  humano vs LLM é, na prática, gold vs LLM (como no E3' braços B vs A).
- Preços de 2021 (GPT-3 Davinci) estão obsoletos; a razão custo LLM/humano só
  melhorou desde então, o que reforça a direção mas invalida os valores
  absolutos.
- Tarefas em inglês com 2-14 classes; a extração de confiança pelo logit do
  primeiro token não transfere diretamente para saída estruturada com 621
  rótulos (tokenização multi-token dos nomes de classe).
- O Teorema 2 depende de suposição de consistência/expansão forte e de erro
  máximo por classe limitado — frágil sob desbalanceamento severo com classes
  raras (justamente o cenário FALCO).

## Ideias que gera para a tese
- Reproduzir a curva desempenho × custo (Fig. 3) para o FALCO no Cap. 5 — o
  formato de apresentação é diretamente reutilizável para a LCE.
- Citar C5 como delimitação honesta: o argumento de custo do FALCO vale no
  regime de orçamento restrito, não assintótico.
- Explorar (trabalho futuro) a re-rotulagem humana ativa dos itens de menor
  confiança do oráculo — encaixa no gate humano do método Maestro.
