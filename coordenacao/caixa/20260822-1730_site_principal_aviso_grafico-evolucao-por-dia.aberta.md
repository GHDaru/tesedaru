---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma — ciência; publicado direto (ADR 0010, site dispensa gate)
referencia: commits 98e2321/429b8b0 · scripts/compute-kpis.py (serie_historica)
criada_em: 2026-08-22T17:30:00Z
---

Pedido direto do autor: o gráfico "Evolução da prontidão" (página Plano)
agora é por dia de calendário, não só por dia com commit no plano. Antes, um
dia sem commit (ex.: 08-19) sumia da linha do tempo e o segmento entre os
dois dias vizinhos parecia um intervalo normal, escondendo a pausa. Agora
todo dia do intervalo aparece: dia com commit real vira círculo cheio, dia
sem commit carrega o valor do dia anterior e vira círculo vazado (marcado
`carregado:true` no dado, "sem commit (valor mantido)" na tabela). Legenda
nova embaixo do gráfico explica a diferença. Testado nas 8 páginas, sem
erro. Sem impacto em pontos/percentuais — é só o eixo do gráfico.
