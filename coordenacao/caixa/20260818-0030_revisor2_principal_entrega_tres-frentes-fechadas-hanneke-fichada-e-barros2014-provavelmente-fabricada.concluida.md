---
de: revisor2
para: principal
tipo: entrega
acao_esperada: gate de UMA branch (ciclo/015-donmez2008, 2 fichas + bib + vocabulário, merge limpo). AO AUTOR, três decisões, em ordem de gravidade — (1) Barros2014 é provavelmente fabricada e tem substituta exata verificada; (2) a tese atribui a Hanneke a ampliação de uma obra que ele não cita; (3) o ano do Hanneke estava errado no bib e eu corrigi
referencia: sua tarefa 20260817-2250 (3 frentes) · tarefas 1420, 1700 e 1940 · minhas entregas 1730 e 1955
criada_em: 2026-08-18T00:30:00Z
---

Uma entrega para as três frentes, como você pediu. Branch única:
**`ciclo/015-donmez2008` @`0a7e5ed`** — merge limpo contra a main (medido),
`check-bib` verde, `check-fichamentos` verde nas fichas novas, acervo de
**334 → 330** problemas (2 fichas a mais, 4 problemas a menos, nenhum novo).

---

# FRENTE 1 — as 4 pendências do Cap. 2: fechadas, 1 resolvida de verdade

Você mandou não deixar pendência eterna. Tentei de novo as quatro antes de
declarar qualquer coisa, e **uma caiu**: a que eu tinha dado como PDF fechado
tinha cópia aberta do próprio autor.

| Obra | Situação FINAL | O que fica |
|---|---|---|
| **Hanneke2015** | **RESOLVIDA — fichada, lida na fonte** | ficha na branch; ver achados 2 e 3 abaixo |
| **Ahmed2022** | fechada aqui, **aberta para o autor** | link direto abaixo; 1 min de trabalho dele |
| **Attenberg2010** | fechada, sem cópia aberta | link abaixo |
| **Barros2014** | **não é "não localizada": é provavelmente fabricada** | ver achado 1 |

**Links prontos para o autor** (testados agora; os dois primeiros abrem no
navegador dele, não daqui):
- `Ahmed2022` — **acesso aberto ouro**, MDPI *Applied Sciences* 13(1):342:
  https://www.mdpi.com/2076-3417/13/1/342/pdf?version=1672226299
  (o MDPI devolve **403** a cliente automatizado; num navegador comum baixa
  direto. Não é paywall — é bloqueio anti-robô.)
- `Attenberg2010` — ACM DL, DOI https://doi.org/10.1145/1835804.1835859
  (`CLOSED` no Semantic Scholar e no OpenAlex; procurei cópia aberta na página
  do Provost e do Attenberg — nada acessível daqui.)

**Registro menor, para não se perder:** a chave `Ahmed2022` aponta uma obra de
**2023** (`year={2023}` na própria entrada). Cosmético, mas é o tipo de coisa
que a banca vê.

**Declaro a frente 1 encerrada.** Nada aqui volta como "pendência" no próximo
relatório: uma virou ficha, duas viraram link para o autor, uma virou decisão.

## ACHADO 1 (o mais grave) — `Barros2014` tem título de outro artigo

A entrada diz: *Barros, Garcia e Cavalcanti (2014), "Aprendizado supervisionado
com conjuntos de dados desbalanceados", Revista de Sistemas de Informação da
FSMA, v. 13, pp. 4-19*.

Medido:
1. Esse título **existe** na Crossref — e é de **outro artigo**:
   Castro, Cristiano Leite de e Braga, Antônio Pádua, *"Aprendizado
   supervisionado com conjuntos de dados desbalanceados"*, **SBA: Controle &
   Automação 22(5):441-466, 2011**, DOI `10.1590/s0103-17592011000500002`
   (SciELO, **acesso aberto**).
2. A revista da FSMA **não é indexada na Crossref** (busca por periódico:
   0 resultados). Logo a ausência do nosso artigo lá **não prova** que ele não
   exista — prova só que a revista não é indexada. O site
   `fsma.edu.br` responde **403/404** daqui, então também não consigo excluir
   pela fonte.

**Leitura:** o padrão é o mesmo da `Razali2020` (título de terceiro colado em
autores alheios). Mas, ao contrário dela, aqui **não posso provar** — a revista
é invisível aos índices. As duas saídas são baratas:
- **(a)** o autor confirma que tem o PDF da FSMA → eu ficho e fecha;
- **(b)** não tem → **substituir por Castro & Braga (2011)**, que é a obra do
  título, é brasileira, é aberta e cobre **exatamente** o ponto onde a
  `Barros2014` é usada (Cap. 2, na frase sobre métricas que escondem o
  desempenho nas classes minoritárias, ao lado de `Sokolova2009` e
  `Grandini2020`). Substituição de uma chave, uma citação; eu ficho a nova no
  mesmo dia.

`Barros2014` é citada **uma vez** na tese. O custo de errar é baixo; o custo de
deixar como está é uma referência possivelmente inexistente na bibliografia
final.

---

# FRENTE 2 — `Donmez2008` fichada e no bib

Fonte primária conferida antes de gravar, como você pediu: Crossref
(DOI `10.1145/1458082.1458165`, CIKM 2008, pp. 619-628) e **PDF lido na
íntegra** — 10 páginas, cópia aberta na página do co-autor na CMU. Nenhuma
duplicata: a `Donmez2009` é KDD 2009, DOI diferente; deixei as duas ligadas no
grafo pela aresta correta (`Donmez2009 builds_on Donmez2008` — 2009 constrói
sobre 2008, e não o contrário; foi o sentido que eu quase gravei errado).

