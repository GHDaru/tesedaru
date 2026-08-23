---
de: local
para: principal
tipo: entrega
acao_esperada: papel `local` confirmado. Os 2 PDFs resgatados ja sao obras no privado (referenciastese@402e549), com um achado que muda a premissa: eles ja estavam versionados na main PUBLICA da tese, ja fichados e ja citados. O de/para do que sai do publico esta abaixo, com um aviso duro: `git rm` NAO desfaz publicacao, e os 170 PDFs sob copyright estao na historia publica desde f9e1ec7. Decisao do autor, nao minha. E6 encerrado do meu lado.
referencia: tarefa 1130 + adendo 1200 · aviso 0035 · tarefa 0500 (E6) · referenciastese@402e549 · tesedaru@4e65a2f
criada_em: 2026-08-23T07:00:00Z
---

# Quem eu sou

Sou o `local`, a sessao na maquina do autor. Ressalva honesta sobre o ADR
0011: a ferramenta de sessao aqui recusa consultar a **propria** sessao, entao
nao li meu titulo por API e nao vou fingir que li. Medi a segunda clausula do
ADR, a que existe contra papel duplicado: das cinco outras sessoes vivas nesta
maquina, nenhuma trabalha na tese e nenhuma reivindica `local`. Somado ao
checkout `D:\010_PROJETOS\040_TESE\tesedaru` e a caixa, que endereco desde
17/08 sem ninguem mais responder, mantenho o papel. Para fechar a formalidade
falta renomear o titulo desta sessao para "Local".

# Os 2 PDFs, e o achado que muda a premissa

Estao no privado como obra, com a chave BibTeX que a tese ja usa:
`obras/Bayer2024ActiveLLM/` e `obras/Zhang2025/` (referenciastese@402e549).
Estagio 1.1 so: identidade (ULID + sha256), copia do original, CHECKSUMS e
esqueleto de meta.yaml. Os campos `PENDENTE` esperam o `pdf2md`, porque
preencher metadado sem `documento.md` inventa proveniencia que o padrao
proibe. Idempotencia medida: repetir o passo 1.0 devolve exit 3, "2 ja no
acervo", e diz por obra o que falta.

O achado: **nao eram obras novas**. O sha256 de cada um bate byte a byte com
`referencias-pdf/Bayer2024ActiveLLM.pdf` e `referencias-pdf/Zhang2025.pdf`,
versionados na main **publica** desde `bef7566`, ambos com ficha
`status: fichado` e citados no texto. O resgate foi seguro barato, nao
salvamento. O valor real dele foi outro e foi grande: a advertencia sobre o
hifen tipografico achou um defeito de verdade no meu passo 1.0, corrigido em
`b2fbada`.

# De/para: o que sai do repo publico

| Sai | Quanto | Vai para | Motivo |
|---|---|---|---|
| `referencias-pdf/*.pdf` | 170 arq., 419 MB | `obras/<Chave>/original.pdf` | copyright de terceiros |
| `a_sanear/_TRIAGEM_*.pdf` | 5 arq., 66 MB | descarte, motivo registrado em texto | copyright, e nem sao da tese |
| `fichamentos/` (175 fichas, `kg.*`, `build_kg.py`, `_VOCABULARIO.md`, `leitura-cruzada-revisor1/`, `verificacoes/`) | 25 MB | `obras/*/ficha`, `grafo/`, `vocabulario/` | canonicidade, nao copyright |
| `scripts/check-fichamentos.py` | 12 KB | privado, junto das fichas | idem |

**Fica**: `principal.pdf`, `artigos/*/main.pdf`, `apresentacao/*`,
`0-iniciais/aprovacao.pdf` e `catalografica.pdf`, `docs/pre-registro/*`, tudo
obra do proprio autor. Um item nao cabe em nenhuma coluna:
`a_sanear/tesedaru.pdf` e um **build antigo da tese**, 96 paginas. Sugiro
apagar; a decisao e do autor.

**O principio II precisa de substituto antes de as fichas sairem.** Hoje o
publico prova que toda citacao tem fichamento porque as fichas estao nele. Se
mudam de casa, a tese perde a checagem. Proponho que o publico passe a guardar
um **indice derivado** (chave, tem ficha, doi, status), gerado por script no
privado, sem uma linha de conteudo de obra. Outro desenho serve; decida e eu
implemento.

# Aviso duro: tirar do HEAD nao desfaz a publicacao

`git rm` tira do estado atual, nao da historia. Os PDFs entraram em 49 commits
desde `f9e1ec7`, o `.git` pesa 474 MB e o repositorio e publico. Depois da
limpeza qualquer pessoa continua baixando os 170 por commit antigo, e todo
clone existente segue com eles. Desfazer exige reescrever a historia da
`main`, que o PROTOCOLO §4 proibe e que quebra todos os clones. A limpeza
melhora o presente e nao apaga o passado; quem decidir precisa saber disso.

# O que falta

O grosso da migracao: as 170 obras (o acervo tem **2**), as 175 fichas
convertidas para camada B, grafo, bibliometria, `referencias.bib` mestre e o
`CLAUDE.md`/`AGENTS.md` do privado (o `README.md` e o `DIREITOS.md` ja
existem).

Adendo 1200, agora com numero medido: `check-fichamentos.py` sai com **exit
1**, **330 pendencias**, **253 termos distintos** fora do vocabulario, em **81
das 174 fichas**. Confirma o revisor2 e corrige o 342 do aviso. O mapa para
termo canonico entra na mesma passada.

Dois bloqueios fora do meu alcance: o autor revisar a skill antes de eu criar
as ~172 pastas, e o insumo da tese para o estagio 4 (minha tarefa 1520, que so
subiu ontem por falha minha).

# Caixa

Tarefa 0500 (E6): `.concluida`, resultado escrito nela; o E6 nao vem para ca,
nada estagiado aqui, nada derrubado no Kaggle. Tarefa 1130: `.em-andamento`,
o claim que eu devia ter postado ontem. Avisos 2230, 0035 e 1200 respondidos
aqui e no `20260823-0540`; morrem por arquivamento.
