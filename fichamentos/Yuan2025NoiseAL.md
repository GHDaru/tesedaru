---
id: Yuan2025NoiseAL
title: "Hide and Seek in Noise Labels: Noise-Robust Collaborative Active Learning with LLM-Powered Assistance"
authors: ["Yuan, Bo", "Chen, Yulin", "Zhang, Yin", "Jiang, Wei"]
year: 2025
venue: "arXiv:2504.02901"
doi: "10.48550/arXiv.2504.02901"
pdf: referencias-pdf/Yuan2025NoiseAL.pdf
paper_type: preprint
pillars: [P3, P4]
status: fichado
proposes: [filtragem-colaborativa-de-ruido, llm-sob-demanda]
uses_methods: [dois-modelos-pequenos-como-filtro, separacao-dinamica-limpo-ruidoso]
datasets: [TREC]
metrics: [acuracia, tokens, custo-usd]
falco_relation:
  - type: estende
    target: E4-futuros
    note: "Aciona o LLM anotador SÓ onde a probabilidade de ruído é alta (small
           models filtram) — contabilidade rara de tokens/custo (25.990 tokens,
           US$0,39 em TREC 20% simétrico). Citado nos trabalhos futuros como
           extensão natural do E4: correção colaborativa em vez de descarte."
---

# NoiseAL / Hide and Seek in Noise Labels (Yuan et al., 2025)

## Resumo
AL robusto a ruído com assistência de LLM: dois modelos pequenos filtram o
conjunto rotulado, um critério dinâmico separa exemplos limpos de ruidosos, e o
LLM é consultado apenas nos suspeitos — transformando o oráculo forte em
recurso pontual, não em anotador universal. Testa ruído sintético 20/40%
simétrico e assimétrico em classificação multiclasse.

## Relação com a tese
Nos futuros do Cap. 6: os 2-4% de inválidos e o erro estruturado do nosso
oráculo poderiam ser tratados por esse mecanismo em vez de contados como perda.

## Limitações
Ruído majoritariamente sintético (ver NoiseBench); poucas classes.
