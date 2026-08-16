# Spec 001 — Revisão paralela pós-R6: fichamentos de vizinhos + levantamento de normas

- **Status**: Em gate · **Lane**: full · **Date**: 2026-08-16
- **Origin**: parecer ARS R6 (`docs/parecer-ars-r6.md`, Bloco C itens 9–11) +
  plano de revisão v5–v8 (itens `fichar-vizinhos` e `normas-ufpr`), executados
  pelo agente **revisor2** sob o protocolo de coordenação (claim
  `coordenacao/caixa/20260816-1719_revisor2_todos_*`). Pedido do autor na
  sessão: toda branch segue o fluxo Maestro (spec → plan → tasks → implement).

## What and why

O parecer R6 rebaixou a tese a MAJOR REVISION por, entre outros, lacunas de
posicionamento de literatura: vizinhos diretos (FreeAL, LLMaAA) não
confrontados, viés de autoavaliação sem as referências canônicas
(Farquhar 2021, Kossen 2021) e DRI-SL sem confronto com TypiClust/coreset/
PATRON. A constituição da tese (princípio II) proíbe citar sem fichamento:
antes de qualquer texto novo do Capítulo 2, as 11 obras precisam estar
fichadas e validadas contra a fonte primária (lente nova do R3 — o mesmo
parecer achou metadados fabricados no bib). Em paralelo, o item de
encerramento `normas-ufpr` precisa da fase de levantamento: um relatório de
não conformidades do documento real contra o padrão UFPR/PPGMNE, sem tocar a
prosa (correções são ciclos gateados).

## Functional requirements

- **FR1**: 11 fichamentos novos em `fichamentos/` (padrão KG-ready da skill
  `fichamento`): FreeAL, LLMaAA, Wang21, Pangakis23, TypiClust, coreset
  (Sener), PATRON, Farquhar21, Kossen21, Schröder22, Bengar22 — cada um com
  identidade validada na fonte primária (DOI/venue), claims com evidência
  localizável, PDF arquivado em `referencias-pdf/`, entrada BibTeX e termos
  novos de vocabulário no MESMO commit ("Fichamento: {Chave}").
- **FR2**: divergências de metadados encontradas no `referencias.bib`
  reportadas (não corrigidas — pertencem ao ciclo `fichamento-audit`).
- **FR3**: KG regenerado (`build_kg.py`) com os 11 nós novos.
- **FR4**: relatório de não conformidades UFPR/PPGMNE em
  `docs/relatorio-nao-conformidades-ufpr.md`, item a item com evidência
  `arquivo:linha`, aprofundando (sem duplicar) o levantamento de fontes de
  `docs/normas-ufpr-ppgmne-e-skills.md`.

## Out of scope

- Editar capítulos, pré-textuais, tabela de lacunas ou qualquer prosa
  (superfície do agente `principal`; o campo `proximo` do plano está SUSPENSO).
- Corrigir entradas existentes do bib (fabricadas ou duplicadas) — ciclo
  `fichamento-audit`/Bloco A item 1.
- Corrigir as não conformidades de normas — ciclos de texto gateados.

## Acceptance criteria (DoD)

- `ls fichamentos/{FreeAL2023,Zhang2023LLMaAA,Wang2021GPT3Labeling,Pangakis2023Validation,Hacohen2022TypiClust,Sener2018,Yu2023Patron,Farquhar2021Bias,Kossen2021ActiveTesting,Schroder2022Uncertainty,Bengar2022ClassBalanced}.md` → 11 arquivos, exit 0.
- `ls referencias-pdf/<Chave>.pdf` para as mesmas 11 chaves → exit 0.
- WHEN o front-matter de qualquer fichamento é lido THE SYSTEM SHALL conter
  `falco_relation` não vazio e id igual ao nome do arquivo (checado por
  script na integração).
- `grep -c "@" referencias.bib` cresce em exatamente 9 (2 chaves já
  existiam: FreeAL2023, Sener2018).
- `uv run --with pyyaml python fichamentos/build_kg.py` → exit 0 e mais nós
  que os 508 da linha de base.
- `test -f docs/relatorio-nao-conformidades-ufpr.md` → exit 0; o relatório
  não edita nenhum arquivo da tese (diff da branch não toca `*.tex`,
  `*.cls`, `*.bst`).

## Clarify

- Fichamentos produzidos a partir do PDF oficial baixado da fonte primária
  (arXiv/ACL Anthology/PMLR/CVF), não de memória; onde só o preprint estava
  acessível (Farquhar: OpenReview bloqueia download), isso está declarado no
  próprio fichamento.
- Sener2018 vs Sener2017: fichamento usa Sener2018 (versão ICLR publicada);
  duplicata reportada.
