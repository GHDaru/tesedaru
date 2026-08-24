---
de: principal
para: banca
tipo: tarefa
referencia: 3-metodo/texto.tex (abertura @74c1fad; §3.2) · esq-preproc-espacos-rotulos da sua branch
acao_esperada: 2 figuras TikZ com loop de excelência; entrega em branch + recibo de 1 linha
prazo: auditoria do autor em curso no Cap.3
---

# Encomenda do autor (auditoria Cap.3): 2 figuras

## Figura 1 — Sequência da metodologia (NOVA)

O autor: *"uma figura para explicarmos a sequência da metodologia... Não fica
claro o processo metodológico, tem apenas as coisas que foram feitas."*

A abertura do Cap.3 acabou de ganhar a narrativa do processo (main @74c1fad,
primeiro parágrafo). A figura deve CONTAR A MESMA HISTÓRIA, na mesma ordem:

1. **Problema** (Cap.1): reduzir custo de rotulagem sem perda relevante de
   desempenho.
2. **Terreno comum**: desenho da pesquisa e registro; dados e auditoria;
   classificadores; métricas.
3. **Processo na ordem em que o custo aparece**:
   a. composição do conjunto inicial $L_0$ (pilar 1) →
   b. construção do $L_0$ sem rótulos, DRI-SL (pilar 2) →
   c. quem rotula: LLM como oráculo, viabilidade/custo/perfil de erro
      (pilar 3) →
   d. integração no framework e avaliação contra referências sob o mesmo
      orçamento (pilar 4).
4. **Transversal**: LCE resume as curvas; validade e reprodutibilidade fecham.

É um fluxo de decisões (o que precisa estar resolvido antes do quê), não um
inventário. Sugira o ponto de inserção na abertura do capítulo; nome
`esq-sequencia-metodologia.tex`.

## Figura 2 — Pré-processamento e espaço de rótulos (JÁ EXISTE, polir)

O autor lembrou desta encomenda anterior. Você já tem
`esq-preproc-espacos-rotulos.tex` na sua branch (esquemas-tikz-metodo).
Passe-a pelo MESMO loop de excelência (renders reais, corpo 12, iterar até
você mesma avaliar como muito boa e ilustrativa), atualize-a ao texto atual
do §3.2 da main, e proponha legenda + ponto de inserção.

## Restrições (série dos esquemas, iguais às anteriores)

- TikZ standalone em `3-metodo/esquemas-propostos/`; legível em P&B e corpo 12.
- Zero números medidos, zero códigos internos, zero caminhos, zero travessões.
- NÃO editar o texto dos capítulos — o principal gateia a inserção com o autor.
- Entrega: branch própria + recibo de 1 linha (`branch@sha:caminho`).
