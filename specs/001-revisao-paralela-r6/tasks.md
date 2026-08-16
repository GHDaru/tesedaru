# Tasks 001 — Revisão paralela pós-R6: fichamentos de vizinhos + levantamento de normas

## Verification first

- [x] **T0** — DoD executável definido na spec (ls/grep/build_kg) + script de
  sanidade dos front-matters (YAML válido, id=arquivo, falco_relation, PDF
  presente, termos × vocabulário) rodado ANTES de qualquer commit.

## Implementation

- [x] **T1** — Lote anotação-LLM: FreeAL2023 (validar entrada bib existente),
  Zhang2023LLMaAA, Wang2021GPT3Labeling, Pangakis2023Validation. (FR1, FR2)
- [x] **T2** — Lote seleção/cold-start: Hacohen2022TypiClust, Sener2018
  (veredito Sener2017×Sener2018), Yu2023Patron. (FR1, FR2)
- [x] **T3** — Lote viés de avaliação: Farquhar2021Bias,
  Kossen2021ActiveTesting. (FR1)
- [x] **T4** — Lote transformers/desbalanceamento: Schroder2022Uncertainty,
  Bengar2022ClassBalanced. (FR1)
- [x] **T5** — Integração sob lock: normalizar slugs divergentes entre lotes,
  9 entradas novas no bib + termos no vocabulário, um commit por fichamento
  ("Fichamento: {Chave}"). (FR1)
- [x] **T6** — Regenerar KG (`build_kg.py`) e commitar. (FR3)
- [x] **T7** — Relatório de não conformidades UFPR
  (`docs/relatorio-nao-conformidades-ufpr.md`), sem editar a tese. (FR4)

## Living documentation (same pull request)

- [x] **T8** — Plano de revisão atualizado a cada transição (v8 claim →
  v10 gate) com links; claim e conclusão na caixa de coordenação; achados de
  bib reportados para o ciclo `fichamento-audit`.

## Closing tail — MANDATORY, one line each, never delete

- [ ] `TAIL:review` — revisão independente em contexto fresco do diff da branch (evidência no qa-report).
- [ ] `TAIL:security` — varredura de segredos no diff (evidência no qa-report).
- [ ] `TAIL:gate` — gate humano do autor no merge da branch (aguardando).
