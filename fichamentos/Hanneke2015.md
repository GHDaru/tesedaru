---
id: Hanneke2015
title: "Theory of Disagreement-Based Active Learning"
authors: ["Hanneke, Steve"]
year: 2014
venue: "Foundations and Trends in Machine Learning 7(2-3), pp. 131-309"
doi: "10.1561/2200000037"
pdf: referencias-pdf/Hanneke2015.pdf
paper_type: survey
pillars: [p1-selecao]
status: fichado
proposes: []
uses_methods: [aprendizado-ativo, pool-based, aprendizado-baseado-em-desacordo, espaco-de-versao, cal, coeficiente-de-desacordo]
metrics: [complexidade-de-rotulos]
tasks: [classificacao-binaria]
builds_on: [Cohn1994Improving]
falco_relation:
  - type: fundamenta
    target: aprendizado-ativo
    note: "É a fonte teórica da promessa do AA: sob condições explícitas, a
           complexidade de rótulos cai de O(1/ε) para O(log(1/ε)) — a
           'melhoria exponencial' que a Seção 2.1 da tese invoca. Vale como
           fundamento do que se ESPERA do laço, e como delimitação honesta de
           quando isso NÃO vale (ver 'o que não sustenta')."
  - type: ameaca
    target: FALCO
    note: "A própria obra registra que a estratégia por desacordo 'às vezes não
           é ótima' (Cap. 1) e que a dependência logarítmica em 1/ε some sob
           ruído com α<1 (Cap. 2). Isto é: a promessa teórica do AA é
           condicional, e as condições não são verificáveis no cenário da
           tese (714 classes, ruído assimétrico de LLM). É argumento a favor
           de medir empiricamente, como a tese faz — e contra prometer ganho
           por autoridade teórica."
---

# Theory of Disagreement-Based Active Learning (Hanneke, FnTML 2014)

## Qual versão foi lida — declaração obrigatória
A versão publicada (FnTML 7(2-3):131-309) é paga. O que li e arquivei em
`referencias-pdf/Hanneke2015.pdf` é a **versão estendida do próprio autor**,
distribuída no site dele (`stevehanneke.com` → `active-survey.pdf`), intitulada
**"Theory of Active Learning", Version 1.1, 22/09/2014, 226 páginas**. A
primeira página diz textualmente: *"An abbreviated version of this article
appears in the Foundations and Trends in Machine Learning series [Hanneke,
2014]"*.

Consequências, para ninguém tropeçar depois:
1. **Não são o mesmo arquivo**: a publicada é a versão abreviada da que li.
2. **A paginação não corresponde**: as páginas abaixo são do PDF estendido; a
   obra publicada vai de 131 a 309. Por isso as evidências estão ancoradas
   também por **capítulo/seção**, que são estáveis entre as duas versões — a
   mesma disciplina do meu aviso 1935 sobre âncoras que apodrecem.
3. Quem precisar citar página da versão publicada terá de abrir a versão
   publicada. Nada nesta ficha depende disso.

## Resumo
Trata a pergunta que a prática do AA deixa em aberto: quanto se deveria
esperar ganhar, e quando não se ganha nada. Formaliza o ganho como
**complexidade de rótulos** — quantos rótulos são necessários para atingir erro
ε — e concentra-se na família **baseada em desacordo** (DBAL), cujo
representante canônico é o algoritmo CAL de Cohn, Atlas e Ladner (1994):
mantém-se a região onde as hipóteses ainda plausíveis discordam, e só se
consultam rótulos dentro dela. O resultado central é que, no caso realizável
(sem ruído), a complexidade de rótulos pode cair de O(1/ε) para O(log(1/ε)) —
melhoria exponencial —, e que essa melhoria é governada por uma única
grandeza, o **coeficiente de desacordo**. O texto é explícito quanto ao preço:
sob modelos de ruído mais realistas a dependência logarítmica se perde, e a
própria estratégia por desacordo "às vezes não é ótima".

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | No caso realizável, a complexidade de rótulos satisfaz Λ(ε,δ) ≤ 1 + ⌈log₂((1/ε)·ln(2/δ))⌉ — "uma melhoria exponencial sobre o aprendizado passivo" | Cap. 2 (Basic Examples), p. 26 do PDF estendido | 2.1 — é a fonte da expressão "melhoria exponencial em certos regimes" |
| C2 | A melhoria logarítmica em 1/ε "continua disponível sob a Condição 2.3 com α=1, **mas não para α<1**" | Cap. 2, p. 26 | 2.1 — é a delimitação do "certos regimes"; hoje a tese diz a promessa e omite a condição |
| C3 | Os limites de complexidade de rótulos do DBAL se exprimem por uma única grandeza, o **coeficiente de desacordo** | Cap. 1 §1.2, p. 9; Cap. 7 (dedicado a ele) | 2.1 — dá nome à quantidade que governa o ganho |
| C4 | O DBAL é atribuído ao "trabalho seminal de Cohn, Atlas e Ladner [1994]"; a Seção 5.1 é literalmente "The Realizable Case: CAL" | Cap. 1 §1.3, p. 10; sumário, p. 3 | ver ACHADO abaixo |
| C5 | "É sabido que o aprendizado ativo baseado em desacordo às vezes **não é ótimo**" | Cap. 1 §1.2, p. 8 | 2.1 e Cap. 6 — sustenta tratar a promessa como condicional |
| C6 | O escopo é **classificação binária**, hipóteses de dimensão VC finita, análise teórica; não há experimento | Cap. 2 (Setting), pp. 12-14 do PDF | limite de escopo — ver abaixo |

