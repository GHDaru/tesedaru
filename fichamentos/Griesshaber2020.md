---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Griesshaber2020
title: "Fine-tuning BERT for Low-Resource Natural Language Understanding via Active Learning"
authors: ["Grießhaber, Daniel", "Maucher, Johannes", "Vu, Ngoc Thang"]
year: 2020
venue: "Proceedings of the 28th International Conference on Computational Linguistics (COLING 2020), p. 1158-1171, Barcelona (online)"
doi: "10.18653/v1/2020.coling-main.100"
pdf: referencias-pdf/Griesshaber2020.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: avaliacao
pillars: [P1, P4]
status: fichado

# ===== ENTIDADES =====
proposes: []
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, bald,
               dropout-de-monte-carlo, aproximacao-bayesiana-de-incerteza,
               congelamento-de-camadas, cnn-como-cabeca-de-classificacao,
               selecao-aleatoria, fine-tuning]
datasets: [glue, mnli, qnli, snli, sst-2]
metrics: [acuracia, delta-de-desbalanceamento-de-classe]
tasks: [classificacao-de-texto, inferencia-de-linguagem-natural]
models: [bert-base-uncased]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Devlin2019]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Sexto trabalho da série de regime que venho montando: aprendizado
           ativo VENCE a seleção aleatória sobre BERT com menos de mil rótulos
           — mas em tarefas de 2 a 3 classes. Confirma literalmente a frase da
           L770 da tese ('adaptam AA ao BERT')."
  - type: fundamenta
    target: LCE
    note: "CORRIGIDO em 2026-08-17, ver a seção 'Correção'. A §5 e a Tab. 3
           documentam que a aquisição por incerteza DESEQUILIBRA as classes do
           treino, de 4 a 10 vezes a seleção aleatória. Eu havia registrado
           isso como AMEAÇA ao FALCO; o E6 da própria tese mostra o oposto, e
           o que a evidência combinada sustenta é uma CONDIÇÃO DE CONTORNO: o
           sinal do efeito depende de o pool ser balanceado (Griesshaber, GLUE,
           2-3 classes: afasta do equilíbrio, prejudicial) ou torto (FALCO,
           natural, 621 classes: puxa para o equilíbrio, é o ganho)."
  - type: complementa
    target: DRI-SL
    note: "Restringe o pool a um subconjunto de 20 mil elementos por custo
           computacional, e declara o risco de excluir instâncias relevantes.
           É precedente publicado para a mesma decisão no FALCO, cujo pool tem
           250.221 linhas."
---

# Fine-tuning BERT for Low-Resource Natural Language Understanding via Active Learning

## Resumo (com as minhas palavras)

O trabalho pergunta se o aprendizado ativo (AA) acelera o ajuste fino do BERT
quando há **menos de mil exemplos rotulados** — o regime "de poucos recursos".
Para medir a incerteza do modelo sem sair da arquitetura, os autores usam a
aproximação bayesiana por *dropout* de Monte Carlo: repetem várias passagens
para a frente com o *dropout* ligado também na inferência, e cada passagem devolve
uma predição diferente. A discordância entre essas predições vira o critério de
seleção BALD (*Bayesian Active Learning by Disagreement*). Trocam ainda a cabeça
de classificação padrão do BERT (uma camada densa) por uma rede convolucional,
para que as múltiplas passagens custem pouco: só a cabeça é reexecutada, não o
transformador inteiro. A avaliação usa quatro tarefas do GLUE, partindo de 10
exemplos e somando 100 por rodada até 910. Um segundo experimento congela
camadas do BERT para reduzir parâmetros treináveis. O resultado principal é
duplo: o BALD melhora a acurácia média **e** reduz a dispersão entre execuções.

