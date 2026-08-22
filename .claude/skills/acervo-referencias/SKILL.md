---
name: acervo-referencias
description: Pipeline completo de acervo bibliográfico — converte cada PDF em markdown integral (figuras viram texto), extrai e valida metadados, gera fichamento com resumo e elementos para a tese, e só no fim monta as referências cruzadas e o grafo de conhecimento. Use quando houver PDFs novos a processar, quando um fichamento precisar ser refeito a partir do PDF, ou quando o grafo do acervo precisar ser regenerado.
---

# Acervo de referências — pipeline de 5 estágios

## Iron Law

**Nada entra no acervo sem sair do PDF.** Todo campo de metadado, todo número,
toda descrição de figura e todo claim tem de ser localizável no documento
convertido (página/seção). Não existe "sei de cor", não existe "provavelmente
é". Campo que o PDF não sustenta fica `null` com o motivo — nunca preenchido
por inferência.

Corolário operacional: **o estágio N não começa sem o portão do estágio N-1
verde**, e cada portão é um script que devolve exit 0 ou lista o que falta.
Julgamento não é portão; checagem é.

## Relação com a skill `fichamento` (que já existe)

A skill `fichamento` cobre **um artigo avulso**: PDF em `a_sanear/` → chave →
ficha → commit, dentro do repositório da tese. Ela continua válida para esse
caso e é a origem do template e do vocabulário usados aqui.

Esta skill é o **acervo inteiro em regime de produção**, e acrescenta o que a
outra não tem: a conversão integral do PDF em markdown (com as figuras viradas
texto), portões executáveis entre estágios, estado retomável para ~180 obras, e
o fecho do grafo feito uma única vez no fim, com o acervo completo.

Qual usar: um artigo novo chegando avulso → `fichamento`. Processar a fila, ou
refazer uma ficha a partir do PDF → esta.

## Antes de começar

1. Leia `references/padrao-grafo.md` — é o padrão semântico do acervo
   (identidade, arestas tipadas, projeções). Ele governa os estágios 2 e 5.
2. Leia `references/conversao-pdf.md` antes do estágio 1 e
   `references/metadados.md` antes do estágio 2.
3. Defina a raiz do acervo. Todos os caminhos deste documento são relativos a
   ela:

```bash
export ACERVO=/caminho/para/o/clone/de/referenciastese
```

A tese (`tesedaru`) é repositório **separado e público**. Esta skill escreve
**apenas** dentro de `$ACERVO`. Se você se pegar editando `principal.tex`, o
`referencias.bib` da tese ou qualquer `N-*/texto.tex`, pare: não é sua
superfície.

## Layout do acervo

```
$ACERVO/
  referencias.bib             # BIB MESTRE — fonte da identidade
  _entrada/                   # fila: PDFs ainda não processados
  pdf/<Chave>.pdf             # acervo, um arquivo por chave BibTeX
  documentos/<Chave>.md       # texto INTEGRAL convertido (estágio 1)
  documentos/figuras/<Chave>/ # imagens extraídas, descritas em texto no .md
  fichas/<Chave>.md           # fichamento (estágios 2-4)
  vocabulario/_VOCABULARIO.md # vocabulário controlado
  grafo/                      # kg.json · kg.ttl · kg.html (estágio 5)
  bibliometria/               # tabelas e relatório (estágio 5)
  scripts/                    # os scripts abaixo, versionados
  _estado/pipeline.jsonl      # estado por chave — o que permite retomar
```

`<Chave>` é **sempre** a chave BibTeX (ex.: `Rouzegar2024Thesis`). Ela é a
identidade única: nome do PDF, nome do documento, nome da ficha, id do nó no
grafo. Um item com duas chaves é um bug, não uma variante.

## O laço

Os estágios **1 a 4 rodam por artigo**, um artigo de cada vez até o fim.
O estágio **5 roda uma única vez, no final**, quando todas as fichas existem —
ele é o único que precisa ver o acervo inteiro.

```
para cada PDF em _entrada/:
    1. converter  → documentos/<Chave>.md  (+ figuras descritas)
    2. metadados  → front-matter validado contra o PDF + entrada na bib
    3. resumo     → resumo, claims com evidência, números citáveis
    4. citações   → onde isto entra na tese   [depende do estágio 4-pré]
depois de TODOS:
    5. grafo      → referências cruzadas, kg.json/ttl/html, bibliometria
```

### Retomada

Antes de processar uma chave, consulte `_estado/pipeline.jsonl`:

```bash
uv run --with pyyaml python "$ACERVO/scripts/estado.py" proximo
```

