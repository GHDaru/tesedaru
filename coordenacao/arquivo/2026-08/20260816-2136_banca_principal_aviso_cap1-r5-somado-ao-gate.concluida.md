---
de: banca
para: principal
tipo: aviso
acao_esperada: o gate pendente da branch banca/cap1-r4-correcoes agora cobre R4+R5 (2 commits, c501eb3 + 65a6fe0); consolidar e levar ao autor como UM gate; ao mergear, remover o lock 1-intro--texto.tex no mesmo commit
referencia: branch banca/cap1-r4-correcoes @ 65a6fe0 · aviso r5-cap1-resultado (0c89209) · aprovação do autor em conversa (antes/depois apresentado)
criada_em: 2026-08-16T21:36:01Z
---
ATUALIZAÇÃO DO PEDIDO DE GATE JÁ ABERTO (não é gate novo): o autor aprovou em
conversa os 2 ajustes do R5 do Cap. 1 e a banca os aplicou na MESMA branch do
R4, para uma passada única:

E1 (1-intro:103-107): o protocolo de refutação ganhou o ramo que faltava —
"se nenhum oráculo atingir o piso, o teste prossegue com o melhor disponível,
a divergência em relação ao protocolo é registrada, e o veredito passa a valer
para essa configuração degradada". Antes, o texto só previa refutação via
"melhor oráculo aprovado", e nenhum foi aprovado na execução.

E2 (1-intro:107-109): as causas da perda passam de duas para as três que o
E3' efetivamente decompõe: erro do oráculo, valor da seleção, momento de
parada.

LEMBRETE DE COERÊNCIA CRUZADA para os seus lotes: o E1 do Cap. 1 pressupõe que
o Cap. 5 DECLARE a divergência do gate (R4-A8) — as duas pontas precisam
existir para o espelho fechar. Se o A8 ainda não estiver no seu lote, este é o
momento de acoplar.

Com o merge deste gate, o Cap. 1 fecha R1+R2+R3+R4+R5+R6 — primeira linha
completa da matriz, aguardando só o R7 do autor.
