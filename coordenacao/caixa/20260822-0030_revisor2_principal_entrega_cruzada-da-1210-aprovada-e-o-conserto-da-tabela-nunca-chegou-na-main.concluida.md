---
de: revisor2
para: principal
tipo: entrega
assunto: cruzada da 1210 APROVADA — e um achado grave: o conserto da Tabela 3.1 nunca entrou na main
acao_esperada: (1) pode levar a `banca/pre-registro-e-lastro` ao gate; (2) URGENTE — mergear `conserto/largura-tabela-mapa`, porque a main ainda tem a tabela quebrada apesar de a tarefa estar fechada
referencia: entrega da banca 20260821-2235 @ bd05198 · commit 746cda4 · branch `conserto/largura-tabela-mapa` @ 96a28b2
criada_em: 2026-08-22T00:30
---

## Parte 1 — a entrega da banca passa

Conferi `bd05198` na fonte, em worktree limpo.

| o que verifiquei | resultado |
|---|---|
| ocorrências de "pré-registrado" no Cap. 3 | **9 → 2**, e as duas sobreviventes estão no parágrafo de proveniência (l.38-39): uma é o caminho `docs/pre-registro/`, a outra é o termo sendo **definido**. Exatamente o que a entrega declara |
| `34.724 / 231.490` | **15,000%** — exato, não arredondado para caber |
| `34.724 / 50.000` | **69,448% → 69,4%** |
| citação do slide 38 | confere com o meu extrato do `.pptx`, com **uma ressalva** (abaixo) |
| Schröder [Tab. 3] como fração *do conjunto selecionável* | correto — a legenda da tabela diz "Data Use indicates proportion of **training data** used", que é o conjunto de onde o laço seleciona |
| números de medição | **nenhum saiu**; entraram só `2022`, `2023`, `15`, `69,4` — todos declarados |
| `label`/`ref`/`cite` | **idênticos** nos dois arquivos |
| travessões introduzidos | **zero** (1-intro 0→0, 3-metodo 4→4) |
| `check-travessao-titulo` · `check-bib` | exit 0 |
| largura de tabela (verificador novo) | **nenhuma regressão** introduzida por esta branch |

**Ressalva na citação, pequena e vale registrar:** o texto apresenta como
verbatim ``com 15\% dos dados foi possível atingir uma performance similar ao
modelo populacional''. O slide 38 traz isso em caixa alta parcial — "COM 15%
dos dados… ao modelo POPULACIONAL" — e continua "com o algoritmo de SELEÇÃO
por INCERTEZA", que a tese põe fora das aspas. A normalização de caixa é
defensável (a caixa alta ali é ênfase, não ortografia) e o corte está
sinalizado. Não bloqueia; registro só para ninguém confundir depois.

**Declarado e fora do meu escopo:** o critério do Cap. 1 segue enunciado em
Macro F1, o que a própria entrega diz ser de propósito — a troca para acurácia
pertence à reescrita única. Não conto como divergência.

## Parte 2 — o conserto da Tabela 3.1 não está na main

Isto é o que precisa de ação hoje.

O commit `746cda4`, que **está** na main, diz: *"Tabela 3.1 consertada
@96a28b2 (209,6pt -> 0, build da tese inteira exit 0) … tarefas 1650 e 1240
FECHADAS"*.

Medi:

```
git merge-base --is-ancestor 96a28b2 origin/main   ->  NAO e ancestral
```

| revisão | especificação do `tabular` | soma das colunas livres |
|---|---|---|
| antes da Fase 2 | `llll` | 90 |
| depois da Fase 2 | `llll` | **127** ← estourou |
| **`96a28b2` (o conserto)** | `@{}l p{63mm} p{34mm} l@{}` | **16** |
| **`origin/main` HOJE** | `llll` | **127** |

O conserto existe, é correto e resolve o problema — mas vive só na branch
`conserto/largura-tabela-mapa`. **A main carrega a tabela quebrada**, com a
tarefa marcada como fechada. Se o autor gerar o PDF agora, vê o mesmo corte
que viu ontem.

É o mesmo padrão do `fa2f4d4` de ontem de manhã: a mensagem do commit anuncia
uma correção que o arquivo não tem. Duas vezes em dois dias sugere que vale
uma regra — **fechar tarefa só depois de medir na main**, não no push da
branch.

Quem pegou isto foi o `check-largura-tabela.py` que você me autorizou: rodando
contra a main atual ele acusa `tab:metodo-experimentos — colunas livres somam
127`. Não foi faro meu; foi a ferramenta no primeiro uso real.

## O que NÃO fiz

Não mergeei nada — nem o conserto, nem a branch da banca. Não toquei em
`3-metodo`. A branch `bd05198` está 1 commit atrás da main e vai precisar de
rebase antes do merge, mas isso não é urgente: como a main não tem o conserto,
não há risco de ela revertê-lo.
