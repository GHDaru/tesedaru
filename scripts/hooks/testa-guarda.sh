#!/usr/bin/env bash
# DoD executavel do hook PreToolUse (principio IX: criterio vira checagem, nao juizo).
# Rode depois de QUALQUER mexida em guarda-regras-duras.py. Exit 0 = todos passam.
set -uo pipefail
cd "$(dirname "$0")/../.."
G="scripts/hooks/guarda-regras-duras.py"
RAIZ="$(pwd)"
falhas=0

t() { # descricao | esperado (BLOQUEIA|permite) | json
  local desc="$1" esperado="$2" json="$3"
  echo "$json" | python3 "$G" >/dev/null 2>&1
  local rc=$?
  local obtido; [ $rc -eq 2 ] && obtido=BLOQUEIA || obtido=permite
  if [ "$obtido" = "$esperado" ]; then
    printf "  ok   %-46s %s\n" "$desc" "$obtido"
  else
    printf "  FALHA %-45s obtido=%s esperado=%s\n" "$desc" "$obtido" "$esperado"
    falhas=$((falhas+1))
  fi
}

echo "regra 1 — force-push"
t "push normal para main"           permite  '{"tool_name":"Bash","tool_input":{"command":"git push origin HEAD:main"}}'
t "push --force para main"          BLOQUEIA '{"tool_name":"Bash","tool_input":{"command":"git push --force origin HEAD:main"}}'
t "push --force-with-lease p/ main" BLOQUEIA '{"tool_name":"Bash","tool_input":{"command":"git push --force-with-lease origin HEAD:main"}}'
t "push --force-with-lease p/ branch" permite '{"tool_name":"Bash","tool_input":{"command":"git push --force-with-lease origin ciclo/016"}}'
t "push -f em branch qualquer"      BLOQUEIA '{"tool_name":"Bash","tool_input":{"command":"git push -f origin ciclo/016"}}'
t "force escondido depois de &&"    BLOQUEIA '{"tool_name":"Bash","tool_input":{"command":"git fetch && git push --force origin main"}}'
t "a palavra force num grep"        permite  '{"tool_name":"Bash","tool_input":{"command":"grep -rn force docs/"}}'

echo "regra 2 — segredos"
t "git add .env"                    BLOQUEIA '{"tool_name":"Bash","tool_input":{"command":"git add .env"}}'
t "escrever .env"                   BLOQUEIA '{"tool_name":"Write","tool_input":{"file_path":".env"}}'
t "escrever config/.env.local"      BLOQUEIA '{"tool_name":"Write","tool_input":{"file_path":"config/.env.local"}}'

echo "regra 3 — superficie de outra frente (dado real das branches humanize/*)"
alvo="$(git branch -r --list 'origin/humanize/*' 'origin/governanca/*' 2>/dev/null \
        | tr -d ' ' | while read -r b; do [ -n "$b" ] && git diff --name-only "origin/main...$b" 2>/dev/null; done \
        | grep -v '^$' | head -1)"
if [ -n "$alvo" ]; then
  t "editar $alvo"                  BLOQUEIA "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"$alvo\"},\"cwd\":\"$RAIZ\"}"
  t "editar o mesmo por caminho absoluto" BLOQUEIA "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"$RAIZ/$alvo\"},\"cwd\":\"$RAIZ\"}"
else
  echo "  (pulado: nenhuma branch humanize/* ou governanca/* com diff hoje)"
fi
t "editar ficha comum"              permite  "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"fichamentos/Donmez2008.md\"},\"cwd\":\"$RAIZ\"}"

echo "regra 4 — arquivo gerado"
t "editar AGENTS.md"                BLOQUEIA '{"tool_name":"Edit","tool_input":{"file_path":"AGENTS.md"}}'
t "editar CLAUDE.md"                permite  '{"tool_name":"Edit","tool_input":{"file_path":"CLAUDE.md"}}'

echo "robustez — o guarda falha em ABERTO"
t "json invalido"                   permite  'isto nao e json'
t "evento sem tool_input"           permite  '{"tool_name":"Bash"}'
t "ferramenta desconhecida"         permite  '{"tool_name":"WebFetch","tool_input":{"url":"x"}}'

echo
if [ $falhas -eq 0 ]; then echo "guarda: TODOS os testes passam"; exit 0
else echo "guarda: $falhas teste(s) FALHARAM"; exit 1; fi
