---
id: Daru2024Dissertacao
title: "Categorização de produtos em e-commerce: avaliação do método Argmax para classificação de descrições curtas em português"
authors: ["Darú, Gilsiley Henrique"]
year: 2024
venue: "Dissertação de Mestrado (MECAI), ICMC-USP, São Carlos. Orientador: Antonio Castelo Filho"
doi: ""
pdf: referencias-pdf/Daru2024Dissertacao.pdf
paper_type: dissertacao
pillars: [geral, P4]
status: fichado
proposes: [argmax-binary, metrica-unificada-acc-macrof1]
uses_methods: [bag-of-words, n-gramas, normalizacao-l2, validacao-cruzada]
datasets: [retail-product-description-ptbr]
metrics: [acuracia, macro-f1]
tasks: [classificacao-de-texto-curto, classificacao-de-produtos-e-servicos]
models: []
extends: [Daru2022]
compares_with: []
contradicts: []
builds_on: [Daru2022]
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "Antecedente direto da tese (mestrado do autor, mesmos dados): otimiza a
           família Argmax e estabelece o melhor baseline leve conhecido do dataset
           (Binary [1,2] sem L2: acc 89,56%, Macro-F1 70,09%). O gap acc↔Macro-F1
           de ~19 p.p. quantifica o problema das classes raras que o FALCO enfrenta."
---

# Categorização de produtos em e-commerce: avaliação do método Argmax (Darú, 2024)

## Resumo
Dissertação de mestrado profissional (MECAI/ICMC-USP, 91 pp.) que aprofunda a
família Argmax do artigo de 2022 sobre o mesmo corpus de descrições de produtos
em português. Investiga sistematicamente o efeito de vetorização (Binary, Term
Frequency, TFIDF), N-gramas ([1,1] vs [1,2]) e normalização L2 sobre acurácia e
Macro-F1, com seleção de parâmetros por validação cruzada. Conclusões de
configuração (Tab. 23): **Binary → sem normalização + bigramas; TF → L2 (fator
dominante) + bigramas; TFIDF → L2 + bigramas (N-gram dominante)**. Melhor
resultado global: **Binary com N-gram [1,2] e sem normalização — acurácia 89,56%
e Macro-F1 70,09%**; TFIDF com L2+[1,2] robusto na sequência. Propõe ainda uma
métrica unificada combinando acurácia e Macro-F1 para comparação holística.
Limitação reconhecida na conclusão: não utiliza algoritmos de AM mais avançados.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Melhor configuração leve do dataset: Binary [1,2] sem L2 → acc 89,56%, Macro-F1 70,09% | Cap. 6, Conclusão (p.101) | Baseline PVBin da tese (E1/E3); números de referência do Cap.4 |
| C2 | Normalização L2 é o parâmetro de maior impacto (TF), bigramas beneficiam todos os métodos | Tab. 23 (p.~82) e pontos-chave (p.~100) | Justifica a configuração do PVBin portado para a biblioteca activelearning |
| C3 | Gap acurácia (89,6%) vs Macro-F1 (70,1%) ≈ 19 p.p. | Cap. 6 | Evidência quantitativa do problema de classes raras no dataset — motiva Macro-F1 como métrica principal da tese e a amostra S-strat do E0 |
| C4 | Métrica unificada acc+Macro-F1 proposta e aplicada | Cap. 6, contribuição 5 | Considerar no Cap.4; se não usada, justificar a escolha por LCE |
| C5 | Limitação declarada: sem AM avançado (transformers) e sem tratamento do custo de rotulagem | Cap. 6, Limitações | Ponte explícita dissertação→tese: BERTimbau (E2) e oráculo LLM (E0/E3) atacam exatamente as duas lacunas |

## Números que posso citar
- Binary [1,2] sem L2: **acc 89,56% / Macro-F1 70,09%** (melhor global).
- Configurações sugeridas por método (Tab. 23): Binary {None*, [1,2]},
  TF {L2*, [1,2]}, TFIDF {L2, [1,2]*} (* = parâmetro mais impactante).

## Crítica / limitações (minha leitura)
- Supervisão completa sobre corpus integral — sem noção de orçamento de rótulos;
  o resultado de 89,56% é o teto do método com TODOS os rótulos, e vira a
  referência natural para a meta de 95% do desempenho com ≤30% dos rótulos.
- A métrica unificada (C4) é ad hoc; a tese usa LCE + testes pareados, que têm
  interpretação estatística mais clara — citar C4 e justificar a diferença.

## Ideias que gera para a tese
- Redundância STC do Cap.2: as seções de vetorização esparsa/pré-processamento do
  Cap.2 da tese cobrem material já detalhado nesta dissertação — condensar citando
  \citet{Daru2024Dissertacao} em vez de reexplicar (pendência anotada no W7).
- Usar C3 no Cap.1 como o número que motiva a tese inteira no dataset: acurácia
  alta esconde 30 p.p. de deficiência nas classes raras.
