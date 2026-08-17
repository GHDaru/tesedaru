---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Wertz2022
title: "Investigating Active Learning Sampling Strategies for Extreme Multi Label Text Classification"
authors: ["Wertz, Lukas", "Mirylenka, Katsiaryna", "Kuhn, Jonas", "Bogojeska, Jasmina"]
year: 2022
venue: "Proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022), Marselha, p. 4597-4605, ELRA"
doi: "10.63317/48xs9zc3987o"
pdf: referencias-pdf/Wertz2022.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: avaliacao
pillars: [P1, P2]
status: fichado

# ===== ENTIDADES =====
proposes: [limiar-variavel-multirrotulo, cnn-como-cabeca-de-classificacao]
uses_methods: [aprendizado-ativo, pool-based, alps, cvirs, discriminative-active-learning, amostragem-por-subpalavras, selecao-aleatoria]
datasets: [eurlex, arxiv-xmtc, nyt, rcv1, yelp-xmtc, agnews, toxic]
metrics: [micro-f1, macro-f1]
tasks: [classificacao-multirrotulo-extrema, classificacao-de-texto]
models: [bert-base-uncased]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Devlin2019]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: ameaca
    target: FALCO
    note: "É o achado mais incômodo da literatura fichada para a premissa do
           FALCO: em rótulo extremo, NENHUMA das quatro estratégias testadas
           (ALPS, CVIRS, DAL, subword) supera a seleção ALEATÓRIA de forma
           consistente entre conjuntos, e em quatro dos sete a aleatória empata
           ou ganha (p. 4601, 4604). Com 621 classes o FALCO opera na mesma
           faixa do EurLex (739) e do Yelp (580) deste artigo. Obriga a tese a
           tratar o braço aleatório como baseline forte, não como palha, e a
           declarar em qual regime a seleção compensa."
  - type: fundamenta
    target: LCE
    note: "Dá base externa para reportar macro F1 e não só micro: §6.2
           (p. 4604) argumenta que micro F1 sobe mesmo quando o classificador
           só melhora nas classes frequentes, e que em rótulo extremo é o macro
           que mede quantas classes o sistema aprende a discriminar. É o mesmo
           motivo pelo qual o Cap. 5 elege macro F1 como métrica principal."
---

# Investigating Active Learning Sampling Strategies for Extreme Multi Label Text Classification

## Resumo (5-8 linhas, com as MINHAS palavras)
Estudo empírico que leva o aprendizado ativo para o regime de **rótulo extremo**
(XMTC — centenas de classes, vários rótulos por texto) e testa quatro
estratégias de seleção (ALPS, CVIRS, DAL e uma baseada em subpalavras) contra
a seleção aleatória, em sete conjuntos, com BERT como classificador e orçamento
de 2.000 textos. O resultado é negativo e é essa a contribuição: nenhuma
estratégia melhora o esquema de forma consistente, e em vários conjuntos a
aleatória empata ou vence. O artigo ainda mede o **custo computacional** de cada
estratégia (que ninguém costuma reportar), compila cinco conjuntos XMTC a partir
de tarefas hierárquicas, propõe avaliar multirrótulo com limiar variável e troca
a camada linear de saída do BERT por uma CNN, o que sobe o teto de desempenho em
todos os sete conjuntos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Nenhuma estratégia de seleção melhora o AL de forma consistente entre conjuntos em rótulo extremo | §7 Conclusion, p. 4604 | Cap. 2 (limites do AL) e Cap. 5 (discussão): justifica por que o braço aleatório é baseline legítimo e não espantalho |
| C2 | A seleção aleatória empata ou supera todas as estratégias em arXiv, RCV1, AGNews e Toxic; no arXiv chega a superar por até 0,15 de micro F1 (exceto ALPS, ~0,01 pior) | §5.4, p. 4601 | Cap. 5: comparador externo para a diferença E-D medida na tese |
| C3 | O AL só melhora o classificador em conjuntos de BAIXA co-ocorrência de rótulos (EurLex, NYT, Yelp) — quando os rótulos são "singulares e espaçados" | §6.1, p. 4603 e Tab. 1, p. 4599 | Cap. 3/Cap. 5: condição sob a qual o ganho de seleção é esperado; caracterizar o nosso conjunto por essa métrica |
| C4 | Macro F1 e micro F1 medem coisas diferentes em rótulo desbalanceado; micro sobe mesmo quando o modelo só aprende as classes frequentes | §6.2, p. 4604 | Cap. 3 (escolha da métrica) e Cap. 5: fundamenta reportar macro F1 como principal |
| C5 | O custo computacional das estratégias varia em duas ordens de grandeza e pode inviabilizar o método (CVIRS: horas por iteração, semanas de experimento) | §5.6 e Tab. 3, p. 4602; §6.3, p. 4604 | Cap. 2 e Cap. 6: eixo de custo COMPUTACIONAL, separado do custo de ANOTAÇÃO que a tese mede |
| C6 | Trocar a camada linear de saída do BERT por uma CNN melhora o F1 nos sete conjuntos, com significância (t-test não pareado, p < 0,05) | Tab. 2, p. 4601 | Cap. 3: nota de arquitetura; o teto de desempenho depende da cabeça de classificação, não só do backbone |
| C7 | DAL cobre ~70% das classes por iteração enquanto as demais estratégias e a aleatória cobrem de 80% a 94% — o que explica seu pior macro F1 | §5.5, p. 4602 | Cap. 5: cobertura de classes como diagnóstico de estratégia de seleção em muitas classes |

