---
id: Daru2024Dissertacao
title: "Categorização de produtos em e-commerce: avaliação do método Argmax para classificação de descrições curtas em português"
authors: ["Darú, Gilsiley Henrique"]
year: 2024
venue: "Dissertação de Mestrado (MECAI), ICMC-USP, São Carlos. Orientador: Antonio Castelo Filho"
doi: "10.11606/D.55.2024.tde-07012025-171839"
url: "https://teses.usp.br/teses/disponiveis/55/55137/tde-07012025-171839/pt-br.html"
pdf: referencias-pdf/Daru2024Dissertacao.pdf
paper_type: dissertacao
pillars: [geral, P4]
status: fichado
verificado_em: 2026-08-16
verificado_por: banca (leitura integral do PDF, 91 pp.)
proposes: [argmax-binary]
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
| C4 | ~~Métrica unificada acc+Macro-F1 proposta e aplicada~~ **CLAIM RETIRADO** — ver "Correção de fichamento" abaixo | Resumo/Abstract apenas | **NÃO citar** como métrica herdada |
| C5 | Limitação declarada: sem AM avançado (transformers) e sem tratamento do custo de rotulagem | Cap. 6, Limitações, p. 102 | Ponte explícita dissertação→tese: BERTimbau (E2) e oráculo LLM (E0/E3) atacam exatamente as duas lacunas |
| C6 | Formalização do Argmax: RI reformulada como sêxtupla (X,Y,M,Q,R,C); protótipo de classe por CONCATENAÇÃO das descrições; predição por argmax(Aᵀx) (sem norma) ou argmax((A/A.)ᵀx) (cosseno) | Seção 3.3, p. 42; Eqs. 3.9-3.10, p. 47-48 | Origem formal do PVBin — citar ao descrever o classificador leve |
| C7 | Base: 250.365 descrições, 7 colunas, zero nulos, hierarquia 6 segmentos/20 subsegmentos/70 categorias/169 subcategorias/**795** categorias de menor nível; 18 maiores varejistas (ABRAS 2020), 95% das vendas | Seção 4.4.1 e Tab. 17, p. 64-65 | Caracterização da base no Cap. 3 |
| C8 | Só acurácia e Macro-F1 foram medidos — precisão e revocação são prometidas na hipótese (p. 22) e na conclusão (p. 101) mas **nunca reportadas**; nenhum teste de hipótese, IC ou tempo de execução consta | Cap. 5 inteiro; ausência verificada por varredura | A tese pode reportá-las sem sobreposição; e não deve atribuir rigor inferencial ao mestrado |

## Números que posso citar
- Binary [1,2] sem L2: **acc 89,56% / Macro-F1 70,09%** (melhor global) — Tab. 19, p. 74.
  Condição obrigatória ao citar: *média de validação cruzada 10-fold, classificação
  nas 795 categorias de menor nível, com todos os 250.365 rótulos*.
- 2º melhor: TFIDF [1,2] com L2 — **82,76% / 59,83%** (Tab. 19, p. 74).
- Pior acurácia: **19,07%** (Binary [1,1] com L2); pior Macro-F1: **23,44%**
  (TF [1,1] sem norma) — mesma tabela.
- Coeficientes de variação nos 10 folds: acurácia 0,21%–2,40%; Macro-F1 1,53%–3,15%.
- Configurações sugeridas por método (Tab. 23, p. 82): Binary {None*, [1,2]},
  TF {L2*, [1,2]}, TFIDF {L2, [1,2]*} (* = parâmetro mais impactante).
- Contexto bibliométrico (Cap. 2): 7.169 artigos em Scopus+WoS, crescimento de
  8,49% a.a.; apenas **46 artigos** sobre classificação de produtos na ACL
  Anthology entre 2016 e 2024 (p. 28) — útil para sustentar o nicho.

## Correção de fichamento (banca, 2026-08-16)

Leitura integral do PDF (91 pp.) corrigiu duas afirmações da versão anterior
deste fichamento:

1. **IEG / IEGE não existem no corpo da dissertação.** Os índices aparecem
   somente no Resumo e no Abstract; não há fórmula, definição formal, valor
   calculado nem tabela em nenhuma seção (varredura por "IEG", "IEGE",
   "Eficiência Geral", "estabilizado"). O que existe no lugar é a leitura
   conjunta acurácia × Macro-F1 por **quadrantes** delimitados pela mediana
   (Figuras 17-18, p. 76-77). **Consequência: a tese não pode citar IEG/IEGE
   como métrica herdada**; se precisar de métrica composta, define do zero — e
   aí é contribuição da tese.
2. **A dissertação não executa Naive Bayes, KNN, SVM, árvore nem regressão
   logística.** Os cinco são formalizados na teoria (Seção 3.5, p. 48-54) e
   nenhum aparece nos resultados; a própria conclusão registra isso como
   limitação (p. 102).

Nota de proveniência: a numeração impressa salta de 82 para 100 (artefato do
contador LaTeX, não conteúdo faltante — texto contínuo verificado no PDF); as
"106 p." da ficha catalográfica refletem essa numeração.

## Fronteira anti-sobreposição (para o R4/R7 da tese)

**É do mestrado — a tese cita, não reivindica:** a formalização Argmax e o
protótipo por concatenação (base do PVBin); a varredura das 12 configurações e
o veredito binário+bigramas+sem-L2; o par 89,56%/70,09% como teto supervisionado;
a publicação e a caracterização da base no Kaggle; a constatação de que remover
números degrada descrições de produto e de que stemming/lematização são inócuos
no domínio; o perfil empírico do texto curto de varejo (20-35 caracteres, 4-6
palavras, 70% dos dados em 80 categorias).

**Ficou em aberto — a tese reivindica legitimamente:** todo o eixo de eficiência
de rotulagem (aprendizado ativo, orçamento, curvas custo×desempenho); oráculo
LLM e seu gate de qualidade; cold start e DRI-SL; tratamento de ruído de rótulo
e a versão auditada da base (250.221); modelos contextuais aplicados (BERTimbau
só aparece no mestrado como tabela de revisão); rigor inferencial (o mestrado
não faz nenhum teste de hipótese); custo computacional e latência (nunca
medidos); precisão e revocação (prometidas e não reportadas).

Verificação léxica que sustenta a fronteira: no texto integral da dissertação há
**zero ocorrências** de "aprendizado ativo"/"active learning" como método, LLM,
oráculo, custo de rotulagem, prompt, zero-shot e PVBin. O único traço é a
referência a Tong & Koller (2002) na tabela bibliométrica (p. 27), citada como
item de contagem, nunca como método.

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
