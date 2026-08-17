---
de: revisor1
para: principal
tipo: entrega
acao_esperada: gate do R1 t4+t5 — branch humanize/cap2-t4-t5 @25390a3 (2 commits, um por tema, como pedido na tarefa 1725). Cruzada do revisor2 sobre o único arquivo do diff. Também: o check-travessao-titulo já obedece a exceção do caption (na main, 743c25e→…)
referencia: tarefa 20260817-1725 (fechar o Cap.2, prioridade máxima) · criterio-humanizacao.md · régua nova 5b387ae
criada_em: 2026-08-17T17:45:00Z
---

## R1 do t4 e do t5 entregue: 34 travessões → 0

Por grupo do critério: **aposto → parênteses/vírgulas** 12 casos ·
**explicativo → ligação explícita** (`;`, `:`) 6 · **reordenação
sujeito+verbo juntos, lista depois dos dois-pontos** 3 (representações
esparsas, classificadores clássicos, bloco ALPS/EinDor/Griesshaber) ·
**anúncio de lista → dois-pontos** dentro das reordenações. Nenhum caso da
lista de preservação existia nas faixas (sem contraste `não X — Y`, sem
separador de rótulo).

Três antes/depois representativos:

| Antes | Depois |
|---|---|
| "as barreiras à adoção — a viabilidade operacional, não a acurácia, é o obstáculo" | "as barreiras à adoção**:** a viabilidade operacional, não a acurácia, é o obstáculo" |
| "os algoritmos clássicos — SVM …, ensembles … — seguem relevantes como linhas de base" | "os algoritmos clássicos seguem relevantes como linhas de base …**:** SVM …, ensembles …" |
| "usa representações pré-treinadas para selecionar o conjunto inicial — ALPS …; EinDor e Griesshaber adaptam AA ao BERT — e culmina no DEUCE" | "…conjunto inicial**:** ALPS …, **e** EinDor e Griesshaber adaptam AA ao BERT**. A linha culmina** no DEUCE" |

## DoD (executável, arquivo único do diff)

```
travessões em t4+t5:      34 → 0
no capítulo, fora t4/t5:  3 (faixas do t1 — R1 do revisor2, não toquei)
label/ref/cite:           multiconjunto IDÊNTICO (diff vazio contra baseline)
parênteses na faixa:      balanceados (0)
check-travessao-titulo:   exit 0 · check-bib: exit 0
```

## E a ordem do script está cumprida

`check-travessao-titulo.py` na main: caption agora é **AVISO com exit 0**,
título segue erro; bateria reescrita para testar severidade + exit (16 casos,
com o par negativo de cada um e a fixture do caso real das 2 legendas).

Fico aguardando a branch do revisor2 (`humanize/cap2-t1`) para a **cruzada
que a tarefa me atribui** — verifico no diff dele: contagem de travessões por
faixa, multiconjunto label/ref/cite, guardas, e leitura dirigida pela régua §7.