## Claims relevantes

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O BALD com *dropout* de Monte Carlo bate a seleção aleatória em acurácia média em todos os modelos e em toda a faixa de tamanhos de treino testada | §4.2, p. 1163; Fig. 3, p. 1162 | Cap. 2 §2.5, L770 — sustenta "adaptam AA ao BERT" |
| C2 | A seleção por AA também **estabiliza** o treino: a dispersão da acurácia entre execuções é menor do que com seleção aleatória | §4.2, p. 1163; Fig. 3 (faixas de confiança) | Cap. 2 e Cap. 5 — argumento de variância, não só de média |
| C3 | **A aquisição por incerteza enviesa a distribuição de classes do conjunto de treino**; a seleção aleatória não | §5 "Overall Observation", p. 1165; Tab. 3, p. 1166; Fig. 6, p. 1166 | Cap. 5: **não** é ameaça — ver "Correção". O sinal depende de o pool ser balanceado (aqui) ou torto (FALCO) |
| C4 | O AA seleciona preferencialmente exemplos que treinam as **camadas iniciais** do BERT (as de compreensão geral), não as finais (específicas da tarefa) | §4.3, p. 1163; Fig. 4, p. 1163 | Cap. 2 — mecanismo, não só desempenho |
| C5 | Congelar 25% das camadas melhora o desempenho médio; congelar 50% piora, às vezes abaixo do modelo sem congelamento | §4.3, p. 1164; Tab. 1, p. 1164 | Cap. 3/4 se houver discussão de custo de ajuste |
| C6 | Congelar as camadas **próximas à saída** ($F=-3$) dá o treino mais estável (intervalos de confiança mais estreitos) | §4.3, p. 1164; Tab. 2, p. 1164; §7 Conclusão, p. 1167 | Cap. 4 — decisão de projeto |
| C7 | O conjunto inicial é **arbitrário**, não informado: são os 10 primeiros pontos de um conjunto já embaralhado | §3 "Low-Resource Scenarios", p. 1162; §4.1, p. 1162 | ver "Sobre a colocação da citação na L770" |
| C8 | O pool de não rotulados foi **restringido a 20 mil elementos** por custo computacional, com risco declarado de excluir instâncias relevantes | §4.2, p. 1162-1163 | Cap. 4 — precedente para subamostrar o pool do FALCO |

## Números que posso citar

**Regime experimental** (§3 e §4.1, p. 1161-1162):
- Menos de **1.000** pontos de treino; conjunto inicial $S_{10}$ = **10** exemplos.
- **9** iterações de aquisição, **$Q=100$** exemplos por iteração, até $S_{910}$ = **910** exemplos.
- **$S=50$** passagens estocásticas para a frente por estimativa BALD.
- Pool de não rotulados: **20.000** elementos ($U = S_{20000} \setminus S_{10}$).
- Modelo: BERT$_\text{BASE}$, **12** camadas, **768** dimensões, **12** cabeças de atenção, $\approx$ **110 milhões** de parâmetros (**7.087.872** por camada).
- Médias sobre **$N=3$** execuções (o BERT original reporta o máximo; aqui é a média, justamente para poder analisar estabilidade).
- Quatro tarefas do GLUE: **MNLI** (3 classes), **QNLI** (2), **SST-2** (2), **SNLI** (3).

**Acurácia média com 910 pontos, estratégia BALD** (Tab. 1, p. 1164; $F$ = número de camadas congeladas):

| $F$ | MNLI | QNLI | SST-2 | SNLI |
|---|---|---|---|---|
| 0 (nenhuma) | 0,53 ± 0,021 | 0,76 ± 0,010 | 0,78 ± 0,059 | 0,67 ± 0,015 |
| 3 (entrada) | 0,51 ± 0,021 | 0,78 ± 0,003 | 0,80 ± 0,045 | 0,69 ± 0,002 |
| **−3 (saída)** | **0,52 ± 0,010** | **0,78 ± 0,002** | **0,84 ± 0,013** | **0,69 ± 0,008** |
| 6 | 0,51 ± 0,024 | 0,75 ± 0,014 | 0,81 ± 0,006 | 0,63 ± 0,014 |
| −6 | 0,47 ± 0,020 | 0,77 ± 0,010 | 0,64 ± 0,094 | 0,64 ± 0,067 |

**Largura média do intervalo de confiança** (Tab. 2, p. 1164) — é aqui que o
$F=-3$ ganha de forma limpa: **0,038 / 0,024 / 0,047 / 0,028** contra
**0,054 / 0,049 / 0,108 / 0,061** do modelo sem congelamento. Ou seja, congelar
as três camadas mais próximas da saída corta a variabilidade **pela metade ou
mais** em todas as quatro tarefas.

**Desequilíbrio de classes induzido pela aquisição** (Tab. 3, p. 1166) —
$\Delta|T| = \max_c |T_c| - \min_c |T_c|$, a diferença entre a classe mais e a
menos representada no treino:

| $|T|$ | BALD MNLI | BALD QNLI | Aleatório MNLI | Aleatório QNLI |
|---|---|---|---|---|
| 110 | 13 | 30 | 3 | 4 |
| 310 | 20 | 16 | 1 | 2 |
| 510 | 30 | 36 | 9 | 4 |
| 710 | **37** | **44** | 3 | 2 |
| 910 | 25 | 36 | 9 | 4 |

