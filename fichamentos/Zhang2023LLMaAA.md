---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Zhang2023LLMaAA
title: "LLMaAA: Making Large Language Models as Active Annotators"
authors: ["Zhang, Ruoyu", "Li, Yanzeng", "Ma, Yongliang", "Zhou, Ming", "Zou, Lei"]
year: 2023
venue: "Findings of the Association for Computational Linguistics: EMNLP 2023, pp. 13088-13103"
doi: "10.18653/v1/2023.findings-emnlp.872"
pdf: referencias-pdf/Zhang2023LLMaAA.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P2, P3]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: []               # método proposto: LLMaAA (termo ausente do vocabulário; ver relatório)
uses_methods: [aprendizado-ativo, pool-based, llm-como-oraculo, amostragem-por-incerteza, entropia, menor-confianca, few-shot, saida-estruturada, fine-tuning]
datasets: []               # OntoNotes 4.0 (zh), CoNLL03 (en), Re-TACRED-subset — fora do vocabulário
metrics: []                # precisão/recall/micro-F1 — fora do vocabulário
tasks: []                  # NER e extração de relações (não é classificacao-de-texto)
models: [gpt-3.5-turbo, gpt-3, gpt-4, bert]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: []          # baselines ZEROGEN/FEWGEN sem chave no repositório
contradicts: []
builds_on: [Wang2021GPT3Labeling]
falco_relation:
  - type: compara
    target: FALCO
    note: "Vizinho direto exigido pelo parecer R6 (Bloco C, item 9 / Dom-M1):
           é O paper que põe o LLM como anotador DENTRO do laço pool-based com
           aquisição por incerteza — a mesma composição estrutural do FALCO.
           Difere: tarefas NER/RE (não classificação em espaço fechado grande),
           precisa de 100 exemplos ouro para demonstração+validação, robustez
           via reponderação automática (meta-learning), e não instrumenta custo
           monetário por rótulo. Confronto central do Cap. 2 e da RQ de seleção."
  - type: compara
    target: DRI-SL
    note: "Compara estratégias de aquisição sob oráculo-LLM: menor confiança e
           entropia máxima superam aleatório e k-means (diversidade) — evidência
           externa para o debate incerteza vs representatividade do P2."
---

# LLMaAA: Making Large Language Models as Active Annotators

