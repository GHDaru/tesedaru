---
de: autor
para: todos
tipo: aviso
acao_esperada: a partir de agora, endereçar TODAS as mensagens ao principal (não ao autor, nem entre agentes); aguardar a redistribuição feita por ele
referencia: coordenacao/PROTOCOLO.md v1.1 · ADR 0009 · constituição v1.2.0 (princípios XI e XII)
criada_em: 2026-08-16T17:44:39Z
---
Decisão do autor, registrada pelo agente principal a pedido dele (conversa de
2026-08-16):

1. TODO O PLANEJAMENTO passa pelo agente principal. Nenhum agente altera
   prioridades, fila, matriz ou estrutura do plano de revisão. Atualizar o
   status da própria execução continua permitido.
2. TODA MENSAGEM passa pelo principal. Não endereçem mensagens diretamente ao
   autor, nem entre si. Endereço válido: "para: principal" (ou "para: todos"
   quando for aviso de claim/conclusão). O principal faz a triagem: decide o
   que sobe ao autor (gates e decisões) e o que é redistribuído, e para quem.
   Motivo declarado pelo autor: com quatro agentes em paralelo, sem um ponto
   único de triagem perde-se o controle do que precisa de decisão humana.
3. Respostas a tarefas encaminhadas pelo principal voltam ao principal.
4. Comunicação com o autor é sempre didática e detalhada (princípio XI da
   constituição): termos explicados, siglas abertas, sem jargão comprimido.
