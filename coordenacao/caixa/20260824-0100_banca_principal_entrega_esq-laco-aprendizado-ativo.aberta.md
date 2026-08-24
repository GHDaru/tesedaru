---
de: banca
para: principal
tipo: tarefa
acao_esperada: gatear com o autor a inserção da figura no §2.2 (após o Algoritmo alg:active_learning, antes do parágrafo dos três cenários), com a legenda proposta abaixo; a banca NÃO tocou no Cap. 2
referencia: tarefa 0036 · 3-metodo/esquemas-propostos/esq-laco-aprendizado-ativo.tex · branch banca/esquemas-tikz-metodo
criada_em: 2026-08-24T01:00:00Z
---
Entrega da tarefa 0036 (encomenda do autor: figura do laço de aprendizado
ativo, Settles, modo em lote). Loop de excelência cumprido (2 renders em
corpo 12; a seta de retorno em curva com rótulo inclinado foi refeita em
caminho reto com a saída de parada movida para fora do corredor; 0 erros,
0 overfull nas medidas reais; prévia versionada; autor já recebeu a imagem).

Conforme a encomenda: notação idêntica à sêxtupla e ao Algoritmo 1
(L, L0, U, theta, S, Q_t, O, B, Learn); seleção EM LOTE destacada
(batch-mode); oráculo genérico sem maquinaria do Cap. 3; zero números,
códigos, caminhos e travessões.

LEGENDA PROPOSTA (para o gate): "O laço do aprendizado ativo com acervo
fixo (\textit{pool-based}), no arcabouço $\mathcal{A}=\langle L, U,
\theta, S, O, B\rangle$ adotado na tese: a cada iteração, o classificador
é treinado no conjunto rotulado, a estratégia $S$ seleciona um lote $Q_t$
do acervo $U$ (modo em lote), o oráculo $O$ rotula o lote e os pares
rotulados retornam a $L$; o processo repete até esgotar o orçamento $B$ ou
o acervo, devolvendo o modelo final."

PONTO DE INSERÇÃO PROPOSTO: 2-fundam/texto.tex, imediatamente após
\end{algorithm} do alg:active_learning, antes de "O laço admite três
cenários" — com uma frase de remissão a critério do gate (ex.: "A
Figura~\ref{fig:fund-laco-al} ilustra o laço.").

Nota: o merge da origin/main de hoje nesta branch teve 1 conflito trivial
em a6-tabelas (a main já integrou meu passe do Apêndice F com um polimento
seu) — resolvido tomando a versão da main.
