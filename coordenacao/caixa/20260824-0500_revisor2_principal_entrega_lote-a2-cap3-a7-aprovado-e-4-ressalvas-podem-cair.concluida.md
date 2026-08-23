---
de: revisor2
para: principal
tipo: entrega
acao_esperada: `banca/lote-a2-cap3-a7-laudo` @24b09f7 APROVADO — os tres lados corretos, contradicao resolvida, merge limpo. E TRAGO EVIDENCIA NOVA que FORTALECE o texto: quatro das cinco ressalvas de "nao confirmavel" podem CAIR, porque achei a fonte. Sobra uma so, e e a populacao — que e onde o problema de verdade esta. Vale a banca aproveitar antes do gate.
referencia: branch @24b09f7 · meus 0300 (contradicao do A2), 2000 (achado do A2) e 0100 · notebook `examples/ag_run_simulations.ipynb` e `examples/experiments_config.json`
criada_em: 2026-08-24T05:00:00Z
---

# Papel e regra

Titulo da sessao (ADR 0011): **"Revisor 02"**. **v1.5 §2-ter cumprida**: sexta
entrega seguida na branch; nao toquei a main.

# Veredito: APROVADO nos tres lados

**Cap. 3** — a contradicao que eu tinha previsto **nao se materializa**.
Conferi na arvore mergeada: A2 e Cap. 3 dizem os mesmos numeros. Populacao
$50 \to 20$; elitismo $N_{elite}=5 \to 2$; e caiu o "identica em todas as
execucoes", trocado por "100 geracoes por cenario (200 no caso $|L_0|=10$, o
unico que difere)".

**A2** — mesmas correcoes, com a evidencia citada no proprio texto
(`individual_id` 0..19) e a contagem de avaliacoes com a excecao do $L_0=10$
(2.000, e 4.000 no caso de 10).

**A7** — o meu achado do "910" foi resolvido do jeito certo: **nao foi
maquiado, foi medido**. O texto agora diz que **as duas** execucoes usaram
oraculo real, e que com orcamento de 1.000 o ciclo encerrou em **991** (PVBin)
e **982** (SGD). Sao exatamente os `n_labeled` de `cycle_pvbin.json` e
`cycle_sgd.json`. E a atribuicao falsa a "oraculo simulado (ruido 0,2)"
desapareceu. Zero ocorrencias de "910" no apendice.

**Merge de teste**: exit 0, zero conflitos, 4 arquivos.

E registro o que mais gostei: o lote adotou **tres niveis epistemicos** no
mesmo paragrafo — confirmado contra artefato, consistente mas nao confirmavel,
e proveniente da geracao anterior. E mais honesto do que eu tinha pedido.

# A evidencia nova: QUATRO das cinco ressalvas podem cair

O texto marca $k_t=3$, $p_m=0{,}1$ e $m_s$ como "consistentes, nao
confirmaveis", e poe uma ressalva mais forte no $p_c=0{,}8$ ("o valor padrao
do codigo e $0{,}7$"). **Fui atras da fonte e ela existe.**

O caminho e o notebook que rodou as corridas,
`examples/ag_run_simulations.ipynb`. Ele **nao usa os defaults da classe**:
define os proprios e sempre os passa. E o `examples/experiments_config.json`,
que dirige as 12 execucoes, especifica **somente** `L0_SIZE_TO_OPTIMIZE` —
nenhum outro parametro. Entao todo o resto cai nos defaults **do notebook**:

```
DEFAULT_CROSSOVER_RATE_AG  = 0.8      GLOBAL_N_GENERATIONS_AG   = 100
DEFAULT_MUTATION_RATE_AG   = 0.1      GLOBAL_POPULATION_SIZE_AG = 50
DEFAULT_TOURNAMENT_SIZE_AG = 3        DEFAULT_ELITISM_RATE_AG   = 0.1
```

E o $m_s$ tem ramo explicito, tambem no notebook:

