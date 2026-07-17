---
id: Forman2010
title: "Apples-to-Apples in Cross-Validation Studies: Pitfalls in Classifier Performance Measurement"
authors: ["Forman, George", "Scholz, Martin"]
year: 2010
venue: "ACM SIGKDD Explorations, 12(1), pp. 49–57"
doi: "10.1145/1882471.1882479"
pdf: referencias-pdf/Forman2010.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [f1-agregado-corretamente-em-cv]
uses_methods: [validacao-cruzada]
datasets: []
metrics: [f1, auc]
tasks: [avaliacao-de-classificadores]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Armadilhas de computar F1/AUC em validação cruzada (formas
           incompatíveis entre papers/software): diretamente aplicável a como
           agregamos Macro-F1 entre dobras/repetições nos E1–E3. (Arquivo veio
           rotulado como Forman 2003; identidade corrigida.)"
---

# Apples-to-Apples in Cross-Validation Studies

## Resumo
SIGKDD Explorations 2010: há diferenças sutis e INCOMPATÍVEIS em como acurácia,
F-measure e AUC são computadas em estudos com validação cruzada (agregar por
dobra vs agregar contagens; tratamento de dobras degeneradas), gerando
inconsistência na literatura e em pacotes de software.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O modo de agregar F1 entre dobras muda o número reportado | Abstract | Cap.3: especificar explicitamente como agregamos Macro-F1 (por rodada, depois média entre seeds) — e citar isto |

## Números que posso citar
- (Metodológico.)

## Crítica / limitações (minha leitura)
- Nenhuma para nosso uso; é um lembrete metodológico valioso e pouco citado.

## Ideias que gera para a tese
- Uma frase na metodologia + rodapé: previne questionamento de banca sobre
  comparabilidade dos nossos números com a literatura.
