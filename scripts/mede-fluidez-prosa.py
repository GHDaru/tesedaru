#!/usr/bin/env python3
"""Mede a fluidez da prosa de um .tex (palavras/frase, frase mais longa).

Dono: revisor1. Instrumento do princípio IX (DoD de texto verificável): a
"fluidez" deixa de ser juízo e vira número comparável entre duas versões.

DOIS ERROS DE MEDIÇÃO QUE ESTE ARQUIVO JÁ CORRIGE (achados em 2026-08-23,
ambos produziam número BOM por engano, que é o pior modo de falha):

  1. O removedor de comentários ingênuo (`%.*$`) come o `\\%` escapado e
     apaga o resto da linha. Como boa parte dos números da tese vem com
     `\\%`, frases inteiras sumiam da medição. Corrigido com `(?<!\\\\)%`.
  2. A matemática PRECISA ser removida ANTES das notas de rodapé: uma nota
     com número ímpar de `$` quebra a paridade do resto do arquivo, e o
     medidor passa a colar frases umas nas outras, inventando uma frase de
     198 palavras que não existe.

Uso: python3 scripts/mede-fluidez-prosa.py <arquivo.tex>
"""
import re, sys, json

def strip_braced(t, cmd):
    """Remove \cmd{...} incluindo o conteudo, com contagem de chaves."""
    out=[]; i=0; pat='\\'+cmd+'{'
    while i < len(t):
        j = t.find(pat, i)
        if j < 0: out.append(t[i:]); break
        out.append(t[i:j]); k = j+len(pat); d=1
        while k < len(t) and d>0:
            if t[k]=='{': d+=1
            elif t[k]=='}': d-=1
            k+=1
        i=k
    return ''.join(out)

def prosa(tex):
    t = tex
    t = re.sub(r'(?m)(?<!\\)%.*$', '', t)
    # remove ambientes nao-prosa
    for env in ['table','tabular','figure','equation','align','itemize','enumerate','description','lstlisting','verbatim']:
        t = re.sub(r'\\begin\{'+env+r'\*?\}.*?\\end\{'+env+r'\*?\}', ' ', t, flags=re.S)
    # matematica PRIMEIRO: remover footnote antes quebra a paridade de $
    t = re.sub(r'\$[^$]*\$', 'M', t)
    for c in ['footnote','label','caption','index','cite','citep','citet','citeonline','textcite']:
        t = strip_braced(t, c)
    t = re.sub(r'\\(ref|autoref|eqref|pageref)\{[^}]*\}', 'X', t)
    t = re.sub(r'\\(section|subsection|subsubsection|chapter|paragraph)\*?\{[^}]*\}', ' ', t)
    t = re.sub(r'\\[a-zA-Z]+\*?', ' ', t)
    t = t.replace('{',' ').replace('}',' ').replace('~',' ')
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

def frases(p):
    # nao quebrar em abreviaturas comuns nem em decimais
    p = re.sub(r'(\d)\.(\d)', r'\1<DOT>\2', p)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÀÇ])', p)
    return [s.replace('<DOT>','.').strip() for s in parts if len(s.split())>2]

def secoes(tex):
    """dict secao -> corpo"""
    idx = [(m.start(), m.group(2)) for m in re.finditer(r'\\(sub)*section\*?\{([^}]*)\}', tex)]
    res={}
    for n,(pos,name) in enumerate(idx):
        end = idx[n+1][0] if n+1 < len(idx) else len(tex)
        res.setdefault(name, '')
        res[name] += tex[pos:end]
    return res

def stats(body):
    p = prosa(body); fs = frases(p)
    if not fs: return None
    ws = [len(f.split()) for f in fs]
    return dict(frases=len(fs), palavras=sum(ws),
                media=round(sum(ws)/len(ws),1), maxima=max(ws),
                longas=sum(1 for w in ws if w>40))

if __name__ == '__main__':
    tex = open(sys.argv[1], encoding='utf-8').read()
    out={}
    for nome, corpo in secoes(tex).items():
        s = stats(corpo)
        if s: out[nome]=s
    g = stats(tex)
    print(json.dumps({'GLOBAL':g, 'secoes':out}, ensure_ascii=False, indent=1))
