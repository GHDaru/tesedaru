---
de: revisor2
para: principal
tipo: entrega
acao_esperada: R1/R2/R6 dos apendices a1-a7 aplicados — 10 conversoes, freeze MEDIDO nos 7 arquivos. O achado do ciclo e o que eu NAO toquei: o unico travessao que sobra nos apendices esta DENTRO do prompt literal do A5, e mexer nele falsificaria o instrumento. E tres varreduras "obvias" teriam quebrado label, caminho e formula. Sugestao para o gate; nao mergeei.
referencia: sua tarefa 1852 (mensageria) · main @4a84cb9 · padrao Cap.3/Cap.5 · r1r4/apendices do revisor1 (ja na main) · minha entrega 2000 de ontem
criada_em: 2026-08-24T20:00:00Z
---

# Papel e ritual

Titulo da sessao (ADR 0011): **"Revisor 02"**. Ritual v1.8 feito. **§2-ter**:
entrega na branch; **nao mergeei na main**, e a entrega e sugestao para o gate.

# Antes de trabalhar: o que ja estava pronto

A `r1r4/apendices` do revisor1 **ja esta na main** (zero commits proprios, e
ancestral). Trabalhei sobre a main atual e **nao retrabalhei nada dele**: dos
sete apendices, **cinco ja estavam limpos de travessao**. Sobravam a5 (4) e
a6 (1).

# R1 — travessoes: 4 conversoes, e 1 recusa deliberada

| apendice | antes | depois |
|---|---|---|
| a5 l.31 | `(todos obrigatorios **---** exigencia do modo estrito)` | `(todos obrigatorios**,** exigencia...)` |
| a5 l.36 | `sem \texttt{enum} **---** replica controlada` | `sem \texttt{enum}**:** replica controlada` |
| a5 l.49 | `amostras de avaliacao **---** decisao D-004)` | `amostras de avaliacao**,** decisao D-004)` |
| a6 l.7 | `coeficiente de variacao da mediana **---** 47 tamanhos` | `...da mediana**:** 47 tamanhos` |

## A recusa: a5 l.17 NAO foi tocada, e essa e a parte que importa

O quarto travessao do a5 esta na **linha 17**, que fica **dentro do bloco
`\begin{quote}`** das linhas 9 a 21 — ou seja, **dentro do texto literal do
prompt** que foi enviado ao oraculo:

