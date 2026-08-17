# Verificação de existência — obras clássicas citadas no tema t2 do Capítulo 2

**Data:** 2026-08-17 · **Executor:** revisor2 · **Tarefa:** 20260817-0150 (ordem
do autor, anterior à decisão de emendar o princípio II) · **Escopo:** chaves
citadas em `2-fundam/texto.tex` linhas 210–471 que ainda não têm fichamento e
são anteriores a 2015.

## Como ler esta página

O autor pediu para separar três situações que costumam ser confundidas:

| Veredito | O que significa |
|---|---|
| `existe` | A obra foi localizada em fonte primária e há identificador resolvível (DOI ou registro de anais). |
| `nao-indexada-declarada` | A obra é real e há evidência bibliográfica, mas **não existe DOI** — situação normal em anais antigos que nunca foram digitalizados por artigo. Não é defeito da entrada; é propriedade da obra. |
| `nao-encontrada` | Não foi possível localizar a obra. **Não equivale a "não existe"**: significa que a busca falhou e o caso precisa de outra rodada ou da biblioteca. |

Nota de contagem, registrada sem alarde: o aviso do revisor1 fala em 27 chaves
clássicas; derivando do próprio texto, contei 26 anteriores a 2015 (mais a
`Hanneke2015`, que é de 2015 e entra ou não conforme o critério de corte). É
divergência de recorte, não de fato — a mesma classe de diferença que ele
mesmo apontou entre "ocorrências" e "chaves distintas".

## Lote A — fundamentos e comitês (1948–1998)

| Chave | Veredito | Identificador verificado | Fonte consultada | Divergência contra o `.bib` |
|---|---|---|---|---|
| `Shannon1948` | existe | `10.1002/j.1538-7305.1948.tb01338.x` | Crossref por DOI | DOI ausente na entrada; nome do periódico com artigo ("The Bell System…") na entrada, sem artigo na fonte; **o artigo saiu em duas partes** (jul. e out. 1948) e a entrada cobre só a primeira |
| `Mitchell1982` | existe | `10.1016/0004-3702(82)90040-6` | Crossref por DOI | **Nenhuma** — única entrada do lote plenamente conforme, e a única que já declarava DOI |
| `MacKay1992` | existe | `10.1162/neco.1992.4.4.590` | Crossref por título+autor | Só a ausência do DOI |
| `Seung1992` | existe | `10.1145/130385.130417` | Crossref por DOI | DOI ausente; caixa do título (ACM registra em caixa baixa); nomes expandidos na entrada, iniciais na fonte — expansão correta, mas não vem da fonte |
| `Lewis1994heterogeneous` | existe | `10.1016/B978-1-55860-335-6.50026-X` | Crossref por DOI + DBLP para editores | Só a ausência do DOI; editores e ISBN conferem |
| `Dagan1995` | existe | `10.1016/B978-1-55860-377-6.50027-X` | Crossref por DOI + DBLP | **A mais problemática do lote**: nomes truncados a iniciais; `~` dentro do campo `author`, que atrapalha a separação de prenome/sobrenome pelo BibTeX; faltam `publisher` e `editor`; DOI ausente |
| `Freund1997` | existe | `10.1023/A:1007330508534` | Crossref por DOI | Só a ausência do DOI |
| `Abe1998` | **nao-indexada-declarada** | registro DBLP `conf/icml/AbeM98` | Crossref (sem casamento) → DBLP | **Nenhuma divergência**: todos os campos conferem. A obra simplesmente não tem DOI — os anais ICML de 1998 (Morgan Kaufmann) nunca foram digitalizados por artigo |
| `Blum1998` | existe | `10.1145/279943.279962` | Crossref por DOI | DOI ausente; caixa do título; **o mesmo autor aparece grafado de duas formas no arquivo** ("Mitchell, Tom M." em `Mitchell1982`, "Tom Mitchell" aqui) |

Nenhuma obra deste lote é posterior a 2000, então nenhuma entra na fila de
fichamento pela regra do item 2 da tarefa.

## Lote B — seleção clássica e anos 2000

