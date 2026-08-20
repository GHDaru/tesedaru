# QA — ciclo 011: integração das 3 checagens do revisor1 ao `check-bib.py`

**Tarefa:** aviso 20260817-1135 do principal (integração LIBERADA, gate `@ae332f3`)
**Executor:** revisor2 · **Branch:** `ciclo/011-integra-check-bib`
**Superfície travada:** `scripts/check-bib.py` (lock `51001e3`, 2026-08-17T12:20Z)
**NÃO tocado:** `scripts/checagens_extra_bib.py` (do revisor1 — **importado, não
copiado**) e `referencias.bib` (superfície dele).
**Skills:** `diagnose-before-fix` (reproduzir antes de consertar) ·
`verifiable-dod` (critério vira comando)

## O que foi integrado

| # | Checagem | Origem | Severidade escolhida |
|---|---|---|---|
| 5 | `campos_key_residuais` | revisor1 | **erro** — substitui o meu `^\s*key\s*=` |
| 7 | `titulos_duplicados` | revisor1 | **erro** — complementa o DOI repetido |
| A1 | `entradas_orfas` | revisor1 | **aviso** — nunca reprova |

Refatoração que a integração exigiu: `checar(raiz) -> list[dict]` saiu de
dentro do `main()`. Agora cada achado é dado (`codigo`, `detalhe`,
`severidade`), o `main()` só imprime e decide o exit, e o verificador pode ser
testado por fixture **sem subprocesso e sem tocar no repositório real**. Novo
`--sem-avisos`, igual ao do `check-fichamentos.py`.

Por que órfã é aviso e não erro: são **95** no acervo. Um invariante que nasce
vermelho em 95 entradas é DoD inalcançável — foi o defeito do lote 5 — e a
regra "matar órfã", aplicada cegamente, já quase matou `Sener2018` e
`Shen2018`.

## DoD executável (princípio IX) — vermelho ANTES, verde DEPOIS

Nenhuma linha é julgamento; todas são comando com saída observada.

| # | Critério | Script da main | Script integrado |
|---|---|---|---|
| 1 | `key = {residuo}` em entrada de **uma linha** | `PROBLEMAS: nenhum`, **exit 0** ← falso negativo | **acusa** `UmaLinhaComKey`, exit 1 |
| 2 | `note = {ver tabela, key = valor}` (falso positivo que eu relatei) | — | **não dispara** |
| 3 | título duplicado com UM lado sem DOI | não vê | **acusa** `TituloDuplicadoA/B` |
| 4 | órfã aparece | não vê | **listada em AVISOS** |
| 5 | órfã **sozinha** não reprova | — | aviso impresso, **exit 0** |
| 6 | `--sem-avisos` some com os 95 avisos e mantém o exit | — | **ok**, exit 1 pelo erro real |
| 7 | `checar()` é pura (não imprime, não sai) | não existia | `{'erro': 1, 'aviso': 95, 'info': 1}` |

O critério 1 é o motivo do ciclo. Reproduzi o defeito **antes** de trocar a
implementação: o fixture com `key = {residuo}` numa entrada de uma linha
passava como "nenhum problema". Falso negativo é pior que falso positivo,
porque tem cara de cobertura.

## Efeito no acervo real (princípio V)

| Medida | Script da main | Script integrado |
|---|---|---|
| entradas no bib | 337 | 337 |
| chaves citadas nos `.tex` | 152 | 152 |
| erros | 0 (**exit 0**) | **1** (exit 1) |
| avisos | não existiam | **95** órfãs |

**O vermelho é achado verdadeiro, não regressão da integração.** Nome, causa e
conserto abaixo.

## Achado: `Razali2020` é entrada fabricada (5º caso de sequestro de identificador)

O erro novo é `mesmo titulo em 2 chaves: Razali2020, Widodo2022`. Investiguei
antes de chamar de duplicata, porque título igual também acontece entre obras
distintas (foi a armadilha do `Barros2014`). Evidência, toda com artefato:

| Verificação | Resultado |
|---|---|
| título na Crossref | existe **uma única** obra com esse título: `10.33395/sinkron.v7i4.11792` — o `Widodo2022`, que eu li no PDF e fichei |
| coordenadas declaradas no `Razali2020` (J. Phys. Conf. Ser. **1529**(2):022098, 2020) | resolvem para **outro artigo**: "Mobile Application Outdoor Navigation Using Location-Based Augmented Reality (AR)", de Asraf, Hashim e Idrus |
| obra real de Razali/Sutikno sobre validação cruzada estratificada | **nenhuma** — nem por busca de título, nem por autor+tema, nem nos 102 registros de Sutikno no próprio periódico |
| a tese cita `Razali2020`? | **não** — `grep` em todos os `.tex` e `.md`: zero ocorrências |
| algum fichamento a ancora? | **não** |

Conclusão: `Razali2020` copia o título do `Widodo2022` sobre coordenadas de um
artigo alheio. É o mesmo padrão das 4 chaves já mortas (`Yu2022`, `Zhang2020`,
`Liang2024LLMActive`, `Qi2020FLAL`).

**Bom que ninguém a cita:** não há dano no texto e o PDF nunca a compilou. O
conserto é remover a entrada — uma linha de bloco no `referencias.bib`, que é
**superfície do revisor1**, por isso não a toquei. Quando ela sair, acrescento
`Razali2020` ao conjunto `MORTAS` do meu script (uma linha, minha superfície),
para que ela não volte a ser citada.

**Não silenciar a checagem para ficar verde.** O `check-bib` deve continuar
acusando até a entrada sair; era exatamente para isto que a checagem 7 existia.

## Pendências declaradas

1. **Verificação cruzada (PROTOCOLO §6):** quem executa não verifica. Pedi ao
   revisor1, via principal, que confira esta integração — em especial se a
   severidade que escolhi para cada código respeita o contrato das funções
   dele ("nenhuma decide severidade; quem integra decide").
2. **Utilitário compartilhado, proposto e não feito:** hoje há **três**
   implementações de "esvaziar o conteúdo entre chaves" — o `_esqueleto` dele
   (preserva posições), o meu `campos_declarados` no `check-fichamentos.py`
   (devolve nomes de campo) e o laço solto de contagem de chaves aqui. Três
   scripts com defeito de parsing de `.bib` no mesmo dia não é coincidência: é
   duplicação. Proposta é módulo único, mas **quem decide é o principal** —
   mexer nos dois donos ao mesmo tempo é romper superfície.
