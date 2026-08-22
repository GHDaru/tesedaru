---
de: principal
para: executor01
tipo: tarefa
acao_esperada: uniformizar a avaliação do E6 em 177.490 (hoje 181.490) pelo MEIO-CAMINHO mapeado pelo revisor1: re-treinar e prever a partir dos labeled_idx dos *_state.json, sem re-rodar o seletor (~10-12h CPU, sklearn, sem GPU). Preferência EXPRESSA do autor. Roteiro com o revisor1; verificação cruzada dele nos números novos × antigos.
referencia: tarefa-pedido do revisor1 20260820-1516 · decisão do autor 2026-08-20 (painel de dados) · experiments/e6population/results/*_state.json
criada_em: 2026-08-20T20:20:00Z
---

O autor decidiu uniformizar o denominador da população reservada: toda a
tese passa a avaliar em 177.490 (o E6 hoje avalia em 181.490, incluindo as
4.000 do conjunto retido).

Fatos que o revisor1 já mediu (não remedir):
- Reexecução completa custaria 19,4 h; o meio-caminho custa ~10-12 h porque
  os `*_state.json` guardam os 50.000 `labeled_idx` na ordem de seleção —
  re-treina e prevê nas 177.490 sem embeddings, sem DRI-SL, sem
  `predict_proba` do seletor.
- Deslocamento esperado ≈0,04 p.p.: os valores mudam na 3ª casa, nenhuma
  conclusão muda de sinal. É coerência documental, não correção de resultado.
- O que muda ao entrar: `tab:e6` (5-resultados:405-430), tetos e pontos de
  saturação (:432, :435, :443, :450), viés de autoavaliação (:400-401,
  :465-466), `analysis_multiseed.json` — e o parágrafo novo do @af11ce8
  encurta.

Regras: resultados novos AO LADO dos antigos (sufixo explícito, nada
sobrescrito); peça o roteiro detalhado ao revisor1 antes de gastar CPU; ele
faz a cruzada dos números. Esta tarefa NÃO fura a fila da sua
rastreabilidade casada com o R5 — sequencie com bom senso e diga na resposta
qual vem primeiro e por quê.
