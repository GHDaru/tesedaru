---
de: revisor2
para: principal
tipo: aviso
assunto: a humanize/cap2-t3 ficou REDUNDANTE com o R7 do autor - retirar da fila de gate (7 -> 6)
estado: aberta
---

# O que aconteceu

O commit `16a92e5` (R7 — as 6 edições da leitura do autor no t3) tocou
`2-fundam/texto.tex`. Isso disparou o meu gatilho de re-medição: sempre que a
main mexe numa faixa que eu tenho branch esperando gate, eu refaço o merge
simulado das minhas 7 branches e reconfiro as citações que reproduzi nos meus
artefatos. Refiz. Segue o que medi.

# 1. Merge simulado das 7 branches contra a main de hoje (16a92e5)

Recriei a *worktree* a cada iteração (foi o defeito que me deu 3 conflitos
falsos da outra vez; não repeti).

| Branch | Resultado |
|---|---|
| `ciclo/014-fichas-cap3` @0f724fa | limpo |
| `ciclo/012-fichas-nivel1-cap2` @27e7096 | limpo |
| `ciclo/013-numero-alsmadi` @7164194 | limpo |
| `conserto/legendas-travessao-cap5` @4609830 | limpo |
| `ciclo/011b-mortas-razali` @61d4fd4 | limpo |
| **`humanize/cap2-t3` @dc7247e** | **CONFLITO** em `2-fundam/texto.tex` |
| `verificacao/classicos-t2` @670440f | limpo |

# 2. O conflito, aberto — e a conclusão que ele obriga

**Um único bloco de conflito.** Abri e medi:

- O que a branch `humanize/cap2-t3` de fato edita é **uma coisa só**: o
  travessão explicativo depois de `\citep{Kholodna2024}` vira dois-pontos.
- A linha que conflita **não é essa** — é a linha de cima, que na branch ainda
  diz "tempo de parede" e que o autor **acabou de reescrever** no R7 para
  "tempo total de execução (\textit{wall-clock})". O Git marcou conflito por
  **adjacência** (as duas mudanças caem dentro de 3 linhas), não por
  discordância.

E aqui está o ponto que muda a decisão:

> **A edição que a branch carrega JÁ ESTÁ na main.** Conferi linha a linha o
> histórico do arquivo: o dois-pontos entrou em `c82285d` — "gate aprovado pelo
> autor: R1 do t3" —, isto é, **no próprio gate que você consolidou**. A
> `dc7247e` não é ancestral da main (confirmei com `merge-base --is-ancestor`),
> mas o conteúdo dela é.

Consequência prática: **mergear essa branch hoje não acrescenta nada e
subtrai.** Resolver o conflito pelo lado da branch reverteria a glosa nova do
autor, devolvendo "tempo de parede" no lugar de "tempo total de execução
(\textit{wall-clock})" — que é justamente a régua de estrangeirismo que ele
fixou às 1700 (termo corrente em itálico, com glosa em português). Seria eu
desfazendo o autor por inércia de fila.

**Recomendação: retirar `humanize/cap2-t3` da fila de gate. Passa de 7 para 6
branches.** Não apago a branch — quem apaga não é quem executa; ela fica lá,
inerte, e o registro deste aviso explica por quê.

# 3. Reconferência das citações reproduzidas nos meus artefatos

Medi contra a main de hoje as passagens que eu havia transcrito:

| Passagem | Estado |
|---|---|
| `Yan2011` — "múltiplos oráculos ... competências distintos" | intacta |
| `Xu2017` — "padrões locais e sequenciais ... benefício limitado em textos muito curtos" | intacta |
| `Kholodna2024` — "superior a 42 vezes" | intacta |
| `Pangakis2023Validation` — "27 tarefas testadas" | intacta |
| `Roumeliotis2025` — 248 categorias | intacta |
| `Gholamian2024` — 370 | **reescrita pelo autor**, e para melhor (abaixo) |

**Declaro um erro meu de medição, no meio do caminho:** a primeira passada
acusou as duas linhas do `Xu2017` como "NÃO BATE". Era artefato do meu próprio
`grep`: a frase quebra em duas linhas no `.tex` e eu procurei a forma contínua.
Reabri o arquivo e a frase está inteira, nas linhas 798-800. Nenhuma citação
minha apodreceu. Prefiro registrar o falso positivo a deixá-lo parecer achado.

**Sobre o `Gholamian2024`:** o autor trocou "370 **folhas**" por "370
**categorias terminais** (as \emph{folhas} da taxonomia)". Conferi se isso
enferruja alguma ficha: a `fichamentos/Gholamian2024.md` (não é minha, veio em
`12df845`) usa "370 folhas" descrevendo **o artigo**, onde "folha" é o termo do
próprio Icecat. Continua correto — a glosa que o autor acrescentou é da **prosa
da tese**, para o leitor, não da ficha. **Nada a fazer.**

# 4. O achado do nível 3 continua de pé

Reconferi na main de hoje: a cláusula "**com benefício limitado em textos muito
curtos**" segue **sem citação própria**, encostada em `\cite{Goodfellow2016,
Xu2017}` — e o `Xu2017` é um artigo que *propõe* redes convolucionais para
texto curto, ou seja, argumenta pelo benefício. O R7 não passou por ali. A
pendência permanece com o autor, como estava.

# 5. Estado das guardas, medido contra `16a92e5`

Rodei numa *worktree* limpa da própria main (na primeira tentativa a
*worktree* falhou por registro obsoleto e os comandos rodaram no diretório
errado; refiz — não vale medição de lugar errado):

- `check-travessao-titulo.py` → **exit 0**, com os 2 AVISOS das legendas do
  Cap. 5, que são exatamente o que a `conserto/legendas-travessao-cap5` conserta
  e que hoje já não travam nada.
- `check-bib.py` → **exit 0**.
- Travessões no Cap. 2 inteiro: **1** — o da linha 113, que é do autor e está
  com ele para decidir. A faixa do t3 está com **zero**.

# 6. O que eu não fiz

Não toquei em `2-fundam/texto.tex`: a faixa do t3 segue congelada por `34bd78a`
e, mesmo que não estivesse, resolver esse conflito é decisão de fila, não minha.
Não peguei lock. Não apaguei branch.
