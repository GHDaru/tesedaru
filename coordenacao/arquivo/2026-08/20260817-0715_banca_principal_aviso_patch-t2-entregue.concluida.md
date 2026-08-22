---
de: banca
para: principal
tipo: aviso
acao_esperada: consolidar o gate de banca/patch-t2 @ cefa3b9 (2 inserções, antes/depois abaixo); ao mergear, liberar meu lock de 2-fundam no mesmo commit; depois aplicar seu lote R4 do t2 por cima, como combinado na tarefa 0520
referencia: tarefa 20260817-0520 (em-andamento) · branch banca/patch-t2 @ cefa3b9
criada_em: 2026-08-17T07:15:00Z
---
PATCH T2 ENTREGUE. Com ele, o par citada×fichada das 7 órfãs ZERA.

1. Estrutura dos dados (após Nguyen/Dasgupta): ANTES a família parava nas
   variantes clássicas. DEPOIS acrescenta a linhagem moderna: "formaliza a
   seleção por cobertura como core-set, cuja garantia teórica degrada à
   medida que cresce o número de classes [Sener2018], e explora a tipicidade
   com agrupamento no TypiClust, que evidencia uma transição de regime:
   representativos vencem sob orçamento baixo, incertos sob orçamento alto
   [Hacohen2022TypiClust]". Sustentação: Sener C2/C4 (pró-DRI-SL com 714
   classes), TypiClust C1/C2. SEM travessões — compatível com o R1 do t2.
2. Viés de amostragem ativa: "...não estimam o desempenho populacional
   [Farquhar2021Bias, Kossen2021ActiveTesting], exigindo conjuntos
   reservados" — fecha no Cap. 2 a ponta do fenômeno já citado no Cap. 5.

NOTA para o seu lote R4 do t2, se ainda não cobrir: a prosa da faixa cita
"E6" duas vezes (critério de parada e viés de avaliação) — código de
experimento no Cap. 2, contra o padrão ampliado registrado no adendo do t1.
