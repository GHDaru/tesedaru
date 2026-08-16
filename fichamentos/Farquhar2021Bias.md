---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Farquhar2021Bias
title: "On Statistical Bias In Active Learning: How and When To Fix It"
authors: ["Farquhar, Sebastian", "Gal, Yarin", "Rainforth, Tom"]
year: 2021
venue: "ICLR 2021 (OpenReview JiYq3eqTKY; arXiv:2101.11665v2)"
doi: ""
pdf: referencias-pdf/Farquhar2021Bias.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P4]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: [estimador-pure, estimador-lure]   # R_PURE e R_LURE (pendentes no vocabulário)
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza]
datasets: [mnist, fashion-mnist]             # pendentes no vocabulário
metrics: [acuracia]
tasks: [classificacao-de-imagens, regressao] # pendentes no vocabulário
models: [rede-neural-bayesiana, regressao-linear]  # pendentes no vocabulário

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: []
contradicts: []
builds_on: [MacKay1992]

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Estabelece formalmente o FENÔMENO que o E6 da tese mede: o risco
           estimado sobre dados coletados ativamente é enviesado porque a
           amostra ativa não segue a distribuição populacional. É a citação
           obrigatória do parecer R6 item 10 [Dom-M3]: a tese cita o fenômeno
           daqui e reivindica apenas a QUANTIFICAÇÃO no seu cenário (texto
           curto pt-BR, oráculo LLM, avaliação interna vs. externa)."
  - type: ameaca
    target: FALCO
    note: "Se a tese avaliasse o laço só no teste interno (dados coletados
           ativamente), estaria usando exatamente o estimador viesado R̃ que
           este paper desmonta. O desenho do E6 (população reservada) e o
           conjunto de validação reservado exigido pelo FALCO respondem a
           essa ameaça; o paper também oferece a alternativa não adotada
           (reponderação LURE), que a tese deve discutir como trabalho futuro."
---

# On Statistical Bias In Active Learning: How and When To Fix It

> **Nota de fonte**: PDF arquivado = arXiv v2 (2101.11665v2, pós-camera-ready); o download do PDF oficial do OpenReview é bloqueado por challenge. Paginação citada refere-se ao PDF do arXiv.

## Resumo (5-8 linhas, com as MINHAS palavras)
Formaliza o viés estatístico do aprendizado ativo: como os pontos são
escolhidos (e não sorteados i.i.d.), o risco empírico calculado sobre o
conjunto ativamente rotulado é um estimador viesado do risco populacional —
e quase toda a literatura de AL com redes neurais ignora isso. Os autores
propõem dois estimadores por reponderação (importância sobre índices do pool):
R_PURE e R_LURE, provando não-viés, consistência e variância frequentemente
MENOR que a do estimador ingênuo. Empiricamente, corrigir o viés ajuda na
AVALIAÇÃO e em modelos subparametrizados (regressão linear), mas pode piorar
o TREINO de redes neurais superparametrizadas: o viés do AL (negativo) cancela
parcialmente o viés de overfitting (positivo), agindo como regularização ad hoc.
A aplicação a avaliação de modelos é apontada como direção nova — semente do
"active testing" de Kossen et al. (2021).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O risco empírico sub-amostrado sobre pontos ativamente selecionados (Eq. 1) NÃO é estimador não-viesado do risco populacional; sob amostragem não uniforme os M pontos não seguem a população | §2, Eq. 1, p. 2 | Cap. 5 (E6): fundamento formal do instrumento interna vs. externa; abre o parágrafo do confronto Dom-M3 |
| C2 | "Almost all work on active learning for neural networks currently ignores the issue of statistical bias" — dos 15 papers revisados mais citados que citam Gal et al. (2017b), só 2 mencionam o viés e nenhum o trata | §2 p. 2; §5 p. 6; Apêndice D | Cap. 2: posicionamento — o fenômeno é conhecido mas negligenciado; a tese não o descobre, o quantifica no seu cenário |
| C3 | R_PURE (Eq. 2-3) e R_LURE (Eq. 5) são não-viesados e consistentes (Teoremas 1-5), com Var[R_LURE] ≤ Var[R_PURE] (Teorema 4) | §3.1-3.2, pp. 3-4 | Cap. 6 / trabalho futuro: alternativa por reponderação ao conjunto reservado que o FALCO usa |
| C4 | O estimador ingênuo R̃ SUPERESTIMA o risco (subestima o desempenho) porque o AL amostra os pontos mais difíceis | Fig. 2 (caption), p. 7 | Cap. 5 (E6): mesmo sinal que a acurácia interna da entropia (subestima em até 14 p.p.); a tese acrescenta que o sinal INVERTE no Macro F1 |
| C5 | Distinção entre viés estatístico (da seleção ativa) e viés de overfitting (do treino); ambos interagem | §2 p. 2; §7 pp. 8-9 | Cap. 3/5: precisão conceitual ao nomear o que o E6 mede (viés estatístico da avaliação, não overfitting) |
| C6 | Remover o viés pode PIORAR o treino de modelos superparametrizados: ALB (negativo) cancela parcialmente OFB (positivo) — AL como regularização ad hoc | §6 Fig. 3, §7 Fig. 4, pp. 8-9 | Cap. 6: por que a tese corrige a AVALIAÇÃO (população reservada) sem reponderar o TREINO |
| C7 | Sob a proposta ótima q* ∝ perda, os estimadores são exatos (variância zero em relação ao risco empírico do pool) | Teorema 7, p. 6 | Contexto do C3; ponte para Kossen2021ActiveTesting, que operacionaliza q* na avaliação |
| C8 | Qualquer estratégia determinística (argmax) vira proposta válida via softmax ou epsilon-greedy — a correção acopla-se a esquemas de AL existentes | §3.3, p. 5 | Cap. 6: viabilidade de aplicar LURE ao FALCO sem redesenhar o seletor |

