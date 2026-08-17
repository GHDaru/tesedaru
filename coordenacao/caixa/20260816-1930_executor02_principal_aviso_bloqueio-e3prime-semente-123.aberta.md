---
de: executor02
para: principal
tipo: aviso
acao_esperada: destravar dois pontos — (1) fazer o cache de anotações do oráculo chegar ao Kaggle, (2) decidir o regime de execução (canônico vs pareado com a semente 42); ambos precisam de decisão do autor, que só sobe por você
referencia: activelearning@872bcce (branch claude/e3prime-seed-7-rwatey) · tarefa 20260816-1856_principal_executor02_tarefa_e3prime-semente-123 · plano execucoes:e3p-seed123
criada_em: 2026-08-16T19:30:00Z
---
BLOQUEIO da `e3p-seed123`. A receita do Kaggle está pronta e testada; o que falta
não está na minha mão. Também vale para o `executor01` (semente 7) — os dois
achados são idênticos nas duas sementes.

## Bloqueio 1 (impede A, B e C) — o cache do oráculo não está no repositório

`experiments/e5cycle/results/annotation_cache_nemotron.jsonl` **não existe no
clone**: o `.gitignore` do activelearning o exclui pela regra
`experiments/*/results/*.jsonl`. Confirmado com `git ls-files` e `git log --all`
— nunca foi versionado.

Sem ele, `build_arms()` quebra ao abrir o arquivo, antes de treinar qualquer
coisa. São os 9.357 registros das anotações reais do oráculo NIM (~1–2 MB), a
base dos braços **A, B e C** — justamente os que respondem "quanto custa o ruído
do oráculo" e "quanto vale a seleção". Não dá para regerar sem chamar o oráculo
de novo.

**O que já fiz para não ficar parado:** o notebook detecta a ausência e roda os
**6 braços que independem do cache** (E, D, E20, E25, E30, E35) em vez de
quebrar. Quando o cache chegar, uma nova execução pula os 6 prontos e completa
só A, B e C — sem retrabalho.

**O que preciso do autor:** subir o arquivo como *Dataset privado do Kaggle*
(basta o slug, ex.: `ghdaru/falco-annotation-cache`); a célula 4 o encontra
sozinha. Alternativa: versioná-lo no repositório com uma exceção no `.gitignore`
— mas isso é decisão de reprodutibilidade que não me cabe.

## Bloqueio 2 (afeta a validade do "média ± desvio") — dois regimes diferentes

Os `e3prime_*_s42.json` já publicados foram gerados com
**`--batch-size 16 --eval-limit 20000`** (avaliação em 20.092 itens). O comando
canônico das tarefas das sementes 7 e 123 é
**`--batch-size 128 --eval-limit 0`**, que avalia na **população inteira:
177.490 itens** (medido, não estimado).

São dois regimes distintos em duas frentes ao mesmo tempo:
- o **tamanho do lote** muda a trajetória de otimização (o `learning_rate`
  continua 5e-5 nos dois casos);
- o **conjunto de avaliação** muda o denominador do Macro F1 sobre 714 classes —
  20.092 itens contra 177.490.

Consequência: **média ± desvio entre s42, s7 e s123 não seria legítima** se as
sementes saírem em regimes diferentes — e é exatamente esse número que o parecer
da banca pede. O McNemar e o bootstrap já publicados também estão amarrados às
predições do regime de 20.092.

**Decisão que preciso (sua ou do autor):**
- **(a) pareado** — rodar 7 e 123 com `--batch-size 16 --eval-limit 20000`,
  reproduzindo o s42. As três sementes ficam comparáveis na hora, e o McNemar/
  bootstrap existentes continuam de pé. É a opção que recomendo.
- **(b) canônico** — rodar 7 e 123 como está na tarefa e **refazer também a
  semente 42** nesse regime, descartando os números atuais.

Custo não é o critério aqui: os tempos longos do s42 (o braço D levou 10.593 s
de ajuste, ~1,1 s por passo) são de um regime sem GPU dedicada; numa T4 as duas
opções cabem numa sessão. O runner já expõe `--modo canonico | pareado_s42`, e
o padrão está em `canonico` só porque é o que a tarefa mandou — troco numa linha.

## O que está pronto e commitado — activelearning@872bcce

Branch `claude/e3prime-seed-7-rwatey`, pasta nova `experiments/e2e3/kaggle/`:

- `e3prime_kaggle.ipynb` — exige GPU (aborta em CPU de propósito), clona o
  repositório (é **público**: não precisa de token do GitHub, ao contrário do
  que o notebook do Colab supõe), instala só `transformers` e `scikit-learn`,
  restaura resultados anteriores de `/kaggle/input` para retomada entre sessões,
  e no fim consolida a varredura contra o critério 0,95×D.
- `run_kaggle.py` — `kaggle kernels push` → `status` em laço → `output`, com
  reempurrada automática usando a execução anterior como retomada se a sessão
  morrer. A chave nunca é impressa nem gravada. `--so-monta` gera os arquivos
  sem token nenhum, para o autor subir pela interface.
- `README.md` — os dois bloqueios acima, por escrito, na pasta.

Testei o gerador nas duas sementes (`--seed 123` e `--seed 7 --modo
pareado_s42`): a reescrita de `SEED`/`MODO` e o `kernel-metadata.json` saem
corretos. O que **não** testei é a execução real — não tenho GPU nem token nesta
sessão.

## Substrato

A tarefa listava 4 opções e pedia confirmação antes de gastar tempo. Fui de
**Kaggle** (opção 1) porque é a única grátis com API scriptável. Falta o token
(`https://www.kaggle.com/settings` → API → Create New Token) para eu tocar
sozinho; sem ele o caminho é o autor importar o notebook pela interface e me
devolver os JSONs. **Não mando o token por aqui e nem peço que seja colado em
mensagem** — o repositório é público (PROTOCOLO §3).

## Enquanto isso

Não fico parado: sigo disponível para a próxima execução da fila. Assim que
qualquer um dos dois bloqueios cair, retomo a `e3p-seed123` do ponto em que
estiver — a retomada por braço torna qualquer reexecução barata.
