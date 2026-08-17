---
de: banca
para: principal
tipo: tarefa
acao_esperada: incluir a edição aprovada pelo autor no ciclo do t1 (mesma zona do reforço das métricas, mensagem b865ae6) — as duas edições do t1 podem ir no mesmo lote/gate
referencia: aprovação do autor em conversa com a banca, 2026-08-17 ("Aprovo a reescrita, manda ao principal") · leitura do autor na subseção de validação (2.1.3) · princípio VII (camadas) e III (fundamentação por argumento)
criada_em: 2026-08-17T04:39:07Z
---
Segunda edição nascida da leitura do autor no t1. Ele flagrou: a exigência de
deduplicação está justificada POR EVIDÊNCIA AINDA NÃO APRESENTADA ("motivada
pela auditoria da base") — resultado do Cap. 3 sustentando frase do Cap. 2.
A banca propôs inverter a direção da justificativa (conceito sustentado por
argumento definicional; decisão da tese como ponte; evidência fica no Cap. 3)
e o autor APROVOU.

FRASE ATUAL (2-fundam/texto.tex:136-140):
"Uma exigência adicional específica desta tese, motivada pela auditoria da
base (Capítulo~\ref{ch:metodo}): como descrições de produto se repetem, o
particionamento deduplica por texto normalizado \emph{antes} do sorteio,
prevenindo vazamento treino$\to$teste por duplicatas exatas."

FRASE APROVADA (substituir integralmente):
"Uma exigência adicional surge em bases textuais com instâncias repetidas:
uma duplicata exata que atravesse a partição coloca a mesma instância no
treino e no teste, e o que se mede deixa de ser generalização para ser
memorização. Por isso, o particionamento desta tese deduplica por texto
normalizado \emph{antes} do sorteio; a extensão do fenômeno na base e o
registro da decisão estão no Capítulo~\ref{ch:metodo}."

RACIONAL (para o commit/gate): o conceito de vazamento por duplicata é
definicional — sustenta-se por argumento (princípio III), sem depender da
auditoria; a menção à tese vira ponte (nomeia a decisão + \ref), padrão que
o R6 da banca estabeleceu para o Cap. 2; os números (19.356 duplicatas, 7,7%)
permanecem no Cap. 3, onde nascem. Decisão consciente de NÃO adicionar a
citação canônica de leakage (Elangovan et al. 2021, ausente do bib): o
argumento basta e citação nova dispararia fichamento com ganho marginal —
registrado aqui para a decisão ser rastreável.
