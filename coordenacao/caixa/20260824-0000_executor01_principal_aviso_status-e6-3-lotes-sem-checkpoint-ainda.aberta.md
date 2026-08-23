---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — status report pedido; assim que um checkpoint fechar, publico o sumário 177.490 na hora, como pedido
referencia: E6 (2020/1915/0600) · 1130 · aviso 1335 (GPU: não parar meus kernels, braço E espera na fila)
criada_em: 2026-08-24T00:00:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Puxei `main` nas duas branches (v1.4/v1.5), sem conflito e
sem novidade endereçada a mim.

**Colab/Databricks**: ciente, seguem cancelados — nada a fazer aí.

**E6 — os 3 kernels ainda `RUNNING`**, testado agora mesmo (status +
tentativa de baixar output dos três, nada disponível ainda). **Nenhum
checkpoint fechou até este momento.** Assim que qualquer um fechar,
publico o sumário 177.490 daquele lote na hora — branch + caixa, nunca
`main` — para destravar a cruzada do `revisor1` e liberar o slot de GPU
pro braço E do `executor02`, como pedido.

**Feito, com hash**: `activelearning@5ca92d0` (bug do output corrigido),
`f810a54`+`5632ae7` (diagnóstico de hardware/versões + RSS por
checkpoint), `611f2c9` (divisão em lotes via `--curves`).

**Falta**: qualquer sessão fechar → comparar `diagnostico_ambiente.json`
entre CPU e GPU (pendência desde 0715, ainda sem dado real pra confirmar
ou refutar) → copiar resultados → repetir até as 42 curvas fecharem →
relatório final Δ vs 181.490 pro `revisor1`. Depois disso, começa a 1130
(passe final de recálculo), ainda não iniciada.

**Bloqueios**: nenhum agora. A cota de CPU (5 pushes) segue sem uso
adicional necessário — os 3 lotes já estão rodando. GPU: só 2 slots, os
dois ocupados pelos meus lotes 2/3; braço E do `executor02` na fila,
decisão do autor já tomada (não parar os meus).

**Previsão / ritmo**: ainda sem dado real — zero checkpoint fechado em
qualquer lote, então não tenho como estimar velocidade de verdade ainda.

**Entrega presa em branch (medido agora)**: em ambos os repositórios,
minha branch (`tesedaru@c20c9ce`, `activelearning@611f2c9`) NÃO é
ancestral de `origin/main` — os commits/avisos deste ciclo aguardam sua
integração.

**Caixa**: atualizada agora, sem pendência de merge.
