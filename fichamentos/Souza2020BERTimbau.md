---
id: Souza2020BERTimbau
title: "BERTimbau: Pretrained BERT Models for Brazilian Portuguese"
authors: ["Souza, Fábio", "Nogueira, Rodrigo", "Lotufo, Roberto"]
year: 2020
venue: "BRACIS 2020, pp. 403–417, Springer (PDF arquivado: dissertação de mestrado Unicamp, versão expandida)"
doi: "10.1007/978-3-030-61377-8_28"
pdf: referencias-pdf/Souza2020BERTimbau.pdf
paper_type: metodo
pillars: [P4]
status: fichado
proposes: [bertimbau]
uses_methods: [pre-treinamento, fine-tuning]
datasets: [brwac, assin2, harem]
metrics: [f1]
tasks: [similaridade-textual, inferencia-textual, ner]
models: [bertimbau, bert, mbert]
extends: [Devlin2019]
compares_with: []
contradicts: []
builds_on: [Devlin2019]
falco_relation:
  - type: usa
    target: FALCO
    note: "É o classificador-alvo dos experimentos E2/E3 da tese (via HuggingFace,
           sem fork, conforme decisão de projeto). Estado da arte para português
           nas três tarefas avaliadas, superando o BERT multilíngue."
---

# BERTimbau: Pretrained BERT Models for Brazilian Portuguese

## Resumo
Treina modelos BERT para o português brasileiro (apelidados BERTimbau), aplicando
a receita de Devlin et al. (2019) com pré-treinamento em corpus de português
(BrWaC). Avaliados em três tarefas downstream — similaridade textual de sentenças,
reconhecimento de implicação textual (RTE) e reconhecimento de entidades nomeadas
(NER) — os modelos **melhoram o estado da arte nas três tarefas, superando o
BERT Multilíngue (mBERT)**, confirmando a eficácia de LMs pré-treinados
monolíngues para línguas com poucos exemplos anotados. Modelos liberados
publicamente como baselines para a comunidade. (O PDF arquivado é a dissertação
de mestrado da Unicamp, versão expandida do paper BRACIS 2020 — a citação
canônica na tese é o paper.)

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | BERTimbau supera mBERT e o estado da arte em STS, RTE e NER em português | Abstract | Justifica a escolha do BERTimbau (e não mBERT) como classificador dos E2/E3 |
| C2 | Transferência de LM pré-treinado é especialmente valiosa quando dados rotulados são escassos | Abstract | Sinergia direta com AL: é o regime de poucos rótulos das iterações do FALCO |

## Números que posso citar
- (Resultados por tarefa estão na dissertação/paper; a tese usa o modelo, não os
  números — citar C1 qualitativamente.)

## Crítica / limitações (minha leitura)
- Avaliado em texto padrão (sentenças completas); nossas descrições (~32 chars,
  CAIXA ALTA, abreviações CERV/REFR) estão fora da distribuição do BrWaC — o
  desempenho do fine-tuning nesse regime é uma pergunta empírica do E2.
- Tokenização subword de abreviações de varejo pode fragmentar termos-chave.

## Ideias que gera para a tese
- No E2, reportar exemplos de tokenização de descrições reais (quantos subwords
  por token de abreviação) para discutir o custo da mudança de domínio.