## Resumo (5-8 linhas, com as MINHAS palavras)
Integra o LLM como anotador dentro de um laço clássico de AL pool-based: um
modelo-tarefa pequeno (TAM, BERT) treina nos rótulos "prata" do LLM, a função de
aquisição (aleatória, entropia, menor confiança, k-means) escolhe o próximo lote
de 50 e o LLM (ChatGPT) o anota. Três componentes de confiabilidade: prompts com
recuperação k-NN de demonstrações e verbalizador de rótulos; e reponderação
automática das amostras de treino (meta-learning contra 100 exemplos ouro de
validação) para robustez ao ruído. Em NER (OntoNotes zh, CoNLL03) e RE
(Re-TACRED), com 100 exemplos ouro + 500 anotações prata, o TAM supera o próprio
LLM professor e os métodos de geração de dados (ZEROGEN/FEWGEN) com 10x mais dados.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Com 100 ouro + 500 prata, o TAM treinado supera o LLM anotador (PROMPTING) em ~4 pts F1 médios (F1 médio 79,21 vs 75,28), com muito menos parâmetros e menor latência de inferência | §5.2, Tab. 1 e texto, p. 13093 | Cap. 2: lacuna — destilar o LLM para um modelo pequeno é viável com poucas centenas de rótulos |
| C2 | Aquisição por incerteza (entropia, menor confiança) converge mais rápido e mais alto que aleatória sob oráculo-LLM; menor confiança é a melhor | §5.3.2, Fig. 3, p. 13094; texto p. 13095; Tab. 1 | Cap. 4/5: baseline conceitual do confronto DRI-SL vs US/RS com oráculo ruidoso |
| C3 | Incerteza atinge o desempenho da seleção aleatória com apenas 30-40% dos dados de treino | §5.3.2, p. 13095 | Cap. 2: eficiência amostral do AL persiste quando o anotador é LLM |
| C4 | k-means (diversidade pura) só ganha do aleatório em 1 de 3 datasets — diversidade falha em regime de poucos dados | §5.3.2, p. 13095 | Cap. 2: motiva o desenho híbrido densidade+incerteza do DRI-SL |
| C5 | Prompt importa muito: sem exemplos k-NN o F1 zero-shot cai 21-25 pts em NER; verbalizador de rótulos +2,8 em RE | §5.3.1, Tab. 3, p. 13094 | Cap. 5: paralelo com o efeito do instrumento (RQ do instrumento de saída) |
| C6 | Estudantes superam professores: TAM > LLM anotador para GPT-3 (+27 F1), ChatGPT (+3,3) e GPT-4 (+1,2) | §6.1, Tab. 4, p. 13095; §6.2, p. 13095-13096 | Cap. 2/5: fundamenta a arquitetura destilar-oráculo-para-classificador do FALCO |
| C7 | Anotação ativa com LLM é mais eficiente que geração de dados: ZEROGEN/FEWGEN perdem mesmo com 5.000 amostras sintéticas vs 500 anotadas | §5.2, Tab. 1, p. 13093 | Cap. 2: justifica anotar corpus real em vez de sintetizar dados |
| C8 | A reponderação automática das amostras torna o treino tolerante ao ruído do oráculo usando apenas 100 exemplos limpos, e o ganho é MAIOR quando o anotador LLM é pior (forte em OntoNotes e Re-TACRED, quase nulo em CoNLL03) | §5.3.3, p. 13095; Fig. 4, p. 13094 | Cap. 5: alternativa de mitigação de ruído ao não-refino do FALCO; candidata a trabalho futuro |
| C9 | A geração sintética degrada por construção: o ZEROGEN produz sentenças em molde ("simple templated sentences") que se afastam do domínio jornalístico do Re-TACRED, induzindo domain shift | §5.2, Tab. 2 (estudo de caso), p. 13093 | Cap. 2: por que o FALCO anota descrições reais de varejo em vez de gerá-las |
| C10 | O ganho do aluno sobre o professor encolhe conforme o professor melhora: com orçamento fixo de 500 amostras, professores mais fortes se aproximam do teto do aluno | §6.1, p. 13095 | Cap. 5: prevê o comportamento do braço A do E3' se o oráculo for trocado por um LLM mais forte |

## Números que posso citar
- Tab. 1 (p. 13093; ChatGPT anotador, 100 ouro/500 prata, média±dp de 3 seeds):
  LLMaAA-confidence F1 = 74,00 (OntoNotes 4.0 zh), 82,84 (CoNLL03), 80,79
  (Re-TACRED-subset) vs PROMPTING 70,73 / 81,33 / 73,77 e vs SUPERVISED (100 ouro)
  73,00 / 77,94 / 74,28.
- Coluna de F1 médio da Tab. 1 (p. 13093): LLMaAA-confidence 79,21 > LLMaAA-random
  75,26 > PROMPTING 75,28 > SUPERVISED 75,07 > FEWGEN 5.000 74,68 > FEWGEN 500
  71,97 > ZEROGEN 5.000 68,84 > ZEROGEN 500 68,75. A aquisição por incerteza vale
  ~4 pontos de F1 médio sobre a aleatória com o mesmo orçamento de 500 rótulos.
- ZEROGEN com 5.000 exemplos sintéticos (Tab. 1, p. 13093): 66,97 (OntoNotes) /
  72,99 (CoNLL03) / 66,57 (Re-TACRED) — perde para o LLMaAA com 500 anotações reais.
- Tab. 3 (p. 13094): instrução pura vs prompt otimizado: 49,62→70,73 (OntoNotes,
  +k-NN), 55,74→81,33 (CoNLL03, +k-NN), 70,94→73,77 (Re-TACRED, +verbalizador).
- Tab. 4 (p. 13095, OntoNotes): GPT-3 PROMPTING 29,49 vs LLMaAA 56,63; ChatGPT
  70,73 vs 74,00; GPT-4 73,68 vs 74,90.
