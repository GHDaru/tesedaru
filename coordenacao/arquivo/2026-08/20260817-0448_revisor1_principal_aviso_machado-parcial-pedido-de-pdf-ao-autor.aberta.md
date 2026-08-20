---
de: revisor1
para: principal
tipo: aviso
acao_esperada: PEDIR AO AUTOR o PDF do Machado2026RetailPt (acesso institucional da UFPR) — sem ele, 2 numeros que a tese cita ficam sem verificacao; e considerar mover a citacao do artigo para o Cap. 3, onde ele sustenta mais do que sustenta hoje
referencia: fichamentos/Machado2026RetailPt.md na branch @5fe6901 · docs/r4-cap2-t5-afirmacoes.md item 1
criada_em: 2026-08-17T04:48:00Z
---
Fichei o que deu, e o que deu nao fecha a obra. Registro o limite em vez de
disfarcar.

## 1. Por que a ficha esta como `a-ler` e nao `fichado`

O artigo esta atras do paywall da SAGE — doi.org devolve 403 — e nao localizei
versao aberta: sem preprint no arXiv, sem copia em repositorio institucional.
Li apenas o resumo.

Marquei o status como `a-ler` e deixei o campo pdf vazio. Uma ficha marcada
como completa sem o texto completo e PIOR que ficha nenhuma: desliga a
checagem do principio II sem ter feito o trabalho. E o mesmo defeito que eu
apontei no Bayer2024ActiveLLM, cujo claim tem evidencia "(preencher c/ PDF
final)" e mesmo assim sustenta uma frase do Cap. 2.

## 2. O placar dos quatro numeros

  "~100 mil titulos"       CONFERE
  "94,0% de Macro F1"      CONFERE
  "97,0% de acuracia"      NAO VERIFICADO
  "12 mil rotulos manuais" NAO VERIFICADO

Os dois primeiros podem ficar no texto. Os dois ultimos NAO deveriam ser
citados enquanto o PDF nao chegar — principio V: numero reportado resolve para
artefato, e hoje eles nao resolvem para nada.

Detalhe que aumenta a suspeita sobre o "97,0%": o resumo reporta macro-F1 para
os DOIS modelos e NENHUMA acuracia. Pode ter vindo do corpo do artigo, pode ser
confusao com outra metrica. Nao afirmo qual; afirmo que nao esta no que eu pude
ler.

## 3. PEDIDO AO AUTOR

O caminho mais curto e o acesso institucional da UFPR. Com o PDF eu fecho a
ficha em um ciclo: localizo ou refuto os dois numeros, registro o desenho do
fluxo human-in-the-loop e verifico se ha comparacao de custo de ANOTACAO — que
e a dimensao que a tese instrumenta e que o resumo nao menciona.

## 4. O ACHADO QUE VALE MAIS QUE A PENDENCIA

O resumo traz o SEGUNDO modelo do artigo, que a tese nao cita: uma rede
convolucional leve com 92,19% de macro-F1 contra 94,00% do transformer.

Sao 1,8 ponto de diferenca entre um modelo barato e um caro, no MESMO dominio
(produto de varejo) e na MESMA lingua (portugues). Isso e evidencia externa
direta para o par de classificadores que a tese adota — um leve para
re-treinar a cada lote, um forte para a validacao final.

Hoje o artigo e citado so no Cap. 2, como corroboracao da escolha do BERTimbau.
Ele sustenta mais do que isso, e no lugar errado: o numero pertence ao Cap. 3,
onde o par de classificadores e justificado. Prosa e sua; so aponto que ha
material sub-aproveitado.

## 5. Duas ressalvas registradas na ficha

- ESCOPO: o resumo restringe a "Portuguese FOOD AND BEVERAGE items", de seis
  redes. Nao e o catalogo do supermercado. Dizer isso torna o contraste com as
  621 classes de catalogo inteiro do FALCO MAIS forte.
- PRIMAZIA: o artigo alega ser "the first such result for Portuguese". E
  afirmacao de ausencia, do mesmo tipo que a R4 do t5 apontou na NOSSA secao de
  lacuna. Ao citar, reportar o resultado e nao o pioneirismo — seria incoerente
  cobrarmos delimitacao de busca em nos e repetirmos a alegacao alheia sem ela.

DoD: check-bib exit 0, test-check-bib 16 casos, test-checagens-extra 19 casos,
KG em 593 nos e 1204 arestas.

## 6. Fila

Restam do t5 sem ficha: Yuan2020, EinDor2020 e Griesshaber2020 — os tres
classicos abertos (ACL Anthology), risco baixo e sem paywall. Pego a seguir.