## O que esta obra NÃO sustenta
1. **Nada empírico.** É teoria: não há dataset, não há execução, não há
   comparação de seletores. Citar como fundamento da expectativa é correto;
   citar como evidência de desempenho, não.
2. **Nada sobre espaço amplo de classes.** O arcabouço é de classificação
   binária com dimensão VC finita. As 714 classes da tese estão fora do
   regime analisado — e essa distância é justamente o que dá valor à medição
   empírica do Cap. 5.
3. **Nada sobre ruído de LLM.** Os modelos de ruído tratados (Tsybakov,
   ruído limitado) são estatísticos e simétricos por hipótese; o ruído do
   oráculo LLM é assimétrico e estruturado (ver `taxonomia-ncar-nar-nnar`).
4. **Não promete ganho incondicional** — C2 e C5 são da própria obra.

## ACHADO: a tese atribui a Hanneke a ampliação de uma obra que ele não cita
O Cap. 2 escreve: *"adapta-se aqui o arcabouço de \citet{Cohn1996}, ampliado
por \citet{Hanneke2015}"*.

Medido no PDF (226 páginas, busca no texto completo):
- **"Ghahramani" aparece ZERO vezes.** `Cohn1996` no nosso `.bib` é Cohn,
  Ghahramani & Jordan, *Active Learning with Statistical Models* (JAIR, 1996)
  — a linha de redução de variância. A monografia **não a cita**.
- O que a monografia amplia é **Cohn, Atlas & Ladner (1994)**: citada como
  "trabalho seminal" (p. 10), presente nas referências (p. 221) e com a
  Seção 5.1 inteira dedicada ao algoritmo deles (CAL).

Essa obra **já está no nosso `.bib` e já é citada pela própria tese**, como
`Cohn1994Improving`, algumas linhas adiante (no parágrafo de comitês e espaço
de versão). É o mesmo padrão dos achados do ALPS e do SBERT multilíngue:
**a chave certa existe; está no lugar errado.**

**Ressalva honesta**: é possível que a intenção fosse "a definição formal (a
sêxtupla) adapta Cohn1996; Hanneke amplia o tratamento teórico do AA em
geral". Como está escrito, porém, "ampliado por" liga Hanneke a Cohn1996. A
prosa é do principal e a decisão é dele e do autor; eu só declaro o que medi.

## ACHADO 2: o ano no `.bib` está errado (2015 → 2014)
- Crossref, DOI **10.1561/2200000037**: *Theory of Disagreement-Based Active
  Learning*, FnTML vol. 7, pp. 131-309, **2014-06-12**.
- O próprio PDF do autor se refere à versão publicada como "[Hanneke, **2014**]".
- Nossa entrada dizia `year = {2015}` e não tinha DOI.

Corrigi `year` para 2014 e acrescentei o DOI nesta branch. **A chave continua
`Hanneke2015`** — renomeá-la exigiria editar `.tex` (superfície do principal),
e a dissonância chave↔ano é cosmética e não sai no PDF. Decisão do autor; é
reversível em um commit.

## Ideias que gera para a tese
1. **Dizer a condição junto com a promessa.** Hoje o Cap. 2 diz "garantias
   teóricas de melhoria exponencial em certos regimes". "Certos regimes" tem
   nome (C2): caso realizável, ou ruído com α=1. Uma oração a mais transforma
   uma alegação vaga em alegação verificável — e a fonte é a mesma.
2. **A obra é aliada da tese onde parece adversária.** C5 ("às vezes não é
   ótimo") e C2 justificam por que uma tese aplicada mede em vez de deduzir.
