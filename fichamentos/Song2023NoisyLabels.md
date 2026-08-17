---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Song2023NoisyLabels
title: "Learning from Noisy Labels with Deep Neural Networks: A Survey"
authors: ["Song, Hwanjun", "Kim, Minseok", "Park, Dongmin", "Shin, Yooju", "Lee, Jae-Gil"]
year: 2023
venue: "IEEE Transactions on Neural Networks and Learning Systems, v. 34, n. 11, p. 8135-8153"
doi: "10.1109/TNNLS.2022.3152527"
pdf: referencias-pdf/Song2023NoisyLabels.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: survey
pillars: [P2, P3]
status: fichado

# ===== ENTIDADES =====
proposes: []
uses_methods: [ruido-simetrico, ruido-assimetrico, ruido-de-par, ruido-dependente-da-instancia, matriz-de-transicao-de-ruido, efeito-de-memorizacao, small-loss-trick, selecao-de-amostras, correcao-de-perda, co-teaching, aprendizado-multi-rodada]
datasets: [cifar-10, cifar-100, mnist, fashion-mnist, svhn, tiny-imagenet, imagenet, clothing1m, animal-10n, food-101n, webvision, cifar-10n, cifar-100n]
metrics: [acuracia, precisao-de-rotulo, revocacao-de-rotulo]
tasks: [classificacao-de-imagens]
models: [wideresnet]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Frenay2014, Natarajan2013]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: DRI-SL
    note: "Dá o vocabulário formal para descrever o ruído do oráculo LLM: a
           matriz de transição T com Tij = p(ỹ=j|y=i) separa ruído SIMÉTRICO
           (uniforme entre classes) de ASSIMÉTRICO ou dependente de rótulo
           (a classe verdadeira tende a ser trocada por uma classe específica —
           o exemplo do survey é 'cachorro' confundido com 'gato' e não com
           'peixe'), e ambos de ruído DEPENDENTE DA INSTÂNCIA. O ruído
           observado no FALCO — confusões concentradas em pares de classes
           semanticamente vizinhas — é assimétrico nessa taxonomia."
  - type: ameaca
    target: FALCO
    note: "ATENÇÃO — a tese cita este survey em 5-resultados-falco/texto.tex:143
           para sustentar que ruído estruturado é 'cenário MENOS DANOSO ao
           classificador treinado que ruído uniforme'. O survey NÃO sustenta
           isso e, na dimensão que ele efetivamente mede, afirma o CONTRÁRIO:
           sob ruído assimétrico as distribuições de perda dos exemplos
           corretos e incorretos se sobrepõem, o desempenho dos métodos
           robustos 'piora consideravelmente' e identificar exemplos limpos
           fica MAIS difícil (§VII-A, p. 14; §III-E Remark, p. 9; Figuras 5 e 7,
           ambas a 40% de ruído no CIFAR-100). Detalhe na seção
           'Contradição com o Cap. 5' abaixo."
---

# Learning from Noisy Labels with Deep Neural Networks: A Survey

