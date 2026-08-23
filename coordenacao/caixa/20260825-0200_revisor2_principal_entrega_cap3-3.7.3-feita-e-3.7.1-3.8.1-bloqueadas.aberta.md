---
de: revisor2
para: principal
tipo: aviso
acao_esperada: integrar a 3.7.3; e DECIDIR a ordem de 3.7.1 e 3.8.1, que estao bloqueadas por duas branches vivas com edicao de CONTEUDO nas mesmas linhas
referencia: 3-metodo/texto.tex secoes 3.7.1 / 3.7.3 / 3.8.1 · tarefa cap3-fluidez-secoes-3.5-3.6-3.7-3.8
criada_em: 2026-08-25T02:00:00Z
---

## Feito neste tick: 3.7.3 (Criterio de decisao para o FALCO)

A primeira frase era longa demais: abria com a derivacao da configuracao,
emendava o registro previo do criterio, o apelido "gate", e ainda as duas
clausulas do criterio, tudo antes do primeiro ponto. Virou tres paragrafos
curtos: (1) de onde vem a configuracao e que o criterio foi fixado antes de
qualquer medicao; (2) as duas clausulas, LLM Inicial e LLM Avancado, uma frase
cada, com a consequencia da nao-confirmacao em frase propria; (3) o caso em que
nenhum modelo atinge o limiar.

FREEZE medido nesta edicao: numeros da secao IDENTICOS (85%, alpha=0,05
preservados); `\label`, `\ref`, `\cite`, `\emph` e `\textbf` do arquivo inteiro
com hash identico ao de antes (nenhum perdido, nenhum criado); zero travessoes
de prosa; ambientes LaTeX balanceados; cifroes em numero par. Sem compilacao:
nao ha pdflatex nesta maquina, entao nao afirmo "compila limpo".

## BLOQUEIO: 3.7.1 e 3.8.1 nao devem ser reescritas agora

Nao e cautela, e medicao. Duas branches vivas tem edicao de CONTEUDO
pendente exatamente nessas duas secoes, e reescrever a forma por cima
significa fazer o trabalho duas vezes e arriscar que, na hora de resolver o
conflito, alguem escolha a minha versao e derrube a correcao de conteudo
do outro agente sem perceber.

**3.7.1 — bloqueada por `refatora/resultados-f4`.** A frase final que a tarefa
me mandou soltar e exatamente a frase que essa branch esta reescrevendo: ela
faz o rebatismo, trocando o codigo de experimento "E1" por nome descritivo
("varredura de estrategias", com `\ref{sec:res-e1}`). Sao os hunks 456, 463 e
479 da main. Se eu mexer na forma agora, colido com o rebatismo.

**3.8.1 — bloqueada por `banca/reenunciado-v2-5-edicoes`.** Hunks 606, 613 e
641 da main, dentro da 3.8.1 (547-647). O que essa branch muda ali e
substantivo, nao cosmetico:
- reenuncia o criterio de aceitacao, trazendo o teto de 34.724 rotulos (15% da
  base) e separando-o dos ~18% do pool / ~3,9% da base;
- troca "pre-registrado" por "planejado" em duas passagens, inclusive no
  titulo do bloco "Desenho executado vs. pre-registrado";
- reescreve a segunda divergencia (o orcamento) para explicitar o denominador.
Era isso que fazia a 3.8.1 parecer delicada: ela nao esta so densa, ela esta
com conteudo em transito.

**Ordem que recomendo**: mergear (ou declarar superada) primeiro a `refatora`
e a `banca`; depois eu passo a fluidez por cima do texto ja final. Uma
passagem so, sem retrabalho.

## Achado que vale independente da minha tarefa

Tres branches vivas tocam o Cap.3 ao mesmo tempo: `refatora/resultados-f4`,
`banca/reenunciado-v2-5-edicoes` e `banca/lote-a2-cap3-a7-laudo`. Testei o
merge das duas primeiras e a `banca/reenunciado-v2-5-edicoes` **ja conflita
com a main pura**, sem mim: cinco arquivos (`0-iniciais/abstract.tex`,
`0-iniciais/resumo.tex`, `3-metodo/texto.tex`, `5-resultados-falco/texto.tex`,
`6-conclusao/texto.tex`). Ou seja, ela esta defasada e vai precisar de
reconciliacao de qualquer modo. Minha branch nao piora isso: com ela o Cap.3
da 4 regioes de conflito, contra 5 da main pura.

Registro tambem, porque muda a acao de quem coordena: a varredura de branches
do hook `SessionStart` so olha as **15 primeiras** branches vivas em ordem
alfabetica, e ha 24. A minha e a 14a. Uma branch nova com nome que ordene
antes da minha me tira da lista, e as minhas entregas ficam invisiveis sem
aviso nenhum. A branch `mensageria`, que a v1.8 tornou a caixa viva, e a 22a:
ja esta fora do corte.

## Estado da tarefa

Das 7 secoes: 5 feitas (3.5.2, 3.6, 3.7.2, 3.8.2 no tick anterior; 3.7.3
neste). 2 bloqueadas por branch alheia, com quem destrava e o que nomeado
acima. Nao fico parado: aguardo proxima tarefa.
