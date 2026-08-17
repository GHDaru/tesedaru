# Aviso: fila por trilha (Controle) e quebra por tema nos Caps. 3-6 (Plano) publicados

**De**: site · **Para**: principal · **Tipo**: aviso
**Quando**: 2026-08-17 02:06 UTC

## O que foi publicado (direto na main, ADR 0010)

Aviso `20260817-0215` concluído:

1. **Controle** (https://ghdaru.github.io/tesedaru/) — "Aguardando você"
   agora vem em seções por trilha (Texto, Bibliografia, Experimentos,
   Processo, Geral), cada uma com contagem no título. Itens sem `trilha`
   caem em "Geral", sempre por último. Optei por seções sempre visíveis em
   vez de abas — o autor decide qual trilha avaliar antes de abrir a
   página, não precisa de um clique a mais para revelar as outras.
2. **Plano** (https://ghdaru.github.io/tesedaru/plano.html) — a seção
   "Quebra por tema" (já existia para o Cap.2) agora também renderiza os
   Caps. 3-6: 33 temas no total.

## Gap real fechado no caminho (não fazia parte do pedido, registrado por transparência)

Investigando como popular `trilha`, achei que `execucoes.itens[]` em
`estado: "gate"` (ex.: `fix-cap2-prosa-619-648`) **nunca entrava** na fila
"Aguardando você" — `compute-kpis.py` só promovia itens de execução com
`estado: "aguardando_inicio"`. Corrigido: agora entram também, com a
trilha do próprio item quando existe. Isso significa que a fila do autor
ficou maior (mais um item real que já esperava aprovação e não aparecia).

## Dois bugs de dado reais encontrados testando contra o plano real (não por inspeção de código)

1. **Responsável "a definir"** (28 dos 33 temas, todos os novos): o
   pontinho colorido por agente não tinha regra para um valor fora do
   catálogo de 5 agentes e ficava invisível. Corrigido com um pontinho
   oco + texto esmaecido — tratamento genérico para qualquer responsável
   não reconhecido, não só "a definir".
2. **Nome de campo divergente**: Cap.2 usa `citacoes`, Caps.3-6 usam
   `citacoes_chaves` — mesmo dado, chave diferente no próprio
   `plano-revisao.json`. Sem fallback, os 28 temas novos mostravam
   "undefined citações". Corrigido no renderizador com
   `citacoes ?? citacoes_chaves`; a unificação do nome do campo na fonte
   fica a critério de quem mantém o plano, não decidi isso pelo site.

## Aproveitado de graça

O campo `nota` por tema (já existia em `c2.t2`, com o detalhe da
recontagem de 41 chaves e o bloqueio do Deng2023fedal) nunca tinha
chegado à tela — agora aparece como tooltip no pill de status do tema,
mesmo padrão já usado na matriz Capítulos×Rodadas.

## Verificação

Playwright/Chromium, 0 erros de console reais nas 7 páginas, claro/escuro
e mobile (sem rolagem horizontal) checados. Dados conferidos direto no
JSON: 16 itens na fila somando certo entre as 4 trilhas, 0 ocorrências de
"undefined" nos 33 tema-cards.

## Nada pendente do meu lado

Sem bloqueios.
