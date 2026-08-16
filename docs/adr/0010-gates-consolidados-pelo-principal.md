# ADR 0010 — Gates de merge consolidados pelo agente principal

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (ditado em conversa)

## Contexto

Com quatro agentes paralelos entregando trabalho, pedidos de aprovação avulsos
chegavam ao autor de várias frentes. Ele relatou perda de foco e de controle
("estou com dificuldade em fazer o controle e ter foco").

## Decisão

1. Todo gate de merge sobe pelo principal: o agente entrega a branch e manda
   mensagem de conclusão (o que mudou, hash/branch, evidência, risco); o
   principal verifica, consolida e leva ao autor em bloco, com antes/depois e
   recomendação.
2. Exceção única: alterações do site/painel (docs/records/*, scripts de render,
   coordenacao/) seguem sem gate — reversíveis e sem efeito no texto ou dados.
3. Registro em PROTOCOLO §2-bis, constituição v1.2.1 (princípio XII) e CLAUDE.md.

## Alternativas consideradas

- **Gates diretos por agente**: menor latência — descartada: é a causa do
  problema relatado.
- **Gate único semanal**: previsível — descartada por ora: travaria entregas
  rápidas; pode ser adotada se o volume crescer.

## Consequências

- (+) O autor decide em bloco, com contexto comparável entre pedidos.
- (+) O principal filtra o que não está pronto antes de consumir atenção humana.
- (−) Latência adicional para o agente que entregou; mitigada pela regra de
  nunca esperar parado (pega o próximo item).

## Registro

PROTOCOLO v1.1 §2-bis; constituição v1.2.1; CLAUDE.md; aviso na caixa; este ADR.
