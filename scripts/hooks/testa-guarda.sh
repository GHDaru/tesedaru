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

echo "regra 3 — superficie de outra frente (fixture proprio, nao dado vivo)"
# Por que fixture: depois da lista de superadas, a regra 3 pode ficar SEM dado
# real (hoje so as duas cap2-* tinham diff, e as duas estao na lista). Um teste
# que depende do dado vivo passa a ser pulado em silencio justamente quando a
# regra deixa de ser exercitada — foi assim que um defeito real escapou antes.
FIX="$(mktemp -d)"; trap 'rm -rf "$FIX"' EXIT
(
  set -e
  cd "$FIX"
  git init -q .; git config user.email t@t; git config user.name t
  mkdir -p coordenacao
  echo base > alvo-listada.tex; echo base > alvo-viva.tex
  git add -A; git commit -qm base
  git update-ref refs/remotes/origin/main HEAD

  git checkout -q -b humanize/listada
  echo mudou > alvo-listada.tex; git commit -qam listada
  git update-ref refs/remotes/origin/humanize/listada HEAD

  git checkout -q --detach refs/remotes/origin/main
  git checkout -q -b humanize/viva
  echo mudou > alvo-viva.tex; git commit -qam viva
  git update-ref refs/remotes/origin/humanize/viva HEAD

  git checkout -q --detach refs/remotes/origin/main
  printf '{"superadas":[{"branch":"humanize/listada","ponta":"%s"}]}\n' \
    "$(git rev-parse refs/remotes/origin/humanize/listada)" \
    > coordenacao/branches-superadas.json
) >/dev/null 2>&1
if [ -f "$FIX/coordenacao/branches-superadas.json" ]; then
  t "branch NA lista -> edicao liberada"   permite  "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"alvo-listada.tex\"},\"cwd\":\"$FIX\"}"
  t "branch FORA da lista -> bloqueia"     BLOQUEIA "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"alvo-viva.tex\"},\"cwd\":\"$FIX\"}"
  t "o mesmo por caminho absoluto"         BLOQUEIA "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"$FIX/alvo-viva.tex\"},\"cwd\":\"$FIX\"}"
  t "arquivo que nenhuma branch toca"      permite  "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"nada.tex\"},\"cwd\":\"$FIX\"}"
  rm -f "$FIX/coordenacao/branches-superadas.json"
  rm -f "$FIX/.git/guarda-superficies.cache"
  t "lista AUSENTE -> volta a bloquear"    BLOQUEIA "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"alvo-listada.tex\"},\"cwd\":\"$FIX\"}"
  echo 'isto nao e json' > "$FIX/coordenacao/branches-superadas.json"
  rm -f "$FIX/.git/guarda-superficies.cache"
  t "lista ILEGIVEL -> nao libera nada"    BLOQUEIA "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"alvo-listada.tex\"},\"cwd\":\"$FIX\"}"
else
  printf "  FALHA %-45s fixture nao pode ser montado\n" "regra 3"
  falhas=$((falhas+1))
fi
t "editar ficha comum (repo real)"  permite  "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"fichamentos/Donmez2008.md\"},\"cwd\":\"$RAIZ\"}"
t "2-fundam/texto.tex destravado"   permite  "{\"tool_name\":\"Edit\",\"tool_input\":{\"file_path\":\"2-fundam/texto.tex\"},\"cwd\":\"$RAIZ\"}"

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
