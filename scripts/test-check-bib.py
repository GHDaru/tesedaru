#!/usr/bin/env python3
"""Teste de fixture do check-bib: prova que cada classe de erro dispara.

Dono do arquivo: revisor1. Monta repositórios .bib/.tex sintéticos num
diretório temporário e verifica o veredito — nenhum julgamento humano no meio
(princípio IX / skill verifiable-dod). Rode:  python3 scripts/test-check-bib.py
"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "check_bib", Path(__file__).resolve().parent / "check-bib.py")
check_bib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_bib)

LIMPO = """
@article{Limpo2021,
  author = {Silva, Ana},
  title  = {Um titulo qualquer},
  year   = {2021},
  doi    = {10.1000/xyz}
}
"""

falhas: list[str] = []


def rodar(bib: str, tex: str = r"\citep{Limpo2021}") -> set[str]:
    """Devolve os códigos de achado para um par .bib/.tex sintético."""
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp)
        (raiz / "referencias.bib").write_text(bib, encoding="utf-8")
        (raiz / "1-intro").mkdir()
        (raiz / "1-intro/texto.tex").write_text(tex, encoding="utf-8")
        return {a["codigo"] for a in check_bib.checar(raiz)}


def caso(nome: str, codigos: set[str], espera: str, deve_estar: bool = True) -> None:
    ok = (espera in codigos) if deve_estar else (espera not in codigos)
    print(f"[{'PASS' if ok else 'FAIL'}] {nome}"
          f" ({'achou' if espera in codigos else 'não achou'} {espera})")
    if not ok:
        falhas.append(nome)


# 1. bib limpo e citado: nenhum erro, nenhuma órfã
codigos = rodar(LIMPO)
caso("bib limpo não acusa título duplicado", codigos, "titulo-duplicado", False)
caso("bib limpo não acusa órfã", codigos, "orfa", False)
caso("bib limpo não acusa falta de identificador", codigos, "sem-identificador", False)

# 2. título duplicado em chaves distintas (acentos/LaTeX/caixa não enganam)
caso("título duplicado", rodar(LIMPO + """
@article{Outra2021,
  author = {Souza, Bruno},
  title  = {UM T{\\'I}TULO   qualquer},
  year   = {2021},
  doi    = {10.1000/abc}
}
"""), "titulo-duplicado")

# 3. mesma chave definida duas vezes
caso("chave duplicada", rodar(LIMPO + LIMPO), "chave-duplicada")

# 4. citada na tese e ausente do bib
caso("citada ausente", rodar(LIMPO, r"\citep{Limpo2021,Fantasma2020}"),
     "citada-ausente")

# 5. entrada no bib que ninguém cita
caso("órfã", rodar(LIMPO + """
@book{NuncaCitado1999,
  author = {Autor, Um},
  title  = {Obra nao citada},
  year   = {1999}
}
"""), "orfa")

# 6. campo key residual
caso("campo key", rodar("""
@inproceedings{ComKey2021,
  key    = {ResiduoAntigo},
  author = {Silva, Ana},
  title  = {Outro titulo},
  year   = {2021},
  doi    = {10.1000/k}
}
""", r"\citep{ComKey2021}"), "campo-key")

# 7. note de trabalho vaza; note bibliográfico legítimo NÃO acusa
caso("nota de trabalho", rodar("""
@misc{Trabalho2025,
  author = {Silva, Ana},
  title  = {Titulo com nota},
  year   = {2025},
  eprint = {2502.00000},
  note   = {Year set to 2025 as per the citation, corresponds to arXiv submission date.}
}
""", r"\citep{Trabalho2025}"), "nota-de-trabalho")
caso("nota bibliográfica legítima passa", rodar("""
@article{Legitimo2021,
  author = {Silva, Ana},
  title  = {Titulo com nota legitima},
  year   = {2021},
  doi    = {10.1000/n},
  note   = {Texto em chines; versao em ingles disponivel como arXiv:1905.11590}
}
""", r"\citep{Legitimo2021}"), "nota-de-trabalho", deve_estar=False)

# 8. identificador: exigido na citada recente, dispensado na antiga e na não citada
caso("citada recente sem identificador", rodar("""
@article{Recente2023,
  author = {Silva, Ana},
  title  = {Sem identificador},
  year   = {2023}
}
""", r"\citep{Recente2023}"), "sem-identificador")
caso("citada antiga sem identificador não acusa", rodar("""
@article{Antiga1999,
  author = {Silva, Ana},
  title  = {Antiga sem identificador},
  year   = {1999}
}
""", r"\citep{Antiga1999}"), "sem-identificador", deve_estar=False)

# 9. \cite com opções e multi-chave é lido corretamente
caso("cite com opções e múltiplas chaves", rodar(
    LIMPO, r"\citep[cf.][p.~3]{Limpo2021,Fantasma2020}"), "citada-ausente")

print(f"\n{'FALHOU' if falhas else 'PASS'} — {len(falhas)} falha(s)"
      + (f": {', '.join(falhas)}" if falhas else " em 12 casos"))
sys.exit(1 if falhas else 0)
