#!/usr/bin/env python3
"""Teste de fixture do check-bib: prova que cada classe de erro dispara.

Dono do arquivo: revisor1. Monta repositórios .bib/.tex/.md sintéticos num
diretório temporário e verifica o veredito — nenhum julgamento humano no meio
(princípio IX / skill verifiable-dod).

    python3 scripts/test-check-bib.py

POR QUE ELE É CAIXA-PRETA (reescrito em 2026-08-17, tarefa 20260817-0505)
-------------------------------------------------------------------------
A versão anterior importava `check-bib.py` e chamava `checar(raiz)`, uma API
que só existia na implementação do lote 0. No gate final do bib as duas
implementações colidiram (add/add) e sobreviveu a do revisor2, que faz tudo
dentro de `main()` imprimindo strings — não há função a chamar. O teste ficou
quebrado, acusando `AttributeError`, o que é pior do que não ter teste: parece
cobertura e não é.

A saída era ou reescrever o arquivo do revisor2 (superfície dele) ou testar
pelo comportamento observável. Escolhi o segundo: copio o script para uma raiz
temporária — ele deriva a raiz do próprio caminho — rodo como subprocesso e
traduzo as mensagens impressas em códigos. Funciona com a implementação de
hoje e continua funcionando se ela ganhar uma API amanhã.

LACUNAS REGISTRADAS COMO TESTE
------------------------------
A implementação do lote 0 tinha duas checagens que a sobrevivente não tem:
`titulo-duplicado` (mesma obra sob duas chaves com títulos que só diferem em
acento, LaTeX ou caixa) e `orfa` (entrada nunca citada e sem fichamento). Elas
estão marcadas abaixo como LACUNA, com o caso que as dispararia. Enquanto a
reconciliação não acontecer, o teste é o registro executável dessa dívida —
não uma reprovação.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SCRIPT = AQUI / "check-bib.py"

# mensagem impressa -> código estável, para o teste não depender da redação
PADROES = [
    (r"^chave duplicada no bib:", "chave-duplicada"),
    (r"^fichamento sem entrada no bib:", "fichamento-sem-entrada"),
    (r"^alvo de relacao sem entrada no bib:", "alvo-de-relacao"),
    (r"^mesmo DOI em \d+ chaves:", "doi-repetido"),
    (r"^citada mas ausente do bib:", "citada-ausente"),
    (r"^chave morta pelo bib-fix voltou a ser citada:", "chave-morta"),
    (r"^campo note com res", "nota-de-modelo"),
    (r"^campo 'key = ", "key-residual"),
    (r"^citada, year=\d+, sem doi nem url:", "sem-identificador"),
]

LIMPO = """
@article{Limpo2021,
  author = {Silva, Ana},
  title  = {Um titulo qualquer},
  year   = {2021},
  doi    = {10.1000/xyz}
}
"""

falhas: list[str] = []
CASOS: list[str] = []


def rodar(bib: str, tex: str = r"\citep{Limpo2021}", fichas: dict[str, str] | None = None) -> set[str]:
    """Monta um repositório sintético, roda o script e devolve os códigos."""
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp)
        (raiz / "scripts").mkdir()
        shutil.copy(SCRIPT, raiz / "scripts" / "check-bib.py")
        # O script deixou de ser um arquivo só: desde a integração do ciclo 011
        # ele IMPORTA `checagens_extra_bib`. Copiar apenas o `check-bib.py`
        # fazia todos os casos estourarem em ImportError — e um teste que
        # falha por não montar o ambiente acusa o script errado. Levar os
        # módulos irmãos junto mantém a caixa-preta funcionando antes e depois
        # do merge, sem que este arquivo precise saber QUAIS são as importações.
        for irmao in AQUI.glob("*.py"):
            if irmao.name not in ("check-bib.py", Path(__file__).name):
                shutil.copy(irmao, raiz / "scripts" / irmao.name)
        (raiz / "referencias.bib").write_text(bib, encoding="utf-8")
        (raiz / "1-intro").mkdir()
        (raiz / "1-intro" / "texto.tex").write_text(tex, encoding="utf-8")
        pasta = raiz / "fichamentos"
        pasta.mkdir()
        for nome, corpo in (fichas or {}).items():
            (pasta / nome).write_text(corpo, encoding="utf-8")
        saida = subprocess.run(
            [sys.executable, str(raiz / "scripts" / "check-bib.py")],
            capture_output=True, text=True,
        ).stdout
        codigos: set[str] = set()
        for linha in saida.splitlines():
            linha = linha.strip().lstrip("- ").strip()
            for padrao, codigo in PADROES:
                if re.match(padrao, linha):
                    codigos.add(codigo)
        return codigos


def caso(nome: str, codigos: set[str], espera: str, deve_estar: bool = True) -> None:
    CASOS.append(nome)
    ok = (espera in codigos) if deve_estar else (espera not in codigos)
    print(f"[{'PASS' if ok else 'FAIL'}] {nome}"
          f" ({'achou' if espera in codigos else 'não achou'} {espera})")
    if not ok:
        falhas.append(nome)


def lacuna(nome: str, codigos: set[str], codigo: str) -> None:
    """Checagem que a implementação sobrevivente ainda não tem.

    Não conta como falha: registra a dívida da reconciliação. No dia em que a
    checagem entrar, esta linha vira PASS sozinha e deve ser promovida a caso().
    """
    entrou = codigo in codigos
    print(f"[{'RESOLVIDA' if entrou else 'LACUNA'}] {nome} ({codigo})")


ficha = lambda alvo: (
    "---\nid: Ficha\nextends: []\ncompares_with: []\n"
    f"contradicts: []\nbuilds_on: [{alvo}]\n---\ncorpo\n"
)

# 1. bib limpo e citado: nada dispara
codigos = rodar(LIMPO)
caso("bib limpo não acusa chave ausente", codigos, "citada-ausente", False)
caso("bib limpo não acusa falta de identificador", codigos, "sem-identificador", False)
caso("bib limpo não acusa chave duplicada", codigos, "chave-duplicada", False)

# 2. chave citada que não existe no bib
caso("citada e ausente do bib", rodar(LIMPO, r"\citep{NaoExiste2020}"), "citada-ausente")

# 3. a mesma chave cadastrada duas vezes
caso("chave duplicada no bib", rodar(LIMPO + LIMPO), "chave-duplicada")

# 4. entrada citada, de 2020 em diante, sem doi nem url
caso("citada pós-2020 sem identificador", rodar("""
@article{Sem2021,
  author = {Silva, Ana},
  title  = {Sem identificador},
  year   = {2021}
}
""", r"\citep{Sem2021}"), "sem-identificador")

# 5. o mesmo corte não vale para obra anterior a 2020
caso("clássico sem identificador não é acusado", rodar("""
@article{Velho1995,
  author = {Silva, Ana},
  title  = {Obra classica},
  year   = {1995}
}
""", r"\citep{Velho1995}"), "sem-identificador", False)

# 6. chave morta pelo bib-fix reaparecendo na prosa
caso("chave morta voltou a ser citada", rodar(LIMPO + """
@article{Su2023,
  author = {Xiao, Ruixuan},
  title  = {Obra},
  year   = {2023},
  doi    = {10.1000/abc}
}
""", r"\citep{Limpo2021, Su2023}"), "chave-morta")

# 7. resíduo de conversa de modelo de linguagem vazando para o note
caso("note com resíduo de modelo", rodar(LIMPO + """
@article{Vaza2021,
  author = {Silva, Ana},
  title  = {Obra},
  year   = {2021},
  doi    = {10.1000/def},
  note   = {As an AI language model, I cannot verify this reference}
}
""", r"\citep{Limpo2021, Vaza2021}"), "nota-de-modelo")

# 8. campo `key = {...}` residual, que confunde o BibTeX
caso("campo key residual", rodar("""
@article{ComKey2021,
  author = {Silva, Ana},
  title  = {Obra},
  year   = {2021},
  doi    = {10.1000/ghi},
  key    = {residuo}
}
""", r"\citep{ComKey2021}"), "key-residual")

# 9. invariante do DOI repetido: a mesma obra sob duas chaves
caso("mesmo DOI em duas chaves", rodar(LIMPO + """
@article{Clone2021,
  author = {Silva, Ana},
  title  = {Outro titulo},
  year   = {2021},
  doi    = {10.1000/XYZ}
}
""", r"\citep{Limpo2021, Clone2021}"), "doi-repetido")

# 10. o mesmo invariante não pode acusar DOIs distintos
caso("DOIs distintos não acusam", rodar(LIMPO + """
@article{Outro2021,
  author = {Souza, Bruno},
  title  = {Outro titulo},
  year   = {2021},
  doi    = {10.1000/abc}
}
""", r"\citep{Limpo2021, Outro2021}"), "doi-repetido", False)

# 11. invariante do alvo de relação: aresta pendurada é violação
caso("alvo de relação sem entrada no bib",
     rodar(LIMPO, fichas={"Ficha.md": ficha("Fantasma2010")}),
     "alvo-de-relacao")

# 12. e alvo de relação que EXISTE no bib não é acusado
caso("alvo de relação existente não acusa",
     rodar(LIMPO, fichas={"Ficha.md": ficha("Limpo2021")}),
     "alvo-de-relacao", False)

# 13. fichamento cuja chave não está no bib
caso("fichamento sem entrada no bib",
     rodar(LIMPO, fichas={"Orfao2019.md": "---\nid: Orfao2019\n---\ncorpo\n"}),
     "fichamento-sem-entrada")

# 14. entrada ancorada por fichamento não é órfã mesmo sem \cite
caso("entrada só com fichamento não vira 'ausente'",
     rodar(LIMPO, tex="sem citacao aqui",
           fichas={"Limpo2021.md": "---\nid: Limpo2021\n---\ncorpo\n"}),
     "citada-ausente", False)

# --- lacunas da reconciliação (tarefa 20260817-0505) ---
lacuna("título duplicado sob chaves distintas", rodar(LIMPO + """
@article{Outro2021,
  author = {Souza, Bruno},
  title  = {UM T{\\'I}TULO   qualquer},
  year   = {2021},
  doi    = {10.1000/jkl}
}
""", r"\citep{Limpo2021, Outro2021}"), "titulo-duplicado")

lacuna("entrada nunca citada e sem fichamento",
       rodar(LIMPO + """
@article{Ninguem2021,
  author = {Silva, Ana},
  title  = {Obra que ninguem cita},
  year   = {2021},
  doi    = {10.1000/mno}
}
""", r"\citep{Limpo2021}"), "orfa")

print()
if falhas:
    print(f"FALHOU — {len(falhas)} caso(s): {', '.join(falhas)}")
    raise SystemExit(1)
print(f"PASS — 0 falha(s) em {len(CASOS)} casos (mais 2 lacunas registradas)")
