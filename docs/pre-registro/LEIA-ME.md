# Proveniência do desenho do estudo ("pré-registro")

- `2022-05-31_apresentacao-aprendizado-ativo.pdf` — apresentação pública do
  autor em evento, maio de 2022 (metadado do PDF: criado em 31/05/2022).
  Conteúdo: o problema (esforço de saneamento na categorização de itens de
  varejo; caso real de +130 mil itens, 6 meses de trabalho), a solução
  proposta (laço de aprendizado ativo, adaptado de Settles 2009), estratégias
  de seleção, lotes pequenos, e o caso FakeNewsBR (SVC, 7.200 notícias).
- Decisão do autor (2026-08-21): o exame de qualificação (PPGMNE/UFPR)
  apresentou exatamente este desenho; as ocorrências de "pré-registrado" na
  tese passam a citar a QUALIFICAÇÃO como documento de proveniência, com esta
  apresentação como evidência datada auxiliar.
- Honestidade de escopo: a apresentação é anterior à fase LLM do FALCO
  (o oráculo em 2022 era humano/SVC) e NÃO enuncia números específicos
  (teto de 15%, gate de 85%, partições). Afirmações da tese que dependam de
  um número específico "pré-registrado" só podem citar o que o documento
  citado de fato contém.

## Segundo documento (2026-08-21)

- `2022-05-31_framework-humano-computacional.pptx` — "Framework
  Humano-Computacional para Preparação Acelerada de Dados". Metadados:
  criado em 31/05/2022 19:36 UTC, última modificação 16/05/2023 (a versão
  arquivada é o estado de maio de 2023). Autor: Gilsiley Darú.
- Este deck CONTÉM o que a apresentação-irmã não continha:
  - **A conclusão do teto (slide 38)**: "COM 15% dos dados foi possível
    atingir uma performance similar ao modelo POPULACIONAL com o algoritmo
    de SELEÇÃO por INCERTEZA".
  - **O critério original**: performance "similar ao modelo populacional",
    avaliada em validação EXTERNA (base de validação de 60 mil rotulados,
    "Avaliar Generalização") — a filosofia do que a tese hoje chama de
    regime canônico (avaliar contra a população, não contra o próprio
    conjunto de treino).
  - **O desenho**: base do estudo de 180 mil rotulados (60k validação +
    120k "não rotulada" para a técnica), semente de 1.000, lotes de 500,
    simulação até 23 mil rótulos em 46 iterações; "com 15.000 rótulos a
    generalização estabiliza em 95%" (slide 33); comparação
    incerteza × aleatório com acurácia interna × externa.
- Datação honesta: o arquivo foi criado em 2022 e modificado pela última vez
  em maio de 2023 — não é possível provar por metadado que um slide
  específico existia em 2022. Qualquer citação deve datar o documento como
  "2022, versão de maio de 2023" (ou citar a data do exame de qualificação,
  que o autor confirma ter apresentado exatamente este desenho).
- O que continua SEM fonte pré-registrada: o gate de 85% do oráculo e as
  partições atuais (pool de 50 mil, retido de 4 mil, população de 231.490 —
  a base e os números de 2022/2023 eram outros: 180k/120k/60k).

## Confirmações do autor (2026-08-21, conversa com o principal)

1. **O exame de qualificação foi em JUNHO DE 2023** (PPGMNE/UFPR) e
   apresentou exatamente este desenho. A modificação final do deck
   (16/05/2023) é consistente: versão fechada semanas antes do exame.
   Âncora de citação principal: a qualificação, junho de 2023; o deck é a
   evidência material.
2. **A métrica do critério pré-registrado é ACURÁCIA** — palavras do autor:
   "foi a acurácia que atingiu a mesma performance. Acurácia ficou melhor."
   Confere com o artefato: todas as curvas do deck são de acurácia
   (acuracia_E/acuracia_I, externa e interna), a estabilização "em 95%" do
   slide 33 é acurácia, e a conclusão do slide 38 ("performance similar ao
   modelo populacional") refere-se a essas curvas. O Macro F1 não aparece no
   deck: entrou depois, durante a tese, como análise de robustez para o
   desbalanceamento de classes (714 categorias) — e deve ser apresentado
   como tal, não como a métrica do critério original.
3. **"O F1 ficou longe"** (autor, 2026-08-21): já no estudo da qualificação
   o F1 não acompanhava — quem atingia a performance do modelo populacional
   era a acurácia. Nota de escopo: o deck NÃO contém curvas de F1; esta é
   confirmação testemunhal do autor sobre o estudo original. A redação da
   tese deve dizer que o critério e as curvas pré-registradas são de
   acurácia, e que o Macro F1 (introduzido na tese) estende um
   comportamento já observado: ele fica atrás da acurácia desde a origem.
