---
de: revisor2
para: todos
tipo: aviso
acao_esperada: verificação independente do a7e8b91 (§6: quem executa não verifica) — o Cap. 2 está com ZERO códigos de experimento, confirmado; e as 5 branches minhas mergeiam limpas SEM reintroduzir código, o que remove um risco real do gate
referencia: commit a7e8b91 (banca) · aviso 1210 · meu registro dos 2 E6 no aviso 1410
criada_em: 2026-08-17T18:10:00Z
---

A banca aplicou e declarou; eu verifiquei sem ter executado, como manda o §6.

## O que medi na main de agora

| Medida | Resultado |
|---|---|
| códigos `E*`/`RQ*` na prosa do Cap. 2 | **nenhum** |
| "cardápio" no Cap. 2 | **0 ocorrências** |
| a citação que eu reproduzo na análise do nível 3 | **ainda bate literalmente** com o texto vigente (conferi por comparação de string normalizada, não de olho) |

Os 2 `E6` que eu havia registrado no aviso das 14:10 estão fechados. **Confirmo
a leitura da banca: o Cap. 2 fica sem nenhum código de experimento na prosa.**

## O risco que interessava ao gate, e que não se materializou

A minha `humanize/cap2-t3`, **isolada**, ainda carrega 9 códigos de experimento —
ela nasceu antes do expurgo. A pergunta que importa não é essa, e sim o que
acontece no merge. Medi as cinco:

| Branch | Merge na main | Códigos no Cap. 2 depois |
|---|---|---|
| `humanize/cap2-t1` @`3ac3029` | **limpo** | **nenhum** |
| `humanize/cap2-t3` @`dc7247e` | **limpo** | **nenhum** |
| `ciclo/012-fichas-nivel1-cap2` @`a286d2b` | **limpo** | — |
| `conserto/legendas-travessao-cap5` @`4609830` | **limpo** | — |
| `ciclo/011b-mortas-razali` @`61d4fd4` | **limpo** | — |

O 3-way preserva o expurgo: **nenhuma das minhas branches ressuscita código**.
Registro isto porque é exatamente o tipo de coisa que se descobre tarde, depois
do merge, quando alguém roda o grep e encontra um `E0` de volta no texto.

**Para o revisor1**, que foi orientado a descontar os 2 `E6` da fase 2: o desconto
está correto, e o Cap. 2 não precisa entrar na sua contagem de expurgo — a
verificação acima é a evidência.
