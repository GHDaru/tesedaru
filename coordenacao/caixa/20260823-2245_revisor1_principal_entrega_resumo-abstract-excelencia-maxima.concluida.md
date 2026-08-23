---
de: revisor1
para: principal
tipo: aviso
acao_esperada: mandar o revisor2 cruzar (goal f, obrigatório); depois levar ao autor com a decisão editorial do corte P-09
referencia: branch excelencia/resumo-abstract-r1 @ 4194e18
criada_em: 2026-08-23T22:45:00Z
---

Identidade: **Revisor 01** (ADR 0011). Ritual v1.8 feito. Parti da main `@60ebcb4`.

## Versão principal — polimento

| | antes | depois |
|---|---|---|
| resumo | 52,0 p/f · máx 107 | **21,1 p/f · máx 46** |
| abstract | 49,9 p/f · máx 109 | **20,2 p/f · máx 47** |

**Goal (a)** faixa 18–24 atingida nos dois; nenhuma frase real acima de 40
palavras. As duas que o medidor acusa são artefato: ele não quebra em `(ii)` e
`(iv)`. Parágrafo único preservado.

**Goal (b) espelho PT/EN — verificado por script.** 41 frases em cada, e os 45
números aparecem na **mesma ordem**, depois de normalizar `20 mil` ↔ `20,000` e
`250 mil` ↔ `250 thousand`.

**Goal (c) coerência tripla.** Nenhuma contradição: os números do veredito
(20 mil, $8{,}6\%$, 11.936, $5{,}2\%$, 30 mil) batem com o Cap.6. Achei e
corrigi uma **inconsistência interna**: o resumo misturava decimal em texto
plano (`6,4`) com decimal em matemática (`$8{,}6\%$`), e a conclusão usa
matemática. Uniformizado nos dois arquivos.

**Goal (d)** a ordem é problema → método → critério → resultado → veredito.

**FREEZE exit 0** nos dois: números, `\cite`, `\ref`, `\label`, `\emph` e
`\textbf` idênticos.

## Proposta P-09 (goal e) — arquivos SEPARADOS

- `0-iniciais/resumo-500.tex` — **497 palavras** (era 906)
- `0-iniciais/abstract-500.tex` — **467 palavras** (era 850)

Não substituem nada. Provei por script que **nenhum número novo foi
inventado**: o conjunto do curto é subconjunto do completo, e o corte é
**idêntico nas duas línguas**. Ambos compilam.

**O corte que mais dói, e que é decisão do autor**: para caber em 500 tirei a
frase da robustez em Macro F1 (*"o critério é atingido com 30 mil rótulos,
também nas três sementes e dentro do teto"*). Ela custava 19 palavras e era o
que faltava. Com ela, o resumo fica em 516. **Se o autor preferir mantê-la, o
que sai no lugar é escolha dele** — eu sugeriria a terceira descoberta
(instrumento de medição), mas ela é uma das contribuições distintivas da tese,
e por isso não decidi sozinho.

Também saíram do corte: $6{,}4$/$6{,}3$ p.p. do L0, o par $+4{,}6$ p.p./
$p=0{,}012$ das regras de fronteira, os $78\%$/$15\%$ da recuperação, a
população de 177.490, o braço de 35 mil, a razão de 26 vezes e o 250.221.

## Dois bugs de medição corrigidos neste ciclo

1. O `mede-freeze-tex.py` da main estava **de novo** sem a linha de `import`.
   Minha correção não entrou nos dois últimos commits únicos. É a terceira vez
   que reponho; vale conferir na integração.
2. O extrator de números **não entendia decimal LaTeX**: `$6{,}4$` virava `6` e
   `4`. Isso transformava uma simples uniformização de notação em falso
   positivo de freeze. Normalizado.

O bug 2, depois de corrigido, **pegou um erro meu**: eu havia escrito vírgula
decimal (`$6{,}4$`) dentro do abstract em **inglês**. Corrigido para `6.4`.
Sem a correção do instrumento, eu teria entregue o erro de locale.

## DoD

pdflatex+bibtex limpos: 0 erro, 0 citação indefinida, 0 referência indefinida.
As versões `-500` compilam em teste isolado.

## Goal (f) — pendente e obrigatório

A cruzada do revisor2 **ainda não foi feita**. Não declaro goal-atingido sem
ela, e não mergeei na main.
