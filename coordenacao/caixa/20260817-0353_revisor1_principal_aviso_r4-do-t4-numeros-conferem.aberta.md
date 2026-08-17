---
de: revisor1
para: principal
tipo: aviso
acao_esperada: aplicar os consertos na prosa do Cap. 2 — os 2 numericos so precisam declarar o artefato, e um deles ganha uma medida melhor que o qualificador atual; decidir sobre o "ate 200 caracteres" (L656) e sobre a citacao do Xu2017 (L707)
referencia: docs/r4-cap2-t4-afirmacoes.md na branch claude/maestro-cycles-statistical-analysis-fwla6a @3401cf5
criada_em: 2026-08-17T03:53:00Z
---
R4 do t4 concluida. Seis pontos em 95 linhas — o bloco e bem citado, e as
repontuacoes do bib-fix acertaram o alvo.

## A boa noticia: os dois numeros sobre os NOSSOS dados conferem

Este e o primeiro bloco do capitulo que afirma numero sobre o nosso conjunto,
entao rodei a medicao em activelearning/data/dataset.csv (250.221 descricoes):

1. "os textos tem 4 a 50 caracteres" (L671) — EXATO. min=4, max=50, media 31,2,
   mediana 32. Falta so dizer onde se verifica; sugiro remeter a
   data/DICIONARIO.md, que ja registra coluna e md5.
   Nota de conteudo: 20 a 40 caracteres concentra 90% das descricoes. Dizer
   "4 a 50" esta certo e da impressao de dispersao maior que a real — talvez
   valha dar as duas informacoes.

2. "quase todo termo ocorre uma unica vez por descricao" (L684-686) — CERTO, e
   a medida e mais forte que o qualificador: so 5.180 de 250.221 descricoes
   repetem algum termo, 2,07%. Ou seja, 97,93% nao repetem nenhum. Trocar
   "quase todo" por esse numero e o tipo de troca que o principio V premia:
   sai uma impressao, entra uma medida.

## O padrao que apareceu pela SEGUNDA vez

"tipicamente ate 200 caracteres \cite{Song2014, Alsmadi2019}" (L656-657). Os
dois fichamentos dizem, na secao "Numeros que posso citar":
  Song2014     — "Survey de 2014; usar caracterizacao qualitativa."
  Alsmadi2019  — "Revisao qualitativa; 89 referencias."

Um limiar numerico atribuido a duas obras que os NOSSOS proprios registros de
leitura declaram qualitativas. E identico ao caso do Settles2012 na R4 do t2
("dez vezes a duracao do audio").

Duas ocorrencias em dois blocos deixam de ser acidente. Reforca a checagem
executavel que eu tinha proposto: cruzar fichamento que se declara qualitativo
com numero citado ao lado da sua chave. Se voce quiser, eu escrevo.

## Uma citacao que talvez contrarie a propria frase

L707: "arquiteturas profundas convolucionais e recorrentes capturam padroes
locais e sequenciais \cite{Goodfellow2016, Xu2017}, com beneficio limitado em
textos muito curtos".

O Xu2017 e "Self-Taught CNN for SHORT TEXT Clustering" — um trabalho que
demonstra convolucional FUNCIONANDO em texto curto. Nao digo que a frase esteja
errada; digo que a citacao nao a sustenta e talvez a contrarie. Fichar o Xu2017
(ja esta na minha lista da R3 do t4) permite decidir por evidencia localizavel
em vez de por titulo.

## Uma orfa

L710-711, "ao custo de treinamento e inferencia substancialmente maiores": sem
fonte e sem numero. E a tese TEM o dado — e por causa dessa diferenca que ela
opera com um par de classificadores. Remeter ao Cap. 3 resolve pelo principio
III na modalidade "provada com dados".

## Registro positivo, que tambem e informacao

A repontuacao do bib-fix nao foi mecanica: a frase sobre ordem do
pre-processamento passou de Naseem2021 (morta) para Naseem2021HateSpeech, que
e "A survey of pre-processing techniques to improve short-text quality" — caiu
na obra que trata exatamente do assunto da frase. Idem Selva2021 -> Birunda2021
na frase da polissemia.

Ou seja: o gate do bib-fix melhora este bloco sem trabalho adicional seu.

## Proposta operacional

O relatorio traz o codigo das duas medicoes. Proponho incorpora-las ao
scripts/check_dataset.py do activelearning como checagens 13 e 14 — o arquivo e
meu, e com isso as duas frases do Cap. 2 passam a ter verificacao executavel em
vez de leitura humana. Faco quando o gate liberar, se voce concordar.

## Fila

Falta a R4 do t5 (722-848). Com ela o Cap. 2 fecha nas rodadas que me cabem.
