---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor no gate em bloco; e abrir tarefa para as 23 ocorrencias fora do Cap.3, que sao de outra superficie
referencia: branch fluidez/cap3-secoes-revisor1 @ 79312f1
criada_em: 2026-08-23T20:50:00Z
---

## O que mudou

Ordem direta do autor: aplicar de fato a skill humanizer, verificar fluidez,
comparar antes/depois, e **tese auto-contida — sem citacao de arquivos ou
diretorios, so citacao bibliografica**. Entrega em `fluidez/cap3-secoes-revisor1
@ 79312f1` (push confirmado).

**1. Auto-contencao.** As 12 referencias a caminhos internos do Cap.3 sairam
(`experiments/*`, `scripts/*`, `docs/pre-registro/`); duas eram minhas, da R4.
Para nao trocar auto-contencao por afirmacao orfa (principio III) nem perder
rastreabilidade (principio V), a rota virou BIBLIOGRAFICA: duas entradas de
software novas no `referencias.bib` (`DaruActiveLearning`,
`DaruActiveTextClassification`), citadas onde antes havia caminho. Sobrou um
unico "/": `neuralmind/bert-base-portuguese-cased`, que e identificador de
modelo, nao diretorio da tese.

**2. Fluidez — o capitulo inteiro.** A medicao mostrou que minhas 6 secoes da R1
nao eram o problema todo: 9 secoes que eu nunca havia tocado ainda estavam entre
40 e 76 palavras por frase. Reescritas todas.

| | media pal./frase | frase mais longa | frases > 40 pal. |
|---|---|---|---|
| main (autor) | 42,7 | 203 | 45 |
| minha R1 | 35,5 | 203 | 34 |
| agora | **23,9** | **53** | **15** |

**3. Auditoria humanizer.** Zero vocabulario de IA, aspas curvas, negrito
mecanico ou "-ndo" superficial. Um achado contra mim: eu havia elevado os
travessoes de prosa de **0** (o autor nao usa nenhum neste capitulo) para 4.
Removidos.

**4. Freeze provado** contra `origin/main`: 276 numeros, 54 refs, 26 labels
IDENTICOS. Unica diferenca, deliberada e declarada: +5 chaves de citacao, que
sao a substituicao do item 1.

**5. Dois bugs de medicao corrigidos** — os dois davam numero BOM por engano,
que e o pior modo de falha:
(a) o removedor de comentarios comia o `\%` escapado e apagava o resto da linha:
**8 numeros da metodologia estavam invisiveis** as checagens de freeze que
rodei neste ramo ate hoje (re-rodei tudo com o corretor: continua batendo);
(b) remover nota de rodape antes da matematica quebrava a paridade de `$` e
colava frases, inventando uma frase de 198 palavras que nao existe.
Os instrumentos entram versionados: `scripts/mede-fluidez-prosa.py` e
`scripts/mede-freeze-tex.py`, com os erros documentados no cabecalho.

**DoD:** pdflatex+bibtex limpos (0 erro, 0 citacao indefinida, 0 referencia
indefinida, 101 paginas); `check-bib`, `check-travessao-titulo`,
`check-largura-tabela` saem 0.

## Duas coisas que sao DECISAO, nao minha

**(a) A regra vale para a tese inteira, e o Cap.3 sozinho fica inconsistente.**
Ha **23** referencias a caminhos internos fora do Cap.3:

    7  a4-biblioteca      7  5-resultados-falco   2  a2-ag
    2  a3-drisl           1  4-resultados-l0      1  a1-lce
    1  a5-prompts         1  a6-tabelas           1  a7-parada-drift

Nao toquei: prosa de capitulo e apendice nao e minha superficie. Duas delas
merecem atencao especial — o Apendice A4 e literalmente o mapa
experimento -> arquivo, e o A1/A3 apontam para modulos de codigo. Ali a
remocao nao e troca de frase, e decisao sobre o que o apendice existe para
fazer. Recomendo tarefa propria, com a mesma rota bibliografica que usei.

**(b) `referencias.bib` e superficie compartilhada COM LOCK, e eu nao consigo
tirar lock**: o lock mora em `coordenacao/locks/` na main, e agente nao empurra
para a main (§2-ter). Entao editei na minha branch e declaro aqui: **confira o
lock do `referencias.bib` na hora de integrar.** Se houver conflito, as duas
entradas sao aditivas e reaplicam-se sozinhas.

## Nao verificado por mim

Principio VI, quem executa nao verifica: a cruzada do revisor2 sobre esta
branch continua pendente. O numero de fluidez e meu; o julgamento de que o
texto ficou melhor **nao pode ser meu**.
