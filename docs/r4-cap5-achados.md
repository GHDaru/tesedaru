# R4 do Capítulo 5 — afirmações × lastro (MODO AUDITORIA)

> Tarefa `20260823-0330` · agente `revisor1` · **a banca aplica; eu não editei
> uma linha do capítulo.** Mesmo método da R4 do Cap. 3.

## Como foi medido

Varredura por padrão, não por leitura impressionista: **7** conectivos causais
(`porque`, `graças a`, `deve-se a`…), **3** generalizações (`sempre`, `nunca`,
`qualquer`…) e **5** verbos fortes (`prova`, `confirma`, `demonstra`…) — 15
gatilhos no total, cada um lido em contexto e confrontado com a tabela ou o
artefato que deveria sustentá-lo.

**O capítulo é disciplinado.** Nenhuma afirmação órfã, e o hedging da varredura
de orçamento é exemplar (média com heterogeneidade declarada, IC, "não como
unanimidade"). Os achados são de **força excessiva** e de **mecanismo afirmado
sem medição**, não de invenção.

## Achados

### 1. [ALTO] A conclusão do pilar é provada com gabarito e atribuída ao FALCO

**Onde**: fecho da varredura de orçamento.
**O texto diz**: *"com uma política de parada ancorada no modelo forte, o FALCO
atinge o critério dentro do teto de rotulagem da hipótese; a versão executada
apenas parou cedo demais."*

**O problema**: os braços que cruzam o critério (E20–E35) são treinados **com
gabarito** — o próprio texto declara, "20, 25, 30 e 35 mil rótulos, com
gabarito". O FALCO **não** usa gabarito: usa oráculo LLM. E o custo desse
oráculo está medido **neste mesmo capítulo**: 7,2 p.p. de acurácia (A vs.\ B,
nos mesmos 11.936 itens).

Aplicando essa penalidade ao braço que cruza — E20, acurácia 0,858 — chega-se a
≈0,786, **abaixo** do critério de 0,843. Ou seja: o dado disponível não sustenta
que o FALCO atinja o critério; sustenta que **o critério é atingível naquele
volume com rótulos perfeitos**.

O texto reconhece a pendência na oração seguinte ("a confirmação de ponta a
ponta com rótulos de oráculo … é a extensão imediata"), mas a frase-conclusão
já afirmou o que a ressalva depois relativiza — e é a frase-conclusão que a
banca vai ler em voz alta.

**Sugestão**: *"com uma política de parada ancorada no modelo forte, o critério
é atingido dentro do teto de rotulagem **com rótulos de gabarito**; a
confirmação de ponta a ponta com rótulos de oráculo é a extensão imediata."*

### 2. [ALTO] O gate: papel atribuído por um critério cuja restrição falhou

**Onde**: seção da decisão do gate.

O critério **pré-registrado** (Cap. 3) define: *LLM Inicial* = melhor razão
acurácia/custo **sujeito a acurácia mínima de 85% na S-rand**.

O Cap. 5 escreve, na mesma seção: *"nenhum oráculo atinge acurácia ≥ 85% na
S-rand"* — e, três linhas abaixo, *"**LLM Inicial** = deepseek-v4-flash
(melhor razão acurácia/custo: 78–82%…)"*.

A restrição que **define** o papel não foi satisfeita por nenhum modelo, e o
papel foi atribuído assim mesmo. Falta a declaração de divergência que o
princípio VI exige, na primeira menção do resultado afetado. Não é preciso
mudar a decisão — é preciso dizer que a regra foi relaxada e por quê.

**Casa com a divergência nº 1 da R4 do Cap. 3** (o racional do gate está
invertido: 85% está 4,56 p.p. *abaixo* do baseline de 89,56%, não acima). São o
mesmo gate: **a banca deveria tratar os dois na mesma passada**, senão conserta
metade.

### 3. [MÉDIO] "78–82%" é faixa onde o critério exige ponto

O número que decide o gate é a acurácia **na S-rand**. Uma faixa impede o
leitor de conferir contra o limiar de 85%. Pedir estimativa pontual com IC de
Wilson na S-rand, que é a régua declarada no Cap. 3.

### 4. [MÉDIO] A amostra dos testes de significância varia sem regra declarada

O limiar do Inicial é medido na **S-rand**; a superioridade do Avançado, na
**S-strat** ($p<0{,}001$); a equivalência do nemotron, de volta na **S-rand**
($p=0{,}76$). A S-strat é balanceada (3 por classe) e **não é a distribuição de
produção** — "superioridade" nela e limiar na outra são grandezas de populações
diferentes. Declarar a regra de qual amostra serve a qual decisão.

### 5. [MÉDIO] Ponteiro para "Princípio III da constituição do projeto"

**Verifiquei os dois documentos.** Em substância a remissão está certa, mas
aponta para o Princípio III da constituição da **biblioteca `activelearning`**
("Constrained Oracle Output"). O leitor de uma tese vai à constituição **da
tese**, cujo Princípio III é "Afirmações fundamentadas" — assunto sem relação.
Nomear o documento, ou dizer a razão diretamente e dispensar a remissão.

### 6. [MÉDIO] Mecanismo causal afirmado sem medição — o lote de 200

*"$b=200$ degrada para $0{,}481$, **porque** com lotes grandes a seleção repete
redundância dentro do próprio lote antes de o modelo se atualizar."*

O **efeito** está medido (LCE 0,481 ± 0,012 contra 0,493 ± 0,006). A
**redundância intra-lote**, não: nenhum artefato a quantifica. Ou vira
interpretação declarada ("uma explicação compatível é…"), ou se mede.

### 7. [MÉDIO] Dois achados de destaque apoiados na mesma proposição não medida

*"o Macro F1 … **cai** para 0,44 quando o pool inteiro é rotulado, **porque a
amostra ativa é mais balanceada por classe** que a distribuição natural"* e
*"o Macro F1 interno **superestima** … **porque a amostra ativa sobre-representa
classes raras**"*.

Os **efeitos** estão medidos (0,59→0,44; até +34 p.p.). A **composição por
classe da amostra ativa contra a natural** — que é a proposição que sustenta os
dois — não aparece em lugar nenhum.

**Uma única medida fecha os dois achados**, e é barata: os `labeled_idx` já
estão salvos nos `*_state.json` do E6, então a distribuição de classes da
amostra ativa sai sem re-executar nada. Recomendo pedir esse número antes de
reescrever qualquer um dos dois. (O contraste com o PVBin — "que constrói um
protótipo por classe, é imune" — já é evidência a favor do mecanismo; o que
falta é a proposição em si.)

### 8. [BAIXO] "isola a causa na política de parada"

A decomposição pareada elimina o oráculo (A vs.\ B) e a seleção (B vs.\ C), e a
política de parada é o que **resta**. É inferência por eliminação, legítima,
mas "isola a causa" soa a identificação positiva. "Aponta para" custa uma
palavra e diz a mesma coisa sem exceder.

---

## Verificado e SEM achado — registro para ninguém "consertar" o que está certo

- **"Nenhum oráculo sustentaria o critério sob a política de parada
  executada."** Conferi: o braço B (gabarito, mesmos 11.936 itens) dá 0,777 e o
  E (gabarito, 15.000) dá 0,816, ambos abaixo do critério de 0,843. Gabarito é
  o teto de qualquer oráculo, logo a afirmação **se sustenta** — e é a
  qualificação *"sob a política de parada executada"* que a torna correta. Um
  parecer anterior listou esta frase como excedida; **pelos números de hoje ela
  não está**.
- **A vs. B em Macro F1**: o texto diz "praticamente empatam (0,297 vs.\ 0,299,
  com B à frente em duas das três sementes)". Correto e honesto — B está à
  frente, e o texto não tenta o contrário.
- **A leitura (iii) da varredura** ("menos é mais"): declara média, dispersão,
  IC da semente que inverte e recusa explicitamente a leitura de unanimidade. É
  o padrão que os achados 6 e 7 deveriam seguir.

## Já aberto por outro agente — não recontado como meu

O $p=0{,}58$ da calibração de lote vem de outro experimento (aviso `0818` do
revisor2, ainda sem resposta do principal). Aparece no capítulo; o dono do
achado é ele.

---

# ADENDO — o achado 7 está MEDIDO e FECHADO (2026-08-23)

Artefato: `scripts/mede-composicao-amostra-ativa.py` (exit 0). Reconstrói o
*pool* pela receita da biblioteca e lê os `labeled_idx` já salvos nos
`*_state.json` do E6 — **nada foi re-executado**.

| amostra | n | classes | nº efetivo | top-1 | classes raras | massa das raras | razão |
|---|---|---|---|---|---|---|---|
| **POOL INTEIRO (natural)** | 50.000 | 649 | **172,6** | 5,97% | 179 | **0,762%** | 1,00× |
| SGD entropia @15k | 15.000 | 644 | **331,7** | 1,87% | 174 | **2,347%** | **3,08×** |
| SGD aleatório @15k (controle) | 15.000 | 556 | 167,6 | 6,01% | 94 | 0,807% | 1,06× |
| PVBin entropia @15k | 15.000 | 632 | **261,1** | 3,78% | 164 | **1,933%** | **2,54×** |
| PVBin aleatório @15k (controle) | 15.000 | 536 | 168,5 | 5,94% | 80 | 0,687% | 0,90× |

*Nº efetivo* = exp(entropia de Shannon): quantas classes equiprováveis
produziriam a mesma dispersão. Maior = mais balanceado.

## As duas proposições do capítulo, agora com número

**(a) "a amostra ativa é mais balanceada por classe que a distribuição
natural"** — **confirmada**. A entropia com 15 mil rótulos tem número efetivo
de classes de **331,7** contra **172,6** do pool inteiro: **1,92× mais
balanceada**, com 30% dos dados. A classe majoritária cai de 5,97% para
**1,87%**.

**(b) "a amostra ativa sobre-representa classes raras"** — **confirmada**. A
massa das classes raras (menos de 5 exemplos no pool) sai de **0,762%** no
natural para **2,347%** na amostra ativa: **3,08×**. E a cobertura: a entropia
alcança **174 das 179** classes raras com 30% dos dados.

## O controle é o que fecha o argumento

O braço **aleatório** é a testemunha: se o efeito viesse de subamostrar, e não
de selecionar, ele apareceria lá também. **Não aparece.** O aleatório fica em
167,6 de número efetivo contra 172,6 do natural — indistinguível — e a massa
de raras em 1,06×. E colhe só **94** das 179 classes raras, contra 174 da
entropia.

Ou seja: não é o tamanho da amostra que rebalanceia, **é a seleção por
incerteza**. Os dois parágrafos do capítulo podem passar de "porque" assertivo
a "porque", medido, com este número ao lado.

O padrão se repete no PVBin (1,51× em número efetivo, 2,54× em massa de raras),
o que mostra que o mecanismo não depende do classificador — coerente com o
capítulo dizer que o PVBin é imune ao *efeito no Macro F1* por construir um
protótipo por classe, e não por selecionar diferente.

## Escopo honesto do que este adendo fecha

Fecha o **achado 7 inteiro** — que embalava as duas afirmações do capítulo.
**Não** fecha o achado 6 (a redundância intra-lote que explicaria a degradação
em $b=200$): é outro mecanismo, e continua afirmado sem medição.

## De quebra, dois números de controle da tese conferidos

O script reproduz, de passagem, dois números que o Cap. 3 declara sobre o
*pool*: **65** classes ausentes e **179** com menos de cinco exemplos. Os dois
batem exatos.
