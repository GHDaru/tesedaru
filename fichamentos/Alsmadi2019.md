---
id: Alsmadi2019
title: "Review of short-text classification"
authors: ["Alsmadi, Issa", "Gan, Keng Hoon"]
year: 2019
venue: "International Journal of Web Information Systems"
doi: "10.1108/IJWIS-12-2017-0083"
pdf: referencias-pdf/Alsmadi2019.pdf
paper_type: survey
pillars: [geral, P1]
status: fichado
proposes: [revisao-por-estagios-do-pipeline]
uses_methods: [selecao-de-atributos, algoritmo-genetico, soft-computing]
datasets: []
metrics: []
tasks: [classificacao-de-texto-curto]
models: []
extends: [Song2014]
compares_with: []
contradicts: []
builds_on: [Song2014]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Revisão de STC organizada por estágio do pipeline; aponta algoritmos
           genéticos como solução promissora para otimização em texto curto — eco
           direto do nosso P1 (otimização do L0 via AG)."
---

# Review of short-text classification

## Resumo
Revisão de classificação de texto curto (STC) estruturada pelos estágios da tarefa
de classificação (pré-processamento, representação/seleção de atributos,
classificação, avaliação), com as técnicas de cada estágio e tendências. Motivação:
explosão de documentos eletrônicos curtos (redes sociais) e aplicações como
filtragem de spam, análise de sentimento e revisão de clientes. Findings
declarados: as soluções correntes ainda têm desempenho baixo; problemas de baixo
desempenho podem ser atacados com soluções otimizadas, como **algoritmos
genéticos** ("poderosos para melhorar a qualidade dos atributos selecionados") e
soft computing/lógica fuzzy.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | STC é etapa essencial de muitas aplicações, mas revisões dedicadas são escassas | Abstract (Purpose) | Cap.1: relevância do recorte em texto curto |
| C2 | Desempenho corrente em STC é baixo; há espaço para otimização | Abstract (Findings/Value) | Justificativa de pesquisa (Cap.1) |
| C3 | Algoritmos genéticos são apontados como solução poderosa de otimização em STC | Abstract (Findings) | Respaldo bibliográfico do P1 (AG para otimizar o conjunto inicial L0) — a literatura de STC já apontava AG como direção |

## Números que posso citar

- **Limiar de 200 caracteres** para texto curto, com a condição exata: a
  afirmação é sobre **publicações e comentários de redes sociais**, e o 140 é o
  exemplo do Twitter à época do artigo.

  > "Millions of short text are produced daily in the form of posts or comments.
  > This type of document tends to have a length of no more than 200
  > characters; for example, Twitter posts consists of up to 140 characters."
  > (§1, Introdução, **p. 2** de 29)

  Usado em `2-fundam/texto.tex:737`, na definição de texto curto. **Condição que
  a tese precisa respeitar ao citar:** o número descreve microblog, e o corpus
  desta tese é **descrição de produto de varejo** — o limiar transfere como
  ordem de grandeza da literatura, não como propriedade medida da nossa base. A
  contagem da nossa base é do Capítulo~\ref{ch:metodo} e não depende desta obra.

- (No mais, revisão qualitativa; 89 referências.)

**Procedência deste registro:** o R5 do principal acusou o número como sem
lastro na ficha; o autor localizou a passagem no PDF e o principal me despachou
o registro (tarefa 20260817-1855). **Eu confirmei a passagem e a página abrindo
o PDF** — não a copiei do relato: a busca no arquivo devolve a frase na p. 2, e
o contexto ao redor (redes sociais, posts e comentários) é o que fixa a condição
acima.

## Crítica / limitações (minha leitura)
- Foco em redes sociais/microblogs, não em descrições de produto; pré-BERT (2019,
  mas sem transformers).
- O endosso a AG (C3) é genérico (seleção de atributos), não idêntico ao nosso uso
  (seleção de instâncias iniciais) — citar com essa distinção explícita.

## Ideias que gera para a tese
- Usar a organização por estágios como checklist da seção de STC do Cap.2 e
  posicionar onde o FALCO intervém (rotulagem, não representação).
