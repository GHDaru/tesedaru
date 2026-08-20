---
de: principal
para: site
tipo: tarefa
acao_esperada: reestilizar a página Plano para renderizar a quebra por tema do Cap. 2 (novo campo no JSON) e revisar a página com os campos novos; publicar sem gate e avisar com a URL
referencia: pedido do autor 2026-08-17 · docs/records/plano-revisao.json v21+ (capitulos.cap2.quebra, sequencia_rodadas, execucoes.itens[].aprovacao_previa_autor)
criada_em: 2026-08-17T00:20:00Z
---

O plano ganhou estrutura nova que a página Plano ainda não mostra — os DADOS
já chegam ao site (o workflow reembute o JSON a cada push), mas o template
não os renderiza. Pedido do autor: "o site já está atualizado com a quebra?
Avise ele para ele reestilizar."

O que renderizar:

1. **`capitulos[].quebra`** (hoje só o cap2 tem): lista de temas
   `{id, tema, linhas, palavras, travessoes, citacoes, responsavel, status}`
   com status em `aberto → r3 → r4 → r1 → gate → feito`. Sugestão: linha do
   capítulo expansível mostrando os temas como sub-linhas ou cards, com chip
   de status, responsável e as métricas de dimensão; barra de progresso do
   capítulo derivada dos temas quando houver quebra.
2. **`capitulos[].sequencia_rodadas`** (texto da regra "R3 antes de R1"):
   exibir como nota do capítulo.
3. **`execucoes.itens[].aprovacao_previa_autor`**: badge "aprovação prévia"
   no item em gate (diferente de gate puro — indica que só falta um
   pré-requisito, não a decisão).
4. Aproveite a passada para conferir se `decisoes_pendentes` (7 itens hoje)
   está legível na página Controle — o autor navega por ali para decidir.

Estilo a seu critério dentro do sistema já publicado (sidebar, tema
claro/escuro, tabelas com rolagem própria). Publicação direta, ADR 0010.
