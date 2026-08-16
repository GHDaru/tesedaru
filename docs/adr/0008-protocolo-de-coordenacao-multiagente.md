# ADR 0008 — Protocolo de coordenação multiagente (mensagens + locks via git)

- **Status**: Proposta (aguarda gate do autor) · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (pedido em conversa; gate pendente)

## Contexto

Quatro sessões de IA (principal, banca, revisor1, revisor2) + o autor passam a
trabalhar em paralelo no mesmo repositório. O único meio comum é o git;
containers morrem sem avisar. O autor pediu: pasta de mensagens com ciclo
aberta→em-andamento→concluída por renomeação, servindo também de lock. Dois
especialistas (mensageria e processo) produziram as bases.

## Decisão

Adotamos `coordenacao/` na main com PROTOCOLO.md v1.0: nome de arquivo codifica
data-hora UTC, remetente, destinatário, tipo e estado (transição por git mv);
front matter com para:/acao_esperada: obrigatórios (anti-spam); locks com nome
determinístico por superfície, claim por push fast-forward (só é seu após push
aceito), TTL 45 min + heartbeat 15 min medidos pelo timestamp do commit, quebra
permitida só após TTL e com aviso; 4 eventos geram mensagem (claim, achado
cross-agente, bloqueio, conclusão); superfícies com dono único como padrão
(prosa=principal, pareceres=banca, fichamentos por revisor) e lock como exceção;
verificação cruzada (banca→principal, revisor1↔revisor2, autor=instância final);
escalonamento em uma réplica com arbitragem do autor; métricas de saúde
(mensagens/commits, idade de bloqueio, retrabalho pós-gate).

## Alternativas consideradas

- **Issues/PRs do GitHub como mensageria**: nativo — descartado: sessões operam
  melhor sobre arquivos no clone; issues não dão lock nem TTL barato.
- **Lock otimista só (sem pasta de locks)**: menos artefatos — descartado: o
  custo do conflito em prosa longa é alto demais; lock explícito é mais barato.
- **Broker externo (fila/banco)**: fora do princípio de artefatos no git.

## Consequências

- (+) Coordenação auditável no histórico; caixa de entrada legível por `ls`.
- (+) Sessões mortas não travam o sistema (TTL) e não se perdem entregas.
- (−) Overhead por ciclo (aviso + lock + heartbeat); mitigado pelos limites e
  pela regra dos 4 eventos.
- (−) Repositório público: disciplina estrita de nunca pôr segredo em mensagem.

## Registro

`coordenacao/` (PROTOCOLO.md, caixa/, locks/, arquivo/); primeiro aviso
broadcast publicado; seção no CLAUDE.md; linha no decisoes.jsonl.
