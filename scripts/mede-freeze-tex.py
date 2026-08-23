#!/usr/bin/env python3
"""Prova que uma edição de forma NÃO mexeu em conteúdo (regra de FREEZE).

Dono: revisor1. Compara duas versões do mesmo .tex por MULTICONJUNTO de
números, chaves de citação, \\ref e \\label. Igualdade de multiconjunto é
mais forte que "olhei o diff": pega troca de 0,822 por 0,882 e pega número
que sumiu numa reescrita.

Sai 0 se os quatro multiconjuntos batem; 1 e lista a diferença se não batem.
Compartilha com mede-fluidez-prosa.py a correção do `\\%` (ver o cabeçalho
de lá): antes dela, 8 números da metodologia ficavam invisíveis à checagem.

Uso: python3 scripts/mede-freeze-tex.py <antes.tex> <depois.tex>
"""
import re, sys, collections

def sig(t):
    t = re.sub(r'(?m)(?<!\\)%.*$','',t)
    nums = re.findall(r'(?<![A-Za-z0-9_])\d+(?:[.,]\d+)*(?![A-Za-z0-9_])', t)
    cites = re.findall(r'\\cite[a-z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}', t)
    ckeys = [k.strip() for c in cites for k in c.split(',')]
    refs  = re.findall(r'\\(?:ref|autoref|eqref|pageref)\{([^}]*)\}', t)
    labs  = re.findall(r'\\label\{([^}]*)\}', t)
    # enfase: o principal exige \emph e \textbf identicos numa edicao de forma.
    # Conta OCORRENCIAS (nao o conteudo): reescrever uma frase pode mover a
    # enfase de lugar, mas nao pode criar nem apagar enfase.
    emph  = ['\\emph'] * len(re.findall(r'\\emph\{', t))
    bold  = ['\\textbf'] * len(re.findall(r'\\textbf\{', t))
    return nums, ckeys, refs, labs, emph, bold
a = sig(open(sys.argv[1],encoding='utf-8').read())
b = sig(open(sys.argv[2],encoding='utf-8').read())
nomes=['numeros','citacoes','refs','labels','emph','textbf']
ok=True
for n,x,y in zip(nomes,a,b):
    ca,cb = collections.Counter(x), collections.Counter(y)
    if ca!=cb:
        ok=False
        print(f'[DIFF] {n}: SO EM A={sorted((ca-cb).elements())}  SO EM B={sorted((cb-ca).elements())}')
    else:
        print(f'[OK] {n}: {len(x)} identicos')
sys.exit(0 if ok else 1)
