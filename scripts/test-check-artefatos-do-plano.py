#!/usr/bin/env python3
"""Bateria do check-artefatos-do-plano. Cada invariante com o PAR NEGATIVO."""
import importlib.util, json, os, tempfile

spec = importlib.util.spec_from_file_location(
    "m", os.path.join(os.path.dirname(__file__), "check-artefatos-do-plano.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

falhas, casos = [], 0

def caso(nome, plano, arquivos, deve_acusar):
    global casos
    casos += 1
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "docs/records"), exist_ok=True)
        for a in arquivos:
            p = os.path.join(d, a); os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w").write("x")
        with open(os.path.join(d, "docs/records/plano-revisao.json"), "w") as f:
            json.dump(plano, f)
        acusou = len(m.varrer(d, os.path.join(d, "docs/records/plano-revisao.json"))) > 0
    ok = acusou == deve_acusar
    print(f"[{'PASS' if ok else 'FALHA'}] {nome}")
    if not ok: falhas.append(nome)

# POSITIVOS: tem de acusar
caso("caminho citado que NÃO existe (o caso real do r4-t4)",
     {"n": "R4 CONCLUIDA, 6 pontos em docs/r4-cap2-t4-afirmacoes.md"}, [], True)
caso("caminho dentro de lista aninhada",
     {"c": [{"q": [{"nota": "ver specs/010/qa-report.md"}]}]}, [], True)
caso("script inexistente citado",
     {"n": "rodar scripts/nao-existe.py"}, [], True)

# NEGATIVOS: NÃO pode acusar
caso("caminho citado que EXISTE",
     {"n": "6 pontos em docs/r4-cap2-t4-afirmacoes.md"},
     ["docs/r4-cap2-t4-afirmacoes.md"], False)
caso("URL não é caminho de arquivo",
     {"n": "painel em https://ghdaru.github.io/tesedaru/index.md"}, [], False)
caso("descrição com reticências não é referência",
     {"n": "a1-lce … a7-parada-drift/texto.tex"}, [], False)
caso("prosa sem caminho nenhum",
     {"n": "R1: lote 1 mergeado (110->92 travessoes)"}, [], False)
caso("caminho com curinga é ignorado",
     {"n": "ver specs/*/qa-report.md"}, [], False)
caso("número com ponto não vira caminho (v1.2.1)",
     {"n": "constituicao v1.2.1 aprovada"}, [], False)

caso("campo 'resultado_esperado' descreve artefato FUTURO — não acusa",
     {"execucoes": {"itens": [{"resultado_esperado": "experiments/x/results/y.json"}]}}, [], False)
caso("mas o mesmo caminho em campo comum ACUSA",
     {"execucoes": {"itens": [{"nota": "ver experiments/x/results/y.json"}]}}, [], True)

print()
if falhas:
    print(f"FALHOU — {len(falhas)} de {casos}: {', '.join(falhas)}")
    raise SystemExit(1)
print(f"PASS — 0 falha(s) em {casos} casos")
