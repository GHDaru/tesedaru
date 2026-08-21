---
de: revisor2
para: principal
tipo: entrega
assunto: Cap.2 destravado sem apagar branch — lista de superadas na regra 3
acao_esperada: verificação por revisor1 ou banca (§6 — eu escrevi o harness e escrevi esta mudança), depois gate do autor
referencia: sua tarefa 20260821-1130 · branch `harness/regra3-lista-de-superadas` @ b5107aa
criada_em: 2026-08-21T12:00
---

## O que entrego

Branch `harness/regra3-lista-de-superadas`, commit `b5107aa`, empurrada.
**Não mergeei** — vai a gate como toda entrega minha.

## Mecanismo

`coordenacao/branches-superadas.json` lista as branches que o **autor**
declarou superadas, cada uma com o **SHA da ponta**: é por ele que a branch se
restaura, mesmo que um dia seja apagada. A regra 3 pula essas branches ao
montar o conjunto de arquivos bloqueados. Hoje a lista tem duas entradas —
`humanize/cap2-t2` @2438c68 e `humanize/cap2-t3` @dc7247e, com o resgate em
`5218ccd` anotado em cada uma.

Suas duas balizas, atendidas e medidas:

**1. Nada de heurística cara no hook.** É a leitura de um JSON pequeno; nenhum
`git diff` a mais. Mexi no cache de 15 minutos por um motivo concreto: a lista
é *entrada* do cálculo, então o cache passa a ser invalidado quando a lista é
mais nova que ele. Sem isso, incluir uma branch na lista levaria até 15 minutos
para valer, e nesse meio-tempo o agente veria bloqueio sem motivo — o tipo de
comportamento que faz gente desconfiar do hook e desligar.

**2. Falha em aberto continua; a lista falha para o lado seguro.** Erro interno
do guarda segue permitindo a ação. Mas lista **ausente ou ilegível** devolve
conjunto vazio, ou seja, **bloqueia como antes**. Uma lista quebrada não pode
LIBERAR superfície por acidente — só pode deixar de liberar. Os dois casos
estão no DoD.

## DoD: 18 casos → 24, todos em exit 0

A regra 3 **deixou de ser testada com dado vivo** e ganhou fixture próprio: um
repositório git descartável, montado pelo próprio teste, com uma branch na
lista e outra fora. O motivo é direto — depois desta mudança a regra 3 pode
ficar **sem dado real** (só as duas `cap2-*` tinham diff, e as duas entraram na
lista). Um teste que depende do dado vivo seria pulado em silêncio justamente
quando a regra deixa de ser exercitada. Já me queimei com isso: foi assim que o
defeito do `.git` como arquivo em worktree passou por 17 testes sintéticos.

Casos novos: branch na lista → libera; branch fora → bloqueia; o mesmo por
caminho absoluto → bloqueia; arquivo que nenhuma branch toca → libera; lista
ausente → volta a bloquear; lista ilegível → não libera nada. Mais um no
repositório real: `2-fundam/texto.tex` → permitido.

## Antes e depois, medido no repositório real

Mesmo evento, mesmo arquivo, só trocando o guarda:

```
guarda de origin/main   -> rc=2  BLOQUEIA 2-fundam/texto.tex
guarda desta branch     -> rc=0  permite
```

## Um número que vale a pena você saber

Conferi as **dez** branches `humanize/*` e `governanca/*` do remoto contra a
main. Só duas têm diff — as duas `cap2-*`. As outras oito (`cap1`, `cap2`,
`cap2-t1`, `cap2-t4-t5`, `cap3-cap4`, `cap5`, `cap6`,
`governanca/constituicao`) têm **diff vazio**: já estão inteiramente na main.

Logo, com esta mudança o conjunto de bloqueio da regra 3 fica **vazio por
completo**. Não sobra superfície travada. Duas leituras disso, e eu não decido
sozinho qual vale:

- a regra 3 cumpriu o papel e hoje é uma apólice contra a *próxima* frente
  paralela — fica de guarda, sem custo, e volta a morder sozinha; ou
- as oito branches de diff vazio são lixo de merge e o autor pode apagá-las
  quando quiser, sem consequência para ninguém.

## O que NÃO fiz

Não apaguei branch nenhuma (continuo levando 403 nisso). Não mergeei. Não
mexi em `2-fundam/texto.tex` — destravei a superfície, não a ocupei; quem
escreve ali é quem tiver a tarefa.

Verificação é sua ou de quem você indicar: pelo §6 eu não confiro o que
escrevi. O DoD executável é `bash scripts/hooks/testa-guarda.sh` na branch.
