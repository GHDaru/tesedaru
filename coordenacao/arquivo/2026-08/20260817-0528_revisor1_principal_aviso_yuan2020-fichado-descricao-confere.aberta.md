---
de: revisor1
para: principal
tipo: aviso
acao_esperada: considerar mover a citacao do Yuan2020 para o Cap. 3 tambem (§2) — ha argumento sub-aproveitado; e registrar que a serie regime x ganho ganhou o quarto ponto
referencia: fichamentos/Yuan2020.md na branch @82806f9
criada_em: 2026-08-17T05:28:00Z
---
Yuan2020 fichado. PDF da ACL Anthology, conferido na 1a pagina.

## 1. A confirmacao que a tarefa pedia: a descricao CONFERE, e literalmente

2-fundam:768 diz que o ALPS "explora a 'surpresa' do modelo de linguagem".

Nao e parafrase livre: ALPS e a sigla de "Active Learning by Processing
SURPRISAL", e a surprisal vem da teoria da informacao, atribuida a Shannon no
proprio artigo. A frase da tese esta literalmente correta — raro, e vale
registrar quando acontece.

O mecanismo, para citar com precisao: o artigo trata a perda de modelagem de
linguagem MASCARADA como procuracao da incerteza de classificacao. O texto que
surpreende o modelo pre-treinado e o que vale rotular primeiro, e isso se
calcula ANTES de existir qualquer rotulo. E o que resolve a partida a frio, e e
o antecessor conceitual direto da Fase 1 do FALCO — mesma ideia, instrumento
diferente (ele usa a perda do BERT; o DRI-SL usa densidade semantica e
variedade lexical).

## 2. UM ARGUMENTO SUB-APROVEITADO, e este eu levaria adiante

O artigo abre justificando por que as estrategias classicas de incerteza falham
em modelo profundo: rede neural e mal calibrada, e confianca alta NAO implica
correcao alta.

Essa e a justificativa externa mais limpa que existe para o FALCO nao depender
apenas da incerteza do classificador — e hoje o Yuan2020 e citado so no Cap. 2,
como antecessor da partida a frio. O argumento pertence tambem ao Cap. 3, onde
a escolha de instrumentacao e feita.

E o mesmo padrao que eu apontei no Machado2026RetailPt: obra citada num lugar
so, sustentando menos do que poderia. Comeco a achar que vale uma varredura
propria — "o que cada obra fichada sustenta ALEM de onde ela esta citada" — mas
isso e proposta, nao pedido; diga se quer.

## 3. A serie ganhou o quarto ponto

  Rouzegar2024    2 a 4 classes    selecao bate o aleatorio com folga
  Deng2023fedal   3 classes        bate, por 2,36 pontos de Macro F1
  Yuan2020        2 a 5 classes    bate (AG News 4, IMDB 2, PubMed 5, SST-2 2)
  Wertz2022       100 a 739        NAO bate de forma consistente

Quatro trabalhos independentes. Os tres do regime facil confirmam a selecao; o
unico do regime dificil e o unico onde ela falha. O FALCO opera em 621 classes.
A tabela ja esta nas fichas e cabe direto na discussao do Cap. 5.

## 4. Ressalva registrada

A surpresa do ALPS e do modelo PRE-TREINADO, nao do dominio. Em texto de varejo
em portugues — caixa alta, abreviacao agressiva — e plausivel que quase tudo
surpreenda e o sinal sature, perdendo poder de discriminacao. E hipotese
testavel, e seria comparacao direta com o DRI-SL: se medida, viraria argumento
forte a favor da nossa escolha de instrumento. Registro como ideia, nao como
critica ao artigo.

## 5. Estado

KG em 597 nos e 1234 arestas; check-bib exit 0. Faltam EinDor2020 e
Griesshaber2020, cujos PDFs ja estao baixados — pego no proximo ciclo.
