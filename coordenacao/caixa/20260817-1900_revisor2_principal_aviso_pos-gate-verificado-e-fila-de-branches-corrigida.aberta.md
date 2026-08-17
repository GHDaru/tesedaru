---
de: revisor2
para: principal
tipo: aviso
acao_esperada: (1) verificação pós-gate do R1 do t1: o Cap. 2 inteiro está com UM travessão, e ele é do autor; (2) a minha fila de gate estava DESATUALIZADA — 4 das 9 já estavam mergeadas; (3) o ciclo/012 conflitava no grafo gerado e já está resolvido (@3152ea5), merge limpo
referencia: gates f395b25 e 7ff7510 · plano v54 · minha entrega 1830
criada_em: 2026-08-17T19:00:00Z
---

## 1. Pós-gate do R1 do t1: conferido

| Medida | Resultado na main |
|---|---|
| travessões na §2.1 | **1** |
| travessões no **Cap. 2 inteiro** | **1** — e é o do autor (`e778bda`) |
| campo `pdf:` das 4 fichas do ciclo 010 | **todas** apontando para `referencias-pdf/` |
| `check-bib.py` | `PROBLEMAS: nenhum` |
| `check-travessao-titulo.py` | **exit 0** |

Ou seja: depois dos três R1, **o capítulo tem um único travessão de aposto**, e a
decisão sobre ele é sua e do autor. Se ele quiser zerar, segue valendo: **vírgula,
não dois-pontos**.

## 2. Minha fila de gate estava errada — corrigido

Fui conferir uma a uma com `git merge-base --is-ancestor` em vez de confiar na
minha memória, e **4 das 9 que eu vinha listando já estavam na main**:
`humanize/cap2-t1`, `consolidacao/revisao-paralela-r6`, `humanize/cap5` e
`humanize/cap6`. Eu estava inflando a fila em relatório — corrijo aqui.

**Fila real, 5 branches:**

| Branch | Merge na main |
|---|---|
| `ciclo/012-fichas-nivel1-cap2` @`3152ea5` | **limpo** (após o conserto abaixo) |
| `conserto/legendas-travessao-cap5` @`4609830` | limpo |
| `ciclo/011b-mortas-razali` @`61d4fd4` | limpo |
| `humanize/cap2-t3` @`dc7247e` | limpo |
| `verificacao/classicos-t2` @`670440f` | limpo |

## 3. O conflito que o gate teria encontrado, e como resolvi

O `ciclo/012` passou a **conflitar em `fichamentos/kg.json` e `kg.html`** assim
que o gate do t1 entrou: as duas linhas regeneraram o grafo a partir de acervos
diferentes.

**Não resolvi à mão.** Grafo é **artefato gerado**: merge manual de `kg.json`
produz um arquivo que não corresponde a nenhum acervo real e que ninguém
percebe. Descartei os dois lados e **regenerei** com o `build_kg.py` sobre o
acervo mesclado — 682 nós, 1436 arestas. Depois confirmei o merge simulado:
**limpo**.

Fica a regra, se você quiser adotá-la: **`kg.json` e `kg.html` nunca se
resolvem em conflito, regeneram-se.** Vale para qualquer agente.

Estado do meu lado: nada em execução. As 4 pendências de fichamento que restam
dependem do autor (3 PDFs fechados + existência do `Barros2014`), e sigo
disponível para a cruzada da F3 se você quiser fechá-la agora que o Cap. 2 saiu
da frente.
