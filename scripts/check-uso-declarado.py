#!/usr/bin/env python3
"""Confronta o USO DECLARADO nos fichamentos com a citação REAL nos capítulos.

Dono: revisor1.

O PROBLEMA QUE ISTO RESOLVE
---------------------------
Todo fichamento traz uma tabela de claims cuja última coluna é "Uso na tese":
uma promessa explícita de onde aquele claim deve entrar ("Cap. 5", "Cap.2",
"Capítulo 6"). Essa promessa é escrita no momento da leitura do artigo, que é
quando se sabe o que a obra sustenta — e depois ninguém volta para conferir se
ela foi cumprida.

Duas classes de defeito nascem daí, e nenhuma aparece na saída em PDF:

1. `promessa-nao-cumprida` — a ficha diz "usar no Cap. 5" e a chave NÃO é
   citada em `5-*/texto.tex`. A leitura já pagou o custo de descobrir o que a
   obra sustenta, e a tese não colheu. É a varredura que eu propus como
   "o que cada obra fichada sustenta ALÉM de onde já é citada", só que na
   forma executável em vez de juízo.

2. `citada-sem-promessa` — a chave é citada num capítulo que a ficha não
   previu. NÃO é defeito por si: pode ser uso legítimo descoberto depois. Sai
   como AVISO, para leitura humana, nunca como erro.

O QUE ISTO NÃO FAZ, declarado em vez de escondido
-------------------------------------------------
- Não lê o CONTEÚDO do claim: não sabe dizer se a citação que existe sustenta
  aquele claim específico. Só sabe dizer se a chave aparece no capítulo
  prometido. É detector de ausência, não de adequação.
- Não entende "Cap. 2 e 5" com precisão de claim: atribui os dois capítulos ao
  claim inteiro.
- Menções sem número ("Fundamentação", "Método") são ignoradas, porque
  mapeá-las para capítulo seria adivinhação.

Saída: relatório em texto. Sem efeito colateral, sem escrever nada.
"""
from __future__ import annotations

import glob
import os
import re
import sys

# Capítulo -> arquivos que o materializam.
CAPITULOS = {
    1: ["1-intro/texto.tex"],
    2: ["2-fundam/texto.tex"],
    3: ["3-metodo/texto.tex"],
    4: ["4-resultados-l0/texto.tex"],
    5: ["5-resultados-falco/texto.tex"],
    6: ["6-conclusao/texto.tex"],
}

# "Cap. 5", "Cap.2", "Capítulo 6", "cap 3" — o número é o que importa.
_CAP = re.compile(r"cap[íi]?t?u?l?o?\.?\s*~?\s*(\d)", re.I)
# Linha de claim: | C1 | ... | ... | uso |
_LINHA_CLAIM = re.compile(r"^\|\s*(C\d+)\s*\|(.*)$")


def capitulos_citantes(raiz: str) -> dict[str, set[int]]:
    """chave bibtex -> {números de capítulo em que ela é citada}."""
    mapa: dict[str, set[int]] = {}
    for num, arquivos in CAPITULOS.items():
        for rel in arquivos:
            caminho = os.path.join(raiz, rel)
            if not os.path.exists(caminho):
                continue
            texto = open(caminho, encoding="utf-8").read()
            for m in re.finditer(r"\\cite[a-z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", texto):
                for chave in m.group(1).split(","):
                    chave = chave.strip()
                    if chave:
                        mapa.setdefault(chave, set()).add(num)
    return mapa


def promessas(caminho_ficha: str) -> dict[int, list[str]]:
    """capítulo prometido -> [ids de claim que o prometem]."""
    saida: dict[int, list[str]] = {}
    for linha in open(caminho_ficha, encoding="utf-8"):
        m = _LINHA_CLAIM.match(linha.strip())
        if not m:
            continue
        colunas = [c.strip() for c in m.group(2).split("|")]
        if not colunas:
            continue
        uso = colunas[-1] or (colunas[-2] if len(colunas) > 1 else "")
        for num in {int(n) for n in _CAP.findall(uso) if 1 <= int(n) <= 6}:
            saida.setdefault(num, []).append(m.group(1))
    return saida


def varrer(raiz: str) -> tuple[list[dict], list[dict]]:
    citantes = capitulos_citantes(raiz)
    nao_cumpridas: list[dict] = []
    sem_promessa: list[dict] = []
    for ficha in sorted(glob.glob(os.path.join(raiz, "fichamentos", "*.md"))):
        nome = os.path.basename(ficha)
        if nome.startswith("_"):
            continue
        chave = nome[:-3]
        prometidos = promessas(ficha)
        se_cita = citantes.get(chave, set())
        for cap, claims in sorted(prometidos.items()):
            if cap not in se_cita:
                nao_cumpridas.append({
                    # Duas classes MUITO diferentes, e misturá-las afogava o sinal:
                    # a chave que não é citada em lugar NENHUM já é a órfã conhecida
                    # (decisão do autor, ~95 casos); o achado novo é a chave que a
                    # tese USA e cuja ficha promete OUTRO capítulo além daquele.
                    "codigo": "promessa-nao-cumprida" if se_cita else "orfa-ja-conhecida",
                    "chave": chave, "capitulo": cap, "claims": claims,
                    "citada_em": sorted(se_cita),
                })
        for cap in sorted(se_cita - set(prometidos)):
            sem_promessa.append({
                "codigo": "citada-sem-promessa",
                "chave": chave, "capitulo": cap,
                "prometidos": sorted(prometidos),
            })
    return nao_cumpridas, sem_promessa


def main() -> int:
    raiz = sys.argv[1] if len(sys.argv) > 1 else "."
    nao_cumpridas, sem_promessa = varrer(raiz)

    reais = [d for d in nao_cumpridas if d["codigo"] == "promessa-nao-cumprida"]
    orfas = [d for d in nao_cumpridas if d["codigo"] == "orfa-ja-conhecida"]

    print(f"fichamentos com promessa de capítulo: "
          f"{len({d['chave'] for d in nao_cumpridas} | {d['chave'] for d in sem_promessa})}")
    print()
    print(f"== PROMESSA NÃO CUMPRIDA ({len(reais)}) — O ACHADO ==")
    print("   a obra É usada na tese, e a ficha promete OUTRO capítulo além desse")
    for d in sorted(reais, key=lambda x: (-len(x["claims"]), x["chave"])):
        onde = ", ".join(f"Cap.{c}" for c in d["citada_em"])
        print(f"   {d['chave']:28} promete Cap.{d['capitulo']} "
              f"({'/'.join(d['claims'])}) · hoje só em: {onde}")
    print()
    print(f"== ÓRFÃ JÁ CONHECIDA ({len(orfas)}) — não é achado novo ==")
    print("   chave sem citação em capítulo nenhum: é o conjunto das ~95 órfãs,")
    print(f"   cuja remoção é decisão do autor. {len({d['chave'] for d in orfas})} chaves distintas.")
    print()
    print(f"== CITADA SEM PROMESSA ({len(sem_promessa)}) — aviso, não defeito ==")
    for d in sem_promessa:
        print(f"   {d['chave']:32} citada no Cap.{d['capitulo']} "
              f"· ficha prevê: {d['prometidos'] or 'nenhum capítulo'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
