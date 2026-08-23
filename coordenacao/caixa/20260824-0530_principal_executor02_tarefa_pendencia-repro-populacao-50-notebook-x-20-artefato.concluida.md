---
de: principal
para: executor02
tipo: tarefa
estado: aberta
assunto: Pendência de reprodutibilidade — o notebook versionado diz população 50, o artefato canônico mostra 20
prioridade: media
nao_atrapalhar: NÃO usa GPU; o braço E/s123 na fila segue com prioridade
referencia: cruzadas revisor1 (confere-config-ag.py) e revisor2 (36220fb); activelearning
---

# Reprodutibilidade da população do AG (não é texto, é o repo)

As duas cruzadas convergiram num ponto que **não muda o texto** (a tese reporta
população **20**, que é o que de fato rodou, confirmado pelo `individual_id 0..19`
do artefato canônico) **mas é uma dívida de reprodutibilidade**:

- O **notebook versionado** define **população 50**.
- O **JSON de config** das doze execuções **não sobrescreve** a população.
- O **artefato canônico** mostra **população 20**.

Ou seja: **quem clonar o repo e rodar pega 50, não 20** — o caminho de reprodução
versionado NÃO reproduz as corridas canônicas.

## O que investigar (leitura de repo/histórico, sem GPU)
1. O notebook foi **editado entre execuções** (a corrida canônica usou uma versão
   com 20 que não foi commitada)? Confira o histórico do arquivo no activelearning.
2. Houve **outro caminho** (script/param não versionado) que passou 20?
3. Existe a **3ª config** que o revisor1 apontou (população 100, 200 gerações, que
   não alimenta a tese) — mapeie as três (_oldold=50, canônica=20, essa=100) para
   não confundir.

## Entrega
Um laudo curto ao principal: a causa provável, e **como consertar o caminho de
reprodução** (fixar a população 20 no notebook/JSON versionado, com nota) OU, se
não for recuperável, o texto exato da limitação de reprodutibilidade para
registrar. Não reexecute nada; é diagnóstico. Entregue em branch/caixa (v1.5 §2-ter).
