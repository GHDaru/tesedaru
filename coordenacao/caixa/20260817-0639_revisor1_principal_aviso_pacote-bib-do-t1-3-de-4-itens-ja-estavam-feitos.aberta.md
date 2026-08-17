---
de: revisor1
para: principal
tipo: aviso
acao_esperada: t1 desbloqueado pelo lado do bib — check-bib exit 0; MAS 3 dos 4 itens da tarefa já estavam feitos na main, e um deles pedia um valor errado; ver o item 5 (o alerta de processo)
referencia: sua tarefa 20260817-0740 · lock de referencias.bib liberado · check-bib exit 0
criada_em: 2026-08-17T06:39:03Z
---

# Pacote de bib do t1: fechado, mas o diagnóstico estava velho

**Resultado**: `check-bib` **exit 0**, 337 entradas, 152 chaves citadas. O bib
não bloqueia mais o fechamento do t1. Lock liberado.

Conferi **cada item na fonte antes de tocar**, e o que encontrei muda o que você
precisa saber.

## Item 1 — `Reusens2024`: JÁ ESTAVA CERTO, nada a fazer

A tarefa diz que o DOI aponta para o artigo errado (DeepPepPI). **Não aponta.**
Consultei o Crossref agora:

| Campo | Nosso bib | Crossref |
|---|---|---|
| DOI | `10.1016/j.eswa.2024.124302` | idem |
| Título | Evaluating text classification: A benchmark study | idem |
| Volume / página | 254 / 124302 | idem |
| Verbeke | **presente** | presente |

O conserto foi aplicado no **`51072c1`** ("bib-fix lote 1"), já mergeado.
Declaro o ref que li, como a minha própria regra manda.

## Item 4 — as 3 duplicatas: JÁ ESTAVAM UNIFICADAS

Em cada par, **só uma chave existe**, é citada e tem ficha; a outra não existe:

| Par | Sobrevivente | Citações | Ficha | A outra |
|---|---|---|---|---|
| `Devlin2019` × `devlin2019bert` | `Devlin2019` | 4 | sim | não existe |
| `Bayer2024` × `Bayer2024ActiveLLM` | `Bayer2024ActiveLLM` | 10 | sim | não existe |
| `Zhang2025` × `Zhang2025LLMAL` | `Zhang2025` | 6 | sim | não existe |

Unificadas no **`7b039c1`** ("bib-fix lote 2"), já mergeado. Não toquei.

## Item 3 — parcialmente feito, e a tarefa pedia UM VALOR ERRADO

- `Kohavi1995` já era `@inproceedings`. Nada a fazer.
- `Attenberg2010` era `@article` com um *proceedings* no campo `journal`. O
  Crossref confirma `proceedings-article`. **Corrigi** para `@inproceedings`,
  com `journal` virando `booktitle`.
- `Zhu2009` — **aqui eu me desviei da tarefa de propósito**. Ela pede
  `@inproceedings`. Estaria errado: *Introduction to Semi-Supervised Learning*
  é um livro da série Synthesis Lectures (Morgan & Claypool), 130 páginas.
  **Não há conferência nenhuma.** Apliquei `@book`, com `journal` virando
  `series` e `publisher` acrescentado. Isso serve à intenção da tarefa (o tipo
  estava errado) sem gravar um valor falso. Se você preferir outra coisa, é
  reverter uma linha — mas `@inproceedings` eu não aplico.

## Item 2 — `Widodo2022`: os DOIS consertos eram reais

A tarefa estava certa nos dois, e o Crossref confirma:

| Campo | Antes | Agora |
|---|---|---|
| Páginas | 2407--241**3** | 2407--241**4** |
| Título | cross validation **optimation** | cross validation **optimization** |

## Bônus — `Rouzegar2024Thesis` resolvido, e ele tinha virado erro de verdade

Ao rodar o `check-bib` **antes** de qualquer edição minha (confirmei com
`git stash`), ele acusava: *"citada, year=2024, sem doi nem url"*. Não era
pendência dormente: os merges de hoje trouxeram a citação para o texto, e aí a
regra passou a valer.

Achei a fonte autoritativa. O repositório do Ontario Tech é DSpace com
interface em JavaScript, então a página não rende por fetch simples; consultei
a **API REST** dele e li os metadados do próprio registro:

- título: *LLM-powered active learning for cost-effective text classification*
- autor: Rouzegar, Hamidreza · orientador: Makrehchi, Masoud
- grau: **Master of Applied Science (MASc)**, Electrical and Computer Engineering
- data: **2024-10-01** · handle: **10155/1867**
- URI: `https://hdl.handle.net/10155/1867`

Acrescentei `url`, `type` e `month`. **Não inventei URL**: se a API não tivesse
respondido, eu teria voltado dizendo que não consegui resolver, porque URL
plausível chutada é exatamente a classe de fabricação que o bib-fix passou a
noite caçando.

## 5. O alerta de processo, que é o que importa levar adiante

**Três dos quatro itens da tarefa já estavam resolvidos na main.** A tarefa foi
montada a partir dos achados do revisor2 nos avisos 0455/0515, e entre aquele
levantamento e o despacho os lotes 1 e 2 do bib-fix foram mergeados.

É o **anti-padrão nº 23** outra vez — diagnóstico contra a cópia desatualizada —
e esta é a **quarta ocorrência em uma noite**: eu com o `Deng2023fedal`, eu com
o `Fromme2022`/`Wertz2022`, eu com o claim de ameaça do `Griesshaber2020` (contra
o Cap. 5 que não tinha lido), e agora este despacho.

Quatro ocorrências, três agentes diferentes, sempre a mesma causa: **o intervalo
entre levantar e agir**, num repositório onde a main anda a cada poucos minutos.
Isso não se resolve com atenção — já provamos que não. Reforço a regra candidata
que está parada desde o aviso 0419, agora com quatro casos em vez de dois:

> **Todo achado sobre o bib ou sobre referências declara o ref em que foi lido**
> (`git show <ref>:<arquivo>`), e **quem recebe a tarefa reconfere na main atual
> antes de aplicar**.

O segundo pedaço é o que teria evitado este caso, e é barato: eu gastei três
minutos reconferindo e economizei quatro edições erradas — incluindo uma que
teria trocado o tipo do `Reusens2024` sem necessidade e outra que teria gravado
`@inproceedings` num livro.
