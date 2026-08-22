# Padrão do grafo de conhecimento do acervo

> **Estado**: proposta v1, escrita pelo agente `local`. O aviso do autor
> (2026-08-22) pede que especialistas em grafos semânticos revisem a forma de
> reportar o grafo. **Se a revisão especialista propuser outra coisa, ela
> prevalece** e este arquivo é substituído — não emendado por cima.
>
> Pendência declarada: os IRIs de CiTO citados na tabela de mapeamento
> precisam ser conferidos **um a um** contra a especificação oficial da
> ontologia antes de qualquer publicação do `kg.ttl`. Estão aqui como intenção
> de mapeamento, não como fato verificado. Princípio III da constituição
> (afirmação fundamentada) vale para metadados também.

## O problema que o padrão resolve

Um acervo de ~180 obras vira grafo de três jeitos ruins e um bom.

Ruins: (a) grafo dentro de um banco proprietário, que ninguém abre sem
subir serviço; (b) grafo escrito à mão em JSON, que diverge das fichas no
primeiro dia; (c) grafo só de wikilinks, bonito de navegar e impossível de
consultar ("me dê todo paper que contradiz X e usa dataset Y").

O bom: **uma fonte de verdade, três projeções geradas**. A fonte é o
front-matter YAML das fichas. As projeções são derivadas por script e nunca
editadas à mão.

```
fichas/<Chave>.md  (YAML front-matter)   ← FONTE DE VERDADE, humana e versionada
        │
        ├─► seção "## Relações" com [[wikilinks]]  → navegação no Obsidian
        ├─► grafo/kg.json                          → a interface FALCO
        └─► grafo/kg.ttl (RDF)                     → consulta formal (SPARQL)
```

Regra dura: **projeção nunca é editada**. Achou erro no `kg.json`? O erro está
na ficha. Corrigir a projeção é criar a segunda verdade que este desenho
existe para impedir.

## Por que Obsidian é a camada humana

O autor sugeriu o modelo Obsidian, e ele serve — pelo motivo certo, que não é
o visual. Obsidian não é um formato: é markdown com front-matter YAML e
`[[wikilinks]]` numa pasta de arquivos. Isso significa:

- o acervo **continua legível sem o Obsidian** (é markdown em git);
- não há lock-in: se a ferramenta sumir, os arquivos ficam;
- os links são resolvidos por **nome de arquivo**, e o nome do arquivo já é a
  chave BibTeX — a identidade que o acervo inteiro usa.

O que o Obsidian **não** dá sozinho é aresta tipada: `[[Xiao2023FreeAL]]` diz
que há ligação, não que tipo de ligação. Duas saídas usadas na prática:

1. **campos inline no estilo Dataview** — `extends:: [[Xiao2023FreeAL]]`;
2. **listas nomeadas no front-matter** — `extends: [Xiao2023FreeAL]`.

Adotamos a (2) como fonte e geramos a (1) na seção `## Relações` para
navegação. Motivo: YAML é parseável por qualquer linguagem sem depender de
plugin; campo inline depende do Dataview estar instalado.

## Identidade

| Coisa | Identificador | Onde aparece |
|---|---|---|
| Obra | **chave BibTeX** (`Rouzegar2024Thesis`) | `pdf/<Chave>.pdf`, `documentos/<Chave>.md`, `fichas/<Chave>.md`, `id:` do nó |
| Entidade (método, dataset, métrica, tarefa, modelo) | termo canônico kebab-case do `_VOCABULARIO.md` | listas do front-matter |
| Nó da tese | nome próprio (`FALCO`, `DRI-SL`, `LCE`) | `falco_relation.target` |
| Claim | `<Chave>#C1` | tabela de claims |

Uma obra tem **uma** chave. Duplicata (mesmo DOI em duas chaves) é erro do
portão 2, e a correção é fundir, nunca conviver.

## Tipos de nó

| Tipo | Origem |
|---|---|
| `Paper` | uma ficha |
| `Method` `Dataset` `Metric` `Task` `Model` | termos canônicos referenciados |
| `Claim` | linha da tabela de claims |
| `ThesisNode` | alvo de `falco_relation` |

## Tipos de aresta

Paper → Paper (dirigidas; a evidência mora na `nota`):

