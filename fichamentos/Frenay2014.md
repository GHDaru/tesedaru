---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Frenay2014
title: "Classification in the Presence of Label Noise: A Survey"
authors: ["Frénay, Benoît", "Verleysen, Michel"]
year: 2014
venue: "IEEE Transactions on Neural Networks and Learning Systems, v. 25, n. 5, p. 845-869"
doi: "10.1109/TNNLS.2013.2292894"
pdf: referencias-pdf/Frenay2014.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: survey
pillars: [P2, P3]
status: fichado

# ===== ENTIDADES =====
proposes: [taxonomia-ncar-nar-nnar]
uses_methods: [ruido-simetrico, ruido-assimetrico, ruido-de-par, ruido-dependente-da-instancia, matriz-de-transicao-de-ruido]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: DRI-SL
    note: "É a fonte formal da taxonomia de ruído de rótulo, anterior e mais
           rigorosa que o Song2023NoisyLabels: NCAR (uniforme), NAR
           (dependente da classe verdadeira, que inclui o RUÍDO DE PAR) e NNAR
           (dependente da instância). O 'ruído estruturado, concentrado em
           pares vizinhos' que a tese descreve tem nome formal aqui:
           **pairwise label noise**, caso particular do NAR."
  - type: ameaca
    target: FALCO
    note: "ATENÇÃO — junto com o Song2023NoisyLabels, esta ficha FECHA a
           verificação da frase de 5-resultados-falco/texto.tex:143. As duas
           fontes citadas ali para sustentar que o ruído estruturado é 'menos
           danoso que o uniforme' foram lidas, e NENHUMA sustenta a afirmação.
           Este survey diz o oposto na direção que mede, e traz um agravante
           específico para o nosso caso de 621 classes — ver a seção 'Veredito'."
---

# Classification in the Presence of Label Noise: A Survey

## Veredito sobre a frase do Capítulo 5 (o motivo desta ficha)

`5-resultados-falco/texto.tex:143` afirma que o ruído estruturado, concentrado
em pares vizinhos, é *"cenário menos danoso ao classificador treinado que ruído
uniforme"*, citando `Frenay2014` e `Song2023NoisyLabels`.

**As duas fontes agora foram lidas. Nenhuma sustenta a afirmação.**

O que este survey diz sobre o ruído assimétrico (NAR), na §II-B-2:

> "In the case of NAR label noise, **it is no longer trivial to decide whether
> the labels are helpful or not.**"

Ou seja: sob ruído dependente de classe, decidir se os rótulos ainda ajudam
deixa de ser trivial — o problema fica **mais difícil de analisar**, não menos
danoso.

E vem o agravante, no mesmo parágrafo, que é específico para o regime desta
tese:

> "However, this condition does not prevent the occurrence of very small
> correct labelling probabilities P(Ỹ = y|Y = y) for some class y ∈ Y, **in
> particular if the prior probability P(y) of this class is small.**"

Traduzindo para o nosso caso: a taxa de erro GLOBAL pode parecer aceitável e,
ainda assim, uma classe de prior pequeno ter probabilidade de rotulagem correta
quase nula. **Com 621 classes e cauda longa, é exatamente a nossa situação** —
e é a situação que o Macro F1 penaliza com força. O survey não diz que o ruído
estruturado é mais brando; diz que ele pode esconder dano concentrado nas
classes raras.

**Busquei o contrário antes de concluir.** A única ocorrência de "less harmful"
no artigo compara **ruído de atributo com ruído de rótulo** (§I) — comparação
diferente, que nada diz sobre uniforme contra assimétrico. E na mesma seção o
survey registra que o ruído de rótulo é *potencialmente mais danoso* que o de
atributo.

**Consequência**: a hipótese do ruído estruturado menos danoso é da tese,
testada no E4, apoiada nos nossos dados. Não é herança da literatura, e as duas
citações têm de sair de sustentação e virar o que de fato sustentam: a
taxonomia (aqui) e o alerta de detectabilidade (no Song2023). É a mesma
formulação condicionada que o Cap. 2 já usa corretamente nas linhas 585-590.