Ele devolve a próxima chave pendente e em que estágio ela parou. Ao concluir
um estágio, registre:

```bash
uv run --with pyyaml python "$ACERVO/scripts/estado.py" marcar <Chave> <estagio> ok
```

O estado é a razão de o laço poder ser interrompido e retomado por outro
agente sem refazer trabalho. **Não mantenha o progresso na sua cabeça** — a
sessão acaba, o arquivo não.

---

## Estágio 1 — Converter o PDF inteiro em markdown

**Objetivo**: `documentos/<Chave>.md` contém o documento **inteiro** em texto:
corpo, tabelas e — este é o ponto que costuma ser pulado — **as figuras
transformadas em texto**.

```bash
uv run --with pymupdf python "$ACERVO/scripts/pdf2md.py" \
    --pdf "$ACERVO/pdf/<Chave>.pdf" --chave <Chave> --acervo "$ACERVO"
```

O script produz o texto com marcas de página (`<!-- p.7 -->`), converte as
tabelas que consegue detectar, exporta cada figura para
`documentos/figuras/<Chave>/p07-fig01.png` e deixa **no lugar da figura** um
bloco marcado:

```markdown
![](figuras/Chave/p07-fig01.png)
> **FIG-01 (p.7) — DESCRICAO PENDENTE**
```

**O script não descreve figura — quem descreve é você.** Abra cada PNG
exportado, olhe, e substitua a linha `DESCRICAO PENDENTE` por uma descrição
factual: o que o gráfico plota, o que está em cada eixo, quais séries, e os
valores que dá para ler. Se a figura for decorativa (logo, selo), escreva
`decorativa — sem conteúdo técnico`. Regras em `references/conversao-pdf.md`.

**Portão 1** (tem de sair exit 0 antes do estágio 2):

```bash
uv run --with pymupdf --with pyyaml python "$ACERVO/scripts/gate.py" 1 <Chave>
```

Ele checa: o `.md` existe; a contagem de páginas do `.md` bate com a do PDF;
não sobrou nenhuma `DESCRICAO PENDENTE`; toda imagem exportada é referenciada
no `.md`; e a densidade de texto não é absurdamente baixa (PDF só-imagem, que
precisa de OCR — o portão avisa em vez de deixar passar um documento vazio).

---

## Estágio 2 — Metadados: extrair, validar, gravar

Leia `references/metadados.md`. Preencha o front-matter da ficha a partir do
`documentos/<Chave>.md`, **não** do PDF binário e **não** de memória.

1. Copie `templates/ficha.md` para `fichas/<Chave>.md`.
2. Preencha identidade (`title`, `authors`, `year`, `venue`, `doi`) lendo a
   primeira página do documento convertido. Cada campo carrega a página de
   onde veio, no bloco `_fonte`.
3. DOI: se o documento não traz DOI, o campo fica `null` — não invente e não
   busque na web sem o autor pedir.
4. Garanta a entrada em `referencias.bib` com a mesma chave. Divergência entre
   a bib e a ficha é erro do estágio 2, não do estágio 5.
5. Entidades (`proposes`, `uses_methods`, `datasets`, `metrics`, `tasks`,
   `models`): **só nomes canônicos** do `vocabulario/_VOCABULARIO.md`. Faltou
   termo? Acrescente ao vocabulário no MESMO commit, com o comentário
   `<!-- Chave -->` dizendo quem o introduziu. Nunca use termo livre.

**Portão 2**:

```bash
uv run --with pyyaml python "$ACERVO/scripts/gate.py" 2 <Chave>
```

Checa: front-matter YAML parseia; `id` = nome do arquivo; campos obrigatórios
presentes ou `null` justificado; chave existe na bib; `pdf:` aponta para
arquivo que existe; todo termo de entidade está no vocabulário; DOI não
duplica o de outra ficha.

---

## Estágio 3 — Resumo e o que a tese pode usar

Ainda por artigo, ainda a partir do documento convertido.

- **Resumo** (5–8 linhas, palavras suas): o problema, o que o trabalho faz, o
  resultado principal e a condição em que ele vale. Resumo que serve para
  qualquer paper não serve para nenhum.
- **Claims**, na tabela: cada um com **evidência localizável** (`§4.2`,
  `Tab. 3`, `p. 7`). Claim sem localização não entra — apague a linha.
- **Números citáveis**: valor exato **com as condições** (dataset, métrica,
  orçamento, semente). Número sem condição é número inútil e vira erro na tese
  (princípio V da constituição: nenhum número sem artefato rastreável).
- **Crítica/limitações**: sua leitura, marcada como sua.

**Portão 3**:

