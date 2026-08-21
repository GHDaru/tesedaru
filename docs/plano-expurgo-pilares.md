# Expurgo da notação de pilar (P1–P4) — Fase 1: levantamento

**Ordem**: do autor, despachada na tarefa `20260817-2330`.
**Regra a aplicar**: a mesma dos códigos de experimento — *notação interna não
vai para o leitor; o texto nomeia o objeto*.
**Natureza desta fase**: levantamento. **Nenhuma linha de prosa foi editada.**
**Executado por**: revisor1 · **Medido na `main`** de 2026-08-20.

---

## 0. Antes do inventário: a contagem é 58, não 81

A tarefa parte de "81 ocorrências". Medi 58 — e a divergência tem causa
localizável, não é ruído de régua:

| Medida | Total |
|---|---|
| `P1`–`P4` com fronteira alfanumérica dos dois lados | **58** |
| idem + `p1`–`p4` minúsculas (só em caminhos de artefato) | 65 |
| idem + a palavra **"pilar"/"pilares"** por extenso | **80** |

**A própria tabela do despacho soma 58** (34+8+6+4+3+2+1). O número 81 só
aparece quando se conta junto a palavra *pilar* escrita por extenso — que é
exatamente **a solução, não o problema**: "o pilar de composição do conjunto
inicial" é o texto nomeando o objeto, que é o que a régua pede.

Uso 58 daqui em diante, e o comando está no fim do documento.

---

## 1. Inventário classificado nas três classes

| Classe | Ocorrências | Destino |
|---|---|---|
| **1. Notação pura** — o texto já nomeia o objeto ao lado | **24** | **SAI** |
| **2. Estrutural** — a notação É o esqueleto do argumento | **17** | substituto **nominal** |
| **3. Rastreabilidade** — tabela, `\texttt{}`, artefato | **17** | **FICA** (com uma ressalva, §4) |

### Classe 1 — notação pura (24): sai sem custo

O padrão é sempre o mesmo: um parêntese com a sigla logo depois da frase que
já diz o que ela é.

| Onde | Trecho | Proposto |
|---|---|---|
| `3-metodo:7-10` | "(P1) o impacto da composição…; (P2) a construção…; (P3) a viabilidade…; e (P4) a avaliação" | remover só os parênteses — a enumeração já descreve cada um |
| `3-metodo:116` | "LLM (P3) e de supervisão para o classificador (P4)" | "LLM e de supervisão para o classificador" |
| `3-metodo:226` | "a otimização por algoritmo genético (P1)" | "a otimização por algoritmo genético" |
| `3-metodo:339-340` | "é avaliado (P2) contra a amostragem aleatória e contra o envelope … (P1)" | remover ambos |
| `3-metodo:535` | "os achados de instrumentação (P3) são mecanismos" | "os achados de instrumentação são mecanismos" |
| `3-metodo:592-595` | "P1 e P2 (estudo de sensibilidade…)"; "os pilares P3 e P4 (…)"; "verificação de P1/P2" | **ver §4** — é o parágrafo de proveniência |
| `4-resultados-l0:55` | "Esses resultados fundamentam o P2" | "…fundamentam o pilar da partida a frio" |
| `4-resultados-l0:126` | "O resultado central do P2" | "O resultado central da partida a frio sem rótulos" |
| `5-resultados-falco:452` | "valiosa na partida a frio sem nenhum rótulo (P2)" | remover o parêntese — a frase **já diz** "partida a frio sem nenhum rótulo" |
| `6-conclusao:209` | "os replays de P1/P2" | "os replays dos dois primeiros pilares" |
| `0-iniciais/declaracao-ia:17` | "os experimentos originais dos pilares P1 e P2" | "os experimentos originais dos dois primeiros pilares" |

`5-resultados-falco:452` é o caso exemplar da regra: a sigla repete, entre
parênteses, o que a frase acabou de dizer por extenso.

### Classe 2 — estrutural (17): precisa de substituto nominal

São três blocos, e os três são **a mesma lista de quatro**, em três lugares.

**(a) Os 4 títulos do Cap. 3** — antes/depois:

| Antes | Depois |
|---|---|
| `\section{Pilar P1: composição do conjunto inicial $L_0$}` | `\section{Composição do conjunto inicial $L_0$}` |
| `\section{Pilar P2: \textit{cold start} sem rótulos --- algoritmo DRI-SL}` | `\section{Partida a frio sem rótulos: o algoritmo DRI-SL}` |
| `\section{Pilar P3: LLMs como oráculo de rotulagem}` | `\section{LLMs como oráculo de rotulagem}` |
| `\section{Pilar P4: o framework FALCO e sua avaliação}` | `\section{O framework FALCO e sua avaliação}` |

Observe que **"Pilar" também sai**: mantê-lo sem o número deixaria "Pilar:
composição do conjunto inicial", que anuncia uma numeração que não existe mais.

**(b) A enumeração da introdução** (`1-intro:126-137`) — é onde a notação
NASCE. Antes/depois do primeiro item, e os outros seguem o mesmo molde:

> **Antes**: `\item \textbf{P1 — composição do conjunto inicial}: quantificar o impacto…`
> **Depois**: `\item \textbf{Composição do conjunto inicial}: quantificar o impacto…`

**(c) O balanço da conclusão** (`6-conclusao:12, 20, 28, 41`) — é o eco da
introdução, e o mais delicado, porque a sigla ali carrega o veredito:

> **Antes**: `\textbf{P1 — a composição do conjunto inicial importa, e importa mais quanto menor o orçamento.}`
> **Depois**: `\textbf{A composição do conjunto inicial importa, e importa mais quanto menor o orçamento.}`

> **Antes**: `\textbf{P4 — respondido, com veredito refinado e diagnóstico.}`
> **Depois**: `\textbf{O framework integrado: respondido, com veredito refinado e diagnóstico.}`

O P4 é o único que **precisa ganhar palavra**: "respondido, com veredito
refinado" sem sujeito fica solto. Os outros três já trazem o objeto na frase.

Restam ainda `1-intro:168-169` ("(P1 e P2)", "(P3 e P4)") e
`5-resultados-falco:4,7` ("O pilar P3 traz…", "O pilar P4 traz…"), que são
ponte entre capítulos: proposta é "os dois primeiros pilares" / "a avaliação
de oráculos e do framework", conforme a frase.

### Classe 3 — rastreabilidade (17): fica

- **Coluna `Pilar` da tabela-mapa** (`3-metodo:61-73`), 13 ocorrências — mas
  **com ressalva**, §4;
- **Caminhos de artefato**: `\texttt{experiments/p1}` (`3-metodo:83`),
  `P1/AG → \texttt{experiments/p1/}` (`a4-biblioteca:33`) — são nome de
  diretório em disco, não prosa;
- `\label`/`\ref`: nenhum usa `P1`–`P4`, então nada a preservar aqui.

---

## 2. Onde eu DIVERGIRIA da instrução — e o argumento

A tarefa manda **rastreabilidade ficar**, e eu concordo com a regra. Mas ela
cria, na coluna `Pilar` da tabela-mapa, exatamente o defeito que acabamos de
consertar com o `E3′`: **notação que sobrevive sem definição em lugar nenhum**.

Hoje o leitor aprende o que é `P3` na introdução. Se a Classe 2 for aplicada,
a introdução deixa de definir a sigla — e a coluna da tabela passa a exibir
`P3` sem que nada na tese diga o que é. É o mesmo orfanato do `E3′` que a
banca acabou de fechar escrevendo a nota sob a tabela.

**Recomendo trocar também os valores da coluna**, que são curtos e cabem:

| Hoje | Proposto |
|---|---|
| `P1` | conjunto inicial |
| `P2` | partida a frio |
| `P1/P2` | conjunto inicial / partida a frio |
| `P3` | oráculo LLM |
| `P4` | framework |
| `apoio a P4` | apoio ao framework |
| `P4 (condicional)` | framework (condicional) |

Com isso a notação **morre por inteiro** e nada fica órfão. O cabeçalho da
coluna continua sendo `Pilar`, que é o que o leitor precisa saber.

Se o autor preferir manter a sigla na tabela, então a alternativa honesta é
**manter a definição na introdução** — mas aí o expurgo é parcial, e isso
precisa ser dito, não descoberto depois.

## 3. Onde eu recomendaria MANTER, contra o expurgo

Um caso, e só um: **`3-metodo:592-595`, o parágrafo de proveniência dupla**.

> "Os resultados *originais* dos pilares **P1** e **P2** … foram produzidos no
> repositório `activetextclassification`; os pilares **P3** e **P4** … foram
> produzidos na biblioteca `activelearning`."

Aqui a sigla mapeia **experimento → repositório**, que é a mesma função da
coluna `Id`. É o gêmeo do caso-limite que marquei na F4, e pela mesma razão:
não é o texto corrido de que a nota da tabela fala, é registro de onde cada
artefato nasceu. **Se o autor aceitar a troca da coluna (§2), este parágrafo
deve usar os mesmos nomes curtos** — e aí some também, por coerência.

## 4. Custo e ordem sugerida

| Etapa | Ocorrências | Risco |
|---|---|---|
| 1. Classe 1 (parênteses) | 24 | nenhum — a frase não muda de sentido |
| 2. Os 4 títulos | 4 | nenhum — não há `\label` com `P1`–`P4` |
| 3. Introdução + conclusão | 13 | **é o que o autor deve ler**: muda a cara da contribuição |
| 4. Coluna da tabela (§2) | 13 | decisão do autor |
| 5. Proveniência (§3) | 6 | decorre de 4 |

**Nenhum `\label`/`\ref` usa a notação**, então a remissão interna não corre
risco: o DoD de multiconjunto passa por construção. O risco desta fatia é
**editorial**, não técnico — e é por isso que a Fase 1 existe.

---

## Como reproduzir as medições deste documento

```bash
cd /home/user/tesedaru
python3 - <<'PY'
import re, glob
pad = re.compile(r"(?<![A-Za-z0-9])P[1-4](?![A-Za-z0-9])")
for f in sorted(glob.glob('[0-9]-*/texto.tex')+glob.glob('a[0-9]*/texto.tex')
                +glob.glob('0-iniciais/*.tex')):
    n = sum(len(pad.findall(re.sub(r'(?<!\\)%.*','',l))) for l in open(f,encoding='utf-8'))
    if n: print(f, n)
PY
```

## O que esta fase NÃO decidiu

- **Nenhuma linha de prosa foi editada** — a tarefa é explícita.
- **A escolha é do autor**, inclusive quanto à minha divergência do §2.
- Os substitutos nominais são **proposta de redação**, não texto final.
