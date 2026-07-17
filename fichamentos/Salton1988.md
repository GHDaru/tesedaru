---
id: Salton1988
title: "Term-Weighting Approaches in Automatic Text Retrieval"
authors: ["Salton, Gerard", "Buckley, Christopher"]
year: 1988
venue: "Information Processing & Management, 24(5), pp. 513–523"
doi: "10.1016/0306-4573(88)90021-0"
pdf: referencias-pdf/Salton1988.pdf
paper_type: metodo
pillars: [geral]
status: fichado
proposes: [tf-idf, ponderacao-de-termos]
uses_methods: [recuperacao-de-informacao]
datasets: []
metrics: []
tasks: [recuperacao-de-informacao]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Origem canônica do TF-IDF — base dos métodos argmax de Darú (2022/2024)
           e da representação esparsa do PVBin. Citação obrigatória da linha de
           representação vetorial do Cap.2."
---

# Term-Weighting Approaches in Automatic Text Retrieval

## Resumo
Artigo canônico da ponderação de termos: 20 anos de evidência experimental
mostram que indexação por termos únicos apropriadamente PONDERADOS supera
representações mais elaboradas, e que o resultado depende crucialmente do esquema
de ponderação. Consolida as componentes tf (frequência no documento), idf
(raridade na coleção) e normalização de comprimento, fornecendo os baselines de
indexação com que representações mais sofisticadas devem ser comparadas.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Termos únicos bem ponderados superam representações elaboradas em recuperação | Abstract | Cap.2 (representações esparsas); explica a força do baseline TF-IDF/argmax no nosso domínio |
| C2 | A escolha do esquema de ponderação é o fator crítico | Abstract | Ecoa o achado da dissertação Daru2024 (normalização L2 como fator dominante) |

## Números que posso citar
- (Clássico conceitual.)

## Crítica / limitações (minha leitura)
- Recuperação, não classificação; coleções de documentos longos — em texto curto
  o tf satura (quase todo termo aparece 1x), o que favorece a variante Binary
  (constatado em Daru2024).

## Ideias que gera para a tese
- Ligar C2→Daru2024-C2: a tradição de 1988 antecipa por que Binary vence em
  descrições curtas.