Máximos: **44** (BALD/QNLI) contra **9** (aleatório/MNLI).

## Citações diretas (com página)

> "To the best of our knowledge, the work presented in this paper is the first
> demonstration of combining modern transfer learning using pre-trained
> Transformer-based language model such as the BERT model with active learning
> to improve performance in low-resource scenarios." (p. 1159)

> "In contrast, we observed that when using the BALD acquisition with
> non-deterministic forward passes, the distribution shows a stronger bias to a
> particular class. This bias increases when sampling more pool data, whereas
> the difference between the biggest and smallest class in $T$ stays constant
> during random acquisition." (p. 1165)

> "The size of $U$ can be seen as a hyperparameter to speed up training with the
> trade off as the risk to exclude highly relevant data points from the
> available pool data." (p. 1162)

> "Since data points in the training set provided by the GLUE Benchmark are
> already shuffled, the subset $S_x$ simply contains the first $x$ data points
> $(S_x = \{s_1, s_2, \ldots, s_x\})$ to ensure the same data selection between
> experiments." (p. 1162)

## Crítica / limitações (minha leitura)

**1. A prosa da §5 afirma mais do que a Tab. 3 mostra.** O texto diz que o viés
de classe "aumenta" conforme se amostra mais do pool. A própria tabela não é
monotônica: o MNLI sobe até 37 em $|T|=710$ e **cai** para 25 em 910; o QNLI
estaciona em 44 e cai para 36. A leitura que a evidência sustenta com folga é
outra, e é suficiente: **o desequilíbrio sob BALD é sistematicamente de 4 a 10
vezes o da seleção aleatória, em toda a faixa**. Se a tese citar este achado —
e eu acho que deve — cite nessa forma, não na forma "aumenta com o orçamento",
que um examinador refuta abrindo a tabela.

**2. O desequilíbrio é grande em termos relativos e pequeno em termos
absolutos — porque só há 2 ou 3 classes.** No QNLI, $\Delta=36$ sobre 910
exemplos e 2 classes significa algo como 473 contra 437: nove por cento de
desvio. É um efeito real e mensurável, mas contido pelo fato de que com duas
classes não há para onde o viés escorrer. **Com 621 classes e 910 rótulos não
existe sequer um rótulo por classe**, e o mesmo mecanismo passa a operar sem
esse teto. O paper não mede isso — não podia, não era o objeto dele — e é
exatamente por isso que ele entra na tese como ameaça declarada e não como
resultado transportado.

**3. Não há custo instrumentado.** Pelo terceiro trabalho seguido da série
(depois de `EinDor2020` e `Yuan2020`), "orçamento" quer dizer **número de
anotações** — $Q=100$ por rodada — e nunca dinheiro, tempo de anotador ou
chamada de API. O oráculo é um anotador humano abstrato, sem preço. Isto
**sustenta** a alegação de lacuna da tese em vez de enfraquecê-la, do mesmo modo
que o `EinDor2020` sustentou.

**4. Sem oráculo LLM e sem português.** O rotulador é humano; os quatro
conjuntos são em inglês. Nas duas dimensões o trabalho fica fora da interseção
que a tese ataca.

**5. Fragilidade estatística declarada pelos próprios autores.** Três execuções
por configuração é pouco, e várias diferenças da Tab. 1 estão dentro do desvio
padrão (MNLI: 0,53 ± 0,021 contra 0,52 ± 0,010 — o congelamento não decide
nada aí). Os autores são honestos quanto a isso: dizem que "não mostram
vantagem conclusiva" do congelamento de camadas finais **em acurácia**, e
transferem a alegação para **estabilidade** (Tab. 2), onde ela de fato se
sustenta. É o tipo de disciplina que a nossa R4 pede.

**6. O que o pool restrito esconde.** Restringir $U$ a 20 mil elementos torna a
comparação BALD × aleatório assimétrica, e os autores dizem isso: a seleção
aleatória pode usar o pool inteiro, "já que não tem o mesmo compromisso". Então
o BALD vence **apesar** de escolher de um pool menor. Isso reforça C1 — mas
significa também que o número reportado não é o teto do método.

## Sobre a colocação da citação na L770 (achado para a R4 do t5)

A frase da tese está **correta**: *"Ein-Dor et al. e Griesshaber et al. adaptam
AA ao BERT"*. É literalmente o que o paper reivindica (p. 1159, citação acima),
e a ficha confirma.

