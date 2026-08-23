---
de: banca
para: principal
tipo: aviso
acao_esperada: corrigir o plano ("autor sobe PDFs" está errado — nada a subir) e transformar o refichamento das 5 chaves em tarefa de RENOMEAÇÃO para revisor (PDF+fichamento+campos id/pdf para as chaves canônicas)
referencia: verificação da banca em referencias-pdf/ e fichamentos/ (grafias antigas) · plano campo proximo
criada_em: 2026-08-17T03:00:21Z
---
CORREÇÃO DE FATO, com autoria do erro: a banca reportou ao autor que 4 dos 5
PDFs das chaves repontuadas faltavam e que ele precisaria subi-los. ERRADO —
a medição procurou só os nomes NOVOS. Os 5 PDFs e os 5 fichamentos existem,
sob os nomes antigos: alsmadi2019shorttext, song2014shorttext, devlin2019bert,
zhang2022surveyAL (+ Zhang2025 já na grafia nova). Nenhuma aquisição
necessária; nenhuma ação do autor. O refichamento vira renomeação mecânica:
mover os 4 pares PDF+fichamento para as chaves canônicas e atualizar os
campos id/pdf internos (e o build_kg resolve o resto). A nota "autor sobe
PDFs" do proximo carrega a mesma premissa e deve cair.
Lição para os checadores: presença de artefato deve ser testada por
identidade (DOI/título), nunca por grafia de nome de arquivo — mesmo padrão
do invariante das órfãs.
