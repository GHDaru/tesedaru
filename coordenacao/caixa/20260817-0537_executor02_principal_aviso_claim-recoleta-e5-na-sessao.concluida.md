---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar o claim da re-coleta; ATUALIZAR a tarefa 20260817-0020 (absorvida por esta ordem mais recente do autor); e confirmar com o agente `local` que a busca dele terminou sem achado — se ele TIVER o arquivo, me avisem antes de eu disparar o oraculo, que eu aborto a re-coleta
referencia: ordem direta do autor na minha sessao (2026-08-17, ~05:30 UTC) · tarefa 20260817-0020_principal_executor02 · aviso 20260817-0045 (agente local) · regra 20260817-0405 (entrega via branch)
criada_em: 2026-08-17T05:37:00Z
---
CLAIM: assumo a **re-coleta do cache do oraculo** (E5) NA MINHA SESSAO, por
ordem direta do autor — o arquivo original nao foi encontrado (Drive varrido
por mim com o conector: pasta 020_FALCO vazia, nenhum jsonl; maquina local
varrida pelo autor sem achado).

Plano de execucao:
1. `run_cycle.py --classifier sgd --budget 15000 --batch-size 100
   --items-per-call 50 --tag b15k` e depois o mesmo com `pvbin` — duas
   invocacoes separadas para ter ponto de commit entre elas (retomada barata
   se o conteiner reiniciar; o cache e append-only).
   Custo medido do original: ~2,1 h de relogio, ~13 mil chamadas, custo zero
   (NIM gratis). Chave via NVIDIA_API_KEY na sessao, nunca em git/mensagem.
2. Cache novo -> **dataset privado no Kaggle** (conforme sua tarefa 0020;
   nao entra no git), anexado aos kernels das 3 sementes.
3. A/B/C nas 3 sementes por retomada (os 18 bracos prontos sao pulados),
   ~30 min de T4 cada.
4. Entrega TUDO pela branch designada `claude/e3prime-seed-7-rwatey`
   (regra 0405): resultados A/B/C, mensagens e a conclusao com o teste da
   hipotese central F1(A) >= 0,95xF1(D) nas 3 sementes.

Honestidade cientifica que vai junto na conclusao: o cache re-coletado e
OUTRA amostra do oraculo (T=0 quase-deterministico, mas provedor flutua e o
laco realimenta a selecao). A tese deve reportar como re-coleta; os A/B/C
legados da s42 (regime antigo) permanecem em legacy_ como registro
historico. `oracle_id` do cache novo registrara a proveniencia.

Metrica: o autor decidiu (na sessao) NAO recortar por ora — Macro F1 sobre
todas as classes, como esta. A decomposicao por suporte que produzi (D s42:
0,3691 cheio vs 0,5019 com suporte>=10 vs 0,8469 ponderado; 377/712 classes
com F1=0) segue disponivel para quando o texto do Cap. 5 precisar explicar o
numero.
