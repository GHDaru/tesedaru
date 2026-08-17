---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: começar o LOTE 0 imediatamente (não toca o .bib); o LOTE 2 só depois que o principal avisar que consolidacao/revisao-paralela-r6 entrou na main
referencia: docs/plano-bib-fix.md (branch claude/critical-review-thesis-submission-f5hjgx) · docs/parecer-auditoria-bib.md · plano aprovado pelo autor em 2026-08-16
criada_em: 2026-08-16T18:49:12Z
---
O autor aprovou o plano de correção da bibliografia da banca. Seus lotes:

LOTE 0 — COMECE JÁ (não depende de nada, não toca o referencias.bib):
scripts/check-bib.py — ferramenta que valida o referencias.bib e falha com
código diferente de zero quando encontrar: (a) títulos duplicados entre
chaves distintas; (b) entrada citada na tese sem DOI/arXiv quando o tipo
exigir; (c) campos residuais de anotação de LLM (note/key com texto de
modelo); (d) chave citada no .tex e ausente no .bib, e vice-versa. Saída
legível (arquivo, chave, problema) e opção --json. Entra depois no DoD
(item dod-scripts do plano). Sua superfície: scripts/ (dono por arquivo).

LOTE 2 — AGUARDE MEU AVISO: duplicatas (17 títulos duplicados; unificar
chaves) + repontuação dos \cite na prosa dos Caps. 1 e 2 (37 citações
afetadas, 9 no cap.1 e 28 no cap.2). Trabalho mecânico, mas exige o lock do
referencias.bib.

REGRA DA BRANCH (para o lock não trocar de mão): os lotes 1, 2 e 3 vivem numa
branch única, bibfix/lotes, em commits separados por lote. Combine com o
revisor2 quem abre a branch; o segundo faz rebase sobre ela. Nada de duas
branches mexendo no mesmo .bib.

Verificação: quem executa não verifica. O lote 4 (conferência independente) é
da banca. Ao concluir cada lote, mande conclusão ao principal com o hash.

## Resultado (revisor1, 2026-08-16T21:30Z)
LOTE 0: scripts/check-bib.py + scripts/test-check-bib.py, 13 casos de fixture
verdes, em claude/maestro-cycles-statistical-analysis-fwla6a @ 33a9c50.
LOTE 2: unificação de 14 duplicatas + repontuação de 8 \cite no Cap. 1 +
renomeação de 5 fichamentos/PDFs para a chave canônica, em bibfix/lotes
@ 7b039c1. Regressão de relação pendurada detectada pelo revisor2 e fechada
por mim em @ d8f5bf0 (varri as 14 chaves removidas, achei mais 2).
Ambos aguardam gate do autor, consolidado pelo principal.
