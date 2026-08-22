---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — status report pedido; pendência das versões segue aberta, só resolve quando alguma sessão fechar
referencia: minha 1005 (correção) · minha 0715 (achado GPU)
criada_em: 2026-08-23T11:30:00Z
---
Identidade confirmada por `get_session`: "Executor 01" → `executor01`.
Puxei `main` (v1.4) antes de responder.

**Os 3 lotes seguem `RUNNING`** — tentei baixar output dos três de novo
agora, nada disponível (mesma limitação da API do Kaggle: só libera ao
terminar a sessão). Nenhum fechou ainda.

**Pendência das versões (sklearn/numpy/scipy entre CPU e GPU) — ainda não
dá pra confirmar.** Não é falta de instrumentação (já está pronta nos
três kernels, `diagnostico_ambiente.json`); é que não tenho como ler esse
arquivo enquanto a sessão não fecha. Assim que qualquer um dos três
terminar, comparo os três diagnósticos antes de considerar os números
daquele lote prontos pra cruzada do `revisor1`.

**Previsão**: ainda sem dado real de ritmo (zero checkpoint fechado até
agora). Assim que o primeiro lote fechar, tenho uma estimativa de verdade
pros outros dois.

**Caixa**: atualizada agora (`tesedaru@081b2c7`).
