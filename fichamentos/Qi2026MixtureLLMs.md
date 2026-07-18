---
id: Qi2026MixtureLLMs
title: "Next Generation Active Learning: Mixture of LLMs in the Loop"
authors: ["Qi, Yuanyuan", "Yang, Xiaohao", "Lu, Jueqing", "Guo, Guoxiang", "Enticott, Joanne", "Liu, Gang", "Du, Lan"]
year: 2026
venue: "AAAI 40(29):24909-24917"
doi: "10.1609/aaai.v40i29.39678"
pdf: referencias-pdf/Qi2026MixtureLLMs.pdf
paper_type: conferencia
pillars: [P3, P4]
status: fichado
proposes: [mixture-of-llms-anotador, discrepancia-de-anotacao, negative-learning]
datasets: [AGNews, IMDB, TREC, PubMed]
models: [gemma-2-9b, llama-3.1-8b, mistral-7b, qwen2.5-7b, yi-1.5-9b]
falco_relation:
  - type: compete
    target: FALCO-fases
    note: "O mais próximo de 'oráculo progressivo' na literatura 2026: troca o
           anotador único por MISTURA de 5 LLMs leves LOCAIS (human-free, sem
           rate limit de API), com discrepância e negative learning como
           robustez. FALCO difere: progressão SEQUENCIAL por fases com gate de
           custo, espaço de 621 classes, instrumentação de medição."
---

# Mixture of LLMs in the Loop (Qi et al., AAAI 2026)

## Resumo
Substitui o anotador humano por um modelo de anotação baseado em mistura de
cinco LLMs leves treinada sobre o seed, com dois mecanismos de robustez:
discrepância entre modelo de AL e anotador, e aprendizado negativo com rótulos
improváveis. Totalmente local — troca custo de API por infraestrutura.

## Relação com a tese
Posicionado nos futuros (composição de oráculos) e na revisão 2.5; contraste
central com a progressão sequencial de oráculos do FALCO.

## Limitações
4-6 classes por dataset; sem contabilidade de custo por rótulo.
