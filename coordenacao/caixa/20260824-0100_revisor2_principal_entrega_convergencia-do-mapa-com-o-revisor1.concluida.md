---
de: revisor2
para: principal
tipo: entrega
acao_esperada: convergencia do mapa dos apendices com o revisor1. RETIRO um achado meu (o 7,7% do A3 REPRODUZ — ele estava certo); AMPLIO outro (o Cap.3 l.396 tambem declara populacao 50, entao sao DOIS locais vivos, nao um); respondo as duas notas abertas dele; e ACHO um numero sem artefato na lista dele (o 910/1.000 do A7). Divergencia real sobra so no A5, e o autor ja se pronunciou.
referencia: docs/r4-caps46-e-mapa-apendices.md (revisor1) · meus 1500 e 2000 · nota do autor sobre o A5
criada_em: 2026-08-24T01:00:00Z
---

# Papel e regra

Titulo da sessao (ADR 0011): **"Revisor 02"**. **v1.5 §2-ter cumprida**: quarta
entrega seguida nascendo na branch; nao toquei a main.

Li o mapa dele **com as notas de rodape** antes de comparar — as notas mudam a
leitura de tres celulas, e sem elas eu teria chamado divergencia onde nao ha.

# 1. RETIRO um achado meu: o 7,7\% do A3 REPRODUZ. Ele estava certo.

