# ADR 0001 — Humanização calibrada da tese, capítulo a capítulo, com gate humano por merge

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: humanize-01 · **Decisor**: Gilsiley Henrique Darú (instrução em conversa, 2026-08-16)

## Contexto

Auditoria com a skill `humanizer` (padrões de escrita de IA, base Wikipedia/WikiProject
AI Cleanup, adaptados ao português acadêmico) varreu os 8 arquivos de texto da tese.
Resultado: vocabulário de IA, muletas e atribuições vagas praticamente zerados; os
achados concentram-se em 4 padrões de ritmo — densidade de travessões (323 no total;
21–22/1000 palavras no resumo/abstract), fórmula enumerativa repetida ("N leituras/
achados/escolhas…", 8×), staccato telegráfico no Cap. 5 (6×) e fecho retórico do
Cap. 6 (tríade + aforismo). Aplicar a skill crua removeria TODOS os travessões — regra
calibrada para prosa web em inglês, inadequada ao registro acadêmico de PT-BR.

## Decisão

1. Adotamos humanização **calibrada** (não a regra crua da skill): reduzir densidade de
   travessões preservando os que fazem trabalho real; quebrar fórmulas repetidas;
   manter negritos definicionais, tríades técnicas e o registro formal.
2. Executamos **capítulo a capítulo**, na ordem 1→6 + resumo/abstract, cada capítulo em
   branch própria (`humanize/capN`).
3. Cada alteração é apresentada **antes/depois na conversa** antes do merge; o **merge é
   gate humano inegociável** (mapa de gates do Maestro, classe "criação reversível").
4. Toda decisão do processo é registrada em ADR imutável + linha em
   `docs/records/decisoes.jsonl` (índice append-only consultável).

## Alternativas consideradas

- **Aplicar a skill crua (zero travessões)**: máxima remoção de sinais — descartada:
  destruiria tipografia legítima de PT-BR acadêmico e o registro formal esperado pela banca.
- **Aplicar tudo de uma vez, sem gates**: mais rápido — descartada: o autor exige
  rastreabilidade e controle de decisão; edições de estilo em texto de defesa são
  irreversíveis na prática após impressão/depósito.
- **Não fazer nada**: mantém 4 clusters de padrão de máquina detectáveis — descartada:
  o autor decidiu tratar.

## Consequências

- (+) Rastreabilidade decisão→edição→merge por capítulo, auditável por terceiros.
- (+) Texto preserva registro acadêmico; remove-se apenas assinatura de máquina.
- (−) Processo mais lento: um ciclo de gate por capítulo (~8 gates).
- (−) Branches de vida curta exigem disciplina de merge para não divergirem da main.

## Registro

Branch `humanize/cap1`; edições em `1-intro/texto.tex`; índice em
`docs/records/decisoes.jsonl`; auditoria quantitativa reportada na conversa de
2026-08-16 (tabela de padrões por capítulo).
