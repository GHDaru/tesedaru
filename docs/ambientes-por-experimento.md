# Ambientes por experimento

Levantamento pedido pelo principal na tarefa
`coordenacao/caixa/20260824-0226_principal_local_tarefa_configuracoes-de-ambiente-por-experimento.aberta.md`
(`origin/mensageria`@f66b62c), para o principal redigir a versão final do 3.10 com o
autor e conferir a coerência do 6.4.

Duas regras que segui, e que mudam como esta tabela deve ser lida:

1. Só leitura de artefato e de metadado. Nada foi reexecutado, nem localmente nem no
   Kaggle. O congelamento vige.
2. Onde o registro não existe, a linha diz "sem evidência" em vez de inferir. Onde há
   indício indireto, por exemplo tempo de execução, ele aparece rotulado como indício e
   fica separado da evidência direta.

Hashes usados nas citações:

| repositório | referência | sha |
|---|---|---|
| `activelearning` | `origin/main` | cd6e1c0 |
| `activelearning` | branch `claude/e3prime-seed-7-rwatey` | e88c20c |
| `tesedaru` | `origin/main` | be82f10 |
| `tesedaru` | `origin/mensageria` | f66b62c |
| legado `activetextclassification` | HEAD do clone local | 26d7c4e |

Caminho sem prefixo de repositório é do `activelearning`.

## A tabela

| ambiente | experimentos | evidência (caminho@sha:campo) |
|---|---|---|
| CPU do sandbox de sessão Claude Code, 4 vCPU, sem GPU. Julho de 2026 | E3' original: braços A, B, C, D, E e a varredura E20/E25/E30/E35. Semente 42 única, lote 16, avaliação limitada a 20.092 itens | `experiments/e2e3/results/e3prime_cpu.log@71d12aa`: o próprio nome do arquivo, e todos os blocos com `"batch_size": 16, "seed": 42, "eval_limit": 20000, "eval_n": 20092` · `experiments/e2e3/run_e3prime.py@13ff0d1`: docstring, linha `CPU : ... --batch-size 16 --eval-limit 20000 --seed 42` · `experiments/e2e3/results/smoke_cpu.json@6b809cd`: `"device": "cpu"` · `docs/e2e3-docker.md@6b809cd`: "medido no sandbox (4 vCPU)" |
| mesma CPU do sandbox, 4 núcleos. Julho e agosto de 2026 | E1 e E4 (varreduras PVBin com oráculo simulado), E5, E6 (curva populacional) | `experiments/e1e4/run_sweeps.py@392392d`: as dependências são scikit-learn e numpy, sem torch e sem rede · `tesedaru` `coordenacao/arquivo/2026-08/20260817-2300_executor02_...@5294a2a`: "E6 usa PVBin e SGD (scikit-learn), roda em CPU" e "CPU deste ambiente ... Paralelizando nos ~4 núcleos" · `experiments/e6population/.../summary@2baf96a`: `wall_seconds` |
| Kaggle, GPU Tesla T4, sessão de notebook. Agosto de 2026 | E3' canônico: braços A a E e varredura, lote 128, avaliação na população inteira (177.490 itens), sementes 7, 42 e 123 | `experiments/e2e3/kaggle/kernel-metadata.json@eff23f2`: `"enable_gpu": true`, `"machine_shape": "NvidiaTeslaT4"` · `experiments/e2e3/kaggle/run_kaggle.sh@eff23f2:ACELERADOR` (linha 38) · `tesedaru` `coordenacao/arquivo/2026-08/20260816-2118_executor02_...@a3a2e56`: "Kernel `ghdaru/falco-e3prime-s123`, GPU T4, 75 min" e "`ghdaru/falco-e3prime-s42` rodando agora numa T4 (~1,3 h)" |
| GPU, máquina não nomeada em registro nenhum | os 25 braços `_bs16v2` de 22/08/2026, lote 16 com avaliação na população inteira, três sementes. É o regime que a tese imprime hoje | sem evidência direta. Indício: `experiments/e2e3/results/e3prime_D_s42_bs16v2.json@e88c20c:fit_seconds` = 1199,2 contra `experiments/e2e3/results/e3prime_cpu.log@71d12aa` braço D `fit_seconds` = 10593,3, mesmo lote e mesmo modelo, fator 8,8. Commits 9132b1d, e51f4fe e 6609df0, nenhum nomeia ambiente |
| Kaggle, CPU. Agosto de 2026 | notebooks de auditoria `falco-auditoria-escala-populacional` e `falco-auditoria-classificador-forte`. Reproduzem resultado já obtido, não produzem resultado novo | `tesedaru` `coordenacao/arquivo/2026-08/20260817-0330_executor01_...@a3a2e56`: "rodando lá, com resultado idêntico ao local ... (CPU, não gastam cota de GPU)" |
| Jupyter local, Python 3.11.0, sem nenhuma dependência de GPU declarada. 2025 | pilares 1 e 2 do legado: sensibilidade a L0, AG, DRI-SL | legado `pyproject.toml@26d7c4e:dependencies` = numpy, pandas, scikit-learn, scipy, unidecode, matplotlib, seaborn, tqdm, sem torch · metadados dos 18 notebooks: `kernelspec.name` = `python3`, `language_info.version` = `3.11.0`, sem chave `colab`, `accelerator` = `None`. Máquina física: sem evidência |
| API remota. Ambiente local irrelevante, só a rede importa | E0 e E0-P (oráculos) | `experiments/e0/config.json` e `experiments/e0/config_full_nvidia.json@26cd1b9`: os campos são `provider`, `model`, `mode`, `items_per_call`, `requests_per_minute`, nenhum campo de compute local · `experiments/e0/results/rand/*.jsonl:oracle_id`, por exemplo `nvidia-nim:nvidia/nemotron-3-ultra-550b-a55b@T0.0#prompt@b10` · `experiments/e0/nvidia_run.log@a3b836f` |
| RTX 3090 | nenhum | sem evidência. Toda menção a 3090 no repositório é plano ou estimativa, nunca registro de corrida: `docs/bertimbau-local-passo-a-passo.md@6b809cd` (linhas 1, 11, 23, 32, 65, 80, 81, 84 e 106, todas "estimado" ou "esperado"), `docs/e2e3-docker.md@6b809cd:12,30,46,77`, `docs/plano-mestre.md:100` ("confirmar disponibilidade da RTX 3090; senão,"), `src/activelearning/adapters/classifiers/bertimbau.py:4` ("Desenhado para a estação com GPU") |

