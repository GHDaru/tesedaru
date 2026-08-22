#!/usr/bin/env bash
# DoD executavel do check-numero-sem-ficha.py (principio IX: criterio vira
# checagem, nao juizo). Rode depois de QUALQUER mexida no verificador.
# Exit 0 = todos passam.
#
# Os casos vivem num diretorio temporario com fichamentos e capitulos de
# mentira. O ultimo bloco olha o dado REAL, mas so como AVISO: se o autor
# consertar a citacao do Settles, o achado some — e um teste que depende de um
# defeito do momento apodrece. Foi a licao do check-largura-tabela, em 21/08.
set -uo pipefail
cd "$(dirname "$0")/.."
V="$(pwd)/scripts/check-numero-sem-ficha.py"
falhas=0

t() { # descricao | esperado (SINALIZA|limpo) | args...
  local desc="$1" esperado="$2"; shift 2
  # Roda a COPIA de dentro do fixture: o verificador faz chdir para a raiz do
  # proprio arquivo, entao chamar o do repositorio mediria a tese de verdade e
  # passaria em silencio — foi exatamente o defeito da 1a versao do DoD irmao.
  ( cd "$FIX" && python3 "$FIX/scripts/check-numero-sem-ficha.py" --raiz "$FIX" "$@" ) >/dev/null 2>&1
  local rc=$?
  local obtido; [ $rc -eq 1 ] && obtido=SINALIZA || obtido=limpo
  if [ "$obtido" = "$esperado" ]; then
    printf "  ok   %-52s %s\n" "$desc" "$obtido"
  else
    printf "  FALHA %-51s obtido=%s esperado=%s\n" "$desc" "$obtido" "$esperado"
    falhas=$((falhas+1))
  fi
}

FIX="$(mktemp -d)"; trap 'rm -rf "$FIX"' EXIT
mkdir -p "$FIX/scripts" "$FIX/fichamentos" "$FIX/1-cap"
cp "$V" "$FIX/scripts/"

ficha() { # chave | conteudo da secao de numeros ("SEM-SECAO" omite a secao)
  local k="$1" corpo="$2"
  { echo "---"; echo "id: $k"; echo "---"; echo; echo "# $k"; echo
    echo "## Claims relevantes"; echo "| # | Claim |"; echo
    if [ "$corpo" != "SEM-SECAO" ]; then
      echo "## Números que posso citar"; echo "$corpo"; echo
    fi
    echo "## Crítica"; echo "- nada"; } > "$FIX/fichamentos/$k.md"
}
cap() { printf '%s\n' "$@" > "$FIX/1-cap/texto.tex"; }

ficha ComNumero   "- A tabela 3 reporta 15,45% no conjunto CR."
ficha SemNumero   "- (Survey; usar taxonomia, não números.)"
ficha SoRemissao  "- (Ver fichamento Outro2012 — conteúdo idêntico.)"
ficha SemSecao    "SEM-SECAO"

echo "o que o guarda deve pegar"
cap 'Estudos reportam menos de $10\%$ do total \citep{SemNumero}.'
t "percentual em obra sem numero"            SINALIZA 1-cap/texto.tex
cap 'Reporta-se $10\%$ na ilustracao de \citet{SoRemissao} para o caso.'
t "ficha que so REMETE a outra tambem conta" SINALIZA 1-cap/texto.tex

echo "o que o guarda NAO pode pegar"
cap 'A tabela reporta $15{,}45\%$ nos testes \citep{ComNumero}.'
t "percentual em obra COM numero"            limpo    1-cap/texto.tex
cap 'Reporta-se $10\%$ do total \citep{SemSecao}.'
t "ficha sem a secao -> desconhecido"        limpo    1-cap/texto.tex
cap 'Reporta-se $10\%$ do total \citep{SemNumero, ComNumero}.'
t "citacao mista: uma delas pode sustentar"  limpo    1-cap/texto.tex
cap 'Reporta-se $10\%$ do total \citep{Inexistente2020}.'
t "chave sem fichamento nenhum"              limpo    1-cap/texto.tex
cap 'O ganho foi de $10\%$ e por isso o desenho adotado nesta tese separa as tres particoes de forma disjunta, com semente fixa e registrada, antes de qualquer treinamento \citep{SemNumero}.'
t "citacao longe demais (>120 car.)"         limpo    1-cap/texto.tex
cap 'O ganho foi de $10\%$ no experimento.' 'Outra frase discute o metodo \citep{SemNumero}.'
t "numero e citacao em sentencas diferentes" limpo    1-cap/texto.tex
cap 'Foram usados 500 itens no total \citep{SemNumero}.'
t "numero absoluto: fora do escopo"          limpo    1-cap/texto.tex
cap 'Conforme a Tabela~3 do trabalho \citep{SemNumero}, o metodo funciona.'
t "'Tabela 3' nao e' dado"                   limpo    1-cap/texto.tex
cap 'O parametro vale $0{,}01 \cdot B$ conforme o desenho \citep{SemNumero}.'
t "parametro do proprio metodo (sem %)"      limpo    1-cap/texto.tex

echo "as superficies padrao (sem argumento) alcancam o que devem"
# Sem este caso, alguem pode encolher PADROES_PADRAO e o guarda passa a pular
# a defesa EM SILENCIO — o modo de falha mais perigoso de um guarda.
cap 'Nada demais aqui.'
mkdir -p "$FIX/apresentacao" "$FIX/artigos/a9"
echo 'Reporta-se $10\%$ do total \citep{SemNumero}.' > "$FIX/apresentacao/defesa.tex"
t "sem argumento, varre apresentacao/"       SINALIZA
rm -f "$FIX/apresentacao/defesa.tex"
echo 'Reporta-se $10\%$ do total \citep{SemNumero}.' > "$FIX/artigos/a9/main.tex"
t "sem argumento, varre artigos/*/main.tex"  SINALIZA
rm -f "$FIX/artigos/a9/main.tex"
t "sem argumento e sem defeito -> limpo"     limpo

echo "robustez"
rm -rf "$FIX/fichamentos"; mkdir -p "$FIX/fichamentos"
cap 'Reporta-se $10\%$ do total \citep{SemNumero}.'
t "sem fichamento algum -> nao quebra"       limpo    1-cap/texto.tex

echo "dado REAL (apenas AVISO: some quando o autor consertar)"
if python3 "$V" 1-intro/texto.tex >/dev/null 2>&1; then
  echo "  AVISO: o Cap.1 nao acusa mais nada — se a citacao do Settles foi"
  echo "         consertada, otimo; se o guarda parou de ver, e' defeito."
else
  saida="$(python3 "$V" 1-intro/texto.tex 2>&1)"
  echo "$saida" | grep -q "Settles2009" \
    && printf "  ok   %-52s %s\n" "acha o caso real do Cap.1 (Settles/10%%)" "SINALIZA" \
    || { printf "  FALHA %-51s\n" "acusa no Cap.1, mas nao o Settles"; falhas=$((falhas+1)); }
  echo "$saida" | grep -q "Schroder" \
    && { printf "  FALHA %-51s\n" "acusou o Schroder, que TEM numero na ficha"; falhas=$((falhas+1)); } \
    || printf "  ok   %-52s %s\n" "nao acusa o Schroder (tem numero na ficha)" "limpo"
fi

echo
if [ $falhas -eq 0 ]; then echo "numero sem ficha: TODOS os testes passam"; exit 0
else echo "numero sem ficha: $falhas teste(s) FALHARAM"; exit 1; fi
