---
de: banca
para: principal
tipo: entrega
acao_esperada: pedir a cruzada do revisor2 sobre `banca/lote-2100-pontuais` @aa669ec (os seis achados sao dele; conferir que a redacao aplicada corresponde as propostas do 1612/1608) e levar ao gate do autor. Independente das outras duas branches da banca em fila (cap4-linha117 ja aprovada; f6-cap4-literatura aguardando cruzada).
referencia: tarefa 20260822-2100 · revisor2 1612 (achados 2, 3, 96%, Settles) e 1608 (divergencias 2 e 3) · branch banca/lote-2100-pontuais @aa669ec
criada_em: 2026-08-22T23:59:00Z
---

# Lote 2100 entregue: as seis correcoes pontuais do revisor2

Uma branch, 5 arquivos, +41/-20. Cada item usa exclusivamente os numeros e as
propostas de redacao do revisor2 (1612/1608); nada foi inventado:

1. **795 categorias** (3-metodo, racional do gate-85): uma oracao declara que
   a regua de 89,56% foi medida nas 795 categorias de menor nivel, espaco de
   rotulo maior que as 621 da amostra em que os oraculos sao avaliados; regua
   no maximo subestimada. Atende a "Condicao obrigatoria ao citar" da ficha
   da dissertacao; "795" passa a existir no corpo da tese.
2. **Wertz2022** (2-fundam:400): a glosa deixa de importar multirrotulo como
   se fosse o nosso caso — agora "classificacao multirrotulo extrema
   (centenas de rotulos possiveis e varios rotulos por texto)" — e ganha as
   duas pecas fichadas que resolvem a tensao com o Cap. 5: o proprio Wertz
   (ganho de selecao onde rotulos pouco co-ocorrem; rotulo unico e o caso
   extremo) e Rouzegar2024 (rotulo unico com poucas classes: selecao vence a
   aleatoria de forma consistente).
3. **Cap. 6 l.87**: 96% corrigido para 95% (par da S-rand, como o 8,5% de
   custo ao lado).
4. **Cap. 1**: o "menos de 10%" atribuido ao Settles2009 saiu (a ficha
   desautoriza numeros); Settles fica como a revisao canonica que estabelece
   o fenomeno e o unico numero da frase passa a ser o 15,45% do
   Schroder2022, que esta fichado com tabela e pagina.
5. **Divergencia 2 (entropia)**: 3-metodo agora diz o que foi medido e nada
   alem — a Fase 2 seleciona por entropia; margem/confianca tem estimativas
   pontuais de LCE superiores, mas o desenho nao as testou entre si (os
   testes sao de cada estrategia contra a aleatoria, e a entropia supera a
   aleatoria com a mesma significancia); troca de estrategia registrada como
   extensao imediata. Redacao do revisor2, adaptada para nao usar codigo E.
6. **Divergencia 3 (dois epsilons)**: 3-metodo separa a tolerancia de
   estagnacao do ruido amostral e remete ao A7; o A7 traz a reconciliacao
   completa do revisor2: eps=1e-3 nao deriva de 1/sqrt(n_V)=0,0224, e cerca
   de vinte vezes menor, logo o criterio executado e o permissivo — a parada
   precoce nao e artefato de tolerancia estrita.

Evidencia: check-bib PROBLEMAS nenhum; check-travessao nenhum; espelhos
varridos (nenhum outro "96%" nem "menos de 10%" na tese).

**Achado no caminho, para sua triagem**: 5-resultados-falco l.243-244 chama a
entropia de "estrategia pre-registrada da Fase~2". O pre-registro nao fixa
estrategia de selecao; depois da reancoragem do termo no Cap. 3, essa
ocorrencia afirma mais do que o documento sustenta. Nao editei (fora do
escopo do lote); candidata a correcao de uma palavra ("adotada" ou "fixada de
antemao") com decisao do autor.

Com isto a banca zera a fila de tarefas abertas: cap4-linha117 (cruzada
aprovada), f6-cap4-literatura e lote-2100-pontuais aguardam cruzada + gate.
