---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Machado2026RetailPt
title: "Turning web data into official statistics: Classifying Portuguese retail products with NLP models"
authors: ["Machado, Juliana de Freitas Ulisses", "Veloso, Bruno"]
year: 2026
venue: "Statistical Journal of the IAOS, v. 42, n. 1, p. 122-136 (SAGE)"
doi: "10.1177/18747655251414407"
pdf: ""   # (preencher c/ PDF final) — artigo fechado, ver "Estado desta ficha"

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: avaliacao
pillars: [P1]
status: a-ler   # lido SÓ o resumo; ver "Estado desta ficha" antes de citar qualquer número

# ===== ENTIDADES =====
proposes: []
uses_methods: [fine-tuning, rotulagem-humano-no-laco]
datasets: [ecoicop-supermercados-pt]
metrics: [macro-f1]
tasks: [classificacao-de-texto]
models: [bertimbau, cnn-como-cabeca-de-classificacao]

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: [Souza2020BERTimbau]

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: complementa
    target: FALCO
    note: "É o trabalho mais próximo do FALCO em DOMÍNIO — descrição de produto
           de varejo em português, classificada em taxonomia oficial — e o mais
           distante em MÉTODO: rotulagem humana no laço, sem estratégia formal
           de aprendizado ativo e sem oráculo automatizado. A tese o usa em
           2-fundam:793-800 para corroborar a escolha do BERTimbau e para
           contrastar processo. Ver 'Estado desta ficha' antes de repetir
           qualquer número."
---

# Turning web data into official statistics: Classifying Portuguese retail products with NLP models

## Estado desta ficha — LEIA ANTES DE CITAR

**Só o resumo foi lido.** O artigo está atrás do paywall da SAGE (`doi.org`
devolve 403) e não localizei versão aberta: não há preprint em arXiv nem cópia
em repositório institucional que eu tenha encontrado. Por isso o `status` é
`a-ler` e não `fichado`, e o campo `pdf` está vazio.

Isto **não** é um fichamento completo. É o registro do que foi possível
verificar, e da verificação que a R4 do tema t5 pediu.

### O que a tese cita e o que se verifica

`2-fundam:793-800` usa quatro números deste artigo:

| Número na tese | Situação |
|---|---|
| "$\approx 100$ mil títulos" | **CONFERE** — o resumo diz "100,000 product titles" |
| "94,0\% de Macro F1 após ajuste" | **CONFERE** — "the transformer attains 94.00%" |
| "97,0\% de acurácia" | **NÃO VERIFICADO** — o resumo não reporta acurácia |
| "12 mil rótulos manuais" | **NÃO VERIFICADO** — o número não aparece no resumo |

Os dois primeiros podem ser citados. **Os dois últimos não devem ser citados
enquanto o PDF não chegar** — princípio V: número reportado tem de resolver
para artefato, e hoje eles não resolvem para nada.

Vale notar que o resumo reporta **macro-F1 para os dois modelos** e nenhuma
acurácia. Isso levanta a hipótese de que "97,0% de acurácia" tenha vindo do
corpo do artigo, ou de confusão com outra métrica. Não afirmo qual — afirmo que
não está no que eu pude ler.

### Imprecisão de escopo, que joga a favor da tese

A tese descreve o estudo como classificação de "títulos de supermercados
portugueses nas categorias ECOICOP". O resumo restringe: **"Portuguese food and
beverage items"**, de seis redes nacionais.

Não é o catálogo do supermercado — é o recorte de **alimentos e bebidas**.
Dizer isso torna o contraste com o FALCO **mais forte**, não mais fraco: nós
operamos sobre 621 classes de catálogo inteiro, com todas as categorias de
varejo.

### O que falta para fechar a ficha

Obter o PDF (o autor pode ter acesso institucional pela UFPR) e então:
localizar ou refutar os dois números pendentes; registrar o desenho do fluxo
"human-in-the-loop"; extrair a estrutura de classes ECOICOP usada; e verificar
se há comparação de custo de anotação, que é o que mais interessaria ao Cap. 6.

