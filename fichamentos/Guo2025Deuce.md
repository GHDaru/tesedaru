---
id: Guo2025Deuce
title: "DEUCE: Dual-diversity Enhancement and Uncertainty-awareness for Cold-start Active Learning"
authors: ["Guo, Jiaxin", "Chen, C. L. Philip", "Li, Shuzhen", "Zhang, Tong"]
year: 2024
venue: "TACL 12:1736-1754"
doi: "10.1162/tacl_a_00731"
pdf: referencias-pdf/Guo2025Deuce.pdf
paper_type: periodico
pillars: [P2]
status: fichado
proposes: [dual-neighbor-graph, diversidade-textual+de-classe, propagacao-de-incerteza]
datasets: [IMDb, Yelp, AGNews, Yahoo, DBpedia, TREC]
falco_relation:
  - type: compete
    target: DRI-SL
    note: "Referência mais forte de cold start em classificação textual: combina
           diversidade TEXTUAL e diversidade de CLASSE PREVISTA num grafo dual,
           contra o 'missed cluster effect'. Seeds de 32/64/128. O DRI-SL difere:
           sem PLM, custo linear, novidade LEXICAL explícita, e validado contra
           envelope evolutivo em 100..5000. A DRI-SL-C (grupos = classes
           previstas) aproxima-se do espírito class-aware do DEUCE."
---

# DEUCE (Guo et al., TACL 2024)

## Resumo
Cold start sem rótulos: constrói um Dual-Neighbor Graph com embeddings e
predições de PLMs, equilibrando diversidade textual e de classe prevista com
propagação de incerteza, para escolher o seed set antes de qualquer anotação.
Evita seeds redundantes e clusters de classes fracas perdidos na largada.

## Relação com a tese
Posicionamento direto do DRI-SL no Cap. 2 (2.5.2) e inspiração convergente da
variante DRI-SL-C do E6 (agrupamento class-aware).

## Limitações
Depende de PLM para embeddings/predições; seeds pequenos (<=128) vs nossos
b0 de centenas.
