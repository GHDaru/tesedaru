# tesedaru — Tese de Doutorado FALCO (reescrita final)

Repositório LIMPO do texto da tese (Gilsiley Darú, PPGMNE/UFPR). Template `ppginf.cls`.

## Regras para agentes
1. **Regra de ouro**: nenhum número experimental entra no texto sem artefato
   rastreável no repositório `GHDaru/activelearning` (config+seed+JSONL). Nunca
   inventar resultados ("[Suposição:]" é proibido).
2. Plano vigente: `docs/plano-mestre.md` (trilhas W1-W9). Parecer da banca simulada:
   `docs/parecer-fase-menos-1.md`.
3. Citações: natbib (`\citep`/`\citet`), BibTeX em `referencias.bib` (chave = ID
   universal: fichamento, PDF e nó do grafo usam a mesma chave).
4. Fichamentos: seguir a skill `fichamento` (`.claude/skills/fichamento/`).
   PDFs originais em `referencias-pdf/{ChaveBibtex}.pdf`; entrada de novos PDFs em
   `a_sanear/`.
5. Repositórios legados (`Tese-Vers-o-Draft`, `activetextclassification`) são
   SOMENTE LEITURA — fonte de porte, nunca destino.
6. Compilação: `pdflatex principal && bibtex principal && pdflatex ×2`.
