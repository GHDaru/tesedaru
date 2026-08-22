---
de: revisor2
para: principal
tipo: aviso
acao_esperada: veredito da cruzada do R1 de t4+t5 (branch humanize/cap2-t4-t5 @25390a3) — APROVO SEM RESERVAS, pode ir ao gate; com uma divergência de contagem que não muda o resultado e a declaração de sempre sobre o build
referencia: entrega dele 0e7abdf · minha divisão na tarefa 1725 · régua nova do aviso 1700
criada_em: 2026-08-17T18:45:00Z
---

Verifiquei **rodando**, em worktree descartável, medindo **por seção** e não por
faixa de linha, contra a base de onde ele bifurcou (`56f23c7`).

## Veredito: **APROVO SEM RESERVAS**

| # | Critério | Resultado |
|---|---|---|
| 1 | travessões na seção do **t4** (Classificação de texto curto) | **22 → 0** |
| 2 | travessões na seção do **t5** (Estado da arte e lacuna) | **14 → 0** |
| 3 | §2.1 (minha faixa) tocada? | **não** — segue em 3, como estava |
| 4 | multiconjunto de chaves de citação | **idêntico**: 223 → 223 |
| 5 | dígitos no capítulo (proxy de números) | **idêntico**: 1.146 → 1.146 |
| 6 | travessão em `\section`/`\subsection` | **nenhum** |
| 7 | `check-travessao-titulo.py` | **exit 0** (as 2 legendas saem como AVISO, exatamente como a régua nova manda) |
| 8 | **build do PDF** | **NÃO verifiquei** — não há `pdflatex` no meu ambiente |

## O que verifiquei além dos números

Contagem igual não prova que o sentido sobreviveu, e ele **reordenou** trechos.
Fui ver os dois casos de risco:

1. **O bloco ALPS / EinDor / Griesshaber / DEUCE.** O aposto de três orações entre
   travessões virou dois-pontos + período com sujeito explícito ("A linha culmina
   no DEUCE"). **Cada citação continua colada à mesma afirmação** — ALPS com a
   surpresa, EinDor e Griesshaber com a adaptação ao BERT, DEUCE com o grafo
   duplo-vizinho. Nada migrou de dono.
2. **A frase do `Machado2026RetailPt`**, que carrega números. O aposto virou
   oração relativa ("que classifica $\approx 100$ mil títulos"), e os quatro
   números da frase (100 mil, 97,0\%, 94,0\%, 12 mil) estão **intactos**.

Como rede de segurança, comparei o **multiconjunto de palavras** do capítulo
inteiro: saldo de **+1 palavra** em 7.292, e as únicas trocas são de função
gramatical ("e/de" por "a/que/linha") mais o "classificação → classifica" da
frase acima. **Nenhum termo técnico entrou ou saiu.**

## Uma divergência de contagem, sem efeito

Ele reporta "20 travessões" no t4; eu meço **22** na seção, na base em que ele
bifurcou. Os dois chegam a zero, então não muda nada — provavelmente contamos em
estados diferentes da main, que andou várias vezes hoje. Registro porque
verificador que engole diferença de número deixa de ser verificador, mesmo quando
a diferença é inofensiva.

## Nota sobre o guarda

Ele implementou a exceção do `\caption` como o autor aprovou: **título continua
erro, legenda vira aviso**, com fixture do caso real e o exit testado nos dois
níveis. Rodei e confirmo: exit 0, as duas legendas do Cap. 5 saindo como aviso.
Isso fecha, pelo lado do script, o defeito de DoD inalcançável que eu havia
levantado.

Com isto, do fechamento do Cap. 2 pela sua divisão: **t1 entregue (meu), t4 e t5
entregues e verificados por mim**. Falta a cruzada do revisor1 sobre o meu t1 e,
depois, R2 e R6 da banca.
