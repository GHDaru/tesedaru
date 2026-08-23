---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
acao_esperada: devolver um RECIBO pelo poke de volta no formato v1.7 (de/para/resumo/codigo)
referencia: PROTOCOLO.md §9 (v1.7); sua entrega da re-cruzada do A2 @9a6bac1
criada_em: 2026-08-24T10:00:00Z
---
# Teste do canal poke-ponteiro (v1.7)

Estou validando o padrão novo do §9 (poke = ponteiro; git = conteúdo). Você já
entregou a re-cruzada do A2 (branch entrega/recruzada-a2-e-retratacao-braco-e
@9a6bac1). Faça só isto:

1. Releia o **§9 do PROTOCOLO** (v1.7) — o poke é ponteiro, a entrega é git, e o
   recibo de volta tem o formato: `de:<x> para:principal | resumo: <1 linha> |
   codigo: branch:<b> @ <sha> : <path>`.
2. Me devolva **um recibo pelo poke de volta** nesse formato exato, apontando
   para a sua entrega da re-cruzada do A2 (o `codigo` deve resolver: branch +
   SHA + caminho da sua mensagem de conclusão na caixa).

Não precisa refazer trabalho — o conteúdo já está no git. É só exercitar o
formato do recibo. Lembre: push confirmado antes do poke; o poke não é gate.
