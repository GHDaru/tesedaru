#!/usr/bin/env python3
"""Checagem executável dos fichamentos (princípios I, II e IX da constituição).

Dono: revisor2 (ciclo de consolidação da revisão paralela pós-R6).

Transforma em comando o que antes era julgamento ("o fichamento está bem
preenchido?"). Verifica, para cada `fichamentos/*.md` (o `_TEMPLATE.md` e o
`_VOCABULARIO.md` ficam de fora, assim como as subpastas de leitura cruzada):

  1. front-matter YAML válido e `id` igual ao nome do arquivo;
  2. `falco_relation` presente e não vazia (regra da skill `fichamento`: paper
     que não toca a tese não precisava ser fichado);
  3. toda entidade declarada em proposes/uses_methods/datasets/metrics/tasks/
     models existe no vocabulário controlado (`_VOCABULARIO.md`);
  4. todo alvo de relação paper→paper (extends/compares_with/contradicts/
     builds_on) é uma chave existente em `referencias.bib` — evita aresta para
     nó inexistente no grafo;
  5. a chave do fichamento existe em `referencias.bib` e o PDF declarado em
     `pdf:` existe no repositório;
  6. toda linha de claim (`| C<n> |`) tem evidência localizável preenchida —
     a coluna de evidência não pode estar vazia nem ser o placeholder do
     template.

Desde a ADR 0012 (referência canônica) verifica também o lado do `.bib`:

  7. REFERÊNCIA CANÔNICA — entrada citada na tese e sem fichamento é
     classificada por `livro OU ano < 2010`. Sendo canônica, a ADR dispensa o
     fichamento mas EXIGE entrada correta: os campos mínimos do tipo precisam
     estar lá (`author` ou `editor`, `title`, `year` e o veículo). Falta de
     campo mínimo é VIOLAÇÃO — foi assim que a `Krause2014` chegou ao texto
     com três campos inventados.

E emite dois AVISOS que NÃO reprovam a execução (a lista existente é grande e
um critério que nasce vermelho vira DoD inalcançável — lição do lote 5):

  A1. citada, sem fichamento e NÃO canônica: pendência real de fichamento;
  A2. ÓRFÃ — no `.bib`, não citada em nenhum `.tex`, sem fichamento e sem ser
      alvo de relação. Ninguém a usa, então nenhum invariante a olhava: era o
      ponto cego por onde `Wu2022` e `Ahmed2023` ficaram no repositório com
      metadados fabricados, disponíveis para alguém citar por engano.

Uso:
  python3 scripts/check-fichamentos.py            # todos
  python3 scripts/check-fichamentos.py A B C      # só as chaves dadas
  python3 scripts/check-fichamentos.py --sem-avisos   # esconde A1/A2

Exit 0 = tudo verde; exit 1 = imprime cada violação com arquivo e campo.
Requer pyyaml: `uv run --with pyyaml python scripts/check-fichamentos.py`
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FICH = ROOT / "fichamentos"
BIB = ROOT / "referencias.bib"
CAMPOS_ENTIDADE = ["proposes", "uses_methods", "datasets", "metrics", "tasks", "models"]
CAMPOS_RELACAO = ["extends", "compares_with", "contradicts", "builds_on"]
PLACEHOLDERS = {"", "§, tab., p.", "§, tab, p.", "seção/tabela/página"}

# ADR 0012: canônica = livro (em qualquer forma) ou obra anterior a 2010.
TIPOS_LIVRO = {"book", "inbook", "incollection"}
ANO_CANONICO = 2010
# Campo mínimo por tipo. `author` aceita `editor` no lugar — coletânea como a
# Chapelle2006 não tem autor único, e reprovar isso seria falso positivo.
CAMPOS_MINIMOS = {
    "article": {"author", "title", "year", "journal"},
    "inproceedings": {"author", "title", "year", "booktitle"},
    "conference": {"author", "title", "year", "booktitle"},
    "incollection": {"author", "title", "year", "booktitle"},
    "book": {"author", "title", "year", "publisher"},
    "inbook": {"author", "title", "year", "publisher"},
    "techreport": {"author", "title", "year", "institution"},
    "phdthesis": {"author", "title", "year", "school"},
    "mastersthesis": {"author", "title", "year", "school"},
}
CAMPOS_MINIMOS_PADRAO = {"author", "title", "year"}


def termos_canonicos() -> set[str]:
    """Termos do vocabulário: tudo que aparece em listas separadas por vírgula
    ou sozinho na linha, ignorando comentários HTML e cabeçalhos markdown."""
    texto = (FICH / "_VOCABULARIO.md").read_text(encoding="utf-8")
    texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    termos: set[str] = set()
    for linha in texto.splitlines():
        if linha.startswith(("#", ">", "|")) or not linha.strip():
            continue
        for parte in linha.split(","):
            t = parte.strip().strip(".").lower()
            if t and " " not in t and re.fullmatch(r"[a-z0-9][a-z0-9\-\._]*", t):
                termos.add(t)
    return termos


def chaves_bib() -> set[str]:
    return set(entradas_bib())


def entradas_bib() -> dict[str, dict]:
    """Cada entrada do .bib com tipo, ano e o conjunto de campos declarados."""
    texto = BIB.read_text(encoding="utf-8", errors="replace")
    marcas = list(re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", texto))
    entradas: dict[str, dict] = {}
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        bloco = texto[m.start():fim]
        ano = re.search(r"\byear\s*=\s*[{\"]?\s*(\d{4})", bloco)
        entradas[m.group(2)] = {
            "tipo": m.group(1).lower(),
            "ano": int(ano.group(1)) if ano else None,
            "campos": campos_declarados(bloco),
        }
    return entradas


def campos_declarados(bloco: str) -> set[str]:
    """Nomes de campo de uma entrada .bib, independente de formatação.

    Não dá para exigir campo no início da linha: metade do arquivo tem a
    entrada inteira em UMA linha (`@article{Cohn1996, author = {...}, ...}`) e
    a regra ancorada reprovava entradas perfeitas. Também não dá para varrer
    `\\w+ =` no texto cru, porque um título ou uma nota podem conter sinal de
    igual. Então primeiro esvazia-se o conteúdo entre chaves (com aninhamento)
    e só depois se leem os nomes de campo do esqueleto que sobra.
    """
    esqueleto, profundidade = [], 0
    for ch in bloco[bloco.find("{") + 1:]:      # pula o `@tipo{`
        if ch == "{":
            profundidade += 1
        elif ch == "}":
            profundidade = max(0, profundidade - 1)
        elif profundidade == 0:
            esqueleto.append(ch)
    return {c.lower() for c in re.findall(r"(\w+)\s*=", "".join(esqueleto))}


def chaves_citadas() -> set[str]:
    """Toda chave que aparece em qualquer \\cite* dos .tex do repositório."""
    citadas: set[str] = set()
    for tex in ROOT.rglob("*.tex"):
        if ".git" in tex.parts:
            continue
        conteudo = tex.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\\[a-zA-Z]*cite[a-zA-Z]*\s*(?:\[[^\]]*\])*\s*\{([^}]*)\}", conteudo):
            for chave in m.group(1).split(","):
                if chave.strip():
                    citadas.add(chave.strip())
    return citadas


def e_canonica(entrada: dict) -> bool:
    """ADR 0012: livro em qualquer forma, ou obra anterior a 2010."""
    ano = entrada["ano"]
    return entrada["tipo"] in TIPOS_LIVRO or (ano is not None and ano < ANO_CANONICO)


def campos_faltando(entrada: dict) -> list[str]:
    exigidos = CAMPOS_MINIMOS.get(entrada["tipo"], CAMPOS_MINIMOS_PADRAO)
    declarados = set(entrada["campos"])
    if "editor" in declarados:            # coletânea: editor faz as vezes de autor
        declarados.add("author")
    return sorted(exigidos - declarados)


def main() -> int:
    argumentos = [a for a in sys.argv[1:] if a != "--sem-avisos"]
    mostrar_avisos = "--sem-avisos" not in sys.argv[1:]
    canon = termos_canonicos()
    entradas = entradas_bib()
    bibkeys = set(entradas)
    alvos = argumentos
    arquivos = sorted(p for p in FICH.glob("*.md") if not p.name.startswith("_"))
    if alvos:
        arquivos = [p for p in arquivos if p.stem in alvos]
    problemas: list[str] = []

    for path in arquivos:
        texto = path.read_text(encoding="utf-8")
        partes = texto.split("---")
        if len(partes) < 3:
            problemas.append(f"{path.name}: sem front-matter delimitado por ---")
            continue
        try:
            fm = yaml.safe_load(partes[1]) or {}
        except yaml.YAMLError as e:
            problemas.append(f"{path.name}: YAML inválido ({e})")
            continue

        if str(fm.get("id", "")) != path.stem:
            problemas.append(f"{path.name}: id='{fm.get('id')}' != nome do arquivo")
        if not fm.get("falco_relation"):
            problemas.append(f"{path.name}: falco_relation vazia (obrigatória)")
        if path.stem not in bibkeys:
            problemas.append(f"{path.name}: chave ausente em referencias.bib")
        pdf = str(fm.get("pdf") or "")
        if pdf and not (ROOT / pdf).exists():
            problemas.append(f"{path.name}: pdf declarado não existe ({pdf})")

        for campo in CAMPOS_ENTIDADE:
            for termo in (fm.get(campo) or []):
                if str(termo).strip().lower() not in canon:
                    problemas.append(
                        f"{path.name}: {campo} usa '{termo}', fora do _VOCABULARIO.md")
        for campo in CAMPOS_RELACAO:
            for alvo in (fm.get(campo) or []):
                if str(alvo).strip() not in bibkeys:
                    problemas.append(
                        f"{path.name}: {campo} aponta '{alvo}', sem entrada no bib")

        for linha in texto.splitlines():
            if re.match(r"^\|\s*C\d+\s*\|", linha):
                celulas = [c.strip() for c in linha.strip("|").split("|")]
                if len(celulas) < 3 or celulas[2].lower() in PLACEHOLDERS:
                    problemas.append(
                        f"{path.name}: claim {celulas[0]} sem evidência localizável")

    # ---- lado do .bib: canônicas, pendências e órfãs (ADR 0012 + aviso 0247)
    fichadas = {p.stem for p in FICH.glob("*.md") if not p.name.startswith("_")}
    alvos_relacao: set[str] = set()
    for path in FICH.glob("*.md"):
        if path.name.startswith("_"):
            continue
        partes = path.read_text(encoding="utf-8").split("---")
        if len(partes) < 3:
            continue
        try:
            fm = yaml.safe_load(partes[1]) or {}
        except yaml.YAMLError:
            continue
        for campo in CAMPOS_RELACAO:
            for alvo in (fm.get(campo) or []):
                alvos_relacao.add(str(alvo).strip())

    citadas = chaves_citadas()
    pendentes: list[str] = []
    orfas: list[str] = []
    for chave, entrada in sorted(entradas.items()):
        if chave in fichadas:
            continue
        if chave in citadas:
            if e_canonica(entrada):
                falta = campos_faltando(entrada)
                if falta:                      # invariante 7: canônica mal declarada
                    problemas.append(
                        f"referencias.bib:{chave}: canônica (ADR 0012) sem campo mínimo "
                        f"{falta} para tipo '{entrada['tipo']}'")
            else:
                pendentes.append(chave)
        elif chave not in alvos_relacao:
            orfas.append(chave)

    print(f"fichamentos verificados: {len(arquivos)}")
    if mostrar_avisos and not alvos:
        print(f"AVISO A1 — citadas, sem fichamento e não canônicas ({len(pendentes)}): "
              f"{', '.join(pendentes) if pendentes else 'nenhuma'}")
        print(f"AVISO A2 — órfãs no bib, ninguém cita nem referencia ({len(orfas)}): "
              f"{', '.join(orfas) if orfas else 'nenhuma'}")
        print("        (avisos NÃO reprovam; viram pendência de trabalho, não de build)")
    if problemas:
        print(f"PROBLEMAS ({len(problemas)}):")
        for p in problemas:
            print(f"  - {p}")
        return 1
    print("PROBLEMAS: nenhum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
