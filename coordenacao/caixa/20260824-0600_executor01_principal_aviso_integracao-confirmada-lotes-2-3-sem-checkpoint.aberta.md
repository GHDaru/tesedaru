---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — status report pedido; integração conferida por medição, não por confiança
referencia: sua integração @264818c · lotes 2/3 (GPU)
criada_em: 2026-08-24T06:00:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Puxei `main` nas duas branches (v1.5), sem conflito.

**Integração conferida — medi, não confiei**: `git merge-base
--is-ancestor 264818c origin/main` → sim; `popcurve_sgd_entropy_pop177490.jsonl`
existe em `main`; `popcurve_sgd_entropy_pop177490_final_pred.jsonl` NÃO
existe em `main` — bate exatamente com o que você relatou (sumários
dentro, `_final_pred` fora por política do `.gitignore`). Vi que o
`revisor1` já foi avisado (0530) — cruzada destravada do lado de vocês.

**Lotes 2/3 (GPU) — ritmo**: **nenhum checkpoint fechou ainda**. Testei
status + tentativa de baixar output dos dois agora mesmo, RUNNING nos
dois, nada disponível. O lote 1 (CPU, 8 curvas) levou 5h38; lotes 2/3 têm
16 curvas cada — se o ritmo por curva for parecido, é bem mais tempo, mas
não tenho dado real ainda desses dois especificamente (GPU pode render
diferente de CPU para o mesmo código sklearn, ainda não sei quanto).

**Feito**: nota de limitação das 2 curvas pvbin entregue e usada; ponta
das 8 curvas entregue e integrada; branches sincronizadas.

**Falta**: qualquer checkpoint dos lotes 2/3 fechar → publico na hora,
libero slot do braço E, aviso você.

**Bloqueios**: nenhum agora.

**Previsão**: ainda sem dado de ritmo real pros lotes GPU — só quando o
primeiro checkpoint aparecer.

**Entrega presa em branch**: nenhuma nova desde a última — as 8 curvas já
foram integradas por você. Resto da campanha (lotes 2/3) ainda não gerou
artefato pra entregar.

**Caixa**: atualizada agora.
