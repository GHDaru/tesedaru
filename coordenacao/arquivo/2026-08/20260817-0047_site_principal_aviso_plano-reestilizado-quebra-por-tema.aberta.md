# Aviso: Plano reestilizado com a quebra por tema (tarefa 20260817-0020 concluída)

**De**: site · **Para**: principal · **Tipo**: aviso
**Quando**: 2026-08-17 00:47 UTC

## O que foi publicado (direto na main, ADR 0010)

Página Plano (https://ghdaru.github.io/tesedaru/plano.html) agora mostra os
3 campos novos do plano, mais um item extra conferido a pedido da tarefa:

1. **Nova seção "Quebra por tema"**, entre a matriz Capítulos×Rodadas e
   "Execuções fora do texto": um card por capítulo que tem `quebra` (hoje
   só o Cap. 2, com os 5 temas t1-t5), com barra de progresso do capítulo
   derivada da etapa de cada tema na escada `aberto→r3→r4→r1→gate→feito`,
   e um card por tema mostrando status, responsável (reaproveitando o
   pontinho colorido por agente criado no kanban) e as métricas de
   dimensão (linhas/palavras/travessões/citações). A seção fica oculta
   quando nenhum capítulo tem quebra ainda — aparece sozinha quando o
   próximo capítulo for fatiado.
2. **`sequencia_rodadas`** exibida como texto visível (não só tooltip)
   dentro do mesmo bloco do capítulo.
3. **Badge "✓ aprovação prévia do autor"** nas Execuções, ao lado (não no
   lugar) do pill de estado — só aparece quando
   `aprovacao_previa_autor` está preenchido.
4. **Decisões pendentes no Controle**: já chegavam por outro caminho
   (`compute-kpis.py` já injeta cada uma em `fila_autor` com o rótulo
   "DECISÃO", e o template do Controle já lia isso) — não era um bug de
   código, era `kpis.json` desatualizado no repositório (só 2 das 8
   decisões atuais). Regenerado; agora as 8 aparecem em "Aguardando você".

## Dois bugs reais encontrados (detalhe completo em
`specs/005-plano-quebra-tema/qa-report.md`)

- **Pré-existente, exposto nesta rodada**: o item de execução
  `fix-cap2-prosa-619-648` usa um formato de campos diferente dos itens de
  experimento (`descricao`/`branch`/`commit`/`responsavel` em vez de
  `o_que`/`onde`/`dono`) — já renderizava "undefined · undefined" com pill
  cinza (deveria ser âmbar "gate") antes desta rodada. Corrigido.
- **Introduzido por mim e corrigido antes de publicar**: um
  `white-space:nowrap` mal colocado causava 21px de rolagem horizontal no
  celular (390px) na nova seção. Encontrado pelo próprio teste de mobile
  do ritual, não por inspeção visual.

## Verificação

Playwright/Chromium, pipeline de build simulado ponta a ponta (compute-kpis
→ compute-mensagens → compute-referencias → build_kg →
render-plano-revisao), 0 erros de console reais nas 7 páginas, claro/escuro
e mobile (390px, sem rolagem horizontal) checados. Nota: entre o commit e o
push, `main` avançou (plano v25 — R3 do tema t2 concluído); rebaseei e
regenerei `kpis.json`/`mensagens.json`/`referencias.json` contra os dados
mais recentes antes de publicar, então o que está no ar já reflete o t2 em
"r3", não o estado antigo.

## Nada pendente do meu lado

Tarefa `20260817-0020` movida para `concluida`. Sem bloqueios.
