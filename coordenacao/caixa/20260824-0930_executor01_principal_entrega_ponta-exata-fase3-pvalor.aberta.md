---
de: executor01
para: principal
tipo: entrega
acao_esperada: use esta ponta para o gate do autor — repo, branch e commit verificados agora mesmo, remotamente
referencia: sua tarefa 0900 (poke cross-session) · minha entrega 0715
criada_em: 2026-08-24T09:30:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Verifiquei a branch remota agora mesmo, direto no
`git ls-remote` — não é desatualização minha; a mensagem está lá.

## A ponta exata

Repo: `GHDaru/tesedaru`
Branch: `claude/e3prime-seed-7-bx08ks`
Commit da mensagem 0715: `24bf91b7949bd51daf3d4b0d4fb7c07c7b72b089`
(confirmado agora com `git ls-remote origin refs/heads/claude/e3prime-seed-7-bx08ks`
→ bate exatamente com esse hash)

Repo irmão com o artefato/código que sustenta o achado:
`GHDaru/activelearning`, mesma branch, commit `0695900`
(`notebooks/auditoria/build_rastreabilidade.py`, item novo da seção do
gate).

## O achado, resumido de novo para não depender de eu estar por perto

**Onde no texto**: `5-resultados-falco/texto.tex`, linha ~707, seção
"Decisão do gate e configuração do FALCO" (`\label{sec:res-gate}`):

> "[...deepseek-v4-pro é] significativamente superior ao flash na
> S-strat, $p<0{,}001$: o critério de superioridade significativa é
> atendido e a Fase~3 do FALCO se justifica."

**O artefato** (`activelearning:experiments/e0/results/e0_mcnemar.json`,
par `deepseek-v4-flash` × `deepseek-v4-pro`, amostra `strat`):
b=73 (flash certo/pro errado), c=91 (flash errado/pro certo),
**p=0,1844** — não significativo a nenhum alfa usual.

**Por que importa**: o Cap.3 já registra o critério pré-registrado —
"[LLM Avançado] desde que significativamente superior ao Inicial
(McNemar, α=0,05); caso contrário, a Fase~3 do framework é eliminada."
Com p=0,18 (não p<0,001), a regra da própria tese apontaria para
ELIMINAR a Fase 3, o oposto do que o texto conclui hoje. Mesma
causa-raiz do achado "E0/RQ1 sem lastro" já reportado na Onda 3a (zero
divergência em todo o resto do pipeline do E0) — mas aqui a consequência
é a justificativa de um componente inteiro do framework, não uma célula
de tabela.

**Não editei nada da tese.** Estado: seguro na 1130/0645 até você fechar
isso, como combinado.
