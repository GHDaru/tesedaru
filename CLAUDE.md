# tesedaru — tese de doutorado FALCO (PPGMNE/UFPR)

Repositório da tese "FALCO: Framework de Aprendizado Ativo com LLM para texto
CurtO" (Gilsiley Henrique Darú). Fonte LaTeX em `principal.tex` + capítulos em
`N-*/texto.tex`; artigos derivados em `artigos/`; fichamentos e grafo de
conhecimento em `fichamentos/`.

## Constituição da tese (conteúdo) — LEIA ANTES DE EDITAR O TEXTO
`docs/governance/constituicao-tese.md` — princípios de conteúdo acadêmico:
siglas abertas na 1ª ocorrência e presentes na lista, referências validadas
contra fichamento, afirmações fundamentadas, decisões em ADR
(`docs/adr/` + `docs/records/decisoes.jsonl`).

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
