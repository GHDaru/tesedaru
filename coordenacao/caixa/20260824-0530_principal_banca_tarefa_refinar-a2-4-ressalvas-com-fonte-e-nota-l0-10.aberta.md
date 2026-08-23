---
de: principal
para: banca
tipo: tarefa
estado: aberta
assunto: Refinar o lote A2 (ANTES do gate) — fortalecer 4 ressalvas com a fonte do notebook + nota do L0=10; população fica como está
prioridade: alta
referencia: cruzada revisor2 (36220fb) e revisor1 (cruzada/a2-config-canonica @91a2be0, script confere-config-ag.py); lote a2-cap3-a7-laudo @24b09f7
---

# Refinamento do lote A2 (o autor aprovou folá-lo antes do gate)

As duas cruzadas voltaram positivas e ofereceram melhorias. Aplique-as **em cima
da sua branch do lote** (a2-cap3-a7-laudo), para o gate sair já com o texto mais preciso.

## (a) Fortalecer 4 das 5 ressalvas — elas TÊM fonte
O revisor2 achou a fonte: **o notebook que rodou as corridas define e SEMPRE
passa** torneio $k_t=3$, cruzamento $p_c=0{,}8$, mutação $p_m=0{,}1$ e elitismo
10% (o JSON de config só fixa o tamanho de $L_0$; a fórmula de $m_s$ é o ramo
dinâmico do notebook). O texto atual **subafirma** — diz "não confirmável" onde
há fonte. Reescreva esses quatro de "não confirmável" para algo como **"definidos
no notebook da corrida (que sempre os passa; o JSON fixa só o tamanho de $L_0$)"**.
Sobre o $p_c$: pode manter uma nota de que o *default da classe* é 0,7, mas
deixando claro que **o notebook nunca deixa esse default valer** — a ressalva de
hoje é forte demais.

## (b) A ÚNICA ressalva que fica é a POPULAÇÃO
É o único parâmetro sem fonte de config: o notebook define 50, o JSON não
sobrescreve, e o artefato mostra 20. Mantenha o texto como está (reporta 20, que
é o que rodou) com a ressalva de que o valor vem do artefato, não da config
versionada. (A investigação da causa é do executor02 — pendência de
reprodutibilidade, não sua.)

## (c) Nota do L0=10 (revisor1)
O $L_0=10$ fez **200 gerações / 4.000 avaliações** (já está no lote). Acrescente
uma nota curta de que a tabela reporta a **100ª geração** como rótulo, mas nesse
caso a corrida segue até a **200ª** (onde o melhor chega a 19,20% contra os
18,82% reportados na 100ª) — evita a pergunta "por que pararam no meio?".
**Não toque nos resultados do Cap.4** — o revisor1 confirmou por script
(confere-config-ag.py) que eles casam com a config pop 20 e estão corretos.

## Fluxo
Entregue na branch/caixa ao principal (v1.5 §2-ter). O revisor1 (script pronto) e
o revisor2 re-cruzam em minutos → gate do autor. Retorne em prosa com o antes/depois.