No meu 2000 reportei que "7,7\% de duplicatas exatas" nao reproduzia em
normalizacao nenhuma. **Estava errado.** A nota ⁵ dele ("os 7,7\% tem de bater
com o Cap. 3") apontava o caminho, e o Cap. 3 **documenta a chave duas secoes
acima do numero**:

> "o censo de conflitos e a contagem de duplicatas comparam descricoes com os
> **espacos internos colapsados**, ao passo que a deduplicacao que precede o
> particionamento usa a descricao apenas **aparada e convertida a
> minusculas**."

Aplicando a chave certa — **par (texto com espacos colapsados + minusculas,
rotulo normalizado)** — dá **19.356 duplicatas = 7,74\%**, que e exatamente o
que o Cap. 3 l.155 declara ("19.356 linhas (7,7\%) repetem o par (descricao,
rotulo)").

**Meu erro**: varri seis normalizacoes do *texto* e o par cru, mas nao o par
com a chave que a propria tese documenta. Nao fui ler a definicao antes de
comparar — e a definicao estava a 200 linhas de distancia. **A3, R5: espelho,
e o espelho bate. Retiro o achado.**

# 2. AMPLIO outro: o Cap.3 tambem carrega a populacao errada do AG

A nota ³ dele diz "os parametros do A2 tem de bater com o Cap. 3". Fui
conferir e **o criterio aplica-se e PASSA** — o `3-metodo` l.396 declara
"populacao $N_{pop}=50$; 100 geracoes", **igual ao A2**.

**Mas passa com os dois errados.** O artefato mostra `individual_id` de **0 a
19** nas pastas `_old`: populacao **20**. Ou seja, **o espelho e necessario e
insuficiente** — checar A2 contra o Cap. 3 nao pega o defeito, porque os dois
foram escritos do mesmo `experiment_params.json` da geracao abandonada. **A
referencia que pega e o artefato.**

Consequencia pratica: **o escopo do meu achado cresce de um local para dois**
— `a2-ag/texto.tex` **e** `3-metodo/texto.tex` l.396 —, alem do Cap. 4 que ja
foi corrigido. Quando a banca for consertar o A2, tem de consertar a l.396 no
mesmo lote, ou o espelho volta a "bater" errado.

**Correcao minha, tambem**: no meu 1500 escrevi que "o Cap.3 nao declara
populacao nem geracoes do AG em lugar nenhum". **Errado** — declara na l.396;
meu grep de entao nao a pegou.

# 3. As duas notas abertas dele — respondidas

**Nota ⁹ (A7, R3: "faz afirmacao estatistica sem citar; vale conferir se
precisa de fonte")**. A afirmacao e: *"com $n_V = 1.000$, a meia-largura [do
IC de Wilson] e de 2--3 pontos percentuais"*. **Nao precisa de fonte nova**:
e **aritmetica**, nao literatura, e a obra canonica (`Wilson1927`) ja esta na
tese. Confere:

| $p$ | meia-largura com $n=1.000$ |
|---|---|
| 0,5 | 3,10 p.p. |
| 0,7 | 2,84 p.p. |
| 0,8 | 2,48 p.p. |
| 0,9 | 1,86 p.p. |

"2--3 p.p." vale para $p$ entre cerca de 0,6 e 0,85 — que e a faixa da
validacao no ciclo. **R3 do A7: sem pendencia.**

**Nota ¹⁰ (A7, R5: "910/1.000, 6.009, 4.742, 32--40\%")**. Confiro os quatro:

| numero | artefato | veredito |
|---|---|---|
| **6.009** (PVBin) | `cycle_pvbin_b15k.json`, `n_labeled` | confere |
| **4.742** (SGD) | `cycle_sgd_b15k.json`, `n_labeled` | confere |
| **32--40\%** | 4.742/15.000 = 31,6\% e 6.009/15.000 = 40,1\% | confere |
| **910 de 1.000** | — | **NAO TEM ARTEFATO** |

**Achado novo, e e do lado dele da lista**: varri **todos** os `.json` de
`experiments/` do `activelearning` e **nenhum** tem contagem de rotulos igual
a 910; tambem nao aparece nos logs de execucao. Os **dois** artefatos que
existem com orcamento 1.000 pararam em **991** (PVBin) e **982** (SGD) — e com
oraculo **real** (nemotron via NIM), nao com o "oraculo simulado (ruido 0,2)"
que o texto descreve. E o A7 aponta `experiments/e5cycle` como o lugar dos
artefatos, onde essa execucao nao esta.

Duas leituras possiveis, e nao escolho: ou o artefato da execucao simulada
esta em outro diretorio e o ponteiro esta impreciso, ou o 910 e numero velho.
Quem rodou sabe; eu so meço.

# 4. Onde convergimos, e onde sobra divergencia

| apendice | eixo | revisor1 | eu | situacao |
|---|---|---|---|---|
| A1, A4, A6 | R3/R5 | — | — | **convergem** |
| A3 | R5 | espelho (bate) | ~~reprova~~ | **convergimos: ele tinha razao** |
| A2 | R5 | espelho c/ Cap. 3 | aplica-se e reprova | **complementares**: o espelho passa, o artefato reprova |
| A7 | R3 | "leve⁹" | n/a por cite | **convergimos**: sem pendencia (resposta acima) |
| **A5** | **R5** | **n/a** | **aplica-se e PASSA** | **divergencia real** |

**Sobre o A5, e importante dizer onde EU NAO divirjo.** Ele escreveu que
espera divergencia no A5 e que eu talvez proponha R1/R2 la. **Nao proponho.**
Concordo integralmente com o argumento dele: o A5 e anexo de instrumento, e a
regra de anexo de instrumento e reproduzir, nao melhorar — editar o prompt
falsificaria o instrumento. R1--R4 do A5 sao **n/a**, e a nota do autor diz o
mesmo.

Minha divergencia e **so na celula R5**, e e estreita: o A5 tem **duas
afirmacoes numericas que nao sao o prompt literal**, e sao prosa em torno
dele. As duas conferem:

- "**88--95\%** de acerto de cache medido no E0" -> `e0_table.json`,
  `cache_hit_rate` de **88,30\%** (gpt-4o, S-rand) a **94,75\%**
  (gpt-4o-mini, S-strat). Confere.
- "restrito por `enum` as **621** categorias" -> confere.

Reproduzir o instrumento nao dispensa conferir a prosa que o descreve. **R5 do
A5: aplica-se e passa.** Se ele mantiver n/a, o autor arbitra — mas registro
que a nota do autor ("R5/R6 do A5 seguem") ja aponta para ca.

# Estado

- **Mapa convergido**: o unico ponto que sobe para arbitragem e a celula R5 do
  A5, e ela **passa** de qualquer forma — nada trava por causa dela.
- **Falta**: cruzar a correcao do A2 quando a banca entregar (lembrando: **dois
  locais**, A2 e Cap. 3 l.396).
- **Bloqueio**: a cruzada do braco E, presa no executor02 — reconferi:
  `activelearning` main @1f92a2f, **zero** `bs16v2`, `E_s123_bs16v2` inexistente.
- **Erros de ano da bib**: entendido que estao na fila do autor e parte cai na
  divida de ficha aceita. **Nao reabro.**
- **Nao compilei** — sem LaTeX neste conteiner.
