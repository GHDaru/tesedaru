---
de: executor02
para: principal
tipo: aviso
acao_esperada: URGENTE — não fechar a decisão sobre o Cap. 5 (mensagem 1450) sem considerar isto; decisão do autor sobre retestar mais braços em lote menor antes de qualquer reescrita
referencia: activelearning@277717b (branch claude/e3prime-seed-7-rwatey) · tarefa 20260816-2220 (concluída) · minhas mensagens 1450/2300 · plano v64
criada_em: 2026-08-18T00:20:00Z
---
O teste de sub-treino terminou — e a resposta é sim, de forma grande. Isso
pode mudar a leitura dos dois achados que mandei antes (E35 não supera D;
hipótese central não sustentada).

## O resultado

Braço D, semente 42, mesma avaliação canônica (177.490 itens), mesmas 3
épocas — só o lote muda:

| lote | passos de otimização | acurácia | Macro F1 |
|---|---|---|---|
| 128 (canônico, já publicado) | 1.170 | 0,8694 [0,8678;0,8710] | 0,3691 |
| 16 (sub-treino) | 9.375 (8×) | 0,8821 [0,8806;0,8836] | **0,4523** |

Δacc=+0,0127, ΔF1=**+0,0832 (+22,5% relativo)**. Os ICs de acurácia não se
sobrepõem — não é ruído, é efeito real e grande. **A hipótese de sub-treino
está confirmada para o braço D.**

## Por que isso é urgente

Os dois achados que mandei em 14:50 e no commit `3d3bca3` — "E35 não supera
D" e "hipótese central F1(A)≥0,95×F1(D) não sustentada" — foram medidos
**inteiramente no regime lote=128**, nas 3 sementes, em todos os 9 braços.
Se o sub-treino afeta os outros braços como afetou o D, essas duas
conclusões podem estar comparando modelos que não tiveram a chance de
convergir — o que muda o que elas significam.

**O que este teste NÃO responde**: eu testei só o braço D. Não sei se A, B, C
e E35 sofrem do mesmo sub-treino na mesma magnitude — é plausível que não
seja uniforme (braços menores como A/B/C, com ~12k itens, fazem menos passos
totais mesmo em lote 128, então o sub-treino relativo pode ser maior OU
menor — não dá para extrapolar sem medir).

## O que isso muda, e o que não muda

**Não muda**: a robustez multi-semente continua válida como método — é sobre
*qual regime* medir, não sobre quantas sementes.

**Pode mudar**: se A e E35 também saltarem ~20%+ de F1 em lote menor, aí sim
"E35 supera D" e "F1(A)≥0,95×F1(D)" podem voltar a valer — ou pelo menos
ficar mais perto. Não sei a resposta; só sei que o regime atual (lote 128)
não estava dando ao modelo a chance que o lote 16 deu.

## Recomendação, sem decidir por você

Antes de fechar a reescrita do Cap. 5 (minha mensagem 1450 propunha duas
opções, (a) reescrever com os números atuais ou (b) investigar mais) — **isto
é evidência de que (b) é necessário**, não só uma alternativa mais cautelosa.
Sugiro ao autor:

1. Retestar D, A, E35 (o mínimo para checar se o padrão se repete) em lote
   16, semente 42, mesma avaliação — 3 execuções, ~30 min cada pela
   velocidade real que acabei de medir (T4, não os ~3h que eu tinha
   projetado errado a partir do tempo legado). Menos de 2h de GPU.
2. Se o padrão se confirmar nos três, aí sim vale considerar rodar TODOS os
   9 braços × 3 sementes em lote menor antes de qualquer conclusão final do
   Cap. 5 — isso é ~9h de GPU (9 braços × 3 sementes × ~20-25 min), dentro
   da cota semanal.
3. Alternativa mais barata: já ADOTAR lote 16 (ou algo entre 16 e 128, ex.
   32) como o regime canônico definitivo, dado que ele é claramente melhor
   E não é caro (26 min por braço grande, medido agora) — e refazer tudo
   nesse regime de uma vez, em vez de comparar dois regimes em paralelo.

**Não vou disparar nada disso sozinho** — é decisão de escopo/custo do autor,
e a decisão sobre o Cap. 5 (mensagem 1450) deveria esperar por ela.

## O que já fiz

Resultado publicado: `activelearning@277717b`, arquivo com sufixo explícito
(`e3prime_D_s42_bs16.json`, não sobrescreve o D canônico). Plano v64
atualizado. Tarefa 2220 concluída.

Nota de tempo: a projeção de "~3h" que passei antes (baseada no tempo legado
de bs=16) estava errada — rodou em 26,4 min na T4. O tempo legado
provavelmente veio de um substrato mais lento, não do regime em si. Ajusto a
estimativa de custo das opções acima para refletir isso.
