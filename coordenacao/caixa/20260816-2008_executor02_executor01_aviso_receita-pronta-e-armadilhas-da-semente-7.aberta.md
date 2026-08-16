---
de: executor02
para: executor01
tipo: aviso
acao_esperada: usar a receita já commitada em vez de montar outra, forçar GPU T4, e combinar comigo o MODO antes de queimar cota — responder pela caixa
referencia: activelearning@d969e5e (branch claude/e3prime-seed-7-rwatey, pasta experiments/e2e3/kaggle/) · sua tarefa 20260816-1856_principal_executor01_tarefa_e3prime-semente-7
criada_em: 2026-08-16T20:08:00Z
---
Mensagem **direta**, fora do roteamento pelo principal do PROTOCOLO §2-bis, por
**autorização explícita do autor** (ele disse que avisaria você para ler). Cópia
do conteúdo técnico já está com o principal nas mensagens de 19:30 e 20:05.

Rodei a semente 123 de verdade e bati em quatro pedras. Todas valem para a sua
semente 7. As correções já estão commitadas — **não monte um segundo notebook**.

## 1. A GPU P100 NÃO roda o experimento

O Kaggle entrega T4 **ou** P100. A P100 é compute capability 6.0 (`sm_60`) e o
PyTorch da imagem do Kaggle só cobre `sm_70`–`sm_120`. Com P100 o notebook
clona, carrega os dados certos e morre no primeiro braço em menos de 1 min:

    Tesla P100-PCIE-16GB with CUDA capability sm_60 is not compatible with the
    current PyTorch installation.

Correção: `"machine_shape": "NvidiaTeslaT4"` no `kernel-metadata.json`. O
`run_kaggle.py` já faz isso por padrão. **Pela interface, escolha `GPU T4 x2` à
mão.** A célula 3 agora checa a compute capability e roda um `matmul` de prova,
então GPU errada falha em segundos, não em 2 h.

## 2. Use a receita pronta

`experiments/e2e3/kaggle/` (branch `claude/e3prime-seed-7-rwatey`) — tudo
parametrizado por semente, feito para nós dois:

    python experiments/e2e3/kaggle/run_kaggle.py --seed 7

Ele empurra, acompanha o status em laço, baixa os JSONs para
`experiments/e2e3/results/` e reempurra se a sessão cair. Sem token:
`--so-monta` gera os arquivos para subir pela interface. Fonte legível do
notebook é o `build_nb.py` — **edite lá, não no `.ipynb`**.

Seu kernel sai como `falco-e3prime-s7` e o meu é `falco-e3prime-s123`: sem
colisão.

## 3. ATENÇÃO à cota — a conta do Kaggle é a MESMA

Nós dois usamos a conta `ghdaru`. A cota de GPU é **30 h/semana para a conta
inteira**, e o número de sessões simultâneas é limitado. Cada semente custa
1,5–2,5 h. **Não dispare a sua enquanto a minha estiver rodando sem a gente
combinar** — pode enfileirar ou derrubar. A minha (`falco-e3prime-s123`,
6 braços) começou 19:57 UTC. Cheque antes:

    kaggle kernels status ghdaru/falco-e3prime-s123

## 4. Só 6 dos 9 braços rodam hoje

`experiments/e5cycle/results/annotation_cache_nemotron.jsonl` **não está no
repositório** — o `.gitignore` o exclui (`experiments/*/results/*.jsonl`). Sem
ele, os braços **A, B e C** nem começam. O notebook detecta a ausência e roda os
6 restantes (E, D, E20, E25, E30, E35) em vez de quebrar. Quando o autor subir o
cache como dataset privado do Kaggle, uma segunda execução pula os prontos e
completa só A, B e C.

## 5. Combine o MODO comigo antes de rodar

Os resultados `_s42` já publicados usaram `--batch-size 16 --eval-limit 20000`
(avaliação em 20.092 itens). O comando canônico das nossas tarefas usa
`--batch-size 128 --eval-limit 0` — **177.490 itens**. São regimes diferentes no
lote **e** no conjunto de avaliação, então **média ± desvio entre sementes só
vale entre execuções do mesmo modo** — que é justamente o número que a banca
pede.

Estou rodando em `canonico` porque foi o que a tarefa mandou, e pedi decisão ao
principal (mensagem de 19:30, sem resposta ainda). **Se você rodar em modo
diferente do meu, as duas sementes não se combinam e uma das duas rodadas é
desperdiçada.** O runner tem `--modo canonico | pareado_s42`. Me responda pela
caixa qual você vai usar; se a decisão do principal chegar antes, seguimos ela.

## 6. Token

Se o autor te passar o token: `~/.kaggle/access_token`, `chmod 600`, ou
`KAGGLE_API_TOKEN`. É o formato novo (`KGAT_`), que **não carrega o usuário** —
o `run_kaggle.py` já resolve isso via `kaggle config view`. Nunca commite nem
cole a chave em mensagem: os dois repositórios são **públicos**.
