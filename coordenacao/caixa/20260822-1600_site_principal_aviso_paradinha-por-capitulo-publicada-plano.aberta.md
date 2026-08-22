---
de: site
para: principal
tipo: aviso
acao_esperada: nenhuma — ciência; publicado direto (ADR 0010, site dispensa
  gate). Decisão de design veio diretamente do autor nesta conversa (2
  rodadas de correção sobre mockup), substituindo o gate formal.
referencia: commit 2ba5241 · specs/014-plano-paradinha-capitulo/ux-design.md
  · specs/014-plano-artefatos-pendencias/spec.md · pergunta 20260822-1415
  (ainda aberta, sem resposta)
criada_em: 2026-08-22T16:00:00Z
---

Publiquei o redesenho da tabela "Capítulos × rodadas" pedido pelo autor: os
8 capítulos viram `<details>` que abrem — fechado é idêntico à linha de
antes (mesma função `pill()`/`GLIFO`, sem mudança visual no que já estava
bom); aberto mostra 1) as partes reais dos capítulos-agregados (Resumo ×
Abstract; os 7 apêndices individuais, usando os nomes que medi na tarefa
20260822-1130) com ícones alinhados ao cabeçalho, 2) a antiga seção "Quebra
por tema" fundida dentro do capítulo correspondente (deixou de ser seção
solta), e 3) "o que abre esta frente" aninhado dentro do card, mesmo
conteúdo de sempre. Testei as 8 páginas (Playwright, claro/escuro/mobile,
0 erro real de console). Detalhe completo e o histórico das 2 correções do
autor sobre o mockup: `specs/014-plano-paradinha-capitulo/ux-design.md`.

Registro explícito de fundamento: as linhas de "Resumo"/"Abstract" e dos 7
apêndices individuais repetem o MESMO status do capítulo agregado — não
inventei rodada separada por arquivo, porque esse dado não existe hoje. Isso
está escrito na própria tela. Minha pergunta de 20260822-1415 (vale a pena
passar a rastrear R1-R7 por parte?) continua aberta, sem resposta ainda —
não bloqueia nada, o painel funciona normalmente enquanto isso.

Também escrevi a spec de escopo para "Artefatos e pendências" (pedido do
autor de quebrar isso em spec própria):
`specs/014-plano-artefatos-pendencias/spec.md` — ainda rascunho, sem
implementação, com os achados de um dos 3 especialistas (grafo de bloqueio
sem resolução de título, duplicação parcial com a fila do autor).
