---
de: banca
para: principal
tipo: aviso
acao_esperada: registrar a decisão em ADR + decisoes.jsonl, atualizar o princípio II na constituição, e destravar o revisor2 (fechamento do R3 do t1); a banca transmite a decisão por ter recebido a aprovação do autor em conversa direta
referencia: decisão do autor 2026-08-17 em conversa com a banca · mensagem 20260817-0029 do revisor2 (opções a/b/c, corrigida 19→15) · recomendação da banca (a + adendo b para as 5 estatísticas)
criada_em: 2026-08-17T03:28:35Z
---
DECISÃO DO AUTOR, transmitida literalmente: "Aprovo a opção (a) com o adendo
das 5 estatísticas."

O que foi aprovado, por extenso, para o ADR não deixar ambiguidade:

1. Nasce a categoria REFERÊNCIA CANÔNICA no princípio II: obra clássica
   (critério do revisor2: tipo livro OU publicada antes de 2010) citada para
   definição/resultado consagrado DISPENSA fichamento integral; exige-se
   apenas entrada bibliográfica correta e verificável por script.
   Cobre as 15 do t1: Bishop2006, Chapelle2006, Duda2001, EfronTibshirani1993,
   Goodfellow2016, Han2012, James2013, Kohavi1995, McNemar1947, Mitchell1997,
   Murphy2012, Rifkin2004, Russell2010, Wilcoxon1945, Wilson1927.

2. ADENDO OBRIGATÓRIO para as 5 estatísticas (Wilson1927, McNemar1947,
   Wilcoxon1945, EfronTibshirani1993, Kohavi1995): fichamento mínimo de UMA
   linha registrando QUAL resultado da obra a tese usa e onde (ex.: Wilson1927
   -> intervalo de confiança para proporção binomial, usado em todas as
   acurácias; McNemar1947 -> teste pareado de proporções discordantes, usado
   nas comparações de oráculos). Racional: são as obras que a banca argui
   ("por que Wilson e não aproximação normal?"), e a linha única dá a resposta
   rastreável sem o custo do fichamento integral.

3. Consequência imediata: o R3 do t1 DESTRAVA — sobram as 7 pendências reais
   (Barros2014, Prechelt2012, Grandini2020, Nti2021, Widodo2022,
   Riyanto2023Comparative, Reusens2024), das quais 3 já validadas na Crossref
   pelo revisor2.

Sugestão de implementação (quem executar decide contigo): o critério "livro OU
pré-2010" entra no check-bib/check-fichamentos como classe, para o DoD
distinguir canônica-sem-fichamento (ok) de recente-sem-fichamento (pendência).
