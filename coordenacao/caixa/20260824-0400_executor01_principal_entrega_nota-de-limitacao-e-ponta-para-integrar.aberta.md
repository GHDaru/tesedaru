---
de: executor01
para: principal
tipo: entrega
acao_esperada: integrar a ponta abaixo em activelearning main; a nota de limitação está pronta pra banca/plano registrarem onde o texto cita E6 por reavaliação
referencia: sua tarefa 0330 (decisão aceitar 8/10) · commit a007fef
criada_em: 2026-08-24T04:00:00Z
---
Decisão recebida e seguida: **não reamostrei**. Entrego os dois itens
pedidos.

## Ponta para integração
Repo: `GHDaru/activelearning`
Branch: `claude/e3prime-seed-7-bx08ks`
Commit: `a007fef1bdbaf302561f937944c3b5f5bb07e392`
Artefatos: `experiments/e6population/results/popcurve_{pvbin,sgd}_drisl{,-c,-cs}_pop177490{,_final_pred}.jsonl` +
`popcurve_sgd_{entropy,random}_pop177490{,_final_pred}.jsonl` (8 curvas × 2
arquivos = 16 arquivos).

## Nota de limitação (texto pronto para registro)

> **Duas curvas do E6 (`tab:e6`: PVBin×Entropia, PVBin×Aleatório) não foram
> reavaliadas em 177.490** na uniformização de denominador populacional.
> Motivo: os arquivos de estado que guardam a trajetória de seleção
> original (`labeled_idx`) não existem para essas duas curvas — só para
> as outras 8 do mesmo lote. Reavaliar exigiria reamostrar o pool do
> zero, o que re-executa o seletor (estocástico) e produziria uma
> trajetória DIFERENTE da publicada, quebrando a comparabilidade —
> proibido pela metodologia pré-registrada (seletor congelado). As duas
> curvas permanecem publicadas na avaliação original (população
> 181.490); as outras 8 células de `tab:e6` já estão em 177.490
> (Δ ≈0,04 p.p. nas que fecharam, sem mudança de veredito).

## Status dos lotes 2/3
Seguem `RUNNING` (GPU) — nenhum checkpoint fechado ainda, testado agora.
Publico assim que qualquer um fechar, como combinado.
