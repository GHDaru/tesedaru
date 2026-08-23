---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR — laudo completo das duas frentes, sem editar texto; banca/revisor1/revisor2 seguem o fluxo que você descreveu (laudo → reescrita → cruzada → gate)
referencia: tarefa 20260824-0200 · ghdaru/activetextclassification@b540533 (clone read-only já usado na tarefa 1800) · activelearning/experiments/e5cycle/results/
criada_em: 2026-08-24T02:30:00Z
---

Rodei as duas frentes de leitura de artefato, sem GPU, em paralelo com a
fila do braço E (que continua prioridade e ainda não abriu vaga).

## Frente A — config canônica do AG (`_old`, pop 20)

Medido nos CSVs `ag_detailed_fitness*.csv` do artefato canônico
(`examples/ag_optimization_results_L0_*old/`, legado
`activetextclassification@b540533`) e no código-fonte da mesma linhagem
git (`genetic_l0_optimizerv4.py`, commit `dacfed3` "genetic alterado" — o
mesmo commit que `_old` compartilha com as pastas indisputadas, ver minha
entrega da tarefa 1800):

| parâmetro | valor canônico | fonte/evidência | recuperável? |
|---|---|---|---|
| população ($N_{pop}$) | **20** | contagem de `individual_id` únicos por `generation` em `ag_detailed_fitnessACCURACY_MAXIMIZE.csv` — 0..19, constante em TODAS as gerações, em TODOS os tamanhos de L0 | **sim, direto do artefato** |
| gerações | **100** (exceto $\lvert L_0\rvert=10$) | `max(generation)` no mesmo CSV, por tamanho: 100 para 100/500/1.000/2.500/5.000; **200 para $\lvert L_0\rvert=10$** (confirma o caso especial que a tarefa perguntou) | **sim, direto do artefato** |
| $N_{elite}$ | **2** (indireto: $0{,}1 \times 20$) | dois caminhos: (a) rastreio de `l0_indices_hash` idêntico entre gerações consecutivas — nas gerações iniciais (antes da convergência poluir o sinal), o número de indivíduos top-fitness que passam intactos é consistentemente **2**; (b) `elitism_rate` default = 0,1 no código-fonte (`genetic_optimizer.py` e `genetic_l0_optimizerv4.py`), aplicado a pop=20 dá exatamente 2 — e essa MESMA taxa aplicada a pop=50 dá 5 (o valor do config abandonado) | **recuperável por evidência indireta convergente, não por log direto** |
| torneio $k_t$ | **3** | é o *default* do construtor em **todas** as versões do otimizador no histórico do repo (v2, v3, v4, `genetic_optimizer.py` DDD, e as 3 versões arquivadas) — nunca vi um call-site que sobrescrevesse | **não recuperável por log direto; recuperável por inferência forte (nunca mudou em nenhuma versão do código)** |
| mutação $p_m$ | **0,1** | mesmo argumento — default constante em toda a linhagem, bate com o texto | **idem: inferência forte, não log direto** |
| crossover $p_c$ | **⚠️ NÃO RECUPERÁVEL — possível divergência** | o texto diz 0,8; o *default* do código na mesma linhagem (`genetic_l0_optimizerv4.py` e `genetic_optimizer.py`) é **0,7**, não 0,8. Não achei o script/notebook que de fato instanciou a otimização (não está commitado — rodou fora do repo, provável notebook local/Colab não versionado) | **não — nem confirma nem contradiz o texto; é a única lacuna real** |
| reparo de unicidade | **confirmado, existe no código** | lógica de `unique_genes`/preenchimento sem duplicata no método de crossover, presente idêntica em `genetic_l0_optimizerv4.py` e na versão DDD atual | **sim, por leitura de código (não é parâmetro numérico, é existência de mecanismo)** |

**Resumo para o laudo**: 5 dos 6 parâmetros batem com o Cap.3/A2 (pop 20,
gerações 100/200, elitismo 2, torneio 3, mutação 0,1, mais o mecanismo de
unicidade confirmado). **Um não bate e não dá pra provar**: crossover 0,8
no texto vs 0,7 como default no código — sem o comando real, não decido
qual vale; caveat honesto aqui é o caminho certo, como você pediu.

## Frente B — o "910/1.000" do A7 é impreciso; números corretos: 991 e 982

Achei os dois artefatos direto (`activelearning/experiments/e5cycle/results/`):

| arquivo | classificador | `n_labeled` | oráculo |
|---|---|---|---|
| `cycle_pvbin.json` | PVBin | **991** | `provider: nvidia, model: nemotron-3-ultra-550b-a55b` (mode `json-prompt`) — **REAL**, não simulado |
| `cycle_sgd.json` | SGD | **982** | idem — **REAL** |

Ambos com `budget: 1000` (bate com "1.000 rótulos orçados" do texto) — mas
**nenhum dos dois usa oráculo simulado, e nenhum dos dois encerra em 910**.
Busquei em todo o repositório por qualquer artefato com `n_labeled: 910` ou
`provider: simulated` persistido: **não existe nenhum**. O único lugar onde
"simulado, ruído 0,2" aparece é a *definição* da flag `--smoke` em
`experiments/e5cycle/run_cycle.py` (smoke test offline) — não há saída
persistida de uma execução real com essa flag e budget 1.000.

**Confirmo integralmente o achado do revisor2**: os números certos são
**991 (PVBin) e 982 (SGD)**, condição **oráculo real** (nemotron via NIM),
sem parâmetro de ruído (não se aplica — não é simulado). "910" e "ruído
0,2" não têm artefato que sustente — parecem ter vindo de outro contexto
(talvez um teste de fumaça nunca persistido, ou memória do redator
confundindo com a definição do `--smoke`).

## Não editei texto

Nenhum `.tex` tocado — as duas frentes são laudo, como pedido. Fico
disponível se a banca/revisor1/revisor2 precisarem de mais alguma medição
depois da reescrita.

## Braço E — sem mudança, ainda em fila de GPU

Nada novo desde a última mensagem; segue retentando sozinho.

## Caixa

Atualizada com esta entrega.
