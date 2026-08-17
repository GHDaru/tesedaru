---
id: Settles2012
title: "Active Learning (Synthesis Lectures on AI and ML)"
authors: ["Settles, Burr"]
year: 2012
venue: "Morgan & Claypool, Synthesis Lectures on Artificial Intelligence and Machine Learning"
doi: "10.2200/S00429ED1V01Y201207AIM018"
pdf: referencias-pdf/Settles2012.pdf
paper_type: livro
pillars: [geral, P2]
status: fichado
proposes: [taxonomia-de-cenarios-de-al, frameworks-de-selecao-de-consulta]
uses_methods: [amostragem-por-incerteza, query-by-committee, densidade]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: [Angluin1988, Cohn1994Improving, Lewis1994]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Referência canônica de AL: define o laço consulta→oráculo→treino e os
           frameworks de seleção que o FALCO combina por fase. É a fonte da
           terminologia (pool-based, uncertainty sampling) usada em toda a tese."
---

# Active Learning (Settles, 2012)

## Resumo
Monografia introdutória canônica de aprendizado ativo. Ideia central declarada na
abertura: um algoritmo de aprendizado pode desempenhar melhor com menos treino se
puder ESCOLHER os dados dos quais aprende, formulando consultas a um "oráculo"
(ex.: anotador humano) — bem motivado quando não-rotulados abundam e rótulos são
caros. Organiza os cenários de consulta (membership query synthesis, stream-based,
pool-based) e os algoritmos de seleção em quatro grandes "frameworks de seleção de
consulta" (incerteza, query-by-committee/espaço de hipóteses, mudança esperada de
modelo/redução de erro, e métodos ponderados por densidade), toca nos fundamentos
teóricos e fecha com forças/fraquezas práticas e desafios abertos.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Aprendiz que escolhe seus dados atinge mesmo desempenho com menos rótulos | Abstract/cap.1 | Premissa de TODO o trabalho; abre o Cap.2 |
| C2 | O oráculo é definido como entidade que "já entende a natureza do problema" (tipicamente humano) | Abstract | Contraste direto com o oráculo LLM ruidoso do FALCO — a definição clássica assume oráculo confiável |
| C3 | Quatro frameworks de seleção organizam o campo (incerteza, QBC, mudança esperada, densidade) | Estrutura do livro | Taxonomia-base do Cap.2; FALCO usa incerteza+densidade por fase |
| C4 | Pool-based é o cenário dominante em aplicações com texto | Cap. de cenários | Justifica o recorte pool-based da tese |

## Números que posso citar
- (Livro conceitual; usar como fonte de definições, não de números.)

## Crítica / limitações (minha leitura)
- Pré-deep learning e pré-LLM: oráculo humano perfeito é suposição estrutural;
  ruído de anotação é tratado como exceção (§ de anotadores falíveis), não como
  regime padrão — exatamente o que o FALCO inverte.
- Cold-start é reconhecido mas pouco resolvido (depende de semente aleatória) —
  lacuna que o P1 (otimização do L0) ataca.

## Ideias que gera para a tese
- Definir formalmente o oráculo do FALCO como relaxamento do oráculo de Settles:
  O: X → Y ∪ {⊥} com taxa de erro ε e custo c por consulta (tabela comparativa).
- Mapear cada fase do FALCO ao framework correspondente de Settles (C3) — mesma
  tabela sugerida no fichamento do zhang-etal-2022-survey; unificar.
