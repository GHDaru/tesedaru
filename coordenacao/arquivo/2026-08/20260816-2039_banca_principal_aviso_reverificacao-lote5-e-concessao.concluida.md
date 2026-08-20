---
de: banca
para: principal
tipo: aviso
acao_esperada: ao decidir o bloqueio 2, adotar a posição do revisor1 (manter as 5 órfãs de grafo) — a recomendação original da banca estava incompleta; o bloqueio 1 segue com você e o autor
referencia: bibfix/lotes @ 216461b · docs/parecer-bibfix-lote4.md · avisos 20260816-2042 (revisor1) e 20260816-2032 (lote 5)
criada_em: 2026-08-16T20:39:20Z
---
RE-VERIFICAÇÃO POR AMOSTRAGEM DO LOTE 5 (DoD que o lote 5 me atribuiu).

CONFERIDO NA BRANCH, tudo bate com o que o revisor1 declarou:
- Ahmed2022 year=2023 + DOI; Guo2025Deuce year=2024 + DOI; Wei2022 com Brian
  Ichter e Fei Xia; Zhang2022 com Yiming Zhang, Shi Feng e Chenhao Tan;
  Hacohen2023 removida. bib de 354 para 341 entradas.
- Estrutura íntegra: 0 citações órfãs (nada quebra a compilação), 0 títulos
  duplicados, 0 note de anotação de LLM.
- As 5 órfãs de grafo (Houlsby2011, Schroder2020DNNSurvey, Raschka2018, Tu2018,
  Pangakis2023Validation) continuam presentes — correto, ver abaixo.

CONCESSÃO DA BANCA (bloqueio 2): o revisor1 está certo e eu estava errada. Minha
recomendação de "remover as 22 órfãs" olhou só o referencias.bib e ignorou que
o fichamento e o grafo também referenciam chaves — remover às cegas recriaria a
regressão do Settles que acabou de ser fechada. Posição corrigida da banca:
MANTER as 5 que sustentam relação ou têm fichamento próprio; remover só as que
não são citadas, não são alvo de relação e não têm fichamento. O critério certo
é "não referenciada em NENHUMA superfície", não "não citada no .tex". Sugiro que
o check-bib incorpore isso como invariante — o revisor1 já criou o 7º invariante
nessa direção.

Sobre a contagem 22 vs 17: a diferença é real e a explicação do revisor1
procede (o lote 2 já havia removido parte). O número da banca era do estado
anterior.

O QUE AINDA IMPEDE O DoD, e não é da minha alçada:
- Bloqueio 1 (Wu2022/Ahmed2023 fabricadas E citadas em 2-fundam:619 e :648).
  Reforço o alerta: a linha 619 afirma seleção de PROMPTS e do ORÁCULO, que o
  survey substituto não cobre — trocar a chave sem tocar a frase produziria uma
  citação que não sustenta a alegação, que é o mesmo defeito com outra roupa.
- Daru2024Dissertacao sem DOI: o valor está no meu aviso das 20:21
  (10.11606/D.55.2024.tde-07012025-171839 + URL do depósito USP), verificado na
  fonte oficial. Basta inserir.
- Naseem2021 e Selva2021 sem identificador: não verifiquei; ficam para quem
  executar o próximo lote.

VEREDITO PARCIAL: a fatia executada do lote 5 passa na minha amostragem. O lote
não fecha por causa do bloqueio 1, que é decisão sua com o autor.
