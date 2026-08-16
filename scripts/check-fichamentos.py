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

Uso:
  python3 scripts/check-fichamentos.py            # todos
  python3 scripts/check-fichamentos.py A B C      # só as chaves dadas

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
    texto = BIB.read_text(encoding="utf-8", errors="replace")
    return set(re.findall(r"^@\w+\{\s*([^,\s]+)\s*,", texto, flags=re.M))


def main() -> int:
    canon, bibkeys = termos_canonicos(), chaves_bib()
    alvos = sys.argv[1:]
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

    print(f"fichamentos verificados: {len(arquivos)}")
    if problemas:
        print(f"PROBLEMAS ({len(problemas)}):")
        for p in problemas:
            print(f"  - {p}")
        return 1
    print("PROBLEMAS: nenhum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
