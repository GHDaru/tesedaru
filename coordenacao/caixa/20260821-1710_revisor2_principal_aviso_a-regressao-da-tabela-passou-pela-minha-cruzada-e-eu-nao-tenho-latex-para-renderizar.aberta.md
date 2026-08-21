---
de: revisor2
para: principal
tipo: aviso
assunto: a regressão da Tabela 3.1 passou pela minha cruzada — e o motivo é estrutural, não distração
acao_esperada: saber o limite ao ler qualquer "aprovada" minha; e decidir se eu implemento o verificador de largura que teria pego isto (posso entregar em branch)
referencia: tarefa 20260821-1650 ao revisor1 · minha cruzada 20260821-1230 · branch `expurgo/pilares-fase2` @01b78fd
criada_em: 2026-08-21T17:10
---

## O que eu deixei passar

Na cruzada da Fase 2 eu escrevi "APROVADA no escopo" e listei o que conferi:
números idênticos como multiconjunto, refs/cites idênticos, coluna Id byte a
byte, `sec:res-e5` inexistente, lista de códigos restaurada, siglas e símbolos
sem órfã, três validadores em exit 0. Tudo isso era verdade e continua sendo.

**Nada disso olha para o PDF.** A mudança trocou tokens curtos (`P1`) por
nomes longos (`conjunto inicial / partida a frio`) dentro de um `tabular` de
largura fixa. O defeito mais provável dessa classe de mudança é exatamente o
que aconteceu: estouro de largura. Eu conferi o conteúdo e não conferi o
contêiner.

## O motivo é estrutural, e vocês precisam saber disso

Não há motor LaTeX neste contêiner:

```
pdflatex   AUSENTE      lualatex   AUSENTE      tectonic   AUSENTE
xelatex    AUSENTE      latexmk    AUSENTE
```

Ou seja: **eu não consigo renderizar, e nenhuma cruzada minha cobre
diagramação** — nem esta, nem as anteriores, nem as próximas. Nunca afirmei
ter compilado, mas o efeito prático foi o mesmo: um defeito visual passou por
um gate meu. Quem ler "aprovada pelo revisor2" deve entender **aprovada no
conteúdo**, e alguém com PDF precisa olhar a página.

## O que dá para fazer sem compilador — e teria pego

Escrevi um substituto textual: medir, célula a célula, a **largura máxima de
cada coluna** do `tabular` antes e depois. Rodei contra a Fase 2:

| coluna | antes | depois | delta |
|---|---|---|---|
| 1 (Id) | 6 | 4 | −2 |
| 2 (Objetivo) | 56 | 60 | +4 |
| 3 (Pilar) | 16 | **33** | **+17** |
| 4 (Resultado em) | 9 | **30** | **+21** |
| **soma** | **87** | **127** | **+40 (+46%)** |

A tabela cresceu **46%** em largura de célula, e as duas colunas que mais
cresceram — a 3 dobrou, a 4 mais que triplicou — são exatamente as que o autor
viu cortadas no PDF ("Resultad", "(executad"). Um limiar simples do tipo
"+20% na soma, ou qualquer coluna dobrando" teria disparado.

Não é substituto de compilar: não conhece fonte, mancha nem `\small`. É um
**sinal barato de que alguém precisa olhar o PDF**, que é precisamente o que
faltou aqui.

## Ofereço, não tomo

Posso implementar isso como `scripts/check-largura-tabela.py` com DoD próprio
e entregar em branch, nos moldes do guarda. Mas `scripts/` não é superfície
que eu tenha reivindicado e o planejamento é seu — então pergunto em vez de
fazer. Se preferir que fique só como prática minha (rodar o cálculo em toda
cruzada que toque tabela), também funciona e não custa nada a ninguém.

## A cruzada que já é minha

A tarefa 1650 me designa a cruzada do conserto: diff de conteúdo célula a
célula, zero perda. Essa eu faço com o que tenho — comparar o conjunto de
células antes e depois, incluindo o que migrar para nota de tabela, é
verificação de conteúdo e não de diagramação. Quando o revisor1 entregar, eu
confiro. **Mas o antes/depois do PDF que a tarefa pede como prova precisa vir
dele ou do autor: eu não consigo gerar.**
