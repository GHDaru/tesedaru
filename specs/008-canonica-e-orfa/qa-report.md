# QA — ciclo 008: classe canônica (ADR 0012) + invariante da órfã

**Tarefa:** 20260817-0420 · **Executor:** revisor2 · **Branch:** `ciclo/r3-t1-canonicas`
**Superfície travada:** `scripts/check-fichamentos.py` (lock de 2026-08-17T04:22Z)
**NÃO tocado:** `referencias.bib` — lock do revisor1. Tudo que achei nele sai
como sugestão, não como edição.

## DoD executável (princípio IX)

Nenhuma linha abaixo é julgamento; todas são comando com saída observada.

| # | Critério | Comando | Resultado |
|---|---|---|---|
| 1 | Invariante 7 REPROVA canônica com campo mínimo faltando | fixture isolado, `check-fichamentos.py` | **exit 1**, nomeando `UmaLinhaQuebrada` e o campo `['journal']` |
| 2 | Invariante 7 APROVA canônica correta | mesmo fixture | `LivroCanonicoOk` e `UmaLinhaOk` passam sem ruído |
| 3 | Invariante 7 não gera falso positivo em coletânea | `ColetaneaComEditor` (só `editor`) | passa — `editor` supre `author` |
| 4 | Invariante 7 lê entrada de UMA linha | `UmaLinhaOk`, com "=" dentro do título | passa; o título não vira campo |
| 5 | Aviso A2 ENXERGA a órfã | fixture com `OrfaDeFixture` | listada em A2 |
| 6 | Aviso A2 NÃO reprova o build | fixture com a órfã e nada mais errado | **exit 0** com a órfã ainda listada |
| 7 | As 5 fichas mínimas passam o verificador | `check-fichamentos.py Wilson1927 McNemar1947 Wilcoxon1945 EfronTibshirani1993 Kohavi1995` | `PROBLEMAS: nenhum`, **exit 0** |
| 8 | O repositório real não ganhou reprovação nova | `check-fichamentos.py` \| grep `referencias.bib:` | nenhuma linha — invariante 7 está verde no acervo atual |

O critério 6 é o que prova a ressalva que levei ao autor: a órfã aparece e
**não** derruba a execução. Com 126 órfãs no acervo, um invariante que
reprovasse nasceria vermelho e viraria DoD inalcançável — foi o defeito do
lote 5, e desta vez ele foi medido antes, não descoberto depois.

## O erro que cometi no meio do ciclo, e como apareceu

Ao rodar o verificador completo pela primeira vez, olhei só as primeiras linhas
da saída e **declarei que o invariante 7 não tinha acusado nada**. Estava errado:
ele acusara três entradas — `Cohn1996`, `Mitchell1982` e `Roy2001` — que ficaram
no fim de uma lista de 341 problemas preexistentes.

Pior: as três acusações eram **falso positivo meu**. Essas entradas estão
escritas em uma única linha, e minha primeira versão do parser só reconhecia
campo ancorado em início de linha. O verificador teria reprovado três entradas
perfeitas.

Causa-raiz e conserto: em vez de ancorar em início de linha (que quebra no
formato de uma linha) ou varrer `\w+ =` no texto cru (que confunde um "=" dentro
de um título com nome de campo), o parser agora **esvazia o conteúdo entre
chaves, respeitando aninhamento, e só então lê os nomes de campo do esqueleto**.
O critério 4 do DoD existe por causa desse erro e o mantém morto.

## Entregas

1. `scripts/check-fichamentos.py` — invariante 7 (classe canônica da ADR 0012,
   reprova) + avisos A1/A2 (não reprovam) + `--sem-avisos` + o conserto do
   parser.
2. Cinco fichas mínimas, cada uma com o resultado que a tese usa e o local
   exato (arquivo:linha) onde é usado: `Wilson1927`, `McNemar1947`,
   `Wilcoxon1945`, `EfronTibshirani1993`, `Kohavi1995`.
3. `fichamentos/verificacoes/pendencias-t1.md` — verificação das 7 pendências.

## Números do acervo, medidos (princípio V)

**Medição refeita após o gate do bib (`7f8e2b2`), que levou o arquivo de 378 a
337 entradas.** Os números da primeira medição estão registrados ao lado porque
a diferença entre eles é o efeito do saneamento, não um erro de contagem.

| Medida | Antes do gate do bib | **Agora (base `7f8e2b2`)** |
|---|---|---|
| entradas no `.bib` | 378 | **337** |
| fichamentos | 152 | **161** |
| aviso A1 (citada, sem ficha, não canônica) | 49 | **35** |
| aviso A2 (órfã) | 126 | **95** |
| reprovações do invariante 7 | 0 | **0** |

As pendências A1 são do repositório inteiro, não só do t1 — a ADR fala em 7
porque o recorte dela é o tema t1.

Rebase feito sobre `7f8e2b2`; as 5 fichas mínimas seguem verdes e o invariante 7
continua sem acusar nada no acervo saneado.

## Para o gate do autor

Os achados de `referencias.bib` que este ciclo levantou **já foram quase todos
corrigidos** no gate do bib aprovado em `ac31dcf`/`7f8e2b2` — confirmei um a um
contra o arquivo saneado:

| Achado | Situação |
|---|---|
| `Reusens2024` com DOI que abria outro artigo | **corrigido** — DOI, volume 254, páginas 124302 e URL agora corretos |
| `Kohavi1995` declarada como `@article` | **corrigido** — virou `@inproceedings` |
| Duplicatas `Devlin2019`/`devlin2019bert`, `Bayer2024`/`Bayer2024ActiveLLM`, `Zhang2025`/`Zhang2025LLMAL` | **resolvidas** — sobrou uma chave por obra |
| `Widodo2022`: última página e grafia do título | **ABERTO** — ainda `2407--2413` (correto: **2414**) e ainda "optimation" (correto: "optimi**z**ation"), ambos conferidos na Crossref pelo DOI `10.33395/sinkron.v7i4.11792` |

Ou seja, resta **um** item de bibliografia, pequeno e verificado. Não o corrigi
aqui porque o `referencias.bib` não é a minha superfície.
