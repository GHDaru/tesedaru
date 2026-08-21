---
de: executor02
para: principal
tipo: tarefa
acao_esperada: URGENTE — decisão do autor sobre corrigir bertimbau.py (gradient clipping) antes de eu tocar código compartilhado por todos os resultados já publicados; enquanto isso sigo sem editar nada
referencia: activelearning@4266c26 · minha mensagem 0120 · plano v67 · src/activelearning/adapters/classifiers/bertimbau.py:96-113
criada_em: 2026-08-18T01:35:00Z
---
Confirmado: o colapso do braço E25 (semente 42, lote 16) é **determinístico
e reprodutível**, não foi azar de uma execução.

## A prova

Retreinei E25 isoladamente, mesmos parâmetros exatos (semente 42, lote 16,
mesmos dados). Resultado:

- Acurácia: **0,0153 nas duas execuções**, IC de Wilson idêntico
  ([0,0147; 0,0159] nas duas).
- Predições: **byte-idênticas** — as 177.490 predições da segunda execução
  são exatamente iguais, item por item, às da primeira. Todas na mesma
  classe ("outro farma").

Isso só é possível se o treino for, na prática, totalmente determinístico
neste ambiente (mesma semente, mesma GPU T4, mesmo software) — o que também
explica por que os braços A/D/E35 reproduziram os mesmos números quando
retreinaram sem querer no sweep (mensagem 0120).

## O que isso significa

Não adianta reexecutar E25 esperando um resultado diferente — vai colapsar
de novo, sempre. A causa segue sendo a que apontei: `AdamW` sem *gradient
clipping* nem *warmup* de taxa de aprendizado em
`BertimbauClassifier.fit()` (`src/activelearning/adapters/classifiers/
bertimbau.py:96-113`), combinado com o ruído maior de gradiente do lote 16.
Nesta combinação específica de dados (o prefixo de 25 mil da trajetória de
entropia) e semente, o treino cai num mínimo degenerado logo cedo e nunca
sai.

## Por que não corrijo sozinho

`bertimbau.py` é o classificador usado por **todos** os resultados E2/E3′
já publicados na tese — canônicos (lote 128) e todo o resto do sub-treino
(lote 16, os outros 26 braços que já rodaram sem esse problema). Adicionar
`clip_grad_norm_` é uma correção pequena, padrão e bem justificada
tecnicamente, mas:

1. Muda o comportamento de um componente citado implicitamente em números
   já no texto — mesmo que os OUTROS resultados provavelmente não mudem
   (clipping só age quando o gradiente já está grande demais; treinos que
   convergiram bem não deveriam ser afetados), não posso garantir isso sem
   medir, e não vou medir modificando o código sem sinal verde.
2. É uma decisão de método, não só um bug de execução — cabe ao autor.

## O que preciso

Uma decisão, com três caminhos possíveis (não escolho por vocês):

- **(a)** Autorizar a correção (`clip_grad_norm_`, valor típico 1.0) em
  `bertimbau.py`, com o `--force` de `run_e3prime.py` reexecutando SÓ o
  E25/s42/bs16 para confirmar que resolve — e eu registro no texto/README
  que essa mudança de código aconteceu nesta data, com o motivo.
- **(b)** Aceitar o E25/s42/bs16 como dado perdido/inválido — a varredura
  de orçamento (E, E20, E25, E30, E35) fica com um ponto faltando nessa
  semente; ainda dá para interpolar visualmente ou reportar como "falha de
  treino, célula omitida".
- **(c)** Trocar só o lote deste braço específico para algo intermediário
  (ex.: 32) como contorno pontual, sem mexer em `bertimbau.py` — mantém o
  restante do experimento como está, mas quebra a comparabilidade estrita
  "mesmo lote em todos os 9 braços" que é o ponto do sub-treino.

Minha recomendação, se puder opinar: **(a)**. É a correção mais honesta
tecnicamente (o resto do experimento não devia estar rodando sem clipping
para começo de conversa) e a mais barata (uma linha de código, um
retreino de ~9 min já pronto para rodar).

## Enquanto aguardo

Não fico parado: a varredura de s123 segue rodando (ainda RUNNING). Se ela
também colapsar em algum braço, vou aplicar o mesmo protocolo de
diagnóstico (retreino isolado + checagem de colapso) antes de reportar.

Plano v67 atualizado, bloqueio explícito no item `e3p-varredura-bs16`.
