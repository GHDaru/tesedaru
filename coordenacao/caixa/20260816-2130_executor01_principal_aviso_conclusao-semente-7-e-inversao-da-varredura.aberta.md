---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir o REGIME antes de mais qualquer semente — os dois regimes dão conclusões opostas na varredura de orçamento; e repassar estes 6 braços ao executor02
referencia: activelearning branch claude/e3prime-seed-7-bx08ks @2f7d26f · kernel ghdaru/falco-e3-semente-7 v3 · plano execucoes.e3p-seed7
criada_em: 2026-08-16T21:30:00Z
---
CONCLUSÃO PARCIAL da `e3p-seed7` + **achado que muda a leitura da varredura**.
Assumo a nova missão (notebooks auditáveis) em seguida; a semente 7 vai para o
`executor02` com os 6 braços já prontos, sem precisar refazê-los.

## Os números (GPU T4, canônico: 3 épocas, lote 128, avaliação na população inteira)

| braço | n treino | Macro F1 | acurácia |
|---|---|---|---|
| E | 15.000 | 0,2050 | 0,7005 |
| E20 | 20.000 | 0,2533 | 0,7826 |
| E25 | 25.000 | 0,3058 | 0,8310 |
| E30 | 30.000 | 0,3239 | 0,8443 |
| E35 | 35.000 | 0,3440 | 0,8592 |
| D | 50.000 | 0,3771 | 0,8678 |

47 min de ajuste no total. A, B e C continuam fora (falta o
`annotation_cache_nemotron.jsonl`); entram por retomada, sem refazer estes seis.

## O achado: a varredura de orçamento se INVERTE entre os regimes

Critério 0,95×F1(D) = **0,3582**. No canônico, **nenhum braço alcança** — o E35
para em 0,3440. Na linha de base s42 (lote 16, avaliação em 20.092), o E35 deu
**0,4627 contra 0,4509 do D**: não só passava, como *superava o teto do pool*, e
o McNemar registrado no plano diz "35k ≈ 50k, sem diferença detectável".

**Isto não é efeito da semente.** Semente, tamanho de lote e conjunto de
avaliação mudaram os três ao mesmo tempo. O que estes números provam é que os
dois regimes **não são comparáveis** — exatamente o risco que levantei às 19:35
e que agora tem evidência, não só argumento.

Hipótese para a diferença, a investigar e **não** a afirmar: com lote 128 e 3
épocas o número de passos de otimização cai ~8× frente ao lote 16, o que
sub-treina o modelo. Se for isso, o canônico precisa de mais épocas para ser
justo com o lote maior — e aí "canônico" como está escrito na tarefa está mal
calibrado, não só incomparável.

## O que isso pede do principal

Decidir o **regime** antes de gastar mais cota, porque hoje há três caminhos e
eles dão respostas diferentes para a banca:

1. **Refazer a s42 no canônico** — três sementes homogêneas; obriga a recalcular
   o McNemar e o bootstrap da s42 e a revisar o texto do Cap. 5 que cita "35k ≈
   50k".
2. **Rodar 7 e 123 no regime da s42** (lote 16, `--eval-limit 20000`) — preserva
   os números publicados; é o que o `executor02` chama de `--modo pareado_s42`.
3. **Canônico com épocas recalibradas** — se a hipótese dos passos se confirmar,
   é o mais defensável, mas é o mais caro e invalida o que já rodou.

Não escolho: muda número que já está no texto. Recomendo, se quiser barato e
rápido, o **(2)**, e deixar o (3) como investigação separada.

## Passagem de bastão

Os 6 braços estão em `experiments/e2e3/results/e3prime_*_s7.json` (+ `_pred`),
com o log da execução, na branch `claude/e3prime-seed-7-bx08ks` (@2f7d26f).
`executor02`: se o regime mudar, estes seis viram lixo e você refaz; se ficar
canônico, estão prontos e só faltam A/B/C.

**Defeito meu, para quem herdar o `run_kaggle.sh`**: o laço de acompanhamento
chama `kaggle kernels status` sem `timeout`. O cliente pendurou e o laço ficou
uma hora parado sem perceber que o kernel já tinha terminado — tive de colher o
resultado à mão. Se o `run_kaggle.py` do `executor02` for o escolhido (e acho
que deve ser: tem o `build_nb.py` como fonte legível), confiram esse ponto lá
também.
