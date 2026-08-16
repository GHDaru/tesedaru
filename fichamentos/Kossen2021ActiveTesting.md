---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Kossen2021ActiveTesting
title: "Active Testing: Sample-Efficient Model Evaluation"
authors: ["Kossen, Jannik", "Farquhar, Sebastian", "Gal, Yarin", "Rainforth, Tom"]
year: 2021
venue: "ICML 2021, PMLR 139:5753-5763"
doi: ""
pdf: referencias-pdf/Kossen2021ActiveTesting.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P4]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: [teste-ativo]                      # "active testing" (pendente no vocabulário)
uses_methods: [aprendizado-ativo, pool-based, entropia, amostragem-por-incerteza, estimador-lure]
datasets: [mnist, fashion-mnist, cifar-10, cifar-100]  # pendentes no vocabulário
metrics: [acuracia]
tasks: [classificacao-de-imagens, regressao] # pendentes no vocabulário
models: [rede-neural-bayesiana, resnet, wideresnet, processo-gaussiano, random-forest]  # pendentes no vocabulário

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: [Farquhar2021Bias]
compares_with: []
contradicts: []
builds_on: [Farquhar2021Bias, Houlsby2011]

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Segunda citação obrigatória do parecer R6 item 10 [Dom-M3].
           Estabelece que rotular o conjunto de TESTE também é caro e que o
           viés de seleção 'is far more harmful for testing than it is for
           training' — a justificativa de literatura para o instrumento
           interna vs. externa do E6 e para o conjunto reservado que o FALCO
           exige. A tese cita o fenômeno e o framework daqui; reivindica a
           quantificação no seu cenário, não a descoberta."
  - type: ameaca
    target: FALCO
    note: "Mostra que avaliar um modelo em pontos adquiridos por incerteza
           SUPERESTIMA a perda de teste (subestima o desempenho), pior em
           modelos sobreconfiantes — exatamente o risco do teste interno do
           laço FALCO se usado para decidir parada/liberação. Também expõe o
           custo da alternativa não adotada: corrigir por LURE exigiria
           registrar q(i_m) e manter um surrogate; o FALCO responde com
           população reservada."
---

# Active Testing: Sample-Efficient Model Evaluation

## Resumo (5-8 linhas, com as MINHAS palavras)
Introduz o "active testing": seleção ativa de quais pontos de TESTE rotular
para avaliar um modelo com poucos rótulos, argumentando que a literatura de AL
reduz o custo de rotular treino mas assume teste grande de graça — irrealista
quando rótulo é caro. Como a seleção ativa enviesa a estimativa (avaliar nos
pontos mais incertos superestima a perda), aplica o estimador não-viesado
R_LURE de Farquhar et al. (2021) e deriva funções de aquisição próprias para
avaliação (proposta ótima q* ∝ perda esperada, aproximada por um modelo
surrogate). Mostra que as aquisições boas para avaliar diferem das boas para
treinar (incerteza aleatórica importa; informação mútua/BALD desempenha mal).
Com surrogates de ensemble, obtém a mesma precisão do teste i.i.d. com fração
dos rótulos (custo relativo ~0,25 em CIFAR-10/Fashion-MNIST) em modelos de
GP e floresta aleatória a ResNet-18 e WideResNet.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | A literatura de AL ignora o custo de rotular dados de TESTE, assumindo irrealisticamente conjuntos de teste grandes; rótulos de teste são tão caros quanto os de treino | Abstract; §1, p. 1 | Cap. 2/5: motivação do instrumento interna vs. externa do E6; o cenário FALCO (rótulo caro) inclui o teste |
| C2 | Adquirir pontos onde o modelo é menos certo tende a SUPERESTIMAR a perda de teste (pontos mais difíceis que a média); o efeito é mais forte em modelos sobreconfiantes e mina seleção de modelos e ajuste de hiperparâmetros | §1, p. 2 | Cap. 5 (E6): mesmo mecanismo e mesmo sinal do resultado de acurácia interna da entropia (subestima até 14 p.p.) |
| C3 | O viés de seleção "is far more harmful for testing than it is for training" — no treino ele pode até ajudar (regularização), no teste queremos viés mínimo | §1 p. 2; box "Why are acquisition strategies different...", p. 5 | Cap. 5: por que a tese trata o viés na AVALIAÇÃO e não repondera o treino; par com Farquhar2021Bias C6 |
| C4 | R_LURE (Eqs. 3-4) corrige o viés da seleção ativa no teste e, com proposta adequada, reduz (drasticamente) a variância vs. teste i.i.d. | §2.2, p. 2-3 | Cap. 6/trabalho futuro: alternativa por reponderação ao conjunto reservado |
| C5 | A proposta ótima é q*(i_m) ∝ perda esperada sob o verdadeiro p(y|x) (aprox. por surrogate, Eq. 6); para classificação vira entropia cruzada entre preditiva do surrogate e do modelo (Eq. 12) | §3.1-3.3, pp. 3-4 | Contexto metodológico; mostra o custo de implementação da alternativa |
| C6 | Funções de aquisição de AL não transferem para avaliação: informação mútua (BALD) desempenha PIOR que entropia preditiva no active testing, pois ignora incerteza aleatórica, que é crítica para estimar perda | §5.6, Fig. 8b, p. 8 | Cap. 2: nuance de posicionamento — avaliar ≠ treinar; reforça que o E6 mede um problema próprio, não um subproduto do seletor |
| C7 | Active testing atinge a precisão do i.i.d. com fração dos rótulos: custo relativo de rotulagem ~0,25 (fator ~4) em Fashion-MNIST/CIFAR-10 e ~fator 2 em CIFAR-100 | §5.3, Fig. 6b, p. 7 | Cap. 6: quantifica o que a tese economizaria adotando teste ativo no lugar da população reservada rotulada |
| C8 | Sem correção, estimativas com aquisição por entropia preditiva são viesadas e claramente superestimam o erro do modelo | §5.5, Fig. 8a, p. 8 | Cap. 5 (E6): confirmação experimental independente do sinal do viés em acurácia/perda |

