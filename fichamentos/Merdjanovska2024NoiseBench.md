---
id: Merdjanovska2024NoiseBench
title: "NoiseBench: Benchmarking the Impact of Real Label Noise on Named Entity Recognition"
authors: ["Merdjanovska, Elena", "Aynetdinov, Ansar", "Akbik, Alan"]
year: 2024
venue: "EMNLP 2024"
doi: ""
pdf: referencias-pdf/Merdjanovska2024NoiseBench.pdf
paper_type: conferencia
pillars: [P4]
pillars_nota: adjacente (NER)
status: fichado
proposes: [benchmark-6-tipos-ruido-real]
compares_with: [Raczkowska2024AlleNoise]
falco_relation:
  - type: contradiz-parcial
    target: E4-leitura
    note: "Braço explícito de RUÍDO DE LLM entre 6 variantes reais (especialista,
           crowd, weak supervision...). Real >> sintético em dificuldade. Motivou
           a nuance honesta no Cap. 5: nossa extrapolação 'estruturado é mais
           benigno' fica condicionada à anatomia do RQ3, não é lei geral."
---

# NoiseBench (Merdjanovska et al., EMNLP 2024)

## Resumo
A partir de um corpus NER limpo, constrói seis variantes com ruído REAL: erros
de especialistas, crowdsourcing, anotação automática, weak supervision e ruído
de LLM. Demonstra que o ruído real degrada modelos muito mais que as corrupções
sintéticas usadas na literatura de noisy labels, e que os métodos atuais estão
longe do teto teórico sob ruído realista.

## Relação com a tese
Contraponto metodológico citado no E4: impede a generalização fácil de que
ruído estruturado é sempre benigno; nossa leitura fica ancorada na anatomia
específica do RQ3 (confusões semanticamente adjacentes, parte defensável).

## Limitações
NER; taxa de ruído fixa por variante; sem AL.
