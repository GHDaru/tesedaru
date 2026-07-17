---
id: Orellana2018
title: "A study on the impact of pre-processing techniques in Spanish and English text classification over short and large text documents"
authors: ["Orellana, Gerardo", "Arias, Belen", "Orellana, Marcos", "Saquicela, Victor", "Baculima, Fernando", "Piedra, Nelson"]
year: 2018
venue: "INCISCOS 2018, IEEE"
doi: ""
pdf: referencias-pdf/Orellana2018.pdf
paper_type: avaliacao
pillars: [geral]
status: fichado
proposes: []
uses_methods: [pre-processamento]
datasets: []
metrics: [acuracia]
tasks: [classificacao-de-texto, classificacao-de-texto-curto]
models: []
extends: []
compares_with: [Naseem2021HateSpeech]
contradicts: []
builds_on: []
falco_relation:
  - type: contextualiza
    target: FALCO
    note: "Impacto de pré-processamento medido em ESPANHOL (língua próxima ao
           português) e cruzando curto×longo — apoio à discussão de
           pré-processamento fora do inglês no Cap.2. (Arquivo veio rotulado como
           Uysal 2014; identidade corrigida no saneamento.)"
---

# Impact of pre-processing in Spanish and English text classification

## Resumo
Estudo IEEE (Equador, 2018) medindo o impacto de técnicas de pré-processamento
na classificação de textos curtos e longos em espanhol e inglês — um dos poucos
trabalhos do lote que cruza idioma (não-inglês) × comprimento do texto.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | O efeito do pré-processamento varia com idioma e comprimento do texto | Escopo | Cap.2: pré-processamento não transfere cegamente do inglês — apoio para validar o pipeline em português |

## Números que posso citar
- (Qualitativo.)

## Crítica / limitações (minha leitura)
- Conferência regional, espanhol≠português; peso bibliográfico menor, citar em
  bloco com Naseem2021HateSpeech.

## Ideias que gera para a tese
- Nota de rodapé sobre a escassez de estudos de pré-processamento para português
  → conecta com Bard2019Normalizador e Branco2012.
