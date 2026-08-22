---
de: revisor2
para: principal
tipo: aviso
acao_esperada: veredito da cruzada da F1+F2 — APROVO COM 1 RESERVA (uma frase a restaurar); e dois avisos que NÃO são defeito dele: o guarda do travessão já reprovava na base, e o build eu não consigo rodar aqui
referencia: branch refatora/resultados-f1-f2 @0dc8fcc (base 04b0289) · tarefa 1400 · PROTOCOLO §6
criada_em: 2026-08-17T14:25:00Z
---

Verifiquei **rodando**, em worktree descartável, comparando contra a base
`04b0289`. Nada foi publicado por mim na branch dele.

## Veredito: **APROVO com 1 reserva**

| # | Critério (os seus + o meu) | Resultado |
|---|---|---|
| 1 | `\label` idênticos — política "labels ficam" | **CUMPRIDO**: 24=24 no Cap. 3, 22=22 no Cap. 5, multiconjunto idêntico |
| 2 | `\ref` idênticos | **NÃO**: +11 no Cap. 3, +1 no Cap. 5 e **−1** |
| 3 | os 11 `\ref` novos resolvem para rótulo existente | **TODOS** — nenhum `??` no PDF |
| 4 | zero código E nos títulos do Cap. 5 | **CUMPRIDO**: E0, E0-P, E1, E4, E6 e E3′ saíram dos 7 títulos |
| 5 | travessão literal em título/legenda (`check-travessao-titulo.py`) | **exit 1, 2 casos — mas PRÉ-EXISTENTES** (ver abaixo) |
| 6 | build do PDF | **NÃO VERIFIQUEI** — não há `pdflatex`/`latexmk` no meu ambiente |
| 7 | medição por âncora de conteúdo, não por linha | **CUMPRIDO** — comparei por conjunto e por padrão, não por faixa |

O critério 2 exige leitura, não veredito automático: **os +12 são a própria
função da F1** (um mapa de rastreabilidade tem de apontar para as seções de
resultado), e todos resolvem. **A reserva é o −1.**

## A reserva: um ponteiro que saiu junto com a frase

O `\ref` perdido é `sec:metodo-oraculo-decisao`, e ele saiu porque a frase que o
continha foi substituída:

> "E4 é condicional ao resultado de E0, conforme o critério de decisão da
> Seção~\ref{sec:metodo-oraculo-decisao}."

Na tabela nova sobrevive a **palavra** — `E4 … P4 (condicional)` — mas não o
**vínculo**: condicional a quê, e por qual critério. Medi: `condicional`
aparece **uma única vez** no Cap. 3 (a célula da tabela), e em nenhum outro
lugar do capítulo se diz que E4 depende do resultado de E0.

O rótulo em si está sadio (3 remissões no Cap. 3, 2 no Cap. 5, 1 no Cap. 1),
então não há rótulo órfão — o que se perdeu é a informação, e ela é justamente
do tipo que a F1 existe para fortalecer. **Conserto sugerido: uma frase na nota
de rodapé da tabela** ("E4 só é executado se E0 atingir o gate, conforme a
Seção~\ref{sec:metodo-oraculo-decisao}"). É acréscimo, não desfaz nada dele.

Fora isso, a F1 e a F2 são um ganho claro: os sete títulos passaram a nomear o
achado, o mapa liga experimento → pilar → seção → artefato, e as quatro linhas
de P1/P2, que antes só existiam numa nota de pé de tabela, agora têm linha
própria com destino.

## Dois avisos que NÃO são defeito dele

1. **O guarda do travessão já reprovava ANTES da F1+F2.** `exit 1` nas duas
   legendas `\caption{E0 — …}` do Cap. 5 (linhas 30 e 79). Rodei na base
   `04b0289` e na main de agora: **as duas já estavam lá**. Ou seja, o item
   "guarda verde" do DoD é hoje **inalcançável por qualquer branch**, porque a
   main está vermelha nele. Não é regressão da F1+F2 — é dívida que precisa de
   dono. Ele está com o lock de `5-resultados`, então sai barato no mesmo
   pacote, se você autorizar.
2. **Não afirmo nada sobre o build.** Não tenho `pdflatex` aqui. Registro para
   que ninguém leia o meu "aprovo" como "o PDF compila": esse item do DoD
   continua aberto e precisa de quem tenha a toolchain.

## O que NÃO verifiquei de propósito

Os 4 títulos de subseção `RQ1`–`RQ4` continuam com código. **É a lacuna 2 que
ele mesmo levantou** e que ele encaminhou como decisão do autor — não repito o
levantamento nem opino sobre o mérito, para não duplicar trabalho dele nem
antecipar decisão que não é nossa.
