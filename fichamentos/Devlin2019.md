---
id: Devlin2019
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
authors: ["Devlin, Jacob", "Chang, Ming-Wei", "Lee, Kenton", "Toutanova, Kristina"]
year: 2019
venue: "Proceedings of NAACL-HLT 2019, pp. 4171–4186"
doi: "10.18653/v1/N19-1423"
pdf: referencias-pdf/Devlin2019.pdf
paper_type: metodo
pillars: [P4]
status: fichado
proposes: [bert, masked-language-model, fine-tuning-com-uma-camada]
uses_methods: [transformer, pre-treinamento-nao-supervisionado]
datasets: [glue, squad, multinli]
metrics: [glue-score, f1]
tasks: [compreensao-de-linguagem]
models: [bert]
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Base arquitetural do classificador-alvo: BERTimbau (usado nos E2/E3 via
           HuggingFace) é um BERT pré-treinado em português. O paradigma
           pré-treino + fine-tuning é o que torna o AL viável com poucos rótulos."
---

# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

## Resumo
Introduz o BERT (Bidirectional Encoder Representations from Transformers):
pré-treinamento de representações profundas **bidirecionais** a partir de texto
não-rotulado, condicionando simultaneamente nos contextos esquerdo e direito em
todas as camadas (via masked language model + next sentence prediction). O modelo
pré-treinado pode ser ajustado (fine-tuned) com **apenas uma camada adicional de
saída** para obter estado da arte em ampla gama de tarefas, sem modificações
arquiteturais específicas. Resultados: novo estado da arte em 11 tarefas de PLN —
GLUE 80,5% (+7,7 p.p. absolutos), MultiNLI 86,7% (+4,6), SQuAD v1.1 F1 93,2
(+1,5), SQuAD v2.0 F1 83,1 (+5,1).

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Pré-treino bidirecional + fine-tuning raso atinge SOTA em 11 tarefas | Abstract | Cap.2 (fundamentos); justifica escolher um encoder BERT como classificador-alvo |
| C2 | O conhecimento vem do pré-treino em texto não-rotulado; a tarefa-alvo precisa de poucos dados | Abstract/§1 | Sinergia com AL: fine-tuning com poucos rótulos é exatamente o regime das iterações do FALCO |

## Números que posso citar
- GLUE 80,5% (+7,7 p.p.); MultiNLI 86,7%; SQuAD v1.1 F1 93,2; SQuAD v2.0 F1 83,1.

## Crítica / limitações (minha leitura)
- Inglês; para português usamos BERTimbau (Souza et al., 2020) — conferir se a
  entrada BibTeX do BERTimbau está em referencias.bib (usar via HuggingFace, sem
  fork, conforme decisão de projeto).
- Textos curtos de produto (~20–40 caracteres, abreviações) estão longe da
  distribuição de pré-treino; tokenização subword de abreviações (CERV, REFR) é um
  risco a discutir no E2.

## Ideias que gera para a tese
- No Cap.2, encadear: BERT (C1) → BERTimbau (português) → por que fine-tuning com
  poucos rótulos torna o AL atrativo (C2) → FALCO fecha o ciclo com oráculo LLM.