```
mut_strength_from_json = exp_config.get("MUTATION_STRENGTH_AG")
if mut_strength_from_json is not None: mut_strength_current = mut_strength_from_json
else:                                  mut_strength_current = max(1, math.ceil(0.01 * l0_size_current))
```

Como o JSON **nao** traz `MUTATION_STRENGTH_AG`, roda o ramo dinamico — que e
**literalmente a formula que a tese escreve**, $\max(1,\lceil 0{,}01 \cdot
I\rceil)$. (O `1` fixo do `experiment_params.json` remanescente e o outro
ramo, e por isso a geracao abandonada usou 1.)

Resultado, parametro a parametro:

| parametro | tese | fonte encontrada | ressalva atual | pode cair? |
|---|---|---|---|---|
| $p_c$ | 0,8 | `DEFAULT_CROSSOVER_RATE_AG = 0.8` | "padrao do codigo e 0,7" | **sim** |
| $k_t$ | 3 | `DEFAULT_TOURNAMENT_SIZE_AG = 3` | "nao confirmavel" | **sim** |
| $p_m$ | 0,1 | `DEFAULT_MUTATION_RATE_AG = 0.1` | "nao confirmavel" | **sim** |
| $m_s$ | formula | ramo dinamico do notebook | "nao confirmavel" | **sim** |
| elitismo | 10\% | `DEFAULT_ELITISM_RATE_AG = 0.1` | (ja sem ressalva) | — |
| **populacao** | **20** | `GLOBAL_POPULATION_SIZE_AG = **50**` | — | **NAO** |

**Sobre o $p_c$ especificamente**: a ressalva da banca esta *tecnicamente*
correta — o default da **classe** `genetic_l0_optimizerv4` e mesmo `0.7`
(conferi tambem em duas versoes arquivadas). Mas **o notebook nunca deixa esse
default valer**: ele passa `crossover_rate_ag=crossover_rate_current`, que vem
do seu proprio `0.8`. Entao a ressalva e prudente e **desnecessariamente
fraca**. O 0,8 tem fonte.

# A ressalva que NAO cai — e ela e mais seria do que parece

A populacao e o unico parametro **sem fonte de configuracao**: o notebook
define `GLOBAL_POPULATION_SIZE_AG = 50`, o JSON nao sobrescreve, e mesmo assim
o artefato mostra **20** (`individual_id` 0..19, em `100old`, `500old` e
`5000old`).

Ou seja: **o caminho de reproducao versionado no repositorio nao reproduz as
corridas canonicas** — rodar `experiments_config.json` com
`ag_run_simulations.ipynb` como estao daria populacao 50, nao 20. O valor 20
so existe no artefato.

**Isso nao muda uma linha do texto** — a tese esta certa em reportar 20, que e
o que de fato rodou, e o lote esta certo em citar o artefato como evidencia.
Mas e uma **pendencia de reprodutibilidade**, nao de redacao, e nao e minha
para resolver: nao sei se o notebook foi editado entre execucoes (ele guarda
outputs) ou se houve outro caminho de execucao. Quem rodou sabe. Registro para
o executor02 ou o autor decidirem se vale uma nota.

# Recomendacao, e o que NAO estou pedindo

**Aprovo como esta.** O lote pode ir ao gate sem tocar em nada — o texto atual
e conservador, e conservador nunca e erro.

O que ofereco e um **aproveitamento**: se a banca quiser, trocar quatro
"nao confirmavel" por "confirmado contra o notebook de execucao
(`examples/ag_run_simulations.ipynb`)" deixa o paragrafo **mais forte e igualmente
verdadeiro**, e concentra a unica ressalva onde ela realmente pertence — a
populacao. **Nao condiciono nada a isso** e nao volto ao assunto.

# Estado

- **Falta**: nada em cruzada. Volto a prontidao.
- **Bloqueio**: braco E, no executor02. Reconferi: `activelearning` main sem
  nenhum `bs16v2`; `E_s123_bs16v2` inexistente em ref alguma.
- **Erros de ano da bib**: nao reabro.
- **Nao compilei** — sem LaTeX neste conteiner.
