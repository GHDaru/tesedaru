---
id: Raczkowska2024AlleNoise
title: "AlleNoise: large-scale text classification benchmark dataset with real-world label noise"
authors: ["Rączkowska, Alicja", "Osowska-Kurczab, Aleksandra", "Szczerbiński, Jacek", "Jasinska-Kobus, Kalina", "Nazarko, Klaudia"]
year: 2024
venue: "arXiv:2407.10992"
doi: "10.48550/arXiv.2407.10992"
pdf: referencias-pdf/Raczkowska2024AlleNoise.pdf
paper_type: preprint-benchmark
pillars: [P4]
status: fichado
proposes: [benchmark-ruido-real]
datasets: [AlleNoise]
metrics: [acuracia, robustez-a-ruido]
tasks: [classificacao-de-produtos]
compares_with: [Merdjanovska2024NoiseBench]
falco_relation:
  - type: suporta
    target: E4
    note: "502.310 títulos CURTOS de produtos, 5.692 categorias, 15% de ruído
           REAL instance-dependent de marketplace com rótulos limpos verificados.
           Mostra que métodos de learning-with-noisy-labels que funcionam com
           ruído sintético falham no real — nuance incorporada à leitura do E4.
           É o benchmark de réplica ideal para o FALCO (Cap. 6, futuros)."
---

# AlleNoise (Rączkowska et al., 2024)

## Resumo
Benchmark de classificação de texto em larga escala com ruído real: meio milhão
de títulos de produtos de e-commerce em 5.692 categorias, 15% de rótulos
ruidosos originados do marketplace (dependentes da instância), com versão limpa
verificada por especialistas. Métodos clássicos de robustez a ruído, eficazes
sob corrupção sintética, não resolvem o ruído real — semanticamente mais duro.

## Relação com a tese
Domínio-irmão do nosso (títulos curtos de produto, alta cardinalidade). Usado
em dois pontos: nuance do E4 (ruído uniforme como limite, não como realidade) e
alvo de réplica externa nos trabalhos futuros, ao lado do STOPS.

## Limitações
Inglês/polonês (não PT-BR); sem laço de AL — benchmark estático.
