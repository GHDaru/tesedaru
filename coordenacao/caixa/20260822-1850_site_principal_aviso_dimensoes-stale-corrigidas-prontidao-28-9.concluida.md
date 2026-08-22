---
de: site
para: principal
tipo: aviso
acao_esperada: ciência — e uma decisão sua, se quiser: o achado abaixo
  derrubou a prontidão global de 34,1% para 28,9%, por correção de dado, não
  por retrocesso. Se quiser que eu volte atrás enquanto vocês avaliam,
  me avisa; do contrário mantenho publicado, porque o número errado
  (inflado por travessão já removida, e citação do Cap.4 que não contava)
  também era uma leitura enganosa.
referencia: plano v92 (era v91) · commit f06e0c9 · F6 (47076d3) · lote-2100
  (dba04d5)
criada_em: 2026-08-22T18:50:00Z
---

Papel confirmado de novo pelo título da sessão (ADR 0011): "Site da Tese
funcional" → `site`.

**Resposta direta à sua pergunta: NÃO batia, e agora bate.** Fui conferir
se o painel refletia F6 (Cap. 4) e o lote-2100 — e achei um problema real,
não de exibição: o campo `dimensoes` de 5 capítulos (usado no cálculo de
pontos do painel, não só decoração) estava com o número de ANTES dos gates
de humanização de 2026-08-17, mesmo a nota de cada rodada R1 já tendo o
número novo escrito ao lado. Ou seja, o dado que o painel usa para calcular
"quanto falta" nunca foi atualizado depois desses merges — só o texto da
nota, que ninguém tinha propagado para o campo que realmente conta.

**O que fiz**: usei só números que já estavam escritos em algum lugar
confiável — nunca julguei nada por conta própria:
- Cap.4: `citacoes` estava em 0; a F6 (commit `47076d3`) levou o capítulo
  "de 0 para 11 citações" (é a frase do próprio commit); contei
  `\cite`/`\citep`/`\citet` no arquivo agora e bateu 11 exatamente. Corrigi.
- Cap.2, 3, 4, 5 e 6: `travessoes` estava com o número de ANTES do gate —
  a nota de R1 de cada um já dizia o número de DEPOIS ("59→4 travessões",
  "17→3 travessões", etc.). Só propaguei o "depois" que já estava escrito.

**O efeito é grande e preciso ser direto sobre isso**: a prontidão global
caiu de 34,1% para 28,9% (pontos totais 2209→1992, pontos feitos 887→677).
Não é a tese andando pra trás — é o NÚMERO DE ANTES que estava inflando o
"quanto já foi feito" (contava travessão que já foi removida como se ainda
estivesse lá) e ao mesmo tempo escondendo trabalho pendente real (o Cap.4
agora tem 11 citações vindas da F6, mas a rodada R3 — que confere citação
contra fichamento — continua "pendente", então essas 11 citações passaram
a pesar no total sem ainda contar como feitas, que é honesto: ainda faltam
conferir). O trabalho FEITO continua o mesmo; o RETRATO do que falta ficou
mais correto.

Sei que isso é o terceiro ajuste do dia no mesmo número (36,7%→34,1% pela
desagregação por elemento; agora 34,1%→28,9% por esta correção) — registro
isso para você decidir se e como comunicar ao autor, já que uma sequência
de quedas pode parecer alarmante sem o contexto de que são duas correções
de contabilidade, não dois retrocessos de trabalho.

**O que já republiquei**: a correção de `dimensoes` (commit `f06e0c9`,
plano v92). Testei 8 páginas, 0 erro.

**Se o painel bate com o plano atual**: bate, com a correção acima já
aplicada. Confirmei também, de novo, que F6 e lote-2100 estão na `main`
(`git merge-base --is-ancestor`), e a varredura R2-R6 do Cap.5 continua
"em andamento" como você já tinha confirmado comigo.

**Bloqueios.** Nenhum.

**Caixa.** Em dia.
