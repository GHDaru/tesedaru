---
de: banca
para: principal
tipo: aviso
acao_esperada: incorporar os achados E1 e E2 à decisão já pendente do veredito (DA-C2/lote 2); com isso e o gate do cap1-r4, o Cap. 1 fecha R5 e fica aguardando só o R7 do autor
referencia: 1-intro/texto.tex:95-107 (branch banca/cap1-r4-correcoes) · 3-metodo:149,173,387,474-476 · 5-resultados:499-501 · plano cap1.R5
criada_em: 2026-08-16T21:23:06Z
---
R5 DO CAP. 1 (números x artefatos + espelhos), escopo estrito no capítulo.

NÚMEROS PRÓPRIOS: só 30% e 95% (o critério). Ambos espelham corretamente:
- 30% do pool: consistente com a re-baseação do Cap. 3 (pool de 50 mil; 30% =
  15 mil, 3-metodo:173) e com o resumo/abstract ("<=30% dos rótulos").
- 95% do Macro F1: operacionalizado em 3-metodo:474-476 (F1(A) >= 0,95*F1(D));
  a aritmética do Cap. 5 confere (0,95 x 0,451 = 0,428).
- O "piso de acurácia fixado de antemão" é citado SEM número no Cap. 1 e
  numerado (85%) só no Cap. 3 — camadas corretas, sem vazamento.

DOIS QUEBRA-ESPELHOS, ambos ligados a decisões já abertas:

E1 (ALTA, acopla ao R4-A8): o protocolo de refutação do Cap. 1 (:101-103) diz
"se nem o melhor oráculo APROVADO sustentar o critério, a hipótese é
refutada". Na execução, NENHUM oráculo foi aprovado (o gate de 85% falhou em
todos) e a hipótese foi testada mesmo assim com o melhor disponível. O
protocolo enunciado no Cap. 1 não descreve o que foi feito. Correção possível
no Cap. 1 (1 frase): prever o ramo "se nenhum oráculo for aprovado, o teste
prossegue com o melhor disponível e a violação do gate é registrada" — mas
isso é a MESMA decisão do R4-A8 (declarar a violação no Cap. 5); tratar junto.

E2 (MÉDIA): o Cap. 1 (:103-105) promete análise que separa DUAS causas da
perda ("o erro que o oráculo introduz" e "a redução da quantidade de
rótulos"); o E3' entrega decomposição em TRÊS (ruído A-B, seleção B-C,
orçamento/parada E) e atribui a perda ao critério de parada — que não é
nenhuma das duas causas nomeadas no Cap. 1. Correção de 1 linha no Cap. 1:
enumerar as causas como "o erro do oráculo, o valor da seleção e o momento de
parada" (ou equivalente).

JÁ RASTREADO EM OUTRO ITEM (não duplicar): a cláusula de superioridade
("superando aleatória e incerteza", :97-99) segue enunciada no Cap. 1 e não
testada no regime pós-hoc — é o DA-C2, que está na sua fila do lote 2.

VEREDITO R5-CAP1: aprovado com os 2 ajustes acima (ambos de redação, 1 frase
cada, mesma superfície do cap1-r4 que está indo a gate — dá para incluir no
mesmo ciclo se o autor preferir).
