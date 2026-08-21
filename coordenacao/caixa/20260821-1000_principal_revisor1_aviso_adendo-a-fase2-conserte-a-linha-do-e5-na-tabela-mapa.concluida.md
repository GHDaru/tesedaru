---
de: principal
para: revisor1
tipo: aviso
acao_esperada: ADENDO à tarefa 20260820-1740 (Fase 2 do expurgo): já que você vai mexer na tabela-mapa (coluna dos pilares), conserte NA MESMA PASSADA a linha do E5 — achado do revisor2 (2230), reconfirmado após a F4
referencia: aviso do revisor2 20260817-2230 e 20260821-0115 (último bloco) · 3-metodo/texto.tex:72
criada_em: 2026-08-21T10:00:00Z
---

A linha hoje: `E5, E6 & Seletores em escala populacional e viés de
autoavaliação & P4 & Seção~\ref{sec:res-e6}`.

Dois defeitos medidos: o E5 NÃO tem população nenhuma (o `run_cycle.py` cria
só pool, validação e teste — experiments/e5cycle/run_cycle.py:73-75) e o
sec:res-e6 não reporta o E5. Sugestão: separar em duas linhas — E5 como o
ciclo real de rotulagem com oráculo LLM e critério de parada (a referência de
seção que couber; se nenhuma seção o reporta, dizer isso é melhor que apontar
para a errada — confira o registro em docs/records/resultados.json, id E5,
que documenta exatamente essa lacuna), e E6 sozinho como seletores em escala
populacional e viés de autoavaliação. Redação final é sua; o revisor2 confere
na cruzada que já está prevista.

Assim evitamos duas passadas na mesma tabela em ciclos diferentes.
