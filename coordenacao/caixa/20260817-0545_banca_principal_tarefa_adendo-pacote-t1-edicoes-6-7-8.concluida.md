---
de: banca
para: principal
tipo: tarefa
acao_esperada: somar ao pacote t1 (a48237c) as edições 6-8 abaixo, todas aprovadas textualmente pelo autor; aplicar como o MESMO lote/gate; repassar ao revisor2 o padrão ampliado do Cap. 2 (nota ao final)
referencia: leitura do autor (2.1, inferência estatística) em conversa com a banca, 2026-08-17 · pacote a48237c · achado grave nº 1 do R4 do revisor2 (seis vs oito sementes)
criada_em: 2026-08-17T05:45:37Z
---
ADENDO AO PACOTE T1 — edições 6, 7 e 8, aprovadas pelo autor:

6. WILCOXON (parágrafo "Comparação pareada por semente", ~l.171-180).
   Remove "indefensável" (juízo inflado), "limitação estrutural" (cerimônia)
   e RESOLVE NA FONTE o achado grave do R4 (aritmética fundamenta seis, texto
   concluía oito sem premissa):
   ANTES: "...sem supor normalidade — suposição indefensável para métricas
   limitadas como o Macro F1 —, e é a recomendação canônica de Demšar (2006)
   [...] Sua limitação estrutural importa ao desenho: com $n$ pares, o menor
   $p$-valor bicaudal atingível é $2/2^n$ — com menos de seis sementes a
   significância a 5% é inalcançável por construção, o que fundamenta o
   mínimo de oito sementes adotado no Capítulo 3."
   DEPOIS: "...sem supor normalidade — suposição difícil de sustentar para
   métricas limitadas ao intervalo $[0,1]$, como o Macro F1 — e é a
   recomendação de Demšar (2006) para comparar dois algoritmos sobre
   múltiplas condições. Um limite aritmético importa ao desenho: com $n$
   pares, o menor $p$-valor bicaudal é $2/2^n$. Seis sementes são o mínimo
   que alcança significância a 5\% ($p=0{,}031$); esta tese adota oito, cujo
   piso de $p=0{,}0078$ mantém a significância alcançável mesmo sob correção
   para comparações múltiplas sobre as mesmas sementes."
   NOTA AO EXECUTOR: a ponte seis->oito agora é propriedade aritmética
   verificável (0,0078 sobrevive a Holm/Bonferroni para até 6 comparações a
   5%), enunciada como propriedade, não como intenção. Confere com o remédio
   que o próprio revisor2 sugeriu no R4.

7. BOOTSTRAP (parágrafo "Intervalos por reamostragem", ~l.181-186).
   DECISÃO DE PRINCÍPIO DO AUTOR, registrada para os demais temas: no Cap. 2
   NÃO entram criações da tese como exemplo — entram os conceitos da
   literatura de que elas descendem. A LCE sai do Cap. 2; o exemplo vira o
   conceito-pai (ALC, já no bib e citada no Cap. 3/A1). Também cai a cauda
   "permanecendo informativo mesmo com poucas repetições" (propriedade que a
   citação não cobre — achado leve nº 6 do R4).
   ANTES: "Para funcionais sem distribuição amostral conhecida — como a
   diferença de LCE entre estratégias —, o bootstrap (Efron e Tibshirani,
   1993) estima o intervalo de confiança reamostrando os pares observados com
   reposição (método do percentil), permanecendo informativo mesmo com poucas
   repetições."
   DEPOIS: "Para funcionais sem distribuição amostral conhecida — caso típico
   das áreas sob curvas de aprendizado usadas para resumir uma execução
   inteira de aprendizado ativo \citep{Guyon2011ALC} — o bootstrap (Efron e
   Tibshirani, 1993) estima o intervalo de confiança reamostrando os pares
   observados com reposição (método do percentil)."

8. TABELA situação->instrumento (linha do bootstrap, ~l.201-202): a célula de
   uso que hoje traz LCE + código de experimento segue a mesma receita:
   "diferença de LCE (E3)" (ou equivalente) -> "comparação de curvas de
   aprendizado (Cap.~\ref{ch:metodo})".

PADRÃO AMPLIADO DO CAP. 2 (para o revisor2 aplicar nos temas dele, e o
revisor1 nos t4/t5): além de zero código de experimento, ZERO criação da tese
usada como objeto conhecido — DRI-SL, PVBin, LCE e FALCO aparecem no Cap. 2
apenas como PONTE (nomeados com \ref para onde nascem), nunca como exemplo ou
premissa de argumento. O R6 da banca já lista as ocorrências; a receita é uma.
