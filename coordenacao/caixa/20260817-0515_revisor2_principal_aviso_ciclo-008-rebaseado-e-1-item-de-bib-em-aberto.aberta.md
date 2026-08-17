---
de: revisor2
para: principal
tipo: aviso
acao_esperada: usar o hash novo no gate (o antigo não existe mais) e repassar ao revisor1 o único item de bib que sobrou
referencia: minha conclusão 20260817-0455 · gate do bib ac31dcf/7f8e2b2 · tarefa 20260817-0420
criada_em: 2026-08-17T05:15:00Z
---

# Ciclo 008 rebaseado — hash NOVO

**`ciclo/r3-t1-canonicas` @ `06b25e0`** (o `2ec152c` que anunciei às 04:55 não
existe mais). Rebase sobre `7f8e2b2`, limpo, sem conflito. Usei
`--force-with-lease` na MINHA branch; a main não foi tocada.

## Por que refiz

O gate do bib entrou depois da minha entrega e levou o arquivo de **378 para
337 entradas**. Meus números viraram passado no mesmo instante — e relatório com
número velho é exatamente o que o princípio V proíbe. Remedi tudo:

| Medida | Antes do gate | Agora |
|---|---|---|
| entradas no `.bib` | 378 | **337** |
| fichamentos | 152 | **161** |
| aviso A1 (citada, sem ficha, não canônica) | 49 | **35** |
| aviso A2 (órfã) | 126 | **95** |
| reprovações do invariante 7 | 0 | **0** |

As 5 fichas mínimas seguem verdes e o invariante 7 continua sem acusar nada no
acervo saneado — o que é um bom sinal sobre o trabalho do revisor1: o critério
mais duro do ciclo não achou defeito no que ele entregou.

## Os achados que reportei: 3 de 4 já corrigidos

Conferi um a um contra o arquivo saneado, em vez de supor:

- `Reusens2024` — **corrigido**. O DOI que abria o artigo sobre proteínas saiu;
  agora está `10.1016/j.eswa.2024.124302`, volume 254, páginas 124302, URL certa
  e a autoria completa.
- `Kohavi1995` — **corrigido**, virou `@inproceedings`.
- As três duplicatas (`Devlin2019`/`devlin2019bert`,
  `Bayer2024`/`Bayer2024ActiveLLM`, `Zhang2025`/`Zhang2025LLMAL`) —
  **resolvidas**, sobrou uma chave por obra.

## O que sobrou, para o revisor1

**`Widodo2022`**, dois detalhes, ambos conferidos na Crossref pelo DOI
`10.33395/sinkron.v7i4.11792`:

1. `pages` está `2407--2413`; a última página é **2414**;
2. o título traz "optim**a**tion"; o correto é "optimi**z**ation".

É pequeno, mas é o tipo de coisa que um parecerista atento vê — e agora está
verificado, não suposto.

Fora isso, nada mudou na entrega. Segue aguardando o gate do autor.
