---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: (1) AUTORIZADO o conserto das 5 autorias corrompidas num commit só na bibfix/lotes (Ren2021 com o DOI certo 10.1145/3472291 incluído), conferindo cada uma na fonte; (2) executar os 4 renomeios PDF+fichamento da tarefa da banca 20260817-0307 (determinação do autor); ao final, avisar com hash — o GATE FINAL do bib vai ao autor com tudo dentro
referencia: seu aviso 20260817-0331 · tarefa da banca 20260817-0307 · bibfix/lotes @162c12b
criada_em: 2026-08-17T04:20:00Z
---
Dois itens, ambos fecham o pacote do gate final:

1. **5 autorias corrompidas — AUTORIZADO.** Sua descoberta do padrão (≥5
   autores → prenomes preenchidos por plausibilidade) e o script
   check-autoria.py entram como o TERCEIRO invariante do ciclo. Ren2021:
   corrigir DOI para 10.1145/3472291 e restaurar Brij B. Gupta.
2. **Renomeios do Cap. 1** (Alsmadi2019, Song2014, Devlin2019,
   zhang-etal-2022-survey): git mv nos pares PDF+fichamento + id/pdf no
   front-matter, como a banca especificou. Banca confere depois.

Registro também: o item Deng não precisava (conserto já estava no lote 1 do
revisor2) — a lição do "conferir se já existe antes de refazer" agora vale
para tarefas, não só para entradas; vou checar a branch do bib antes de
despachar conserto de bib daqui em diante.
