---
id: Zhang2025
title: "Applying LLMs to Active Learning: Toward Cost-Efficient Cross-Task Text Classification Without Manually Labeled Data"
authors: ["Zhang, Yejian", "Takada, Shingo"]
year: 2025
venue: "International Journal of Intelligent Systems (Wiley), vol. 2025, artigo 6472544, 14 pp."
doi: "10.1155/int/6472544"
pdf: referencias-pdf/Zhang2025.pdf

paper_type: metodo
pillars: [P3, P4]
status: fichado

proposes: [llm-como-oraculo]
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza,
               query-by-committee, entropia, selecao-por-diversidade,
               core-set-selection, saida-estruturada, rotulagem-em-lote]
datasets: [imdb, agnews, jigsaw-toxic]
metrics: [acuracia, macro-f1, custo-por-rotulo]
tasks: [classificacao-de-texto]
models: [gpt-4o, roberta-base, svm, random-forest]

extends: []
compares_with: []
contradicts: []
builds_on: [Settles2009]

falco_relation:
  - type: compara
    target: FALCO
    note: "Vizinho mais próximo na frente 'anotador': o LLM substitui o humano
           dentro do laço de aprendizado ativo, rotulando o que a estratégia de
           seleção escolheu, e um modelo pequeno é treinado com esses rótulos.
           O FALCO difere em três pontos: progressão de oráculos entre fases,
           espaço fechado de 621 rótulos imposto na saída, e gate de parada
           pré-registrado com instrumentação de custo."
  - type: fundamenta
    target: LCE
    note: "Traz a conta que a tese também persegue: reter mais de 93% do
           desempenho gastando cerca de 6% do tempo e do dinheiro (Resumo, p. 1)."
---

# Applying LLMs to Active Learning (Zhang e Takada, 2025)

## Resumo (com as minhas palavras)
Os autores montam um laço de aprendizado ativo em que o GPT-4o ocupa o lugar do
anotador humano: a estratégia de consulta escolhe as instâncias, o modelo de
linguagem devolve o rótulo por meio de um prompt estruturado, e um classificador
pequeno é retreinado a cada rodada. Comparam quatro estratégias de seleção em
três tarefas de classificação de texto em inglês. O argumento central é de
custo: em vez de mandar a base inteira para o modelo grande, manda-se só o que
a seleção apontou — o desempenho fica próximo, e a conta cai a uma fração.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Um laço de aprendizado ativo com LLM no lugar do anotador humano atinge alta acurácia sem NENHUM rótulo humano | Resumo, p. 1; §4.4, p. 8 | Cap. 2: vizinho direto do FALCO na frente do oráculo |
| C2 | Contra o uso direto do GPT para classificar tudo, a abordagem retém **mais de 93%** do desempenho gastando cerca de **6%** do tempo computacional e do custo monetário | Resumo, p. 1 | Cap. 2 e Cap. 5: é a comparação de custo que a tese também faz |
| C3 | O oráculo é disciplinado por prompt estruturado em três componentes (domínio, tipo de tarefa, critério de classificação) mais a consulta, com a ordem explícita "retorne apenas o rótulo" | §3.2 e Tab. 1, p. 5 | Cap. 3: precedente para a saída restrita do CategorySchema |
| C4 | Determinismo do oráculo obtido por configuração: GPT-4o com temperatura 0 e limite de 10 tokens em todas as chamadas | §3.2, p. 5 | Cap. 3: mesma escolha do nosso E0/E5 — reforça que é prática da área |
| C5 | Entropia com diversidade foi a melhor estratégia em duas das três tarefas; densidade de informação levou vantagem na terceira | §4.4, pp. 7--8; Figs. 6--8 | Cap. 2/5: nenhuma estratégia domina — coerente com o que medimos |
| C6 | Os números finais saem com MUITO poucos rótulos: 85,42% de acurácia com 175 instâncias rotuladas (IMDB), 84,88% com 200 (AGnews) e 86,44% com 145 (Jigsaw) | §4.4, p. 8 | Cap. 5: referência externa de ordem de grandeza para o orçamento de rótulos |
| C7 | O protocolo escolhe o ponto de corte por PLATÔ da curva de aprendizado (25ª, 30ª e 19ª iterações), e não por um orçamento fixado antes | §4.4, pp. 7--8 | Cap. 3/6: contraste honesto com o nosso gate pré-registrado — decidir na curva é post hoc |

## Números que posso citar
- Oráculo: **GPT-4o**, temperatura **0**, `max_tokens = 10` em todas as chamadas
  de API (§3.2, p. 5).
- Semente inicial de **50 instâncias** (0,625% do conjunto de treino), lote de
  **5** por rodada e **100 iterações** por laço (§4.3.3, p. 7).
- Validação cruzada de **5 dobras**, 80% treino e 20% teste (§4.3.3, p. 7).
- Conjuntos: IMDB e AGnews com **10.000** instâncias cada; Jigsaw com **5.000**
  tóxicos e **5.000** não tóxicos, após remover textos com cinco palavras ou
  menos (§4.2, p. 5).
- Ambiente: Google Colab com **NVIDIA A100-SXM4-40GB** (§4.3.2, p. 7).
- Comitê da estratégia por incerteza: **quatro** classificadores em votação
  suave — SVM linear, árvore de decisão, floresta aleatória (100 estimadores) e
  regressão logística (§3.1.1, p. 4).
- Métricas: acurácia como principal, com F1 e revocação como apoio; Macro F1
  definido para o caso multiclasse (§4.3.1, Eqs. 3--7, p. 5).

## Citações diretas (com página)
> "our approach retains over 93% of its classification performance while
> requiring only approximately 6% of the computational time and monetary cost"
> (Resumo, p. 1)

## Crítica / limitações (minha leitura)
- **Três tarefas, todas em inglês, e duas delas binárias.** O espaço de rótulos
  maior tem 4 classes (AGnews). Nada aqui informa o comportamento com 621
  rótulos e cauda longa, que é o nosso caso — a diferença de escala é de duas
  ordens de grandeza.
- **Textos longos.** As distribuições de comprimento (Figs. 2--4, p. 6) mostram
  resenhas e notícias de dezenas a centenas de palavras; a tese trabalha com
  descrições de produto de poucas palavras, onde o contexto é escasso.
- **O ponto de parada é escolhido olhando a curva** (C7). É legítimo como
  relato, mas não é critério pré-registrado: o número final depende de onde o
  analista viu o platô. É exatamente a fragilidade que o nosso gate pretende
  evitar — e vale citar quando defendermos o pré-registro.
- **Não há medida do erro do oráculo.** O GPT rotula e os rótulos são usados;
  o trabalho não separa quanto do desempenho final se perde por ruído de
  anotação, que é a pergunta do nosso par A--B.

## Ideias que gera para a tese
- C2 é a citação de custo mais direta que temos de um vizinho publicado: "mais
  de 93% do desempenho por cerca de 6% do custo". Serve de âncora externa
  quando apresentarmos a nossa própria conta.
- O contraste do C7 rende um parágrafo de método: eles param no platô
  observado, nós paramos por critério fixado antes de olhar os dados. Dá para
  usar a favor do rigor da tese sem desqualificar o trabalho deles.