- Protocolo: pool = treino original; seed 50; lotes de 50 por 9 iterações = 500
  prata; validação/demonstração = mesmos 100 ouro (§5.1, p. 13092).

## Citações diretas (com página)
> "task-specific models trained from LLM-generated labels can outperform their teacher LLMs within only hundreds of annotated examples, which is much more cost-effective than other baselines" (Abstract, p. 13088)

> "uncertainty-based methods are able to achieve on-par performance with random selection with only 30%~40% training data" (§5.3.2, p. 13095)

> "This toy case nonetheless explains that an ordinary teacher can raise better students." (§6.2, p. 13096)

> "ZEROGEN tends to generate simple templated sentences that deviate from the news domain, i.e. the original corpus of Re-TACRED. These results may induce low-quality and domain-shift issues that hamper TAMs' performance." (§5.2, p. 13093)

## Crítica / limitações (minha leitura)
- Não é human-free nem custo-transparente: exige 100 exemplos ouro e não reporta
  custo monetário/tokens — a comparação de custo do FALCO (por rótulo, com cache)
  não tem análogo aqui.
- Tarefas NER/RE com poucos tipos; nada sobre classificação em espaço fechado
  grande (714 classes) nem sobre texto curto esparso.
- A incerteza usada é a do modelo-aluno (TAM), não a do oráculo; o FALCO explora
  também a confiança estruturada do oráculo — distinção a marcar no confronto.
- Reponderação automática requer laço de meta-otimização por batch (custo de
  treino não discutido) e um conjunto limpo — de novo o humano volta pela porta
  dos fundos (assunção Dval limpa).
- Saída JSON do prompt de NER (Fig. 2) sem tratamento de erro de formato relatado.
- O cold start não é resolvido, é herdado: o laço parte de um conjunto-semente
  ALEATÓRIO de 50 itens e exige re-treinar o aluno em cada uma das 9 iterações
  (§5.1, p. 13092) — custo de treino que o DRI-SL evita ao selecionar sem modelo
  treinado.
- Anotadores são APIs proprietárias da família GPT em regime caixa-preta; os
  próprios autores admitem o risco de exposição do conjunto de teste no
  pré-treino do LLM e apenas argumentam que isso "não afeta" o método
  (Limitations, p. 13096) — ameaça de validade que o corpus PT-BR privado do
  FALCO não tem.
- Os autores reconhecem o teto duplo do arranjo: professor fraco não forma bom
  aluno, e quando o professor ultrapassa a capacidade do aluno é "theoretically
  impossible" o aluno superá-lo (Limitations, p. 13096).

## Ideias que gera para a tese
- C2+C4 dão sustentação externa ao argumento do P2: incerteza pura vence
  diversidade pura em regime pobre, e o DRI-SL combina os dois — posicionar na
  2.3 e retomar na discussão dos resultados do P2.
- C6 (aluno supera professor, com explicação teórica em §6.2) casa com o
  resultado FALCO vs oráculo puro; citar no Cap. 5.
- C5 é o precedente mais direto para a RQ do efeito do instrumento: mudar o
  prompt muda dezenas de pontos de F1 no MESMO modelo.
- O argumento do §6.2 (p. 13095-13096) é usável como explicação teórica no Cap. 5:
  professor estocástico com acurácia p > 0,5 gera rótulos ~Bernoulli(p) e o aluno,
  minimizando a entropia cruzada, converge para S(x) = p e prediz sempre a classe
  correta sob o limiar 0,5 — daí o braço A do E3' poder alcançar o braço B em
  várias classes apesar do ruído do oráculo.
- A falha do k-means em regime pobre (C4) é o contraste a explorar a favor do
  DRI-SL: no cold start a diversidade tem de vir de representação pré-treinada e
  variedade lexical, não do embedding de um aluno ainda cru.
- A reponderação automática com um conjunto limpo pequeno (C8) é candidata a
  trabalho futuro do FALCO: mitigar ruído do oráculo sem pagar re-rotulagem.
