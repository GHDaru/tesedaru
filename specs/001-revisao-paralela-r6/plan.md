# Plan 001 — Revisão paralela pós-R6: fichamentos de vizinhos + levantamento de normas

- **Spec**: `spec.md` · **Lane**: full · **Date**: 2026-08-16

## Constitution Check (docs/governance/principles.md)

| Principle | Compliance |
|---|---|
| I. Spec-driven | ✅ nasce do parecer R6 (Bloco C) e dos itens `fichar-vizinhos`/`normas-ufpr` do plano de revisão aprovado; esta spec fixa o escopo antes do texto. |
| II. Human-governed orchestration | ✅ revisor2 executa em branch; Accountable humano preservado — merge só com gate do autor; verificação por agentes em contexto fresco (quem fichou não integra sem checagem). |
| III. Reversibility / risk gates | ✅ apenas arquivos novos + appends (bib/vocabulário) em branch — reversível por descarte; superfícies compartilhadas sob lock do protocolo de coordenação. |
| IV. Test-first / verifiable DoD | ✅ DoD da spec é executável (ls/grep/build_kg com exit codes); front-matters validados por script antes dos commits. |
| V. Context economy / boundary | ✅ corte por fronteira: 4 lotes temáticos de fichamento em agentes paralelos + 1 agente de normas, cada um cego aos demais; prosa fora do alcance. |
| VI. Living artifacts | ✅ bib, vocabulário e KG evoluem no MESMO commit de cada fichamento; relatório de normas referencia (não duplica) o levantamento anterior. |
| VII. Light governance / YAGNI | ✅ nenhuma estrutura nova: skill `fichamento` e template existentes; vocabulário ganha só termos efetivamente usados. |
| VIII. Intelligible communication | ✅ siglas abertas nos fichamentos e no relatório; cada achado com fonte e evidência localizável. |

**No violations.**

## Artifacts of this cycle (declare all five)

| Artifact | Declaration | Why |
|---|---|---|
| `research.md` | `ART:research=no` | a "pesquisa" é o próprio produto (fichamentos com fonte primária); um research.md duplicaria função (princípio VI). |
| `data-model.md` | `ART:data-model=no` | o modelo (front-matter KG-ready) já é dado por `fichamentos/_TEMPLATE.md`. |
| `contracts/` | `ART:contracts=no` | nenhuma interface nova; o contrato dos nós é o vocabulário controlado. |
| `checklist.md` | `ART:checklist=no` | o checklist executável está no DoD da spec e no script de sanidade da integração. |
| `ux-design.md` | `ART:ux-design=no` | não toca tela (o KG.html é regenerado por script versionado, sem mudança de interface). |

## How

- **Fan-out por fronteira**: 4 agentes de fichamento (lotes: anotação-LLM ×
  seleção/cold-start × viés de avaliação × transformers/desbalanceamento) +
  1 agente de normas, todos proibidos de editar arquivos existentes; a
  integração (bib/vocabulário/commits/KG) é centralizada no revisor2 sob lock
  (`coordenacao/locks/referencias.bib.md` + `fichamentos--_VOCABULARIO.md.md`).
- **Lente R3 nova**: identidade de cada obra validada na fonte primária
  (DOI resolvido/venue oficial); hipóteses de identificação erradas são
  corrigidas pela fonte, nunca acomodadas (caso PATRON: ACL main, não
  Findings; caso Bengar: hipótese alternativa descartada com DOI conferido).
- **Achados sobre superfícies alheias não são corrigidos aqui**: entradas
  fabricadas/duplicadas do bib (FreeAL2023/Su2023, Sener2017, sinalizações
  Diao2023/Margatina2023/Tian2023, Alsmadi 2019a/b) vão para o ciclo
  `fichamento-audit`; não conformidades de normas vão para ciclos gateados.
- Decisão de registro: rodada executada sob o protocolo de coordenação
  multiagente (ADR 0008, do agente principal) — sem ADR novo neste ciclo
  (nenhuma decisão de efeito duradouro além do que o plano já registra).

## Verification (DoD)

Ver `qa-report.md`: cada critério da spec com comando, esperado e resultado
real; tails de revisão independente, segurança e gate.
