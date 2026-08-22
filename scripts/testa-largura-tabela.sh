#!/usr/bin/env bash
# DoD executavel do check-largura-tabela.py (principio IX: criterio vira
# checagem, nao juizo). Rode depois de QUALQUER mexida no verificador.
# Exit 0 = todos passam.
#
# Os casos sinteticos vivem num diretorio temporario com um repositorio git
# proprio: o modo regressao precisa de duas revisoes reais para comparar, e
# depender do repositorio de verdade tornaria o teste refem do estado da main.
# O ultimo bloco, esse sim, roda contra o dado REAL — foi testar so no
# sintetico que deixou um defeito passar no guarda, em 2026-08-21.
set -uo pipefail
cd "$(dirname "$0")/.."
V="$(pwd)/scripts/check-largura-tabela.py"
falhas=0

t() { # descricao | esperado (SINALIZA|limpo) | diretorio | args...
  # Roda a COPIA que vive dentro de $dir, nunca a do repositorio: o
  # verificador faz chdir para a raiz do proprio arquivo, entao chamar o do
  # repositorio faria todo caso sintetico medir a tese de verdade — e passar
  # em silencio. Foi exatamente o que aconteceu na primeira versao deste teste.
  local desc="$1" esperado="$2" dir="$3"; shift 3
  ( cd "$dir" && python3 "$dir/scripts/check-largura-tabela.py" "$@" ) >/dev/null 2>&1
  local rc=$?
  local obtido; [ $rc -eq 1 ] && obtido=SINALIZA || obtido=limpo
  if [ "$obtido" = "$esperado" ]; then
    printf "  ok   %-50s %s\n" "$desc" "$obtido"
  else
    printf "  FALHA %-49s obtido=%s esperado=%s\n" "$desc" "$obtido" "$esperado"
    falhas=$((falhas+1))
  fi
}

FIX="$(mktemp -d)"; trap 'rm -rf "$FIX"' EXIT
mkdir -p "$FIX/scripts"; cp "$V" "$FIX/scripts/"

escreve() { # arquivo | spec | linhas...
  local arq="$1" spec="$2"; shift 2
  { echo "\\begin{table}"; echo "\\label{tab:$(basename "$arq" .tex)}"
    echo "\\begin{tabular}{$spec}"; printf '%s\n' "$@"
    echo "\\end{tabular}"; echo "\\end{table}"; } > "$FIX/$arq"
}

echo "colunas livres x colunas com largura declarada"
escreve estreita.tex "ll" "A & B \\\\" "CC & DD \\\\"
t "tabela curta"                       limpo    "$FIX" estreita.tex
escreve larga.tex "ll" \
  "$(printf 'A%.0s' {1..70}) & $(printf 'B%.0s' {1..70}) \\\\"
t "tabela larga (140 > orcamento)"     SINALIZA "$FIX" larga.tex
escreve pfixo.tex "p{5cm}p{5cm}" \
  "$(printf 'A%.0s' {1..70}) & $(printf 'B%.0s' {1..70}) \\\\"
t "mesma largura, mas colunas p{} -> pulada"  limpo "$FIX" pfixo.tex
escreve tabx.tex "XX" \
  "$(printf 'A%.0s' {1..70}) & $(printf 'B%.0s' {1..70}) \\\\"
t "colunas X de tabularx -> pulada"    limpo    "$FIX" tabx.tex
escreve mista.tex "lp{4cm}" \
  "$(printf 'A%.0s' {1..70}) & $(printf 'B%.0s' {1..70}) \\\\"
t "so a coluna livre conta na mista"   limpo    "$FIX" mista.tex --orcamento 100

echo "o que ocupa espaco e o texto composto, nao a marcacao"
escreve ref.tex "ll" "A & Secao~\\ref{$(printf 's%.0s' {1..120})} \\\\"
t "rotulo gigante de \\ref nao infla"  limpo    "$FIX" ref.tex
escreve neg.tex "ll" "A & $(printf 'X%.0s' {1..120}) \\\\"
t "texto real do mesmo tamanho infla"  SINALIZA "$FIX" neg.tex
escreve bold.tex "ll" "\\textbf{$(printf 'A%.0s' {1..120})} & B \\\\"
t "argumento de \\textbf CONTA"        SINALIZA "$FIX" bold.tex
escreve mc.tex "ll" "\\multicolumn{2}{l}{$(printf 'A%.0s' {1..140})}\\\\" "A & B \\\\"
t "linha \\multicolumn ignorada"       limpo    "$FIX" mc.tex

echo "modo regressao (duas revisoes reais de um repo proprio)"
( cd "$FIX" && git init -q . && git config user.email t@t && git config user.name t \
  && git add -A && git commit -qm base ) >/dev/null 2>&1
escreve estreita.tex "ll" "AAAAAAAAAA & BBBBBBBBBB \\\\" "CC & DD \\\\"
t "crescimento de 2 para 10 (x5)"      SINALIZA "$FIX" estreita.tex --base HEAD
t "sem --base, o mesmo arquivo passa"  limpo    "$FIX" estreita.tex
( cd "$FIX" && git checkout -q -- estreita.tex )
t "sem mudanca, regressao limpa"       limpo    "$FIX" estreita.tex --base HEAD

echo "dado REAL do repositorio (nao so fixture)"
if git rev-parse --verify -q 206fbdd^1 >/dev/null; then
  t "Tabela 3.1 de hoje estoura o orcamento" SINALIZA "$(pwd)" 3-metodo/texto.tex
  t "e cresceu contra o pre-Fase 2"          SINALIZA "$(pwd)" 3-metodo/texto.tex --base 206fbdd^1
else
  echo "  (pulado: revisao 206fbdd nao alcancavel neste clone)"
fi

echo
if [ $falhas -eq 0 ]; then echo "largura de tabela: TODOS os testes passam"; exit 0
else echo "largura de tabela: $falhas teste(s) FALHARAM"; exit 1; fi
