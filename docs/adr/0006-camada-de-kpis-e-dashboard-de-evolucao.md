# ADR 0006 — Camada de KPIs em pontos de esforço e dashboard de evolução

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú ("quero um dashboard... chame um especialista em indicadores e um UX")

## Contexto

O painel v2 mostrava status, mas não evolução nem prioridade. Dois especialistas
(subagentes) produziram os documentos de base: a camada de indicadores e o
ux-design (agente ux-semantics do Maestro).

## Decisão

1. **Moeda única = pontos de esforço**, nunca contagem de células: célula
   capítulo×rodada pesada pelas dimensões reais do capítulo (R1: 1,0×travessões;
   R3: 2,5×citações; R5: 0,4×tokens numéricos; R2/R4/R6/R7 fixos; piso 5).
   Contagem de células foi banida como métrica de vaidade.
2. **Seis KPIs**: Prontidão Global (0,85×texto + 0,15×artefatos bloqueantes;
   crédito feito=1, gate=0,9, andamento=0,5, com override `progresso` e crédito 0
   para célula bloqueada); Velocidade (pontos/semana, janela 14d, série do git
   log do plano); ETA (guarda: indeterminado se velocidade <10); Fila do Autor;
   Pontos Represados (fecho de `bloqueado_por`); Dívida de Fundamentação
   (citações pendentes + chaves sem fichamento). Cortados: % de células, nº de
   commits, lead time de gate, KPI de ARS (vira meta estática de rodapé).
3. **Schema**: plano v3 ganha `dimensoes` por capítulo e `progresso`/
   `bloqueado_por` por célula; KPIs vivem em `docs/records/kpis.json`
   (recomputado por `scripts/compute-kpis.py`, sem lógica no front).
4. **UX**: hierarquia em 6 zonas (KPIs → Fila do Autor → próximo passo do agente
   → burn-up → matriz → telemetria); UM único grito visual, e ele pertence ao
   autor (fila de gates, âmbar, nunca dentro de details fechado); burn-up de
   linha única com Y fixo 0-100 e X em datas reais (semanas paradas visíveis);
   estados por ícone+letra+cor (🔒 gate distinguível em cinza); anti-padrões
   registrados: percentual de vaidade sem decisão vizinha, eixo por commit,
   gate afogado na matriz.

## Alternativas consideradas

- **Progresso por células concluídas**: simples — descartado: 4 células feitas
  parecem 8,5% mas valem 5,4% em pontos; incentivaria fechar células baratas.
- **Registrar série à mão**: descartado; o git log do plano é a série, sem
  bookkeeping.
- **Gráfico espaçado por commit**: descartado pelo UX — apaga semanas paradas.

## Consequências

- (+) "Quanto falta" honesto (PGP 4,6% na primeira medição — o número duro real).
- (+) Priorização objetiva: as sementes do Colab destravam ~230 pontos, topo da fila.
- (−) Pesos são estimativas de custo; recalibráveis por ADR se a prática divergir.
- (−) Crédito 0,9 em gate pode inflar estoque parado; mitigação futura: regressão
  do crédito após 14 dias em gate (anotada, não implementada).

## Registro

Plano v3; scripts/compute-kpis.py; docs/records/kpis.json; template v3 do
painel; workflow com etapa de KPIs; documentos dos especialistas na conversa de
2026-08-16.
