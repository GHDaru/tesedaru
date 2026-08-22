---
de: principal
para: todos
tipo: tarefa
acao_esperada: revisor1 e revisor2 executam o lote 5 (corretivo de COBERTURA) na branch bibfix/lotes; banca re-verifica depois; ninguém pede gate direto ao autor
referencia: docs/parecer-bibfix-lote4.md · decisão do autor 2026-08-16 ("refazer com o cuidado da cobertura")
criada_em: 2026-08-16T20:32:39Z
---
O autor leu o parecer do lote 4 e determinou: REFAZER COM CUIDADO DE
COBERTURA. O trabalho feito está correto — o que faltou foi alcance. Lote 5,
corretivo:

BLOQUEADORES (a banca abriria e não encontraria a obra):
1. Wu2022, citada em 2-fundam:619 — inexistente. ATENÇÃO: a alegação da linha
   fala em seleção de PROMPTS e do ORÁCULO, que o survey substituto não cobre.
   NÃO troque a chave e pronto: sinalize ao principal, porque a FRASE é
   superfície de prosa e será tratada por ele com o autor.
2. Ahmed2023, citada em 2-fundam:648 — inexistente. Remover a entrada e
   repontuar a citação (a repontuação da prosa também passa pelo principal).

CORREÇÕES DIRETAS: Ahmed2022 year=2023; Guo2025Deuce year=2024; Wei2022
faltam Brian Ichter e Fei Xia; Hacohen2023 (órfã, fabricada) remover;
Zhang2022 (órfã, autores fabricados) corrigir ou remover.

AS 22 ÓRFÃS: adoto a recomendação da banca — REMOVER, não verificar. Entrada
que ninguém cita não sustenta afirmação nenhuma, e removê-la é reversível
pelo git. Se algum de vocês achar que uma delas deveria estar citada, avise o
principal ANTES de remover.

AS 15 CITADAS: o revisor1 já as verificou contra a fonte (arXiv/Crossref) e
todas conferem — não precisam ser refeitas.

MÉTODO QUE MUDA (a lição do lote 4): verificar contra a FONTE PRIMÁRIA, nunca
contra o parecer. E rodar check-fichamentos.py ao fim de cada lote, não só o
check-bib.py — a lição do revisor2: deduplicar chave atravessa superfícies
(fichamentos e \cite dos capítulos).

DoD do lote 5: os dois checadores em exit 0, zero fabricação entre as citadas,
zero órfã, e a banca re-verificando por amostragem contra a fonte.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
