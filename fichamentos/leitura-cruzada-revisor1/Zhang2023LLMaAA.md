---
id: Zhang2023LLMaAA
title: "LLMaAA: Making Large Language Models as Active Annotators"
authors: ["Zhang, Ruoyu", "Li, Yanzeng", "Ma, Yongliang", "Zhou, Ming", "Zou, Lei"]
year: 2023
venue: "Findings of EMNLP 2023"
doi: "10.18653/v1/2023.findings-emnlp.872"
pdf: referencias-pdf/Zhang2023LLMaAA.pdf
paper_type: metodo
pillars: [P2, P3, P4]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, pool-based, llm-como-oraculo,
               amostragem-por-incerteza, menor-confianca, entropia,
               saida-estruturada, few-shot, fine-tuning]
datasets: []
metrics: []
tasks: []
models: [gpt-3.5-turbo, gpt-3, gpt-4, bert]
extends: []
compares_with: []
contradicts: []
builds_on: [Settles2009]
falco_relation:
  - type: fundamenta
    target: oraculo-progressivo
    note: "Evidência central para o desenho do FALCO: um modelo específico de
           tarefa (BERT) treinado com rótulos de LLM SUPERA o próprio LLM
           professor com apenas centenas de exemplos anotados — inclusive com
           argumento teórico (professor com acurácia p>0,5 gera aluno que
           converge para a predição correta)."
  - type: compara
    target: DRI-SL
    note: "A seleção do LLMaAA é dirigida pela incerteza do modelo ALUNO (exige
           seed set + 9 re-treinos); o k-means de diversidade falha nas iterações
           iniciais com poucos dados — exatamente o regime cold-start que o
           DRI-SL ataca sem depender de modelo treinado."
  - type: compara
    target: FALCO
    note: "LLMaAA usa 100 exemplos gold reutilizados como demonstração e
           validação (reponderação automática); o FALCO usa braços gold (B/C/D)
           só para avaliação e mantém o laço de treino livre de gold."
---

# LLMaAA: Making Large Language Models as Active Annotators

## Resumo (5-8 linhas, com as MINHAS palavras)
Coloca o LLM (ChatGPT) como anotador dentro de um laço clássico de aprendizado
ativo pool-based: a cada iteração, o modelo aluno (BERT) escolhe por incerteza
(menor confiança/entropia) ou diversidade (k-means) os itens que o LLM deve
rotular; o treino é robustecido por reponderação automática das amostras, que usa
100 exemplos gold como validação meta-aprendida. Em NER (OntoNotes 4.0 chinês,
CoNLL03) e extração de relações (subconjunto do Re-TACRED), com 100 gold + 500
rótulos "prata" do LLM, o aluno supera o LLM professor e supera com folga métodos
de geração de dados sintéticos (ZeroGen/FewGen) mesmo quando esses usam 10x mais
dados. Prompt com exemplos k-NN e verbalizador de rótulos é decisivo para a
qualidade da anotação; a saída do LLM é restrita a formato JSON.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Aluno treinado com rótulos de LLM supera o LLM professor com ~500 exemplos (média 79,21 vs 75,28 de F1) | §5.2, Tab. 1, p. 13093 | Cap. 2 e Cap. 5: justifica treinar BERTimbau fora do laço com rótulos do oráculo |
| C2 | Aquisição por incerteza ≫ aleatória: mesma qualidade com 30-40% dos dados e convergência mais rápida | §5.3.2, Fig. 3, p. 13094-13095 | Cap. 2 (AL clássico ainda vale com oráculo LLM) |
| C3 | k-means (diversidade) só supera aleatório em 1 de 3 datasets; falha com poucos dados/representações cruas | §5.3.2, p. 13095 | Cap. 5: diversidade via embedding do aluno ≠ diversidade lexical pré-treino do DRI-SL |
| C4 | Reponderação automática com apenas 100 gold torna o treino tolerante a ruído; ganho maior quando o anotador LLM é pior | §5.3.3, Fig. 4, p. 13094-13095 | Cap. 5: alternativa de mitigação de ruído ao (não-)refino do FALCO |
| C5 | Prompt importa: sem exemplos k-NN o F1 de NER despenca 21-25 pontos; verbalizador de rótulos +2,8 em RE | §5.3.1, Tab. 3, p. 13094 | Cap. 3: fundamenta o investimento em engenharia de prompt do oráculo |
| C6 | Geração de dados sintéticos (ZeroGen) produz frases template com domain shift; anotar corpus real é mais eficiente | §5.2, Tab. 2, p. 13093 | Cap. 2: por que FALCO anota descrições reais em vez de gerar dados |
| C7 | Anotadores melhores → alunos melhores, com professor fraco o aluno o supera por margem enorme (GPT-3: 29,49 → 56,63) | §6.1, Tab. 4, p. 13095 | Cap. 5: sensibilidade do FALCO à escolha do LLM |

## Números que posso citar
- Com 100 gold + 500 prata (ChatGPT, menor confiança): F1 74,00 (OntoNotes 4.0
  zh), 82,84 (CoNLL03 en), 80,79 (Re-TACRED-subset) vs PROMPTING direto do LLM
  70,73 / 81,33 / 73,77 (Tab. 1, p. 13093; média de 3 seeds, micro F1).
- ZeroGen com 5.000 exemplos sintéticos: 66,97 / 72,99 / 66,57 — pior que LLMaAA
  com 500 (Tab. 1, p. 13093).
- Backbone GPT-3 (text-curie-001): professor F1 29,49 → aluno 56,63 (+27);
  GPT-4: professor 73,68 → aluno 74,90 (Tab. 4, p. 13095, OntoNotes).
- Sem k-NN demos: F1 49,62 (OntoNotes) e 55,74 (CoNLL) vs 70,73 e 81,33 com
  demos (Tab. 3, p. 13094).

## Citações diretas (com página)
> "task-specific models trained from LLM-generated labels can outperform the
> teacher within only hundreds of annotated examples, which is much more
> cost-effective than other baselines" (Abstract, p. 13088)

> "This toy case nonetheless explains that an ordinary teacher can raise better
> students." (§6.2, p. 13096)

## Crítica / limitações (minha leitura)
- Tarefas com 4-7 tipos (NER/RE); nada aproxima a classificação extrema de 714
  classes desbalanceadas do FALCO, onde a incerteza do aluno nas classes raras é
  pouco confiável.
- O laço exige re-treinar o aluno a cada uma das 9 iterações e depende de um seed
  set aleatório de 50 itens — o cold start não é resolvido, é herdado.
- Requer 100 exemplos gold desde o início (demonstração + validação da
  reponderação): não é "human-free"; o próprio paper admite o gargalo.
- Resultados com APIs proprietárias em evolução (Azure gpt-35-turbo); autores
  admitem risco de exposição do teste no pré-treino do LLM (Limitations,
  p. 13096).

## Ideias que gera para a tese
- O argumento teórico do §6.2 (professor estocástico com p>0,5 → aluno
  determinístico correto) ajuda a explicar no Cap. 5 por que o braço A do E3'
  chega perto de B em várias classes apesar do ruído do oráculo.
- A falha do k-means em regime de poucos dados (C3) é evidência de contraste a
  favor do DRI-SL: diversidade precisa vir de representação pré-treinada/lexical
  no cold start, não do embedding do aluno ainda cru.
- Reponderação automática com pequeno conjunto limpo é candidata a trabalho
  futuro do FALCO (mitigar ruído do oráculo sem re-rotular).