**O que a obra dá à tese:** é ela que nomeia as **quatro** suposições do
oráculo clássico — infalível, incansável, individual e **insensível a custo** —
e relaxa as quatro. A Seção 2.2.3 hoje trata as três primeiras
(`Sheng2008`, `Snow2008`, `Donmez2009`, `Yan2011`); a quarta, que é a do FALCO,
estava sem lastro. Também dá antecedente formal a duas escolhas nossas:
- a decisão do laço como **par** instância-oráculo, `argmax (P(ans|x,k)·V(x) − Ck)`;
- o **orçamento** como restrição, no lugar do número de rótulos.

**Sugestão de local** (a prosa é sua): a frase que hoje termina em
"…roteamento entre anotadores de custos distintos
`\cite{Sheng2008, Snow2008, Donmez2009, Yan2011}`". Ancoro por trecho e não por
linha, pela razão do meu aviso 1935.

Na ficha há uma seção **"o que esta obra NÃO sustenta"**: não fala de LLM, não
fala de texto curto nem de espaço amplo de classes (4 bases **binárias**, de
1.550 a 4.601 instâncias), não mede custo real (os custos são parâmetros do
desenho) e não trata custo e falibilidade ao mesmo tempo. Serve para o R5 não
herdar atribuição indevida.

---

# FRENTE 3 — R3 do Cap. 3: já estava fechado; o que falta é o gate

As 3 fichas que você pediu (`Loshchilov2019AdamW`, `Reimers2019SBERT`,
`Wolf2020Transformers`) foram entregues às 19:55 na branch
**`ciclo/014-fichas-cap3` @`0f724fa`**, cada uma lida no PDF e com o registro do
que a tese usa de cada uma — inclusive a linha que diz que 3e-5, lote 32 e
decaimento 0,01 são **escolha da tese**, não resultado do AdamW. Reconferi
agora: a branch está íntegra e continua limpa.

**Não refiz nada.** O que falta ali não é trabalho meu, é **gate**. E o achado
daquela rodada continua aberto e depende do revisor1: o "SBERT multilíngue" do
apêndice do DRI-SL é atribuído ao artigo de 2019, onde "multilingual" aparece
zero vezes; a obra certa (Reimers & Gurevych, EMNLP 2020) **ainda não está no
`.bib`**. Fico com a ficha pronta para o momento em que a entrada existir.

## ACHADO 2 — a tese atribui a Hanneke a ampliação de uma obra que ele não cita

O Cap. 2 escreve: *"adapta-se aqui o arcabouço de `\citet{Cohn1996}`, **ampliado
por** `\citet{Hanneke2015}`"*.

Medido no PDF de 226 páginas, texto completo:
- **"Ghahramani" aparece ZERO vezes.** Nosso `Cohn1996` é Cohn, **Ghahramani** &
  Jordan, *Active Learning with Statistical Models* (JAIR 1996).
- O que a monografia amplia é **Cohn, Atlas & Ladner (1994)**: chamada de
  "trabalho seminal", presente nas referências, com a Seção 5.1 inteira
  dedicada ao algoritmo deles (CAL).

Essa obra **já está no nosso bib e já é citada pela tese** — `Cohn1994Improving`,
poucas linhas adiante, no parágrafo de comitês e espaço de versão. É o mesmo
padrão do ALPS e do SBERT: **a chave certa existe e está no lugar errado**.

Ressalva honesta: pode ser que a intenção fosse "a sêxtupla adapta Cohn1996;
Hanneke amplia a teoria do AA em geral". Como está escrito, "ampliado por" liga
Hanneke a Cohn1996. A prosa é sua; eu só declaro a medição.

## ACHADO 3 — corrigi o ano do Hanneke no bib (2015 → 2014)

Crossref (DOI `10.1561/2200000037`): FnTML 7, pp. 131-309, **2014-06-12**. O
próprio PDF do autor se refere à versão publicada como "[Hanneke, **2014**]".
Nossa entrada dizia 2015 e não tinha DOI. **Corrigido na branch, com o DOI.**
A chave continua `Hanneke2015` — renomear exigiria editar `.tex`, que é sua
superfície; a dissonância chave↔ano não sai no PDF. Reversível em um commit.

**Uma coisa que a ficha declara e que peço que não se perca no merge:** o que
li não é o arquivo publicado. A versão do FnTML é paga; li a **versão estendida
do próprio autor** (226 pp., "Theory of Active Learning", v1.1), que se declara
o superconjunto da publicada. Está escrito em destaque no topo da ficha, e por
isso as evidências estão ancoradas **por capítulo/seção**, não só por página.

---

## Estado dos locks e das tarefas
Liberei os dois locks (`referencias.bib` e `fichamentos/`) neste mesmo commit —
o trabalho está entregue e aguardando gate, que é exatamente quando o protocolo
manda liberar. Movi para `concluida` as tarefas **1420** (pendências do Cap. 2),
**1700** (Donmez) e **1940** (R3 do Cap. 3), além da **2250**.

## O que NÃO fiz
Não toquei em prosa, em nenhum `.tex`, no plano nem nas branches de outros. Não
inventei entrada de bib nenhuma: as duas que toquei (`Donmez2008` nova,
`Hanneke2015` corrigida) têm DOI conferido na Crossref e PDF lido. O build da
tese não é verificável neste ambiente e nada aqui depende dele.
