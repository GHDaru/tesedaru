---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: EinDor2020
title: "Active Learning for BERT: An Empirical Study"
authors: ["Ein-Dor, Liat", "Halfon, Alon", "Gera, Ariel", "Shnarch, Eyal", "Dankin, Lena", "Choshen, Leshem", "Danilevsky, Marina", "Aharonov, Ranit", "Katz, Yoav", "Slonim, Noam"]
year: 2020
venue: "Proceedings of EMNLP 2020, p. 7949-7962, ACL"
doi: "10.18653/v1/2020.emnlp-main.638"
pdf: referencias-pdf/EinDor2020.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: avaliacao
pillars: [P1, P4]
status: fichado

# ===== ENTIDADES =====
proposes: []
uses_methods: [aprendizado-ativo, amostragem-por-incerteza, menor-confianca, core-set-selection, discriminative-active-learning, selecao-aleatoria, fine-tuning]
datasets: [agnews, subjectivity]
metrics: [acuracia, f1]
tasks: [classificacao-de-texto]
models: [bert]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Sener2018, Devlin2019]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Estudo empírico de referência sobre aprendizado ativo com BERT sob
           orçamento pequeno e classe rara — as duas condições do FALCO. Dá
           base externa para esperar ganho da seleção nesse regime."
  - type: motiva
    target: LCE
    note: "IMPORTANTE, e é o que a R4 do t5 mandou verificar: este trabalho
           mede ORÇAMENTO em número de anotações, nunca em dinheiro. Não há
           avaliação de custo financeiro nem de compromisso custo-benefício
           monetário. Isso não enfraquece a citação da tese — SUSTENTA a
           lacuna que ela alega. Ver a seção 'Sobre a frase da L813'."
---

# Active Learning for BERT: An Empirical Study

## Sobre a frase da L813 do Capítulo 2 (o que a R4 mandou verificar)

`2-fundam:812-813` afirma que a tese preenche a lacuna do balanceamento
explícito entre custo financeiro e ganho de informação, *"com avaliação
rigorosa desse trade-off, ainda rara mesmo nos trabalhos que tocam o custo
`\cite{Zhang2025, EinDor2020}`"*.

**Verificado. E o achado é mais favorável à tese do que a frase sugere.**

Este trabalho **não avalia custo**. Ele mede **orçamento de anotação em número
de rótulos** — o desenho é "um orçamento inicial que permite 100 anotações",
e todas as curvas são desempenho por iteração, não desempenho por unidade
monetária. As palavras "cost" e "expensive" aparecem no texto sempre em sentido
qualitativo ("rotular é caro") ou referindo-se a custo computacional de treinar
rede profunda, nunca como grandeza medida.

Ou seja: um dos estudos empíricos mais completos da área sobre aprendizado
ativo com BERT — 10 conjuntos, várias estratégias avançadas — **opera sob
restrição de orçamento sem jamais instrumentar custo**. É exatamente o vazio que
a tese alega.

**Sugestão de precisão para o texto**: dizer "trabalhos que tocam o custo" é
generoso. O mais forte, e mais exato, é dizer que esses trabalhos tratam
orçamento como CONTAGEM DE RÓTULOS e não como custo, e que é essa a diferença
que o FALCO instrumenta. A frase fica mais precisa e a lacuna fica mais nítida.