## Por que nenhum JSON de braço responde sozinho

Vale saber disso antes de procurar: os artefatos do E3' não têm campo de ambiente, e
isso não é descuido de uma corrida, é do código. O dicionário que o `run_e3prime.py`
serializa está em `experiments/e2e3/run_e3prime.py@13ff0d1:225-235` e carrega
exatamente estes campos:

```
arm, n_train, n_train_classes, epochs, batch_size, max_length, seed, data_seed,
eval_n, eval_limit, accuracy, accuracy_wilson95, macro_f1, fit_seconds, predict_seconds
```

Não há `device`, nem `gpu`, nem hostname, nem versão de biblioteca. Um `grep` por
`device|cuda|cpu|gpu|tesla|nvidia` em `e3prime_cpu.log@71d12aa` e em `e3prime_s7.log`
não devolve nada. O único artefato da árvore de resultados que carrega `device` é o
`smoke_cpu.json@6b809cd`, que é o teste de fumaça, não um braço.

A consequência prática para quem redigir o 3.10: o ambiente de cada corrida só pode ser
declarado por fora do artefato, pela receita commitada e pela mensagem de coordenação.
As duas únicas grandezas do próprio artefato que falam de máquina são `fit_seconds` e
`predict_seconds`.

## Item 3: a frase "semente única e CPU" do 6.4

A resposta tem dois lados, e por isso ela não se resolve trocando uma palavra.

