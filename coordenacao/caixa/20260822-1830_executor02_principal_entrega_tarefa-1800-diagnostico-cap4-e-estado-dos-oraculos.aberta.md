---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR e levar ao autor — diagnóstico da tarefa 1800 completo, com recomendação; e achado de governança sobre a tarefa 0120 que precisa de decisão (foi marcada concluída sem ter sido executada)
referencia: tarefa 20260822-1800 · ghdaru/activetextclassification@b540533 (clonado read-only nesta sessão) · 4-resultados-l0/texto.tex tab:ag-evolucao l.83 / tab:drisl-vs-ag l.117 · tarefa arquivada 20260818-0120
criada_em: 2026-08-22T18:30:00Z
---

## 1. Discrepância do Cap.4 em L0=100: qual é a canônica

**`examples/ag_optimization_results_L0_100old/` é a execução canônica —
36,71% (melhor) / 10,86% (pior).** `_100oldold` (38,76% / 5,75%, hoje na
`tab:drisl-vs-ag`) é a que está fora do lugar. Três evidências independentes,
todas na mesma direção:

1. **Convenção de nomes do resto da varredura.** Para L0=500, 1.000, 2.500 e
   5.000 só existe pasta `_<n>old` — não há `_<n>oldold` alternativa para
   nenhum desses tamanhos. As duas tabelas do Cap.4 usam
   necessariamente `_<n>old` para essas quatro linhas, sem ambiguidade.
   `_100old` segue essa mesma convenção; `_100oldold` é a exceção.
2. **Schema do CSV.** `_500old/ag_best_l0_ACCURACY_MAXIMIZE.csv` (referência
   indisputada) tem cabeçalho `metric_value,metric_type,optimization_goal` —
   idêntico ao de `_100old`. `_100oldold` tem cabeçalho diferente
   (`metric_value_on_eval_set`, com BOM `﻿` no início — assinatura de
   outro script/exportador).
3. **Histórico do arquivo no legado** (`git log --follow`, história completa
   após `fetch --unshallow`): `_100old` compartilha exatamente os mesmos 4
   commits de `_500old` (`461533f`→`904047b`→`dacfed3`→`26d7c4e`, "ags" → "l0
   ags" → "genetic alterado" → "rename"). `_100oldold` tem esses 4 **mais
   dois commits extras e posteriores**: `cc74c99` ("Refactor code
   structure...", 27/05) e `a3bf612` (**"oraculo"**, 01/06) — nomes que não
   têm relação com o AG, sugerindo que essa pasta foi tocada por trabalho de
   oráculo alheio à varredura, depois do sweep original ter fechado.

O `experiment_params.json` que só existe em `_100oldold` (pop=50, 100
gerações, PVBin, semente 42) não é evidência de canonicidade — nenhuma das
outras quatro pastas (`_500old` etc., todas indisputadas) tem esse arquivo,
então a ausência é a norma da varredura, não uma lacuna de `_100old`.

**Impacto na alegação central**: nas duas leituras o DRI-SL (41,23%) supera o
melhor indivíduo do AG — a alegação **sobrevive nas duas**. O que muda é a
margem:

| leitura | melhor do AG | margem do DRI-SL |
|---|---|---|
| atual (`_100oldold`, o que está no texto hoje) | 38,76% | +2,47 p.p. |
| **recomendada** (`_100old`, canônica) | 36,71% | **+4,52 p.p.** |

Corrigir para a leitura canônica **fortalece** a alegação, não enfraquece —
é a `tab:ag-evolucao` (36,71%/10,86%) que está certa; é a `tab:drisl-vs-ag`
que precisa da correção na linha de L0=100. Não editei o texto (decisão do
autor, conforme a tarefa pediu).

## 2. Estado dos oráculos de nova geração (tarefa 0120) — achado de governança

Reportando estado, sem rodar nada, como pedido. E preciso trazer um problema
maior que "está pendente":

**A tarefa 0120 está marcada `.concluida` (arquivada em
`coordenacao/arquivo/2026-08/`) mas, pelas evidências que encontrei, nunca
foi executada.** Os números de `deepseek-v4-pro`, `deepseek-v4-flash` e
`glm-5.2` que já aparecem no Cap.5 (l.40-50, S-rand/S-strat) **datam de
20/07** (commit `99f86e9`) — quase um mês **antes** da tarefa 0120 ter sido
criada (18/08). São sobra do bake-off original de oráculos do E0, não uma
nova coleta. Não há reconstrução de cache, não há curva sem critério de
parada, e **GLM-5.1 não aparece em nenhum `.tex` da tese** — conferi todos.
O aviso do revisor2 (20260820-1620, arquivado) já tinha notado exatamente
isso: 3 dos 4 modelos coincidem por acaso com candidatos antigos, só o
GLM-5.1 é genuinamente novo e está ausente.

Também não encontrei a mensagem de plano/custo que a própria tarefa exigia
**antes** de qualquer execução ("quero, em UMA mensagem, antes da execução:
ordem, custo estimado, o que é reaproveitável...") — nunca a escrevi, e não
achei de mais ninguém.

**O que falta, de fato**: tudo — cache reconstruído do zero, curva completa
sem parada antecipada, e a medição dos 4 modelos (3 com número antigo
reaproveitável só como candidato do bake-off, não como entrega da 0120; o
GLM-5.1 nem isso). Isso é relevante para o gate-85: nenhum oráculo, novo ou
velho, cruzou os 85% (o melhor medido é deepseek-v4-pro em 82,6%).

**Não decido isto** — só registro: a tarefa 0120 parece ter sido fechada por
engano, possivelmente arrastada pela integração em massa de 21/08
("missoes-dos-executores-fechadas", 10 tarefas fechadas de uma vez). Se o
autor ainda quiser essa frente (reconstrução + GLM-5.1 + curva completa),
ela precisa ser reaberta como tarefa nova — não decido isso sozinho, é
prioridade de fila e custo de GPU/créditos, decisão de vocês/autor.

## Fechamento

Não alcanço a `main` para fazer o `git mv` de nenhuma das duas tarefas
(1800/0120) — sessão restrita à branch designada. Peço que marque a 1800
como `.concluida` do seu lado com esta entrega, e que decidam o que fazer
com a 0120 (reabrir como tarefa nova, ou arquivar como decisão consciente
de não perseguir).

Repositório legado clonado nesta sessão só para leitura
(`ghdaru/activetextclassification@b540533`, mesmo commit citado nas suas
referências) — nenhuma escrita, constituição respeitada.

Caixa atualizada: esta é a única mensagem nova da minha fila desde a última
entrega (grad_clip, 20260822-0445). Sem tarefa pendente depois desta.
