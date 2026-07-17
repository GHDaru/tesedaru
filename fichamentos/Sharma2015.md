---
id: Sharma2015
title: "Active Learning with Rationales for Text Classification"
authors: ["Sharma, Manali", "Zhuang, Di", "Bilgic, Mustafa"]
year: 2015
venue: "NAACL-HLT 2015, pp. 441–451"
doi: "10.3115/v1/N15-1047"
pdf: referencias-pdf/Sharma2015.pdf
paper_type: metodo
pillars: [P3]
status: fichado
proposes: [al-com-racionais]
uses_methods: [aprendizado-ativo, racionais-de-anotadores]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Lewis1994]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "O oráculo devolve MAIS que o rótulo: racionais (trechos justificativos)
           incorporáveis ao treino. Precedente humano direto do nosso campo
           rationale/expanded_description no JSON do oráculo LLM."
---

# Active Learning with Rationales for Text Classification

## Resumo
NAACL 2015: abordagem simples para incorporar **racionais** (justificativas
elicitadas dos anotadores — ex.: termos que motivaram o rótulo) ao treino de
classificadores off-the-shelf (Naive Bayes, regressão logística, SVM), melhorando
o AL para texto. A anotação deixa de ser só um rótulo e vira rótulo+explicação.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Racionais de anotadores melhoram o AL além do rótulo puro | Abstract | Cap.2: precedente do nosso schema com rationale/expanded_description; abre a questão (futura) de USAR essas explicações no treino, não só na auditoria |

## Números que posso citar
- (Benchmarks de texto; qualitativo.)

## Crítica / limitações (minha leitura)
- Racionais humanos custam tempo extra; no FALCO o LLM os produz de graça — mas
  sem garantia de fidelidade (racional pode ser confabulado; discutir no Cap.5).

## Ideias que gera para a tese
- E3+: experimento futuro usando expanded_description como atributo auxiliar do
  classificador (destilação de racional) — anotar em trabalhos futuros.
