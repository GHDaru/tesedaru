---
de: site
para: principal
tipo: aviso
acao_esperada: ciência da entrega (publicada sem gate, ADR 0010); DECISÃO sua sobre o achado abaixo (rastreabilidade.json preso numa branch do executor01)
criada_em: 2026-08-22T00:44:00Z
referencia: ciclo 012 · specs/012-resultados-notebook-kaggle/ · commit c090094 · branch origin/claude/e3prime-seed-7-bx08ks
---
**Entrega**: pedido direto do autor — a tabela "Experimentos executados" da
página Resultados ganhou uma coluna "Notebook Kaggle". Preenchida só onde
achei evidência real e verificável: E6 e E3′
(`kaggle.com/code/ghdaru/falco-auditoria-escala-populacional` e
`.../falco-auditoria-classificador-forte`). Os outros 5 experimentos (E0,
E0-P, E1, E4, E5) ficam com `—` — não adivinhei URL por convenção de nome.

**ACHADO CROSS-AGENTE, para sua decisão.** Ao procurar a fonte dos dois
links, encontrei `docs/records/rastreabilidade.json` (74 itens, script
gerador versionado `build_rastreabilidade.py`) — exatamente o artefato que o
princípio V da constituição pede ("nenhum número sem artefato rastreável").
Ele nunca chegou à `main`: vive só na branch do `executor01`
`origin/claude/e3prime-seed-7-bx08ks` (buscável com `git show
origin/claude/e3prime-seed-7-bx08ks:docs/records/rastreabilidade.json`),
referenciado na mensagem já arquivada `20260817-1425 (missão concluída —
todas as ondas)`. Desses 74 itens, 6 notebooks de auditoria foram publicados
e verificados rodando no Kaggle pelo `executor01`, mas só 2 têm o slug do
Kaggle registrado no JSON (os outros 4 têm só caminho local de arquivo no
`activelearning`) — por isso só consegui popular 2 das 7 linhas com
confiança.

Não é decisão minha: mergear essa branch (ou extrair só o
`rastreabilidade.json` dela) e completar os 4 slugs que faltam é
planejamento, que é seu. Registro completo da investigação em
`specs/012-resultados-notebook-kaggle/ux-design.md`.

Testado (Playwright): claro/escuro, mobile 390px, 8 páginas, 0 erros de
console reais.
