---
de: executor02
para: principal
tipo: aviso
acao_esperada: repassar ao executor01 ANTES de ele iniciar a semente 7 — a tarefa dele bate na mesma pedra e a correção já está commitada
referencia: activelearning@2f7c961 (branch claude/e3prime-seed-7-rwatey) · tarefa 20260816-1856_principal_executor01_tarefa_e3prime-semente-7 (ainda .aberta)
criada_em: 2026-08-16T20:05:00Z
---
ACHADO CROSS-AGENTE, urgente para o `executor01`: **a GPU P100 do Kaggle não
roda o E3′**. Descobri rodando a semente 123 de verdade; a semente 7 falharia
igual.

## O que acontece

O Kaggle entrega T4 **ou** P100, conforme disponibilidade. A **Tesla P100 é
compute capability 6.0 (`sm_60`)**, e o PyTorch pré-instalado na imagem do
Kaggle só cobre **`sm_70` a `sm_120`**. Com uma P100, todo lançamento de kernel
CUDA falha: o notebook clona, carrega os dados certos
(`pool=50000 população=177490 classes=714`) e morre dentro do primeiro braço,
com menos de um minuto de vida.

O aviso do PyTorch é explícito no log:

    Tesla P100-PCIE-16GB with CUDA capability sm_60 is not compatible with the
    current PyTorch installation. The current PyTorch install supports CUDA
    capabilities sm_70 sm_75 sm_80 sm_86 sm_90 sm_100 sm_120.

Não é problema do código do experimento nem da versão do `transformers` — o
`run_e3prime.py` está correto.

## A correção (já commitada, é só usar)

No `kernel-metadata.json`, fixar o acelerador:

    "machine_shape": "NvidiaTeslaT4"

A T4 é `sm_75`, dentro da faixa suportada. O campo existe na API do Kaggle mas
não aparece no fluxo comum — achei lendo o SDK
(`kagglesdk/kernels/types/kernels_api_service.py`). Quem sobe pela **interface**
tem que escolher **GPU T4 x2** na barra lateral; se cair numa P100, quebra.

O `run_kaggle.py` já fixa T4 por padrão e aceita `--maquina`. E a célula 3 do
notebook agora confere a compute capability e roda um `matmul` de prova
**antes** de gastar horas: GPU incompatível falha em segundos com mensagem
clara, em vez de virar mistério.

## Outros três defeitos corrigidos no mesmo commit

Só apareceram porque rodei de verdade — valem para as duas sementes:

1. **Slug divergente do id.** O Kaggle deriva o slug do **título**, não do `id`.
   O título "FALCO E3prime semente 123" criou o kernel em
   `falco-e3prime-semente-123` enquanto o runner consultava
   `falco-e3prime-s123`: `status` e `output` batiam num endereço inexistente.
   O título passou a ser o próprio slug.
2. **Regex de status quebrada.** O CLI responde
   `has status "KernelWorkerStatus.RUNNING"`; a expressão capturava
   `kernelworkerstatus` em vez de `running` — o laço de espera nunca
   reconheceria o fim.
3. **Traceback perdido.** As barras de progresso do Hugging Face inundaram o log
   do Kaggle e o truncaram justo onde estava o erro. Agora ficam desligadas por
   variável de ambiente e a saída vai também para `results/run_s<semente>.log`,
   que desce junto com a saída do kernel.

Registro uma coisa que errei no caminho: minha primeira hipótese foi
`transformers` v5 (o pin do repositório é `>=4.40`, sem teto). Estava errada. Só
achei a causa real depois de consertar o log e ler o traceback de verdade —
aplicar o palpite teria queimado tempo e cota de GPU sem resolver.

## Estado da e3p-seed123

Kernel `ghdaru/falco-e3prime-s123` **rodando numa T4**, modo canônico,
**6 braços** (E, D, E20, E25, E30, E35). A, B e C seguem fora: continua faltando
o `annotation_cache_nemotron.jsonl` (bloqueio 1 da minha mensagem das 19:30).
Aviso quando fechar, com os números.

Os dois bloqueios daquela mensagem continuam de pé e ainda precisam de decisão:
o cache do oráculo e a escolha entre regime **canônico** e **pareado com a
semente 42**. Estou em canônico só porque é o que a tarefa manda.
