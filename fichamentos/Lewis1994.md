---
id: Lewis1994
title: "A Sequential Algorithm for Training Text Classifiers"
authors: ["Lewis, David D.", "Gale, William A."]
year: 1994
venue: "SIGIR '94, pp. 3–12, Springer-Verlag"
doi: "10.1007/978-1-4471-2099-5_1"
pdf: referencias-pdf/Lewis1994.pdf
paper_type: metodo
pillars: [geral, P2]
status: fichado
proposes: [amostragem-por-incerteza, cenario-pool-based]
uses_methods: [classificador-probabilistico]
datasets: [newswire-categorization]
metrics: [reducao-de-rotulos]
tasks: [classificacao-de-texto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Origem do uncertainty sampling E do cenário pool-based — as duas escolhas
           estruturais do FALCO nasceram aqui, num problema de classificação de
           texto, o mesmo domínio da tese."
---

# A Sequential Algorithm for Training Text Classifiers

## Resumo
Artigo seminal que introduz o **uncertainty sampling**: um algoritmo de amostragem
sequencial em que o classificador estatístico corrente seleciona para rotulagem
manual os exemplos sobre os quais está mais incerto. Testado em categorização de
texto de agência de notícias (newswire). Resultado central: redução de **até
500 vezes** na quantidade de dados de treino que precisariam ser rotulados
manualmente para atingir um dado nível de eficácia, em comparação com o que seria
necessário de outra forma. Motivação explícita: "há frequentemente mais texto
disponível do que se pode rotular economicamente", logo é preciso escolher o
subconjunto a rotular — a formulação pool-based.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Uncertainty sampling reduz em até 500x os rótulos necessários para um dado nível de eficácia | Abstract | Cap.2 (marco histórico); baseline conceitual das fases de incerteza do FALCO |
| C2 | Rotular é o gargalo econômico da classificação de texto; amostragem aleatória é o default a bater | §1 | Motivação da tese (Cap.1); random é baseline obrigatório nos E1–E3 |
| C3 | A seleção usa o próprio classificador corrente (laço sequencial modelo→consulta) | Abstract/§1 | Estrutura do laço do FALCO |

## Números que posso citar
- Redução de até 500x nos rótulos necessários (newswire, classificador
  probabilístico) — citar como "até" (é o melhor caso reportado).

## Crítica / limitações (minha leitura)
- Tarefas binárias/poucas categorias com classificador probabilístico simples;
  o fator 500x não transfere para 621 classes desbalanceadas em texto curto.
- Oráculo humano perfeito; custo modelado apenas como quantidade de rótulos.

## Ideias que gera para a tese
- Abrir a seção de AL do Cap.2 com este artigo (1994) e fechar com LLM-como-oráculo
  (2023+): arco de 30 anos em que o custo migrou do rótulo humano para o token.
