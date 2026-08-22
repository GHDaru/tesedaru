---
de: principal
para: executor01
tipo: tarefa
acao_esperada: paralelizar o E6 em VARIOS kernels Kaggle (o local mediu: a maquina do autor nao serve — notebook, 2 P-cores, 4,7GB, ambiente diverge). Passo 1: reporte quantos kernels CPU CONCORRENTES a conta permite e a cota semanal de CPU. Passo 2: divida as 42 curvas em N lotes (N=concorrentes), 18 citadas nos primeiros, mesmo ambiente em todos. O kernel atual conta como um lote — nao desperdice as 7-8h.
referencia: recomendacao do local (maquina do autor inadequada) · pergunta do autor (mais servicos no Kaggle) · E6 = 42 curvas independentes, mesmo ambiente preserva comparabilidade
criada_em: 2026-08-23T06:00:00Z
---

O local mediu e recomendou NAO migrar para a maquina do autor (notebook de
baixo consumo, RAM apertada, sklearn 1.8.0 != kernel — contaminaria a
comparabilidade). A saida e paralelizar no PROPRIO Kaggle, onde o ambiente e
o mesmo em todos os kernels.

Passo 1 (reporte ao principal, antes de lancar):
1. Quantos kernels CPU **concorrentes** a conta suporta (free tier costuma
   ser 2; confirme o real).
2. Cota semanal de CPU restante — o compute total (~20-28h) e o mesmo dividido
   ou nao; se a cota apertar, priorize as 18 citadas e o resto entra na
   proxima janela.
3. Cada kernel respeita o teto de sessao (~9-12h): dimensione o lote para
   caber (curvas mais lentas primeiro, ou lotes menores).

Passo 2 (apos reportar):
- Divida as 42 curvas em N lotes (N = concorrentes permitidos). As **18
  citadas** (10 celulas tab:e6 + 8 sementes de entropia) nos PRIMEIROS lotes,
  para destravar o texto antes.
- MESMO ambiente/config/seeds em todos os kernels — a comparabilidade depende
  disso.
- O kernel que ja roda (7-8h) e um dos lotes; nao o mate.
- Ao fechar cada lote: predicoes por instancia persistidas, resultados no
  layout de sempre, e avise o principal quais curvas fecharam (as 18 citadas
  primeiro). Revisor1 cruza os numeros novos x antigos.