| Chave | Veredito | Identificador verificado | Fonte consultada | Divergência contra o `.bib` |
|---|---|---|---|---|
| `McCallum1998` | existe (sem DOI) | registro DBLP `conf/icml/McCallumN98` | DBLP + **PostScript original do autor** (`cs.cmu.edu/~mccallum/papers/emactive-icml98.ps.gz`, primeira página lida) | **TÍTULO ERRADO**: a entrada diz "Employing EM **in** Pool-Based…"; o título real é "Employing EM **and** Pool-Based Active Learning for Text Classification". Faltam o coautor Kamal Nigam e as páginas 350–358 |
| `Muslea2000` | existe (sem DOI) | PDF oficial AAAI `AAAI00-095.pdf` | DBLP + AAAI (PDF aberto) | Nenhuma no título/ano; conferir se os três autores (Muslea, Minton, Knoblock) e a venue AAAI estão declarados |
| `Tong2000` | existe (sem DOI) | DBLP `conf/icml/TongK00` (ICML 2000, pp. 999–1006) | DBLP + PDF do autor em Stanford (aberto) | **DECISÃO EDITORIAL**: existem duas versões — ICML 2000 (a declarada, correta) e a de periódico, JMLR 2:45–66 (2001), que é a mais citada. Se o capítulo cita seção ou resultado específico, é preciso saber qual |
| `Roy2001` | existe (sem DOI) | registro DBLP `conf/icml/RoyM01` | DBLP + PostScript original do McCallum (primeira página lida) | Nenhuma; faltam só as páginas 441–448 |
| `Melville2004` | existe | `10.1145/1015330.1015385` | Crossref por DOI | Nenhuma de substância; confirmar o coautor Raymond J. Mooney |
| `Nguyen2004` | existe | `10.1145/1015330.1015349` | Crossref por DOI | Nenhuma; atenção à grafia completa dos nomes |
| `Guestrin2005` | existe | `10.1145/1102351.1102385` | Crossref por DOI | Nenhuma na forma declarada. **Armadilha registrada**: existe versão estendida em periódico (JMLR 9:235–284, 2008) com subtítulo e **ordem de autores invertida** — a chave `Guestrin2005` só serve para a versão dos anais |
| `Dasgupta2008` | existe | `10.1145/1390156.1390183` | Crossref por DOI + PDF oficial dos anais | Nenhuma; confirmar o coautor Daniel Hsu |
| `Settles2008` | existe (sem DOI) | ACL Anthology `D08-1112` | BibTeX oficial da ACL Anthology + DBLP | Nenhuma. **Desambiguação confirmada**: é o artigo do EMNLP 2008 com Mark Craven (pp. 1070–1079), e não o "Active Learning Literature Survey", que é obra distinta |

**PDFs abertos, prontos para o autor clicar** (regra do item 2 da tarefa — só
os posteriores a 2000): Nguyen2004 via repositório CWI; Guestrin2005 no
repositório da CMU, com licença aberta; Dasgupta2008 no site oficial dos anais;
Settles2008 direto na ACL Anthology. **Fechado:** apenas `Melville2004` — e
aqui vale a distinção que o autor pediu: o veredito é "não localizei espelho
aberto em quatro fontes", não "não existe espelho aberto". A existência da obra
está provada de forma independente pelo DOI.

## Lote C — livros, periódicos e submodularidade

Este é o lote que muda a conclusão. Seis das oito entradas têm erro
bibliográfico, e três são graves.

