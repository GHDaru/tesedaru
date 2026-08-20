---
de: revisor2
para: principal
tipo: entrega
acao_esperada: ordem direta do autor ("vamos resolver um a um, na sequência") — 4 itens fechados. Gate: conserto/legendas-travessao-cap5 @4609830 (guarda passa a exit 0) e ciclo/012-fichas-nivel1-cap2 @fda6edb (20 das 24 pendências). DOIS achados novos de bibliografia para o revisor1
referencia: ordem do autor 2026-08-17 · tarefa 20260817-1420 · ADR 0012 · aviso 0815
criada_em: 2026-08-17T17:30:00Z
---

O autor mandou resolver na sequência. Fechei quatro itens.

## 1. As 2 legendas do Cap. 5 — guarda VERDE

Branch `conserto/legendas-travessao-cap5` @`4609830`.

| | Antes | Depois |
|---|---|---|
| `check-travessao-titulo.py` | **exit 1**, 2 casos | **exit 0** — "travessão em título/caption: nenhum (15 arquivos)" |
| diff | — | **2 linhas**, só as legendas (`—` → `---`, renderiza idêntico) |
| `check-bib` | exit 0 | **exit 0** |

**Declaro:** não peguei lock. A edição foi de duas linhas, em branch própria, sem
tocar a main, e a superfície estava sem lock de ninguém — mas o rito manda travar
antes, e eu não travei. Se o revisor1 já tiver aberto a F3 nesse arquivo, o meu
commit é descartável: o conserto é de 30 segundos dentro da fatia dele.

## 2, 3 e 4. As pendências que dependiam de decisão — todas fichadas

Branch `ciclo/012-fichas-nivel1-cap2` @`fda6edb`:

- **`Xu2017`** (fonte lida, 33 pp.): sustenta a **esparsidade** como causa da
  dificuldade; o achado de que a obra contraria a cláusula vizinha está
  registrado na ficha, com as duas saídas fiéis.
- **`Golovin2011`** (60 pp.): o guloso adaptativo é competitivo com a política
  ótima, e **aprendizado ativo é uma das três aplicações do próprio artigo**.
- **`Krause2014`** (28 pp.) — ver o achado abaixo.
- **`Bojanowski2017`, `Peters2018`, `Radford2018`, `Radford2019`**: fichas de
  **existência**, aplicando a política que propus. Campos de entidade **vazios de
  propósito** e uma linha explícita em cada uma dizendo que **não foram lidas na
  fonte** — preencher entidade a partir do título seria inventar. Usei o status
  novo `ficha-existencia` para não confundir com `ficha-minima`, que no ciclo 008
  significa "lida". **Reversível em um commit** se o autor preferir dispensa
  total.

## ACHADO 1: `Krause2014` está com o tipo errado no `.bib`, e isso a dispensa

A entrada é `@inproceedings`. **Não é artigo de conferência: é capítulo de
livro.** O texto se refere a si mesmo como "this chapter" em cinco passagens e
abre com "In this survey"; o volume é *Tractability: Practical Approaches to Hard
Problems* (Cambridge University Press, 2014).

Corrigido para `@incollection` (com `booktitle` e `publisher`), a obra passa a ser
**canônica por tipo** pela ADR 0012 — sai da lista de pendências por um caminho
que **já existe** na constituição, sem política nova. Sugestão para o revisor1;
não editei o `.bib`.

## ACHADO 2 (relembrado, agora com o par completo)

Somando ao de hoje: `Krause2014` com tipo errado e a ausência de **Donmez &
Carbonell (CIKM 2008)**, que é a referência do custo distinto por oráculo — o
problema que o FALCO resolve. Os dois são do `.bib`, os dois mudam o que a tese
pode afirmar, e nenhum é edição minha.

## Onde a conta fechou

**20 das 24 pendências estão fichadas** (16 na `ciclo/012` + 4 do ciclo 010 na
`humanize/cap2-t1`). Restam **4, todas dependentes do autor**: `Ahmed2022`,
`Attenberg2010`, `Hanneke2015` (PDFs fechados, links já passados) e `Barros2014`
(não localizada; só a homônima existe na Crossref).

Medições: `check-fichamentos` passa em **todas** as minhas; o acervo sai de 334
problemas na main para **332** na minha branch — dois a menos, nenhum
acrescentado. KG em **678 nós / 1432 arestas**.

## Resultado (principal)
Entrega processada e integrada; arquivada na limpeza.
