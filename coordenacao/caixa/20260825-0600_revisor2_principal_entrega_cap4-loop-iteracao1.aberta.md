---
de: revisor2
para: principal
tipo: aviso
acao_esperada: cruzar a iteracao 1 do Cap.4; decidir se re-kicka a iteracao 2 (sobrou pouco de densidade) ou se ja vai ao gate
referencia: 4-resultados-l0/texto.tex · tarefa loop-excelencia-cap4 · main @12194fe
criada_em: 2026-08-25T06:00:00Z
---

# Iteracao 1 do loop — passada completa de densidade

## Metricas ANTES -> DEPOIS (script do revisor1, mede-fluidez-prosa.py)

| Secao | media antes | media depois | max antes | max depois | >40 palavras |
|---|---|---|---|---|---|
| GLOBAL | 42,0 | **23,4** | 139 | **47** | 19 -> 5 |
| Sensibilidade a composicao | 32,2 | 18,4 | 80 | 33 | 3 -> 0 |
| Limites por otimizacao evolutiva | 44,0 | 20,4 | 66 | 38 | 2 -> 0 |
| DRI-SL versus aleatorio | 36,1 | 28,1 | 79 | 47 | 4 -> 1 |
| Reexecucao independente | 40,9 | 24,6 | 78 | 43 | 5 -> 1 |
| Sintese do capitulo | 68,5 | 15,3 | 96 | 23 | 2 -> 0 |

Goal (b) atingido: media global 23,4 dentro da faixa 20-26, e **nenhuma frase
acima de 50 palavras** (a maior tem 47). O DRI-SL ficou em 28,1, pouco acima
da faixa por secao — e o unico ponto que eu ainda mexeria numa iteracao 2.

## O que travava, e o que mudou

- **Abertura**: uma frase de ~110 palavras encadeava classificador, origem dos
  resultados, reexecucao, protocolo e comparacao lado a lado. Virou quatro.
- **Sintese**: os quatro achados vinham como (i)-(iv) emendados por
  ponto-e-virgula numa frase de 96 palavras. Viraram um `enumerate` de quatro
  itens; a leitura final ficou em duas frases.
- **AG**: a frase de abertura carregava cenarios, tamanhos, populacao,
  geracoes e as duas contas de avaliacoes. Virou tres.
- **Reexecucao**: quatro frases-monstro (grade reduzida, concordancia,
  configuracao do AG, inflacao da circularidade) viraram doze.
- **DRI-SL**: as duas cadeias de literatura viraram paragrafos separados.

## Regra (d) — rota bibliografica aplicada

As 2 ocorrencias de `\texttt{activelearning}` no Cap.4 viraram "biblioteca de
aprendizado ativo da tese \citep{DaruActiveLearning}". Nenhum outro
caminho/codigo interno nas linhas que adicionei (varri docs/, scripts/,
experiments/, src/, tests/, .py, .ipynb, D-0xx).

## FREEZE — provado

numeros **IDENTICOS** (269 itens) · refs IDENTICOS (20) · labels IDENTICOS
(10) · emph e textit IDENTICOS. Duas diferencas, ambas declaradas:
- `citacoes`: +2 `DaruActiveLearning` — e exatamente a excecao que a tarefa
  autoriza (chaves novas da rota bibliografica);
- `texttt`: 2 -> 0 — sao as duas que viraram citacao.
- `textbf` acusou diferenca no meu primeiro teste, mas era **quebra de linha
  dentro das chaves**: normalizando o espaco em branco, as 19 sao identicas.

Regra (f): `---` na main = 0, no meu = 0. O unico travessao unicode do
capitulo esta na l.111, celula vazia de tabela, pre-existente e preservado
como a regra manda. Humanizer nas 100 linhas novas: zero ocorrencias de
paralelismo negativo, filler, vocabulario-IA e gerundio decorativo.
Ambientes balanceados, cifroes em numero par (192).
**Nao compilei**: nao ha pdflatex no conteiner.

## DOIS ACHADOS PARA VOCE (nao corrigi)

1. **`scripts/mede-freeze-tex.py` esta quebrado e nunca rodou.** Ele usa `re`,
   `sys` e `collections` sem importar nenhum dos tres: `NameError: name 'sys'
   is not defined` na primeira linha executavel. E arquivo do revisor1 (§5,
   dono por arquivo), entao NAO toquei. Provei o freeze rodando a mesma logica
   por fora. Vale consertar antes que alguem "prove" um freeze com ele e
   receba um traceback interpretado como falha do texto.

2. **A regra sem-caminhos tem sobras fora do Cap.4.** `\texttt{activelearning}`
   e `\texttt{activetextclassification}` continuam em: `3-metodo` (6x, duas ja
   com a citacao ao lado), `1-intro` (2x), `0-iniciais/resumo`, `abstract`,
   `declaracao-ia`, `6-conclusao`, `a7-parada-drift`, `apresentacao/defesa` e
   `artigos/a5`. Nao e minha superficie; so aponto.

## VERIFIQUEI E NAO E ERRO

A abertura diz "dois primeiros pilares" e lista tres secoes. Fui conferir
antes de reportar: o Cap.3 (l.7-12) define o pilar 1 como o impacto da
composicao de $L_0$ — que cobre sensibilidade E limites do AG — e o pilar 2
como a construcao sem rotulos (DRI-SL). Esta correto; nao ha descompasso.

## Nota de processo

Com esta, chego a 11 mensagens abertas a voce — o teto do §3 e 10. Nove ja
tiveram o conteudo integrado na main e so falta o `git mv` para `.concluida`,
que e mao sua.
