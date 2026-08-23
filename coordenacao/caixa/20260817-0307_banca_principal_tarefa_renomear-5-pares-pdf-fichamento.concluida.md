---
de: banca
para: principal
tipo: tarefa
acao_esperada: rotear a um revisor (determinação do autor em conversa, 2026-08-17): renomear os 4 pares PDF+fichamento para as chaves canônicas e fechar o refichamento do Cap. 1; banca confere depois
referencia: aviso correcao-5-pdfs-existem (e18fb84) · plano cap1.R3 nota pendente · superfície fichamentos/ e referencias-pdf/ (revisores)
criada_em: 2026-08-17T03:07:47Z
---
O autor mandou executar a renomeação. Especificação completa (mecânica, sem
aquisição, sem tocar prosa):

RENOMEAR (git mv, preserva história):
1. referencias-pdf/alsmadi2019shorttext.pdf -> Alsmadi2019.pdf
   fichamentos/alsmadi2019shorttext.md      -> Alsmadi2019.md
2. referencias-pdf/song2014shorttext.pdf    -> Song2014.pdf
   fichamentos/song2014shorttext.md         -> Song2014.md
3. referencias-pdf/devlin2019bert.pdf       -> Devlin2019.pdf
   fichamentos/devlin2019bert.md            -> Devlin2019.md
4. referencias-pdf/zhang2022surveyAL.pdf    -> zhang-etal-2022-survey.pdf
   fichamentos/zhang2022surveyAL.md         -> zhang-etal-2022-survey.md
(Zhang2025 já está na grafia canônica — nada a fazer.)

DENTRO de cada fichamento renomeado, atualizar 2 campos do front-matter:
- id: <chave canônica>
- pdf: referencias-pdf/<chave canônica>.pdf

DEPOIS: varrer os DEMAIS fichamentos por relações que apontem para as chaves
antigas (extends/builds_on/compares_with etc.) e repontuá-las — é o mesmo
invariante da relação pendurada; o check-fichamentos.py deve sair 0 nessa
classe. Regenerar o KG (build_kg.py) no mesmo commit.

DoD (executável): os 4 nomes antigos não existem mais em fichamentos/ nem em
referencias-pdf/; check-fichamentos.py sem relação pendurada e sem PDF
declarado ausente; check-bib.py com o invariante fichamento-âncora verde; KG
regenerado sem nó duplicado (contagem de nós igual ou menor).

ATENÇÃO DE TIMING: as chaves canônicas só passam a ser CITADAS quando
bibfix/lotes mergear. A renomeação pode rodar antes (fichamento órfão de
citação não quebra nada), mas o commit deve declarar essa ordem para o gate.
Fecha a última pendência do R3 do Cap. 1.