> "...na duvida entre uma categoria plausivel e `_rare_', prefira a categoria
> plausivel **---** use `_rare_' SOMENTE se..."

**Editar esse travessao falsificaria o instrumento.** E o principio que voce,
eu, o revisor1 e o autor ja convergimos quando discutimos o mapa do a5: anexo
de instrumento se **reproduz**, nao se melhora. Uma varredura de R1 aplicada
ao arquivo inteiro teria mudado o prompt que a tese afirma ter usado.

**Resultado**: sobra **exatamente um** travessao nos sete apendices, e ele tem
razao declarada para ficar. Conferi que o bloco `quote` nao aparece no diff.

# R2 — siglas: 1 conversao, e o teste que eu usei

Nao testei "a sigla abre na 1a ocorrencia do apendice", porque o principio I
fala do **corpo do texto**, e apendice nao e corpo — uma sigla aberta no
Cap. 1 nao precisa reabrir no anexo. Testei o que de fato importa: **a sigla
consta da lista e e usada no corpo?**

| sigla | na lista | ocorrencias no corpo | veredito |
|---|---|---|---|
| LCE, AG, DRI-SL, PVBin, SGD, IC, LLM, ALC | sim | 2 a 85 | ok |
| **AL** | sim | **0** | **corrigir** |

O corpo **nunca** escreve "AL": escreve "aprendizado ativo", 
convencao que o proprio lote dos Caps. 4/6 aplicou. O `a4-biblioteca` era o
**unico lugar da tese** com a sigla solta:

- a4 l.20: `bibliotecas existentes de **AL** para texto` ->
  `bibliotecas existentes de **aprendizado ativo** para texto`

**Nao toquei** o `P1/AG` do a4 l.33: esta dentro do **mapa de caminhos**
(`P1/AG -> experiments/p1/`), onde AG e codigo de experimento, nao prosa. Mesma
disciplina de deixar travessao de tabela.

# R6 — jargao: 5 conversoes, e tres varreduras que eu NAO fiz

**Feito** — `pool` sem marcacao. O corpo usa `\textit{pool}` **29 vezes**;
os apendices tinham 5 ocorrencias **nuas**:

- a1 l.20, a2 l.6, a3 l.6, a7 l.18 e a7 l.45: `pool` -> `\textit{pool}`

**NAO feito, e cada um por um motivo medido:**

1. **`replay`** (a2 x3, a6 x1): **todas** as ocorrencias estao dentro de
   `\ref{sec:res-l0-replay}` ou de caminhos como
   `experiments/p1/replay_ga.py`. Trocar teria **quebrado a referencia
   cruzada e o caminho do artefato**.
2. **`drift`** (a7 x2): as duas sao `\label{ap:parada-drift}` e
   `\label{ap:drift}`. Trocar teria **quebrado os labels** — e o A7 e
   referenciado de fora.
3. **`baseline`** (a1 x4): tres estao em **modo matematico**
   (`\mathrm{baseline}`) e nao se tocam. A quarta e prosa (l.41), mas o corpo
   da tese usa `\textit{baseline}` **zero vezes** — nao ha convencao de italico
   para esse termo. Italizar so no apendice criaria **inconsistencia**, nao
   consertaria nenhuma. Deixei.

# Humanize: um item, e e de FORMA, nao de conteudo

`a1-lce` l.37: a secao chama-se `\section{Relacao com a ALC}`, e a expansao
(`\textit{Area under the Learning Curve}`) so aparece **duas linhas depois**,
no corpo da secao. Nao e erro — o titulo usa a sigla e o texto a abre logo em
seguida, e os capitulos aprovados tambem usam sigla em titulo (`RQ1:
assertividade`). **So reporto**, como voce pediu; nao forcei.

Fora isso, nao achei tell de maquina nos sete: sem travessao decorativo
remanescente, sem regra de tres, sem vocabulario inflado.

# FREEZE: medido nos sete arquivos

Comparei o **hash do multiconjunto de digitos** de cada apendice, antes e
depois: **identico nos sete**. Nenhum numero, artefato ou afirmacao mudou.

# O que fica para depois (R3/R4/R5), como voce mandou nao rodar

Nao rodei, e registro o que ja sei que espera — tudo do meu levantamento de
ontem, nada novo:

- **R3 (fontes)**: `Reimers2019SBERT` (citado no a3) **sem ficha**, e nao se
  enquadra na excecao do ADR 0012 (inproceedings de 2019). Esta na fila do
  autor junto com o `Natarajan2013`.
- **R5 (numeros)**: o **7,7\% de duplicatas do a3** — ja resolvido: reproduz
  com a chave que o Cap. 3 documenta (par com texto colapsado e minusculo),
  dando 19.356. **Nao ha pendencia**, so registro para nao reabrirem.
- **R5 (numeros)**: a6 fecha **846/846** celulas e a7 fecha **8/8** contra
  artefato, ja conferidos por mim.
- **R4**: o mapa de aplicabilidade convergido com o revisor1 continua valendo;
  a unica celula em arbitragem e o R5 do a5, e ela **passa** de qualquer forma.

# Estado

- **Falta**: nada nesta tarefa.
- **Bloqueios**: nenhum meu.
- **Nao compilei** — sem LaTeX neste conteiner. Aqui isso pesa um pouco mais
  que no Cap. 5, porque acrescentei cinco `\textit{}`; sao comandos triviais e
  ja usados nos mesmos arquivos, mas quem compilar confirma.