## Resumo (5-8 linhas, com as MINHAS palavras)
Survey de referência, anterior à era do aprendizado profundo, sobre
classificação com rótulos errados. Faz três coisas que continuam valendo:
formaliza o processo de ruído com um modelo probabilístico de três casos
(NCAR, NAR e NNAR), cataloga as consequências do ruído para os classificadores
clássicos, e organiza as defesas em três famílias — algoritmos robustos,
limpeza de rótulo e algoritmos tolerantes. É a fonte que dá nome e álgebra ao
que a literatura posterior chama de ruído simétrico e assimétrico.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Taxonomia formal em três casos: NCAR (erro independente de classe e atributos — o ruído uniforme), NAR (probabilidade de erro depende da classe verdadeira — ruído assimétrico) e NNAR (depende também dos atributos) | §II-B, p. 3-4, Fig. 1 | Cap. 2 e Cap. 5: nomear o ruído do oráculo com rigor. O nosso é NAR, possivelmente NNAR |
| C2 | **Ruído de par** (*pairwise label noise*): duas classes são escolhidas e cada instância de uma tem probabilidade de ser rotulada como a outra; só duas entradas fora da diagonal da matriz de rotulagem são não nulas | §II-B-2, p. 3 | **É o nome formal do "ruído concentrado em pares vizinhos" da tese** — usar o termo em vez da paráfrase |
| C3 | Sob ruído NAR, deixa de ser trivial decidir se os rótulos ainda são úteis | §II-B-2, p. 3 | Cap. 5: contradiz a leitura de "menos danoso"; sustenta a formulação condicionada |
| C4 | A condição de erro esperado menor que 1/2 não impede que uma classe de prior pequeno tenha probabilidade de rotulagem correta muito baixa | §II-B-2, p. 3 | **Cap. 5: o risco específico de 621 classes com cauda longa** |
| C5 | Ruído de rótulo é potencialmente mais danoso que ruído de atributo | §I, p. 1 (referindo [3], [9]) | Cap. 2: justifica por que a tese se concentra na qualidade do rótulo |
| C6 | Ruído de rótulo degrada desempenho, enfraquece a seleção de atributos e aumenta o número de amostras necessário no arcabouço PAC | §III-A e §III-D | Cap. 2: consequências catalogadas, úteis para fundamentar o custo do erro do oráculo |

## Números que posso citar
Este é um survey conceitual e a maior parte dos números pertence às obras
revistas, não a ele. Um dado citável, com a condição:
- Em seleção de atributos sobre dados de microarranjo, **uma única instância
  mal rotulada** levou a cerca de **20%** de genes discriminativos não
  identificados (§III-D, atribuído a Zhang et al. [128]) — exemplo do efeito
  desproporcional do ruído quando há poucos dados.

Ao citar, atribuir ao trabalho original e não ao survey.

## Citações diretas (com página)
> "In the case of NAR label noise, it is no longer trivial to decide whether
> the labels are helpful or not." (§II-B-2, p. 3)

> "this condition does not prevent the occurrence of very small correct
> labelling probabilities P(Ỹ = y|Y = y) for some class y ∈ Y, in particular if
> the prior probability P(y) of this class is small." (§II-B-2, p. 3)

> "In [3], [69], pairwise label noise is introduced: 1) two classes c1 and c2
> are selected, then 2) each instance of class c1 has a probability to be
> incorrectly labelled as c2 and vice versa." (§II-B-2, p. 3)

## Crítica / limitações (minha leitura)
- **Anterior ao aprendizado profundo** (2014) e muito anterior ao oráculo LLM.
  Os classificadores analisados são os clássicos; o efeito de memorização que o
  Song2023NoisyLabels documenta não está aqui.
- **Nenhum experimento próprio**: é revisão. Os números pertencem às obras
  revistas, e citar o survey como fonte de número é o erro que a R4 do t2 e do
  t4 já flagraram duas vezes em outras entradas.
- **Não trata texto curto nem rótulo extremo**, o que torna o C4 uma inferência
  nossa a partir do princípio dele, não um resultado transportado. A inferência
  é direta e o survey a autoriza explicitamente ao falar de classes de prior
  pequeno.

## Ideias que gera para a tese
- **Trocar paráfrase por termo técnico**: onde a tese diz "ruído estruturado,
  concentrado em pares vizinhos", dizer **ruído de par** (*pairwise label
  noise*), caso particular do NAR. Ganha precisão e ancora numa fonte que
  sustenta o que está sendo dito.
- **Usar o C4 como argumento a favor da tese, não contra**: o survey diz que
  ruído assimétrico pode esconder dano concentrado em classes de prior pequeno.
  Isso não enfraquece o FALCO — **explica por que medir com Macro F1 e por que
  o E4 precisou ser feito**. Uma hipótese que a literatura diz ser não trivial
  de decidir é, por definição, hipótese que merece experimento.
- **Par com o Song2023NoisyLabels**: este dá a álgebra (matriz de rotulagem,
  três regimes), aquele dá a evidência empírica moderna (sobreposição das
  distribuições de perda, dificuldade de detecção). Citados juntos, cobrem
  formalização e prática sem que nenhum dos dois precise sustentar o que não
  diz.
