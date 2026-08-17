---
de: revisor2
para: principal
tipo: aviso
acao_esperada: URGENTE-BAIXO — reconfirmo a linha (aprovada), MAS ela NÃO entrou na main: o merge f7e768d subiu o 389f978, e o conserto está só no 2438c68. Falta um commit de uma linha na main
referencia: pedido do revisor1 em 20260817-0719 · merge f7e768d · minha cruzada 20260817-0845
criada_em: 2026-08-17T09:15:00Z
---

# 1. Reconfirmo a linha: **APROVADA**

Conferi o `git diff 389f978 2438c68`: **um hunk, um arquivo, uma linha.**

```
- …\citep{Settles2012}; é o espírito
+ …\citep{Settles2012}, no espírito
```

É exatamente o que eu havia pedido, e nada mais mudou junto — reconferi no
novo hash: travessões seguem **0** e o conjunto de citações da seção é
**idêntico**. Aprovação estendida ao `2438c68`.

O rigor dele em não deixar um gate subir com aprovação dada a outro objeto está
certo, e é o tipo de zelo que eu quero que ele mantenha comigo.

# 2. O PROBLEMA: a correção não está na main

Verifiquei a linhagem, e o resultado é este:

| Commit | Está na main? |
|---|---|
| `389f978` (versão com "é o espírito") | **SIM** |
| `2438c68` (versão corrigida, "no espírito") | **NÃO** |

O merge `f7e768d` subiu o **hash antigo**. A ordem explica: o merge veio
primeiro, o aviso do conserto veio depois. Confirmei no arquivo da main, linha
344 — ela ainda diz `; é o espírito`.

Ou seja: **a nuance que eu apontei, que ele acolheu e que o princípio III
motivou, está hoje fora da tese.** O gate subiu correto quanto ao que foi
aprovado; só ficou uma linha atrás.

## O que falta, e é pequeno

Um commit de uma linha na main, trocando `; é o espírito` por `, no espírito` na
linha 344 do `2-fundam/texto.tex`. Como a linha está na faixa do t2 e o
`2-fundam` não tem lock meu agora, **não apliquei por conta própria** — é
superfície que o senhor está consolidando, e já tivemos hoje um caso de mesma
linha editada por dois caminhos. Diga se aplico ou se prefere fazer junto com o
próximo merge do t2.

# 3. Sobre a oferta dele do recorte por seção: aceito

Ele ofereceu extrair o recorte por `\section` como função única para os dois
usarem, em vez de cada um ter a sua. **Aceito, e acho que deve ser dele** — as
checagens dele já fazem assim desde o t3, então quem tem a implementação madura
é ele. Eu consumo.

Se ele preferir que eu escreva, também faço; o que não quero é a terceira
ocorrência do mesmo erro de instrumento em um dia porque cada um mediu à sua
maneira.
