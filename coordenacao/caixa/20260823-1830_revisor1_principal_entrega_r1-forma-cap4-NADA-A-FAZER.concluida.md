---
de: revisor1
para: principal
tipo: entrega
estado: aberta
acao_esperada: LAUDO, não diff — o Cap.4 já está no padrão aprovado do Cap.3. Os 3 travessões que você mediu são TODOS de tabela (células vazias), que a própria tarefa manda deixar. Nenhum .tex foi alterado. Segue a varredura de tells, que é a parte que tinha trabalho.
referencia: 4-resultados-l0/texto.tex @ main 4ec5431 · padrão aprovado do Cap.3 · tarefa 20260824-1812 na mensageria
criada_em: 2026-08-23T18:30:00Z
---

# Resultado: nada a fazer, e a medição mostra por quê

**Não alterei nenhum arquivo `.tex`.** Não é esquiva: é que os três travessões
estão todos na **mesma linha, e é linha de tabela**.

## Antes/depois: idênticos, e este é o ponto

A única linha do Cap. 4 com `—` é a do $|L_0|=10$ na `tab:ag-evolucao`:

```latex
10     & 13,06\% & 18,82\% & $+5{,}76$ & —       & —       & — \\
```

Os três marcam **células vazias**: o cenário de minimização não foi executado
para esse tamanho. São formatação, e a sua tarefa é explícita — *"deixe
travessões de TABELA"*. Convertê-los em dois-pontos ou parênteses produziria
uma tabela sem sentido.

**Medição completa das formas de travessão no Cap. 4:**

| forma | ocorrências | onde |
|---|---|---|
| `—` (em-dash Unicode) | 3 | **1 linha, dentro do `tabular`** |
| `---` (em-dash LaTeX) | 0 | — |
| `--` (en-dash) | 1 | intervalo numérico (legítimo) |

**Travessões de prosa: zero.**

## O Cap. 4 já está no padrão aprovado do Cap. 3

Conferi o capítulo que serve de régua. O Cap. 3, depois do R1 aprovado, ficou
com **0 travessões Unicode** e **5 `---`**, todos em legendas e tabelas. Ou
seja, o padrão aprovado é "tira os de prosa, deixa os de formatação" — e é
exatamente o estado em que o Cap. 4 já se encontra.

Isso é coerente com o que eu havia medido no mapa dos apêndices: o Cap. 4
aparecia com densidade 1,5 por mil palavras, dentro da faixa 0,0–1,5 dos
capítulos revisados. Agora sei por quê: aqueles 3 eram os de tabela, então a
densidade de **prosa** é **zero**.

# A varredura de tells (só reporto, como pedido)

Varri as cinco famílias. O capítulo é o mais limpo que auditei:

| tell | ocorrências |
|---|---|
| paralelismo negativo ("não é X, mas Y") | **0** |
| filler / meta-comentário ("vale ressaltar", "é importante notar") | **0** |
| vocabulário-IA inflado (crucial, robusto, abrangente, aprofundar…) | **0** |
| regra de três (enumeração ternária) | **0** |
| gerúndio de fim de frase | **1** |

## A única ocorrência, e por que eu NÃO a marcaria

> "a curva de Macro F1 segue de perto a curva de cobertura, **indicando que**,
> no regime pequeno, o fator dominante é *quais classes* entram no sorteio."

Este **não é** o gerúndio superficial que o tell procura. O tell de escrita
automática é o gerúndio **decorativo**, que não acrescenta informação
("…, demonstrando a importância do tema"). Aqui o gerúndio faz trabalho real:
liga uma observação específica (as duas curvas se acompanham) a uma inferência
específica (o fator dominante é a cobertura de classes). Tirá-lo exigiria
quebrar a frase em duas e **perder o vínculo causal**, que é conteúdo — e
conteúdo está em freeze.

**Recomendo deixar como está.** Registro para que ninguém "conserte" depois
achando que passou batido.

# Freeze respeitado

Nenhum número, artefato ou conclusão foi tocado — nem havia o que tocar, já
que não editei arquivo nenhum. Esta branch carrega **só esta nota**.
