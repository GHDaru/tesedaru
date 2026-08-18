---
de: autor
para: todos
tipo: aviso
acao_esperada: nenhum agente pede gate diretamente ao autor; entregar a branch pronta e avisar o principal, que consolida e leva ao autor
referencia: coordenacao/PROTOCOLO.md §2-bis · constituição princípio XII · ADR 0010
criada_em: 2026-08-16T18:19:50Z
---
Complemento à decisão de roteamento (registrado pelo principal a pedido do
autor, conversa de 2026-08-16):

TODOS OS GATES DE MERGE passam pelo agente principal. Ao terminar um trabalho,
o agente publica a branch e envia ao principal uma mensagem de conclusão com:
o que mudou, o hash/branch, a evidência (número, artefato, teste) e o risco.
O principal consolida os pedidos, verifica e leva ao autor em bloco, com
antes/depois e recomendação. Nenhum agente pede aprovação diretamente ao autor.

ÚNICA EXCEÇÃO: alterações do site/painel (docs/records/*, scripts de render,
coordenacao/) seguem sem gate, por serem reversíveis e não tocarem o texto da
tese nem os dados.

Motivo declarado pelo autor: com quatro agentes paralelos, aprovar pedidos
avulsos tira o foco e o controle; ele quer decidir em bloco, com contexto.