## Números que posso citar
Condições comuns: BERT `bert-base-uncased` truncado em 512 tokens, cabeça CNN,
orçamento de AL de **2.000 textos** adicionados de **100 em 100**, cada
experimento repetido com **3 sementes**, batch 16, Adam com taxa inicial 5e-5,
máximo de 15 épocas com parada antecipada, NVIDIA RTX A6000 (§5.3, p. 4601).

- **Escala dos conjuntos (Tab. 1, p. 4599)** — número de classes e co-ocorrência
  média de classes: EurLex **739** (co-oc. 1,88; 44.689 de treino);
  Yelp **580** (2,33); NYT **303** (3,03); arXiv **113** (42,85);
  RCV1 **100** (116,72); Toxic 6 (2.065,47); AGNews 4 (0).
  *O FALCO, com 621 classes, cai entre o Yelp e o EurLex.*
- **Teto de desempenho com o conjunto inteiro (Tab. 2, p. 4601)**, camada linear
  → CNN: EurLex micro 0,62 → **0,78** e macro 0,47 → **0,69**;
  Yelp micro 0,38 → **0,58** e macro 0,26 → **0,52**;
  NYT macro 0,32 → **0,51**; AGNews 0,91 → **0,94**. Todos os ganhos da CNN
  significativos a p < 0,05.
- **Ganho da seleção sobre a aleatória (§5.4, p. 4601)**: EurLex, ALPS e
  subword até **+0,154** de micro F1; NYT, ALPS **+0,25** sobre a aleatória e
  +0,1 sobre a segunda melhor; arXiv, a aleatória **supera** as estratégias por
  até **0,15**; EurLex em macro F1, o ganho cai para **+0,05** (significativo).
- **Custo computacional (Tab. 3, p. 4602)** — segundos para 100 lotes de 16
  (1.600 textos), média dos 5 conjuntos XMTC: subword **3,80 s** (calculado uma
  única vez), ALPS **50 s**, DAL **56 s**, CVIRS **123 s**; aleatória
  desprezível. O CVIRS recalcula do zero a cada iteração e chega a **horas por
  iteração**, levando alguns experimentos a **mais de uma semana** (§6.3,
  p. 4604).

## Citações diretas (com página)
> "Overall, we conclude that none of the selection strategies investigated in
> our experiments manage to consistently improve the AL scheme across all the
> datasets." (§7, p. 4604)

