#!/usr/bin/env python3
"""Três checagens do referencias.bib em FUNÇÃO PURA, para integração ao check-bib.

Dono: revisor1. Entregue ao revisor2 na reconciliação da tarefa 20260817-0505,
nos termos que ele aceitou (proposta 20260817-0402 §3, itens a-d).

O QUE ESTÁ AQUI E POR QUÊ
-------------------------
1. `titulos_duplicados`  — a mesma obra cadastrada sob duas chaves, com títulos
   que só diferem em acento, comando LaTeX, caixa ou pontuação. Complementa a
   checagem de DOI repetido: pega a duplicata quando UMA das entradas não tem
   DOI, que é justamente quando a de DOI não pega.
2. `entradas_orfas`      — entrada que ninguém cita E que não está ancorada por
   fichamento nem por alvo de relação. Não é erro: é candidata a remoção, e por
   isso deve ser AVISO, nunca erro que derruba (foi assim que a regra "matar
   órfã", aplicada cegamente, quase matou Sener2018 e Shen2018).
3. `campos_key_residuais` — corrige o FALSO NEGATIVO que o revisor2 achou: a
   implementação atual ancora o padrão em início de linha (`^\\s*key\\s*=`), e
   várias entradas do nosso bib estão escritas numa linha só (Goudjil2018,
   Roy2001, Cohn1996, Hanneke2015...). Nessas, um `key = {...}` residual passa
   despercebido. Reproduzido antes de corrigir: entrada de uma linha com
   `key = {residuo}` sai "PROBLEMAS: nenhum".

CONTRATO
--------
Toda função recebe texto (e, quando precisa, conjuntos já calculados pelo
chamador) e devolve `list[dict]` com pelo menos `codigo` e `detalhe`. Nenhuma
lê disco, nenhuma imprime, nenhuma decide severidade — quem integra decide se
o código vira erro ou aviso.

Códigos: `titulo-duplicado`, `orfa`, `key-residual`.
"""
from __future__ import annotations

import re
import unicodedata

# Comandos de acento LaTeX que envolvem UMA letra: {\'I} -> I, {\c c} -> c.
_ACENTO_CHAVE = re.compile(r"\{\\[a-zA-Z]{1,2}\s*\{?([a-zA-Z])\}?\}")
_ACENTO_SOLTO = re.compile(r"\\[a-zA-Z]{1,2}\s*\{([a-zA-Z])\}")
_ACENTO_SIMBOLO = re.compile(r"\\[`'^\"~=.]\s*\{?([a-zA-Z])\}?")


def normalizar_titulo(bruto: str) -> str:
    """Reduz um título à forma comparável.

    As chaves são removidas SEM inserir espaço: `{LLM}s` tem de virar `llms`,
    não `llm s`. Foi o defeito que o fixture pegou na primeira versão desta
    função, antes de ela ir para o repositório.
    """
    texto = _ACENTO_CHAVE.sub(r"\1", bruto)
    texto = _ACENTO_SOLTO.sub(r"\1", texto)
    texto = _ACENTO_SIMBOLO.sub(r"\1", texto)
    texto = re.sub(r"\\[a-zA-Z]+", " ", texto)      # comandos restantes: separam
    texto = texto.replace("{", "").replace("}", "")  # chaves: NÃO separam
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^\w\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip().lower()


def _corpo_das_entradas(texto: str) -> list[tuple[str, str]]:
    """[(chave, corpo)] contando chaves — aceita entrada em uma linha só."""
    saida: list[tuple[str, str]] = []
    for m in re.finditer(r"@\w+\{\s*([^,\s]+)\s*,", texto):
        i = texto.index("{", m.start())
        profundidade = 0
        for j in range(i, len(texto)):
            if texto[j] == "{":
                profundidade += 1
            elif texto[j] == "}":
                profundidade -= 1
                if profundidade == 0:
                    saida.append((m.group(1), texto[i + 1 : j]))
                    break
    return saida


def _campo(corpo: str, nome: str) -> str | None:
    """Lê um campo contando chaves — `title = {A {LLM} survey}` sai inteiro."""
    m = re.search(rf"(?:^|[{{,\s]){nome}\s*=\s*", corpo, re.I)
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
        return resto[1 : resto.index('"', 1)]
    return resto.split(",")[0].strip()


def titulos_duplicados(texto: str) -> list[dict]:
    """Chaves distintas cujo título normalizado coincide."""
    por_titulo: dict[str, list[str]] = {}
    for chave, corpo in _corpo_das_entradas(texto):
        titulo = _campo(corpo, "title")
        if not titulo:
            continue
        normalizado = normalizar_titulo(titulo)
        if normalizado:
            por_titulo.setdefault(normalizado, []).append(chave)
    achados = []
    for titulo, chaves in sorted(por_titulo.items()):
        if len(chaves) > 1:
            achados.append({
                "codigo": "titulo-duplicado",
                "chaves": sorted(chaves),
                "detalhe": f"mesmo titulo em {len(chaves)} chaves: "
                           f"{', '.join(sorted(chaves))} -> \"{titulo}\"",
            })
    return achados


def entradas_orfas(texto: str, citadas: set[str], ancoradas: set[str]) -> list[dict]:
    """Entradas que ninguém cita e que nada ancora.

    `ancoradas` deve chegar JÁ contendo os alvos de relação — é o conjunto que
    o check-bib atual monta como `ancoradas |= set(alvos)`. Órfã é candidata a
    remoção, não defeito: quem integra deve tratá-la como aviso.
    """
    achados = []
    for chave, _ in _corpo_das_entradas(texto):
        if chave not in citadas and chave not in ancoradas:
            achados.append({
                "codigo": "orfa",
                "chave": chave,
                "detalhe": f"entrada nunca citada e sem fichamento nem relacao: {chave}",
            })
    return achados


def campos_key_residuais(texto: str) -> list[dict]:
    """Campo `key = {...}` residual, que confunde o BibTeX.

    Correção do falso negativo: o padrão exige que `key` esteja em fronteira de
    CAMPO (precedido de `{` ou `,`), e não em início de linha. Assim vale
    também para entrada escrita numa linha só. `keywords = {...}` não casa,
    porque a fronteira exige `=` logo depois de `key`.
    """
    achados = []
    for chave, corpo in _corpo_das_entradas(texto):
        for m in re.finditer(r"[{,]\s*key\s*=", corpo, re.I):
            achados.append({
                "codigo": "key-residual",
                "chave": chave,
                "detalhe": f"campo 'key = {{...}}' residual em {chave} "
                           f"(posicao {m.start()} do corpo)",
            })
        # o primeiro campo da entrada não é precedido de vírgula
        if re.match(r"\s*key\s*=", corpo, re.I):
            achados.append({
                "codigo": "key-residual",
                "chave": chave,
                "detalhe": f"campo 'key = {{...}}' residual em {chave} (primeiro campo)",
            })
    return achados
