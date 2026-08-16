---
de: executor01
para: principal
tipo: aviso
acao_esperada: destravar os três pontos abaixo (pedir ao autor o cache do oráculo, o token do Kaggle, e decidir a questão dos hiperparâmetros); com o cache e o token eu disparo sozinho
referencia: tarefa 20260816-1856_principal_executor01_tarefa_e3prime-semente-7 · activelearning branch claude/e3prime-seed-7-bx08ks commit 661eb6a · plano execucoes.e3p-seed7 (versao 12)
criada_em: 2026-08-16T19:35:00Z
---
BLOQUEIO da `e3p-seed7`: o comando canônico não roda hoje. Três impedimentos,
em ordem de gravidade. Não fiquei parado — notebook do Kaggle e automação já
prontos e testados (fim da mensagem).

## 1. O cache de anotações do oráculo não está no repositório (grave)

A tarefa diz que o repositório "já traz o cache de anotações do oráculo". Não
traz. Verifiquei:

- `experiments/e5cycle/results/annotation_cache_nemotron.jsonl` não existe no clone;
- `git log --all -- <esse caminho>` volta vazio: **nunca foi commitado**;
- a causa é a linha 7 do `.gitignore` (`experiments/*/results/*.jsonl`), que
  casa exatamente com esse caminho.

Consequência: os braços **A, B e C não rodam a partir de um clone** — o
`run_e3prime.py` lê esse arquivo para saber quais itens o pipeline anotou (A),
os mesmos itens com rótulo gold (B) e quantos sortear (C). Sem eles a semente 7
não produz A−B (custo do ruído do oráculo) nem B−C (valor da seleção), que são
as comparações que a banca quer ver repetidas. Sobram 6 braços: D e a varredura
E/E20/E25/E30/E35.

**Quem destrava**: o autor — o arquivo está na máquina onde o ciclo E5 rodou.
(a) commitar o cache com `git add -f` (~9.357 linhas, arquivo pequeno; resolve
    também a reprodutibilidade: hoje o E3′ não é reproduzível por terceiros);
(b) ou subir como Kaggle Dataset privado — o notebook já o procura sozinho em
    `/kaggle/input`.

## 2. Sem token do Kaggle e sem GPU nesta sessão

Minha sessão não tem GPU (`nvidia-smi` ausente, `torch` não instalado) nem
credenciais do Kaggle. CPU está fora de questão: nove ajustes finos completos.

**Quem destrava**: o autor, com o token da API do Kaggle numa sessão minha
(`~/.kaggle/kaggle.json` ou `KAGGLE_USERNAME`/`KAGGLE_KEY`) — aí o
`run_kaggle.sh` faz tudo sem navegador. Sem ele, o autor roda pela interface e
me manda os JSONs.

## 3. A linha de base da semente 42 usa hiperparâmetros diferentes (decisão sua)

Este achado muda o desenho, não só a logística. Os nove `e3prime_*_s42.json`
que estão na main foram gerados com `--batch-size 16 --eval-limit 20000`
(avaliação em 20.092 instâncias), e **não** com o comando canônico
`--batch-size 128 --eval-limit 0` (população inteira).

Comparar s42 com s7 exige que só a semente mude. Do jeito que está mudariam
três coisas ao mesmo tempo — semente, tamanho de lote e conjunto de avaliação —
e a diferença observada não seria atribuível à semente, que é a pergunta da
banca. Duas opções:

- **(A) casar com a base existente**: s7 com `--batch-size 16 --eval-limit
  20000`. Nada a refazer, mas herda o lote 16 (os tempos da s42 somam ~11,7 h).
- **(B) adotar o canônico**: s7 e s123 com lote 128 e população inteira, e
  **refazer a s42** igual. Uma execução extra, mas dá três sementes homogêneas
  e avaliação sobre a população toda — mais defensável no Cap. 5.

Recomendo a **(B)** e o notebook já está no canônico, mas a decisão é sua: mexe
em números já citados no texto, e o McNemar e o bootstrap da s42 teriam de ser
recalculados sobre as novas predições.

## O que já está entregue (branch `claude/e3prime-seed-7-bx08ks`, commit 661eb6a)

- `experiments/e2e3/e3prime_kaggle.ipynb` — o Colab adaptado ao Kaggle: GPU
  P100/T4, internet ligada, `GITHUB_TOKEN` lido dos Kaggle Secrets e nunca
  impresso, instalação só de `transformers` e `scikit-learn`, log em tempo real.
  Faltando o cache, **avisa alto e roda os 6 braços possíveis** em vez de estourar.
- `experiments/e2e3/kaggle/run_kaggle.sh` + `kernel-metadata.json` — o passo 3 da
  tarefa: empurra, acompanha, baixa o output, commita os parciais na branch e
  reempurra; queda de sessão vira só mais uma rodada (o runner pula braço pronto).
  Para após duas rodadas sem progresso, para não queimar cota de GPU. Nenhuma
  credencial entra no repositório.

Verifiquei sem GPU o que dá: sintaxe das células e do shell, a injeção de
branch/semente, e a execução real das células de seleção de braços e retomada
(sem o cache caem corretamente para E,D,E20,E25,E30,E35). O treino em si é o
que **não** foi verificado — depende do destrave.

## Estado no plano

Marquei `execucoes.e3p-seed7` como `aguardando_inicio` com um campo `bloqueio`,
e **não** como `rodando`: nada está rodando, e "rodando" faria o painel mentir
sobre os ~230 pontos que esta execução destrava. Passo para `rodando` quando o
primeiro braço entrar na GPU.

**Cross-agente**: o `executor02` (semente 123) vai bater nos itens 1 e 2 do
mesmo jeito; o destrave serve para os dois e o notebook roda a 123 trocando uma
variável.
