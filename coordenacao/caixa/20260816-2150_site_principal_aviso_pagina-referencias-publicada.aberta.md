---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma ação obrigatória — registro de conclusão; repassar ao autor se fizer sentido no próximo bloco
referencia: tesedaru branch main (b5a64b1) · tarefa 20260816-2110
criada_em: 2026-08-16T21:50:00Z
---
Página "Referências" publicada e no ar — pedido literal do autor atendido:
tabela com título, autores, onde citada, link, PDF (sim/não), fichado
(sim/não) e um botão "ver" que expande o fichamento inteiro renderizado.
Todas as colunas ordenáveis por clique no cabeçalho (asc → desc → volta à
ordem do livro), mais uma busca por texto livre que não estava no pedido
mas resolvia a mesma necessidade que as pílulas de filtro já resolvem no
kanban (decisão registrada em specs/003-pagina-referencias/ux-design.md).

## Números
378 referências no total, 152 citadas de fato no texto da tese (as outras
226 estão no referencias.bib mas não aparecem em nenhum \cite — aparecem
por último na tabela, marcadas "não citada", nunca escondidas).

## Achado de qualidade de dados (não é bug meu, é do conteúdo)
A chave `Aggarwal2012` é citada no Cap. 2 mas não tem fichamento; a chave
`Aggarwal2012MiningText` tem fichamento completo mas nunca é citada sob
essa chave exata — são duas entradas BibTeX genuinamente diferentes para
fontes relacionadas (o livro inteiro vs. o capítulo específico dele). A
tabela expõe isso corretamente lado a lado; não tentei fundir/corrigir
porque seria uma decisão editorial sobre a bibliografia, fora do meu
escopo de site.

## Três bugs reais no script novo, encontrados e corrigidos antes de
publicar (detalhe completo em specs/003-pagina-referencias/qa-report.md):
um deles travava o build inteiro (parágrafo de fichamento começando com
**negrito** entrava em loop infinito no conversor Markdown que escrevi);
os outros dois eram acentos LaTeX incompletos e um parser de BibTeX que
quebrava campos com vírgula dentro de aspas. Nenhum foi pego por inspeção
— só apareceram rodando contra os 378 dados reais.

## Evidência
Testado no Chromium: 0 erros de console nas 5 páginas, ordenação e busca
conferidas contra o JSON bruto (não só a tela), tema claro/escuro, mobile
sem rolagem lateral do body. Deploy confirmado (run 31974563458, sucesso):
- https://ghdaru.github.io/tesedaru/referencias.html

## Aviso separado (não é sobre isto)
O autor me pediu, em paralelo nesta sessão, para redesenhar o site do
`activelearning` (MkDocs, ghdaru.github.io/activelearning) no estilo do
"livro do harness" (repositório `harness_engineering`, que tem um sistema
de design de livro documentado em `publicar/DESIGN-SISTEMA.md`), com
possível frontend/backend separados (Vercel/Railway). Ele mesmo decidiu
adiar essa frente para depois da página de Referências — só avisando que
ela está na fila, caso apareça em outro lugar da coordenação.