| Chave | Veredito | Identificador verificado | Fonte consultada | Divergência contra o `.bib` |
|---|---|---|---|---|
| `Krause2014` | existe | `10.1017/CBO9781139177801.004` | Crossref (capítulo e livro) + Cambridge Core | **A PIOR DO CONJUNTO — três campos inventados**: o `booktitle` declarado ("Tracts in Machine Learning") NÃO EXISTE; os editores declarados são de OUTRO livro; a `note` cita um terceiro livro que não contém o capítulo. O real: capítulo de *Tractability: Practical Approaches to Hard Problems*, CUP 2014, pp. 71–104, editores Bordeaux, Hamadi e Kohli. Tipo também errado |
| `Baum1992` | nao-indexada-declarada | registro em duas bibliografias revisadas por pares | Crossref (sem cobertura de IJCNN 1992) → survey do Settles + anais IJCAI 2020 | **Autoria INVERTIDA** (o correto é Lang e Baum, não Baum e Lang — a literatura inteira cita "Lang e Baum") e **páginas erradas** (335–340, não 1386–1391). A chave `Baum1992` está mal escolhida |
| `Hanneke2015` | existe | `10.1561/2200000037` | Crossref por DOI | **ANO ERRADO**: a obra é de **2014**, não 2015. Muda a citação no texto e desalinha a chave |
| `Zhu2009` | existe | `10.2200/S00196ED1V01Y200906AIM006` | Crossref (tipo `book`) + DBLP | **É LIVRO, está declarado como artigo** — sairia formatado como artigo de periódico. Volume e número são da série, não de periódico. Bônus: o título contém um hífen não-ASCII (U+2011) que quebra busca |
| `Attenberg2010` | existe | `10.1145/1835804.1835859` (confere) | Crossref por DOI + DBLP | Tipo errado: anais declarados como periódico. O DOI está **correto** |
| `Golovin2011` | existe | — (ver observação) | Crossref + página do JAIR | **O DOI que o próprio JAIR declara está MORTO** (404 no doi.org e na Crossref). Não inserir esse DOI: um parecerista o leria como fabricado. Usar a URL do JAIR, que abre |
| `Yan2011` | nao-indexada-declarada | PDF oficial no servidor do ICML | DBLP + icml.cc (HTTP 200) | Sem DOI, o que é normal para o ICML de 2011 (anais Omnipress, anteriores ao PMLR). Só o `booktitle` está abreviado |
| `Cohn1996` | existe | `10.1613/jair.295` | Crossref por DOI | **Nenhuma** — só falta declarar o DOI. Periódico aberto |

## Leitura para a decisão sobre o princípio II

**O resultado contraria a hipótese com que eu mesmo abri esta verificação.**
Eu havia sugerido ao autor que obras clássicas fossem dispensadas de
verificação por serem de baixo risco. Os dados dizem outra coisa.

Das 26 chaves, **nenhuma obra é inexistente** — nesse ponto a suspeita de
fabricação em massa não se confirma. Mas **as entradas em si estão longe de
limpas**, e o erro se concentra justamente onde eu previa risco baixo:

- `Krause2014` tem **conteúdo inventado** em três campos. Não é descuido de
  transcrição: é um livro que não existe, editores de outra obra e uma nota
  que aponta para um terceiro livro. É exatamente o padrão que o parecer R6
  descreveu para as entradas recentes — só que numa clássica.
- `Baum1992` inverte a autoria e erra as páginas.
- `Hanneke2015` erra o ano, e a chave carrega o erro no nome.
- `Zhu2009` e `Attenberg2010` declaram o tipo errado, o que produz
  formatação errada na lista final de referências.
- `McCallum1998` (lote B) tem o **título trocado**: "EM *in*" onde o correto
  é "EM *and*".

Ou seja: **a idade da obra não prediz a qualidade da entrada.** O que prediz
é se alguém já conferiu aquela entrada contra a fonte — e a evidência disso
está no lote A, onde a única entrada que já declarava DOI (`Mitchell1982`) foi
também a única sem nenhuma divergência.

### Recomendação revisada

Mantenho a ideia de não exigir **fichamento** de obra clássica citada apenas
para definição consagrada: ler 700 páginas de livro-texto para sustentar uma
definição continua desproporcional. Mas separo o que antes eu havia juntado:

1. **Fichamento** (ler a obra e registrar claims com evidência): dispensável
   para a referência canônica.
2. **Verificação de existência e de metadados** (título, autoria, ano, venue,
   identificador): **obrigatória para toda entrada, sem exceção de idade**.
   Foi ela que achou os cinco erros acima, e é barata — a maior parte se
   resolve com uma consulta à Crossref.

A regra que proponho ao autor, portanto, não é "clássico dispensa conferência",
e sim **"clássico dispensa fichamento, mas nenhuma entrada dispensa
verificação"** — com o vocabulário de três vereditos incorporado, porque
`Abe1998` e `Yan2011` provam que exigir DOI de forma dura reprovaria obras
legítimas que nunca terão identificador.
