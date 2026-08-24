#!/usr/bin/env python3
"""Verifica metadiscurso encenado (regra do autor, 2026-08-24; ver
docs/criterio-humanizacao.md). Uso: checa-metadiscurso.py a.tex [b.tex ...]
Imprime arquivo:linha:trecho por violação; saída vazia e exit 0 = passa."""
import re, sys

PADROES = [
    r"[Ff]alta (a última peça|agora|ainda) ",
    r"não cabe (na tabela|neste capítulo|aqui)",
    r"precisam? ser dit[ao]s?\b",
    r"é preciso dizer",
    r"[Qq]uem quiser",
    r"[Nn]ote-se",
    r"[Vv]ale (lembrar|notar|mapear|a pena|ressaltar|destacar|a visão)",
    r"[Nn]ão custa (dizer|lembrar|repetir)",
    r"[Cc]abe (dizer|notar|registrar|lembrar|destacar)",
    r"como veremos|veremos que",
    r"[Cc]hegou a hora",
    r"[Cc]onvém (fixá|dizer|lembrar|notar)",
    r"[Rr]esta (declarar|dizer|registrar|notar|mencionar)",
    r"deve(m)? ser (registrad|dit|mencionad|notad)[ao]s?\b",
    r"[Aa] (pergunta|questão) (muda|final é|seguinte é|agora é)",
    r"(a peça|o passo) seguinte é",
    r"[Aa]parece o custo|[Rr]esolvido o custo",
    # laudo do Cap.4 (revisor1): encenacao de surpresa e autoelogio de metodo.
    # Medidos nos oito .tex de capitulo: 2 disparos, ambos reais, zero falso positivo.
    r"[Aa] surpresa (está|é|fica)",
    r"\b(reavaliação|análise|leitura|medição) honesta\b",
]
RX = [re.compile(p) for p in PADROES]

falhas = 0
for arq in sys.argv[1:]:
    for i, linha in enumerate(open(arq, encoding="utf-8"), 1):
        prosa = linha.split("%")[0]
        for rx in RX:
            m = rx.search(prosa)
            if m:
                print(f"{arq}:{i}: {m.group(0)!r} em: {prosa.strip()[:80]}")
                falhas += 1
sys.exit(1 if falhas else 0)
