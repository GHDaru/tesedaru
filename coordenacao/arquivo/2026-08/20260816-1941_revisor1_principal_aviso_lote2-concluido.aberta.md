---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor no bloco de gates; encaminhar à banca para o lote 4 (verificação independente), com atenção especial aos 3 pontos de julgamento listados abaixo
referencia: bibfix/lotes @ 7b039c1 · mapa docs/mapa-duplicatas-bib.md · lock de referencias.bib liberado neste commit
criada_em: 2026-08-16T19:41:00Z
---
LOTE 2 CONCLUÍDO (7b039c1, na bibfix/lotes, sobre os lotes 1 e 3 do revisor2).
Lock do referencias.bib liberado no mesmo commit que integra o trabalho.

O QUE MUDOU: bib de 368 para 354 entradas (14 duplicatas removidas); 8
ocorrências de \cite reescritas, TODAS no Cap. 1; 5 fichamentos e 5 PDFs
renomeados; KG regenerado (527 nós, 1049 arestas).

EVIDÊNCIA: o check-bib.py do revisor2 não acusa mais duplicata, chave morta
nem fichamento sem entrada no bib; meu checador dá 0 titulo-duplicado,
0 citada-ausente e 0 chave-duplicada.

TRÊS PONTOS QUE PEDEM O OLHO DA BANCA (julgamento meu, não mecânica):

1. Bates2022 NÃO era duplicata: é entrada FABRICADA. Mesmo título, autores
   inventados (Bates, Leach, Serttas) sobre a obra real de Karl e Scherp
   (LNCS 14065). Removi. A chave citada, Karl2023, já estava correta. Como
   fabricação é matéria do lote 1, registro aqui para a banca conferir se há
   irmãs do mesmo tipo que passaram por "duplicata".

2. O lote transbordou para fichamentos/ por necessidade, não por escolha. A
   skill fichamento define a chave BibTeX como o ID do fichamento, do PDF e do
   nó do grafo; ao unificar a chave, 5 fichamentos ficariam ancorados em
   chaves inexistentes (foi o checador do revisor2 que apontou). Renomeei os 5
   pares, atualizei id/pdf no front-matter e corrigi 30 arestas em 25
   fichamentos. Superfície compartilhada — revisor2, confira.

3. Ao remover, mantive sempre a versão PUBLICADA sobre o preprint
   (Sener2018 sobre Sener2017, Ash2020 sobre Ash2019, Bojanowski2017 sobre
   Bojanowski2016) e fundi na canônica os campos que só existiam na removida,
   para não perder informação (booktitle completo do EinDor2020, volume do
   Souza2023). Nenhuma dessas escolhas está no parecer; são minhas.

DEFEITO MEU, PEGO ANTES DO COMMIT (para a retrospectiva): minha primeira
tentativa de reescrever os \cite normalizava espaço depois da vírgula e chegou
a alterar 28 linhas do Cap. 2 que NÃO deviam ser tocadas — inclusive juntando
linhas, o que deslocaria as referências arquivo:linha que a banca e o parecer
usam. Revertido e refeito com substituição só do token da chave. O Cap. 2 está
byte a byte intacto.

PENDÊNCIA ANTERIOR AINDA ABERTA: colisão em scripts/check-bib.py. O lote 0
dessa ferramenta era meu (entreguei em 33a9c50, com 13 casos de fixture) e o
revisor2 escreveu outra no mesmo caminho. Hoje a da branch é a dele. Não
sobrescrevi nada; decida qual fica, ou se fundimos — a minha cobre título
duplicado e identificador, a dele cobre fichamento órfão e chave morta.
