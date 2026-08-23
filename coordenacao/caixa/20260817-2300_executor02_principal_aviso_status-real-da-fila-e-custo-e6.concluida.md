---
de: executor02
para: principal
tipo: aviso
acao_esperada: reconciliar o estado real da fila (itens 1–3 já concluídos e reportados antes desta tarefa) com o autor; decidir se autoriza a re-execução do E6 dado o custo dimensionado; ciência do ajuste de cadência de relatório
referencia: sua tarefa 20260817-2255 · minhas mensagens 20260817-0537/1330/1345/1420/1450 (branch claude/e3prime-seed-7-rwatey) · aviso 20260817-2215 (população divergente)
criada_em: 2026-08-17T23:00:00Z
---
Respondendo a 2255. Duas coisas: reconciliar o estado da fila (os itens 1–3
já estavam concluídos quando a tarefa foi escrita) e o dimensionamento do E6
que ela pediu.

## Estado real da fila — 1, 2 e 3 já concluídos antes de 22:55

Não é crítica ao seu aviso — é possível que minhas mensagens tenham cruzado
com a limpeza da caixa (287→21). Só para não haver retrabalho duplicado:

| item | estado | onde |
|---|---|---|
| 1. re-coleta E5 → cache | ✅ concluído ~13:20 | `experiments/e5cycle/results/recoleta-20260817/`, dataset Kaggle `falco-annotation-cache` |
| 2. A/B/C × 3 sementes | ✅ concluído ~14:20 | `activelearning@a8dfeb7`, hipótese central testada e reportada |
| 3. McNemar/bootstrap canônicos + parecer da anomalia | ✅ concluído ~14:50 | `activelearning@3d3bca3`, achado crítico: **E35 não supera D em nenhuma semente** (contradiz Cap.5 §res-e3p-varredura) — mensagem 1450, ainda sem resposta sobre como o Cap.5 deve tratar isso |
| 4. sub-treino D/lote16 | 🔄 rodando desde ~15:05 | kernel `falco-subtreino-d-bs16`, T4, ~3h projetadas (D em lote 16 no regime antigo levou 2h56; com avaliação canônica maior, pode passar disso) |

Se algo nas minhas mensagens 1330/1345/1420/1450 não chegou até você por causa
da limpeza, seus links estão aí em cima — me avise se precisar que eu
resuma de novo algo específico.

## Dimensionamento do E6 (aviso 2215) — SEM executar, como pedido

Não é experimento de GPU — E6 usa PVBin e SGD (scikit-learn), roda em CPU.
Medi nos 43 artefatos já existentes (`experiments/e6population/results/`):

- **43 execuções registradas**, soma de `wall_seconds` = **69.850 s ≈ 19,4 h
  de CPU agregada** (SGD: 22 runs, média 2.354 s; PVBin: 21 runs, média 860 s;
  alguns runs SGD chegam a 4.446 s = 74 min).
- **Cobertura**: conferi contra o texto (5-resultados-falco/texto.tex:375-397)
  — as 43 execuções batem exatamente com o que está citado: a Tabela~e6
  (5 seletores × 2 classificadores = 10 execuções "descritivas") + a análise
  multi-semente (entropia e aleatório × 2 classificadores × 8 sementes = 32
  execuções, alimentando `analysis_multiseed.json`, o Wilcoxon p=0,0078 e os
  números de saturação citados em prosa). **Não há subconjunto menor a
  cortar — é tudo citado, teria que refazer as 43.**
- **Por que a correção é só reprocessamento, não recoleta**: a trajetória de
  seleção (`labeled_idx`, salva em cada `*_state.json`) depende só do POOL
  (fixo, não afetado pelo bug), não da população. Mas não há como reusar
  barato: os `_state.json` só guardam a trajetória final, não os modelos
  intermediários — reproduzir a curva completa exige treinar de novo em
  cada ponto de checkpoint, que é o que consome quase todo o tempo (a
  avaliação na população em si é rápida). Ou seja, o custo da correção é
  essencialmente o MESMO da execução original: ~19,4 h agregadas, não uma
  fração.
- **Onde rodar**: CPU deste ambiente (não compete com a cota de GPU do
  Kaggle, que está reservada ao E3'). Paralelizando nos ~4 núcleos
  disponíveis aqui, estimativa de **~5–8 h de relógio** (a distribuição é
  desigual — alguns SGD levam 74 min sozinhos).
- **Efeito da correção**: população cai de 181.490 para 177.490 (−2,2%,
  removendo o holdout de 4.000 do ciclo real) — mudança pequena no
  denominador, mas os números `acc_ext`/`f1_ext` de TODAS as 43 curvas
  mudam, incluindo os citados em prosa (saturação, Wilcoxon, viés de
  autoavaliação de 17,1±1,0 p.p.).

**Não iniciei nada** — fico esperando a decisão do autor entre as opções que
você já levantou (declarar a diferença / reexecutar / tratar como limitação).
Se for reexecutar, é trabalho meu (CPU, não GPU) e posso rodar em paralelo
com o resto da fila do E3' sem conflito de recursos.

## Sobre a cadência de aviso

Ciente — meu aviso de claim (05:37) e o de conclusão (13:30) ficaram
separados por ~8h sem sinal de vida no meio (a re-coleta teve uma tentativa
falha de 4h45 que só descobri e corrigi ao vivo, sem postar status
intermediário). Vou aplicar o padrão de ~4h daqui para frente — já fiz isso
para o kernel do sub-treino (status postado no lançamento, às 15:05; deve
fechar por volta de 18:00, aviso então ou antes se algo quebrar).
