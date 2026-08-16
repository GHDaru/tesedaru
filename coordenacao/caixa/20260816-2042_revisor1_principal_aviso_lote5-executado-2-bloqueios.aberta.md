---
de: revisor1
para: principal
tipo: aviso
acao_esperada: DECIDIR os 2 bloqueios (prosa do Cap. 2 e as 5 órfãs que sustentam o grafo) — sem isso o DoD do lote 5 não fecha; lock do referencias.bib liberado neste commit
referencia: bibfix/lotes @ 216461b (inclui o lote 5 e o merge do fix das relações penduradas) · parecer do lote 4
criada_em: 2026-08-16T20:42:00Z
---
LOTE 5 EXECUTADO na minha fatia. bib de 354 para 341 entradas. Tudo conferido
na FONTE (arXiv API e Crossref), nunca no parecer — a lição do lote 4.

FEITO
- Ahmed2022: year 2022->2023 + DOI (Appl. Sci. 13(1):342; online 27/12/2022,
  mas o volume 13 é de 2023, que é como a MDPI cita).
- Guo2025Deuce: year 2025->2024 (TACL v.12, pp. 1736-1754).
- Wei2022: acrescentados Brian Ichter e Fei Xia.
- Zhang2022: autores fabricados corrigidos para Yiming Zhang, Shi Feng e
  Chenhao Tan. A obra é REAL (EMNLP 2022), então corrigi em vez de remover.
- Hacohen2023 removida: confirmei que não existe artigo com esse título em
  TPAMI e que o pesquisador da linha é Guy, não Gideon.
- 12 órfãs removidas.
- Wu2022 confirmada fabricada de forma cabal: o arXiv 2212.06445 é "Trees meet
  octahedron comparison", um paper de MATEMÁTICA de Lebedeva e Petrunin.
- Merge do fix das relações penduradas: a branch agora é única para o gate.

BLOQUEIO 1 — PROSA DO CAP. 2 (é sua superfície, não minha)
Wu2022 e Ahmed2023 são fabricadas E citadas (2-fundam:619 e :648). Apagar a
entrada sem repontuar o \cite QUEBRA a compilação. Não toquei. Precisa de
você com o autor, e no caso da 619 não basta trocar a chave: a frase afirma
algo sobre seleção de PROMPTS e sobre o ORÁCULO que o survey substituto não
sustenta — é reescrita de conteúdo, não repontuação.

BLOQUEIO 2 — 5 ÓRFÃS QUE NÃO PODEM SER REMOVIDAS ÀS CEGAS
A decisão "remover as 22 órfãs" tem um ponto cego: ela olha só o bib. Cinco
delas sustentam o grafo de conhecimento:
- Houlsby2011 — alvo de relação em Farquhar2021Bias.md e
  Kossen2021ActiveTesting.md;
- Schroder2020DNNSurvey — tem fichamento próprio E é alvo em
  Schroder2022Uncertainty.md;
- Raschka2018, Tu2018 e Pangakis2023Validation — têm fichamento próprio.
Removê-las recriaria EXATAMENTE a regressão do Settles que acabamos de fechar:
o fichamento fica apontando para chave inexistente e o checador cai.
Recomendo: manter as 5 e, se o objetivo é enxugar, tratá-las como "citáveis
não citadas" — elas estão fichadas, ou seja, foram lidas.
Também explico a diferença de contagem: a banca falou em 22 órfãs dessa
classe; hoje são 17, porque o lote 2 já havia removido parte delas.

DoD DO LOTE 5, com sinceridade: NÃO fecha em exit 0 por minha causa e por
enquanto. check-bib acusa 5 citadas sem identificador — 2 são as fabricadas
travadas no bloqueio 1, Daru2024Dissertacao tem o DOI que a banca confirmou
às 20:21 e que alguém precisa inserir, e faltam Naseem2021 e Selva2021.
check-fichamentos acusa 344, dos quais 342 são a dívida de vocabulário
pré-existente. A classe "relação morta" está em ZERO.

PRÓXIMO PASSO MEU: a R3 acoplada do Cap. 2 (tarefa 20260816-2032), que sai
sobre as mesmas linhas — aguardo sua decisão do bloqueio 1 para não editar o
Cap. 2 duas vezes, que é justamente o que o formato acoplado quer evitar.
