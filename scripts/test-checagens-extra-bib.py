#!/usr/bin/env python3
"""Fixtures das três checagens entregues ao revisor2 para integração.

Dono: revisor1. Companheiro de `scripts/checagens_extra_bib.py`.

    python3 scripts/test-checagens-extra-bib.py

Cada checagem tem, no mínimo, um caso POSITIVO (dispara) e um NEGATIVO (não
dispara no caso legítimo). Sem o negativo, o teste só prova que a função
reclama — não que reclama da coisa certa.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "checagens", Path(__file__).resolve().parent / "checagens_extra_bib.py")
ch = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ch)

falhas: list[str] = []
casos = 0


def caso(nome: str, condicao: bool) -> None:
    global casos
    casos += 1
    print(f"[{'PASS' if condicao else 'FAIL'}] {nome}")
    if not condicao:
        falhas.append(nome)


def codigos(achados) -> set[str]:
    return {a["codigo"] for a in achados}


# ---------------------------------------------------------------- normalização
caso("acento LaTeX em chave não distingue título",
     ch.normalizar_titulo("Um T{\\'i}tulo") == ch.normalizar_titulo("Um Título"))
caso("cedilha em comando de duas letras resolve",
     ch.normalizar_titulo("Aten{\\c c}ao") == ch.normalizar_titulo("Atencao"))
caso("chave NÃO insere espaço no meio da palavra",
     ch.normalizar_titulo("{LLM}s in the loop") == "llms in the loop")
caso("pontuação e caixa não distinguem",
     ch.normalizar_titulo("Deep Learning: A Survey!") == ch.normalizar_titulo("deep learning a survey"))
caso("títulos realmente diferentes continuam diferentes",
     ch.normalizar_titulo("Active learning") != ch.normalizar_titulo("Passive learning"))

# ------------------------------------------------------------ titulo-duplicado
BIB_DUP = """
@article{A2021, author = {Silva, Ana}, title = {Um T{\\'i}tulo   Qualquer}, year = {2021}}
@article{B2021, author = {Souza, Bruno}, title = {um titulo qualquer}, year = {2021}}
"""
achados = ch.titulos_duplicados(BIB_DUP)
caso("título duplicado dispara", "titulo-duplicado" in codigos(achados))
caso("título duplicado nomeia as duas chaves",
     achados and achados[0]["chaves"] == ["A2021", "B2021"])

BIB_NAO_DUP = """
@article{A2021, author = {Silva, Ana}, title = {Aprendizado ativo}, year = {2021}}
@article{B2021, author = {Souza, Bruno}, title = {Aprendizado passivo}, year = {2021}}
"""
caso("títulos distintos não disparam",
     "titulo-duplicado" not in codigos(ch.titulos_duplicados(BIB_NAO_DUP)))

BIB_UMA_LINHA = (
    "@article{A2021, title = {Obra Repetida}, year = {2021}}\n"
    "@article{B2021, title = {obra repetida}, year = {2021}}\n"
)
caso("título duplicado também em entrada de UMA LINHA",
     "titulo-duplicado" in codigos(ch.titulos_duplicados(BIB_UMA_LINHA)))

# ------------------------------------------------------------------------ orfa
BIB_ORFA = """
@article{Citada2021, title = {Obra citada}, year = {2021}}
@article{Fichada2021, title = {Obra fichada}, year = {2021}}
@article{Alvo2021, title = {Alvo de relacao}, year = {2021}}
@article{Ninguem2021, title = {Obra que ninguem usa}, year = {2021}}
"""
achados = ch.entradas_orfas(BIB_ORFA, {"Citada2021"}, {"Fichada2021", "Alvo2021"})
caso("órfã dispara", "orfa" in codigos(achados))
caso("só a órfã de verdade dispara",
     [a["chave"] for a in achados] == ["Ninguem2021"])
caso("entrada citada não é órfã",
     "Citada2021" not in [a["chave"] for a in achados])
caso("entrada ancorada por fichamento não é órfã",
     "Fichada2021" not in [a["chave"] for a in achados])
caso("entrada que é alvo de relação não é órfã",
     "Alvo2021" not in [a["chave"] for a in achados])

# ---------------------------------------------------- key-residual (o falso negativo)
BIB_KEY_LINHAS = """
@article{ComKey2021,
  title = {Obra},
  year  = {2021},
  key   = {residuo}
}
"""
caso("key residual dispara em entrada multilinha",
     "key-residual" in codigos(ch.campos_key_residuais(BIB_KEY_LINHAS)))

# O caso do bug: a implementação anterior ancorava em início de linha e passava.
BIB_KEY_UMA_LINHA = (
    "@article{ComKey2021, title = {Obra}, year = {2021}, key = {residuo} }\n"
)
caso("key residual dispara em entrada de UMA LINHA (regressão do falso negativo)",
     "key-residual" in codigos(ch.campos_key_residuais(BIB_KEY_UMA_LINHA)))

BIB_KEY_PRIMEIRO = "@article{ComKey2021, key = {residuo}, title = {Obra}}\n"
caso("key residual dispara quando é o PRIMEIRO campo",
     "key-residual" in codigos(ch.campos_key_residuais(BIB_KEY_PRIMEIRO)))

BIB_KEYWORDS = (
    "@article{Legitima2021, title = {Obra}, keywords = {active learning}, year = {2021}}\n"
)
caso("keywords NÃO é confundido com key",
     "key-residual" not in codigos(ch.campos_key_residuais(BIB_KEYWORDS)))

BIB_KEY_NO_VALOR = (
    "@article{Legitima2021, title = {Obra}, note = {the key = value pattern}, year = {2021}}\n"
)
caso("'key =' DENTRO de um valor não dispara",
     "key-residual" not in codigos(ch.campos_key_residuais(BIB_KEY_NO_VALOR)))

# O falso POSITIVO que o revisor2 achou em 20260817-0600: o fixture acima usa
# a forma SEM vírgula, e por isso cobria menos do que a afirmação que
# sustentava. Com vírgula antes do `key`, o padrão antigo casava.
BIB_KEY_NO_VALOR_COM_VIRGULA = (
    "@article{Legitima2021, title = {Obra}, note = {ver tabela, key = valor}, year = {2021}}\n"
)
caso("'key =' dentro de um valor COM VÍRGULA antes não dispara (regressão do falso positivo)",
     "key-residual" not in codigos(ch.campos_key_residuais(BIB_KEY_NO_VALOR_COM_VIRGULA)))

# Duas classes que o relato não citava e que o mesmo conserto passa a cobrir.
BIB_KEY_NO_VALOR_ASPAS = (
    '@article{Legitima2021, title = {Obra}, note = "ver tabela, key = valor", year = {2021}}\n'
)
caso("'key =' dentro de valor entre ASPAS não dispara",
     "key-residual" not in codigos(ch.campos_key_residuais(BIB_KEY_NO_VALOR_ASPAS)))

BIB_KEY_NO_VALOR_ANINHADO = (
    "@article{Legitima2021, title = {A {LLM} survey, key = x}, year = {2021}}\n"
)
caso("'key =' dentro de valor com chave ANINHADA não dispara",
     "key-residual" not in codigos(ch.campos_key_residuais(BIB_KEY_NO_VALOR_ANINHADO)))

BIB_KEY_MAIUSCULO = "@article{ComKey2021, title = {Obra}, KEY = {residuo}}\n"
caso("KEY maiúsculo ainda dispara (o conserto não quebrou a insensibilidade a caixa)",
     "key-residual" in codigos(ch.campos_key_residuais(BIB_KEY_MAIUSCULO)))

print()
if falhas:
    print(f"FALHOU — {len(falhas)} de {casos}: {', '.join(falhas)}")
    raise SystemExit(1)
print(f"PASS — 0 falha(s) em {casos} casos")
