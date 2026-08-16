---
de: banca
para: principal
tipo: tarefa
acao_esperada: levar ao autor o gate deste procedimento e designar executor; NÃO iniciar as fases 3-4 enquanto houver branches abertas do bib-fix/mínimo-banca
referencia: docs/parecer-referencias-pdf-repositorio-privado.md @ 45733d5 (branch claude/critical-review-thesis-submission-f5hjgx)
criada_em: 2026-08-16T19:00:54Z
---
O QUE MUDOU: parecer novo com o procedimento de migração dos PDFs de
referência para repositório privado, pedido pelo autor.

EVIDÊNCIA (medida, não estimada): 140 PDFs rastreados em referencias-pdf/;
294 MB no working tree; 155 blobs no histórico; repositório tesedaru é
PÚBLICO. Há artigos de Elsevier, IEEE, Springer, Sage e MDPI-pagos, cujas
licenças proíbem redistribuição.

RISCO: (a) jurídico/reputacional durante a defesa; (b) apagar na main não
resolve — blobs seguem acessíveis por SHA e por forks, exige git filter-repo
+ pedido de GC ao GitHub; (c) a reescrita de histórico INVALIDA branches
abertas — por isso o parecer separa fases reversíveis (0-2, podem rodar já)
das irreversíveis (3-4, só depois do bib-fix e do lote do veredito).

PONTO QUE EXIGE DECISÃO DO AUTOR: a fase 3 precisa de force-push em todas as
refs, o que contraria o PROTOCOLO §4 ("force-push em main é proibido"). O
parecer propõe exceção nominal, autorizada por ele, com git bundle como rede
de segurança. Sem essa autorização explícita, a migração para no fim da fase 2
(que já para o crescimento do problema).

NÃO É BLOQUEIO DA BANCA: é dívida com prazo, não afeta o mérito nem o texto.
Prioridade segue sendo o mínimo-banca.

DoD verificável e riscos com mitigação estão no parecer (§4 e §5). Executor
sugerido: quem detiver menos superfícies de texto no momento — banca não
executa (não edita superfície alheia).
