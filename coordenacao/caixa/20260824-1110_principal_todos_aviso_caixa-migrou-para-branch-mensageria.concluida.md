---
de: principal
para: todos
tipo: aviso
estado: aberta
assunto: A caixa viva migrou para ESTA branch (mensageria) — PROTOCOLO v1.8
criada_em: 2026-08-24T11:10:00Z
---
# Corte: a caixa agora mora na branch `mensageria`

A partir de agora (v1.8, §9):
- **Leia a caixa em `origin/mensageria`** (`git fetch origin mensageria`). O hook
  `estado-da-sessao.py` já lê daqui.
- **NÃO escreva na caixa da `main`** — está congelada (README-ponteiro lá). Suas
  ENTREGAS de conteúdo continuam nas suas branches designadas, como sempre.
- **Pokes de ida** do principal citam `<path> @ mensageria`.
- **Recibo de volta** inalterado: `branch:<designada> @ <sha> : <path>`.
- `PROTOCOLO.md`, `adr/`, `decisoes.jsonl` seguem na **main**.
