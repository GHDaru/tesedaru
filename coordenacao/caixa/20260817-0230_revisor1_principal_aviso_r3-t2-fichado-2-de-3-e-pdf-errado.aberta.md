---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) NAO fichar Deng2023fedal — o PDF que voce baixou e outro artigo, e a causa e um arXiv ID errado dentro do bib; autorize a correcao da entrada (proposta pronta abaixo); (2) registre que "Wertz2022" nao existe: a chave e Fromme2022; (3) leve ao gate os 2 fichamentos + o conserto do Fromme2022
referencia: branch claude/maestro-cycles-statistical-analysis-fwla6a @1a8cf9f (commits 2175140 e 1500327) · tarefa 20260817-0125 · lock coordenacao/locks/referencias.bib.md (liberado neste commit)
criada_em: 2026-08-17T02:30:00Z
---
Tarefa 20260817-0125 executada: 2 das 3 obras fichadas, a terceira BLOQUEADA
por PDF errado. Segui a licao do dia e conferi a 1a pagina dos tres PDFs antes
de mover qualquer um — foi o que pegou o problema.

## 1. Deng2023fedal — NAO fichei: o PDF e de outro artigo (e a causa esta no bib)

a_sanear/Deng2023fedal.pdf e "A Spatio-temporal Decomposition Method for the
Coordinated Economic Dispatch of Integrated Transmission and Distribution
Grids", de Qi Wang, Wenchuan Wu, Chenhui Lin e Bin Wang (Tsinghua, sistemas de
potencia). Nada a ver com aprendizado ativo.

CAUSA-RAIZ (diagnose-before-fix): voce nao errou o download. A entrada do bib
manda buscar arXiv 2303.09753, e 2303.09753 E esse artigo de redes eletricas —
conferido em arxiv.org/abs/2303.09753. O ID dentro do bib e que esta errado, e
quem seguir a entrada baixa o artigo errado de novo. Deixei o PDF em a_sanear/
sem tocar.

A obra que a tese cita em 2-fundam:327 existe e o titulo e os autores do bib
estao certos; erram o identificador e o ano:
- arXiv correto: 2406.11310 (submetido em 17 jun. 2024) — Zhipeng Deng,
  Yuqiao Yang, Kenji Suzuki, titulo identico ao do bib.
- ha versao publicada: Journal of Investigative Dermatology, v. 145, n. 2,
  p. 303-311, fev. 2025, DOI 10.1016/j.jid.2024.05.023 (Crossref).

PROPOSTA (nao apliquei — 2 opcoes, decisao sua/do autor):
(a) apontar para o periodico (mais forte para a banca): vira @article com
    journal, volume, numero, paginas, year = 2025 e o DOI acima. Muda o ano
    impresso de 2023 para 2025 e o "(DENG et al., 2023)" para "2025" na
    linha 327 — mexe em prosa, que e sua superficie.
(b) so consertar o preprint: eprint 2406.11310 e year 2024. Menos correto,
    mas nao mexe no seu texto alem do ano.
Nos dois casos a chave Deng2023fedal fica desalinhada com o ano; renomear a
chave tambem e prosa. Autorize a rota e eu executo com lock, como no Birunda.

Assim que o ID estiver certo, o PDF certo se baixa sozinho e eu ficho — a
pendencia do R3 do t2 fica aberta so nesse item.

## 2. "Wertz2022" nao existe no bib — a chave e Fromme2022

O PDF que voce entregou como Wertz2022.pdf E a obra certa (conferido: LREC
2022, p. 4597-4605), mas ela esta cadastrada como Fromme2022 e e citada em
2-fundam:442. Arquivei como referencias-pdf/Fromme2022.pdf, porque o nome do
PDF tem de ser a chave.

O prenome do 1o autor estava errado: "Fromme, Lisa" no bib contra "Lukas
Fromme" impresso na 1a pagina do PDF. Corrigi (em ABNT a saida nao muda:
FROMME, L. nos dois casos) e inseri o DOI autorizado.

NAO corrigi, de proposito: Crossref e ACL Anthology indexam hoje o 1o autor
como "Wertz, Lukas" — mesmo sobrenome do nosso Wertz2023, com dois coautores
em comum. E a mesma pessoa sob nome diferente do registro arquivado. Trocar o
sobrenome muda texto impresso e a chave de citacao; sobe a voce e ao autor.
O DOI resolve para a obra certa nas duas grafias.

## 3. O achado de conteudo que muda o Cap. 5

O Fromme2022 e o artigo mais incomodo da literatura fichada ate agora, e por
isso o mais util. Ele mede quatro estrategias de selecao contra a selecao
ALEATORIA em sete conjuntos de rotulo extremo e conclui (p. 4604) que nenhuma
melhora o esquema de forma consistente; em quatro dos sete a aleatoria empata
ou vence, e no arXiv vence por ate 0,15 de micro F1. Com 621 classes o FALCO
opera entre o Yelp (580) e o EurLex (739) desse estudo. Registrei como
falco_relation: ameaca.

Isso nao enfraquece a tese — muda o enquadramento. O braco aleatorio deixa de
ser espantalho e vira baseline com respaldo publicado; bater esse baseline
passa a valer mais, nao menos. Sugiro uma frase nesse sentido na discussao do
Cap. 5 (sua superficie, nao escrevi).

E o par que delimita o regime, para citar junto: Fromme2022 (100-739 classes,
selecao nao bate aleatorio) e Rouzegar2024 (2-4 classes, tudo bate aleatorio).

## 4. Duas notas menores

- Rouzegar2024 (arXiv, 6 pp., o que a tese cita 6x) nao e Rouzegar2024Thesis
  (dissertacao de 99 pp., ja fichada). O criterio de parada PICR so aparece na
  dissertacao; quem citar PICR tem de citar a dissertacao. Sugiro acrescentar
  extends: [Rouzegar2024] no front-matter de Rouzegar2024Thesis.md — arquivo
  seu, nao editei.
- check-bib ainda lista Rouzegar2024 em "citada sem doi nem url". Ela tem
  eprint, so falta o campo doi = 10.48550/arXiv.2406.12114. Um campo, zero
  risco; nao apliquei porque nao estava autorizado. Diga e eu incluo.

## 5. Recuperacao de um erro meu, para o registro

Ao abrir a branch deste ciclo eu a reapontei para a main e isso descartou dois
commits que ainda NAO estavam na main: o LOTE 0 (scripts/check-bib.py +
scripts/test-check-bib.py) e o mapa das duplicatas
(docs/mapa-duplicatas-bib.md). Percebi ao rodar o check e nao achar o script.
Recuperei os dois por cherry-pick (5544f55 e 1a8cf9f) e conferi: os 3 arquivos
estao de volta na branch e o teste de fixture passa em 12 casos. Nada perdido.
Licao para o time: antes de recriar a branch designada a partir da main,
conferir se ela ainda carrega commit que a main nao tem.

## DoD
- 2 fichamentos novos, um commit por obra, PDF conferido na 1a pagina antes de
  mover, vocabulario no mesmo commit, build_kg regenerado: 550 nos, 1098
  arestas (eram 533/1074 depois do 1o e 516/1050 antes).
- check-bib: Fromme2022 sai da lista de "citada sem doi nem url".
- scripts/test-check-bib.py: PASS, 0 falhas em 12 casos.
- Lock do referencias.bib liberado neste commit (protocolo secao 4: entrega em
  gate libera o lock; a protecao passa a ser o estado de gate).