## Resumo (5-8 linhas, com as MINHAS palavras)
Survey de referência sobre treinar redes profundas quando parte dos rótulos
está errada. Organiza o problema em duas metades: **como o ruído é modelado**
(uma taxonomia formal por matriz de transição, separando ruído simétrico,
assimétrico, de par e dependente da instância) e **como se treina apesar dele**
(62 métodos do estado da arte agrupados em cinco famílias: arquitetura robusta,
regularização robusta, função de perda robusta, ajuste da perda e seleção de
amostras). Fecha com estimação da taxa de ruído, o protocolo experimental
consolidado da área — conjuntos sintéticos e conjuntos com ruído real — e uma
agenda de pesquisa. O ponto de partida teórico é o **efeito de memorização**:
redes profundas conseguem ajustar um conjunto de treino inteiro com qualquer
proporção de rótulos corrompidos, e a regularização convencional não resolve.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Taxonomia formal do ruído por matriz de transição: simétrico (`∀i≠j Tij = τ/(c−1)`), assimétrico/dependente de rótulo (`∃i≠j,k Tij > Tik`), de par (`∃i≠j Tij = τ`) e dependente da instância (`ρij(x) = p(ỹ=j\|y=i,x)`) | §II-A-1 e §II-A-2, p. 2-3 | Cap. 2 e Cap. 5: nomear com precisão o ruído do oráculo LLM em vez de dizer só "ruído estruturado" |
| C2 | Redes profundas ajustam o conjunto de treino inteiro sob qualquer proporção de rótulos corrompidos, com má generalização; regularização convencional (aumento de dados, weight decay, dropout, batch norm) não elimina o problema | §I, p. 1-2 (citando Zhang et al. [22]); Fig. 1 (WideResNet-16-8, CIFAR-100, ruído simétrico de 40%) | Cap. 2: fundamenta por que o ruído do oráculo é ameaça real e não detalhe |
| C3 | **Sob ruído assimétrico, o desempenho dos métodos robustos "piora consideravelmente" em relação ao simétrico, porque as distribuições de perda de exemplos corretos e incorretos se sobrepõem** | §VII-A, p. 14 (apoiando-se em Song et al. [141]); Fig. 5(b), p. 9 | **Cap. 5: contradiz a citação atual da linha 143** — ver seção abaixo |
| C4 | O "small-loss trick" — tratar os exemplos de menor perda como corretos, base de boa parte da seleção de amostras — não funciona bem quando essas distribuições se sobrepõem, "como no ruído assimétrico da Figura 5(b)" | §III-E Remark, p. 9 | Cap. 6: limita quais defesas contra ruído são aplicáveis ao nosso caso |
| C5 | O ruído do mundo real é estatisticamente diferente do ruído independente da instância — provado por teste de hipótese sobre o Clothing1M | §VII-A, p. 14 (citando Chen et al. [122]) | Cap. 5/6: ruído sintético uniforme não é bom modelo do ruído de oráculo LLM |
| C6 | A taxa de ruído estimada por validação cruzada tem fórmulas diferentes conforme o tipo: `(1−τ̂)² + τ̂²/(c−1)` no simétrico e `(1−τ̂)² + τ̂²` no assimétrico | Eq. (20), §V-C, p. 13 | Cap. 3/5: se algum dia estimarmos taxa de ruído por esse caminho, a fórmula depende do tipo — e o nosso é o assimétrico |

## Números que posso citar
- **62 métodos** de treino robusto revistos, em **5 famílias** metodológicas,
  comparados por **6 propriedades** (Resumo, p. 1).
- **Figuras 5 e 7**: distribuições de perda no **CIFAR-100 com ruído sintético
  de 40%**, nas duas variantes (simétrico e assimétrico) — é a comparação
  **na mesma taxa** que interessa à tese.
- **Figura 1**: WideResNet-16-8 no CIFAR-100 sob **ruído simétrico de 40%**,
  curvas de treino e teste com e sem regularização.
- **Taxas de ruído dos conjuntos com ruído real** (Tab. IV, p. 13): ANIMAL-10N
  ≈8,0%; CIFAR-10N ≈9,0/18,0/40,2%; CIFAR-100N ≈25,6/40,2%; Food-101N ≈18,4%;
  Clothing1M ≈38,5%; WebVision ≈20,0%.
- **Eq. (20)**, acurácia de teste esperada na validação cruzada entre dois
  subconjuntos ruidosos: `(1−τ̂)² + τ̂²/(c−1)` (simétrico) e `(1−τ̂)² + τ̂²`
  (assimétrico), com `c` = número de classes.

## Citações diretas (com página)
> "In contrast to symmetric noise, the noise is called an asymmetric (or
> label-dependent) noise […] where a true label is more likely to be mislabeled
> into a particular label. For example, a 'dog' is more likely to be confused
> with a 'cat' than with a 'fish'." (§II-A-1, p. 2)

> "Song et al. pointed out that their performance could considerably worsen in
> the instance-dependent (or real-world) noise compared to symmetric noise due
> to the confusion between true-labeled and false-labeled examples. The loss
> distribution of true-labeled examples heavily overlaps that of false-labeled
> samples in the asymmetric noise […] Thus, identifying clean examples becomes
> more challenging when dealing with the instance-dependent label noise."
> (§VII-A, p. 14)

> "the small-loss trick does not work well when the loss distribution of
> true-labeled and false-labeled examples largely overlap, as in the asymmetric
> noise in Figure 5(b)." (§III-E Remark, p. 9)

## Contradição com o Cap. 5 (achado principal deste fichamento)
O trecho `5-resultados-falco/texto.tex:143` afirma que o ruído estruturado,
concentrado em pares vizinhos, é *"cenário menos danoso ao classificador
treinado que ruído uniforme"*, e cita `\citep{Frenay2014,Song2023NoisyLabels}`
como fundamento.

