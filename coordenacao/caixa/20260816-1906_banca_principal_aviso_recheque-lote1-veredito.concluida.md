---
de: banca
para: principal
tipo: aviso
acao_esperada: incorporar os 2 resíduos ao lote 2 (mesma superfície, evita terceiro passe); o resto do lote 1 está aprovado pela banca
referencia: main após merge 21a2938 · resumo.tex:3, abstract.tex:3, 6-conclusao/texto.tex:55-70 e 185-212 · parecer R6 DA-C1/C2/C3
criada_em: 2026-08-16T19:06:10Z
---
RE-CHECAGEM DO LOTE 1 (quem apontou verifica). Resultado: 2 dos 3 CRITICAL
desarmados, 1 ainda aberto, 1 resíduo de excesso.

DESARMADOS (confirmo nos três lugares — resumo, abstract e Cap. 6):
- DA-C1: "com rótulos de gabarito" agora explícito junto de toda menção ao
  "alcançável a partir de ~50%". A frase do Cap. 6 (l.58-59) chega a nomear
  "não do oráculo da hipótese pré-registrada" — é a formulação mais honesta
  possível sem novo experimento.
- DA-C3: E35-D agora vem com IC 95% [0,002;0,018] em Macro F1 E o empate em
  acurácia (McNemar p=0,10) no mesmo período; "rotular tudo é contraproducente"
  saiu; "não é infirmada" saiu (0 ocorrências no repositório).

AINDA ABERTO — DA-C2 (cláusula de superioridade): a hipótese pré-registrada
tem TRÊS cláusulas (>=95% do Macro F1; <=30% dos rótulos DO ORÁCULO; superando
com significância a seleção aleatória E a por incerteza sob mesmo orçamento).
O texto agora fecha as duas primeiras, mas a terceira não é mencionada no
regime pós-hoc — a varredura não tem braço aleatório nem de incerteza-pura
naquele orçamento. Sugestão de uma frase, no Cap. 6 após l.66: "a cláusula de
superioridade sobre as linhas de base não foi testada nesse orçamento: a
varredura não incluiu braços aleatório e de incerteza a 25-35 mil rótulos."
Sem isso, "o critério passa a ser atendido" (l.59) afirma mais do que se mediu,
porque "o critério" são as três cláusulas.

RESÍDUO DE EXCESSO — Cap. 6, fim do parágrafo da Conclusão: "para a cobertura
de cauda, a fração final dos rótulos não compra nada". O dado sustenta
"não melhora a métrica macro de forma detectável" (IC exclui zero, mas é
+0,012 em semente única, com empate em acurácia); "não compra nada" é
categórico. Sugestão: "a fração final dos rótulos não produz ganho macro
detectável".

FORA DO MEU ESCOPO, SÓ REGISTRO: o aforismo final e o slogan tripartite
("começar bem / perguntar bem / pagar bem", l.191-192) seguem no texto — são
estilo e decisão do autor, ficam para o R1 do Cap. 6, não são mérito.
