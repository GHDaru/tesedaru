---
de: principal
para: executor02
tipo: tarefa
acao_esperada: você está ocioso — frente independente do E6: INVESTIGAR a discrepância do Cap.4 em L0=100 (duas tabelas dão valores diferentes para o AG), determinar qual execução é a canônica a partir dos artefatos e entregar as duas leituras + o impacto na alegação central, para o principal levar ao autor decidir. Diagnóstico, sem editar texto.
referencia: achado do revisor2 20260822-0744 · 4-resultados-l0/texto.tex tab:ag-evolucao (l.83) e tab:drisl-vs-ag (l.117) · activetextclassification@b540533 (legado) · experiments/p1/results/ na main do activelearning · examples/ag_optimization_results_L0_100old/
criada_em: 2026-08-22T18:00:00Z
---

O revisor2 mediu: em L0=100 o Cap.4 reporta DOIS valores para a mesma grandeza
(AG melhor indivíduo 36,71% em tab:ag-evolucao vs 38,76% em tab:drisl-vs-ag;
pior 10,86% vs 5,75%). Só a linha de 100 diverge; 500/1.000/5.000 batem nas
duas. Uma versão vem de `examples/ag_optimization_results_L0_100old/`.

O que preciso (diagnóstico com evidência, seu estilo):
1. **Qual é a execução canônica?** Compare as duas pastas/artefatos: qual foi
   gerada com o protocolo final (mesma semente/config das linhas 500-5.000) e
   qual é a `_100old`. Diga qual valor os artefatos sustentam para L0=100.
2. **Impacto na alegação central**: o Cap.4 conclui que o DRI-SL (41,23%)
   supera o MELHOR indivíduo do AG. Sob CADA um dos dois valores (36,71% e
   38,76%), a conclusão se mantém? (41,23 > 38,76 ainda é vitória, mas a
   margem muda — reporte a margem nos dois casos.)
3. Entregue as duas leituras + sua recomendação de qual vale ao PRINCIPAL,
   com o caminho do artefato. Não edite o texto (é decisão do autor qual valor
   entra; a correção de texto vem depois, por quem tem a superfície).

Segunda pergunta, à parte: a nova geração de oráculos da tarefa 0120 (GLM 5.1/
5.2, DeepSeek v4 Pro/Flash) chegou a ser rodada? Se sim, onde estão os
resultados; se não, diga que está pendente — não rode agora (custo/créditos),
só reporte o estado, porque afeta a decisão do gate-85.
