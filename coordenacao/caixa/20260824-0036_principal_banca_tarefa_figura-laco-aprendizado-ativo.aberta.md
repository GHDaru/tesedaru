---
de: principal
para: banca
tipo: tarefa
referencia: 2-fundam/texto.tex §2.2 (sec:fund-al)
acao_esperada: figura TikZ do laço de aprendizado ativo; loop de excelência; entrega em branch + recibo de 1 linha
prazo: sem prazo rígido; auditoria do autor em curso no Cap.2
---

# Encomenda do autor: figura do laço de aprendizado ativo (Settles, modo em lote)

O autor, na auditoria do Cap.2, encomendou: *"uma figura do aprendizado ativo
segundo Settles e que utilizamos na tese baseado em lote e no arcabouço"*.

## O que desenhar

O ciclo do aprendizado ativo com acervo fixo (\textit{pool-based}), na
formulação de Settles (2009/2012), instanciado como a tese o usa:

1. **Acervo não rotulado $U$** (pool fixo, disponível desde o início).
2. **Conjunto rotulado $L$** (inicia como $L_0$).
3. **Treinamento do classificador** sobre $L$.
4. **Estratégia de seleção** escolhe um **lote** de instâncias de $U$
   (modo \textit{batch-mode} — destacar que a seleção é por lote, não
   instância a instância; é assim que a tese opera).
5. **Oráculo** rotula o lote (na tese: oráculo de rotulagem, incluindo LLM —
   mas a figura é do Cap.2, fundamento: rotule como "oráculo" genérico, sem
   antecipar a maquinaria do Cap.3).
6. Lote rotulado retorna a $L$; laço repete até o **critério de parada**
   (orçamento).

## Restrições (mesmas da série de esquemas)

- TeX/TikZ standalone em `3-metodo/esquemas-propostos/` (ex.:
  `esq-laco-aprendizado-ativo.tex`), corpo legível no tamanho de página.
- Figura ILUSTRATIVA: **zero números medidos**, zero códigos internos, zero
  caminhos. Símbolos apenas ($U$, $L$, $L_0$, lote).
- Sem travessões em texto de figura/legenda.
- Loop de excelência: itere até você mesma avaliar que a figura está muito boa
  e ilustrativa (mesmo padrão das figuras anteriores: esq-lce, esq-drisl etc.).
- Proponha também a legenda e o ponto de inserção no §2.2 (após a formalização
  do laço), mas NÃO edite o texto do capítulo — o principal gateia a inserção
  com o autor.

## Entrega

Branch própria + recibo de 1 linha na caixa (`de:banca para:principal`),
formato `branch@sha:caminho`. O gate é do principal com o autor.