**Este survey não sustenta essa afirmação.** Procurei a evidência nas três
frentes em que ela poderia estar e o resultado é consistente:

1. **Não há, no survey, comparação de dano final entre ruído simétrico e
   assimétrico na mesma taxa.** As tabelas de resultados (II, III) organizam os
   62 métodos por propriedade metodológica, não medem acurácia por tipo de
   ruído. Ausência de evidência, portanto — não é que o survey diga o
   contrário nessa métrica; é que ele não mede essa métrica.
2. **Na dimensão que o survey mede — detectabilidade do rótulo errado — ele
   afirma o oposto.** Sob ruído assimétrico as perdas dos exemplos corretos e
   incorretos se sobrepõem (Fig. 5b, mesma taxa de 40% da Fig. 5a), o
   *small-loss trick* deixa de funcionar (§III-E, p. 9) e o desempenho dos
   métodos robustos "piora consideravelmente" (§VII-A, p. 14).
3. **A intuição por trás da frase da tese não é falsa, é de outra ordem.**
   Trocar uma classe por uma vizinha semântica preserva mais estrutura do que
   trocar por uma classe qualquer, e isso pode de fato custar menos em métrica
   final. Só que essa é uma hipótese sobre o *dano*, e o survey fala da
   *dificuldade de detecção*. São coisas diferentes, e a citação junta as duas.

**Consequência para o texto** (não apliquei — prosa é superfície do
`principal`): a frase do Cap. 5 herda a formulação condicionada que o Cap. 2 já
usa corretamente na linha 585-590 — lá o texto diz que o dano do caso do
oráculo LLM *"não se deduz da regra geral — é examinado empiricamente nesta
[tese]"*. É a formulação certa: a hipótese do ruído estruturado menos danoso é
**nossa, testada no E4**, apoiada nos nossos dados; não é herança da
literatura. O survey continua citável no mesmo lugar — mas para a taxonomia
(C1) e para o alerta de que a detecção fica mais difícil (C3/C4), não para
"menos danoso".

**`Frenay2014` fica pendente**: é o outro fundamento citado na mesma frase,
está atrás do paywall do IEEE e não tenho o PDF. Enquanto ele não chegar, a
frase tem uma das duas fontes verificada e refutada, e a outra não verificada —
não é base suficiente para uma afirmação positiva.

## Crítica / limitações (minha leitura)
- **É um survey de visão computacional.** Todos os conjuntos da Tab. IV são de
  imagem (MNIST, CIFAR, SVHN, ImageNet, Clothing1M, WebVision). Nenhum
  resultado é de texto, e nenhum é de rótulo extremo. Transportar as conclusões
  para 621 classes de texto curto exige a ressalva explícita.
- **O ruído é sintético na maior parte da literatura revista**: os conjuntos
  limpos são corrompidos artificialmente para avaliar. O próprio survey trata
  isso como limitação (§VII-A) e é justamente o ponto em que o FALCO tem algo a
  acrescentar: nosso ruído é de um oráculo real, não simulado.
- **Não cobre ruído de oráculo LLM**, que é posterior ao recorte. As defesas
  catalogadas assumem que o rótulo errado é acidente estatístico, não a saída
  sistemática de um modelo com viés próprio.
- **Publicado em 2023 no periódico, com DOI de 2022** (`10.1109/TNNLS.2022.
  3152527`): o `year = {2023}` do nosso bib segue o fascículo (v. 34, n. 11),
  que é o correto para ABNT.

## Ideias que gera para a tese
- **Nomear o ruído com a taxonomia do survey** no Cap. 5, em vez de "ruído
  estruturado": o nosso é assimétrico (dependente de rótulo) e provavelmente
  também dependente da instância. Ganha precisão e conecta a tese à literatura
  formal com uma citação que se sustenta.
- **Inverter o uso da citação**: em vez de apoiar "menos danoso", usar C3/C4
  para dizer que o nosso cenário é o *difícil* de detectar — e que é por isso
  que o E4 precisou medir o dano em vez de deduzi-lo. O argumento fica mais
  forte, não mais fraco, e passa a ser sustentado pela fonte.
- **Eq. (20) e a Tab. IV como régua**: as taxas de ruído dos conjuntos reais
  (8% a 40%) situam a taxa de erro do nosso oráculo na escala da literatura —
  útil para o leitor saber se estamos num regime brando ou severo.
