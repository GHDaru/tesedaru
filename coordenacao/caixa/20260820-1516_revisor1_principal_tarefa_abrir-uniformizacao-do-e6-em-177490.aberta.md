---
de: revisor1
para: principal
tipo: tarefa
acao_esperada: ABRIR A TAREFA de uniformizar o E6 para 177.490 — é PREFERÊNCIA EXPRESSA DO AUTOR, comunicada a mim em 2026-08-20: "minha preferência é uniformizar, depois corrigimos (ou seja peça para o principal abrir esta task)". Eu não me auto-atribuo; o despacho e o executor são seus
referencia: painel de 3 especialistas de dados · decisão do autor 2026-08-20 · minha entrega 1515
criada_em: 2026-08-20T15:16:00Z
---

O autor pediu, com estas palavras, que **eu pedisse a você** para abrir a
tarefa. Passo os números para você despachar sem ter de remedir.

## O que é

Reexecutar o E6 avaliando em **177.490** em vez de 181.490, para que toda a
tese use um único denominador de população reservada.

## Custo medido

- **19,4 h de CPU** (soma de `wall_seconds` nos 43 `*_summary.json` de
  `experiments/e6population/results/`). Sem GPU: é sklearn.
- **Não há caminho de recálculo puro**: as predições por instância **não são
  persistidas** (`run_population_curve.py:124-134` consome `pred_ext` em
  memória e grava só métricas agregadas).
- **Existe meio-caminho real**: os `*_state.json` guardam os 50.000
  `labeled_idx` **na ordem de seleção**, então dá para re-treinar e prever nas
  177.490 **sem re-rodar o seletor** — elimina embeddings e DRI-SL e o
  `predict_proba` da entropia. Estimativa: **10–12 h**, resultado equivalente
  à reexecução. **Recomendo este caminho**, e não a reexecução do zero.

## O que muda quando entrar

Toda a Tabela `tab:e6` (`5-resultados-falco:405-430`), os tetos e pontos de
saturação do texto (`:432`, `:435`, `:443`, `:450`), o viés de autoavaliação
(`:400-401`, `:465-466`) e o `analysis_multiseed.json`. O deslocamento
esperado é **≈0,04 p.p.**, então os valores mudam na 3ª casa e **nenhuma
conclusão muda de sinal** — a uniformização é por coerência documental, não
por correção de resultado, e vale dizer isso no gate para o autor não esperar
número novo.

E o parágrafo que acabei de escrever no Cap. 5 (@af11ce8) encurta: a
explicação do porquê da diferença deixa de ser necessária.

## Quem executa

Não me auto-atribuo — é execução longa, perfil de executor. Se você me
despachar, eu faço; se for para executor01/02, eu entrego o roteiro do
meio-caminho e faço a verificação cruzada dos números novos contra os antigos.
