---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR — causa-raiz encontrada com evidência direta de código+histórico git; proponho o conserto (fixar 20 no notebook/JSON, com nota de proveniência); a "3ª config" de população 100 não achei em artefato nenhum — preciso da referência exata do revisor1 para checar
referencia: tarefa 20260824-0530 · ghdaru/activetextclassification@b540533 · examples/ag_run_simulations.ipynb (commits dacfed3/ca3c614/a3bf612) · examples/experiments_config.json
criada_em: 2026-08-24T06:00:00Z
---

Causa-raiz encontrada, com evidência de código e git — não é achado de
artefato de resultado, é achado de proveniência de execução.

## Causa provável: o valor 20 NUNCA foi commitado

O notebook que roda a varredura (`examples/ag_run_simulations.ipynb`) tem
só 3 commits no histórico inteiro do repositório legado:

| commit | `GLOBAL_POPULATION_SIZE_AG` | `GLOBAL_N_GENERATIONS_AG` |
|---|---|---|
| `dacfed3` ("genetic alterado", criação) | **2** | **1** |
| `ca3c614` ("ag run") | **2** | **2** |
| `a3bf612` ("oraculo", o mais recente) | **50** | **100** |

**Nunca existiu um commit com população 20.** O valor foi de um placeholder
de fumaça (pop=2) direto para o config abandonado (pop=50) — pulando por
cima do valor que de fato gerou os resultados canônicos. Confirma a
hipótese 1 da tarefa: o notebook foi editado entre execuções, e a edição
que produziu o canônico (pop=20) rodou **sem nunca ser commitada** — provável
edição manual interativa (célula 1 do notebook, `GLOBAL_POPULATION_SIZE_AG`
é uma constante Python simples, editável e reexecutável sem gerar diff se
não salva) entre a rodada de fumaça e a rodada abandonada.

**Confirmando o mecanismo de override**: o notebook lê
`experiments_config.json` (também só 1 commit em toda a história, o mesmo
`dacfed3`) e faz `pop_size_current = exp_config.get("POPULATION_SIZE_AG",
GLOBAL_POPULATION_SIZE_AG)` — a JSON versionada **nunca** define
`POPULATION_SIZE_AG` por tamanho de $L_0$ (só `L0_SIZE_TO_OPTIMIZE`), então
sempre cai no valor global do notebook. **Hoje, quem clonar o repo e rodar
como está pega o valor do commit mais recente (`a3bf612` = 50).**

## Bônus: isso também resolve a ressalva do crossover que eu tinha deixado em aberto (tarefa 1800)

Reli a função `execute_single_ag_optimization` do mesmo notebook: ela
**sempre** passa `crossover_rate_ag=DEFAULT_CROSSOVER_RATE_AG` (=0,8,
definido na célula 1) para o construtor — o default 0,7 da classe
(`genetic_l0_optimizer.py`/`v4.py`) nunca chega a valer, porque o notebook
sempre passa um valor explícito. Minha ressalva anterior ("não recuperável")
estava certa sobre o *default da classe*, mas eu não tinha visto que o
*notebook* sempre sobrescreve. Bate exatamente com o que o revisor2 achou
(referenciado na tarefa da banca 0530) — convergência independente, dois
caminhos de leitura diferentes, mesmo resultado.

## A "3ª config" (população 100) — NÃO encontrei artefato que sustente

Vasculhei **todos** os `experiment_params.json` existentes no legado (só 4:
`_100oldold`, `_10oldold`, `_50oldold` = pop 50/gens 100; `_250old` = pop
**2**/gens **2**, um resíduo de fumaça, e $L_0=250$ nem entra na tabela de 5
pontos do Cap.4) e as contagens de `individual_id`/`generation` de TODOS os
CSVs de fitness das pastas `_old`/`_oldold` dos 5 tamanhos canônicos (100,
500, 1.000, 2.500, 5.000) mais o caso especial $L_0=10$. **Não achei
nenhuma execução com população 100 em lugar nenhum.** Os únicos dois
valores reais que existem em artefato são 20 (canônico) e 50 (abandonado),
mais o resíduo pop=2 do `_250old`.

Não tenho acesso à branch do revisor1 nem ao script `confere-config-ag.py`
que ele citou — preciso do hash/caminho exato para conferir essa terceira
config, porque com o que tenho não consigo nem confirmar nem descartar.

## Conserto proposto

Recomendo **fixar 20 no caminho versionado**, não deixar como limitação:
- `examples/ag_run_simulations.ipynb`, célula 1: `GLOBAL_POPULATION_SIZE_AG
  = 20` (em vez de 50).
- `examples/experiments_config.json`: adicionar `"POPULATION_SIZE_AG": 20`
  explícito nas 5 entradas de $L_0$ que alimentam o Cap.4 (100, 500, 1.000,
  2.500, 5.000) — assim o valor fica preso ao experimento certo mesmo que o
  global mude de novo no futuro.
- **Nota de proveniência obrigatória junto da edição** (isto não é uma
  correção "restaurando" um valor perdido — é uma **reconstrução**): "o
  valor 20 é inferido do artefato publicado (`individual_id` 0..19 em todas
  as gerações, `examples/ag_optimization_results_L0_*old/`), não recuperado
  de um estado de execução commitado — nenhum commit do notebook contém
  este valor."

Não editei nada — nem o legado (é somente leitura por constituição) nem o
`a2`/`Cap.3` (superfície da tese). Fica a decisão com quem tem a
superfície: aplicar o conserto acima é uma opção; registrar como limitação
permanente de reprodutibilidade é a outra. Recomendo a primeira — o custo é
uma edição de 2 arquivos no repo legado (mesmo sendo "somente leitura" para
mim, não sei se a regra bloqueia esse tipo de correção documental; quem
decide isso também não sou eu).

## Braço E — sem mudança

Ainda em fila de GPU, script retentando sozinho.

## Caixa

Atualizada com esta entrega.
