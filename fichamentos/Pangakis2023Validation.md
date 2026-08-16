---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Pangakis2023Validation
title: "Automated Annotation with Generative AI Requires Validation"
authors: ["Pangakis, Nicholas", "Wolken, Samuel", "Fasching, Neil"]
year: 2023
venue: "arXiv:2306.00176 [cs.CL] (preprint, v1 de 31/05/2023)"
doi: "10.48550/arXiv.2306.00176"
pdf: referencias-pdf/Pangakis2023Validation.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: avaliacao
pillars: [P3]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: []               # workflow-de-validacao-llm, consistency-score (termos ausentes do vocabulário; ver relatório)
uses_methods: [llm-como-oraculo, zero-shot]
datasets: []               # 11 datasets não públicos de ciências sociais (sem nomes canônicos)
metrics: [acuracia]        # também: precisão, recall, F1 (fora do vocabulário)
tasks: [classificacao-de-texto]
models: [gpt-4]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: []
contradicts: [Gilardi2023]
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Base normativa do bloco custo/validação do parecer R6 (Bloco C, item
           12 vizinho): TODO uso de LLM como anotador deve ser validado contra
           rótulos humanos, tarefa a tarefa, porque o desempenho é altamente
           heterogêneo (9/27 tarefas com precisão ou recall < 0,5 mesmo com
           GPT-4). Fundamenta o E0-como-gate do FALCO (validar o oráculo contra
           gabarito antes do laço) e a leitura honesta dos resultados do P3."
  - type: complementa
    target: oraculo-progressivo
    note: "O consistency score (re-rotular >=7x com temperatura 0,6; consistência
           correlaciona com acurácia) é um mecanismo de confiança do oráculo
           independente da autoavaliação — alternativa a discutir nos futuros."
---

# Automated Annotation with Generative AI Requires Validation

## Resumo (5-8 linhas, com as MINHAS palavras)
Posição metodológica + avaliação em larga escala: como o desempenho do LLM
anotador varia com prompt, idiossincrasias do texto e dificuldade conceitual — e
essas causas persistem mesmo com LLMs melhores — qualquer anotação automatizada
deve ser validada contra rótulos humanos de qualidade, tarefa a tarefa. Propõem
um workflow de 5 passos (codebook → especialistas rotulam subconjunto → LLM
anota com o MESMO codebook → refinar codebook se fraco → testar em held-out) e o
validam replicando 27 tarefas de anotação de 11 datasets NÃO públicos (evitando
contaminação) com GPT-4: mediana boa (acurácia 0,850; F1 0,707), mas um terço
das tarefas com precisão ou recall abaixo de 0,5. Introduzem o consistency score
(voto modal de >=7 rotulagens a temperatura 0,6) como detector de casos difíceis.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Desempenho do LLM anotador é altamente contingente ao dataset e à tarefa: mediana F1 0,707, mas 9/27 tarefas com precisão OU recall < 0,5 (3/27 com ambos) | §3, Tab. 1 e Fig. 2, pp. 7-8 | Cap. 2/5: contra-peso a claims otimistas; justifica validar o oráculo por tarefa (E0) |
| C2 | Validação deve usar dados não contaminados: benchmarks públicos podem estar no pré-treino e inflar desempenho por memorização | §1, p. 3 | Cap. 3/5: vantagem metodológica do corpus proprietário de varejo (não público) |
| C3 | Consistency score: rotular >=7x a temperatura 0,6 e tomar o voto modal; consistência 1,0 tem acurácia +19,4 pp vs <1,0; 85,1% das amostras são totalmente consistentes | §3.1, Fig. 3, pp. 9-10 | Cap. 5/futuros: sinal de confiança do oráculo sem autoavaliação |
| C4 | Refinar o prompt/codebook ajuda pouco: 1 rodada de atualização melhora acurácia/F1 modestamente; recall frequentemente piora | §3.2, Fig. 4, pp. 11-12 | Cap. 5: modera expectativas de prompt engineering como alavanca |
| C5 | Validação exige 250-1.250 amostras humanas aleatórias (mais se classes raras) e as mesmas instruções (codebook) para humano e LLM | §2, fn. 7-8, pp. 5-6 | Cap. 3: dimensionar o gabarito do E0; mesma instrução para oráculo e gabarito |
| C6 | Variação intra-dataset: F1 de 0,259 a 0,811 em duas tarefas do MESMO dataset (dif. 0,552) | §3, p. 10 | Cap. 2: 'o LLM anota bem' não é propriedade do dataset, é da tarefa |
| C7 | Anotação com GPT-4 é barata e rápida: >200 mil textos, 27 tarefas, ~$420; ~2-3h por 1.000 amostras (7 iterações) | §2, pp. 6-7 | Cap. 5: âncora externa de ordem de custo para a tabela de custo |

## Números que posso citar
- Tab. 1 (p. 7; GPT-4, 27 tarefas binárias, 11 datasets não públicos, held-out):
  acurácia mediana 0,850 (mín 0,674; máx 0,981); F1 mediana 0,707 (mín 0,059!);
  precisão mediana 0,650 (mín 0,033); recall mediana 0,829.
- 20/27 tarefas com recall > precisão (Fig. 2, p. 8); 8/27 com precisão E recall > 0,7.
- Consistency score (§3.1): +19,4 pp acurácia, +16,4 pp TPR, +21,4 pp TNR para
  consistência 1,0; 85,1% das amostras com consistência 1,0.
- Custo total ~US$ 420 para >200.000 amostras x 7 rotulagens (GPT-4 API, 2023).

## Citações diretas (com página)
> "any automated annotation process using an LLM must validate the LLM's performance against labels generated by humans" (Abstract, p. 1)

> "for a full one-third of tasks, the LLM either missed at least half of the true positive cases, had more false positives than true positives, or both" (§3, pp. 7, 10)

> "these tests are plausibly affected by contamination [...] strong performance may reflect memorization, which will not generalize to new datasets and tasks" (§1, p. 3)

## Crítica / limitações (minha leitura)
- Tarefas todas binarizadas (dimensões separadas) — a dificuldade de um espaço
  fechado de 714 classes é de outra natureza; os números não transferem, o
  PRINCÍPIO (validar por tarefa) sim.
- Zero-shot com codebook, sem demonstrações nem saída estruturada; parte da
  variância pode ser de formato, não de conceito (nosso resultado de taxa de
  inválidos separa isso).
- Preprint não revisado por pares (v1); tratar como posição metodológica bem
  evidenciada, citando os números com a condição 'GPT-4, tarefas de ciências
  sociais, 2023'.
- Consistency score custa 7x mais chamadas — colide com o objetivo de custo do
  FALCO; se citado como alternativa, citar junto o multiplicador de custo.
- Ground truth = rótulos humanos originais dos estudos, eles próprios ruidosos
  (os autores reconhecem no caso de uso 1, Tab. 2, p. 13).

## Ideias que gera para a tese
- É a fonte normativa perfeita para abrir a subseção de validação do oráculo:
  citar C1+C6 e então mostrar que o FALCO operacionaliza a recomendação (E0 com
  gabarito, mesmas instruções, corpus não contaminado — C2).
- C4 dialoga com o efeito do instrumento (P3): eles mexem no codebook e ganham
  pouco; nós mudamos o INSTRUMENTO de saída e medimos efeito — distinguir os dois
  eixos no Cap. 5.
- Contrapor a Gilardi2023 (ChatGPT supera MTurk): Pangakis mostra que a
  generalização dessa claim depende da tarefa — usar o par como exemplo de
  contradição divulgada com qualidade de evidência (regra da tese).
