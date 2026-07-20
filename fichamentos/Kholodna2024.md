---
id: Kholodna2024
title: "LLMs in the Loop: Leveraging Large Language Model Annotations for Active Learning in Low-Resource Languages"
authors: ["Kholodna, Nataliia", "Julka, Sahib", "Khodadadi, Mohammad", "Gumus, Muhammed Nurullah", "Granitzer, Michael"]
year: 2024
venue: "arXiv:2404.02261"
doi: "10.48550/arXiv.2404.02261"
pdf: referencias-pdf/Kholodna2024.pdf
paper_type: preprint
pillars: [P3]
pillars_nota: adjacente (NER, não classificação curta)
status: fichado
proposes: [selecao-de-anotador-llm, anotacao-em-lote]
uses_methods: [llm-como-oraculo, amostragem-por-incerteza]
datasets: [MasakhaNER-2.0]
metrics: [f1, custo-por-rotulo, correcao-de-formato]
models: [gpt-4-turbo, afroxlmr-mini]
compares_with: [Rouzegar2024Thesis]
falco_relation:
  - type: suporta
    target: RQ2-lote
    note: "Precedente direto da anotação em LOTE no laço de AL com LLM: mostra a
           amortização do prompt como componente central da economia (>=42x vs
           humano). Também mede 'output format correctness' — antecipa nosso
           achado de que erro de formato != erro semântico (taxa de inválidos)."
---

# LLMs in the Loop (Kholodna et al., 2024)

## Resumo
Laço de AL para NER em 20 línguas africanas de baixo recurso: um AfroXLMR-mini
treina com 5% de seed; a cada iteração os 5% mais incertos vão ao LLM anotador.
Fase prévia SELECIONA o anotador entre vários LLMs por acordo com um gabarito
pequeno (vence GPT-4-Turbo). Anotação em lote (vários exemplos por prompt)
reduz tokens de overhead. Economia estimada >=42,45x frente à anotação humana.

## Relação com a tese
Cita-se no Cap. 5 (RQ2/lote) como precedente da calibração de lote do E0 e no
plano do Cap. 2 (2.3.2/2.3.4). A seleção prévia de oráculo é análoga ao nosso
E0-como-gate; diferimos por espaço fechado de 621 classes e instrumentação de
cache/custo por anotação individual.

## Limitações
NER (não classificação); custo humano estimado, não medido; sem análise de
efeito do instrumento de saída.
