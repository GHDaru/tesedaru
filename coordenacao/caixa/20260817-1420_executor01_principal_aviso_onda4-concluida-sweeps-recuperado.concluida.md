---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma decisão nova — registro de fechamento; sigo para a Onda 5 (índice final)
referencia: activelearning notebooks/auditoria/estrategias-e-robustez.ipynb · experiments/e1e4/results/sweeps.jsonl
criada_em: 2026-08-17T14:20:00Z
---
**Onda 4 concluída** (E1/E4). Diferente de todas as ondas anteriores: não
havia dado bruto versionado, então não é reanálise — **reexecutei as 104
células do zero**, medindo o custo antes (1 célula, ~18 s) para não disparar
às cegas: ~30 min de CPU no total, sem GPU.

## Reprodução quase exata — melhor do que eu esperava

O `run_sweeps.py` fixa a semente do pool (`random.Random(7)`), então a
reexecução não é "mesmo desenho, amostra diferente" — é o **mesmo pool**.
Resultado: as cinco estratégias do E1 e os seis pares ε×estratégia do E4
reproduzem os agregados publicados até a 3ª/4ª casa decimal. **Zero
divergências.**

## O artefato que faltava, agora existe

`experiments/e1e4/results/sweeps.jsonl` (104 células, 112 KB) — commitado com
`git add -f`, exatamente como eu tinha previsto no lote 2 (a linha 7 do
`.gitignore` casa). As conclusões do Cap. 5 sobre E1/E4 deixam de depender só
de um agregado; agora há o dado por célula por trás.

## Defeito meu, achado ao olhar a figura

O eixo Y do gráfico de curvas duplicava rótulos (0,1 aparecia duas vezes, 0,2
também) — o matplotlib escolhe passo de 0,05 e meu formatador arredondava
para 1 casa decimal. Corrigido para 2 casas antes de commitar.

## Placar geral

`rastreabilidade.json`: **74 itens · 62 rastreados · 10 divergentes · 1 sem
evidência · 1 legado**. Só resta uma lacuna de dado bruto: as figuras de
`experiments/plots/`, que o script gera mas nada versiona — não é prioridade
igual às anteriores, porque não sustenta número, só a imagem.

## Próximo

**Onda 5**: `00-visao-geral.ipynb`, o índice que lista os 8 experimentos e o
estado de cada auditoria. É o fechamento da missão.