```bash
uv run --with pyyaml python "$ACERVO/scripts/gate.py" 3 <Chave>
```

Checa: resumo entre 5 e 8 linhas e não copiado do abstract (sobreposição de
n-gramas acima do limite reprova); toda linha da tabela de claims tem
evidência preenchida; toda linha de número tem condição.

---

## Estágio 4 — Citações para a tese

Este estágio **depende de insumo externo**: o conteúdo atual da tese. Sem ele,
"onde isto entra na tese" vira chute.

**Pré-requisito (estágio 4-pré, uma vez por rodada, não por artigo):** peça ao
agente `principal` — pelo protocolo da caixa, nunca direto ao autor — o
recorte vigente da tese: sumário com seções, o `referencias.bib` da tese e o
mapa de quais chaves já são citadas em qual capítulo. Deposite em
`$ACERVO/_insumos/tese/`. Enquanto esse insumo não existir, **pule o estágio 4
e siga o laço** — a ficha fica com `status: aguarda-tese` e o pipeline não
para (PROTOCOLO §3: postado o bloqueio, pegue o próximo item).

Com o insumo na mão, para cada ficha preencha:

- `falco_relation`: tipo (`compara | fundamenta | motiva | ameaca |
  complementa`), alvo (nó da tese: `FALCO`, `DRI-SL`, `LCE`, ...) e nota.
  **É obrigatório**: se o artigo não toca a tese, ele não precisava ser
  fichado — registre isso explicitamente em vez de forçar uma relação.
- Coluna "Uso na tese" de cada claim: capítulo/seção concretos.
- `cited_in`: capítulos que já citam a chave (vem do insumo, não do seu
  palpite).

**Portão 4**:

```bash
uv run --with pyyaml python "$ACERVO/scripts/gate.py" 4 <Chave>
```

Checa: `falco_relation` não vazia; alvos existem na lista de nós da tese;
seções citadas em "Uso na tese" existem no sumário do insumo.

---

## Estágio 5 — Referências cruzadas e grafo (uma vez, no fim)

Só rode quando **todas** as chaves estiverem com os portões 1–3 verdes. Este
estágio é o único que lê o acervo inteiro de uma vez, porque é o único que
pode: aresta entre dois papers só existe quando os dois estão fichados.

```bash
uv run --with pyyaml python "$ACERVO/scripts/build_kg.py"     --acervo "$ACERVO"
uv run --with pyyaml python "$ACERVO/scripts/bibliometria.py" --acervo "$ACERVO"
```

1. **Referências cruzadas**: com todos os resumos carregados, resolva
   `extends`, `compares_with`, `contradicts` e `builds_on`. Aresta é
   **dirigida e tipada**, e só vale se o texto do artigo de origem a sustenta
   — a evidência vai no campo `nota` da aresta. Aresta apontando para chave
   inexistente é erro, não "referência externa".
2. **Grafo**: gera as três projeções descritas em `references/padrao-grafo.md`
   — wikilinks Obsidian (navegação humana), `kg.json` (a interface) e
   `kg.ttl` (consulta formal).
3. **Bibliometria**: cobertura (chaves citadas × fichadas), autoria,
   distribuição por ano/veículo, DOIs, e o mapa chave × capítulo.
   **Toda contagem sai de script**, nunca digitada.

**Portão 5**:

```bash
uv run --with pyyaml python "$ACERVO/scripts/gate.py" 5
```

Checa: nenhuma aresta órfã; nenhum DOI repetido; nenhuma chave sem PDF **nem**
justificativa de referência canônica (ADR 0012: livro ou obra anterior a 2010
citada por definição consagrada é dispensada do fichamento integral); nenhum nó
isolado sem justificativa; e os números da bibliometria batem com os arquivos.

---

## Erros que este pipeline existe para impedir

- **Descrever figura sem olhar.** É o atalho mais tentador do estágio 1 e o
  mais caro: uma figura mal descrita vira número errado na tese três meses
  depois. Se a imagem não abriu, escreva `ilegível` — é resposta honesta.
- **Resumo colado do abstract.** O portão 3 reprova por sobreposição, mas o
  motivo é outro: resumo copiado prova que ninguém leu.
- **Termo livre no vocabulário.** Cada termo solto é uma aresta que o grafo não
  vai fechar. Canonize na hora, não "depois".
- **Fechar o grafo com o acervo pela metade.** As arestas mudam quando entra
  artigo novo; grafo gerado cedo é grafo que mente.
- **Trabalhar sem registrar estado.** Outro agente vai continuar isto. O
  `_estado/pipeline.jsonl` é o único lugar onde o progresso é real.
