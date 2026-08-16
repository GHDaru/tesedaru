# ADR 0011 — Identidade de agente pelo título da sessão

- **Status**: aceita
- **Data**: 2026-08-16
- **Decisor**: autor (Gilsiley Henrique Darú), via principal
- **Contexto**: com 8 agentes em sessões paralelas, houve caso real de sessão
  sem saber qual papel exercia (perguntas 20260816-2049 e 20260816-2056), e
  caso real de título trocado (sessão "Revisor 01" exercendo o papel de
  revisor2), corrigido pelo autor renomeando as sessões em 2026-08-16.

## Decisão

1. **A fonte de verdade da identidade de um agente é o título da sua própria
   sessão**, consultado com a ferramenta `get_session` (servidor MCP
   `claude-code-remote`) sem `session_id` — nunca a memória da conversa, nunca
   suposição. Aviso operacional: `coordenacao/caixa/20260816-2044_principal_
   todos_aviso_identidade-pelo-titulo-da-sessao.aberta.md`.
2. **Conflito com papel ocupado** (emenda sugerida pelo revisor2, acolhida):
   se o título da sessão apontar para um papel que OUTRA sessão ativa já
   exerce, o agente NÃO assume o papel do título — mantém o papel que vinha
   exercendo e avisa o principal. Só o autor resolve o conflito (renomeando
   sessões ou reatribuindo papéis). Foi exatamente o comportamento que evitou
   colisão no caso real.
3. O endereçamento das mensagens continua pelos **nomes canônicos de papel**
   (`principal`, `banca`, `revisor1`, `revisor2`, `site`, `executor01`,
   `executor02`, `autor`) no nome do arquivo — sem IDs de sessão. O papel é
   durável; a sessão é descartável.

## Consequências

- O §0 do PROTOCOLO.md ganha o passo de auto-identificação antes da leitura
  da caixa (emenda v1.2).
- Sessão com título fora do registro de agentes trabalha em nada até o
  principal responder quem ela é.
