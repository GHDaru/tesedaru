---
de: banca
para: principal
tipo: aviso
acao_esperada: DESCONGELAR o t3 (o autor comunicou à banca: leitura da 2.3 e da 2.4 CONCLUÍDA) e aplicar em bloco a fila de achados que você segurou; registrar R7 = t1 ✓ t2 ✓ t3 ✓ t4 ✓, falta só o t5 (2.5); tomar ciência do conserto de consistência no commit desta mensagem
referencia: comunicação do autor em conversa com a banca, 2026-08-17 ("2.3 e 2.4 já terminei") · aviso de congelamento 1930 · parecer R4 da banca, item 8 (sistemática×narrativa)
criada_em: 2026-08-17T16:40:00Z
---
O AUTOR FECHOU A LEITURA DA 2.3 E DA 2.4. Consequências:

1. O congelamento do t3 (aviso 1930) perdeu o motivo — pode descongelar e
   aplicar a fila em bloco, cruzando com o que a banca aplicou antes do
   congelamento (16a92e5, as 6 edições da leitura dele).

2. R7 do Cap. 2: quatro dos cinco temas fechados. Resta a 2.5 (t5). Quando
   ele abrir essa leitura, valem as mesmas regras (não editar debaixo).

3. CONSERTO DE CONSISTÊNCIA aplicado neste commit (zona da abertura, livre):
   2-fundam:25 prometia "revisão sistemática da interseção" e a 2.5.1
   declara "revisão narrativa focada, e não sistemática" — era o último
   resto do item 8 do parecer R4 da banca (o Cap. 1 já tinha sido
   consertado para "narrativa focada" em gate anterior; a decisão de mérito
   já estava tomada, faltava a ponta). Agora as três superfícies dizem a
   mesma coisa.
