---
de: banca
para: principal
tipo: tarefa
acao_esperada: aplicar as 5 edições no ciclo do t1 (revisor2) como UM lote — todas aprovadas textualmente pelo autor em leitura ao vivo com a banca; gate em bloco; as duas primeiras já foram enviadas (b865ae6 e 7de13dc) e este pacote as consolida com as três novas
referencia: leitura do autor (seção 2.1) em conversa com a banca, 2026-08-17 · R6 da banca (vazamentos) · auditoria de escrita (linha 145) · zona t1, 2-fundam/texto.tex
criada_em: 2026-08-17T04:55:04Z
---
PACOTE COMPLETO DA LEITURA DO AUTOR NO T1 — 5 edições aprovadas:

1. MÉTRICAS (já enviada, b865ae6): reforço da justificativa de dispensa de
   acurácia balanceada/MCC/Kappa — "separação operacional, não estética" +
   \ref ao capítulo de resultados. Linha ~109-113.

2. DEDUP (já enviada, 7de13dc): justificativa invertida — argumento
   definicional no Cap. 2, evidência fica no Cap. 3. Linha ~136-140.

3. "MEDIR NÃO BASTA" (linha ~145) — NOVA. Remove aforismo de abertura +
   par de travessões com anáfora tripla:
   ANTES: "Medir não basta: as comparações desta tese — entre oráculos,
   entre estratégias de seleção, entre configurações — exigem afirmar se uma
   diferença observada excede a flutuação amostral. Quatro instrumentos
   cobrem as situações que aparecem nos Capítulos 4 e 5, cada qual com a
   referência original e a referência aplicada ao aprendizado de máquina."
   DEPOIS: "Toda comparação desta tese (entre oráculos, estratégias de
   seleção ou configurações) exige afirmar se a diferença observada excede a
   flutuação amostral. Quatro instrumentos cobrem as situações que aparecem
   nos Capítulos 4 e 5, cada qual com a referência original e a de uso em
   aprendizado de máquina."
   (Era a linha 145 do catálogo da auditoria de escrita — autor e auditoria
   convergiram no mesmo ponto.)

4. E0 NO PARÁGRAFO DO WILSON + TABELA (linhas ~159, ~199, ~200) — NOVA.
   Expurgo de código de experimento do Cap. 2 (item 3 do R6):
   a) l.159: "toda acurácia de oráculo do E0 é reportada" -> "toda acurácia
      de oráculo desta tese é reportada com IC de Wilson a 95\%
      (Capítulo~\ref{ch:resultados-falco})."
   b) l.199 (célula): "toda acurácia de oráculo (E0)" -> "toda acurácia de
      oráculo (Cap.~\ref{ch:resultados-falco})"
   c) l.200 (célula): "pareamentos do E0/E0-P" -> "pareamentos de oráculos e
      de variantes de \textit{prompt} (Cap.~\ref{ch:resultados-falco})"
   As demais ocorrências de códigos no Cap. 2 (l.631 e as do R6) seguem a
   mesma receita nos ciclos t3/t4 — não precisam de aprovação item a item.

5. McNEMAR/DIETTERICH (linhas ~163-170) — NOVA. Remove dois termos órfãos
   ("erro tipo I": única ocorrência na tese, nunca definido; "testes t
   re-amostrados": idem) e desadensifica:
   ANTES: "Comparação pareada na mesma amostra (McNemar). Quando dois
   oráculos rotulam as mesmas instâncias, os erros são dependentes e o teste
   correto opera sobre os pares discordantes: o teste de McNemar (1947)
   examina a assimetria entre os $b$ casos em que só o primeiro acerta e os
   $c$ em que só o segundo acerta; quando $b+c<25$, usa-se a versão binomial
   exata. Dietterich (1998), avaliando empiricamente cinco testes para
   comparar classificadores, recomenda o McNemar precisamente no regime desta
   tese — modelos avaliados uma única vez sobre um conjunto comum — por
   controlar o erro tipo~I onde os testes $t$ re-amostrados falham."
   DEPOIS: "Comparação pareada na mesma amostra (McNemar). Quando dois
   oráculos rotulam as mesmas instâncias, seus acertos não são independentes,
   e a comparação correta olha apenas os pares discordantes: as $b$
   instâncias em que só o primeiro acerta e as $c$ em que só o segundo. O
   teste de McNemar (1947) verifica se a assimetria entre $b$ e $c$ excede o
   que o acaso produziria; quando $b+c<25$, usa-se a versão binomial exata. A
   escolha segue Dietterich (1998), que comparou empiricamente cinco testes e
   concluiu que o McNemar é o adequado quando cada modelo é avaliado uma
   única vez sobre um conjunto comum — o regime desta tese; nesse cenário, as
   alternativas declaram diferenças inexistentes com frequência acima da que
   prometem."
   (Dietterich1998 tem fichamento; conteúdo técnico intacto.)

NOTA DE APLICAÇÃO: linhas citadas referem-se ao estado atual da main; o
executor deve localizar por conteúdo (as zonas podem deslocar com merges).
Todas as 5 são da zona t1 — um lote, um gate, e o R1 do t1 humaniza por cima
já sem esses alvos.
