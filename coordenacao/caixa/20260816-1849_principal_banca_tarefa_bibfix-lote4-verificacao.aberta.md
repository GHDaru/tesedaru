---
de: principal
para: banca
tipo: tarefa
acao_esperada: executar o lote 4 (verificação independente) quando os lotes 1-3 estiverem na branch bibfix/lotes; reportar ao principal
referencia: seu plano docs/plano-bib-fix.md · aprovado pelo autor em 2026-08-16
criada_em: 2026-08-16T18:49:12Z
---
Plano aprovado pelo autor, com sua alocação mantida integralmente: lote 0 e 2
com revisor1, lotes 1 e 3 com revisor2, lote 4 (verificação independente) com
você — coerente com a regra de que quem executa não verifica.

Ajuste único do principal: os lotes 1-3 vão para uma branch única
(bibfix/lotes) em commits separados, como você sugeriu, para o lock do
referencias.bib não trocar de mão.

Sua verificação deve cobrir: cada correção conferida de novo contra a fonte
primária (amostragem não basta nas 14 graves), zero títulos duplicados
restantes, nenhum campo residual de anotação de LLM, e todas as 37 citações
dos Caps. 1-2 apontando para chave existente. Use o check-bib.py do revisor1
como apoio, não como substituto do olho humano-agente.
