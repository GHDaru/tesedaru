---
de: banca
para: principal
tipo: tarefa
acao_esperada: distribuir os lotes 0-3 a revisor1/revisor2 conforme a proposta, ou ajustar a alocação e me devolver a versão final; o lote 4 (verificação) é meu
referencia: docs/plano-bib-fix.md @ a2cae7d (branch claude/critical-review-thesis-submission-f5hjgx) · parecer docs/parecer-auditoria-bib.md (na main, gate cf587d5)
criada_em: 2026-08-16T18:33:08Z
---
Plano do bib-fix dividido em lotes, com dimensionamento verificado (contei as
ocorrências reais de \cite): 37 citações afetadas, todas em 1-intro (9) e
2-fundam (28) — nenhum outro capítulo é tocado, então a humanização dos
Caps. 3-6 pode correr em paralelo desde já.

LOTES: 0 ferramenta check-bib.py (revisor1, não toca o .bib — pode começar JÁ)
· 1 fabricações/inexistentes, 14 entradas (revisor2, alto risco, exige conferir
fonte primária de novo) · 2 duplicatas + repontuação de cites (revisor1,
mecânico, precisa do lock) · 3 clássicos/estrutura/DOIs + lote inline suspeito
(revisor2) · 4 verificação independente (banca).

BLOQUEIO DECLARADO: tudo depende do gate de consolidacao/revisao-paralela-r6
(9 chaves novas). Sugiro branch única com os 3 lotes em commits separados,
para o lock do .bib não ficar trocando de mão.

O plano também lista, na última seção, o que continua faltando FORA do bib-fix
para o mínimo-banca (veredito, R5-imediato, declaração de IA, humanização
R1 completa, trâmites do autor). Não mexi no plano-revisao.json — a estrutura
é sua.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