## Números que posso citar
- Levantamento informal: dos **15** papers revisados por pares mais citados que
  citam Gal et al. (2017b) (AL profundo para imagens), **apenas 2** mencionam o
  viés de AL e **nenhum** o trata (§5 p. 6; lista no Apêndice D).
- BNN convolucional com ~**80.000** parâmetros em MNIST/FashionMNIST
  modificados (desbalanceados, rótulos ruidosos) — cenário dos experimentos de
  avaliação e treino (§6, p. 7; detalhes no Apêndice C.2).
- Sinais dos vieses (§7, Figs. 2 e 4): ALB tipicamente **negativo** (pontos
  informativos são mais difíceis que a média), OFB tipicamente **positivo**
  (treino explica melhor os dados vistos); cancelamento parcial explica por que
  treinar com o estimador viesado pode dar modelo MELHOR (Fig. 3c: acurácia de
  teste levemente pior ao treinar com R_LURE/R_PURE na BNN).
- Condições: resultados de treino/avaliação com regressão linear (dados toy
  não lineares, 1000 trajetórias) e BNN (45 aquisições, proposta estilo BALD
  relaxada estocasticamente); sombreamento ±1 desvio-padrão.

## Citações diretas (com página)
> "Almost all work on active learning for neural networks currently ignores
> the issue of statistical bias." (p. 2)

> "Note the sign: R̃ overestimates risk because active learning samples the
> hardest points." (p. 7, legenda da Fig. 2)

> "This final application, of active learning for model evaluation, is an
> interesting new research direction that is opened up by our estimators."
> (p. 9)

## Crítica / limitações (minha leitura)
- Experimentos apenas em imagens (MNIST/FashionMNIST) e regressão toy; nada de
  texto, nada de oráculo imperfeito — o rótulo é sempre o gabarito. O cenário
  FALCO (texto curto, oráculo LLM com erro próprio) fica fora do escopo.
- A correção LURE exige registrar a probabilidade de aquisição q(i_m) a cada
  passo — fácil em esquemas estocásticos, mas intrusiva em pipelines já
  existentes; a tese optou pelo caminho ortogonal (população reservada), que o
  próprio paper reconhece como prática padrão de model selection.
- Mede viés em risco/perda (NLL, MSE) e acurácia; não examina métricas
  macro-averaged nem desbalanceamento severo de classes — exatamente onde o E6
  da tese encontra o sinal INVERTIDO (Macro F1 interno superestima). O achado
  de "sinal dependente da métrica" não está aqui.
- O levantamento dos "15 papers" é declaradamente informal (amostra de
  conveniência por citação); citável como indício, não como estatística.

## Ideias que gera para a tese
- Parágrafo Dom-M3 (Cap. 2 ou 5): citar C1+C2 para estabelecer que o fenômeno
  é conhecido desde MacKay (1992) e formalizado aqui; em seguida delimitar a
  contribuição da tese como a QUANTIFICAÇÃO do viés no cenário texto-curto +
  oráculo LLM + avaliação interna/externa (17,1±1,0 p.p. em acurácia; +34 p.p.
  em Macro F1), com o sinal dependente da métrica como achado novo.
- Trabalho futuro (Cap. 6): aplicar R_LURE ao teste interno do FALCO (C8 mostra
  que o seletor por entropia vira proposta via softmax) e comparar com a
  estimativa da população reservada — validação cruzada dos dois instrumentos.
- C6 dá linguagem precisa para discutir por que o FALCO não repondera o treino:
  em modelos superparametrizados (BERTimbau no E3') o viés de seleção pode ser
  regularizador; corrigir só a avaliação é a escolha conservadora certa.
