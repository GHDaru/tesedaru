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

    # ENTREGAS PRESAS EM BRANCH: mensagens ao principal que estao numa branch
    # designada e nunca chegaram na main. Existe porque os executores nao podem
    # empurrar para a main (o harness so libera a branch deles): a mensagem de
    # entrega nasce correta na caixa, mas na branch — invisivel para o principal
    # que le a main. Este bloco poe a fonte no contexto de graca.
    # so branches de trabalho vivas: pula forks antigos (overleaf/*) e branches
    # muito adiante da main, que sao historia velha e nao entrega pendente.
    def viva(n):
        curto = n.replace("origin/", "")
        if curto.startswith("overleaf"):
            return False
        q = git("rev-list", "--count", f"origin/main..{n}")
        return q.isdigit() and int(q) <= 40
    alvo = [n for n in nomes if viva(n)][:15]
    if alvo:
        refspecs = [f"+refs/heads/{n.replace('origin/', '')}:refs/remotes/{n}" for n in alvo]
        git("fetch", "-q", "origin", *refspecs, timeout=20)
    # basenames ja presentes na main (em qualquer estado): serve para a mensagem
    # SUMIR do aviso assim que o principal a integrar.
    na_main = set(os.path.basename(c) for c in caixa.splitlines() if c.endswith(".md"))
    na_main_raiz = set(b.rsplit(".", 2)[0] for b in na_main)  # sem o .<estado>.md
    presas = []
    for n in alvo:
        # o que a branch INTRODUZIU desde que saiu da main (tres pontos), so
        # mensagens ABERTAS ao principal, E que ainda nao existem na main (em
        # nenhum estado) — o sinal real de entrega que ainda nao foi integrada.
        novos = git("diff", "--name-only", f"origin/main...{n}", "--", "coordenacao/caixa/")
        for a in novos.splitlines():
            base = os.path.basename(a)
            if not ("_principal_" in base and base.endswith(".aberta.md")):
                continue
            if base in na_main or base.rsplit(".", 2)[0] in na_main_raiz:
                continue  # ja integrada (mesma mensagem, talvez ja arquivada)
            partes = base.split("_")
            de = partes[1] if len(partes) > 1 else "?"
            presas.append(f"  [{n.replace('origin/', '')}] de {de}: {base[:70]}")
    if presas:
        linhas.append(f"ENTREGAS/AVISOS AO PRINCIPAL PRESOS EM BRANCH (nao estao na main): {len(presas)}")
        linhas.extend(presas[:20])
        if len(presas) > 20:
            linhas.append(f"  ... e mais {len(presas) - 20}")
        linhas.append("  ACAO: buscar a branch e recuperar a mensagem "
                      "(git show <branch>:<caminho>) — nao espere na main.")

    linhas.append("REGRA: meca sempre em worktree limpo destacado de origin/main; "
                  "o checkout local pode estar velho.")
    print("\n".join(linhas))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"(estado-da-sessao: nao foi possivel medir — {type(e).__name__})")
    sys.exit(0)
