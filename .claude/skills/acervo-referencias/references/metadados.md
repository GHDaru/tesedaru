# Estágio 2 — metadados: o schema e as regras

## Princípio

Metadado é **transcrição**, não pesquisa. Tudo o que entra no front-matter foi
lido no documento convertido, e o bloco `_fonte` diz em que página. Se o campo
não está no documento, ele é `null` com motivo. "Achei na internet" só entra
se o autor pedir, e aí o `_fonte` registra a origem externa.

## Schema

### Identidade — obrigatório

| Campo | Tipo | Regra |
|---|---|---|
| `id` | string | = chave BibTeX = nome do arquivo, sem `.md` |
| `title` | string | como impresso; sem reescrever caixa |
| `authors` | lista | `"Sobrenome, Nome"`, na ordem do artigo. Todos — sem `et al.` |
| `year` | int | ano da publicação transcrita; preprint usa o ano do preprint |
| `venue` | string\|null | periódico, conferência ou `arXiv` |
| `doi` | string\|null | só o sufixo `10.xxxx/...`, sem `https://doi.org/` |
| `pdf` | caminho | `pdf/<Chave>.pdf`, tem de existir |
| `paginas` | int | do documento convertido |
| `idioma` | string | `pt` \| `en` \| ... |

### Classificação

| Campo | Valores |
|---|---|
| `paper_type` | `metodo` \| `survey` \| `dataset` \| `avaliacao` \| `posicao` \| `livro` \| `tese` |
| `pillars` | `P1`..`P4`, `LCE`, `geral` |
| `status` | `a-ler` \| `convertido` \| `metadados` \| `resumido` \| `aguarda-tese` \| `fichado` |
| `canonica` | bool — ADR 0012: livro ou obra pré-2010 citada por definição consagrada |

`canonica: true` **dispensa o fichamento integral**, mas não dispensa a entrada
bibliográfica correta nem a ficha mínima de uma linha dizendo qual resultado da
obra a tese usa e onde. Se a tese passar a depender do conteúdo específico da
obra (não só da sua existência), ela volta à regra cheia — `canonica: false`.

### Entidades — só termos canônicos

`proposes`, `uses_methods`, `datasets`, `metrics`, `tasks`, `models`.

Regra única e sem exceção: **todo item existe no `_VOCABULARIO.md`**. Faltou?
Duas saídas legítimas, nenhuma delas é "escrevo assim mesmo":

1. o conceito já existe com outro nome → use o canônico;
2. o conceito é novo → acrescente ao vocabulário **no mesmo commit da ficha**,
   com `<!-- Chave -->` marcando quem o introduziu.

Distinguir `proposes` de `uses_methods` é o que dá valor ao grafo: quem
inventou versus quem aplicou. Na dúvida, o artigo diz — procure "we propose",
"introduzimos", "our method".

### Relações — preenchidas no estágio 5, declaradas aqui

`extends`, `compares_with`, `contradicts`, `builds_on` nascem `[]` e só se
resolvem quando o acervo inteiro existe. Não tente adivinhar no estágio 2:
aresta para chave que ainda não entrou é aresta órfã.

### `_fonte` — a prova

```yaml
_fonte:
  title: p.1
  authors: p.1
  year: p.1
  venue: "p.1 (rodapé)"
  doi: null   # nao consta no documento
```

Este bloco é o que separa metadado transcrito de metadado inventado. O portão
2 exige uma entrada por campo de identidade preenchido.

## Derivar a chave BibTeX

`SobrenomeDoPrimeiroAutor` + `Ano` + sufixo distintivo quando necessário:

```
Xiao2023FreeAL      Rouzegar2024Thesis      Daru2022
```

- Sobrenome sem acento e sem espaço, em CamelCase (`vanDerMaaten` → `VanDerMaaten`).
- Colisão no mesmo ano → sufixo com o termo distintivo do título, nunca `a`/`b`
  (a letra não diz nada a quem lê a citação).
- **A chave nunca muda depois de criada.** Ela é o identificador em três
  arquivos e em N citações da tese; renomear é uma migração, não uma correção
  de gosto.

## Sincronia com o `referencias.bib`

A bib mestre do acervo é a fonte da entrada bibliográfica. Ao criar a ficha:

1. a chave existe na bib? senão, crie a entrada com os campos transcritos;
2. os campos da bib batem com os da ficha? divergência resolve-se **agora**, e
   quem manda é o documento convertido;
3. DOI já existe em outra entrada? é duplicata — funda as duas chaves antes de
   seguir. Duas chaves para a mesma obra quebram o grafo e a contagem.

## Erros comuns

| Erro | Por que dói |
|---|---|
| `authors: ["Xiao et al."]` | destrói a bibliometria de autoria |
| DOI com URL completa | quebra a deduplicação por igualdade de string |
| `year` do acesso em vez do da publicação | envelhece o acervo inteiro |
| `venue: "IEEE"` | editora não é veículo |
| termo livre "porque é só um" | é sempre "só um", 253 vezes |
