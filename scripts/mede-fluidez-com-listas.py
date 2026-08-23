#!/usr/bin/env python3
"""Fluidez CONTANDO o texto de itemize/enumerate. Complementa, nao substitui,
o mede-fluidez-prosa.py.

Dono: revisor2. Existe por um ponto cego medido em 2026-08-25: o
mede-fluidez-prosa.py (dono: revisor1) remove os ambientes itemize e enumerate
INTEIROS antes de medir. A consequencia e perversa para quem edita forma:
transformar uma frase-monstro em lista faz a metrica despencar sem que uma
palavra do texto tenha encurtado. E o mesmo modo de falha que o cabecalho
daquele script ja documenta duas vezes: numero BOM por engano.

Aqui cada \\item vira uma unidade de prosa e o resto do pipeline e identico.
Use os DOIS: se as medias divergem muito, a diferenca esta dentro das listas.

Uso: python3 scripts/mede-fluidez-com-listas.py <arquivo.tex>
"""
import re, sys, json
try:  # nao estourar quando a saida vai para `| head`
    import signal; signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except (ImportError, AttributeError, ValueError):
    pass

def strip_braced(t, cmd):
    out=[]; i=0; pat='\\'+cmd+'{'
    while i < len(t):
        j = t.find(pat, i)
        if j < 0: out.append(t[i:]); break
        out.append(t[i:j]); k=j+len(pat); d=1
        while k < len(t) and d>0:
            if t[k]=='{': d+=1
            elif t[k]=='}': d-=1
            k+=1
        i=k
    return ''.join(out)

def prosa(tex):
    t = re.sub(r'(?m)(?<!\\)%.*$', '', tex)
    # remove SO os ambientes que nao sao prosa; listas ficam
    for env in ['table','tabular','figure','equation','align','lstlisting','verbatim']:
        t = re.sub(r'\\begin\{'+env+r'\*?\}.*?\\end\{'+env+r'\*?\}', ' ', t, flags=re.S)
    t = re.sub(r'\\(begin|end)\{(itemize|enumerate|description)\*?\}', ' ', t)
    t = re.sub(r'\\item\s*', ' ', t)
    t = re.sub(r'\$[^$]*\$', 'M', t)
    for c in ['footnote','label','caption','index','cite','citep','citet','citealp','citeonline','textcite']:
        t = strip_braced(t, c)
    t = re.sub(r'\\(ref|autoref|eqref|pageref)\{[^}]*\}', 'X', t)
    t = re.sub(r'\\(section|subsection|subsubsection|chapter|paragraph)\*?\{[^}]*\}', ' ', t)
    t = re.sub(r'\\[a-zA-Z]+\*?', ' ', t)
    t = t.replace('{',' ').replace('}',' ').replace('~',' ')
    return re.sub(r'\s+',' ',t).strip()

def frases(p):
    p = re.sub(r'(\d)\.(\d)', r'\1<DOT>\2', p)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÀÇ])', p)
    return [s.replace('<DOT>','.').strip() for s in parts if len(s.split())>2]

def secoes(tex):
    idx=[(m.start(), m.group(2)) for m in re.finditer(r'\\(sub)*section\*?\{([^}]*)\}', tex)]
    res={}
    for n,(pos,name) in enumerate(idx):
        end = idx[n+1][0] if n+1<len(idx) else len(tex)
        res.setdefault(name,''); res[name]+=tex[pos:end]
    return res

def stats(b):
    fs=frases(prosa(b))
    if not fs: return None
    ws=[len(f.split()) for f in fs]
    return dict(frases=len(fs), media=round(sum(ws)/len(ws),1), maxima=max(ws),
                acima40=sum(1 for w in ws if w>40))

tex=open(sys.argv[1],encoding='utf-8').read()
print("GLOBAL", stats(tex))
for k,v in secoes(tex).items():
    st=stats(v)
    if st: print("  %-38s media %5.1f  max %3d  >40: %d" % (k[:38], st['media'], st['maxima'], st['acima40']))
