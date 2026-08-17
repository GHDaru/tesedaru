#!/usr/bin/env python3
"""Todo caminho de arquivo citado no plano de revisão tem de resolver no disco.

Dono: revisor1.

POR QUE ISTO EXISTE
-------------------
Em 2026-08-17 o `plano-revisao.json` afirmou, por **nove horas**, que o R4 do
tema t4 estava concluído "em `docs/r4-cap2-t4-afirmacoes.md`" — um arquivo que
**nunca existiu em commit nenhum**. O trabalho tinha sido feito e commitado em
`3401cf5`, mas um force-push desanexou o commit; ele virou *dangling* e o
caminho citado passou a apontar para o nada.

Ninguém percebeu porque o plano é lido como texto, não como referência
resolvível. Um artefato citado e inalcançável é, para quem lê, indistinguível
de um artefato inexistente — e o princípio V existe justamente para não deixar
afirmação sem artefato rastreável. Aqui o que estava sem lastro era um
**status**, não uma medida, o que é pior: status errado redireciona trabalho
alheio (o principal me redespachou um R4 já feito).

O QUE ELE FAZ
-------------
Varre recursivamente o JSON do plano, extrai qualquer coisa que se pareça com
caminho de arquivo do repositório e verifica se existe. Reporta os que faltam,
com o campo em que apareceram, e sai com código 1.

LIMITES DECLARADOS
------------------
1. **Exige barra**: só trata como referência o que tem `/` (`docs/x.md`). Um
   nome solto em prosa ("o `decisoes.jsonl` registra…") é MENÇÃO, não
   referência, e acusá-lo enche o relatório de ruído. Primeira versão deste
   script não fazia isso e devolveu 15 acusações no plano real, das quais 9
   eram exatamente esse caso.
2. Reconhece por extensão conhecida (`.md`, `.json`, `.py`, `.tex`, `.sh`,
   `.jsonl`, `.csv`, `.yaml`, `.yml`). Caminho sem extensão escapa.
3. Ignora URLs e trechos com curinga (`*`) ou reticências (`…`) na vizinhança —
   ali o texto descreve um conjunto, não aponta um arquivo.
4. Caminhos de OUTRO repositório (ex.: `activelearning/...`) são reportados à
   parte, porque a ausência aqui não prova ausência lá.
5. Não valida âncoras internas (seção, linha) — só existência. É detector de
   referência QUEBRADA, não de referência desatualizada.
"""
from __future__ import annotations

import json
import os
import re
import sys

EXTENSOES = (".md", ".json", ".jsonl", ".py", ".tex", ".sh", ".csv", ".yaml", ".yml")

# `docs/foo.md`, scripts/bar.py, 2-fundam/texto.tex — com ou sem crase.
_CAMINHO = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./\-]*(?:" + "|".join(re.escape(e) for e in EXTENSOES) + r")\b")


def _percorrer(no, trilha=""):
    """Gera (trilha, texto) para cada string dentro do JSON."""
    if isinstance(no, dict):
        for k, v in no.items():
            yield from _percorrer(v, f"{trilha}.{k}" if trilha else str(k))
    elif isinstance(no, list):
        for i, v in enumerate(no):
            yield from _percorrer(v, f"{trilha}[{i}]")
    elif isinstance(no, str):
        yield trilha, no


# Repositórios irmãos: ausência aqui não prova ausência lá.
OUTROS_REPOS = ("activelearning/",)

# Campos que descrevem artefato FUTURO por definição. Acusá-los seria erro de
# semântica: "resultado_esperado" é justamente o que ainda não existe.
CAMPOS_FUTUROS = ("resultado_esperado", "resultado_previsto", "saida_esperada")


def varrer(raiz: str, plano: str) -> list[dict]:
    with open(plano, encoding="utf-8") as f:
        dados = json.load(f)
    faltando: list[dict] = []
    vistos: set[tuple[str, str]] = set()
    for trilha, texto in _percorrer(dados):
        if any(c in trilha for c in CAMPOS_FUTUROS):
            continue
        if "http" in texto:
            texto = re.sub(r"https?://\S+", " ", texto)
        for m in _CAMINHO.finditer(texto):
            caminho = m.group(0)
            # (1) sem barra = menção em prosa, não referência
            if "/" not in caminho:
                continue
            # (3) curinga/reticências na VIZINHANÇA: o texto descreve um
            # conjunto. Olhar o entorno, não só o trecho casado — o `*` de
            # `specs/*/qa-report.md` fica fora do casamento.
            janela = texto[max(0, m.start() - 30):m.end() + 5]
            if "*" in janela or "…" in janela or "..." in janela:
                continue
            chave = (trilha, caminho)
            if chave in vistos:
                continue
            vistos.add(chave)
            if os.path.exists(os.path.join(raiz, caminho)):
                continue
            faltando.append({
                "campo": trilha,
                "caminho": caminho,
                "outro_repo": caminho.startswith(OUTROS_REPOS),
            })
    return faltando


def main() -> int:
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    plano = os.path.join(raiz, "docs/records/plano-revisao.json")
    if not os.path.exists(plano):
        print(f"plano não encontrado: {plano}")
        return 2
    faltando = varrer(raiz, plano)
    if not faltando:
        print("artefatos citados no plano: todos resolvem")
        return 0
    proprios = [d for d in faltando if not d["outro_repo"]]
    alheios = [d for d in faltando if d["outro_repo"]]
    if proprios:
        print(f"PROBLEMAS ({len(proprios)}) — caminho citado no plano que NÃO existe:")
        for d in proprios:
            print(f"  {d['caminho']}")
            print(f"     citado em: {d['campo']}")
    if alheios:
        print(f"\nOUTRO REPOSITÓRIO ({len(alheios)}) — não verificável daqui:")
        for d in alheios:
            print(f"  {d['caminho']}  (campo: {d['campo']})")
    return 1 if proprios else 0


if __name__ == "__main__":
    raise SystemExit(main())