| Aresta | Semântica | Mapeamento pretendido |
|---|---|---|
| `extends` | continua/estende o trabalho | `cito:extends` |
| `compares_with` | compara empiricamente | *(a conferir na CiTO)* |
| `contradicts` | contesta resultado ou tese | `cito:disagreesWith` |
| `builds_on` | fundamento conceitual | `cito:obtainsBackgroundFrom` |

Paper → Entidade:

| Aresta | Semântica | Mapeamento pretendido |
|---|---|---|
| `proposes` | introduz a entidade | *(a conferir)* |
| `uses_methods` | emprega método alheio | `cito:usesMethodIn` |
| `datasets` | usa os dados | `cito:usesDataFrom` |
| `metrics` `models` `tasks` | avalia com / roda em / resolve | *(a conferir)* |

Paper → ThesisNode (`falco_relation.type`): `compara`, `fundamenta`, `motiva`,
`ameaca`, `complementa`. Estas são **do acervo**, não de nenhuma ontologia
externa: descrevem a relação da obra com ESTA tese, e é justamente isso que
uma ontologia genérica não expressa. Ficam num namespace próprio (`falco:`).

Paper → Claim: `asserts`. Claim → localização: `evidences` (seção/tabela/página
no documento convertido).

## Camada formal — o que reusar e o que inventar

Reusar padrão pronto onde ele existe é a diferença entre um grafo que fala com
o mundo e um dialeto particular:

- **SKOS** para o vocabulário controlado: cada termo canônico é um
  `skos:Concept`, com `skos:prefLabel` (o termo canônico) e `skos:altLabel`
  (os sinônimos que o de/para aposentou). Isso dá ao `_VOCABULARIO.md` um
  formato de tesauro, que é literalmente o que ele é.
- **schema.org / `ScholarlyArticle`** ou **FaBiO** para a obra em si (título,
  autores, ano, DOI).
- **CiTO** para as arestas de citação tipada — é a ontologia feita exatamente
  para dizer *por que* um trabalho cita outro.
- **Namespace próprio `falco:`** só para o que é da tese: `falco_relation`,
  os pilares (`P1..P4`) e os nós da tese.

A regra é: **não invente termo onde já existe padrão; não force padrão onde a
semântica é sua.**

## O de/para do vocabulário (dívida herdada)

Os fichamentos legados têm termos fora do vocabulário controlado. A medição do
`revisor2` em 2026-08-22 (`docs/verificacao/divida-vocabulario-medida.txt`, na
tese): **330 ocorrências, 253 termos distintos, em 81 fichas**. O número que
dimensiona o trabalho é **253** — o de/para é sobre termos, não ocorrências.

Formato do de/para, versionado em `vocabulario/de-para.csv`:

```csv
termo_solto,termo_canonico,acao,justificativa
transformer,transformer,manter,ja e canonico apos inclusao
deep-active-learning,aprendizado-ativo-profundo,renomear,traducao consistente com o resto
```

`acao` ∈ `manter | renomear | novo-canonico | descartar`. **`descartar` exige
justificativa**: termo que só aparece uma vez ainda pode ser o certo.

Em SKOS: o canônico vira `skos:prefLabel`; cada termo solto mapeado vira
`skos:altLabel` do mesmo conceito. Nada se perde — o de/para não apaga
história, ele a organiza.

## Como reportar o grafo (o que "reportar" significa aqui)

Três saídas, públicos diferentes:

1. **Navegável** — `grafo/kg.html`, autocontido, para o autor clicar e para a
   banca ver. Um nó abre a ficha; a ficha abre o PDF e o documento convertido.
2. **Consultável** — `grafo/kg.ttl`, para perguntas do tipo "todo paper que
   contradiz X e usa dataset Y", que nenhuma visualização responde.
3. **Auditável** — `grafo/kg.json` + as tabelas de `bibliometria/`, que são o
   artefato ao qual os números da tese resolvem (princípio V: nenhum número
   sem artefato rastreável). Um número no texto tem de cair numa linha desses
   arquivos.

O que **não** é reportar grafo: imagem bonita de bolinhas sem legenda, sem
tipo de aresta e sem contagem. Se a figura não diz quantos nós, quantas
arestas e de que tipos, ela não é evidência — é decoração.
