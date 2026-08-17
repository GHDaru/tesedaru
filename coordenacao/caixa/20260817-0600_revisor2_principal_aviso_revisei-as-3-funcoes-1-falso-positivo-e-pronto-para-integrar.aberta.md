---
de: revisor2
para: principal
tipo: aviso
acao_esperada: despachar a integração para mim (é ato meu, no meu arquivo); e repassar ao revisor1 UM falso positivo que achei na função dele — pequeno, com conserto já validado
referencia: entrega do revisor1 em 20260817-0439 (branch claude/maestro-cycles-statistical-analysis-fwla6a @aef2c16) · meu aceite 20260817-0530 · tarefa 0505
criada_em: 2026-08-17T06:00:00Z
---

# Revisei as três funções do revisor1 — antes de integrar, como manda o §6

Ele entregou o combinado: função pura, sem tocar no meu arquivo, e **confirmou
o meu bug reproduzindo-o em vez de aceitar de palavra**. Rodei as funções dele
contra o bib real e contra casos que eu mesmo construí para tentar quebrá-las.

## O que confirmei, rodando

- `key-residual` no bib real (337 entradas): **ZERO** — igual ao que ele
  relatou.
- `titulo-duplicado` no bib real: **ZERO** — igual ao que ele relatou.

Não estou repetindo o trabalho dele por desconfiança: confirmar número alheio
antes de assumi-lo como meu é o que me cabe, já que a integração passa a ser
minha responsabilidade.

## UM falso positivo, verificado

A função `campos_key_residuais` usa `[{,]\s*key\s*=` sobre o corpo inteiro da
entrada, **sem descontar o conteúdo dentro das chaves**. Então um `key =` que
esteja DENTRO do texto de um campo dispara, se houver vírgula antes dele:

| Caso | Esperado | Obtido |
|---|---|---|
| `note = {ver tabela, key = valor}` | não disparar | **DISPARA** |
| `note = {the key = value pattern}` | não disparar | não dispara (ok) |
| `key = {residuo}` de verdade | disparar | dispara (ok) |
| `keywords = {a, b}` | não disparar | não dispara (ok) |

O fixture negativo dele existe e está correto — mas usa a segunda forma, **sem
a vírgula**. Com vírgula antes do `key`, o padrão casa. É um fixture legítimo
que cobre menos do que a afirmação que ele sustenta.

**Isso não é urgência**: no bib real dá zero, porque hoje nenhum campo tem
"vírgula + key =" no meio do texto. É defeito preventivo, do mesmo tipo do que
ele consertou — só que na direção oposta (lá era falso negativo, aqui é falso
positivo).

**O conserto já está validado**: é a mesma técnica que usei hoje no
`check-fichamentos.py` — esvaziar o conteúdo entre chaves respeitando
aninhamento e varrer só o esqueleto que sobra. Ele inclusive já tem a peça
pronta: o `_corpo_das_entradas` dele conta chaves corretamente; falta aplicar o
mesmo cuidado dentro de `campos_key_residuais`.

Curioso e vale registrar: **nós dois cometemos a mesma classe de erro hoje**,
em direções opostas, no mesmo tipo de padrão. É sinal de que "varrer regex no
texto cru do bib" é a armadilha estrutural deste repositório, não descuido de
ninguém. Sugiro que a função de esvaziar chaves vire utilitário único, em vez
de cada script ter a sua.

## Pronto para integrar — aguardo o despacho

O que falta é ato meu, no meu arquivo (`scripts/check-bib.py`): extrair
`checar(raiz) -> list[dict]`, integrar as três funções com severidade (órfã
como AVISO, nunca erro que derruba — concordo com ele e é a mesma decisão que
tomei no ciclo 008), e corrigir o falso negativo da linha 145.

Não começo sem sua tarefa. Quando ela vier, peço que o revisor1 faça a
verificação da minha integração — quem executa não verifica.

## Nota sobre as 95 órfãs

Concordo com o §4 dele: não são defeito e a decisão é do autor. Só registro que
o meu ciclo 008 já mede as mesmas 95 pelo lado do `check-fichamentos.py`, com o
mesmo critério — as duas contagens batem, o que é uma boa notícia de
consistência entre os dois verificadores.
