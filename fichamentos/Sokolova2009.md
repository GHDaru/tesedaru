---
id: Sokolova2009
title: "A systematic analysis of performance measures for classification tasks"
authors: ["Sokolova, Marina", "Lapalme, Guy"]
year: 2009
venue: "Information Processing & Management, 45(4), pp. 427–437"
doi: "10.1016/j.ipm.2009.03.002"
pdf: referencias-pdf/Sokolova2009.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [analise-de-invariancia-de-metricas]
uses_methods: [analise-sistematica]
datasets: []
metrics: [acuracia, f1, macro-micro]
tasks: [avaliacao-de-classificadores]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "A referência das métricas usadas na tese (já citada na seção de
           avaliação do Cap.2): analisa 24 medidas em binário/multiclasse/
           multirrótulo/hierárquico via propriedades de invariância."
---

# A systematic analysis of performance measures for classification tasks

## Resumo
IPM 2009: análise sistemática de **24 medidas de desempenho** cobrindo
classificação binária, multiclasse, multirrótulo e hierárquica, relacionando cada
medida a invariâncias sob mudanças na matriz de confusão — base formal para
escolher métricas conforme o que se quer detectar/ignorar.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Métricas diferem por propriedades de invariância; a escolha deve ser justificada pela tarefa | Abstract | Já citada no Cap.2 (eqs. de acurácia/P/R/F1 e macro vs micro); o PDF dá lastro |
| C2 | Macro dá peso igual às classes; micro reflete as majoritárias | Corpo | Sustenta Macro-F1 como métrica principal sob desbalanceamento |

## Números que posso citar
- 24 medidas analisadas.

## Crítica / limitações (minha leitura)
- Nenhuma relevante — é exatamente a referência certa para a seção.

## Ideias que gera para a tese
- Nenhuma ação nova; PDF arquivado fecha a cadeia citação→fonte.
