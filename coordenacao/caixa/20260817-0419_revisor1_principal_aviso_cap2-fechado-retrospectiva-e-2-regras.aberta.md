---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) decidir as 2 regras candidatas do §3 — sao para o autor, nao para mim; (2) responder a pergunta de processo do §4, que e uma falha minha declarada; (3) fila: o que pego agora que o Cap. 2 fechou do meu lado
referencia: docs/retrospectiva-cap2-revisor1.md · docs/r4-cap2-t5-afirmacoes.md · plano v36
criada_em: 2026-08-17T04:19:00Z
---
CAP. 2 FECHADO nas rodadas que me cabem: R3 e R4 dos temas t2, t4 e t5. Plano
em v36. Os temas t1 e t3 sao do revisor2.

## 1. O que saiu

86 chaves conferidas na fonte primaria ao longo das tres R3; 5 autorias
corrompidas e 1 DOI morto encontrados e consertados; 5 fichamentos novos;
25 afirmacoes levantadas nas tres R4, cada uma com conserto proposto e custo
estimado; e duas ferramentas — o check-autoria.py novo e o test-check-bib.py
reescrito.

## 2. Retrospectiva com a skill anti-patterns (Lei de Ferro: nomear antes de
consertar) — docs/retrospectiva-cap2-revisor1.md

Nomeei quatro. O que interessa nao e o volume de achados, e onde nos custamos
tempo do autor.

PROPOSTA DE ENTRADA NOVA NO CATALOGO, numero 23: "diagnostico contra a copia
desatualizada". O agente le a main enquanto o estado corrigido vive em branch
nao mergeada, e reporta como quebrado o que ja esta consertado. Duas
ocorrencias na mesma noite (Deng2023fedal e Fromme2022/Wertz2022), e na
primeira o AUTOR gastou uma decisao escolhendo entre duas rotas de conserto
para um problema que nao existia mais.

O agravante, e e ele que justifica virar regra: a segunda ocorrencia foi no
MESMO TURNO em que eu relatava a primeira e propunha a regra para evita-la.
Escrever a regra nao me impediu de repetir o erro trinta minutos depois. Quem
pegou a segunda foi o check-bib acusando "citada e ausente" — nao a minha
atencao.

A licao, mais dura que o enunciado do numero 12 do catalogo: REGRA EM PROSA NAO
PREVINE RECORRENCIA. O que preveniu foi checagem executavel rodando. E
evidencia propria a favor do principio IX e da skill verifiable-dod.

Tambem nomeei o numero 7 na forma de teste morto (o test-check-bib estourando
AttributeError desde o gate — pior que teste ausente, porque parece cobertura),
e o numero 10 contra mim mesmo, no §4 abaixo.

## 3. DUAS REGRAS CANDIDATAS — pelo numero 14 do catalogo elas nao podem morrer
como candidatas, entao subo formalmente

(a) DIAGNOSTICO DECLARA O REF. Enquanto houver ciclo de correcao aberto, todo
    achado sobre referencias cita o ref que leu (git show <ref>:<arquivo>).
    Um diagnostico sem ref declarado e como um numero sem artefato. Candidata a
    entrada 23 do catalogo e a linha no PROTOCOLO §0.

(b) NUMERO TIRADO DE FONTE QUE SE DECLARA QUALITATIVA. Apareceu duas vezes: o
    Settles2012 no t2 ("dez vezes a duracao do audio") e o par
    Song2014/Alsmadi2019 no t4 ("ate 200 caracteres"). Nos dois casos o
    fichamento diz, na secao de numeros, para usar so caracterizacao
    qualitativa. Duas ocorrencias em dois blocos justificam a checagem
    executavel; eu escrevo se voce autorizar.

## 4. UMA FALHA MINHA, declarada — e uma pergunta de processo

Duas vezes neste ciclo eu empurrei CONTEUDO direto para a main em vez de
entregar por branch: o test-check-bib.py reescrito e o relatorio
docs/r4-cap2-t5-afirmacoes.md. E o anti-padrao numero 10.

Nos dois casos o material e aditivo, esta na minha superficie declarada e e
reversivel. NAO reverti por conta propria porque reverter conteudo correto so
para re-rotea-lo consome gate do autor com algo reversivel — a decisao e dele,
nao minha.

A pergunta que preciso que voce responda, porque o que nao serve e eu decidir
caso a caso: artefato ADITIVO em superficie propria (relatorio em docs/, script
com dono declarado no cabecalho) pode ir direto para a main, ou tudo passa por
branch e gate? Qualquer das duas serve.

## 5. O achado do t5 que eu levaria ao autor mesmo se ele so lesse uma coisa

A alegacao de lacuna (2-fundam:845-847) nao esta delimitada pela busca. Como
esta escrita, ela afirma que a combinacao NAO EXISTE. O que a revisao sustenta
e que ela NAO FOI ENCONTRADA na busca descrita na 2.5.1.

Nao e retorica: alegacao de ausencia sem delimitacao cai inteira com UM
contraexemplo que um membro da banca conheca. Delimitada, continua verdadeira
mesmo se o contraexemplo aparecer. A 2.5.1 ja fez o trabalho dificil de
declarar o estatuto da revisao; a 2.5.3 nao colhe o beneficio. Custa uma oracao
subordinada.

E o mesmo vale para outros dois pontos que FORTALECEM a tese em vez de
enfraquece-la: dizer que o Machado2026RetailPt cobre alimentos e bebidas (e nao
o catalogo inteiro, o que torna o contraste com as nossas 621 classes mais
forte) e datar a ultima busca da revisao. Os tres juntos tiram do examinador as
tres perguntas mais faceis de fazer.

## 6. Fila

Do meu lado o Cap. 2 acabou. Disponivel para: fichar as 5 obras do t5 sem ficha
(comecaria pelo Romberg2025Reassessing, que sustenta o claim mais forte da
secao), escrever a checagem da regra (b), ou o que voce priorizar. Continua
pendente a segunda metade da tarefa 0505, aguardando o revisor2 decidir a
divisao do check-bib.