Era verdade da corrida ORIGINAL. A validação com o classificador forte de julho de 2026
rodou mesmo com semente 42 única, lote 16, avaliação limitada a 20.092 itens, em CPU. A
cadeia de prova está na primeira linha da tabela, e o elo mais forte dela não é o nome
do arquivo: é o `fit_seconds` do braço D, 10593,3 segundos, contra 1199,2 segundos do
mesmo braço no mesmo lote 16 no regime `_bs16v2`. Fator 8,8 com modelo igual e lote
igual é a assinatura de CPU contra GPU.

Não é verdade do que a tese imprime hoje. O regime `_bs16v2` tem três sementes (7, 42 e
123) e rodou em GPU. Ver
`experiments/e2e3/results/legacy_s42_bs16_eval20k/README.md@a176748`, que documenta a
separação dos regimes e avisa "Não misture".

E o 3.10 está errado na direção oposta. Nenhum artefato registra corrida em RTX 3090,
como mostra a última linha da tabela. Se o 3.10 declara 3090 como ambiente de
treinamento, ele declara uma máquina que nenhum resultado do repositório atesta.

## O que sustenta, e o que não sustenta, a atribuição de GPU aos `_bs16v2`

Não sustenta: nenhum registro nomeia kernel, conta ou acelerador para essas 25 corridas.
Varri a caixa de 21 e 22 de agosto por `T4`, `GPU`, `kernel` e `cota` e não achei
mensagem de execução delas. Os três commits (9132b1d com 9 braços da semente 7, e51f4fe
com 8 da 42, 6609df0 com 8 da 123, todos de 22/08/2026, todos com a mensagem "regerados
com gradient clipping") também não dizem onde rodaram.

Sustenta, como indício: além do fator 8,8 já citado, o `predict_seconds` sobre o mesmo
conjunto de avaliação de 177.490 itens se agrupa por semente, não aleatoriamente.
Semente 123 fica entre 300,4 e 300,9 segundos, semente 7 entre 308,9 e 311,0, semente 42
entre 323,6 e 324,5. São três patamares estreitos e separados, que é o que se espera de
três sessões distintas de máquina, cada uma com seus braços rodando em sequência.

Ou seja: dá para dizer com segurança "GPU", e dá para dizer "três sessões". Dizer "T4 do
Kaggle" já é inferência a partir da receita commitada, e por isso fica marcado como sem
evidência direta.

## Três armadilhas para quem for redigir

A primeira é o `docs/records/resultados.json@655606d`, que dá link de `notebook_kaggle`
para E3 e para E6. Lido rápido, isso diz "E3 e E6 rodaram no Kaggle". Está certo para o
E3 e errado para o E6: os dois notebooks do E6 são de auditoria em CPU, reproduzem o
resultado local e não gastam cota de GPU, conforme o executor01 em
`20260817-0330...@a3a2e56`.

A segunda são os três regimes do E3', que não podem ser somados nem comparados entre si:
o original (lote 16, avaliação 20.092, semente 42, CPU), o canônico (lote 128, população
inteira, três sementes, T4) e o homogêneo `_bs16v2` (lote 16, população inteira, três
sementes). Na semente 123, o E35 canônico dá Macro F1 0,3461 e o original dá 0,4627. O
README do diretório legado registra o motivo da separação: a média com desvio pedida
pela banca só é legítima entre corridas do mesmo regime.

A terceira é o legado. A coordenação cita `activetextclassification@b540533`, mas o
clone local está em 26d7c4e (01/06/2025, 19 commits, o mais antigo de 12/05/2025) e não
contém aquele commit. As afirmações desta tabela sobre o legado valem para 26d7c4e.

## Onde não há evidência

- máquina, kernel ou conta das 25 corridas `_bs16v2` de 22/08/2026
- máquina física onde rodaram os notebooks dos pilares 1 e 2 do legado
- qualquer corrida em RTX 3090
- versões de biblioteca (torch, transformers, CUDA) de qualquer corrida do E3', porque
  nenhum artefato as registra
- conta Google usada no Colab, questão que segue aberta de antes
