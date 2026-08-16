---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: aguardar o aviso do principal sobre a entrada de consolidacao/revisao-paralela-r6 na main e então executar os lotes 1 e 3 na branch bibfix/lotes
referencia: docs/plano-bib-fix.md · docs/parecer-auditoria-bib.md (tabela "Graves") · plano aprovado pelo autor em 2026-08-16
criada_em: 2026-08-16T18:49:12Z
---
O autor aprovou o plano de correção da bibliografia da banca. Seus lotes (os
de maior risco — exigem reconferir a FONTE PRIMÁRIA de cada entrada, não
confiar no que está no .bib):

LOTE 1 — 14 entradas fabricadas ou inexistentes. A tabela "Graves" do parecer
traz chave, problema e a correção proposta (por exemplo: Su2023/FreeAL2023 ->
Xiao2023FreeAL com os autores reais; Tian2023 -> "Just Ask for Calibration";
Margatina2023 -> verificar se a obra real sustenta a alegação da linha 568 do
Cap.2, senão recitar Rouzegar2024; Wu2022 -> redirecionar para o survey real;
triplicata do ActiveLLM -> unificar em Bayer2024ActiveLLM). Confirme cada
correção na fonte antes de aplicar: o parecer é a hipótese, não a prova.

LOTE 3 — clássicos (venue/páginas), estrutura do arquivo, DOIs e o lote
inline suspeito.

BRANCH: bibfix/lotes, commits separados por lote, junto com o lote 2 do
revisor1 (combinem quem abre; o segundo rebaseia). O lock do referencias.bib
fica com quem estiver editando no momento.

BLOQUEIO: não comece antes do meu aviso — a branch consolidacao/
revisao-paralela-r6 traz 9 chaves novas; corrigir antes seria trabalho dobrado.
Enquanto espera, NÃO fique parado: pegue o próximo item livre do plano.

Ao concluir cada lote, conclusão ao principal com hash. A verificação é da
banca (lote 4).
