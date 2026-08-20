#!/usr/bin/env python3
"""Bateria do check-travessao-titulo. Cada invariante com o PAR NEGATIVO.

Sem o par negativo, um teste só prova que o script reclama — não que reclama
da coisa certa. Foi a lição do teste morto do `check-bib` (anti-padrão nº 7).

Desde 2026-08-17 a regra tem dois níveis (exceção do \\caption aprovada pelo
autor, `docs/criterio-humanizacao.md`): título com `—` é ERRO (exit 1);
legenda com `—` é AVISO (aparece, mas não reprova). A bateria testa os dois
níveis e o exit resultante — não só "achou/não achou".
"""
import importlib.util, os, tempfile

spec = importlib.util.spec_from_file_location(
    "m", os.path.join(os.path.dirname(__file__), "check-travessao-titulo.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

falhas, casos = [], 0

def caso(nome, texto, severidades):
    """severidades: lista esperada de severidades dos achados ([] = limpo)."""
    global casos
    casos += 1
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.tex")
        open(p, "w", encoding="utf-8").write(texto)
        achados = m.varrer([p])
    obtidas = [a["severidade"] for a in achados]
    ok = obtidas == severidades
    print(f"[{'PASS' if ok else 'FALHA'}] {nome}")
    if not ok:
        print(f"    esperado {severidades}, obtido {obtidas}")
        falhas.append(nome)

# --- ERROS: título com — reprova
caso("section com — é erro",
     "\\section{Pilar P2: cold start — algoritmo DRI-SL}\n", ["erro"])
caso("chapter com — é erro", "\\chapter{Resultados — P3 e P4}\n", ["erro"])
caso("subsection com — é erro", "\\subsection{Custo — instrumentação}\n", ["erro"])
caso("section estrelada com — é erro", "\\section*{Anexo — notas}\n", ["erro"])
caso("section com argumento opcional e — é erro",
     "\\section[curto]{Titulo longo — com travessao}\n", ["erro"])

# --- AVISOS: a exceção do \caption (fixture do caso real do Cap.5)
caso("caption com — é AVISO, não erro (exceção registrada)",
     "\\caption{E0 — desempenho dos oráculos LLM.}\n", ["aviso"])
caso("caption com — E section com — na mesma varredura: um de cada",
     "\\caption{E0 — custo}\n\\section{Titulo — quebrado}\n",
     ["aviso", "erro"])

# --- NEGATIVOS: NÃO pode acusar nada
caso("section com --- (a forma correta) NÃO acusa",
     "\\section{Pilar P2: cold start --- algoritmo DRI-SL}\n", [])
caso("CORPO do texto com — NÃO acusa (a unificação segue valendo)",
     "O laço tem duas fases — e ambas custam rótulo.\n", [])
caso("corpo com — logo APÓS uma linha de título limpa NÃO acusa",
     "\\section{Titulo limpo}\nO texto abaixo tem travessão — e pode ter.\n", [])
caso("caption com --- NÃO acusa", "\\caption{E0 --- custo por mil rótulos}\n", [])
caso("label/ref na mesma linha sem travessão NÃO acusa",
     "\\section{Metodo}\\label{sec:m}\n", [])
caso("comando parecido (\\captionsetup) NÃO acusa",
     "\\captionsetup{format=plain} % nota — sem travessao em titulo\n", [])

# --- EXIT: aviso não reprova; erro reprova
def caso_exit(nome, texto, exit_esperado):
    global casos
    casos += 1
    import io, sys as _sys
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.tex")
        open(p, "w", encoding="utf-8").write(texto)
        argv, _sys.argv = _sys.argv, ["x", p]
        buf, _sys.stdout = _sys.stdout, io.StringIO()
        try:
            codigo = m.main()
        finally:
            _sys.stdout, _sys.argv = buf, argv
    ok = codigo == exit_esperado
    print(f"[{'PASS' if ok else 'FALHA'}] {nome}")
    if not ok:
        print(f"    exit esperado {exit_esperado}, obtido {codigo}")
        falhas.append(nome)

caso_exit("exit 0 com SÓ avisos de caption (DoD não trava)",
          "\\caption{E0 — desempenho}\n", 0)
caso_exit("exit 1 com erro de título (mesmo havendo aviso junto)",
          "\\caption{E0 — custo}\n\\section{Titulo — quebrado}\n", 1)
caso_exit("exit 0 limpo", "\\section{Titulo limpo}\n", 0)

print()
if falhas:
    print(f"FALHOU — {len(falhas)} de {casos}: {', '.join(falhas)}")
    raise SystemExit(1)
print(f"PASS — 0 falha(s) em {casos} casos")
