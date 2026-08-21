---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar o destravamento de A/B/C; nenhuma ação pendente — os 3 kernels rodam sozinhos, aviso a conclusão com o teste da hipótese central quando fecharem
referencia: activelearning branch claude/e3prime-seed-7-rwatey @fa83556 (re-coleta) · dataset ghdaru/falco-annotation-cache · kernels falco-e3prime-s42 v2, falco-e3prime-s123 v3, falco-e3-semente-7 v2 · plano v37
criada_em: 2026-08-17T13:30:00Z
---
A re-coleta do E5 fechou e os braços A/B/C das 3 sementes estão rodando.

## Re-coleta do oráculo — concluída

Dois ciclos (SGD e PVBin), oráculo `nvidia/nemotron-3-ultra-550b-a55b` T=0,
mesmo pool (semente de dados 42):

| ciclo | n_labeled | inválidos | tempo |
|---|---|---|---|
| SGD | 3.699 (julho: 4.742) | 51 (julho: 208) | 43 min |
| PVBin | 7.113 (julho: 6.009) | 137 (julho: 241) | 135 min |

**Cache consolidado: 12.152 registros únicos**, validado (zero duplicatas,
zero IDs malformados, zero rótulos fora do schema de 715 classes, proveniência
única). Artefatos e proveniência em
`activelearning/experiments/e5cycle/results/recoleta-20260817/` (branch
designada, commits `e100cae` e `fa83556`) — os originais de julho citados pela
tese permanecem intocados na pasta de cima.

**Incidente registrado**: a primeira tentativa (comando sem `--cache`) rodou
4h45 sem persistir nada — o `CachedOracle` só existe quando `--cache` é
passado, e o comando canônico do E5 não deixa isso escrito. Recuperei via
`gdb` (dump das listas internas do processo vivo, 6.952 itens resgatados sem
perda) em vez de descartar a rodada. Vale registrar essa exigência no
comando canônico do experiments/e5cycle/README ou onde ele estiver
documentado, para não se repetir.

## A/B/C destravados nas 3 sementes

Cache subiu como **dataset privado** `ghdaru/falco-annotation-cache` (regra da
sua tarefa 20260817-0020: não entra no git). Os 3 kernels já com os 6 braços
prontos (D/E/E20/E25/E30/E35) foram reempurrados com `--dataset` +
`--retomar-de`, então cada um roda agora os 9 braços completos, pulando os 6
já feitos:

- `falco-e3prime-s42` — pushed, QUEUED
- `falco-e3prime-s123` — pushed
- `falco-e3-semente-7` — pushed (kernel originalmente do executor01; retomo
  a partir da saída dele, que já estava na main)

Estimativa: 30–45 min por semente (A/B/C juntos são ~9k itens de treino,
pequenos comparado a D). O `run_kaggle.py` acompanha e reempurra sozinho se
alguma sessão cair.

## Honestidade científica para o texto

O cache é re-coleta, não reprodução — os A/B/C que vão sair diferem dos
originais da s42 (preservados em `legacy_s42_bs16_eval20k/`) tanto pelo
regime (canônico vs antigo) quanto pela proveniência do oráculo (nova
amostra). Quando os 3 kernels fecharem, o teste da hipótese central
(F1(A) ≥ 0,95×F1(D)) sai nas 3 sementes, canônico, cache único — o número
mais limpo que o E3′ vai ter produzido até agora.

Plano v37 atualizado (e3p-seed7/123 → rodando; item novo e3p-seed42-abc).
Nada pendente do meu lado agora — os 3 kernels rodam sozinhos; aviso a
conclusão com os números.
