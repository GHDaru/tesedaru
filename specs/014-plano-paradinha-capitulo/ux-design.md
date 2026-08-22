# Ciclo 014 — Painel expansível por capítulo (Plano)

**Status**: publicado em `main` (commit `2ba5241`), aprovado pelo autor em
2026-08-22 após 2 rodadas de correção sobre o mockup.

## Pedido original

O autor pediu, para cada elemento da matriz "Capítulos × rodadas" (Pré-
textuais, 1-Introdução, ..., Apêndices), um painel que abre ("a paradinha")
com os 7 elementos de revisão (R1-R7) visíveis, mantendo a marcação de topo
como já estava. Pediu também para remover a antiga seção solta "o que abre
esta frente" e decidir sobre "Quebra por tema"; e para tratar "Artefatos e
pendências" em spec própria (ver `specs/014-plano-artefatos-pendencias/`).
Pediu para ver telas e decidir junto antes de publicar — desvio do padrão
autônomo usado nos ciclos anteriores desta sessão.

## Processo

1. Consultei 3 especialistas em paralelo (agentes read-only, sem edição de
   arquivo): um propôs manter a tabela com linha de detalhe; outro propôs
   substituir por grade de `<details>` por capítulo; o terceiro tratou
   especificamente "Quebra por tema" (recomendou fundir dentro do card do
   capítulo) e o escopo de "Artefatos e pendências" (virou spec própria).
2. Construí um mockup local (não publicado) com a abordagem de card
   (`<details class="cap-card">`), reaproveitando `pill()`/`GLIFO` sem
   alteração no nível fechado.
3. Trouxe capturas de tela reais (dados verdadeiros da tese) para o autor
   decidir — duas rodadas de correção:
   - **Correção 1**: o nível aberto não deveria virar cards descritivos com
     nota em parágrafo — deveria seguir os mesmos ícones do nível de cima,
     só que sempre visíveis (a nota, que hoje só existe em `title=""`
     invisível em toque, ficou por conta da 3ª correção abaixo).
   - **Correção 2**: "Pré-textuais" e "Apêndices A1-A7" são agregados de
     várias partes (resumo+abstract; 7 arquivos). O nível aberto precisa
     listar cada parte pelo nome, com sua fileira de ícones (repetida — é o
     mesmo registro de revisão, ainda não existe rodada por arquivo), e o
     que hoje é "o que abre esta frente" vira um nível A MAIS, aninhado
     dentro do card, com o mesmo conteúdo de antes.
   - **Correção 3 (ajuste fino)**: os ícones das partes precisavam alinhar
     com a coluna de ícones do cabeçalho, e cada linha de parte precisava
     terminar com um resumo (`N/M rodadas`), espelhando a estrutura do
     cabeçalho — resolvido com colunas equivalentes (`margin-left:auto` nos
     ícones + `min-width` fixo no resumo à direita).

## Estrutura final (3 níveis)

1. **Fechado**: idêntico à antiga linha da tabela — título, selo
   "encerrado", arquivo, 7 pills (`pill()`/`GLIFO` sem alteração), pontos.
   Acrescenta só um contador pequeno `N/M rodadas` (`feito` sobre `7 - na`).
2. **Aberto — partes do agregado ou Quebra por tema**:
   - `pre` e `ap`: lista das partes reais (Resumo/Abstract; A1-A7, usando os
     títulos medidos em `pos_textuais[]`), cada uma com a MESMA fileira de
     ícones do capítulo (mesmo dado — texto pequeno avisa isso) e um resumo
     `N/M rodadas` à direita, alinhado ao cabeçalho.
   - `cap2`-`cap6` (têm `quebra`): a antiga seção "Quebra por tema" fundida
     aqui — vira lista leve (1 ícone por tema + nome + responsável), sem
     mais os cards com caixa e borda de antes.
   - `cap1` e chapters sem agregado/quebra: nada neste nível.
3. **Aberto — "O que abre esta frente"**: `<details>` aninhado, mesmo
   conteúdo de sempre (bullets de `capitulos[].abertura`), agora dentro do
   card em vez de solto abaixo da matriz.

## Dado não fabricado

As partes de `pre`/`ap` repetem o status do capítulo inteiro porque não
existe, hoje, rodada rastreada por arquivo individual — está escrito na
tela ("mesma revisão do capítulo — ainda sem rodada rastreada por arquivo").
Perguntei ao `principal` (caixa 20260822-1415) se vale a pena passar a
rastrear granularmente; resposta ainda pendente. Nenhum status foi inventado
para fechar essa pergunta.

## Verificação

8 páginas testadas via Playwright (Chromium headless): 0 erros de console
reais (só o 404 conhecido de favicon), 0 rolagem horizontal indevida, testado
em claro/escuro/mobile (390×844). `fichamentos/kg.json`/`kg.html`
restaurados após o teste (não são superfície do site).

## TAIL

- `TAIL:review` — n/a (ciclo leve, sem código de produção fora do template
  HTML/JS/CSS já testado end-to-end).
- `TAIL:security` — n/a (sem input de usuário novo, sem dado sensível).
- `TAIL:gate` — n/a (site/painel dispensa gate, ADR 0010); decisão de design
  vinda diretamente do autor nesta conversa substitui o gate formal.
