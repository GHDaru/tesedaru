---
de: principal
para: local
tipo: tarefa
referencia: 3-metodo/texto.tex §3.10 (l.~901) e 6-conclusao §6.4 item 2 · auditoria do autor
acao_esperada: levantar, SOMENTE LENDO artefatos/metadados (sem reexecutar nada), o mapeamento execução->ambiente; recibo com tabela e evidência por linha
prazo: bloqueia uma correção do §3.10 na auditoria do autor
---

# Configurações de ambiente por experimento (pedido do autor)

Na auditoria do Cap.3, o autor perguntou se tivemos diversos ambientes de
execução e pediu as configurações. O §3.10 declara só "estação com GPU NVIDIA
RTX 3090 (24 GB), 64 GB de RAM e Linux"; o §6.4 (item 2) fala em "semente
única e CPU" para a validação do classificador forte; e o registro de
coordenação mostra kernels Kaggle (GPU T4) nas reexecuções multi-semente do
regime `_bs16v2`. Precisamos do quadro completo, com evidência.

## O que levantar (leitura de artefatos/metadados apenas — congelamento vige:
nada de reexecutar)

Para cada família de resultados IMPRESSOS na tese, o ambiente que os produziu
e a evidência (campo do artefato, metadado do JSON, log, cronologia do git):

1. Braços A-E do regime `_bs16v2` (sementes 7, 42, 123) — activelearning
   `experiments/e2e3/results/` (e a branch `rwatey`): estação local? Kaggle
   T4? Que campos de ambiente os JSONs gravam (GPU, hostname, versões)?
2. Varredura de orçamento (E20/E25/E30/E35) — mesmo levantamento.
3. Corrida ORIGINAL da validação do forte (a que o §6.4 chama de "semente
   única e CPU") — isso é verdadeiro? Onde rodou?
4. E1/E6 (classificadores leves) — CPU de qual máquina?
5. Pilares 1-2 no repo legado activetextclassification (sensibilidade L0,
   AG, DRI-SL) — ambiente da época, se recuperável.
6. Oráculos (E0/E0-P): chamadas de API — só confirmar que o ambiente local é
   irrelevante ao resultado (rede), se for o caso.

## Entrega

Recibo de 1 linha ao principal + tabela em arquivo na sua branch
(`ambiente | experimentos | evidência (caminho@sha:campo)`), para o
principal redigir a versão final do §3.10 com o autor e conferir a coerência
do §6.4. Se algum item não tiver evidência recuperável, diga "sem evidência"
em vez de inferir.
