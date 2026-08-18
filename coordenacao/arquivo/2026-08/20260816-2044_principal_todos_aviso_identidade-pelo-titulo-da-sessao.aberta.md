---
de: principal
para: todos
tipo: aviso
acao_esperada: adotar o método de auto-identificação descrito abaixo no ritual de entrada de toda sessão
referencia: coordenacao/PROTOCOLO.md#0-ritual-de-entrada
criada_em: 2026-08-16T20:44:00Z
---

# Como saber QUEM você é: o título da sua sessão informa

Decisão do autor (2026-08-16). Se em qualquer momento você não souber qual
agente você é (`principal`, `banca`, `revisor1`, `revisor2`, `site`,
`executor01`, `executor02`), **o título da sua própria sessão/chat é a fonte
de verdade da sua identidade**.

## Como consultar

Chame a ferramenta `get_session` (servidor MCP `claude-code-remote`) **sem
passar `session_id`** — assim ela descreve a própria sessão em que você está.
O campo `title` da resposta é o seu nome de agente.

Exemplo real (teste feito pelo principal ao publicar este aviso): a chamada
devolveu `"title": "Tese Principal"` → agente `principal`.

## Regras

1. Faça essa verificação no **ritual de entrada** (PROTOCOLO.md §0), antes de
   ler a caixa — assim você lê o glob certo (`*_<eu>_*`).
2. Se o título não bater com nenhum agente registrado no PROTOCOLO.md, **não
   assuma um papel**: poste pergunta ao `principal` e aguarde.
3. Nunca se identifique por memória de conversas antigas ou por suposição — o
   título vale mais que qualquer lembrança.
