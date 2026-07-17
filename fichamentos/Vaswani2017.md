---
id: Vaswani2017
title: "Attention Is All You Need"
authors: ["Vaswani, Ashish", "Shazeer, Noam", "Parmar, Niki", "Uszkoreit, Jakob", "Jones, Llion", "Gomez, Aidan N.", "Kaiser, Łukasz", "Polosukhin, Illia"]
year: 2017
venue: "NeurIPS 2017 (Advances in Neural Information Processing Systems 30)"
doi: ""
pdf: referencias-pdf/Vaswani2017.pdf
paper_type: metodo
pillars: [geral, P4]
status: fichado
proposes: [transformer, self-attention]
uses_methods: [atencao, encoder-decoder]
datasets: [wmt14]
metrics: [bleu]
tasks: [traducao-automatica]
models: [transformer]
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "A arquitetura de TUDO que a tese usa: BERTimbau (encoder Transformer)
           e os próprios LLMs-oráculo (decoders Transformer). Uma citação, duas
           pontas do FALCO."
---

# Attention Is All You Need

## Resumo
Propõe o Transformer: arquitetura de transdução de sequências baseada
exclusivamente em mecanismos de atenção, dispensando recorrência e convoluções.
Superior em qualidade nas tarefas de tradução WMT14, mais paralelizável e
significativamente mais rápido de treinar que os modelos recorrentes/convolutivos
com atenção então dominantes.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Atenção pura substitui recorrência/convolução com ganho de qualidade e paralelismo | Abstract | Cap.2: base arquitetural de BERT/BERTimbau (encoder) e dos LLMs-oráculo (decoder) |

## Números que posso citar
- (Os BLEU de WMT14 não interessam à tese; citar arquiteturalmente.)

## Crítica / limitações (minha leitura)
- Nenhuma relevante ao nosso uso — é citação de arquitetura.

## Ideias que gera para a tese
- Observação elegante para o Cap.2: classificador-alvo e oráculo do FALCO são o
  MESMO bloco arquitetural em papéis opostos (encoder que entende vs decoder que
  gera) — a tese mede a colaboração entre as duas metades do Transformer.
