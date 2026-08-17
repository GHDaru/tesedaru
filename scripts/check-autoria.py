#!/usr/bin/env python3
"""Confere a AUTORIA das entradas do referencias.bib contra a fonte primária.

Dono: revisor1 (arquivo novo; alheio = lock + mensagem, conforme PROTOCOLO §5)

POR QUE ESTE SCRIPT EXISTE
--------------------------
O `check-bib.py` cobre existência de chave, duplicata, identificador e resíduo.
Ele NÃO detecta a falha que a R3 do t4 e do t5 encontraram cinco vezes: a obra
é real, o título está certo, o DOI está presente — e os PRENOMES dos autores
foram inventados, mantendo os sobrenomes. Exemplos confirmados na fonte:

  Ren2021     "Peng Ren"    -> Pengzhen Ren   (+ 1 autor ausente, + DOI que
                                               não resolve)
  EinDor2020  "Lior Ein-Dor"-> Liat Ein-Dor   (7 de 10 prenomes alterados)
  Baykal2021  autor "Oren Gal" que NÃO consta do artigo
  Xu2017      "Xu, Jun"     -> Xu, Jiaming    (+ 1 autor ausente)
  Kowsari2019 "Sanjeet Mendu" -> Sanjana Mendu

Em ABNT os prenomes viram iniciais, então quase nada disso aparece no PDF.
Por isso passa despercebido — e por isso precisa de checagem mecânica: o que
está errado é o REGISTRO, que é o que a tese promete ser auditável
(princípios II e IX da constituição).

CLASSE DE RISCO
---------------
A falha se concentra em entradas com MUITOS AUTORES. Por padrão o script
confere só as entradas citadas nos .tex que tenham DOI e >= 5 autores (use
--todas para varrer tudo o que tiver DOI).

USO
---
    python3 scripts/check-autoria.py                 # classe de risco
    python3 scripts/check-autoria.py --todas         # toda entrada com DOI
    python3 scripts/check-autoria.py --chave Ren2021 # uma entrada

Exit 0 = nenhuma divergência. Exit 1 = imprime cada divergência.

ATENÇÃO AO ARQUIVO: por padrão lê o referencias.bib da árvore atual. Enquanto o
bib-fix não estiver mergeado, use --bib apontando para o arquivo da branch
bibfix/lotes: a main está atrasada, e várias entradas só ganharam DOI lá (sem
DOI, esta checagem não roda e a entrada sai como não-conferida).

REDE: consulta api.crossref.org. Não é para CI — é verificação sob demanda,
a rodar quando se mexe no bib ou ao abrir uma R3. Sem rede, o script avisa e
sai com 0 (ausência de verificação não é reprovação).

DOI de arXiv (10.48550/*) não consta do Crossref: sai como NAO-VERIFICAVEL, para
conferência manual. Já um DOI de prefixo depositável que devolve 404 é DEFEITO e
entra como divergência — foi assim que o Ren2021 apareceu.

LIMITE CONHECIDO: para não acusar "J." contra "Jiaming", o comparador aceita
prenome abreviado (<= 2 caracteres) com a mesma inicial. Isso deixa passar
prenomes curtos e reais trocados por outros de mesma inicial — "Bin" contra
"Bo", no Xu2017, não é acusado. O script reduz o trabalho manual; não o
substitui em entradas com prenomes curtos.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
BIB = RAIZ / "referencias.bib"
UA = "tesedaru-check-autoria/1.0 (mailto:ghdaru@gmail.com)"
MIN_AUTORES = 5


def normalizar(texto: str) -> str:
    """Tira comandos LaTeX, chaves, acentos e caixa — só para COMPARAR."""
    texto = re.sub(r"\\[a-zA-Z]+\s*", "", texto)
    texto = texto.replace("{", "").replace("}", "").replace("~", " ")
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", texto).strip().lower()


def entradas(texto: str) -> dict[str, str]:
    """Chave -> corpo. Aceita entrada em uma linha só (há várias no nosso bib)."""
    achadas: dict[str, str] = {}
    for m in re.finditer(r"@\w+\{\s*([^,\s]+)\s*,", texto):
        i = texto.index("{", m.start())
        profundidade = 0
        for j in range(i, len(texto)):
            if texto[j] == "{":
                profundidade += 1
            elif texto[j] == "}":
                profundidade -= 1
                if profundidade == 0:
                    achadas[m.group(1)] = texto[i + 1 : j]
                    break
    return achadas


def campo(corpo: str, nome: str) -> str | None:
    """Lê um campo contando chaves — títulos com {LLM} quebram regex ingênua."""
    m = re.search(rf"\b{nome}\s*=\s*", corpo, re.I)
    if not m:
        return None
    resto = corpo[m.end() :].lstrip()
    if resto.startswith("{"):
        profundidade = 0
        for j, c in enumerate(resto):
            if c == "{":
                profundidade += 1
            elif c == "}":
                profundidade -= 1
                if profundidade == 0:
                    return resto[1:j]
        return None
    if resto.startswith('"'):
        fim = resto.index('"', 1)
        return resto[1:fim]
    return resto.split(",")[0].strip()


def partir_autores(bruto: str) -> list[tuple[str, str]]:
    """Devolve [(prenome, sobrenome)] normalizados."""
    saida = []
    for pedaco in re.split(r"\s+and\s+", bruto.strip()):
        pedaco = pedaco.strip()
        if not pedaco or normalizar(pedaco) == "others":
            continue
        if "," in pedaco:
            sobrenome, prenome = pedaco.split(",", 1)
        else:
            partes = pedaco.split()
            sobrenome = partes[-1] if partes else ""
            prenome = " ".join(partes[:-1])
        saida.append((normalizar(prenome), normalizar(sobrenome)))
    return saida


def tem_others(bruto: str) -> bool:
    return any(normalizar(p) == "others" for p in re.split(r"\s+and\s+", bruto))


def chaves_citadas() -> set[str]:
    fontes = list(RAIZ.glob("[0-9]-*/texto.tex")) + list(RAIZ.glob("0-*/*.tex"))
    citadas: set[str] = set()
    for caminho in fontes:
        texto = caminho.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"\\[a-zA-Z]*cite[a-zA-Z]*\*?(?:\[[^]]*\])*\{([^}]*)\}", texto):
            citadas.update(c.strip() for c in m.group(1).split(","))
    return {c for c in citadas if c}


# DOIs destes prefixos não são depositados no Crossref; ausência ali é normal.
PREFIXOS_FORA_DO_CROSSREF = ("10.48550/",)


def crossref(doi: str) -> tuple[str, list[tuple[str, str]]]:
    """Devolve (situacao, autores). situacao: 'ok' | 'ausente' | 'rede'.

    'ausente' com prefixo depositável = DOI que não resolve, e isso é DEFEITO,
    não falta de cobertura: foi assim que o Ren2021 apareceu.
    """
    if not doi:
        return "rede", []
    req = urllib.request.Request(
        f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}",
        headers={"User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            dados = json.load(r)["message"]
    except urllib.error.HTTPError as e:
        return ("ausente" if e.code == 404 else "rede"), []
    except (urllib.error.URLError, ValueError, KeyError):
        return "rede", []
    return "ok", [
        (normalizar(a.get("given", "")), normalizar(a.get("family", "")))
        for a in dados.get("author", [])
    ]


def inicial_compativel(nosso: str, fonte: str) -> bool:
    """'Matthew E.' x 'Matthew' e 'J.' x 'Jiaming' NÃO são divergência."""
    if not nosso or not fonte:
        return True
    if nosso.startswith(fonte) or fonte.startswith(nosso):
        return True
    abrevia = len(nosso.replace(".", "").strip()) <= 2 or len(fonte.replace(".", "").strip()) <= 2
    return abrevia and nosso[0] == fonte[0]


def comparar(chave: str, nossos: list, fonte: list, truncada: bool) -> list[str]:
    divergencias = []
    for i, (prenome, sobrenome) in enumerate(nossos):
        if i >= len(fonte):
            divergencias.append(f"  #{i+1} nosso '{prenome} {sobrenome}' não tem par na fonte")
            continue
        f_prenome, f_sobrenome = fonte[i]
        if sobrenome != f_sobrenome:
            divergencias.append(f"  #{i+1} SOBRENOME: nosso '{sobrenome}' × fonte '{f_sobrenome}'")
        elif not inicial_compativel(prenome, f_prenome):
            divergencias.append(
                f"  #{i+1} prenome: nosso '{prenome}' × fonte '{f_prenome}' ({f_sobrenome})"
            )
    if len(fonte) > len(nossos) and not truncada:
        faltam = [f"{g} {f}".strip() for g, f in fonte[len(nossos) :]]
        divergencias.append(f"  faltam {len(faltam)} autor(es): {', '.join(faltam)}")
    return divergencias


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--todas", action="store_true", help="não filtrar pela classe de risco")
    ap.add_argument("--chave", action="append", help="conferir só estas chaves")
    ap.add_argument(
        "--bib",
        default=str(BIB),
        help="qual .bib conferir. IMPORTANTE: enquanto o bib-fix não for mergeado, "
        "aponte para o arquivo da branch bibfix/lotes — a main está atrasada e "
        "diagnosticar contra ela produz achado errado.",
    )
    args = ap.parse_args()

    caminho_bib = Path(args.bib)
    if not caminho_bib.exists():
        print(f"não achei {caminho_bib}", file=sys.stderr)
        return 1

    todas = entradas(caminho_bib.read_text(encoding="utf-8", errors="replace"))
    citadas = chaves_citadas()

    alvos = []
    for chave, corpo in sorted(todas.items()):
        if args.chave and chave not in args.chave:
            continue
        if not args.chave:
            if chave not in citadas:
                continue
            if not args.todas and len(partir_autores(campo(corpo, "author") or "")) < MIN_AUTORES:
                continue
        if campo(corpo, "doi"):
            alvos.append((chave, corpo))

    if not alvos:
        print("nenhuma entrada no escopo pedido.")
        return 0

    problemas: list[str] = []
    nao_verificaveis: list[str] = []
    rede_ok = False

    for chave, corpo in alvos:
        doi = (campo(corpo, "doi") or "").strip()
        bruto = campo(corpo, "author") or ""
        nossos = partir_autores(bruto)
        situacao, fonte = crossref(doi)
        if situacao == "ausente":
            rede_ok = True
            if doi.startswith(PREFIXOS_FORA_DO_CROSSREF):
                nao_verificaveis.append(f"{chave} (doi {doi} — prefixo fora do Crossref)")
            else:
                problemas.append(f"{chave}: DOI {doi} NÃO RESOLVE (404 no Crossref)")
            continue
        if situacao == "rede":
            nao_verificaveis.append(f"{chave} (doi {doi} — não consegui consultar)")
            continue
        rede_ok = True
        if not fonte:
            nao_verificaveis.append(f"{chave} (registro sem autoria no Crossref)")
            continue
        divergencias = comparar(chave, nossos, fonte, tem_others(bruto))
        if divergencias:
            problemas.append(f"{chave}: {len(nossos)} autores no bib × {len(fonte)} na fonte")
            problemas.extend(divergencias)

    if not rede_ok and nao_verificaveis:
        print("sem acesso ao Crossref — nada verificado; ausência de verificação não reprova.")
        return 0

    print(f"conferidas {len(alvos) - len(nao_verificaveis)} entradas contra o Crossref.")
    if nao_verificaveis:
        print(f"\nNÃO-VERIFICÁVEIS ({len(nao_verificaveis)}) — conferir à mão:")
        for item in nao_verificaveis:
            print(f"  - {item}")
    if problemas:
        print(f"\nDIVERGÊNCIAS DE AUTORIA:")
        for linha in problemas:
            print(linha if linha.startswith("  ") else f"\n- {linha}")
        return 1
    print("\nautoria: nenhuma divergência.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
