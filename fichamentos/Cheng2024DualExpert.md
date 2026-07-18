---
id: Cheng2024DualExpert
title: "E-Commerce Product Categorization with LLM-based Dual-Expert Classification Paradigm"
authors: ["Cheng, Zhu", "Zhang, Wen", "Chou, Chih-Chi", "Jau, You-Yi", "Pathak, Archita", "Gao, Peng", "Batur, Umit"]
year: 2024
venue: "CustomNLP4U @ EMNLP 2024"
doi: "10.18653/v1/2024.customnlp4u-1.22"
pdf: referencias-pdf/Cheng2024DualExpert.pdf
paper_type: workshop
pillars: [P3]
status: fichado
proposes: [dual-expert, contracao-top-k]
tasks: [classificacao-de-produtos]
falco_relation:
  - type: estende
    target: FALCO-futuros
    note: "Arquitetura de dois especialistas p/ taxonomias amplas: especialista
           de domínio fine-tuned reduz o espaço a top-K candidatos; LLM
           generalista decide entre eles. Citado nos futuros como desenho
           complementar para as 621 classes (contração antes do oráculo forte)."
---

# Dual-Expert Product Categorization (Cheng et al., 2024)

## Resumo
Sistema de categorização de produtos em duas etapas: um modelo especializado
propõe top-K categorias; um LLM generalista escolhe a final combinando
conhecimento local e geral. Foco em arquitetura e eficiência de pipeline, não
em AL formal.

## Relação com a tese
Instância pronta da ideia "oráculo fraco/barato -> oráculo forte" aplicada a
produto; entra em 2.3.2 e nos futuros (contração top-K).

## Limitações
Sem orçamento de rotulagem/AL; detalhes de dataset proprietário (Amazon).