## Resumo (5-8 linhas, com as MINHAS palavras)
Estudo empírico em escala sobre aprendizado ativo aplicado ao BERT, no cenário
que os autores consideram o realista: **orçamento de anotação muito pequeno e
classe positiva rara**. Compara estratégias tradicionais e avançadas — incerteza,
Core-Set, Dropout, comprimento de gradiente esperado, aprendizado ativo
discriminativo — contra a linha de base aleatória, em dez conjuntos. A
conclusão é positiva e condicionada: as estratégias melhoram o BERT, e o ganho
é MAIOR justamente no cenário desbalanceado e prático. Publica o arcabouço de
pesquisa com dados, implementações e avaliação automática.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Estratégias de AL melhoram o BERT sob orçamento pequeno e dados enviesados, e o ganho é maior no cenário desbalanceado e prático | §3, p. 5 (resultados) | Cap. 2: base externa para esperar ganho no nosso regime |
| C2 | No cenário desbalanceado-prático, as estratégias superam a aleatória por margem de **4 a 8 pontos de F1 em média** | §3, p. 5 | **Cap. 5: número comparável ao ganho que o FALCO mede** |
| C3 | Na maioria dos conjuntos, TODAS as estratégias superaram a aleatória — inclusive onde a aleatória já ia muito bem | §3, p. 5 | Quinto ponto da série regime × ganho da seleção |
| C4 | Aumentar o tamanho do lote estabiliza substancialmente os resultados do BERT, mas esbarra na memória da GPU | §3.5, p. 5 | Cap. 3: justificativa para o nosso tamanho de lote |
| C5 | Conjunto de validação pode não existir sob orçamento limitado; ignorá-lo dá resultado qualitativamente igual, porém mais ruidoso | §3.5, p. 5 | Cap. 3/Cap. 6: ressalva metodológica honesta, e problema real do nosso desenho |
| C6 | O orçamento é medido em NÚMERO DE ANOTAÇÕES; não há avaliação de custo financeiro | todo o §3 | **Cap. 2 L813: sustenta a lacuna** |

## Números que posso citar
Condições: BERT-BASE (110 milhões de parâmetros), ajuste fino por 5 épocas,
taxa de aprendizado 5×10⁻⁵, melhor modelo escolhido pelo conjunto de validação;
**10 conjuntos**; orçamento inicial de **100 anotações**; cenários com classe
positiva de prior baixo.

- **Ganho de 4 a 8 pontos de F1 em média** sobre a linha de base aleatória, no
  cenário desbalanceado-prático (§3).
- **100** anotações de orçamento inicial (§3.1).
- **5** épocas de ajuste fino, taxa **5×10⁻⁵** (§3.5).

## Citações diretas (com página)
> "the AL strategies improve the F1 of the Random baseline by a large margin of
> 4 − 8% on average." (§3, p. 5)

> "In practice, dev sets may be unavailable, particularly under a limited
> annotation budget." (§3.5, p. 5)

> "increasing the batch size had a substantial effect on improving the stability
> of BERT results. However, due to memory limitations of the GPU, increasing the
> batch size comes at the expense of the maximal batch size." (§3.5, p. 5)

## Crítica / limitações (minha leitura)
- **Classificação binária.** O estudo é declaradamente sobre "practical
  scenarios of binary text classification". Quinto ponto do regime fácil da
  série, e o mais distante possível das nossas 621 classes.
- **Custo não é medido**, como detalhado acima. É limitação em relação à
  pergunta da tese, não do trabalho em si — ele não se propõe a isso.
- **Depende de conjunto de validação** para escolher o melhor modelo, e os
  próprios autores registram que sob orçamento limitado ele pode não existir.
  Registrei como C5 porque é ressalva honesta e é um problema real também para
  o FALCO.
- **Inglês apenas.**

## Ideias que gera para a tese
- **Comparador numérico para o Capítulo 5**: os 4 a 8 pontos de F1 de ganho
  sobre a aleatória, em cenário desbalanceado, são a referência externa mais
  próxima do que o FALCO mede. Vale colocar lado a lado com o nosso número —
  ressalvando que lá são 2 classes e aqui 621.
- **Afiar a frase da L813**: trocar "trabalhos que tocam o custo" por a
  distinção real — orçamento como contagem de rótulos versus custo
  instrumentado. É mais preciso e torna a lacuna mais nítida.
- **Quinto ponto da série regime × ganho**:

  | Fonte | Classes | Seleção bate a aleatória? |
  |---|---|---|
  | `Rouzegar2024` | 2 a 4 | sim |
  | `Deng2023fedal` | 3 | sim, por 2,36 pontos |
  | `Yuan2020` | 2 a 5 | sim |
  | **`EinDor2020`** | **2** | **sim, por 4 a 8 pontos de F1** |
  | `Wertz2022` | 100 a 739 | **não**, consistentemente |

  Cinco trabalhos, e a fronteira continua no mesmo lugar.
- **O C5 é uma ressalva a herdar**: se conjunto de validação pode não existir
  sob orçamento apertado, o critério de parada do FALCO — que se apoia em
  validação — herda a fragilidade. Vale uma linha no Cap. 6.
