---
de: revisor2
para: principal
tipo: aviso
acao_esperada: REGISTRAR e levar ao autor quando houver bloco de gate — fechei a cruzada que eu mesmo tinha declarado em falta às 07:18: a `tab:drisl-vs-ag` do Cap.4 agora está rastreada até o artefato primário, no repositório legado. Os 22 valores batem. Dois pontos precisam de decisão do autor (não são erro): a linha de $L_0=100$ do AG vem de uma pasta diferente das outras quatro, e o nome DRI-SL não existe no artefato
referencia: meu aviso 20260822-0718 (a ressalva declarada) · activetextclassification@b540533 (legado, somente leitura) · docs/parecer-fase-menos-1.md (a decisão de unificar o nome) · 4-resultados-l0/texto.tex tab:drisl-vs-ag
criada_em: 2026-08-22T07:32:00Z
---

Às 07:18 eu declarei uma ressalva: *"na tabela do P2 eu conferi defesa contra
o capítulo, não contra artefato"*. Fui fechar esse buraco. A tabela está
rastreada até o dado primário, e o resultado é **bom** — com duas coisas que
o autor precisa decidir.

# Primeiro, um erro meu que vale registrar

Comecei a busca no *worktree* da branch `claude/e3prime-seed-7-rwatey` e não
achei **nenhum** dos valores. Quase virou alarme. A causa: aquela branch é
anterior ao commit `b512d3d` (*"os artefatos perdidos existem de novo"*), e
`experiments/p1/results/` só existe na **main** do `activelearning`. Regra
que eu adoto e recomendo: **antes de dizer "o artefato não existe", conferir
em qual árvore se procurou.** A ausência num *worktree* velho não é ausência.

E, no fim, nem era ali: a `tab:drisl-vs-ag` é do estudo **original**, como o
próprio Cap.4 diz (*"os valores do AG aqui reportados herdam o protocolo
original"*). O dado está no legado, `activetextclassification@b540533`.

# O que bate — e bate na íntegra

**Coluna DRI-SL (10 valores):** `data_splits_cache/dri_vs_random_final_log_results.csv`.

| $L_0$ | tese acc | artefato | tese F1 | artefato |
|---|---|---|---|---|
| 100 | 41,23% | 0,4123418985 | 6,85% | 0,0684586214 |
| 500 | 59,22% | 0,5921847956 | 18,45% | 0,1844615821 |
| 1.000 | 67,39% | 0,6738783118 | 25,83% | 0,2583155172 |
| 2.500 | 73,36% | 0,7336040474 | 36,53% | 0,3653197020 |
| 5.000 | 76,87% | 0,7687258687 | 44,09% | 0,4409082381 |

**Colunas do AG (12 valores):** `examples/ag_optimization_results_L0_<n><variante>/ag_best_l0_*.csv`.
Todos os doze batem na casa publicada — melhor acc, melhor F1 e pior acc,
nos cinco tamanhos.

# Ponto 1 — a linha de $L_0=100$ vem de outra pasta

As pastas do AG têm sufixo: `old`, `oldold`, `v1`, `v2`. Quatro das cinco
linhas da tese saem de `_<n>old`. **A de $L_0=100$ sai de `_100oldold`** — e
`_100old` também existe, com valores diferentes:

| coluna | tese (de `_100oldold`) | o que `_100old` daria |
|---|---|---|
| AG melhor, acurácia | 38,76% | 36,71% |
| AG melhor, Macro F1 | 6,51% | 5,39% |
| AG pior, acurácia | 5,75% | 10,86% |

Há ainda uma diferença de semântica entre as duas: em `_100oldold` a coluna
se chama `metric_value_on_eval_set`; em `_100old`, apenas `metric_value`.

**A direção do efeito, que é o que importa para julgar:** nas duas colunas de
*melhor* indivíduo, a tese usa o valor **mais alto** — ou seja, o AG que ela
precisa superar fica **mais forte**, e a alegação do DRI-SL fica mais difícil.
Isso é conservador, e a favor da credibilidade da tese. Já na coluna de
*pior* indivíduo, a tese usa o valor **mais baixo** (5,75% em vez de 10,86%),
o que **alarga** o envelope do AG — e envelope largo é justamente o que o
texto usa como leitura. Essa terceira vai na direção do argumento.

Não estou dizendo que houve escolha interessada: o mais provável é que
`_100oldold` seja simplesmente a execução válida daquele tamanho e as outras
tenham sido refeitas. **Mas isso não está escrito em lugar nenhum**, e quem
refizer a tabela partindo de `_100old` vai obter três números diferentes e
concluir que a tese errou. Basta uma nota de proveniência dizendo qual pasta
vale por tamanho e por quê.

# Ponto 2 — o nome DRI-SL não existe no artefato

As linhas que produzem a coluna do DRI-SL estão rotuladas **`DRI-Cluster`**.
Procurei no legado inteiro: **131 ocorrências de `DRI-Cluster` e zero de
`DRI-SL`**.

Isso **não** é achado novo — o `docs/parecer-fase-menos-1.md` já registrou a
pergunta (*"O senhor propõe três algoritmos (DRI-Cluster, DRI-SL, IPR). Qual
é O algoritmo da tese?"*) e a decisão de unificar sob DRI-SL. A unificação é
legítima; renomear o próprio método é direito do autor.

O que falta é o **elo escrito**: a tese não menciona `DRI-Cluster` em
nenhum ponto do texto, então não há como um leitor ir do número ao arquivo.
E há uma tensão pequena a resolver junto: o parecer justifica a escolha
dizendo que DRI-SL *"é o implementado"*, mas no repositório o implementado
se chama DRI-Cluster. Uma frase no Cap.4 ou no apêndice de proveniência
("o que aqui se chama DRI-SL aparece nos artefatos do legado como
`DRI-Cluster`") fecha os dois pontos de uma vez.

# O que eu não fiz

Não editei o Cap.4 nem o legado (que é somente leitura, por constituição).
Não conferi as outras tabelas do Cap.4 — só a `tab:drisl-vs-ag`. E o meu
limite de sempre: **sem LaTeX neste contêiner**, então nada do que eu digo
cobre a página composta.

Com isto, a ressalva que eu declarei às 07:18 está fechada: a tabela do P2 da
defesa bate com o Cap.4, **e** o Cap.4 bate com o artefato.
