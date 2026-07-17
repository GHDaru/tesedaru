---
id: song2014shorttext
title: "Short Text Classification: A Survey"
authors: ["Song, Ge", "Ye, Yunming", "Du, Xiaolin", "Huang, Xiaohui", "Bie, Shifu"]
year: 2014
venue: "Journal of Multimedia, 9(5), pp. 635–643"
doi: "10.4304/jmm.9.5.635-643"
pdf: referencias-pdf/song2014shorttext.pdf
paper_type: survey
pillars: [geral]
status: fichado
proposes: [caracterizacao-de-texto-curto]
uses_methods: [analise-semantica, semi-supervisao, ensemble]
datasets: []
metrics: []
tasks: [classificacao-de-texto-curto]
models: []
extends: []
compares_with: []
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Define as quatro dificuldades canônicas do texto curto (esparsidade,
           larga escala, imediatismo, não-padronização) — a caracterização do
           nosso objeto de estudo (descrições de produto ~20–40 caracteres)."
---

# Short Text Classification: A Survey

## Resumo
Survey dedicado à classificação de texto curto (PDF: versão avulsa do artigo, substituída no saneamento de 17/07/2026).
Caracteriza o gênero "texto curto" (mensagens instantâneas, títulos de BBS,
comentários, SMS, tweets) e suas dificuldades intrínsecas: **esparsidade**
(palavras de menos para representar o espaço de atributos), **larga escala**,
**imediatismo** e **não-padronização** — métodos tradicionais falham porque o
texto não provê coocorrência/contexto compartilhado suficiente para boa medida de
similaridade. Revisa as famílias de solução: análise semântica (enriquecimento),
classificação semi-supervisionada, ensembles e classificação em tempo real, além
das formas de avaliação.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Texto curto tem 4 dificuldades: esparsidade, escala, imediatismo, não-padronização | Abstract/§I | Cap.1 e Cap.2: caracterizar nosso dataset (descrições com abreviações = não-padronização extrema) |
| C2 | Poucas palavras não representam o espaço de atributos nem a relação palavra-documento | Abstract | Motiva representações densas (BERTimbau) sobre BoW; e o campo `expanded_description` do nosso prompt (expansão de abreviações como enriquecimento) |
| C3 | Enriquecimento semântico é a família clássica de mitigação | Abstract | Ligar ao nosso prompt v3: a expansão de abreviações pelo LLM é enriquecimento semântico embutido no oráculo |

## Números que posso citar
- (Survey de 2014; usar caracterização qualitativa.)

## Crítica / limitações (minha leitura)
- Anterior a embeddings contextuais e LLMs; as soluções revisadas (enriquecimento
  via Wikipedia/ontologias) foram superadas, mas o DIAGNÓSTICO (C1/C2) permanece
  válido e é o que citamos.
- Nada sobre português nem sobre descrições de produto de varejo.

## Ideias que gera para a tese
- Enquadrar o `expanded_description` do prompt do oráculo como herdeiro direto da
  linha de enriquecimento semântico (C3) — de ontologias externas para o
  conhecimento paramétrico do LLM.
