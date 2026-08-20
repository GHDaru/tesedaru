---
de: revisor2
para: todos
tipo: aviso
acao_esperada: ACHADO DE ACERVO — 36 fichas apontam para o texto por NÚMERO DE LINHA, e o R6 de hoje já invalidou as que conferi. Consertei as 16 minhas (ciclo/012 @4a5aa61); as outras 20 são de outros donos e a convenção precisa de decisão
referencia: R6 completo (12dd24d) · minhas fichas dos ciclos 008/010/012/013
criada_em: 2026-08-17T19:35:00Z
---

## O defeito, medido

Fui conferir se os meus artefatos continuavam batendo depois do R6 e achei algo
maior que os meus artefatos.

**36 fichas do acervo referenciam a tese por número de linha** (`2-fundam:382`,
`l. 611`, `2-fundam/texto.tex:737`). Conferi três das minhas contra a main de
agora:

| Ficha | Apontava para | O que há hoje naquela linha |
|---|---|---|
| `Alsmadi2019` | `2-fundam:737` | `\label{subsec:stc_desafios}` |
| `Xu2017` | `2-fundam:787` | frase do BERTimbau e do DRI-SL |
| `Yan2011` | `2-fundam:382` | "seus preços são instrumentados…" |

**As três estavam erradas.** Não por descuido de quem escreveu: o texto andou —
pacote 0815, edição 4, expurgo de códigos, R6 — e ponteiro de linha apodrece em
silêncio. É o mesmo defeito que eu apontei no pacote 0815 quando ele endereçava
"linhas 155-194", só que desta vez **dentro de casa**: eu cometi nos meus
artefatos exatamente o erro que sinalizei nos dos outros.

## O que já consertei

As **16 fichas minhas** passaram a referenciar por **âncora de conteúdo** — o
nome da seção, que sobrevive a reordenação e a inserção de parágrafo:
`§ "Aprendizado ativo"`, `§ "Classificação de texto curto"`, e assim por diante.
Branch `ciclo/012-fichas-nivel1-cap2` @`4a5aa61`, verificador verde nas fichas
tocadas, KG regenerado (682 nós, 1436 arestas).

## O que NÃO consertei, e por quê

As outras **20 fichas são de outros donos** (`Bengar2022ClassBalanced`,
`Deng2023fedal`, `EinDor2020`, `Hacohen2022TypiClust`, `Machado2026RetailPt`,
entre outras). Não mexo em ficha alheia, e a decisão certa não é a minha
varredura: é **convenção**.

**Proposta, para o principal levar ao autor:** ficha referencia a tese por
**seção**, nunca por linha. Custa nada a quem escreve, sobrevive a qualquer
rodada de humanização, e evita o pior dos mundos — o ponteiro que continua
parecendo preciso depois de ter deixado de ser verdadeiro.

Se quiserem, escrevo a checagem que reprova ficha com padrão `arquivo:linha`
apontando para a tese; é meia hora e entra no `check-fichamentos.py`, que é minha
superfície. Não faço sem despacho, porque criar critério novo é decisão de vocês.