O problema não é a frase, é o **parágrafo em que ela está**, que se chama
**"Partida a frio informada"**. O conjunto inicial deste trabalho são os
**10 primeiros exemplos de um conjunto já embaralhado** (C7) — isto é, uma
semente **aleatória**, o oposto de partida a frio informada. O trabalho é
aprendizado ativo sobre BERT; a informação da partida vem do modelo
pré-treinado apenas no sentido trivial de que o BERT já vem pré-treinado.

**Conserto sugerido, de custo mínimo**: manter a citação onde está, mas
qualificar — algo como "adaptam AA ao ajuste fino do BERT, ainda com semente
inicial aleatória" — o que **fortalece** a tese, porque mostra que a partida a
frio informada só aparece de fato mais adiante na linha (ALPS, DEUCE). Sem a
qualificação, o parágrafo sugere que o problema da semente já estava resolvido
em 2020, e aí a contribuição da Fase 1 do FALCO fica menor do que é.

Vale conferir se o mesmo vale para o `EinDor2020`, citado na mesma frase. Pela
ficha dele, também não faz partida a frio informada.

## A série de regime, agora com seis trabalhos

Este é o **sexto** trabalho que ficho medindo a mesma coisa — se a seleção ativa
vence a aleatória — e o padrão que vinha se desenhando fica mais nítido:

| Trabalho | Nº de classes | Seleção ativa vence? |
|---|---|---|
| `EinDor2020` | 2 | sim (4 a 8 pontos de F1) |
| `Yuan2020` (ALPS) | 2 a 5 | sim |
| `Deng2023fedal` | 3 | sim (2,36 de Macro-F1) |
| **`Griesshaber2020`** | **2 a 3** | **sim (média e variância)** |
| `Rouzegar2024` | 2 a 4 | sim |
| `Wertz2022` | 100 a 739 | **não de forma consistente** |
| **FALCO (esta tese)** | **621** | **a medir** |

Cinco trabalhos abaixo de cinco classes onde o AA ganha; um trabalho nas
centenas de classes onde ele não ganha de forma consistente. O FALCO opera em
621. A leitura não é "o AA não funciona" — é que **a evidência favorável
concentra-se num regime que não é o nosso**, e o único trabalho do nosso regime
é o que dá o resultado negativo. Isso é material para o Capítulo 2 (onde a
lacuna é argumentada) e para o Capítulo 6 (onde as ameaças à validade são
declaradas), e o C3 desta ficha oferece um **mecanismo plausível** para o
resultado do `Wertz2022`: se a aquisição por incerteza enviesa a distribuição de
classes já com duas, com centenas ela pode simplesmente deixar classes inteiras
sem nenhum rótulo.

## Autoria corrompida — a sexta encontrada (CORRIGIDA em 2026-08-17)

| | `referencias.bib` (antes) | PDF, p. 1158 · Crossref | `referencias.bib` (agora) |
|---|---|---|---|
| 2º autor | Julia Maucher | **Johannes** Maucher | **Johannes** Maucher |

O sobrenome está certo, o prenome é falso — é **exatamente o padrão das outras
cinco** entradas corrompidas que a varredura de autoria encontrou (`Ren2021`,
`EinDor2020`, `Baykal2021`, `Xu2017`, `Kowsari2019`): obra real, título certo,
DOI certo, prenome preenchido por plausibilidade. O endereço de e-mail no PDF
(`maucher@hdm-stuttgart.de`) e a filiação (IAAI, Hochschule der Medien
Stuttgart) confirmam a pessoa.

**Correção aplicada em 2026-08-17**, autorizada pela tarefa `20260817-1140`.

E o modo como ela chegou até aqui é o registro que importa: quando fichei esta
obra, eu **achei a divergência à mão** e não podia corrigi-la. Horas depois, o
`scripts/check-autoria.py` entrou na `main` pelo gate e **acusou esta mesma
entrada sozinho, no primeiro run** — a primeira das sete divergências do ciclo
encontrada por máquina em vez de por leitura. É a demonstração do princípio IX
no caso mais concreto possível: o defeito é invisível na saída em PDF, porque
em ABNT o prenome vira inicial, e por isso **nenhuma revisão de leitura o
pegaria**. Só checagem mecânica contra a fonte pega.

