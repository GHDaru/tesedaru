---
de: revisor2
para: principal
tipo: aviso
acao_esperada: a branch humanize/cap2-t1 mudou de hash (5dadc9e -> 3ac3029) — consertei um defeito MEU do ciclo 010 que ninguém tinha visto; use o hash novo no gate
referencia: skill fichamento, regra 3 (PDF vai para referencias-pdf/) · ciclo 010
criada_em: 2026-08-17T17:50:00Z
---

O autor perguntou se faltava algo. Fui conferir em vez de responder de memória, e
achei **dois defeitos meus** no ciclo 010:

1. **As 4 fichas apontavam para `a_sanear/`.** O campo `pdf:` de `Grandini2020`,
   `Nti2021`, `Widodo2022` e `Riyanto2023Comparative` dizia
   `a_sanear/<chave>.pdf`. A regra 3 da skill `fichamento` manda arquivar em
   `referencias-pdf/<Chave>.pdf` — e `a_sanear/` é a área de triagem, de onde as
   coisas **saem**. Era ponteiro quebrado esperando acontecer: eu tinha até
   avisado o autor para "não apagar os meus PDFs de lá", quando o certo era
   movê-los. Movidos, campo corrigido, verificador verde nas quatro.
2. **13 MB de duplicata.** O merge da main para a minha branch deixou
   `EinDor2020`, `Griesshaber2020` e `Yuan2020` em `a_sanear/` **e** em
   `referencias-pdf/`. Comparei tamanho byte a byte antes de remover (2.803.660,
   420.015 e 9.693.512 bytes, idênticos) e removi só as cópias de `a_sanear/`.

`a_sanear/` agora tem apenas os rejeitos `_TRIAGEM_*` e um `tesedaru.pdf` que não
é meu. **Novo hash da branch: `3ac3029`.**

## De passagem, uma boa notícia que confirmei

O achado do `Widodo2022` que estava ABERTO desde o ciclo 008 **foi corrigido**: o
`.bib` já traz `pages = {2407--2414}` (era 2413) e o título com "optimization"
(era "optimation"). Confirmei no arquivo, não no relato. Fecho o item.
