#!/usr/bin/env python3
"""Hook SessionStart: imprime o ESTADO REAL medido, para o contexto da sessao.

Existe por causa de um erro concreto: um agente carregou por varios ciclos a
afirmacao falsa de que um lock tinha vencido sem entrega, porque repetia o
proprio bilhete em vez de medir. O bilhete e rapido; a fonte e verdadeira.
Este hook poe a fonte no contexto de graca, todo inicio de sessao.

Sai sempre 0. Qualquer erro vira uma linha de aviso, nunca uma falha.
"""
import os, re, subprocess, sys
from datetime import datetime, timezone

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def git(*args, timeout=10):
    try:
        r = subprocess.run(["git", "-C", RAIZ, *args],
                           capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip() if r.returncode == 0 else ""
    except Exception:
        return ""

def main():
    linhas = ["=== ESTADO REAL DO REPOSITORIO (medido agora, nao de memoria) ==="]
    git("fetch", "-q", "origin", "main", timeout=15)

    anc = git("log", "--oneline", "-1", "origin/main")
    linhas.append(f"main: {anc[:150] if anc else '(nao foi possivel medir)'}")

    atras = git("rev-list", "--count", "HEAD..origin/main")
    if atras and atras != "0":
        linhas.append(f"AVISO: este checkout esta {atras} commits ATRAS de origin/main. "
                      "Meca em worktree limpo destacado de origin/main, nunca aqui.")

    # locks vivos, com TTL calculado
    locks = git("ls-tree", "--name-only", "origin/main", "coordenacao/locks/")
    vivos = []
    agora = datetime.now(timezone.utc)
    for caminho in [l for l in locks.splitlines() if l.endswith(".md")]:
        txt = git("show", f"origin/main:{caminho}")
        dono = (re.search(r"^dono:\s*(.+)$", txt, re.M) or [None, "?"])[1].strip()
        ttl = int((re.search(r"^ttl_min:\s*(\d+)", txt, re.M) or [0, 45])[1])
        m = re.search(r"^renovado_em:\s*\"?([0-9T:\-]+)", txt, re.M) or \
            re.search(r"^criada_em:\s*\"?([0-9T:\-]+)", txt, re.M)
        estado = "sem data"
        if m:
            try:
                t = datetime.fromisoformat(m[1].rstrip("Z")).replace(tzinfo=timezone.utc)
                resta = ttl - (agora - t).total_seconds() / 60
                estado = f"VENCIDO ha {abs(int(resta))} min" if resta < 0 else f"expira em {int(resta)} min"
            except Exception:
                pass
        vivos.append(f"  {os.path.basename(caminho)[:48]} · dono {dono} · {estado}")
    linhas.append(f"locks: {len(vivos)}")
    linhas.extend(vivos[:8])

    # caixa: mensagens abertas por remetente
    caixa = git("ls-tree", "--name-only", "origin/main", "coordenacao/caixa/")
    abertas = {}
    for c in caixa.splitlines():
        if not c.endswith(".aberta.md"):
            continue
        partes = os.path.basename(c).split("_")
        if len(partes) > 2:
            abertas[partes[1]] = abertas.get(partes[1], 0) + 1
    if abertas:
        linhas.append("caixa aberta por remetente: " +
                      " · ".join(f"{k} {v}" for k, v in sorted(abertas.items())))

    # branches remotas fora da main
    brs = git("branch", "-r", "--no-merged", "origin/main")
    nomes = [b.strip() for b in brs.splitlines()
             if b.strip() and "->" not in b and b.strip() != "origin/main"]
    linhas.append(f"branches fora da main: {len(nomes)}")
    for n in nomes[:12]:
        q = git("rev-list", "--count", f"origin/main..{n}")
        linhas.append(f"  {n.replace('origin/', '')} ({q or '?'} commits)")
    if len(nomes) > 12:
        linhas.append(f"  ... e mais {len(nomes) - 12}")

    linhas.append("REGRA: meca sempre em worktree limpo destacado de origin/main; "
                  "o checkout local pode estar velho.")
    print("\n".join(linhas))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"(estado-da-sessao: nao foi possivel medir — {type(e).__name__})")
    sys.exit(0)
