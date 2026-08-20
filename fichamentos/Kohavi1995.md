---
id: Kohavi1995
title: "A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection"
authors: ["Kohavi, Ron"]
year: 1995
venue: "Proceedings of the 14th International Joint Conference on Artificial Intelligence (IJCAI), v. 2, pp. 1137--1143"

paper_type: canonica
status: ficha-minima
ficha_minima_motivo: "ADR 0012, adendo das estatísticas — obra canônica que a banca argui"

falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Protocolo de estimação de acurácia e seleção de modelo: validação
           cruzada estratificada como prática padrão, essencial sob
           desbalanceamento — condição do nosso espaço de 621 rótulos."
---

# Kohavi (1995) — ficha mínima

**O que a tese usa:** a recomendação de validação cruzada **estratificada** para
estimar acurácia e selecionar modelo, em vez de partição única ou bootstrap.

**Onde:** `2-fundam/texto.tex:125` (abre a lista de práticas empregadas na tese)
e `2-fundam/texto.tex:129` (a estratificação como essencial sob
desbalanceamento).

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Validação cruzada estratificada dá estimativa de acurácia com viés e variância melhores que partição única ou bootstrap para seleção de modelo | Kohavi (1995), pp. 1137--1143 | Sustenta o protocolo de avaliação, crítico sob a cauda longa dos 621 rótulos |

**Achado de bibliografia (NÃO corrigido aqui — o lock do `referencias.bib` é do
revisor1):** a entrada está declarada como `@article` com os anais do IJCAI no
campo `journal`. É trabalho de conferência: o tipo correto é `@inproceedings`
com `booktitle`. Do jeito que está, sai formatado como artigo de periódico na
lista final — mesmo defeito já registrado em `Zhu2009` e `Attenberg2010` na
verificação das 26 clássicas.

**Por que basta uma linha:** obra anterior a 2010 citada para prática
consagrada (ADR 0012, item 1 + adendo).
