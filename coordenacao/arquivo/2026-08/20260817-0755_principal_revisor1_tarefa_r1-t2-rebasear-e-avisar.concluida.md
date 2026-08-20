---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: (1) rebasear/mergear a main na sua humanize/cap2-t2 — ela nasceu ANTES dos merges do patch-t2 e do pacote-t1, e a faixa do t2 na main ganhou a inserção Sener/TypiClust que a sua branch não tem; reconciliar preservando as citações novas E a sua reescrita; (2) postar a conclusão com hash novo (a entrega atual está SEM aviso — evento 4 do §3 é obrigatório); (3) verificar se os "0 travessões" respeitaram a exceção de contraste do critério (o t3 preservou 1 de propósito)
referencia: sua branch humanize/cap2-t2 @ ba9a9a9 (detectada pelo principal, sem aviso na caixa) · merges e70389d..cefa3b9 na main · docs/criterio-humanizacao.md
criada_em: 2026-08-17T07:55:00Z
---
O trabalho está bom pelos números (28→0 na faixa, citações do seu ponto de
partida intactas), mas o diff contra a main atual mostra TRÊS citações
ausentes — não porque você as removeu, e sim porque entraram na main depois
do seu ponto de corte (Farquhar/Kossen, Guyon2011ALC, Hacohen2022TypiClust
+ Sener2018 na sua faixa). Merge sem reconciliação perderia texto aprovado
pelo autor hoje. Depois do rebase: conclusão ao principal, verificação
cruzada do revisor2, e o gate sobe em bloco com o R1 do t3.
