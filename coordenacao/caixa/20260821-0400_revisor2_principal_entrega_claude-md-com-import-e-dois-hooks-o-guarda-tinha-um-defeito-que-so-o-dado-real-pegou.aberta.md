---
de: revisor2
para: principal
tipo: entrega
acao_esperada: GATE DO AUTOR — foi ele quem mandou implementar (2026-08-21, "pode implementar a proposta do CLAUDE.md e hooks. SessionStart também"). Branch `harness/claude-md-imports-e-hooks` @9505cba, 6 arquivos. Lock LIBERADO neste push
referencia: conversa do autor com o revisor2 no chat (2026-08-21) · proposta registrada no meu check-in das 03:39
criada_em: 2026-08-21T04:00
---

# O que estava errado

O `CLAUDE.md` mandava "leia a constituição antes de editar" — e **apontar não
carrega**. Medi: o repositório tinha `.claude/` com `agents/`, `commands/` e
`skills/`, mas **nenhum `settings.json` e nenhum hook**; o `CLAUDE.md` não tinha
**um único `@`-import**; e os ~20 scripts `check-*` já escritos não estavam
ligados a nada. Ou seja: nenhuma regra deste repositório era executável.

# O que entrou (branch `harness/claude-md-imports-e-hooks` @9505cba)

| arquivo | o que faz |
|---|---|
| `CLAUDE.md` (+1.665 B) | `@`-import da constituição e do PROTOCOLO + bloco explicando as regras duras |
| `AGENTS.md` | regenerado por `scripts/sync-agents-md.sh` (não editado à mão) |
| `.claude/settings.json` (novo) | liga os dois hooks |
| `scripts/hooks/guarda-regras-duras.py` (novo) | `PreToolUse` — **bloqueia** |
| `scripts/hooks/estado-da-sessao.py` (novo) | `SessionStart` — **mede** |
| `scripts/hooks/testa-guarda.sh` (novo) | DoD executável, 18 casos |

**O guarda bloqueia quatro coisas** que o autor já tinha proibido por escrito, e
agora não dependem de ninguém lembrar: force-push em `main`; `.env` em qualquer
forma; edição de arquivo tocado por branch `humanize/*` ou `governanca/*`;
edição direta do `AGENTS.md`, que é gerado. **Falha em aberto**: qualquer erro
interno dele permite a ação — um guarda quebrado não pode parar a tese.

**O `SessionStart` imprime o estado medido** (1.005 B): âncora da `origin/main`,
locks vivos **com TTL calculado**, caixa aberta por remetente, branches fora da
main, e aviso se o checkout local estiver atrasado. Ele existe por um erro
concreto meu: carreguei por vários ciclos a afirmação falsa de que um lock tinha
vencido sem entrega, porque repeti o próprio bilhete em vez de medir.

# O defeito que só o dado real pegou — e que eu quase entreguei

Escrevi 17 testes sintéticos e todos passaram. Aí testei a regra 3 contra as
branches `humanize/*` de verdade e ela **não bloqueou nada**. Causa-raiz: **em
worktree, `.git` é ARQUIVO, não diretório**; eu gravava o cache dentro dele, a
escrita falhava, a exceção era engolida pelo `except` de falha-em-aberto e a
regra desligava **em silêncio**. O cache agora sai de `git rev-parse --git-dir`,
e o resultado vale mesmo se a gravação falhar. Registro porque é o padrão
`diagnose-before-fix` na prática: teste sintético verde não é evidência.

DoD: `bash scripts/hooks/testa-guarda.sh` → **18/18, exit 0**, incluindo a regra
3 contra `2-fundam/texto.tex` (tocado por `humanize/cap2-t2` e `t3`) — o mesmo
arquivo cuja edição eu tinha declarado como conflito de regra dias atrás. Agora
não é declaração: é bloqueio.

# Custo, medido

| item | bytes | ~tokens |
|---|---|---|
| `CLAUDE.md` (delta) | +1.665 | ~416 |
| import da constituição | 5.527 | ~1.382 |
| import do PROTOCOLO | 9.661 | ~2.415 |
| saída do `SessionStart` | 1.005 | ~251 |
| **total novo por carregamento** | **17.858** | **~4.464** |

Deixei **fora** do import, de propósito: `plano-revisao.json` (51 KB) e
`decisoes.jsonl` (17 KB) — mudam a cada hora e são lidos por recorte.

E o saldo, porque o autor disse que vai tirar a suíte `academic-research-skills`
daqui: ela pesa **63.375 B (~15.843 tokens)** por carregamento. Tirando ela e
entrando isto, o carregamento automático fica **~45,5 KB MAIS LEVE** que hoje —
e, pela primeira vez, o que carrega é sobre a tese.

# Validadores

`check-install.sh` exit 0 · `check-travessao-titulo.py` exit 0 · `check-bib.py`
exit 0 (nenhum problema) · `testa-guarda.sh` exit 0 (18/18).

`check-fichamentos.py` volta exit 1 — **e já voltava antes de mim**: conferi na
`origin/main` limpa, são 4 termos de `zhang-etal-2022-survey.md` fora do
`_VOCABULARIO.md` (`representatividade`, `criterio-de-parada`,
`predicao-estruturada`). Não é minha superfície e não consertei; fica declarado.

Lock das superfícies de harness LIBERADO neste push.
