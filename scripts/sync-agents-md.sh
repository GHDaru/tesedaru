#!/usr/bin/env bash
# Gera AGENTS.md a partir do CLAUDE.md (fonte única).
# Por que não um link simbólico: o Overleaf recusa repositórios com symlinks.
# Rode após editar o CLAUDE.md; o check-install.sh exige o conteúdo nos dois.
set -euo pipefail
cd "$(dirname "$0")/.."
{
  echo "<!-- GERADO por scripts/sync-agents-md.sh a partir do CLAUDE.md."
  echo "     NÃO edite este arquivo: edite o CLAUDE.md e rode o script."
  echo "     (era um symlink; virou cópia porque o Overleaf não aceita symlinks) -->"
  echo
  cat CLAUDE.md
} > AGENTS.md
echo "AGENTS.md regenerado a partir do CLAUDE.md"
