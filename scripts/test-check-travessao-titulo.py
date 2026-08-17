#!/usr/bin/env python3
"""Bateria do check-travessao-titulo. Cada invariante com o PAR NEGATIVO.

Sem o par negativo, um teste só prova que o script reclama — não que reclama
da coisa certa. Foi a lição do teste morto do `check-bib` (anti-padrão nº 7).
"""
import importlib.util, os, tempfile

spec = importlib.util.spec_from_file_location(
    "m", os.path.join(os.path.dirname(__file__), "check-travessao-titulo.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

falhas, casos = [], 0

def caso(nome, texto, deve_acusar):
    global casos
    casos += 1
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "t.tex")
        open(p, "w", encoding="utf-8").write(texto)
        acusou = len(m.varrer([p])) > 0
    ok = acusou == deve_acusar
    print(f"[{'PASS' if ok else 'FALHA'}] {nome}")
    if not ok:
        falhas.append(nome)

# --- POSITIVOS: tem de acusar
caso("section com — acusa",
     "\\section{Pilar P2: cold start — algoritmo DRI-SL}\n", True)
caso("caption com — acusa (os 2 casos reais do Cap.5)",
     "\\caption{E0 — desempenho dos oráculos LLM.}\n", True)
caso("chapter com — acusa", "\\chapter{Resultados — P3 e P4}\n", True)
caso("subsection com — acusa", "\\subsection{Custo — instrumentação}\n", True)
caso("section estrelada com — acusa", "\\section*{Anexo — notas}\n", True)
caso("section com argumento opcional e — acusa",
     "\\section[curto]{Titulo longo — com travessao}\n", True)

# --- NEGATIVOS: NÃO pode acusar
caso("section com --- (a forma correta) NÃO acusa",
     "\\section{Pilar P2: cold start --- algoritmo DRI-SL}\n", False)
caso("CORPO do texto com — NÃO acusa (a unificação segue valendo)",
     "O laço tem duas fases — e ambas custam rótulo.\n", False)
caso("corpo com — logo APÓS uma linha de título limpa NÃO acusa",
     "\\section{Titulo limpo}\nO texto abaixo tem travessão — e pode ter.\n", False)
caso("caption com --- NÃO acusa", "\\caption{E0 --- custo por mil rótulos}\n", False)
caso("label/ref na mesma linha sem travessão NÃO acusa",
     "\\section{Metodo}\\label{sec:m}\n", False)
caso("comando parecido (\\captionsetup) NÃO acusa",
     "\\captionsetup{format=plain} % nota — sem travessao em titulo\n", False)

print()
if falhas:
    print(f"FALHOU — {len(falhas)} de {casos}: {', '.join(falhas)}")
    raise SystemExit(1)
print(f"PASS — 0 falha(s) em {casos} casos")
