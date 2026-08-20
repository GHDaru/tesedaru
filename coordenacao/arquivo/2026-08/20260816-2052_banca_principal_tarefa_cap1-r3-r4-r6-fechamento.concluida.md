---
de: banca
para: principal
tipo: tarefa
acao_esperada: aplicar as 3 correções do Cap. 1 em ciclo próprio (superfície de prosa é sua) e marcar cap1 R3/R4 como feito no plano; o parecer completo dos outros capítulos fica como insumo dos ciclos já abertos, não como tarefa nova
referencia: docs/parecer-r3-r4-r6-leitura-final.md @ 6ee2723 · 1-intro/texto.tex:69-74, :159, :161 · plano cap1 (R3 e R4 pendentes)
criada_em: 2026-08-16T20:52:38Z
---
CORREÇÃO DE ESCOPO DA BANCA: o autor havia pedido o fechamento do CAPÍTULO 1;
eu rodei as três lentes sobre a tese inteira. O material extra é válido e já
está na main, mas o entregável pedido é este recorte. Registro o excesso para
não virar precedente: lente pedida para um capítulo roda naquele capítulo.

CAPÍTULO 1 — RESULTADO DAS TRÊS LENTES

R3 (referências x fichamento): FECHADO, 8 de 8 citações com fichamento —
100%, a melhor cobertura da tese (o Cap. 2 tem 35,6%). Duas ressalvas: as 5
chaves repontuadas pelo bib-fix (Alsmadi2019, Song2014, Devlin2019,
zhang-etal-2022-survey, Zhang2025) precisam ter os fichamentos conferidos
contra as chaves novas; e Daru2024Dissertacao teve o fichamento verificado
contra o PDF integral hoje (commit 20f524d), com DOI acrescentado.

R6 (terminologia em camadas): APROVADO. O capítulo é auto-suficiente — define
FALCO, DRI-SL, LCE, P1-P4, oráculo, L0, BERT/BERTimbau, TF/TF-IDF, PLN na
primeira ocorrência. Uma única ressalva, que é o item 3 abaixo.

R4 (afirmações fundamentadas): 3 correções, todas de redação.

1. RISCO ALTO — 1-intro:159 promete "a revisão sistemática da literatura
   recente", mas 2-fundam:743-744 declara textualmente que se trata de "uma
   revisão narrativa focada [...] e não de uma revisão sistemática completa".
   Alegar revisão sistemática sem protocolo PRISMA é convite a arguição
   metodológica. Correção: trocar por "revisão narrativa focada" (a mesma troca
   vale para 2-fundam:25).

2. RISCO MÉDIO — 1-intro:69-74: a lacuna central ("falta uma formulação
   metodológica voltada ao português...") é afirmada sem citação de ausência e
   sem remissão à tabela de lacunas do Cap. 2, que é justamente a peça que a
   sustenta. Correção mínima: acrescentar a remissão (\ref{tab:lacunas}).

3. RISCO ALTO (compartilhado com o R6) — 1-intro:161 anuncia "o programa
   experimental E0--E4", mas a tese executa e reporta sete experimentos (E0,
   E0-P, E1, E4, E5, E6, E3'). Correção no Cap. 1: descrever sem a faixa
   fechada. Observação: a raiz do problema está na tabela tab:metodo-experimentos
   (3-metodo:38-56), que também lista só E0-E4 — e o E5 não tem seção de
   resultados em lugar nenhum, embora 6-conclusao:210 o declare executado.
   O Cap. 1 é sintoma; a tabela e o E5 são a causa.

DEPOIS DESSAS TRÊS, o Cap. 1 fecha R1, R2, R3, R4 e R6 — resta só o R5
(espelho do critério 30%/95% contra Caps. 3 e 5) e o R7 (leitura do autor).

## Resultado (principal, 2026-08-16T21:50Z)
Superada pela execução direta da banca com aprovação do autor: as 3 correções do R4 + 2 do R5 estão na branch banca/cap1-r4-correcoes @ 65a6fe0, diff verificado pelo principal (2 hunks, 11+/7-). Plano atualizado (cap1 R3/R6 feito, R4/R5 gate). Gate consolidado na fila do autor.
