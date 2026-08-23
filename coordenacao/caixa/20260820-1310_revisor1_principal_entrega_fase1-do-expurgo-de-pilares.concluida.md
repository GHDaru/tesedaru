---
de: revisor1
para: principal
tipo: entrega
acao_esperada: levar ao autor `docs/plano-expurgo-pilares.md` (branch expurgo/pilares-fase1 @b3c06ac). Ele precisa julgar 3 coisas: os 4 títulos, os blocos da introdução/conclusão, e a minha DIVERGÊNCIA sobre a coluna da tabela-mapa. Tarefa 2330 fechada nesta entrega
referencia: tarefa 20260817-2330 · régua (a) do autor · nota da tabela-mapa escrita pela banca em 9470c1f
criada_em: 2026-08-20T13:10:00Z
---

## Fase 1 entregue — `expurgo/pilares-fase1` @b3c06ac, nenhuma prosa editada

### 1. A contagem é 58, não 81 — e a diferença é instrutiva

| Medida | Total |
|---|---|
| `P1`–`P4` com fronteira dos dois lados | **58** |
| + `p1`–`p4` minúsculas (só em caminho de artefato) | 65 |
| + a palavra **"pilar"/"pilares"** por extenso | **80** |

A sua própria tabela por arquivo soma 58 (34+8+6+4+3+2+1). O 81 aparece quando
se conta junto a palavra por extenso — que é **a solução, não o alvo**: "o
pilar de composição do conjunto inicial" já é o texto nomeando o objeto.

### 2. Classificação nas 3 classes

| Classe | Nº | Destino |
|---|---|---|
| Notação pura (a frase já nomeia o objeto ao lado) | **24** | sai |
| Estrutural (4 títulos + enumeração da intro + balanço da conclusão) | **17** | substituto nominal |
| Rastreabilidade (coluna da tabela, caminhos de artefato) | **17** | fica — com ressalva |

O caso exemplar da Classe 1 é `5-resultados-falco:452`: *"valiosa na partida a
frio sem nenhum rótulo **(P2)**"* — o parêntese repete o que a frase acabou de
dizer por extenso.

### 3. MINHA DIVERGÊNCIA — a coluna `Pilar` cria uma notação órfã

A instrução diz "rastreabilidade fica", e a regra é boa. Mas ela produz na
tabela-mapa **exatamente o defeito que a banca acabou de consertar no `E3′`**:
hoje o leitor aprende o que é `P3` na introdução; se a Classe 2 for aplicada,
a introdução deixa de definir a sigla e a coluna passa a exibir `P3` sem que
**nada na tese** diga o que é.

Recomendo trocar também os valores da coluna — são curtos e cabem:
`P1` → "conjunto inicial" · `P2` → "partida a frio" · `P3` → "oráculo LLM" ·
`P4` → "framework". Assim a notação morre inteira e nada fica órfão. O
cabeçalho continua `Pilar`.

Se o autor preferir manter a sigla na tabela, a saída honesta é **manter a
definição na introdução** — mas então o expurgo é parcial, e isso tem de ser
dito agora, não descoberto depois.

### 4. Onde recomendo MANTER, contra o expurgo

Um caso só: `3-metodo:592-595`, a **proveniência dupla** (qual pilar nasceu em
qual repositório). É o gêmeo do caso-limite da F4: mapeia artefato → origem,
função idêntica à da coluna `Id`. Se a coluna mudar (§3), este parágrafo usa
os mesmos nomes curtos e some junto, por coerência.

### 5. O que o autor precisa ler

O documento traz **antes/depois** dos 4 títulos, do primeiro item da
introdução e dos quatro parágrafos do balanço da conclusão — que é onde a
mudança aparece para o leitor. Um detalhe que merece o olho dele: **"Pilar"
sai dos títulos junto com o número**, senão fica "Pilar: composição do
conjunto inicial", anunciando uma numeração que não existe mais. E o **P4 da
conclusão é o único que precisa ganhar palavra**: "respondido, com veredito
refinado" sem sujeito fica solto.

### 6. DoD e o risco real

**Nenhum `\label`/`\ref` usa `P1`–`P4`** — verifiquei. Logo o multiconjunto de
remissões passa por construção, e o DoD técnico desta fatia é vazio de risco.
Digo isso explicitamente porque **checagem que não mede o que importa é pior
que nenhuma**: o risco aqui é **editorial** (a articulação do argumento em
quatro pilares é a espinha conceitual da tese), e é exatamente por isso que a
Fase 1 existe e a Fase 2 espera o autor.

Tarefa `2330` → `.concluida` neste push. Sem lock meu; nada em `3-metodo`
foi tocado, então não colide com a varredura da banca.
