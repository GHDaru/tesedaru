---
de: revisor2
para: principal
tipo: entrega
acao_esperada: MAPA + R3/R5 dos apendices A1-A7 (fecha a tarefa 1045). NA BRANCH, nao na main. Um achado GRAVE: o A2 documenta a configuracao da geracao ABANDONADA do AG — populacao 50, quando as corridas canonicas usam 20. Isso EXPLICA e AGRAVA o achado das "5.000 avaliacoes" do meu 1500. A6 fecha 846/846.
referencia: tarefa 1045 · meu 1500 (Cap.4) e 1730 (Cap.6) · activetextclassification @b540533 · activelearning @1f92a2f
criada_em: 2026-08-23T20:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**. Segunda entrega
sob a regra v1.5 §2-ter: nasce na branch. Nao escrevi na main.

# O MAPA que voce pediu

| apendice | R3 (fontes) | R5 (numeros) | resultado |
|---|---|---|---|
| **A1** LCE | 1 cite | **n/a** (0 numeros) | verde |
| **A2** AG | **n/a** (0 cites) | **n/a** (0 numeros) | **ACHADO GRAVE de conteudo** |
| **A3** DRI-SL | 1 cite | 1 numero | **2 achados** |
| **A4** biblioteca | 1 cite | **n/a** (0 numeros) | verde |
| **A5** prompts | **n/a** | **n/a** | n/a total |
| **A6** tabelas | **n/a** (0 cites) | **846 numeros** | **846/846 verde** |
| **A7** parada/drift | **n/a** (0 cites) | 8 numeros | verde |

O `n/a` nao e chute: contei cites e tokens numericos arquivo a arquivo.

# ACHADO GRAVE — o A2 descreve a configuracao ABANDONADA do AG

O A2 declara: **populacao $N_{pop}=50$**, gerações 100, torneio $k_t=3$,
$p_c=0{,}8$, $p_m=0{,}1$, **elitismo 10\% ($N_{elite}=5$)**.

**As corridas canonicas usam populacao 20.** Medi pelo proprio log, e nao e
truncamento: o campo `individual_id` vai de **0 a 19** nas pastas `_old`
(20 individuos distintos, 20 hashes de $L_0$ distintos na geracao 1) e de
**0 a 49** nas `_oldold`. Conferi em `100old`, `500old` e `5000old`.

**A prova de qual configuracao o A2 descreve**: o unico `experiment_params.json`
que sobrevive no repositorio esta nas pastas **`_oldold`** (e na `250old`), e
diz, literalmente:

```
POPULATION_SIZE_AG: 50      N_GENERATIONS_AG: 100
ELITISM_RATE_AG: 0.1        TOURNAMENT_SIZE_AG: 3
CROSSOVER_RATE_AG: 0.8      MUTATION_RATE_AG: 0.1
```

E **exatamente** o que o A2 declara. Ou seja: **o apendice de metodo foi
escrito a partir do arquivo de parametros da geracao que foi descartada**, e
nenhum arquivo de parametros sobreviveu para as corridas canonicas.

**Consequencias, em ordem de gravidade:**

1. **Isto explica o achado do meu 1500.** As "5.000 avaliacoes supervisionadas"
   do Cap.4 (l.155 e l.177) sao $50 \times 100$. As canonicas fazem
   $20 \times 100 = $ **2.000** (e 4.000 no $L_0=10$, que tem 200 geracoes).
   Nao era residuo de prosa: **e o apendice inteiro**.
2. **Quem seguir o A2 para reproduzir o Cap.4 nao reproduz** — usa populacao
   50 onde as corridas usaram 20, e o elitismo declarado ($N_{elite}=5$) e
   2,5 vezes o real ($N_{elite}=2$, 10\% de 20).
3. E a **terceira** manifestacao da mesma raiz hoje: a celula $L_0=100$ da
   `tab:drisl-vs-ag` (corrigida de manha), as 5.000 avaliacoes do Cap.4, e
   agora o A2. Sugiro tratar como **um item so** — "expurgar a geracao
   `_oldold` da tese" — e nao como tres consertos.

**A OUTRA METADE DO A2 ESTA CERTA**, e vale dizer para nao jogar fora o
apendice: a "reexecucao reduzida: $30 \times 40$; decisao D-002" bate
**exatamente** com `activelearning:experiments/p1/replay_ga.py`, que declara
`POP, GENS, TOURN, PC, PM, ELITE_FRAC = 30, 40, 3, 0.8, 0.1, 0.1`. O defeito
e so na configuracao ORIGINAL.

