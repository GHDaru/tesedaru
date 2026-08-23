---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONFIRMADO — e3prime_E_s{123,42,7}_bs16.json na main SÃO os canônicos (bs16+clipping); re-run parado, não gastou GPU de verdade (nunca saiu da fila de cota); valores finais abaixo para a banca
referencia: main@21aca3d (e demais commits do destravamento do braço E, minha própria autoria) · experiments/e2e3/results/e3prime_E_s{123,42,7}_bs16.json
criada_em: 2026-08-24T06:15:00Z
---

Confirmado. Fiz uma verificação direta antes de simplesmente aceitar,
porque a informação contradizia o que a tarefa 1015 tinha dito 3 dias
antes ("E/s123 homogêneo não existe") — valia checar em vez de assumir.

## Por que são canônicos

`git diff` entre o arquivo na `main` e o mesmo arquivo na minha branch dá
**zero diferença** — são byte-idênticos. E eu reconheço o arquivo: é
exatamente o que produzi quando destravei o colapso do braço E/s123 com
`clip_grad_norm_`, ANTES da tarefa 2015 existir (por isso o nome é
`_bs16`, sem o sufixo `_bs16v2` que só introduzi depois, para os outros 25
braços regenerados). A tarefa 2015 me disse explicitamente para NÃO
retreinar este braço de novo — "é a referência de que o retreino é
estável" — e eu já vinha usando este mesmo arquivo (inalterado) como fonte
do braço E/s123 no McNemar/bootstrap homogêneo que entreguei naquela
tarefa. Ou seja: **não é só canônico — já estava correto em tudo que
entreguei até agora**, incluindo o achado do E35×D que inverte em s7 (esse
usou D e E35, não o E puro, então não muda).

**Causa provável da divergência com a tarefa 1015**: quem procurou deve
ter buscado por `e3prime_E_s123_bs16v2.json` (o padrão de nome dos outros
24 braços regenerados) e não achou — mas os dois braços excluídos da
regeneração (E25/s42 e E/s123) ficam com o nome antigo `_bs16` de
propósito, porque já eram homogêneos antes da tarefa 2015 existir.

## Valores finais (braço E, 3 sementes, regime homogêneo)

| semente | acurácia | Macro F1 |
|---|---|---|
| 42 | 0,8363 | 0,3699 |
| 123 | 0,8046 | 0,3212 |
| 7 | 0,8016 | 0,3041 |

## Re-run parado — não gastou GPU de verdade

Matei o processo local. O push do kernel **nunca foi aceito** pelo Kaggle
— ficou o tempo todo preso em "cota de GPU esgotada", nunca chegou a
"successfully pushed". `kaggle kernels status` mostra `COMPLETE`, mas é o
status da rodada ANTERIOR desse mesmo slug (os 8 outros braços da s123, já
entregues antes) — não uma rodada nova. Custo real desta tentativa: zero
GPU, só o tempo de parede do meu script esperando vaga.

## Tarefa viva: 0530 (repro da população) — já entregue, sem mudança

Entreguei o laudo completo às 06:00 (`tesedaru@4de58c5`): causa-raiz
(população 20 nunca foi commitada no notebook — foi de um placeholder
pop=2 direto para o abandonado pop=50), conserto proposto (fixar 20 no
notebook/JSON versionados com nota de proveniência), e a ressalva de que
não achei artefato pra a "3ª config" de população 100 — preciso da
referência exata do revisor1 pra conferir. Nada novo desde então; segue
como está, aguardando decisão de quem tem a superfície do repo legado.

## Feito / falta / bloqueios

**Feito**: braço E confirmado e parado sem desperdício; laudo da 0530
entregue. **Falta**: nada do meu lado nas duas frentes — braço E fechado,
0530 é laudo puro (não editei nada, decisão é de vocês). **Bloqueios**:
nenhum ativo agora.

## Caixa

Atualizada com esta entrega.
