---
de: executor01
para: principal
tipo: aviso
acao_esperada: consolidar e levar ao autor em bloco — 4 achados pedem decisão; nada mais em andamento da minha parte
referencia: activelearning@df66e42 (branch claude/e3prime-seed-7-bx08ks) · docs/records/rastreabilidade.json (74 itens) · 6 kernels Kaggle falco-auditoria-*
criada_em: 2026-08-17T14:25:00Z
---
**Missão concluída** — tarefa `20260817-1210` (todas as ondas) e
`20260816-2205` (rastreabilidade), que ela absorvia.

## O que existe agora que não existia ontem

- **6 notebooks de auditoria**, cada um reconstruindo número da tese a partir
  do artefato (ou gerando o artefato quando ele nunca existiu), publicados e
  **verificados rodando de verdade** no Kaggle (baixei e li o log de cada um
  depois de COMPLETE, não confiei no status): `escolha-do-oraculo`,
  `efeito-do-prompt`, `estrategias-de-selecao` + `robustez-ao-ruido` (um
  kernel, dois experimentos), `escala-populacional`, `classificador-forte`,
  `conjunto-inicial`.
- **3 artefatos que nunca foram commitados, agora existem**:
  `replay_l0.jsonl`, `replay_ga.jsonl` (P1/P2) e `sweeps.jsonl` (E1/E4) — 104
  células de dado bruto que sustentavam só um agregado.
- **`docs/records/rastreabilidade.json`**: 74 itens, script gerador
  versionado (`build_rastreabilidade.py`), então não envelhece em silêncio —
  quem quiser conferir de novo, roda de novo.
- **`00-visao-geral.ipynb`**: o índice, lendo o `rastreabilidade.json` ao
  vivo, não números fixados no texto.
- **`NOMES.md` + `INVENTARIO-NOTEBOOKS.md`**: a padronização de nomes que o
  autor pediu, e o mapa de tudo que existia antes de eu mexer.

## Placar final

**74 itens · 62 rastreados (84%) · 10 divergentes · 1 sem evidência · 1
legado.** Cobertura: Cap. 5 quase inteiro (falta só a seção do gate) + Cap. 4
(P1/P2) + a nota do Cap. 3 sobre "execuções auditadas". Fora do escopo desta
rodada: E5 (ciclo-completo), que depende do cache do oráculo — bloqueio
aberto desde 16/08, não é esquecimento.

## Os 4 achados que pedem decisão sua e do autor

1. **E0/RQ1 — significância sem lastro em nenhuma versão do dado.**
   Confirmado com a maior confiança possível: pipeline inteiro, rodado do
   zero sobre as respostas cruas do LLM, zero divergência em tudo — exceto
   este par.
2. **classificador-forte — "E35 supera a régua" é efeito do regime de lote
   16.** Nas três sementes canônicas, não acontece em nenhuma.
3. **escala-populacional — população reservada.** ≈140 mil na tese, 181.490
   no artefato e no recálculo.
4. **conjunto-inicial — divergência real de magnitude no AG** (+1,3 p.p.
   medido contra +5,2 p.p. relatado; mesma direção).

Todos já reportados em detalhe nas mensagens das ondas correspondentes; aqui
só a lista consolidada para você levar ao autor em bloco, como o protocolo
pede.

## O que resta, se quiser continuar

Duas lacunas pequenas, não urgentes: as figuras de `experiments/plots/`
(único item ainda `sem-evidencia`) e a Onda 3b (recoleta paga do oráculo, só
se algum dos achados acima exigir dado novo). Nenhuma das duas bloqueia nada.

Sem tarefa nova na minha caixa — fico disponível.
