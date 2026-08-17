#!/usr/bin/env python3
"""Checagem executável do referencias.bib (princípios II e IX da constituição).

Dono: revisor2 (ciclo bib-fix, lotes 1 e 3 — tarefa do principal 2026-08-16).
Integração das checagens do revisor1: ciclo 011, liberado pelo aviso 1135 do
principal (gate @ae332f3).

Transforma o DoD do parecer de auditoria em comandos. Verifica:

  1. toda chave citada em `\\cite*{...}` nos capítulos e apêndices existe no
     `referencias.bib` (evita "citação indefinida" na compilação);
  2. nenhuma chave duplicada no arquivo;
  3. nenhuma chave morta pelo ciclo bib-fix reaparece citada (lista abaixo);
  4. nenhum campo `note` com resíduo de conversa de modelo de linguagem
     (o parecer achou 2 vazando para o PDF);
  5. nenhum campo `key = {...}` residual (artefato que confunde o BibTeX);
  6. toda entrada citada com `year >= 2020` tem `doi` ou `url`;
  7. a mesma obra não está cadastrada sob duas chaves com títulos que só
     diferem em acento, comando LaTeX, caixa ou pontuação (checagem do
     revisor1: pega a duplicata quando UMA das entradas não tem DOI, que é
     justamente quando o item de DOI repetido não pega).

E AVISA (nunca reprova) sobre:

  A1. entrada órfã — ninguém cita, nenhum fichamento a ancora, nenhuma relação
      do grafo a aponta. É candidata a remoção, não defeito. A severidade é
      aviso de propósito: a regra "matar órfã", aplicada cegamente, quase
      matou Sener2018 e Shen2018, e um invariante que nasce vermelho em ~95
      entradas viraria DoD inalcançável.

O item 6 é o critério do DoD §5 do parecer. Entradas não citadas ficam de fora
dele de propósito: o que não é citado não entra no PDF.

DE ONDE VÊM AS CHECAGENS 5, 7 e A1
----------------------------------
De `scripts/checagens_extra_bib.py`, que é do revisor1 e é **importado, não
copiado** — uma função com dois donos é uma função com nenhum. O item 5 era um
FALSO NEGATIVO meu: a versão anterior ancorava o padrão em início de linha
(`^\\s*key\\s*=`), e metade do nosso bib está escrita numa linha só, então um
`key = {...}` residual passava batido. Falso negativo é pior que falso
positivo, porque tem cara de cobertura.

Uso:  python3 scripts/check-bib.py [--sem-avisos]
Exit 0 = nenhum ERRO (avisos não reprovam); exit 1 = imprime cada violação.
Sem dependências externas.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checagens_extra_bib import (  # noqa: E402  (import após ajuste de sys.path)
    campos_key_residuais,
    entradas_orfas,
    titulos_duplicados,
)

ROOT = Path(__file__).resolve().parents[1]

# Chaves removidas pelo ciclo bib-fix — nenhuma pode voltar a ser citada.
MORTAS = {
    "Su2023", "FreeAL2023",        # -> Xiao2023FreeAL
    "Bayer2024", "activellm2024",  # -> Bayer2024ActiveLLM
    "Zhang2025LLMAL",              # -> Zhang2025
    "Yusuf2023",                   # obra fabricada; a real é Riyanto2023Comparative
    "Jung2021",                    # obra fabricada; a real é Nti2021
    # bloco de linha única: fabricadas por sequestro de identificador —
    # o DOI/arXiv declarado resolve, mas para artigo de OUTRA obra/área.
    "Yu2022", "Zhang2020", "Liang2024LLMActive", "Qi2020FLAL",
    # Razali2020: removida em 10cd093 após a checagem `titulo-duplicado` do
    # ciclo 011 a acusar. Copiava o título do Widodo2022 sobre coordenadas de
    # outro artigo (J. Phys. Conf. Ser. 1529(2):022098 = navegação outdoor em
    # AR). Entra aqui por um motivo concreto, não por simetria: o revisor1
    # verificou que ela É CITADA no repositório LEGADO (Tese-Vers-o-Draft), na
    # mesma frase de estratificação, ao lado de Forman2010 e James2013. Texto
    # trazido do rascunho antigo reintroduziria a citação fabricada, e é
    # exatamente isso que esta lista existe para pegar.
    "Razali2020",
}

ERRO = "erro"
AVISO = "aviso"


def fontes_tex(raiz: Path) -> list[Path]:
    """Capítulos, pré-textuais e apêndices — não inclui artigos/ (bib próprio)."""
    return [p for p in raiz.glob("*/texto.tex")] + list((raiz / "0-iniciais").glob("*.tex"))


def checar(raiz: Path) -> list[dict]:
    """Todos os achados do bib de `raiz`, como dados — não imprime, não sai.

    Cada achado é `{"codigo", "detalhe", "severidade"}`. Quem chama decide o
    que fazer; só `severidade == ERRO` deve derrubar build. Esta função existe
    para o verificador ser testável por fixture sem subprocesso e sem tocar no
    repositório real.
    """
    texto = (raiz / "referencias.bib").read_text(encoding="utf-8", errors="replace")
    achados: list[dict] = []

    def erro(codigo: str, detalhe: str) -> None:
        achados.append({"codigo": codigo, "detalhe": detalhe, "severidade": ERRO})

    chaves = re.findall(r"^@\w+\{\s*([^,\s]+)\s*,", texto, flags=re.M)
    vistas: set[str] = set()
    for c in chaves:
        if c in vistas:
            erro("chave-duplicada", f"chave duplicada no bib: {c}")
        vistas.add(c)

    # Chaves ancoradas por fichamento: são nós do grafo de conhecimento e
    # NÃO são órfãs, mesmo sem \cite na prosa — remover uma quebraria o KG e
    # o check-fichamentos.py. (Achado do ciclo bib-fix: a regra "matar órfã"
    # do parecer, aplicada cegamente, mataria Sener2018 e Shen2018.)
    ancoradas = {p.stem for p in (raiz / "fichamentos").glob("*.md")
                 if not p.name.startswith("_")}
    for chave in sorted(ancoradas - vistas):
        erro("fichamento-sem-entrada", f"fichamento sem entrada no bib: {chave}")

    # Invariante acolhido pelo principal em 2026-08-16 (tarefa 20260816-2152):
    # uma chave também está ancorada quando é ALVO DE RELAÇÃO no front-matter
    # de qualquer fichamento, mesmo sem ter fichamento próprio. Sem isto o
    # checador aprova a remoção de uma chave que sustenta aresta do grafo —
    # foi o que aconteceu 3x num dia (Settles2010, Houlsby2011 e o quase-caso
    # do Naseem2021HateSpeech). Alvo de relação que não existe no bib é
    # aresta pendurada e entra como violação.
    alvos: dict[str, str] = {}
    # glob NAO recursivo, de proposito: e o mesmo alcance do build_kg.py
    # (HERE.glob("*.md")). Subpastas como leitura-cruzada-revisor1/ guardam
    # leituras preservadas verbatim, ficam FORA do grafo e por isso suas
    # referencias sao registro historico, nao aresta viva.
    for ficha in (raiz / "fichamentos").glob("*.md"):
        if ficha.name.startswith("_"):
            continue
        corpo = ficha.read_text(encoding="utf-8", errors="replace")
        if not corpo.startswith("---"):
            continue
        frente = corpo.split("---", 2)[1]
        for campo in ("extends", "compares_with", "contradicts", "builds_on"):
            m = re.search(rf"^{campo}:\s*\[([^\]]*)\]", frente, flags=re.M)
            if not m:
                continue
            for alvo in m.group(1).split(","):
                alvo = alvo.strip().strip("'\"")
                if alvo:
                    alvos.setdefault(alvo, ficha.name)
    for chave in sorted(set(alvos) - vistas):
        erro("alvo-sem-entrada",
             f"alvo de relacao sem entrada no bib: {chave} "
             f"(referenciado em {alvos[chave]})")

    # `ancoradas` passa a incluir os alvos: quem consultar esta variavel para
    # decidir remocao ve o conjunto COMPLETO do que sustenta o grafo.
    ancoradas |= set(alvos)

    # DOI repetido = a MESMA obra cadastrada sob duas chaves. Foi o defeito do
    # ciclo em 2 ocorrencias no mesmo dia: ao corrigir metadado fabricado
    # apontando para a obra real, a obra real ja estava no arquivo sob outra
    # chave (Naseem2021 x Naseem2021HateSpeech; Selva2021 x Birunda2021).
    # A regra que faltava: antes de RECONSTRUIR uma entrada, perguntar se a
    # obra corrigida ja existe. Isto verifica isso mecanicamente.
    por_doi: dict[str, list[str]] = {}
    for m in re.finditer(r"@\w+\{\s*([^,\s]+)\s*,", texto):
        chave = m.group(1)
        i, prof = m.end(), 1
        while i < len(texto) and prof:
            if texto[i] == "{":
                prof += 1
            elif texto[i] == "}":
                prof -= 1
            i += 1
        doi = re.search(r"doi\s*=\s*\{([^}]*)\}", texto[m.start():i], re.I)
        if doi:
            por_doi.setdefault(doi.group(1).strip().lower(), []).append(chave)
    for doi, chaves_doi in sorted(por_doi.items()):
        if len(chaves_doi) > 1:
            erro("doi-duplicado",
                 f"mesmo DOI em {len(chaves_doi)} chaves: {doi} -> "
                 f"{', '.join(sorted(chaves_doi))}")

    # Checagem 7 (revisor1): duplicata por TÍTULO normalizado. Complementar à
    # de DOI, e não redundante — pega o par em que uma das entradas não tem DOI.
    for achado in titulos_duplicados(texto):
        erro(achado["codigo"], achado["detalhe"])

    citadas: dict[str, list[str]] = {}
    for path in fontes_tex(raiz):
        conteudo = path.read_text(encoding="utf-8", errors="replace")
        for grupo in re.findall(r"\\[a-zA-Z]*cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", conteudo):
            for chave in (k.strip() for k in grupo.split(",")):
                if chave:
                    citadas.setdefault(chave, []).append(path.name)

    for chave, onde in sorted(citadas.items()):
        if chave not in vistas:
            erro("citada-ausente",
                 f"citada mas ausente do bib: {chave} (em {', '.join(sorted(set(onde)))})")
        if chave in MORTAS:
            erro("chave-morta", f"chave morta pelo bib-fix voltou a ser citada: {chave}")

    if re.search(r"note\s*=\s*\{[^}]*(?:as an AI|language model|I cannot|Não posso|As an AI)", texto, re.I):
        erro("note-residuo-llm", "campo note com resíduo de conversa de modelo de linguagem")

    # Checagem 5, agora pela função do revisor1: fronteira de CAMPO em vez de
    # início de linha, e varredura sobre o esqueleto da entrada (conteúdo dos
    # campos apagado), de modo que um `key =` escrito dentro do TEXTO de um
    # campo não dispara. Substitui o `^\s*key\s*=` que deixava passar entrada
    # de uma linha só.
    for achado in campos_key_residuais(texto):
        erro(achado["codigo"], achado["detalhe"])

    for m in re.finditer(r"^@\w+\{\s*([^,\s]+)\s*,", texto, flags=re.M):
        chave = m.group(1)
        if chave not in citadas:
            continue
        i = m.start(); j = texto.index("{", i); d = 0
        for k in range(j, len(texto)):
            if texto[k] == "{": d += 1
            elif texto[k] == "}":
                d -= 1
                if d == 0:
                    corpo = texto[i:k + 1]; break
        ano = re.search(r"year\s*=\s*\{?\s*(\d{4})", corpo)
        if ano and int(ano.group(1)) >= 2020:
            # sem âncora de linha: há entradas escritas em linha única, em que
            # o campo não começa a linha (falso positivo pego na execução).
            if not re.search(r"[\s,{](doi|url)\s*=", corpo, flags=re.I):
                erro("sem-doi-nem-url",
                     f"citada, year={ano.group(1)}, sem doi nem url: {chave}")

    # A1 (revisor1): órfã. AVISO, nunca erro — ver o cabeçalho.
    for achado in entradas_orfas(texto, set(citadas), ancoradas):
        achados.append({"codigo": achado["codigo"], "detalhe": achado["detalhe"],
                        "severidade": AVISO})

    achados.append({"codigo": "_resumo", "severidade": "info",
                    "detalhe": f"entradas no bib: {len(chaves)} · "
                               f"chaves citadas nos .tex: {len(citadas)}"})
    return achados


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    sem_avisos = "--sem-avisos" in argv

    achados = checar(ROOT)
    resumo = [a for a in achados if a["codigo"] == "_resumo"]
    erros = [a for a in achados if a["severidade"] == ERRO]
    avisos = [a for a in achados if a["severidade"] == AVISO]

    for a in resumo:
        print(a["detalhe"])

    if avisos and not sem_avisos:
        print(f"AVISOS ({len(avisos)}) — não reprovam:")
        for a in avisos:
            print(f"  ~ {a['detalhe']}")

    if erros:
        print(f"PROBLEMAS ({len(erros)}):")
        for a in erros:
            print(f"  - {a['detalhe']}")
        return 1
    print("PROBLEMAS: nenhum")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
