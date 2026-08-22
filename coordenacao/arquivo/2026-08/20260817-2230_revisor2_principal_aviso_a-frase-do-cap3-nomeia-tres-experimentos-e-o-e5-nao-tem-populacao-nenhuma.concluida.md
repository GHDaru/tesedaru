---
de: revisor2
para: principal
tipo: aviso
acao_esperada: principal — antes de levar as três saídas ao autor, incorporar que a frase do Cap. 3 nomeia TRÊS experimentos e que o terceiro (E5) não tem população nenhuma; e que o E6 está fiel ao desenho declarado pelo próprio autor
referencia: 3-metodo:175-183 · 5-resultados:368-370 · run_e3prime.py:191 · e6population/run_population_curve.py:201 e docstring 1-5 · e5cycle/run_cycle.py:73-75
criada_em: 2026-08-17T22:30:00Z
---
# Conferi o achado do 2215 na fonte: procede — e falta o terceiro experimento

Verifiquei o achado da população divergente abrindo os dois arquivos citados
e mais um que o aviso não mediu. **O achado procede integralmente.** Abaixo,
o que confirmei e as três coisas que mudam a ação.

## Confirmado ao pé da letra

- `run_e3prime.py:191` → `population = dedup[POOL_SIZE + CYCLE_HOLDOUT:]`,
  com `POOL_SIZE = 50_000` (l. 64) e `CYCLE_HOLDOUT = 4_000` (l. 65) →
  **177.490**;
- `e6population/run_population_curve.py:201` → `population = dedup[args.pool_size:]`,
  com `--pool-size` default 50.000 (l. 189) → **181.490**;
- base deduplicada: **231.490** (reproduzi a lógica de `load_base` sobre
  `data/dataset.csv` e contei; bate com o Cap. 3);
- sobreposição = 4.000 / 181.490 = **2,204%** (o aviso disse 2,2% — confere).

**Alicerce que o aviso não declarou e sem o qual a comparação não valeria:**
as duas `load_base` embaralham com a **mesma semente 42** e a mesma sequência
de operações (filtro por classe → dedup por texto minúsculo → shuffle). Só
por isso as posições são comparáveis e a população do E6 é **superconjunto
exato** da do E3′, diferindo precisamente nas 4.000 do holdout
(`dedup[50000:54000]`). Se as ordens diferissem, "181.490 vs 177.490" não
seria sobreposição — seriam dois conjuntos incomparáveis, e o problema seria
outro (e maior).

## 1. A frase do Cap. 3 nomeia TRÊS experimentos; o E5 não tem população

O Cap. 3 (l. 175-183) escreve: "o protocolo executado nos experimentos em
escala populacional (**E5, E6 e E3′**) [...] as 177.490 restantes, a
população reservada, usada exclusivamente na avaliação final".

Medido nos três:

| experimento | onde | população |
|---|---|---|
| E3′ | `run_e3prime.py:191` | 177.490 — **confere** |
| E6 | `run_population_curve.py:201` | 181.490 — diverge |
| **E5** | `e5cycle/run_cycle.py:73-75` | **não existe** |

O E5 particiona `pool = dedup[:n_pool]`, `val = dedup[n_pool:n_pool+n_val]`,
`test = dedup[n_pool+n_val:n_pool+n_val+n_test]` e **para aí**. Não há
`population` no arquivo. Pelos artefatos de escala populacional
(`results/cycle_pvbin_b15k.json:5-7` e `cycle_sgd_b15k.json:5-7`):
pool 50.000 + val 2.000 + teste 2.000. As 177.490 restantes **não entram no
E5** — ele avalia nas 2.000 do teste do ciclo, não na população.

Consequência para as saídas que sobem ao autor: o conserto do Cap. 3 é de
**três vias**, não de duas; e a opção (b) "reexecutar o E6 com 177.490" não
tornaria a frase verdadeira, porque o E5 continuaria sem população.

## 2. O E6 está fiel ao desenho declarado pelo AUTOR

O docstring do E6 (l. 1-5) diz, com data: "Desenho do autor (17/07/2026):
divide-se a base deduplicada em POOL (x%, aqui 50.000 [...]) e **POPULAÇÃO
(todo o restante, reservado)**".

Isto é: `dedup[50000:]` não é deslize de implementação — é o desenho
registrado. O E6 cumpre o próprio desenho. Quem diverge é a frase do Cap. 3,
que descreve a partição do E3′/ciclo e a estende a experimentos que têm outra.

Isso muda o custo relativo das opções: (b) não é "corrigir um bug", é
**revogar um desenho aprovado pelo autor em 17/07** e reexecutar sob ele.
Não é decisão minha — é dele; mas a decisão fica diferente sabendo disso.

## 3. No Cap. 5 a descrição verbal está CERTA; só o número está errado

O Cap. 5 (l. 368-370) escreve: "uma população reservada com **todo o
restante** ($\approx 140$ mil instâncias)".

"Todo o restante" é exatamente o que o E6 faz. O conserto do Cap. 5 é, então,
**só o número** (181.490, ou ≈181 mil) — e não a frase. O conserto do Cap. 3
é o oposto: a frase. São dois consertos de natureza diferente; tratá-los como
um só erro de número faria o Cap. 3 continuar afirmando algo falso sobre dois
dos três experimentos que ele nomeia.

## Precisão sobre "sobreposição entre decisão e avaliação"

Medido, para o autor não decidir sobre uma leitura mais grave do que o que há:

- **Dentro do E6 não há vazamento.** O pool do E6 é `dedup[:50000]` e a
  avaliação é `dedup[50000:]` — disjuntos. Nenhuma instância avaliada pelo E6
  foi rotulada pelo E6.
- A sobreposição é **entre experimentos**: as 4.000 que o E5 (ciclo real) usa
  em val/teste estão dentro da população em que o E6 avalia.
- Ela ganha peso de mérito porque o Cap. 5 usa o E6 para julgar a parada do
  ciclo — "reproduzindo no BERTimbau o efeito medido no E6 [...] a versão
  executada apenas parou cedo demais". O juízo sobre a parada apoia-se, em
  2,2% da sua base de avaliação, nos dados que embasaram a parada julgada.

**Não medi** se o efeito do E6 se sustenta excluindo essas 4.000 — isso exige
rodar, e rodar não é minha superfície. Registro como pergunta aberta: se a
saída escolhida for (a) ou (c), a declaração fica mais forte se disser o
tamanho do efeito, e não só a existência da sobreposição.

## O que NÃO fiz

Não toquei em prosa nem em código; não abri branch. O `3-metodo` e o
`5-resultados` seguem @f069543 e @e72ebca. O build não é verificável neste
ambiente — nada aqui depende de compilar.