> "we find, that AL improves the classifier on datasets which have low label
> co-occurence: EurLex, NYT and Yelp." (§6.1, p. 4603)

> "while it is true that Micro F1 is a better description of how many mistakes
> our classifier makes overall we should keep in mind that Macro F 1 reflects
> how many of the classes our system is able to discriminate." (§6.2, p. 4604)

## Crítica / limitações (minha leitura)
- **Orçamento pequeno para o espaço de rótulos**: 2.000 textos para 739 classes
  dá menos de 3 textos por classe no melhor caso. Os próprios autores admitem
  no §7 que benchmarks maiores exigirão conjuntos iniciais maiores "para ter
  alguma chance de cobrir parte significativa do espaço de rótulos". O achado
  negativo pode ser, em parte, um efeito de orçamento — o que **não** enfraquece
  o uso na tese, porque o FALCO também opera sob orçamento apertado.
- **Nenhuma estratégia é de LLM**: as quatro são pré-LLM (embeddings, incerteza,
  discriminador). O artigo não fala sobre oráculo LLM; o que ele ameaça é a
  metade "seleção" do FALCO, não a metade "oráculo". A decomposição B−C do
  Cap. 5 é exatamente a que dialoga com ele.
- **Três sementes** e teste t **não pareado** entre curvas com o mesmo pool: o
  regime de significância é frouxo perto do que a tese usa (McNemar pareado e
  bootstrap pareado). Citar os achados como direção, não como magnitude exata.
- **Conjuntos compilados pelos autores** a partir de tarefas hierárquicas: as
  contagens de classe da Tab. 1 são desta compilação, não do benchmark original
  (o Yelp aqui tem 580 classes, e não é o `yelp-full` de 5 estrelas usado em
  outros fichamentos). Não misturar os dois no grafo.

## Discrepância de nome do primeiro autor (registro, não correção)
A entrada do bib tinha `Fromme, Lisa`; corrigi para `Fromme, Lukas`, que é o
que está impresso na primeira página do PDF publicado
(`lukas.fromme@ims.uni-stuttgart.de`, IMS/Universidade de Stuttgart).
Fica um segundo ponto, que **não** corrigi porque muda texto impresso e a chave
de citação: o Crossref (DOI 10.63317/48xs9zc3987o) e a ACL Anthology
(2022.lrec-1.490) indexam hoje o primeiro autor como **Wertz, Lukas** — mesmo
sobrenome do `Wertz2023` do nosso bib, com dois dos mesmos coautores
(Mirylenka e Bogojeska). É a mesma pessoa sob nome diferente do registro
arquivado. Decisão de forma (manter FROMME, como no PDF, ou adotar WERTZ, como
nos índices) sobe ao principal e ao autor; enquanto isso o DOI resolve para a
obra certa em qualquer das duas grafias.

## Ideias que gera para a tese
- **Baseline aleatório com estatura**: usar C1/C2 no Cap. 5 para enquadrar o
  braço D — a tese passa a comparar-se contra um aleatório que a literatura
  mostra ser difícil de bater em muitas classes, o que **fortalece** um
  resultado positivo em vez de enfraquecê-lo.
- **Reportar a co-ocorrência média de classes do nosso conjunto** (métrica da
  Tab. 1) no Cap. 3: é uma linha de estatística descritiva que situa o FALCO na
  condição C3 e dá ao leitor a régua para saber se esperar ganho de seleção.
- **Par de citações que delimita o regime**: `Wertz2022` (100-739 classes,
  seleção não bate aleatório) e `Rouzegar2024` (2-4 classes, tudo bate
  aleatório) citados juntos definem em que faixa a seleção ativa compensa —
  e o FALCO, em 621 classes, cai do lado difícil.
- **Custo computacional como terceiro eixo**: a tese mede custo de anotação e
  desempenho; a Tab. 3 lembra que a estratégia de seleção também custa GPU.
  Uma linha no Cap. 5 dizendo quanto custa a nossa seleção fecha esse flanco.
