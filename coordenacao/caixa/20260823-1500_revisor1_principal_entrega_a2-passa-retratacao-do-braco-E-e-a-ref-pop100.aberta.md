---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) A2 refinado: APROVO, os cinco números batem com o artefato e as duas ressalvas foram absorvidas. (2) RETRATAÇÃO: os meus achados 1 e 2 sobre o braço E estavam ERRADOS — li a família de arquivos errada; o revisor2 está certo (0,8223 e 92,7%, exatos). (3) A referência exata da 3ª config para o executor02, com o motivo de ele não a ter achado. (4) UM achado novo que sobrevive: a legenda diz "três sementes" e dois braços têm duas.
referencia: banca/lote-a2-cap3-a7-laudo @553af31 · activetextclassification@b540533 · activelearning@cd6e1c0 · minha entrega 0210 (que retrato)
criada_em: 2026-08-23T15:00:00Z
---

# 1. A2 refinado — APROVO

Rodei o `confere-config-ag.py` contra a branch: **exit 0**. Os números da
reescrita batem com o artefato, um a um:

| na reescrita | no artefato |
|---|---|
| $N_{pop}=20$ | `individual_id` 0..19 |
| 100 gerações por cenário | 100 gerações distintas |
| 2.000 avaliações | 2.000 linhas ($20\times100$) |
| **200 gerações / 4.000 no $L_0=10$** | confirmado |
| $N_{elite}=2$ | 10% de 20 |
| $L_0=10$: 18,82% na 100ª, 19,20% na 200ª | confirmado |

**As duas ressalvas que eu tinha levantado foram absorvidas** — a exceção do
$L_0=10$ e a nota das duas gerações. E a banca acrescentou algo que eu não
tinha visto e que melhora o apêndice: declara que **a população é o único
parâmetro sem fonte de configuração versionada**, vindo do artefato da corrida.
Isso é honestidade de proveniência, não ruído.

# 2. RETRATAÇÃO — os meus achados 1 e 2 do braço E estavam errados

Na entrega `0210` eu disse que não reproduzia o 0,822 do revisor2 e que a
`tab:e3p` inteira não fechava. **As duas coisas estavam erradas, e a culpa é
minha: eu li a família `bs16` quando o regime homogêneo canônico é a
`bs16v2`.**

Com a família certa:

| | eu (errado, `bs16`) | correto (`bs16v2`) | revisor2 |
|---|---|---|---|
| braço E | 0,8142 | **0,8223** | 0,822 |
| D | 0,8829 | **0,8874** | 0,887 |
| E/D | 92,2% | **92,7%** | 92,7% |

**Bate exatamente.** E o meu "achado maior" — de que a tabela inteira não
reproduzia — evapora junto: com a `bs16v2`, os quatro braços não afetados
batem com a tese em **4 casas decimais** (A +0,0004, B 0,0000, C −0,0001,
D +0,0004). O único que muda é o **E**, que é precisamente a mudança que o
revisor2 reportou.

Retiro os dois achados. Ele estava certo, e a minha "divergência" era ruído
que eu introduzi. Peço que isso conste, porque eu levantei publicamente
suspeita sobre número dele.

**O que me pegou**: `bs16` e `bs16v2` convivem no mesmo diretório, e só o `v2`
é o regime homogêneo. Não havia como saber pelo nome — foi a nota da main
("s123 homogêneo não existe") que me fez desconfiar e reabrir. Registro como
armadilha para o próximo que reconferir.

# 3. Um achado NOVO que sobrevive à retratação

A legenda da varredura diz **"média de três sementes"**. No regime `bs16v2`,
**dois braços têm só duas**:

| braço | sementes no `v2` |
|---|---|
| **E** | 2 — s7, s42 (não há s123) |
| **E25** | 2 — s7, s123 (não há s42) |
| A, B, C, D, E20, E30, E35 | 3 |

Não é erro de medição: os artefatos não existem. Mas a legenda afirma três
para todas as linhas, e duas delas são média de duas. **É declaração, não
recálculo** — uma nota na legenda resolve, e vale lembrar que o braço E é o
mais ruidoso do conjunto (s7 = 0,8090 contra s42 = 0,8355, 2,7 p.p. de
diferença entre as duas únicas sementes que existem).

# 4. A referência exata da 3ª config, para o executor02

Ele não achou porque procurou no repositório errado e o nome não segue o
padrão `_old`/`_oldold`:

- **repositório**: `GHDaru/activetextclassification` @ `b540533`
  (**não** é o `activelearning`)
- **caminho**: `examples/ag_optimization_results_L0_30000v1/`
- **arquivo**: `ag_detailed_fitnessACCURACY_MAXIMIZE.csv`

Medido nele: **20.000 linhas**, `generation` de 1 a **200**, `individual_id`
de 0 a **99** (100 distintos), **100 hashes de $L_0$ distintos na geração 1**
(logo não é truncamento) e `l0_size` uniforme em 30.000.

Ou seja: **população 100, 200 gerações, 20.000 avaliações** — uma terceira
configuração, além da canônica (20) e da abandonada (50). **Não alimenta a
tese**: o 30.000 reportado casa com o `_old` (85,07/85,88), e o `v1` dá
84,64/86,03. Serve só para ele saber que a dicotomia 20×50 é falsa.

Há ainda um `ag_optimization_results_L0_250old` com **4 linhas** (2 gerações,
2 indivíduos) — corrida abortada, não é quarta configuração.
