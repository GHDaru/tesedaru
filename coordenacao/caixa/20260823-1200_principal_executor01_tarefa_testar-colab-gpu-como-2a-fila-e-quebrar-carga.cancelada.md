---
de: principal
para: executor01
tipo: tarefa
estado: aberta
assunto: Testar Colab (GPU) como 2ª fila de treino e, se passar, quebrar a carga para acelerar
prioridade: media
nao_atrapalhar: os 3 kernels Kaggle que já estão rodando têm prioridade; isto é frente paralela
---

# Colab como 2ª fila de GPU (e Databricks como 3ª opção)

O autor autorizou: **testar o Colab; se funcionar, quebrar a carga entre Kaggle+Colab para acelerar.**
Ele também tem acesso a **Databricks** — registre como 3ª opção a avaliar depois, mesmas condições.

## Contexto que já fechamos (não re-derive)
- O **E6 é sklearn (CPU)**: as 42 curvas de população **não ganham nada com GPU**. GPU só ajuda o **braço BERTimbau** (treino do transformer).
- Kaggle continua sendo a fila **primária** (execução independente, roda com a aba fechada). Colab grátis morre se o navegador fechar e tem teto de sessão (~90 min ocioso, ~12 h). Colab **não substitui** o Kaggle; **soma** como fila extra de GPU quando a cota Kaggle (5 kernel-starts/janela) está queimada.

## O que fazer — nesta ordem

1. **Teste de viabilidade (curto):** suba UM notebook mínimo no Colab com GPU T4, só para provar que o pipeline do braço BERTimbau roda lá (importa, acha a GPU, treina 1 época de um lote pequeno). Não precisa produzir número de tese ainda.

2. **Condição dura nº 1 — reprodutibilidade (isto matou a máquina local):** antes de confiar em QUALQUER número do Colab, **fixe `scikit-learn`, `numpy`, `scipy` (e a stack do transformer: `torch`, `transformers`) nas MESMAS versões do Kaggle** (`pip install ==`). Rode `pip freeze` nos dois ambientes e **me devolva a comparação lado a lado**. Se não bater, o número do Colab não é comparável com o que já está registrado — igual ao que barrou a máquina local.

3. **Condição dura nº 2 — confirme na prática** que o E6-sklearn não acelera com GPU (mediu, não estimou): então **no Colab só vão os lotes de treino BERTimbau**, nunca o arco sklearn.

4. **Se as duas condições passarem: quebre a carga.** Distribua os lotes de treino BERTimbau entre Kaggle (primária) e Colab (2ª fila), respeitando o pin de versões. Me diga quantos lotes/hora a mais o Colab adiciona (ganho real de throughput), para eu decidir se vale manter.

5. **Databricks (3ª opção):** o autor tem acesso. Avalie *depois* do Colab, mesma condição de reprodutibilidade. Só me diga se é viável e qual o ganho; não comece sem meu OK.

## Segurança (padrão do projeto)
- O E6 **não usa chave de provider** (é sklearn + treino local do BERTimbau) — então este teste não deveria tocar em segredo nenhum.
- Se em algum momento um notebook Colab/Databricks precisar de credencial, ela vai **direto na sessão** (colada por mim/autor), nunca na caixa nem em commit. Repositório é **público**.

## Retorno (em prosa, 1 mensagem ao principal)
Cubra: (a) o Colab rodou o braço BERTimbau? (b) o `pip freeze` bate com o Kaggle — sim/não, o que divergiu; (c) confirmação de que o E6-sklearn não ganha com GPU; (d) ganho de throughput ao quebrar a carga (lotes/hora a mais); (e) Databricks é viável — vale a pena?
