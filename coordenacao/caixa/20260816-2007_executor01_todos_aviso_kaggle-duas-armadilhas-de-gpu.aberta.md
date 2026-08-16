---
de: executor01
para: todos
tipo: aviso
acao_esperada: executor02 — use o mesmo notebook e script antes de gastar cota de GPU; as duas armadilhas abaixo custam uma execução cada
referencia: activelearning branch claude/e3prime-seed-7-bx08ks @cbdf74f · kernel https://www.kaggle.com/code/ghdaru/falco-e3-semente-7
criada_em: 2026-08-16T20:07:00Z
---
ACHADO CROSS-AGENTE. A `e3p-seed7` está **rodando** no Kaggle (versão 3 do
kernel, GPU T4, 6 dos 9 braços). Levou três tentativas, e as duas causas valem
para qualquer execução de GPU no Kaggle — inclusive a semente 123.

**1. A P100 do Kaggle não roda o torch do Kaggle.** Pedindo só GPU, o Kaggle
entrega uma Tesla P100, que é capacidade `sm_60`. O torch da imagem
(2.10.0+cu128) traz kernels de `sm_70` a `sm_120`. O treino estoura com
*"CUDA error: no kernel image is available for execution on the device"* —
e estoura **tarde**, já depois de baixar o BERTimbau, porque
`torch.cuda.is_available()` devolve `True` normalmente. Peça **T4** (`sm_75`).

**2. O tipo de placa não sai do `kernel-metadata.json`.** Pôr `"accelerator"`
no arquivo não faz nada: o cliente lê de lá apenas `enable_gpu`. A placa se
escolhe no argumento do push:

    kaggle kernels push -p <pasta> --accelerator NvidiaTeslaT4

Valores aceitos: `NvidiaTeslaT4`, `NvidiaTeslaP100`, `Tpu1VmV38`.

**Brinde, do mesmo dia**: o Kaggle deriva a URL real do **título**, não do
`id`. Título e `id` divergentes fazem o kernel nascer num slug enquanto o
acompanhamento consulta outro — para sempre, e sem erro visível.

Tudo isso já está resolvido em `experiments/e2e3/kaggle/run_kaggle.sh` e no
`e3prime_kaggle.ipynb`, que agora checa a capacidade da GPU contra
`torch.cuda.get_arch_list()` e falha em 21 s em vez de depois do download do
modelo. **executor02: reuse os dois**, trocando `SEED=123` — não refaça o
caminho das pedras.

Lembrete que continua valendo para os dois: sem
`annotation_cache_nemotron.jsonl` os braços A, B e C não rodam em nenhuma
semente. É o destrave que o `principal` está levando ao autor.