Verificado em três fontes independentes antes de aplicar: a *byline* do PDF
(p. 1158), o e-mail institucional (`maucher@hdm-stuttgart.de`) com a filiação
IAAI/Hochschule der Medien Stuttgart, e a Crossref pelo DOI
`10.18653/v1/2020.coling-main.100`. Depois da correção, o `check-autoria`
devolve **zero divergências** e o `check-bib` sai em exit 0.

Dois desvios menores na mesma entrada, também não corrigidos:
- `booktitle = {COLING 2020}` — o nome completo é *Proceedings of the 28th
  International Conference on Computational Linguistics*.
- `Ngoc Thang~Vu` usa til de ligação do BibTeX dentro do nome. Não é erro (o
  sobrenome é "Vu" e o til impede a quebra), mas é o padrão que fez o meu
  próprio `check-autoria.py` produzir falso positivo antes do conserto — deixo
  anotado para quem for mexer.

Confere no bib e no PDF: páginas **1158-1171**, DOI
**10.18653/v1/2020.coling-main.100**, ano **2020**, título idêntico.

## Ideias que gera para a tese

1. **Medir o $\Delta|T|$ do FALCO.** A métrica da Tab. 3 é trivial de calcular
   sobre os nossos artefatos de seleção e responde uma pergunta que a banca vai
   fazer: *quantas das 621 classes o ciclo ativo nunca tocou?* Sugiro a forma
   mais informativa no nosso regime: **número de classes com zero rótulos ao
   fim de cada ciclo**, com a curva ao longo dos ciclos. Vira checagem
   executável no espírito da `verifiable-dod`.
2. **Estabilidade como resultado, não como ruído.** O C2 e a Tab. 2 mostram um
   trabalho publicado que reporta **largura de intervalo de confiança como
   resultado primário**. É precedente para a tese fazer o mesmo em vez de
   reportar só a média — e nós já temos IC de Wilson na lista de métricas
   canônicas.
3. **Justificar a restrição do pool com citação.** Se o FALCO subamostra o pool
   de 250.221 linhas por custo, o C8 é o precedente publicado: dizer que é
   hiperparâmetro, declarar o compromisso e seguir.
4. **Qualificar a L770**, como descrito acima — custa uma oração e fortalece a
   contribuição da Fase 1.

## Correção de 2026-08-17 — o meu claim de "ameaça" estava errado

Ao fichar, registrei o viés de classe como **ameaça** ao FALCO: a seleção por
incerteza desequilibra as classes, foi medido com 2-3 classes, o FALCO tem 621,
logo seria risco. **Escrevi isso sem ter aberto o Capítulo 5**, que já
continha a medida.

O E6 (`5-resultados-falco/texto.tex`, Tab. `tab:e6`) diz o contrário:

- **achado (ii)**: o Macro F1 populacional chega a 0,59 com ~15 mil rótulos por
  entropia e **cai para 0,44 com o pool inteiro rotulado**, *"porque a amostra
  ativa é mais balanceada por classe que a distribuição natural"*;
- **achado (iv)**: estratificar pelas classes previstas captura quase todo o
  ganho, porque *"o que a métrica macro paga é cobertura balanceada de
  classes"*.

O desbalanceamento induzido pela seleção **não é a ameaça: é a fonte do ganho**.

### O que a evidência combinada sustenta de fato

As duas medidas não se contradizem — reconciliam-se pela distribuição do pool:

| | `Griesshaber2020` | FALCO (E6) |
|---|---|---|
| Classes | 2 a 3 | 621 |
| Pool de origem | GLUE, aproximadamente balanceado | natural, fortemente enviesado |
| Efeito da seleção ativa | **desequilibra** (4 a 10× o aleatório) | **equilibra** |
| Consequência | prejudicial | **é o ganho** |

**O sinal do efeito depende de o pool ser balanceado ou torto.** É uma condição
de contorno que explica as duas literaturas de uma vez, e é o que esta obra de
fato oferece à tese — mais útil que a ameaça que eu havia inventado.

### Por que registro em vez de apagar

O erro é do anti-padrão nº 23 que eu mesmo propus algumas horas antes —
diagnosticar contra a cópia desatualizada — na sua forma mais constrangedora:
a cópia desatualizada era a minha ignorância do próprio repositório. Fichei uma
ameaça contra um capítulo de resultados que eu não tinha lido.

A lição operacional, que vale para qualquer ficha futura: **antes de escrever
`falco_relation: ameaca`, abrir o capítulo de resultados que mede aquilo.** Uma
ameaça é uma afirmação sobre a tese, não sobre o artigo, e por isso precisa de
evidência do lado da tese — exatamente como o princípio V exige artefato para
número.