## Números que posso citar
- Sintético (GP/GP/GP prior, Fig. 3a): com **5** rótulos de teste ativos o
  desvio-padrão da estimativa já é tão baixo quanto o do i.i.d. com **40**
  (quase o conjunto inteiro); 5000 execuções (2500 em c), sombreado = 1 dp.
- Custo relativo de rotulagem (Fig. 6b, medianas sobre 1000 conjuntos de
  teste): **~0,25** (fator ~4 de economia) para Fashion-MNIST e CIFAR-10
  (ResNet-18) — inclusive estimando ACURÁCIA (curva "CIFAR-10 Accuracy") —
  e mais próximo de **fator 2** para CIFAR-100 (WideResNet).
- Escala: treino de 50.000 pontos em CIFAR-10/100 (§5.3); cenário small-data
  com **250** pontos de treino no estudo de surrogates (§5.2, Fig. 4:
  medianas sobre 1085/872 execuções).
- Condições: perda = entropia cruzada (Eq. 12) salvo indicação; surrogates de
  ensemble (deep ensemble de ResNets treinado só em D_train já supera i.i.d.);
  probabilidade mínima de proposta imposta para limitar os pesos (§5, p. 6).

## Citações diretas (com página)
> "existing literature largely ignores the cost of labeling test data,
> typically unrealistically assuming large test sets for model evaluation"
> (p. 1, Abstract)

> "For example, acquiring points where the model is least certain (Houlsby
> et al., 2011) will likely overestimate the test loss: the least certain
> points will tend to be harder than average. Moreover, the effect will be
> stronger for overconfident models, undermining our ability to select models
> or optimize hyperparameters." (p. 2)

> "this bias is far more harmful for testing than it is for training." (p. 2)

## Crítica / limitações (minha leitura)
- Avalia um modelo FIXO ("f is fixed as given", §2): não cobre o laço completo
  de AL em que o mesmo processo de seleção contamina treino E teste interno a
  cada iteração — o cenário do E6. A tese mede o viés emergente do laço, não o
  de um teste ativo desenhado de propósito.
- Só imagens e regressão sintética; sem texto, sem oráculo imperfeito (rótulo
  de teste = gabarito). Transferência para texto curto pt-BR com oráculo LLM
  é exatamente a lacuna que o E6 preenche.
- Métricas: perda (entropia cruzada/MSE) e acurácia; nada de Macro F1 nem
  desbalanceamento — o sinal invertido do Macro F1 interno (+34 p.p. no E6)
  está fora do alcance dos dois papers do lote.
- O método exige infraestrutura própria (surrogate retreinado, registro de
  q(i_m), pesos v_m); a tese pode citá-lo como alternativa mais barata em
  rótulos, mas mais cara em engenharia, à população reservada.

## Ideias que gera para a tese
- Par de citação com Farquhar2021Bias no parágrafo Dom-M3: Farquhar formaliza
  e corrige o viés no laço de treino; Kossen mostra que na AVALIAÇÃO ele é
  ainda mais nocivo e propõe o teste ativo. A tese então delimita: reivindica
  a quantificação do viés de autoavaliação no seu cenário (17,1±1,0 p.p.
  acurácia; +34 p.p. Macro F1; sinal dependente da métrica), não o fenômeno.
- C6 responde a uma possível objeção da banca ("por que não usar BALD/MI no
  laço?"): mesmo para avaliação as aquisições de AL não transferem.
- Trabalho futuro (Cap. 6): substituir parte da população reservada rotulada
  por teste ativo com surrogate (C7 sugere ~4x menos rótulos de avaliação),
  medindo se a economia sobrevive a texto curto e classes desbalanceadas.
