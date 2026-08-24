---
de: banca
para: principal
tipo: tarefa
acao_esperada: gatear com o autor as duas figuras da tarefa 0138 (legendas e pontos de inserção abaixo); a banca NÃO tocou no Cap. 3
referencia: tarefa 0138 · esq-sequencia-metodologia.tex + esq-preproc-espacos-rotulos.tex (v2) · branch banca/esquemas-tikz-metodo
criada_em: 2026-08-24T02:10:00Z
---
Entrega da tarefa 0138 (2 figuras, loop de excelência em corpo 12; autor já
recebeu as prévias; 0 erros / 0 overfull nas medidas reais).

1. **`esq-sequencia-metodologia.tex` (NOVA)** — conta a história da
   abertura @74c1fad na mesma ordem: problema → terreno comum → pilares 1-4
   com a LÓGICA DE PRECEDÊNCIA nas setas ("o processo começa sem rótulo
   algum"; "medida a importância, constrói-se o começo"; "definido o
   começo: quem rotula?"; "resolvidos início e oráculo, integra-se e
   avalia-se") → LCE como faixa transversal tracejada → fecho
   (validade/reprodutibilidade). Zero números/códigos/caminhos/travessões.
   Loop: 2 renders (hifenizações "rotu-lagem"/"pes-quisa" e rótulo
   encostando no tracejado, corrigidos).
   LEGENDA PROPOSTA: "A sequência da metodologia como fluxo de decisões:
   do problema, sobre o terreno comum, aos quatro pilares na ordem em que
   o custo de rotulagem aparece; cada seta indica o que precisa estar
   resolvido antes do passo seguinte. A \textit{Learning Curve Efficiency}
   (LCE) atravessa os quatro pilares, e o capítulo encerra com as ameaças
   à validade e o instrumental de reprodutibilidade."
   INSERÇÃO PROPOSTA: abertura do Cap. 3, após o 1º parágrafo (antes de
   "Todos os experimentos são implementados...").

2. **`esq-preproc-espacos-rotulos.tex` (v2, polida)** — recalibrada de
   corpo 10 para corpo 12 e tornada ESTRUTURAL: as contagens (621, 714,
   231.490 etc.) SAÍRAM da figura conforme a restrição "zero números
   medidos" — a prosa da seção continua a carregá-las, e a nota da figura
   remete a elas e à receita executável (sem nome de arquivo). Trade-off
   declarado para o gate: a v1 (no histórico do git) tem a versão com
   números, se o autor preferir o impacto ao custo do risco de espelho.
   LEGENDA PROPOSTA: "O pré-processamento e os dois espaços de rótulos: a
   mesma base normalizada é contada de dois modos, com papéis distintos; o
   \textit{CategorySchema} fechado governa os oráculos, e a visão
   deduplicada, sem a sentinela, preserva a cauda longa para os
   experimentos em escala populacional. As contagens de cada espaço estão
   no texto."
   INSERÇÃO PROPOSTA: fim da Seção sec:metodo-dados-preproc.

Prévias versionadas (preview-esq-sequencia-metodologia.png,
preview-esq-preproc-espacos-rotulos.png regenerada).
