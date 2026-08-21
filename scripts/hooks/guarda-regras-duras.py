#!/usr/bin/env python3
"""Hook PreToolUse: transforma em REGRA as tres proibicoes que o autor deu por escrito.

Instrucao no CLAUDE.md depende de o agente lembrar. Este hook nao depende:
a chamada de ferramenta simplesmente nao acontece.

Contrato: le o JSON do evento em stdin; sai 0 para permitir, 2 para BLOQUEAR
(o texto do stderr volta para o agente). Qualquer erro interno -> sai 0.
Falhar em ABERTO e deliberado: um guarda quebrado nao pode parar a tese.
"""
import json, os, re, subprocess, sys

def bloqueia(motivo: str) -> None:
    print(motivo, file=sys.stderr)
    sys.exit(2)

# ---------------------------------------------------------------- 1. force-push
FORCE = re.compile(r"(?:^|\s)(?:--force(?!-with-lease)|-f)(?:\s|$)")
LEASE = re.compile(r"--force-with-lease")

def checa_push(cmd: str) -> None:
    if "git" not in cmd or "push" not in cmd:
        return
    for trecho in re.split(r"&&|\|\||;|\n", cmd):
        if not re.search(r"\bgit\b[^|]*\bpush\b", trecho):
            continue
        tem_force = bool(FORCE.search(trecho)) or bool(LEASE.search(trecho))
        if not tem_force:
            continue
        alvo_main = re.search(r"(?:^|\s)(?:HEAD:)?main(?:\s|$)", trecho) or \
                    re.search(r":main(?:\s|$)", trecho)
        if alvo_main:
            bloqueia(
                "BLOQUEADO pela regra dura do autor: force-push em main e proibido.\n"
                "Push rejeitado resolve-se com `git fetch origin main && git rebase "
                "origin/main` e push normal. Nunca force.\n"
                f"Comando recusado: {trecho.strip()[:200]}")
        if FORCE.search(trecho):
            bloqueia(
                "BLOQUEADO: `--force` puro. Se a branch e sua e voce precisa reescrever,\n"
                "use `--force-with-lease` com o destino EXPLICITO (nunca main).\n"
                f"Comando recusado: {trecho.strip()[:200]}")

# ---------------------------------------------------------------- 2. segredos
SEGREDO = re.compile(r"(?:^|/)\.env(?:\.|$)|(?:^|/)\.env$")

def checa_segredo(caminho: str) -> None:
    if caminho and SEGREDO.search(caminho):
        bloqueia(
            "BLOQUEADO pela regra dura do autor: `.env` fica FORA do git.\n"
            f"Caminho recusado: {caminho}")

def checa_segredo_no_bash(cmd: str) -> None:
    if re.search(r"\bgit\s+add\b[^|]*\.env\b", cmd):
        bloqueia("BLOQUEADO: `git add` de arquivo .env. Segredo nao entra no repositorio.")

# ------------------------------------------------- 3. superficies de outras frentes
def _caminho_do_cache(raiz: str):
    """Diretorio .git REAL. Em worktree, `.git` e um ARQUIVO, nao um diretorio:
    escrever cache dentro dele falha e desliga a regra em silencio. Foi um
    defeito real, encontrado ao testar a regra com dado de verdade."""
    try:
        r = subprocess.run(["git", "-C", raiz, "rev-parse", "--git-dir"],
                           capture_output=True, text=True, timeout=5)
        if r.returncode != 0 or not r.stdout.strip():
            return None
        gitdir = r.stdout.strip()
        if not os.path.isabs(gitdir):
            gitdir = os.path.join(raiz, gitdir)
        return os.path.join(gitdir, "guarda-superficies.cache")
    except Exception:
        return None

def arquivos_de_outras_frentes(raiz: str):
    """Arquivos tocados por branches humanize/* e governanca/*, com cache de 15 min."""
    import time
    cache = _caminho_do_cache(raiz)
    if cache:
        try:
            if os.path.exists(cache) and (os.path.getmtime(cache) + 900) > time.time():
                with open(cache, encoding="utf-8") as fh:
                    return set(l.strip() for l in fh if l.strip())
        except Exception:
            pass
    achados = set()
    try:
        listagem = subprocess.run(
            ["git", "-C", raiz, "branch", "-r", "--list",
             "origin/humanize/*", "origin/governanca/*"],
            capture_output=True, text=True, timeout=8)
        if listagem.returncode != 0:
            return set()                 # sem git utilizavel -> falha em aberto
        for b in (x.strip() for x in listagem.stdout.splitlines() if x.strip()):
            if "->" in b:
                continue
            saida = subprocess.run(
                ["git", "-C", raiz, "diff", "--name-only", f"origin/main...{b}"],
                capture_output=True, text=True, timeout=8)
            if saida.returncode == 0:
                achados.update(x.strip() for x in saida.stdout.splitlines() if x.strip())
    except Exception:
        return set()
    if cache:                            # cache e otimizacao: se falhar, o resultado vale
        try:
            with open(cache, "w", encoding="utf-8") as fh:
                fh.write("\n".join(sorted(achados)))
        except Exception:
            pass
    return achados

def checa_frente_alheia(caminho: str, raiz: str) -> None:
    if not caminho:
        return
    rel = os.path.relpath(caminho, raiz) if os.path.isabs(caminho) else caminho
    if rel in arquivos_de_outras_frentes(raiz):
        bloqueia(
            "BLOQUEADO pela regra dura do autor: nao edite arquivo tocado por branch\n"
            "`humanize/*` ou `governanca/*` — o merge delas conflitaria com a sua edicao.\n"
            f"Arquivo recusado: {rel}\n"
            "Se a edicao for mesmo necessaria, peca ao principal e registre a razao.")

# ------------------------------------------------------------- 4. arquivo gerado
def checa_gerado(caminho: str) -> None:
    if caminho and os.path.basename(caminho) == "AGENTS.md":
        bloqueia(
            "BLOQUEADO: `AGENTS.md` e GERADO a partir do CLAUDE.md.\n"
            "Edite o `CLAUDE.md` e rode `scripts/sync-agents-md.sh`.")

def main() -> None:
    try:
        evento = json.load(sys.stdin)
    except Exception:
        sys.exit(0)                      # sem evento legivel -> permite
    ferramenta = evento.get("tool_name", "")
    entrada = evento.get("tool_input", {}) or {}
    raiz = evento.get("cwd") or os.getcwd()
    try:
        if ferramenta == "Bash":
            cmd = entrada.get("command", "") or ""
            checa_push(cmd)
            checa_segredo_no_bash(cmd)
        elif ferramenta in ("Edit", "Write", "NotebookEdit", "MultiEdit"):
            caminho = entrada.get("file_path", "") or entrada.get("notebook_path", "") or ""
            checa_segredo(caminho)
            checa_gerado(caminho)
            checa_frente_alheia(caminho, raiz)
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)                      # erro interno -> permite (falha em aberto)
    sys.exit(0)

if __name__ == "__main__":
    main()