## Resumo (do que foi lido — apenas o resumo do artigo)
Treina dois modelos para classificar títulos de produtos de alimentação e
bebidas, obtidos por raspagem de seis redes de supermercado portuguesas, nas
categorias da ECOICOP (classificação europeia do consumo individual por
finalidade), com vista a alimentar estatística oficial de preços e inflação.
Compara uma rede convolucional leve com um BERTimbau ajustado, e o argumento
central é de compromisso entre custo computacional e desempenho: a rede leve
chega perto por uma fração do custo. Os modelos são publicados no Hugging Face;
os dados de origem permanecem confidenciais.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O BERTimbau ajustado atinge 94,00% de macro-F1 na classificação ECOICOP de produtos em português, primeiro resultado desse tipo para a língua | Resumo | 2-fundam:796 — corrobora a escolha do BERTimbau como classificador forte |
| C2 | Uma rede convolucional leve atinge 92,19% de macro-F1 com custo computacional mínimo — 1,8 ponto abaixo do transformer | Resumo | **Cap. 3**: é o mesmo compromisso custo-capacidade que justifica o nosso par de classificadores. Sustenta o desenho, e a tese ainda não o usa assim |
| C3 | A rotulagem foi feita por um fluxo "human-in-the-loop", sem estratégia formal de aprendizado ativo | Resumo ("labeled via a human-in-the-loop workflow") | 2-fundam:798-800 — sustenta a primeira metade da afirmação da tese |
| C4 | Entrega classificadores abertos e um fluxo de rotulagem replicável para cenário de poucos recursos | Resumo | Cap. 6: comparador de praticidade |

## Números que posso citar
**Somente estes dois**, ambos do resumo:
- **100.000** títulos de produtos, raspados de **seis** redes de supermercado
  portuguesas.
- Macro-F1: **94,00%** (BERTimbau ajustado) e **92,19%** (rede convolucional).

Os demais números que a tese atribui a este artigo estão na tabela do "Estado
desta ficha" e **não** podem ser citados por enquanto.

## Citações diretas (com página)
> "Using 100,000 product titles scraped from six national supermarket sites and
> labeled via a human-in-the-loop workflow, the CNN reaches a macro-F1 of
> 92.19 % with minimal computing cost, while the transformer attains 94.00 %,
> the first such result for Portuguese." (Resumo)

*(Sem página: só o resumo foi acessível.)*

## Crítica / limitações (minha leitura)
- **Alegação de primazia** ("the first such result for Portuguese", "the first
  open-source Portuguese ECOICOP classifiers"): é afirmação de ausência, do
  mesmo tipo que a R4 do t5 apontou na nossa própria seção de lacuna. Ao citar,
  **não repetir a alegação de primazia** — reportar o resultado, não o
  pioneirismo.
- **Dados de origem confidenciais**: o artigo publica os modelos, não os dados.
  Reprodutibilidade parcial, e vale registrar o contraste com o nosso princípio V.
- **Escopo estreito** (alimentos e bebidas) comparado ao catálogo completo do
  FALCO — ver acima.
- **Sem comparação com o custo de anotação**: pelo resumo, o compromisso medido
  é de custo COMPUTACIONAL (treino e inferência), não de custo de ANOTAÇÃO, que
  é a dimensão que a tese instrumenta. Confirmar quando o PDF chegar.

## Ideias que gera para a tese
- **Usar o C2 no Capítulo 3, e não só na revisão.** A diferença de 1,8 ponto de
  macro-F1 entre a rede leve e o transformer, no mesmo domínio e na mesma
  língua, é evidência externa direta para o par de classificadores que a tese
  adota. Hoje o artigo é citado só como corroboração do BERTimbau; ele sustenta
  mais do que isso.
- **Comparador de processo para o Capítulo 6**: os dois trabalhos resolvem o
  mesmo problema de domínio com processos opostos — rotulagem humana no laço
  contra oráculo LLM progressivo. É o contraste mais concreto que a tese tem
  para argumentar praticidade, e melhora quando o recorte de alimentos e
  bebidas for dito.