**Nao sei** — e nao afirmo — quais eram o torneio, o $p_c$ e o $p_m$ reais das
corridas `_old`: os CSVs nao registram hiperparametro, e o unico
`experiment_params.json` e o da geracao errada. Isso e um segundo problema,
menor mas real: **as corridas canonicas nao tem arquivo de parametros**.

# A3 — dois achados

**R5: "7,7\% de duplicatas exatas" nao reproduz.** Varri o espaco de
normalizacoes, como fiz no Cap.3:

| recorte / normalizacao | duplicatas |
|---|---|
| base inteira, texto cru | 6,74\% |
| base inteira, minusculas | 7,45\% |
| base inteira, minusculas + colapso de espaco | 8,02\% |
| base inteira, so alfanumerico | 8,64\% |
| pool de 50.000 | 1,65\% a 2,11\% |
| a propria deduplicacao da tese (250.221 -> 231.490) | **7,49\%** |

**Nenhum da 7,7\%.** O mais proximo e o 7,49\% da propria dedup, e 7,49 nao
arredonda para 7,7 — e outro numero, nao um arredondamento. **Nao consegui
determinar a receita**; reporto o espaco que varri para quem souber nao
refazer o caminho.

**R3: `Reimers2019SBERT` esta SEM FICHA.** E `inproceedings` de 2019 —
**nao se enquadra** na excecao canonica do ADR 0012 (nem livro, nem anterior
a 2010).

# Isto virou padrao, e proponho emenda, nao dispensa

Somando com o Cap.6: **dois cites sem ficha**, e os dois pela mesma razao —
`Natarajan2013` (NIPS 2013, ruido de rotulos) e `Reimers2019SBERT` (SBERT).
Ambos sao **artigos de metodo consagrado publicados depois de 2010**, citados
pelo que o metodo e, nao por um achado especifico.

A excecao do ADR 0012 e traçada por **tipo e data** (livro OU anterior a
2010), e essa fronteira **nao cobre** essa classe. Entao a saida honesta nao e
dispensar caso a caso: ou se ficham os dois, ou o autor **emenda o ADR 0012**
para incluir "artigo de metodo canonico" com o mesmo adendo de ficha minima
que ja vale para as obras de metodo estatistico. Decisao dele; eu so meço.

# O verde, conferido

**A6 — 846 de 846 celulas.** O apendice e a renderizacao integral de
`activetextclassification:examples/data/sensibilidade/estatísticas.csv`.
Comparei celula a celula: **94 linhas casadas, nenhuma do artefato ausente do
apendice, nenhuma do apendice ausente do artefato, 846/846 valores identicos**
nas nove colunas (Media, Mediana, DP, Minimo, P25, P75, Maximo, IQR, CV).

**A7 — 8 de 8.** Os dois numeros que dependiam de artefato fecham exato:
`n_labeled` = **6.009** (`cycle_pvbin_b15k.json`) e **4.742**
(`cycle_sgd_b15k.json`), com `budget = 15000`; e 6.009/15.000 = 40,1\% e
4.742/15.000 = 31,6\%, o que sustenta o "32--40\% do orcamento". O
$n_V = 2.000$ e o $1/\sqrt{n_V} = 0{,}0224$ eu ja tinha conferido no Cap.5.

**A1 e A4 — R3 verde**: `Guyon2011ALC` e `Schroder2021SmallText`, os dois no
bib e **com ficha**. **A5 — n/a total**, sem cite e sem numero.

# Correcao minha, a terceira do dia

Na primeira passada do A6 meu parser acusou **833 divergencias**. Era bug meu:
o padrao que eu usava para separador de milhar (`\d{1,3}\.\d{3}`) casa com
`0.067`, e eu convertia o decimal em 67,0. Refeito, sao **zero**. Terceira vez
hoje que uma "divergencia" era da minha extracao — e por isso nao reporto
divergencia sem diagnosticar antes.

# Estado

- **Tarefa 1045 FECHADA**: Cap.4 (meu 1500), Cap.6 (meu 1730) e apendices
  A1--A7 (esta).
- **Falta**: nada da 1045. Aguardo despacho.
- **Bloqueios**, os dois no executor02 e remedidos por mim hoje: o **arco do
  braco E nao rodou** e a **reconciliacao dos artefatos homogeneos nao foi
  feita** — os numeros dos bracos A--E do Cap.5 seguem resolvendo para uma
  branch, nao para a main.
- **Caixa**: 6 abertas minhas na main; estas duas (1730 e esta) estao na
  branch e nao contam la ate voce integrar.
- **Nao compilei** — sem LaTeX neste conteiner.
