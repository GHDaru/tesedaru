---
id: Paulucio2020
title: "Product Categorization by Title Using Deep Neural Networks as Feature Extractor"
authors: ["Paulucio, Leonardo S.", "Paixão, Thiago M.", "Berriel, Rodrigo F.", "De Souza, Alberto F.", "Badue, Claudine", "Oliveira-Santos, Thiago"]
year: 2020
venue: "IJCNN 2020, IEEE"
doi: "10.1109/IJCNN48605.2020.9207093"
pdf: referencias-pdf/Paulucio2020.pdf
paper_type: avaliacao
pillars: [geral, P4]
status: fichado
proposes: [dnn-como-extrator-de-atributos]
uses_methods: [deep-learning, extracao-de-atributos]
datasets: [mercado-libre-20m]
metrics: [acuracia-balanceada]
tasks: [classificacao-de-produtos-e-servicos, classificacao-de-texto-curto]
models: []
extends: []
compares_with: [Karl2023]
contradicts: []
builds_on: []
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Grupo brasileiro (UFES) no MESMO problema — categorizar produtos pelo
           título — em escala Mercado Libre (20M, espanhol/português). Confirma
           as características do domínio (desbalanceamento, rótulos não
           confiáveis) e dá um número de referência: 86,57% de acurácia
           balanceada com supervisão total em massa."
---

# Product Categorization by Title Using DNNs as Feature Extractor

## Resumo
Sistema de categorização automática de produtos **usando apenas os títulos**
(IJCNN 2020, grupo UFES). Uma rede profunda estado-da-arte extrai atributos dos
títulos, que alimentam diferentes classificadores. Avaliado no dataset
**Mercado Libre em larga escala: 20 milhões de amostras**, com "características
comuns de problemas do mundo real: classes desbalanceadas e rótulos não
confiáveis". Resultado: **acurácia balanceada de 86,57%** no split local de
teste, superando o 4º lugar da competição pública.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Categorização de produto por título é problema real em escala industrial (20M amostras) | Abstract | Cap.1: relevância econômica do nosso domínio, com exemplo latino-americano |
| C2 | O domínio tem desbalanceamento e RÓTULOS NÃO CONFIÁVEIS como características intrínsecas | Abstract | Valida nossa auditoria (conflitos de gold 0,7%, teto ~99,3%) como típica do domínio, não defeito da nossa base |
| C3 | 86,57% de acurácia balanceada com 20M rótulos disponíveis | Abstract | Referência de teto do domínio sob supervisão em massa — contraste com a pergunta do FALCO (o que se atinge com ≤30% de rótulos LLM?) |

## Números que posso citar
- Mercado Libre: 20.000.000 amostras; acurácia balanceada 86,57% (split local).

## Crítica / limitações (minha leitura)
- Supervisão total com dados massivos — o oposto do nosso regime de escassez; a
  comparação é de contexto, não de método.
- Acurácia balanceada ≈ Macro-Recall: métrica próxima mas não idêntica ao nosso
  Macro-F1; cuidado ao comparar números diretamente.

## Ideias que gera para a tese
- Usar C2 como blindagem da auditoria da base no Cap.3: literatura independente
  descreve rótulos não confiáveis como característica padrão de catálogos.
