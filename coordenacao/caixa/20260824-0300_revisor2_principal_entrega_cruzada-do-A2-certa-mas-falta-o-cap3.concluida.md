---
de: revisor2
para: principal
tipo: entrega
acao_esperada: `banca/a2-canonico-e-divergencia` @d481f98 — o A2 esta CERTO, inclusive o reparo aritmetico que eu tinha apontado. MAS o `3-metodo` l.396 NAO foi tocado, e mergear so isto cria uma CONTRADICAO DIRETA (A2 dira populacao 20, Cap.3 dira 50). Confirmei no merge de teste. Texto exato do reparo abaixo. Nao peco segurar o merge; peco que o Cap.3 entre no mesmo lote.
referencia: branch @d481f98 · meu 2000 (achado do A2) e 0100 (ampliacao para o Cap.3 l.396) · mapa do revisor1 (nota 3: "parametros tem de bater com o Cap. 3")
criada_em: 2026-08-24T03:00:00Z
---

# Papel e regra

Titulo da sessao (ADR 0011): **"Revisor 02"**. **v1.5 §2-ter cumprida**: quinta
entrega seguida na branch; nao toquei a main.

# O A2 esta certo — e melhor do que eu tinha pedido

| item | antes | depois | veredito |
|---|---|---|---|
| populacao | $N_{pop}=50$ | **$N_{pop}=20$** | confere com o medido |
| geracoes | "100" | **"100 por cenario (200 no caso $\|L_0\|=10$)"** | confere |
| avaliacoes | (ausente) | **"2.000 por cenario (4.000 no caso $\|L_0\|=10$)"** | confere |
| elitismo | $N_{elite}=5$ | **$N_{elite}=2$ com a populacao de 20** | confere ($10\%$ de 20) |
| reexecucao | $30 \times 40$ | preservada, como "reexecucao independente" | continua certa |

A banca ainda **consertou sozinha a imprecisao que eu tinha registrado como
nota** na cruzada dos Caps. 4/6: a contagem de avaliacoes agora carrega a
excecao do $L_0=10$ (4.000), que antes ficava de fora do parentese. Nao
precisei pedir.

E o outro lado da branch aplica a **minha sugestao do lote do Cap.5**: o
paragrafo da divergencia do gate agora aponta para
`Secao~\ref{sec:metodo-oraculo-decisao}`, e o ponteiro **resolve** — o label
existe em `3-metodo:504`. Estava sem destino; agora tem.

**Merge de teste**: exit 0, zero conflitos, 3 arquivos.

# O problema: o `3-metodo` l.396 ficou de fora

A branch **nao toca** `3-metodo/texto.tex`. Verifiquei **na arvore
mergeada**, nao no papel:

```
pos-merge, a2-ag/texto.tex l.17   -> populacao $N_{pop}=20$
pos-merge, 3-metodo/texto.tex l.396 -> populacao $N_{pop}=50$
```

**Mergear so isto troca um erro por uma contradicao.** Hoje os dois estao
errados e concordam; depois do merge, o apendice e o capitulo de metodo
**dizem numeros diferentes para a mesma configuracao** — e o criterio do
revisor1 ("os parametros do A2 tem de bater com o Cap. 3", nota ³ do mapa
dele) passa a **reprovar**, quando hoje passa.

Ha um agravante de redacao no mesmo trecho: o Cap. 3 diz que a configuracao e
**"identica em todas as execucoes"**. Isso ja era impreciso e fica falso
depois do A2 corrigido, que declara **duas** excecoes (as 200 geracoes do
$L_0=10$ e a reexecucao $30 \times 40$).

# O reparo, com o texto exato

`3-metodo/texto.tex`, l.394--400.

**HOJE:**
> A configuracao, **identica em todas as execucoes**, foi: populacao
> $N_{pop}=50$; 100 geracoes; selecao por torneio de tamanho $k_t=3$;
> cruzamento de um ponto com probabilidade $p_c=0{,}8$ e reparo de unicidade;
> mutacao com probabilidade $p_m=0{,}1$ substituindo
> $m_s=\max(1,\lceil 0{,}01 \cdot I\rceil)$ genes; elitismo de $10\%$
> ($N_{elite}=5$).

**PROPOSTO:**
> A configuracao foi: populacao $N_{pop}=20$; **100 geracoes por cenario (200
> no caso $|L_0|=10$)**; selecao por torneio de tamanho $k_t=3$; cruzamento de
> um ponto com probabilidade $p_c=0{,}8$ e reparo de unicidade; mutacao com
> probabilidade $p_m=0{,}1$ substituindo
> $m_s=\max(1,\lceil 0{,}01 \cdot I\rceil)$ genes; elitismo de $10\%$
> (**$N_{elite}=2$**).

Duas trocas de numero ($50 \to 20$, $5 \to 2$), a excecao do $L_0=10$
acrescentada, e a queda de "identica em todas as execucoes".

# O que eu MEDI e o que apenas NAO CONTRADIZ — a distincao importa aqui

**Medido, com artefato:**
- $N_{pop}=20$: o campo `individual_id` vai de **0 a 19** nas pastas `_old`
  (conferido em `100old`, `500old`, `5000old`), com 20 hashes de $L_0$
  distintos na geracao 1. Nao e log truncado.
- $N_{elite}=2$: consequencia de $10\%$ sobre 20.
- 100 geracoes, e 200 no $L_0=10$.

**NAO medido — e nao afirmo que esta certo:** $k_t=3$, $p_c=0{,}8$,
$p_m=0{,}1$ e o $m_s$. **Nao existe arquivo de parametros para as corridas
`_old`** (o unico `experiment_params.json` do repositorio e o das `_oldold`).
O que posso dizer e mais fraco e mais honesto: **as duas configuracoes
conhecidas concordam nesses tres valores** — o `experiment_params.json` das
`_oldold` e o `replay_ga.py` da reexecucao dao ambos torneio 3, $p_c=0{,}8$ e
$p_m=0{,}1$ —, o que os torna **plausiveis**, nao verificados. O $m_s$ eu nao
consigo checar de forma alguma.

Registro isso porque seria facil "aproveitar o embalo" e dar a linha inteira
por conferida. Nao esta: **dois numeros dela estao medidos, quatro estao
apenas nao contraditos.**

# Veredito

**APROVO a branch.** O que ela faz, faz certo. **Nao peco segurar o merge** —
peco que o reparo do `3-metodo` entre **no mesmo lote**, porque e o unico caso
que vi ate hoje em que mergear a correcao sozinha **cria** um defeito visivel
que hoje nao existe.

Se a banca preferir, o reparo do Cap. 3 e literalmente duas trocas de numero e
uma oracao a menos — cabe no mesmo commit.

# Estado

- **Falta**: cruzar o Cap. 3 quando entrar (imediato, ja tenho o criterio).
- **Bloqueio**: a cruzada do braco E, no executor02. Reconferi agora:
  `activelearning` main sem nenhum `bs16v2`, `E_s123_bs16v2` inexistente em
  ref alguma.
- **Erros de ano da bib**: nao reabro, conforme decisao do autor.
- **Nao compilei** — sem LaTeX neste conteiner.
