---
de: revisor2
para: principal
tipo: aviso
acao_esperada: cruzar a autoavaliacao e levar o Cap.4 ao gate do autor
referencia: 4-resultados-l0/texto.tex · tarefa loop-excelencia-cap4 · iteracao 2 (fechamento)
criada_em: 2026-08-25T08:00:00Z
---

# Iteracao 2 + AUTOAVALIACAO contra o goal completo

A iteracao 1 tinha atingido so o numerico. Rodei o goal inteiro e ele
REPROVOU em dois pontos, que esta iteracao corrigiu.

## O que a autoavaliacao reprovou na iteracao 1

**(c) frase-topico falhava em 3 das 5 secoes.** Elas abriam com procedimento
ou com ponteiro para tabela, nao com o que aquilo diz ao leitor:
- Sensibilidade abria em "O experimento avaliou 47 tamanhos..." (metodo);
- DRI-SL abria em "A Tabela X compara..." (ponteiro);
- Reexecucao abria em "usa grade reduzida de 15 tamanhos x 10 repeticoes"
  (configuracao).
Cada uma ganhou uma frase-topico que so reafirma o que a propria secao
demonstra, sem numero novo e sem afirmacao nova.

**(b) DRI-SL estava em 28,1**, acima da faixa por secao. Quebrei as duas
frases longas que restavam.

## Metricas (iteracao 1 -> iteracao 2)

| Secao | media it.1 | media it.2 | faixa 20-26 |
|---|---|---|---|
| GLOBAL | 23,4 | **21,6** | OK |
| Sensibilidade | 18,4 | 17,8 | abaixo |
| Limites por otimizacao evolutiva | 20,4 | 20,4 | OK |
| DRI-SL versus aleatorio | 28,1 | **22,9** | OK |
| Reexecucao independente | 24,6 | 23,3 | OK |
| Sintese do capitulo | 15,3 | 15,3 | abaixo |

Maxima do capitulo: 47 palavras (o goal proibe acima de 50).

## AUTOAVALIACAO — item a item

- **(a) R1-R6 + humanizer**: ATINGIDO, com uma declaracao. As siglas do Cap.4
  (AG, DRI-SL, PVBin, FALCO, BERT, LCE, LLM) estao todas na lista. Zero
  paralelismo negativo, filler, vocabulario-IA ou gerundio decorativo nas
  linhas novas — **exceto** um "nao so... mas" que ja existia e que esta
  DENTRO de um `\textbf{}`. Preservei de proposito: mexer nele quebraria a
  igualdade de `textbf` que o freeze exige, e ali o contraste faz trabalho
  real (sao duas comparacoes distintas: contra a aleatoria e contra o melhor
  individuo do AG).
- **(b) densidade**: ATINGIDO no global (21,6) e em todas as secoes quanto ao
  teto; nenhuma frase acima de 50 palavras. **Duas secoes ficaram ABAIXO de
  20** (17,8 e 15,3) e eu as julgo legitimas, nao defeito: as duas sao
  dominadas por itens de `enumerate`, que sao curtos por natureza. Se voce
  discordar, e reverter facil — mas alongar frase para caber numa faixa seria
  piorar o texto para melhorar a metrica.
- **(c) frase-topico**: ATINGIDO, 5 de 5 secoes. Registro que a do AG
  ("Para estimar o quanto a composicao pode render alem do sorteio...")
  enuncia o PROPOSITO, nao o achado; julguei suficiente porque responde
  "por que agora", mas e a mais fraca das cinco.
- **(d) zero caminhos/codigos**: ATINGIDO. Nenhuma ocorrencia de docs/,
  scripts/, experiments/, src/, tests/ ou D-0xx no capitulo.
- **(e) terminologia**: ATINGIDO. Unifiquei "conjunto de afericao" para
  "particao de afericao", que e o termo do Cap.3. Nenhum codigo E0-E6 no
  capitulo, entao a P-10 estacionada nao e tocada.
- **(f) zero travessoes novos**: ATINGIDO. `---` = 0 na main e 0 no meu. O
  unico travessao unicode e a celula vazia da l.111, pre-existente, que a
  propria regra manda preservar.

## FREEZE da iteracao 2 — tudo identico

numeros (269), citacoes (14), refs (20), labels (10), emph, textbf, textit e
texttt: **todos IDENTICOS** a iteracao 1. Esta iteracao nao teve nem excecao
declarada. Ambientes balanceados, cifroes em numero par (194).

## O QUE EU NAO CONSIGO VERIFICAR

**Nao compilei, e ninguem deveria ler "goal atingido" como "compila".** Nao ha
pdflatex neste conteiner. Tudo acima e checagem estrutural e lexical. A
compilacao com 0 erros e 0 referencias indefinidas (principio IX) continua
pendente de uma maquina com a toolchain, antes do gate.

## Correcao de uma medicao minha

Na iteracao 1 eu quase reportei "terminologia inconsistente: 'particao de
afericao' nao existe no Cap.3". Era falso: existe, quebrada em duas linhas
("particao de\nafericao"), e meu grep de linha unica nao viu. Mesmo tipo de
erro do padrao de travessao. Passei a conferir com quebra de linha antes de
reportar divergencia.

## VEREDITO

**Goal atingido**, com as duas ressalvas declaradas acima (secoes abaixo da
faixa por serem listas; o "nao so... mas" preservado dentro do negrito) e com
a compilacao pendente. Recomendo levar ao gate.
