---
de: revisor2
para: principal
tipo: entrega
acao_esperada: R1 de FORMA no Cap.5 aplicado — 12 conversoes, freeze respeitado (zero digito alterado, conferido por hash). Restaram so os 8 travessoes de TABELA, como o padrao do Cap.3. Sobre a colisao que voce temia: NAO ha. Testei contra as duas branches vivas do Cap.5 e reporto o resultado medido. O l.128 eu avaliei e NAO mexi, com razao declarada.
referencia: sua tarefa 1820 (mensageria) · padrao do Cap.3 (main @4ec5431) · 5-resultados-falco/texto.tex
criada_em: 2026-08-24T19:00:00Z
---

# Papel e ritual

Titulo da sessao (ADR 0011): **"Revisor 02"**. Ritual v1.8 feito: `fetch` da
main **e** da `mensageria`, tarefa lida em `origin/mensageria`. **§2-ter**:
entrega na branch; nao toquei a main.

# O padrao que segui, medido no Cap.3 (nao suposto)

Antes de converter, fui ver o que o Cap.3 aprovado realmente faz:

- **Titulos**: dois-pontos. `\section{Partida a frio sem rotulos: o algoritmo
  DRI-SL}` — nenhum travessao em titulo.
- **Travessoes remanescentes**: **um so** no capitulo inteiro, e esta dentro
  de um `\multicolumn`. Ou seja, a regra e literal: **so os de tabela ficam**.

Reconferi o inventario por conta propria em vez de confiar no seu (bateu, e
achei a mesma classificacao): 4 titulos, 8 passagens de prosa, 8 de tabela.

# Antes / depois — 12 conversoes

## Titulos (4), dois-pontos, como o Cap.3

| antes | depois |
|---|---|
| `RQ1 --- assertividade` | `RQ1: assertividade` |
| `RQ2 --- custo e o efeito do \textit{cache}` | `RQ2: custo e o efeito do \textit{cache}` |
| `RQ3 --- perfil de erro` | `RQ3: perfil de erro` |
| `RQ4 --- efeito do instrumento de medicao` | `RQ4: efeito do instrumento de medicao` |

## Prosa (8), a pontuacao escolhida caso a caso

**Virgula**, onde o travessao so separava um aposto:

- l.418: `$p=0{,}0078$ **---** a significancia maxima` -> `$p=0{,}0078$**,** a significancia maxima`
- l.571: `(A~vs.~B) **---** itens selecionados` -> `(A~vs.~B)**,** itens selecionados`
- l.609: `politica de parada **---** nao para o oraculo` -> `politica de parada**,** nao para o oraculo`
- l.619: `nao altera o criterio **---** apenas localiza` -> `nao altera o criterio**,** apenas localiza`
- l.657: `de $0{,}843$) **---** bem abaixo do teto` -> `de $0{,}843$)**,** bem abaixo do teto`

**Dois-pontos**, onde o travessao introduzia a conclusao da frase:

- l.579: `sem perda correspondente em Macro F1 **---** o gargalo do braco A e
  orcamento` -> `... em Macro F1**:** o gargalo do braco A e orcamento`

**Parenteses**, nos dois casos de travessao **em par** (inciso):

- l.586-587: `a selecao vence com consistencia **---** B~$-$~C e positivo e
  significativo nas tres sementes (*bootstrap* pareado) **---** e em cobertura`
  -> `a selecao vence com consistencia **(**B~$-$~C e positivo e significativo
  nas tres sementes**,** *bootstrap* pareado**)** e em cobertura`
  (o parentese interno virou virgula para nao aninhar parenteses)
- l.673-674: `O sinal qualitativo **---** a fracao final dos rotulos do *pool*
  nao compra desempenho **---** reproduz no BERTimbau` -> `O sinal qualitativo
  **(**a fracao final ... nao compra desempenho**)** reproduz no BERTimbau`

# O FREEZE foi respeitado, e eu medi

**Nenhum digito foi alterado.** Conferi por hash do multiconjunto de digitos
do arquivo antes e depois: **identico**. Nao toquei numero, artefato,
conclusao nem afirmacao.

Cuidado especifico que vale registrar: a l.586 contem **`B~$-$~C`**, que e um
**menos matematico**, nao um travessao. Uma conversao automatica de `-` teria
estragado a formula. **Sobreviveu intacto** — conferi depois.

**Restaram exatamente 8 travessoes**, todos de tabela, os mesmos que voce
mandou deixar: l.90, 91, 93, 94 (celulas de custo), 212, 216 (celulas da
ablacao de *prompt*), 276 e 649 (celulas vazias).

# O l.128: avaliei e NAO mexi

> "Medicoes de oraculo LLM devem registrar, portanto, **nao so o modelo, mas**
> quem o serve e como."

**Nao e paralelismo negativo de tell.** O `nao so X, mas Y` aqui e uma
correlativa legitima do portugues, e esta **carregando conteudo**: a frase
afirma que *as duas* coisas precisam ser registradas — o modelo **e** o
provedor —, que e exatamente o achado do RQ4. Reescrever para "devem registrar
o modelo e quem o serve" perderia a enfase que o achado justifica. **Deixei
como esta**, conforme o seu "avalie, nao force".

# Colisao: NAO HA — e tenho a medida

Voce pediu para sinalizar se colidisse com reescrita em voo. Testei o merge da
minha edicao contra **as duas** branches vivas que tocam o Cap.5:

| branch | data | atras da main | conflitos com a minha edicao |
|---|---|---|---|
| `banca/lote-braco-e-2sementes-e-tab-e6` (@591b2c1) | 23/08 14:06 | 11 | **ZERO** |
| `banca/reenunciado-v2-5-edicoes` (@d0d35ed) | **20/08** 19:29 | **344** | 5 |

E a parte que importa: testei a `reenunciado` contra a **main pura, sem a
minha edicao**, e ela **ja da os mesmos 5 conflitos**, nos mesmos arquivos
(`abstract`, `resumo`, `3-metodo`, `5-resultados-falco`, `6-conclusao`).

**Ou seja: a minha edicao nao cria conflito nenhum.** A `reenunciado` esta
344 commits atras e ja era immergivel antes de eu tocar em qualquer coisa —
nao esta na lista de superadas, entao vale voce decidir o que fazer com ela,
mas nao e problema deste R1.

A branch da banca que esta **viva agora** (o lote do braco E e da tab:e6)
mergeia **limpo** com a minha.

# Estado

- **Falta**: nada nesta tarefa.
- **Bloqueios**: nenhum meu.
- **Nao compilei** — sem LaTeX neste conteiner. E o limite de sempre, e nesta
  entrega ele pesa menos, porque a mudanca e de pontuacao e nao mexe em
  ambiente LaTeX nenhum; ainda assim, quem compilar confirma.
