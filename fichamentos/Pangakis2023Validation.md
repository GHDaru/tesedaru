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
| C3 | Consistency score: rotular >=7x a temperatura 0,6 e tomar o voto modal; consistência 1,0 tem acurácia +19,4 pp vs <1,0; 85,1% das amostras são totalmente consistentes. A RECOMENDAÇÃO do paper é de no mínimo 3 rotulagens a temperatura > 0 — as 7 são a escolha dos autores, não o piso metodológico | §3.1, p. 9; Fig. 3, p. 10 | Cap. 5/futuros: sinal de confiança do oráculo sem autoavaliação |
| C4 | Refinar o prompt/codebook ajuda pouco: 1 rodada de atualização melhora acurácia/F1 modestamente; recall frequentemente piora | §3.2, Fig. 4, pp. 11-12 | Cap. 5: modera expectativas de prompt engineering como alavanca |
| C5 | Validação exige 250-1.250 amostras humanas aleatórias (mais se classes raras) e as mesmas instruções (codebook) para humano e LLM | §2, fn. 7-8, pp. 5-6 | Cap. 3: dimensionar o gabarito do E0; mesma instrução para oráculo e gabarito |
| C6 | Variação intra-dataset: F1 de 0,259 a 0,811 em duas tarefas do MESMO dataset (Card et al. 2022; dif. 0,552) | §3, p. 9 | Cap. 2: 'o LLM anota bem' não é propriedade do dataset, é da tarefa |
| C7 | Anotação com GPT-4 é barata e rápida: >200 mil textos, 27 tarefas, ~$420; ~2-3h por 1.000 amostras (7 iterações) | §2, pp. 6-7 | Cap. 5: âncora externa de ordem de custo para a tabela de custo |
| C8 | O paper tipifica QUATRO usos legítimos do LLM anotador conforme o desempenho validado: (1) confirmar a qualidade de rótulos humanos já existentes, (2) priorizar itens para revisão humana (consistência < 1,0 ou alto recall), (3) produzir dados rotulados para treinar e validar um classificador supervisionado, (4) classificar o corpus inteiro diretamente | §4, p. 12; Tab. 2, p. 13 | Cap. 1/2: o FALCO é exatamente o caso de uso 3 — enquadramento pronto e citável para posicionar o desenho da tese na literatura metodológica |

## Números que posso citar
- Tab. 1 (p. 7; GPT-4, 27 tarefas binárias, 11 datasets não públicos, held-out):
  acurácia mediana 0,850 (mín 0,674; máx 0,981); F1 mediana 0,707 (mín 0,059!);
  precisão mediana 0,650 (mín 0,033); recall mediana 0,829.
- Tab. 1 completa (p. 7), com quartis — útil para mostrar a CAUDA e não só a mediana:
  acurácia mín 0,674 / p25 0,808 / média 0,855 / mediana 0,850 / p75 0,905 / máx 0,981;
  precisão 0,033 / 0,472 / 0,615 / 0,650 / 0,809 / 0,957;
  recall 0,250 / 0,631 / 0,749 / 0,829 / 0,899 / 0,982;
  F1 0,059 / 0,557 / 0,660 / 0,707 / 0,830 / 0,969.
  Um quarto das tarefas tem precisão abaixo de 0,472 — a mediana esconde isso.
- 20/27 tarefas com recall > precisão (Fig. 2, p. 8); 8/27 com precisão E recall > 0,7.
- Consistency score (§3.1): +19,4 pp acurácia, +16,4 pp TPR, +21,4 pp TNR para
  consistência 1,0; 85,1% das amostras com consistência 1,0.
- Custo total ~US$ 420 para >200.000 amostras x 7 rotulagens (GPT-4 API, 2023).
  Dividindo, dá ~US$ 0,002 por texto anotado — DERIVAÇÃO NOSSA: o paper reporta
  só o total ($420) e o volume ("slightly over 200,000 text samples", §2, p. 6),
  nunca um custo por rótulo. Citar sempre como ordem de grandeza derivada.

## Citações diretas (com página)
> "any automated annotation process using an LLM must validate the LLM's performance against labels generated by humans" (Abstract, p. 1)

> "for a full one-third of tasks, the LLM either missed at least half of the true positive cases, had more false positives than true positives, or both" (§3, p. 7)

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
  FALCO; se citado como alternativa, citar junto o multiplicador de custo. O
  próprio paper admite que a temperatura 0,6 é ARBITRÁRIA e deixa a escolha ótima
  para trabalho futuro (nota 14, p. 9); o piso recomendado é 3 rotulagens, o que
  reduziria o multiplicador de 7x para 3x.
- Um único LLM (GPT-4) e uma única rodada de refino de codebook: o argumento
  central de que "os desafios persistem mesmo com LLMs melhores" é POSIÇÃO
  argumentada, não resultado longitudinal testado — não há comparação entre
  gerações de modelo no próprio estudo.
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
- Enquadrar o E3' (braço A contra os braços gold B/C/D) explicitamente como a
  "validação obrigatória" que o paper exige: a tese não ASSUME a qualidade do
  oráculo, ela a MEDE. E citar C8 para dizer em que casa da tipologia o FALCO
  mora (caso de uso 3).
- A recomendação de 250-1.250 rótulos humanos de validação, com a ressalva de
  ampliar quando a classe positiva tem menos de 1% (nota 7, p. 5), dá ancoragem
  quantitativa externa ao dimensionamento dos braços gold — e a ressalva é
  exatamente o caso da cauda longa das 714 classes.
- Auditoria barata: aplicar o escore de consistência só a uma AMOSTRA do corpus
  (k rotulagens em algumas centenas de itens) em vez de 7x no corpus inteiro —
  preserva o sinal de confiança sem estourar o orçamento do P3.
- Quando o desempenho é ruim, o paper sugere DESAGREGAR a anotação complexa em
  decisões mais simples (§4, p. 12) — leitura direta para a hierarquia de
  categorias do varejo: decompor a escolha entre 714 classes em etapas.
