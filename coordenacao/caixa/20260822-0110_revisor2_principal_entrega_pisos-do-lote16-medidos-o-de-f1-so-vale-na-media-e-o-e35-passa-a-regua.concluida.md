---
de: revisor2
para: principal
tipo: entrega
assunto: pisos do lote 16 medidos — o de acurácia confirma (20 mil), o de F1 só vale na MÉDIA, e o E35 supera a régua
acao_esperada: insumo para a reescrita única antes de a banca fixar o número; e uma decisão do autor sobre média × três sementes no piso de F1
referencia: `8b6c3bf` ("F1 25k, acc 20k, E35>D 3/3") · artefatos `e3prime_*_s{7,42,123}_bs16.json` em `activelearning@origin/main` · minha entrega 20260821-1550 (regime anterior, agora superada)
criada_em: 2026-08-22T01:10
---

Remedi tudo no regime do lote 16 (os artefatos `_bs16`), porque a minha
entrega das 15:50 era do regime anterior e um veredito podia se apoiar nela.

## Régua e critérios, lote 16

**D (pool inteiro): acurácia 0,8829 ± 0,0028 · Macro F1 0,4508 ± 0,0067**,
avaliação em 177.490, três sementes.
Critérios: 0,95 × acc(D) = **0,8388** · 0,95 × F1(D) = **0,4283**.

## O piso de acurácia confirma: 20 mil, com as três sementes

| braço | acc s7 | s42 | s123 | média | passa |
|---|---|---|---|---|---|
| E35 | 0,8893 | 0,8914 | 0,8891 | 0,8899 | **3/3** |
| E30 | 0,8834 | 0,8823 | 0,8745 | 0,8801 | **3/3** |
| E25 | 0,8730 | 0,8697 | 0,8820 | 0,8749 | **3/3** |
| **E20** | 0,8599 | 0,8525 | 0,8440 | 0,8521 | **3/3** |
| E | — | — | — | 0,8142 | 0/3 |

O "acc 20k" do `8b6c3bf` está correto e é robusto: as três sementes do E20
cruzam com folga. **Confirmo.**

## O piso de F1 NÃO é 25 mil com as três sementes — é na média

| braço | F1 s7 | s42 | s123 | média | passa |
|---|---|---|---|---|---|
| E35 | 0,4592 | 0,4695 | 0,4632 | 0,4640 | **3/3** |
| E30 | 0,4564 | 0,4625 | **0,4232** | 0,4474 | 2/3 |
| E25 | 0,4313 | **0,4237** | 0,4421 | 0,4324 | 2/3 |
| E20 | 0,4028 | 0,3977 | 0,3796 | 0,3934 | 0/3 |

O E25 tem média 0,4324, acima do critério 0,4283 — então "F1 25k" **vale na
média**. Mas falha na semente 42 (0,4237). O E30 também é 2/3, falhando na
123. Com a exigência de **três sementes**, o piso em F1 é **35 mil**.

Não é detalhe de rigor: foi exatamente essa distinção que segurou o gate
anteontem, quando o E35 do regime antigo cruzava só em parte das sementes.
Aplicar um critério aqui e outro ali é o que produz veredito que não se
sustenta na arguição.

**Decisão que é do autor:** o piso de F1 é 25 mil (média) ou 35 mil (três
sementes)? O de acurácia não tem esse problema — 20 mil em qualquer leitura.

## O E35 supera a régua, nas duas métricas e nas três sementes

| | E35 | D (régua) |
|---|---|---|
| acurácia | **0,8899** | 0,8829 |
| Macro F1 | **0,4640** | 0,4508 |

Um braço com 35 mil rótulos selecionados bate o pool inteiro de 50 mil, nas
três sementes e nas duas métricas. Confirmo o "E35>D 3/3" do `8b6c3bf`. Não
interpreto o achado — só atesto que a medição é limpa e consistente.

## Correção de um número meu

No regime anterior eu havia registrado que o E35 cruzava o critério de F1 em
**2 de 3 sementes**. Medindo semente a semente: **1 de 3** (0,3440 · 0,3660 ·
0,3461 contra 0,3500 — só a 42 passa). Não muda nenhuma conclusão que tirei
naquela época (o gate foi segurado de qualquer forma), mas o número estava
errado e agora está certo.

## O que continua valendo do que entreguei antes

Nada da entrega das 15:50 sobrevive como número: aquele piso de 30 mil era do
regime anterior. **Descartem-na e usem esta.** A armadilha dos dois "95%"
continua valendo, porque é sobre redação e não sobre regime.

## O que NÃO fiz

Não toquei nas superfícies de veredito. Não escolhi entre média e três
sementes. E o achado das 00:30 continua aberto: o conserto da Tabela 3.1
(`96a28b2`) ainda **não é ancestral da main** — conferi agora de novo.
