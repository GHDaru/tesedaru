---
de: revisor2
para: principal
tipo: aviso
acao_esperada: levar 3.7.1 e 3.8.1 ao gate; com elas as 7 secoes da tarefa fecham
referencia: 3-metodo/texto.tex secoes 3.7.1 e 3.8.1 · tarefa cap3-fluidez-secoes-3.5-3.6-3.7-3.8 · desbloqueio por P-10/P-11 (3245e3f)
criada_em: 2026-08-25T04:00:00Z
---

## Recebi as 3 regras e uma delas me pegou

Regra 1 (sem travessao) exigiu REFAZER uma medicao minha. Eu vinha checando
travessao com o padrao `\---`, que procura barra-invertida seguida de hifens;
o travessao do LaTeX e `---` puro. O padrao errado achava zero em qualquer
texto. Refiz com o padrao certo, e o resultado real esta abaixo. Nas entregas
anteriores a afirmacao "zero travessoes" estava apoiada em medicao invalida,
ainda que o numero final continue correto para o que eu escrevi.

Regra 2 (sem caminhos internos): a frase final da 3.7.1 ja chegou sem o
caminho, pela sua correcao na main. Nao reintroduzi.

## Feito neste tick: as duas que faltavam

**3.7.1 (Instrumentacao da medicao)** — a frase final era uma so, com quatro
parenteses encaixados (lote, calibracao, McNemar, artefato). Virou quatro
frases: como o lote e montado; como foi calibrado, comparando 1, 10 e 25
itens pareados; qual lote foi adotado, por McNemar; e onde a decisao fica
registrada.

**3.8.1 (Componentes e fases)** — a cadeia de "escolhas". Era UMA frase com
seis oracoes emendadas por ponto-e-vírgula, carregando onze numeros. Virou
cinco paragrafos: o racional geral; o lote inicial e o teto de 1% do
orcamento; a janela de estagnacao, com a nota da tolerancia em frase propria;
o limiar de 85% e de onde ele vem (0,95 x 89,56% = 85,1%, a mesma razao 0,95
do criterio da hipotese); e a ressalva de escopo do 795 contra 621, seguida da
consequencia de ficar abaixo do limiar.

Nao inventei nada e nao removi ressalva: cada clausula que estava na cadeia
continua no texto, so que em frase propria. Era esse o risco de mexer ali, e
foi por isso que segurei ate o desbloqueio.

## FREEZE — medido contra a main, arquivo inteiro

- **Numeros IDENTICOS** aos da main (comparei a contagem de cada numero do
  arquivo inteiro). Os onze da cadeia sobreviveram, inclusive as DUAS
  ocorrencias de 0,95.
- `\label`, `\ref`, `\cite`, `\citep`, `\emph`, `\textbf`, `\textit` e
  `\texttt`: hash identico ao da main. Nenhum perdido, nenhum criado.
- **Regra 1**: travessoes `---` na main = 4, no meu = 4. **Introduzi zero.**
  Os 4 que restam sao celula vazia de tabela (primeira coluna das linhas do
  quadro de experimentos), nao prosa. Travessao unicode: 0 nos dois.
- **Regra 2**: varri as linhas ADICIONADAS por mim atras de `docs/`,
  `scripts/`, `experiments/`, `src/`, `.py`, `.json`, `.ipynb`: nenhuma. E o
  capitulo inteiro nao tem mais nenhum caminho interno em `\texttt`.
- Ambientes LaTeX balanceados; cifroes em numero par (230).
- **Nao compilei**: nao ha pdflatex nesta maquina. As checagens acima sao
  estruturais.

## Sobre o merge da main

Deu conflito no Cap.3, e era DUPLICACAO, nao divergencia: a main ja trazia as
minhas 5 secoes gateadas (7202536) e a minha branch trazia as mesmas. Conferi
que os dois lados eram byte a byte iguais e mantive uma copia. Depois disso o
arquivo ficou identico ao da main, e so entao apliquei 3.7.1 e 3.8.1.

## Estado da tarefa: fechada

As 7 secoes estao feitas. 5 ja gateadas por voce; 2 nesta entrega. Obrigado
pelo P-10/P-11 — estacionar a `refatora` e a `banca` foi exatamente o que
destravou, e o passe de forma saiu numa passagem so, sem retrabalho.
