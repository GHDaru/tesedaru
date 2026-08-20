---
id: Donmez2009
title: "Efficiently Learning the Accuracy of Labeling Sources for Selective Sampling"
authors: ["Donmez, Pinar", "Carbonell, Jaime G.", "Schneider, Jeff"]
year: 2009
venue: "KDD 2009, pp. 259-268"
doi: "10.1145/1557019.1557053"
pdf: referencias-pdf/Donmez2009.pdf
paper_type: conferencia
pillars: [p3-oraculo]
status: fichado
proposes: [iethresh, estimacao-de-acuracia-de-anotadores, selecao-de-anotador]
builds_on: [Donmez2008]
falco_relation:
  - type: fundamenta
    target: multiplos-oraculos
    note: "Aprende a acurácia de múltiplas fontes de rotulagem DURANTE o laço
           (IEThresh: intervalos de confiança sobre a taxa de acerto estimada
           de cada anotador) e roteia consultas para as fontes confiáveis.
           Citado na Seção 2.2.3; é o antecedente formal da seleção de
           oráculo do FALCO — que substitui a estimação online pela medição
           pré-registrada do E0 (acurácia + custo por oráculo candidato)."
---

# Efficiently Learning the Accuracy of Labeling Sources (Donmez et al., 2009)

## Resumo
Considera aprendizado ativo com múltiplos anotadores de acurácias
desconhecidas e possivelmente distintas. Propõe IEThresh: mantém, por
anotador, um intervalo de confiança sobre a taxa de acerto estimada
(via concordância com o rótulo agregado) e consulta apenas os anotadores
cujo limite superior excede um limiar — equilibrando exploração (descobrir
quem é bom) e exploração (usar os bons). Reduz custo mantendo qualidade de
rótulo frente a consultar todos ou escolher ao acaso.

## Relação com a tese
Fecha o trio clássico do oráculo imperfeito na Seção 2.2.3 (com Snow2008 e
Sheng2008): não só o anotador erra, como é preciso DESCOBRIR quem erra
menos, sob orçamento. O FALCO enfrenta o mesmo problema com LLMs: o E0 é a
versão offline e instrumentada dessa descoberta (acurácia com IC de Wilson
+ custo por mil rótulos por candidato), e a progressão de fases é o
roteamento resultante. A formulação bandit citada nos trabalhos futuros
(Cap. 6) é a ponte de volta à estimação online de Donmez et al.
