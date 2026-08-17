---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: verificar a EXISTÊNCIA das 27 chaves clássicas do t2 (lista no aviso 20260817-0052 do revisor1) com evidência por chave; ordem do autor antes de emendar o princípio II; prioridade DEPOIS da Margatina2023 e do saneamento dos 3 PDFs
referencia: aviso 20260817-0052 (lista das 27) · decisão do autor 2026-08-17 · §6 (a lista é do revisor1, a verificação é sua)
criada_em: 2026-08-17T01:50:00Z
---

O autor condicionou a emenda do princípio II a uma verificação real. Política
que ele ditou, chave a chave:

1. **Toda entrada**: confirmar que a obra EXISTE, na fonte (Crossref por
   DOI/título, ACL Anthology, página da editora, registro da revista).
   Inserir o DOI onde existir (lock do bib; o invariante do DOI repetido te
   protege de duplicata). Link resolvível entra na entrada (campo doi/url) —
   é o que a tabela do site expõe para o autor auditar com um clique.
2. **Artigo publicado APÓS 2000**: não basta existir — marcar para
   FICHAMENTO. Se o PDF for aberto (relatórios do Settles, anthology etc.),
   baixe para a_sanear/ e siga a skill; se for fechado, entregue ao
   principal o LINK pronto para o autor baixar (regra do autor: busca
   pronta, ele só clica).
3. **Livro**: achar referência de existência — página da editora, WorldCat/
   ISBN ou Google Books — e registrar o link.
4. **Registro da verificação**: arquivo SEU,
   `fichamentos/verificacoes/classicos-t2.md`, uma linha por chave:
   o que conferiu, onde, link da evidência, veredito
   (existe | não-indexada-declarada | não-encontrada). "Não achei" ≠ "não
   existe" — o vocabulário do veredito separa os dois.

Saída: aviso ao principal com o resumo (quantas existem, quantos DOIs
inseridos, quais artigos pós-2000 entram na fila de fichamento, links para o
autor). Com isso o autor decide a emenda com dados, não com estimativa.

## Resultado (revisor2, 2026-08-17)

VERIFICAÇÃO CONCLUÍDA. Relatório em `fichamentos/verificacoes/classicos-t2.md`,
branch **verificacao/classicos-t2** (@670440f). 26 chaves, cada uma conferida
em fonte primária, com o vocabulário de três vereditos que você definiu.

O PLACAR: **nenhuma obra é inexistente** — 24 `existe` e 2
`nao-indexada-declarada` (Abe1998 e Yan2011, ambas com causa identificada:
anais que nunca receberam DOI, compensadas por PDF oficial ou registro
canônico). Zero `nao-encontrada`.

MAS — e é isto que muda a decisão do autor — **SEIS ENTRADAS ESTÃO ERRADAS**,
três delas gravemente:

1. `Krause2014` tem TRÊS CAMPOS INVENTADOS: o livro declarado não existe, os
   editores são de outra obra e a nota aponta um terceiro livro. É o MESMO
   padrão que o parecer R6 achou nas entradas recentes — numa clássica de
   2014. O real: capítulo de "Tractability", CUP, pp. 71-104.
2. `Baum1992` inverte a autoria (a literatura inteira cita "Lang e Baum") e
   erra as páginas (335-340, não 1386-1391).
3. `Hanneke2015` erra o ANO: a obra é de 2014. A chave carrega o erro no nome.
4. `Zhu2009` é LIVRO declarado como artigo; `Attenberg2010` é anais declarado
   como periódico — os dois sairiam formatados errado na lista final.
5. `McCallum1998` tem o TÍTULO TROCADO: "Employing EM IN..." quando o correto
   é "Employing EM AND Pool-Based Active Learning", confirmado no PostScript
   do próprio McCallum.

EU ESTAVA ERRADO, E REGISTRO ISSO COM DESTAQUE. Fui eu quem propôs dispensar
as clássicas por serem de "risco baixo". Os dados dizem o contrário: a idade
da obra não prediz a qualidade da entrada. O que prediz é se alguém já
conferiu aquela entrada — no lote A, a única que já declarava DOI foi também
a única sem nenhuma divergência.

RECOMENDAÇÃO REVISADA, para o autor decidir: separar as duas coisas que eu
havia juntado. Clássico dispensa FICHAMENTO (ler 700 páginas para sustentar
uma definição continua desproporcional); NENHUMA entrada dispensa
VERIFICAÇÃO de existência e metadados, que é barata e foi o que achou os seis
erros. E o vocabulário de três vereditos entra na regra, porque exigir DOI de
forma dura reprovaria Abe1998 e Yan2011, que são legítimas e nunca terão
identificador.

PARA O REVISOR1 (o lock do bib é dele, não meu) — 13 DOIs conferidos e prontos
para colar, listados no relatório. DOIS AVISOS: (a) NÃO inserir o DOI do
`Golovin2011` — o que o próprio JAIR declara está MORTO (404 no doi.org e na
Crossref); usar a URL do JAIR, que abre; (b) as correções do Krause2014,
Baum1992, Hanneke2015 e McCallum1998 são de conteúdo, não de formato.

PARA O AUTOR, links prontos de PDF aberto (regra "busca pronta, ele só
clica"): Nguyen2004 (repositório CWI), Guestrin2005 (CMU, licença aberta),
Dasgupta2008 (site dos anais), Settles2008 (ACL Anthology), Golovin2011
(JAIR e arXiv), Yan2011 (icml.cc), Krause2014 (cópia dos autores na ETH),
Muslea2000 (AAAI), Tong2000 e Roy2001 (páginas dos autores). Fechados:
Melville2004, Zhu2009, Attenberg2010 e Hanneke2015 — para esses o autor
precisa de acesso institucional.

DUAS DECISÕES EDITORIAIS que aparecem de brinde: `Tong2000` existe em duas
versões (ICML 2000, declarada, e JMLR 2001, mais citada) e `Guestrin2005` tem
versão estendida de 2008 com ordem de autores invertida. Se o capítulo cita
resultado específico, é preciso escolher.

CONTAGEM: você e o revisor1 falaram em 27; derivando do texto contei 26
anteriores a 2015 (a 27ª seria a Hanneke, que é de 2015 — e que, ironicamente,
a verificação mostrou ser de 2014, o que a coloca dentro do corte de qualquer
forma). Diferença de critério, não de fato.
