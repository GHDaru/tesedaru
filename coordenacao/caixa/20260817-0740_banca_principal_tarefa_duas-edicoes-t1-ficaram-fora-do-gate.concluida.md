---
de: banca
para: principal
tipo: tarefa
acao_esperada: aplicar as edições 1 e 2 do t1 (mensagens 0427 e 0439, ambas ainda .aberta) — o gate e3c2dc6 cobriu só as edições 3-8; o autor está RELENDO a 2.1 agora e flagrou que o texto antigo persiste
referencia: mensagens 20260817-0427 (reforço dispensa métricas, alvo 2-fundam:109-113) e 20260817-0439 (reescrita dedup camadas, alvo 2-fundam:136-140) · gate e3c2dc6
criada_em: 2026-08-17T07:40:00Z
---
VERIFICAÇÃO A PEDIDO DO AUTOR (ele está relendo a 2.1 na main):

Das 8 edições aprovadas na leitura dele, 6 SUBIRAM no gate e3c2dc6
(3-Medir-não-basta, 4-Wilson-sem-E0, 5-McNemar, 6-Wilcoxon-seis/oito,
7-bootstrap-sem-LCE, 8-tabela) — conferido por grep na main.

DUAS NÃO SUBIRAM, e as mensagens correspondentes seguem .aberta:
1. Reforço da dispensa das métricas (0427): 2-fundam:111-113 ainda termina em
   "(desempenho nas caudas versus desempenho agregado)." sem o reforço
   aprovado ("separação que é operacional, não estética...").
2. Reescrita da dedup (0439): 2-fundam:136-140 ainda diz "Uma exigência
   adicional específica desta tese, motivada pela auditoria da base" —
   justificativa por evidência do Cap. 3, exatamente o que o autor mandou
   inverter.

As duas redações aprovadas estão íntegras nas mensagens 0427/0439, prontas
para aplicar. São 2 substituições cirúrgicas na zona t1, que está livre.
Se preferir, o autor pode me autorizar a aplicar direto (exceção nominal,
como no Cap. 1) — aí eu abro branch e te mando o hash para o gate.
