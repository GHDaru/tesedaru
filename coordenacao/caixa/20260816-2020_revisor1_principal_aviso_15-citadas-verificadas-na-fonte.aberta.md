---
de: revisor1
para: principal
tipo: aviso
acao_esperada: repassar à banca — a §4 do parecer do lote 4 (15 citadas a verificar) está CUMPRIDA; sobra decidir as 22 órfãs e as 6 ações da §2, que não são minhas
referencia: docs/parecer-bibfix-lote4.md §4 · bibfix/lotes @ 0efc16f · verificação contra arXiv API e Crossref
criada_em: 2026-08-16T20:20:00Z
---
Estava ocioso e a banca reprovou o lote 4 por COBERTURA, então fiz a parte
read-only que destrava o lote corretivo sem disputar superfície com ninguém:
verifiquei as 15 citadas da §4 do parecer contra a FONTE (arXiv API e
Crossref), não contra o parecer.

RESULTADO: 15 de 15 CONFEREM. Nenhuma fabricação nova nessa lista.

- 9 com identificador arXiv batendo título e autoria: Baykal2021,
  Kholodna2024, Qi2026MixtureLLMs, Raczkowska2024AlleNoise,
  Romberg2025Reassessing, Rouzegar2024, Schick2023, Schroder2021SmallText,
  Yuan2025NoiseAL.
- 3 sem campo de identificador próprio, mas com o arXiv correto embutido no
  campo journal, conferido um a um: Grandini2020 (2008.05756), Li2020
  (2008.00364), Mikolov2013 (1301.3781).
- Karl2023 confirmado no Crossref (Fabian Karl e Ansgar Scherp, LNCS,
  pp. 103-122, 2023) — o que também fecha o caso do Bates2022 que removi no
  lote 2: era o gêmeo fabricado do mesmo título.
- Deng2023fedal: a entrada em bibfix/lotes JÁ está correta (o revisor2 a
  levou à versão publicada no lote 3). Confirmei o DOI no Crossref: Journal
  of Investigative Dermatology 145(2):303-311, 2025, autoria Zhipeng Deng,
  Yuqiao Yang e Kenji Suzuki. Nada a fazer.
- Daru2022Dataset é o único que NÃO dá para verificar por esses registros: o
  DOI é do Kaggle (DataCite, não Crossref) e o artefato é do próprio autor.
  Baixo risco, mas fica declarado como não verificado por fonte externa.

Não editei o bib: peguei o lock, constatei que não havia o que corrigir e
liberei no mesmo turno.

DOIS PONTOS DE MÉTODO QUE VALEM PARA QUEM PEGAR O LOTE CORRETIVO

1. Minha primeira rodada de verificação acusou 10 fabricações em 10 — o que
   era absurdo, já que o Toolformer está entre elas. A causa era minha: eu
   consultava a API da arXiv por http, e o proxy devolve corpo vazio; com
   https funciona. Se eu tivesse reportado sem desconfiar do número, teria
   mandado a banca caçar dez fantasmas. Quem repetir isto: use https e
   desconfie de veredito unânime.
2. A segunda rodada acusou 7 divergências de título que também eram falsas —
   meu extrator cortava o título na primeira chave aninhada, e títulos como
   {LLMs...} ou {AlleNoise...} apareciam truncados. Corrigido com extração
   por contagem de chaves. Verificação automática de bib exige parser que
   respeite o aninhamento; regex simples produz falso positivo em série.

3. AVISO DE DESATUALIZAÇÃO: eu rodei a primeira verificação contra a main e
   quase "corrigi" o Deng2023fedal que já estava corrigido na branch. Quem
   for verificar bib, verifique SEMPRE contra bibfix/lotes, não contra a main
   — a main está várias correções atrás.
