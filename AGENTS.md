<!-- GERADO por scripts/sync-agents-md.sh a partir do CLAUDE.md.
     NÃO edite este arquivo: edite o CLAUDE.md e rode o script.
     (era um symlink; virou cópia porque o Overleaf não aceita symlinks) -->

# tesedaru — tese de doutorado FALCO (PPGMNE/UFPR)

Repositório da tese "FALCO: Framework de Aprendizado Ativo com LLM para texto
CurtO" (Gilsiley Henrique Darú). Fonte LaTeX em `principal.tex` + capítulos em
`N-*/texto.tex`; artigos derivados em `artigos/`; fichamentos e grafo de
conhecimento em `fichamentos/`.

> **AGENTS.md é cópia gerada deste arquivo** (`scripts/sync-agents-md.sh`):
> editou o CLAUDE.md, rode o script. Não use symlink — o Overleaf recusa
> repositórios que contenham links simbólicos.

## Constituição da tese e protocolo — CARREGADOS, não apenas citados
Os dois arquivos abaixo entram no contexto por `@`-import a **cada**
carregamento. Não é "leia quando puder": é texto que você já tem na mão, e
por isso ninguém pode alegar que não sabia a regra.

@docs/governance/constituicao-tese.md
@coordenacao/PROTOCOLO.md

O que eles obrigam, em uma linha cada: siglas abertas na 1ª ocorrência e
presentes na lista; referência validada contra fichamento; nenhuma afirmação
sem fundamento; **nenhum número sem artefato rastreável**; decisão registrada
em ADR (`docs/adr/` + `docs/records/decisoes.jsonl`).

Os arquivos GRANDES ficam de fora do import de propósito — `plano-revisao.json`
(51 KB) e `decisoes.jsonl` (17 KB) mudam a cada hora e são lidos por recorte;
importá-los custaria mais contexto do que entregam.

## Regras duras — executadas por hook, não por boa vontade
`.claude/settings.json` liga dois hooks, com o código em `scripts/hooks/`:

- **`PreToolUse` → `guarda-regras-duras.py`** BLOQUEIA a chamada, sem depender
  de ninguém lembrar: (1) **force-push em `main`** — push rejeitado resolve-se
  com `git fetch origin main && git rebase origin/main`, nunca com force;
  (2) **`.env`** em qualquer forma — segredo fica fora do git; (3) edição de
  arquivo tocado por branch **`humanize/*` ou `governanca/*`**; (4) edição
  direta de **`AGENTS.md`**, que é gerado. Se você foi bloqueado, a mensagem
  diz qual regra e qual é a saída legítima.
- **`SessionStart` → `estado-da-sessao.py`** imprime o estado **medido**:
  âncora da `origin/main`, locks vivos com TTL calculado, caixa aberta por
  remetente, branches fora da main. Existe por um erro real: bilhete repetido
  de sessão em sessão vira mentira; medição não vira.

O guarda **falha em aberto** — qualquer erro interno dele permite a ação,
porque um guarda quebrado não pode parar a tese. As quatro proibições acima,
essas não são negociáveis por esquecimento.

## Comunicação com o autor (princípio XI — "ELI15") e roteamento (XII)
Ao falar com o AUTOR: didático e detalhado — termos explicados, siglas abertas,
nada de expressões curtas/telegráficas; o autor decide melhor com contexto
completo. Ao coordenar: o agente `principal` é o HUB — mensagens ao autor só
via principal; agente↔agente via principal; planejamento só pelo principal;
GATES DE MERGE consolidados pelo principal e levados ao autor em bloco (exceto
site/painel, que dispensa gate) — constituição v1.2.1, ADRs 0009/0010,
PROTOCOLO §2-bis.

## Coordenação multiagente — OBRIGATÓRIO para toda sessão
4 agentes (principal · banca · revisor1 · revisor2) + o autor coordenam-se por
`coordenacao/` (PROTOCOLO.md = a regra; caixa/ = mensagens; locks/ = locks de
superfície com TTL 45 min). Ritual de entrada de TODA sessão: `git pull
--rebase` → ler a caixa só por glob (`*_<eu>_*` e `*_todos_*`) → arquivar
antigas → postar o claim do próprio ciclo. Estados por `git mv`
(aberta→em-andamento→concluida). Lock só é seu após push aceito; force-push em
main é proibido. "Escreva só na sua superfície, verifique só o que não fez,
poste só o que muda a ação de outro, e nunca espere parado — a main é do autor."

## Rodadas de revisão (R1–R7) = ciclos Maestro — OBRIGATÓRIO
Cada célula capítulo×rodada do plano (`docs/records/plano-revisao.json`) é UM
ciclo Maestro completo: branch própria → antes/depois na conversa → DoD →
gate humano no merge → ADR quando houver decisão → atualizar o plano
(versao+1) e dar push (o painel https://ghdaru.github.io/tesedaru/ se
re-renderiza sozinho). O campo `ritual` do plano é a forma executável desta
regra; o campo `proximo` diz o passo seguinte de qualquer sessão.

**Mapa skill → rodada (invocar pelo nome ao abrir o ciclo):**
| Skill | Quando usar |
|---|---|
| `fight-the-pile-up` | R1 (humanização) e R2 (siglas): é a skill editorial de des-densificar sem mudar conteúdo técnico |
| `constitution-check` | Ao abrir QUALQUER ciclo: tabela contra os 8 princípios do método + os 10 da tese |
| `verifiable-dod` | R5 e todo DoD de merge (princípio IX): critério vira checagem executável (grep/script), não juízo |
| `diagnose-before-fix` | R5-imediato e qualquer inconsistência numérica: causa-raiz antes de corrigir |
| `anti-patterns` | Retrospectiva ao fechar cada capítulo |
| `living-journey` | Já cumprida por painel + decisoes.jsonl; usar o formato dela em jornadas novas de interface |

## Method: Maestro
- Read `docs/governance/principles.md` (the constitution) and
  `docs/governance/operating-model.md` before any work.
- **Skills first**: before acting, check whether one of the skills below applies; if
  there is a reasonable chance, follow it (each carries its Iron Law):
  - `anti-patterns` — Catalogue of what NOT to do when one human runs many agents — the recurring mistakes observed in our own retrospectives and in the ecosystem.
  - `constitution-check` — Produces the Constitution Check table (Maestro Principles I–VIII) inside a plan.md, decides when a principle counts as violated and what to do with the violation.
  - `diagnose-before-fix` — Root-cause discipline — investigate before fixing.
  - `fight-the-pile-up` — Editorial checklist that turns a dense document (a "pile-up" — many acronyms with no dictionary, everything on one page, no narrative) into clear text without changing the technical content.
  - `living-journey` — Living journey documentation — one document per journey, screenshots generated from the real build by a versioned script, and a dated heuristic evaluation, all in the same pull request.
  - `verifiable-dod` — Turns vague acceptance criteria into executable fitness functions (grep, ls, tests) that a machine can verify without human judgement.
- Flow: `spec → plan (Constitution Check) → tasks → implement → DoD → review in
  fresh context → human gate → merge`.
- Lanes: light (the pull request is the artifact) · full (complete spec) · infra (full +
  reversibility).
- Every cycle declares its conditional artifacts and carries the closing tail
  (`TAIL:review`, `TAIL:security`, `TAIL:gate`) in `tasks.md`, with the evidence in
  `qa-report.md`. Catalogue: `docs/governance/artifacts.md`.
- **Asked "are you following the method?" — do NOT answer from memory.** Run
  `scripts/check-conformance.sh <NNN>` and read it: memory reports intention, not fact.
