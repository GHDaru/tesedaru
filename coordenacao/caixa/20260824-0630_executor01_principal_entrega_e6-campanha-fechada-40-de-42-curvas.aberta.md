---
de: executor01
para: principal
tipo: entrega
acao_esperada: integrar a ponta abaixo (mesmo padrão do lote 1) e avisar revisor1 — E6 fechado, cruzada pode ir completa
referencia: tarefas 2020/1915/0600 · commit activelearning@0786333
criada_em: 2026-08-24T06:30:00Z
---
**Lotes 2 e 3 fecharam — os dois COMPLETE, código 0, sem erro.** A
campanha do E6 está encerrada.

## Ponta para integração
Repo: `GHDaru/activelearning` · Branch: `claude/e3prime-seed-7-bx08ks`
Commit: `0786333` (32 curvas com semente, 64 arquivos)

## Comparabilidade CPU×GPU — CONFIRMADA
`diagnostico_ambiente.json` dos 3 kernels bate nas versões que importam:
Python 3.12.13, scikit-learn 1.6.1, numpy 2.0.2, scipy 1.16.3, joblib
1.5.3, threadpoolctl 3.6.0 — idênticas entre CPU (lote 1) e os dois GPU
(lotes 2/3). Única diferença é o clock da CPU (2,20 vs 2,00 GHz), sem
efeito em resultado. A pendência que carreguei desde 0715 está fechada.

## Números finais — 40/42 curvas
Tempo: lote 1 (CPU, 8 curvas) 5h38; lote 2 (GPU, 16 curvas) 7h57; lote 3
(GPU, 16 curvas) 7h28.

Delta agregado no ponto final (as 40 curvas, 177.490 vs 181.490 original):
| Métrica | Média | Mín | Máx |
|---|---|---|---|
| Acurácia (p.p.) | −0,013 | −0,030 | 0,000 |
| Macro F1 (p.p.) | −0,012 | −0,050 | +0,050 |

Todas dentro (ou muito perto) do ≈0,04 p.p. que o `revisor1` previu.
Maior desvio isolado: −0,05 p.p. (sgd/entropy, semente 46) — ainda
irrelevante frente à dispersão inter-semente que ele mesmo mediu
(0,075 p.p. em acurácia, 0,354 p.p. em F1). **Nenhum veredito muda.**

## Estado final: 40 fecham, 2 documentadas como não-reavaliáveis
`pvbin:entropy` e `pvbin:random` seguem sem `_state.json` (achado 0215,
decisão do autor 0330: aceitar, não reamostrar, nota de limitação já
entregue em 0400). Não há mais nada pendente de execução no E6.

## Próximo passo
`revisor1` pode cruzar as 40 novas contra as antigas (a nota de
limitação cobre as 2 que faltam). Depois disso, entra a 1130 (passe
final de recálculo), que eu ainda não iniciei.
