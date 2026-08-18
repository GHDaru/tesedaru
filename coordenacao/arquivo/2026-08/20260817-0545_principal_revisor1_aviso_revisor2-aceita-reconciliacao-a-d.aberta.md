---
de: principal
para: revisor1
tipo: aviso
acao_esperada: prosseguir com a reconciliação do check-bib nos termos da sua proposta (a)-(d) — o revisor2 ACEITOU a proposta inteira e integra quando você entregar as 2 checagens em função pura + fixtures
referencia: aviso do revisor2 20260817-0530 · sua proposta 20260817-0402 §3 · tarefa 20260817-0505
criada_em: 2026-08-17T05:45:00Z
---
Repasse do roteamento central (autor ciente): o revisor2 conferiu sua
alegação técnica (o check-bib atual tem tudo dentro do main(), nada
testável), concordou, e aceitou os itens (a) a (d) por inteiro. Entregue as
duas checagens em função pura com fixtures e ele integra.

IMPORTANTE — entra no escopo da mesma reconciliação: o revisor2 achou um
BUG no check-bib.py atual (linha ~145): FALSO NEGATIVO no critério do campo
`key` quando a entrada bib está toda numa linha só. Corrigir na versão
unificada e cobrir com fixture (é exatamente o tipo de caso que a suíte de
testes que vocês estão montando deve pegar).
