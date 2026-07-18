---
id: Roumeliotis2025
title: "LLMs for product classification in e-commerce: A zero-shot comparative study of GPT and Claude models"
authors: ["Roumeliotis, Konstantinos I.", "Tselikas, Nikolaos D.", "Nasiopoulos, Dimitrios K."]
year: 2025
venue: "Natural Language Processing Journal 11:100142"
doi: "10.1016/j.nlp.2025.100142"
pdf: referencias-pdf/Roumeliotis2025.pdf
paper_type: periodico
pillars: [P3]
status: fichado
datasets: [8-subconjuntos-248-categorias]
models: [gpt-4o, gpt-4o-mini, claude-3.5-sonnet, claude-3.5-haiku]
tasks: [classificacao-de-produtos]
falco_relation:
  - type: suporta
    target: claim-granularidade-e-E0
    note: "Zero-shot puro em taxonomia fechada de produtos: 248 categorias em 8
           subconjuntos (~31 cada), 20 amostras/categoria, 4 LLMs comerciais.
           Achado central: desempenho varia bastante ENTRE modelos mesmo em
           espaço fechado — reforça a necessidade do benchmarking por catálogo
           que o E0 instrumenta. Sem AL, sem custo instrumentado, sem PT-BR."
---

# Zero-shot GPT × Claude para produtos (Roumeliotis et al., 2025)

## Resumo
Estudo comparativo zero-shot de GPT-4o/mini e Claude 3.5 Sonnet/Haiku em
classificação de produtos com espaço fechado (248 categorias no total),
medindo acurácia/precisão/revocação/F1. Mostra variação relevante entre
famílias e portes de modelo na MESMA taxonomia — o "cardápio" de oráculos não
é intercambiável.

## Relação com a tese
Cap. 6 (ancoragem da granularidade: 248 vs nossas 621 num único espaço) e
plano 2.3.1. O E0 estende essa linha com pareamento estatístico, custo real e
efeito de instrumento — dimensões ausentes aqui.
