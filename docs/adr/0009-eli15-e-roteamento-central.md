# ADR 0009 — Comunicação ELI15 com o autor e roteamento central pelo principal

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (ditado em conversa)

## Contexto

Com 4 agentes paralelos ativos e a caixa de mensagens em uso real, o autor
identificou dois riscos: (a) respostas comprimidas/telegráficas dificultam a
decisão dele; (b) mensagens fluindo diretamente entre agentes e ao autor tiram
dele o controle do que exige decisão humana.

## Decisão

1. Princípio XI (constituição v1.2.0): toda comunicação ao autor é didática e
   detalhada — termos explicados, siglas abertas, sem telegrama.
2. Princípio XII: o principal é hub obrigatório — mensagens ao autor só via
   principal; agente↔agente via principal (broadcast de claim/conclusão segue
   direto); planejamento só pelo principal.
3. PROTOCOLO v1.1 ganha o §2-bis (roteamento) e a regra do lock em gate
   (liberar ao entregar para gate; a proteção passa a ser o estado "gate").
4. Aviso do autor publicado na caixa (registrado pelo principal a pedido dele).

## Alternativas consideradas

- **Hub só para mensagens ao autor** (agente↔agente livre): menos gargalo —
  descartada: o autor quer triagem única ("senão perdemos o controle").
- **Sem regra de estilo**: descartada: o autor a ditou explicitamente.

## Consequências

- (+) Um único ponto de triagem; o autor vê apenas o que exige decisão dele.
- (+) Decisões chegam ao autor com contexto completo.
- (−) O principal vira gargalo potencial; mitigação: broadcasts diretos e
  limite de mensagens ativas já existentes.

## Registro

Constituição v1.2.0; PROTOCOLO v1.1; CLAUDE.md; aviso na caixa; este ADR.
