---
de: executor02
para: principal
tipo: aviso
acao_esperada: ciência do progresso (s7 completa) e do achado metodológico (E25 colapsou); se o retreino confirmar colapso reprodutível, vou precisar de decisão sobre tocar bertimbau.py (código de experimento compartilhado) — aviso quando souber
referencia: activelearning@4266c26 (branch claude/e3prime-seed-7-rwatey) · plano v66
criada_em: 2026-08-18T01:20:00Z
---
Progresso da varredura completa (9×3, lote 16) + um achado metodológico que
pode ser mais importante que qualquer número isolado.

## Progresso

- **s7: 9/9 braços completos**, sweep automático ponta a ponta sem
  intervenção. E30 e E35 superam D nas duas métricas; E25 cruza os dois
  critérios da hipótese central.
- **s42: 8/9** — E25 colapsou (ver abaixo). Os outros 8 publicados.
- **s123: rodando** (kernel `falco-subtreino-s123`).

## Achado metodológico: E25/s42/lote16 colapsou — e pode ser reprodutível

O braço E25 (25 mil itens) treinou o tempo todo (553s, nada travou) mas o
modelo **degenerou**: previu a MESMA classe ("outro farma") para as
177.490 instâncias da avaliação, sem exceção. Macro F1=0, acurácia=0,0153.

**Diagnóstico**: `BertimbauClassifier.fit()` usa `AdamW` sem *gradient
clipping* nem *warmup* de taxa de aprendizado
(`src/activelearning/adapters/classifiers/bertimbau.py`). Lote 16 dá
gradientes mais ruidosos que lote 128 — mais chance de uma sequência de
passos grandes empurrar o modelo para esse mínimo degenerado. É um risco
conhecido e bem documentado de treino com lote pequeno sem essas duas
salvaguardas.

**O que descobri no caminho, sem procurar**: ao investigar se um retreino
simples resolveria, percebi que os braços A, D e E35 desta MESMA sessão
reproduziram **exatamente** os mesmos `macro_f1`/`acurácia` das execuções
anteriores (só o tempo de treino mudou) — o que sugere que, neste ambiente
(mesma semente, mesmo hardware T4, mesmo software), **o treino é
determinístico na prática**, mesmo sem eu ter configurado isso
explicitamente. Se for esse o caso, o colapso do E25 **não é azar de uma
execução** — é reproduzível, e uma simples nova tentativa com os mesmos
parâmetros vai colapsar de novo.

**Retreino isolado já disparado** (`falco-retry-e25-s42-bs16`) com detecção
de colapso embutida (conta quantas classes distintas o modelo prevê). Dois
desfechos possíveis:
- **Colapsa de novo** → confirma reprodutibilidade; a correção exige mudar
  `bertimbau.py` (adicionar `clip_grad_norm_`, o remédio padrão) — isso é
  código de experimento compartilhado, citado implicitamente em TODOS os
  resultados já publicados da tese. Não vou tocar nisso sem sua/do autor
  decisão explícita, mesmo sendo uma correção pequena e bem justificada.
- **Recupera** → foi mesmo raro/específico deste ponto; seguimos sem mudar
  código, só registrando que lote 16 tem esse risco ocasional.

Aviso o resultado assim que o retreino terminar (~15 min de execução).

## Bug menor de ferramenta (não bloqueia nada)

A retomada que eu tinha montado para o sweep de s42 (reaproveitar os 3
braços já feitos via `--retomar-de`) não funcionou — o log mostrou "já
concluídos: nenhum", então os 9 braços treinaram do zero (~30 min extra de
GPU, sem prejuízo além do tempo). A pista da determinância acima veio
justamente de comparar os resultados "recalculados" com os antigos.
Investigo com calma depois; não impede a varredura de fechar.

Plano v66 atualizado.
