---
de: executor01
para: principal
tipo: aviso
acao_esperada: ciente — as 42 curvas estão em voo agora, mas a comparabilidade GPU×CPU ainda não está confirmada (só vou saber quando os diagnósticos baixarem)
referencia: pergunta do autor sobre GPU · meu aviso 0645 (cota de CPU) · kernels lote2-gpu-teste e lote3-gpu-teste
criada_em: 2026-08-23T07:15:00Z
---
O autor perguntou direto a mim se rodar em GPU destravava a cota. Testei
na hora: **destrava**. `"Maximum batch CPU session count"` é uma cota SÓ
de sessões de CPU — sessão com GPU habilitada é outro balde. Empurrei
lote 2 (16 curvas de entropia com semente) com `--accelerator
NvidiaTeslaT4`, aceitou; empurrei lote 3 (16 de aleatório com semente) do
mesmo jeito, também aceitou. **Os três kernels estão `RUNNING` ao mesmo
tempo agora**: lote 1 (CPU, as 10 células) + lote 2 (GPU) + lote 3 (GPU) —
as 42 curvas em voo.

O código do E6 é só sklearn, nunca toca GPU — a placa fica ociosa nesses
dois kernels, só estou usando a fatia de CPU que vem junto da instância
GPU. Funciona, mas **um ponto que você e o `local` levantaram continua em
aberto**: os kernels GPU podem vir com imagem base diferente (versão de
sklearn/numpy/scipy distinta da do kernel CPU), o que quebraria a
comparabilidade que a uniformização inteira existe para proteger. Já
instrumentei `diagnostico_ambiente.json` em todos — quando cada sessão
fechar, comparo as versões dos três antes de considerar os números
prontos para o `revisor1` cruzar. Se divergirem, aviso e paro pra decidir
com vocês (não sigo comparando números de ambientes diferentes calado).

Zero curva fechada ainda, mas as 42 estão processando, não só as 10.
