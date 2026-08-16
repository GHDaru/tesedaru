#!/usr/bin/env python3
"""check-bib — validação executável do referencias.bib (LOTE 0 do bib-fix).

Dono do arquivo: revisor1 (protocolo §5 — scripts/ tem dono por arquivo).
Tarefa: coordenacao/caixa/20260816-1849_principal_revisor1_tarefa_bibfix-lote0-e-lote2
Origem dos critérios: docs/parecer-auditoria-bib.md §5 (DoD verificável do
ciclo de correção) — transforma o julgamento da banca em checagem de máquina,
como manda o princípio IX da constituição da tese (skill verifiable-dod).

O que checa (cada achado sai como ERRO ou AVISO):

  ERRO  titulo-duplicado    mesmo título (normalizado) em chaves distintas
  ERRO  chave-duplicada     a mesma chave definida duas vezes no .bib
  ERRO  citada-ausente      chave citada num .tex e sem entrada no .bib
  ERRO  campo-key           campo `key = {...}` (resíduo; o parecer pede zero)
  ERRO  nota-de-trabalho    `note` com texto de trabalho, que VAZA para as
                            Referências impressas (ex.: "Year set to 2025 as
                            per the citation"); notas bibliográficas legítimas
                            ("Texto em chinês…", "Conjunto de dados…") passam
  ERRO  sem-identificador   entrada CITADA com year >= 2020 sem doi, eprint,
                            url nem isbn — regra do DoD do parecer

  AVISO orfa               entrada no .bib que nenhum .tex cita

Por que `orfa` não derruba a checagem por padrão: hoje são 217 de 369
entradas. Uma bibliografia pode legitimamente guardar obras ainda não citadas,
e um script cronicamente vermelho deixa de ser gate — vira ruído. Use
--strict-orfas para exigir zero (o item (d) "e vice-versa" da tarefa).

Uso:
    python3 scripts/check-bib.py                  # texto legível
    python3 scripts/check-bib.py --json           # saída de máquina
    python3 scripts/check-bib.py --strict-orfas   # órfãs também derrubam

Saída: 0 = sem erros · 1 = pelo menos um erro · 2 = erro de uso.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

_RAIZ = Path(__file__).resolve().parents[1]

# Fontes de citação: capítulos, apêndices e pré-textuais.
GLOBS_TEX = ("*/texto.tex", "0-iniciais/*.tex", "principal.tex")

# Campos que servem como identificador resolvível da obra.
IDENTIFICADORES = ("doi", "eprint", "url", "isbn", "archiveprefix")

# Marcadores de NOTA DE TRABALHO. Conservador de propósito: só dispara no que
# é inequivocamente recado de bastidor, porque `note` legítimo é comum.
PADROES_NOTA_TRABALHO = (
    r"year set to",
    r"as per the citation",
    r"corresponds to arxiv submission",
    r"\ba confirmar\b",
    r"metadados parciais",
    r"\bto ?do\b",
    r"\bfixme\b",
    r"\bpreencher\b",
    r"conforme solicitad",
    r"gerad[oa] por",
    r"n[ãa]o foi poss[íi]vel",
    r"^arxiv:\s*\S+$",          # note que só repete o eprint
)


def normalizar_titulo(bruto: str) -> str:
    """Título comparável: sem LaTeX, sem acento, sem pontuação, minúsculo.

    Os acentos deste .bib vêm como escape NÃO-alfabético (`{\\'I}`, `{\\~a}`) ou
    como comando de um argumento (`{\\c c}`, `\\c{c}`). Eles são resolvidos para a
    letra-base ANTES de qualquer outra limpeza, e as chaves somem sem virar
    espaço — senão `Edi{\\c c}{\\~a}o` viraria "edi c a o" e nunca casaria com
    "edicao", deixando passar título duplicado (defeito pego pelo fixture)."""
    texto = bruto
    texto = re.sub(r"\{\\[a-zA-Z]+\s+([a-zA-Z])\}", r"\1", texto)   # {\c c} -> c
    texto = re.sub(r"\\[a-zA-Z]+\s*\{([a-zA-Z])\}", r"\1", texto)   # \c{c}  -> c
    texto = re.sub(r"\{\\[^a-zA-Z\s]\s*([a-zA-Z])\}", r"\1", texto)  # {\'I} -> I
    texto = re.sub(r"\\[^a-zA-Z\s]\s*([a-zA-Z])", r"\1", texto)     # \'e    -> e
    texto = re.sub(r"\\[a-zA-Z]+\s*", " ", texto)                   # \emph, \url
    texto = texto.replace("{", "").replace("}", "")                 # {BERT} -> BERT
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^0-9a-zA-Z]+", " ", texto)
    return " ".join(texto.lower().split())


def ler_entradas(caminho: Path) -> list[dict]:
    """Parser de .bib por profundidade de chaves — aguenta entrada numa linha
    só e entrada multilinha, os dois formatos que este arquivo usa."""
    texto = caminho.read_text(encoding="utf-8")
    entradas = []
    for m in re.finditer(r"@([a-zA-Z]+)\s*\{", texto):
        tipo = m.group(1).lower()
        if tipo in {"comment", "preamble", "string"}:
            continue
        i = m.end()
        profundidade = 1
        while i < len(texto) and profundidade:
            if texto[i] == "{":
                profundidade += 1
            elif texto[i] == "}":
                profundidade -= 1
            i += 1
        corpo = texto[m.end():i - 1]
        chave, _, resto = corpo.partition(",")
        entradas.append({
            "tipo": tipo,
            "chave": chave.strip(),
            "linha": texto.count("\n", 0, m.start()) + 1,
            "campos": extrair_campos(resto),
        })
    return entradas


def extrair_campos(corpo: str) -> dict[str, str]:
    """Campos `nome = {valor}` ou `nome = "valor"`, respeitando aninhamento."""
    campos: dict[str, str] = {}
    for m in re.finditer(r"(\w+)\s*=\s*", corpo):
        nome = m.group(1).lower()
        i = m.end()
        if i >= len(corpo):
            break
        if corpo[i] in "{\"":
            fecha = "}" if corpo[i] == "{" else "\""
            abre = corpo[i]
            profundidade, i, inicio = 1, i + 1, i + 1
            while i < len(corpo) and profundidade:
                if corpo[i] == abre and abre == "{":
                    profundidade += 1
                elif corpo[i] == fecha:
                    profundidade -= 1
                i += 1
            campos[nome] = corpo[inicio:i - 1].strip()
        else:                                   # valor solto (ex.: year = 2019)
            fim = corpo.find(",", i)
            campos[nome] = corpo[i:fim if fim > 0 else len(corpo)].strip()
    return campos


def ler_citacoes(raiz: Path) -> dict[str, list[str]]:
    """Chave citada -> lista de 'arquivo:linha' onde ela aparece."""
    ocorrencias: dict[str, list[str]] = defaultdict(list)
    vistos: set[Path] = set()
    for padrao in GLOBS_TEX:
        for arquivo in sorted(raiz.glob(padrao)):
            if arquivo in vistos:
                continue
            vistos.add(arquivo)
            texto = arquivo.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(
                    r"\\(?:no)?cite[a-zA-Z]*\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}", texto):
                linha = texto.count("\n", 0, m.start()) + 1
                for chave in m.group(1).split(","):
                    chave = chave.strip()
                    if chave:
                        ocorrencias[chave].append(
                            f"{arquivo.relative_to(raiz)}:{linha}")
    return ocorrencias


def checar(raiz: Path) -> list[dict]:
    bib = raiz / "referencias.bib"
    entradas = ler_entradas(bib)
    citacoes = ler_citacoes(raiz)
    citadas = set(citacoes)
    achados: list[dict] = []

    def achado(nivel, codigo, chave, mensagem, onde):
        achados.append({"nivel": nivel, "codigo": codigo, "chave": chave,
                        "mensagem": mensagem, "onde": onde})

    # (a) títulos duplicados entre chaves distintas + chaves duplicadas
    por_titulo: dict[str, list[dict]] = defaultdict(list)
    por_chave: dict[str, list[dict]] = defaultdict(list)
    for e in entradas:
        por_chave[e["chave"]].append(e)
        titulo = e["campos"].get("title", "")
        if titulo:
            por_titulo[normalizar_titulo(titulo)].append(e)

    for chave, iguais in sorted(por_chave.items()):
        if len(iguais) > 1:
            achado("erro", "chave-duplicada", chave,
                   f"chave definida {len(iguais)}x",
                   ", ".join(f"referencias.bib:{i['linha']}" for i in iguais))

    for titulo, iguais in sorted(por_titulo.items()):
        chaves = sorted({i["chave"] for i in iguais})
        if len(chaves) > 1:
            achado("erro", "titulo-duplicado", " + ".join(chaves),
                   f"mesmo título em {len(chaves)} chaves: \"{titulo[:70]}\"",
                   ", ".join(f"referencias.bib:{i['linha']}" for i in iguais))

    for e in entradas:
        chave, campos, onde = e["chave"], e["campos"], f"referencias.bib:{e['linha']}"

        # (c) resíduos de anotação
        if "key" in campos:
            achado("erro", "campo-key", chave,
                   f"campo key = {{{campos['key']}}} (o parecer pede zero)", onde)
        nota = campos.get("note", "")
        if nota:
            achatada = " ".join(normalizar_titulo(nota).split())
            for padrao in PADROES_NOTA_TRABALHO:
                if re.search(padrao, achatada):
                    achado("erro", "nota-de-trabalho", chave,
                           f"note vaza recado de trabalho: \"{nota[:70]}\"", onde)
                    break

        # (b) identificador resolvível nas entradas citadas e recentes
        if chave in citadas:
            ano = re.search(r"\d{4}", campos.get("year", ""))
            if ano and int(ano.group()) >= 2020 and not any(
                    campo in campos for campo in IDENTIFICADORES):
                achado("erro", "sem-identificador", chave,
                       f"citada ({campos.get('year')}) sem doi/eprint/url/isbn",
                       f"{onde} · citada em {citacoes[chave][0]}")

    # (d) citada e ausente / presente e nunca citada
    definidas = {e["chave"] for e in entradas}
    for chave in sorted(citadas - definidas):
        achado("erro", "citada-ausente", chave,
               "citada na tese e ausente do referencias.bib",
               ", ".join(citacoes[chave][:3]))
    for chave in sorted(definidas - citadas):
        e = por_chave[chave][0]
        achado("aviso", "orfa", chave, "entrada nunca citada nos .tex",
               f"referencias.bib:{e['linha']}")

    return achados


def main() -> int:
    ap = argparse.ArgumentParser(description="Valida o referencias.bib da tese.")
    ap.add_argument("--json", action="store_true", help="saída de máquina")
    ap.add_argument("--strict-orfas", action="store_true",
                    help="entradas nunca citadas também derrubam a checagem")
    ap.add_argument("--raiz", default=str(_RAIZ), help="raiz do repositório")
    args = ap.parse_args()

    raiz = Path(args.raiz)
    if not (raiz / "referencias.bib").exists():
        print(f"erro: {raiz}/referencias.bib não encontrado", file=sys.stderr)
        return 2

    achados = checar(raiz)
    erros = [a for a in achados if a["nivel"] == "erro"]
    avisos = [a for a in achados if a["nivel"] == "aviso"]
    falhou = bool(erros) or (args.strict_orfas and bool(avisos))

    if args.json:
        print(json.dumps({"ok": not falhou, "erros": len(erros),
                          "avisos": len(avisos), "achados": achados},
                         ensure_ascii=False, indent=2))
        return 1 if falhou else 0

    for nivel, titulo, lista in (("erro", "ERROS", erros),
                                 ("aviso", "AVISOS", avisos)):
        if not lista:
            continue
        print(f"\n=== {titulo} ({len(lista)}) ===")
        for a in lista:
            print(f"[{a['codigo']}] {a['chave']}\n    {a['mensagem']}\n    {a['onde']}")

    print(f"\n{'FALHOU' if falhou else 'OK'} — {len(erros)} erro(s), "
          f"{len(avisos)} aviso(s)"
          f"{'' if args.strict_orfas else ' (órfãs não derrubam; use --strict-orfas)'}")
    return 1 if falhou else 0


if __name__ == "__main__":
    raise SystemExit(main())
