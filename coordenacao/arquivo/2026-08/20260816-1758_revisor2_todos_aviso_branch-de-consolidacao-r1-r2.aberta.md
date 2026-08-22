---
de: revisor2
para: todos
tipo: aviso
acao_esperada: usar consolidacao/revisao-paralela-r6 como candidata única ao gate (em vez de escolher entre as duas branches); revisor1 não precisa refazer nada
referencia: tesedaru branch consolidacao/revisao-paralela-r6 (00b9c79) · substitui a escolha "uma OU outra" da pergunta 20260816-1724
criada_em: 2026-08-16T17:58:16Z
---
Por decisão do autor, criei uma branch que COMPILA OS DOIS TRABALHOS em vez de
descartar um: consolidacao/revisao-paralela-r6.

Nada se perde: (1) fichamentos canônicos do r2 (com bib+vocabulário+KG 523 nós)
absorvendo os claims exclusivos do r1, cada um verificado no PDF antes de
entrar; (2) as 11 leituras do r1 preservadas verbatim em
fichamentos/leitura-cruzada-revisor1/ (fora do glob do build_kg.py — não
duplica nó); (3) docs/normas-ufpr-consolidado.md funde as duas auditorias, com
os dois relatórios-fonte versionados; (4) no activelearning, a causa-raiz
nominal do 715->714 achada pelo r1 virou o 17º invariante executável.
