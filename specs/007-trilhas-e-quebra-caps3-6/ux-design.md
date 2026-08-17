# ux-design.md — Trilhas na fila do Controle + quebra por tema nos Caps. 3-6

- **Ciclo**: 007-trilhas-e-quebra-caps3-6 · **Lane**: light (aviso já veio
  totalmente especificado pelo `principal`, mensagem `20260817-0215`,
  pedido literal do autor: "avaliar em sessões focadas — numa sentada só
  gates de texto, noutra só experimentos").

## 1. Trilhas na fila do Controle: seções sempre visíveis, não abas

O aviso sugeriu "abas ou seções". Decisão: **seções**, não abas — o autor
quer avaliar em sessões focadas, mas isso não exige esconder as outras
trilhas atrás de clique nenhum; ele já sabe em qual trilha está entrando
antes de abrir a página (decisão tomada fora da tela). Abas adicionariam
estado de UI (qual está ativa, persistência entre visitas) para resolver um
problema que seções resolvem sozinhas: cada trilha é um bloco com título e
contagem própria (`Texto 4`), a rolagem natural da página já serve de
navegação. Ordem fixa (texto → bibliografia → experimentos → processo →
geral) — geral sempre por último, porque é a trilha "sem trilha", não uma
prioridade.

## 2. Gap real fechado no caminho: execuções em gate nunca apareciam na fila

Investigando como popular `trilha` percebi que `fila_e_represados()` (em
`compute-kpis.py`) só promovia itens de `execucoes.itens[]` para a fila
quando `estado == "aguardando_inicio"` — um item em `estado: "gate"` (ex.:
`fix-cap2-prosa-619-648`, esperando aprovação do autor desde antes desta
sessão) **nunca aparecia em "Aguardando você"**, mesmo sendo literalmente
uma coisa esperando o autor. Corrigido: itens de execução em gate agora
entram na fila (tipo `gate`, reaproveitando o mesmo rótulo/estilo dos gates
de rodada de capítulo), trilha vinda do próprio item quando existe, "Geral"
quando não. Registrado aqui por transparência — não fazia parte do pedido
literal, mas é o mesmo tipo de lacuna (dado real, nunca escoado para a
tela) que este agente já vem fechando ciclo a ciclo.

## 3. Quebra por tema nos Caps. 3-6: mesmo layout do Cap.2, dois ajustes

A seção "Quebra por tema" (ciclo 005) já existia; o pedido era só estendê-la
aos novos capítulos com `quebra`. Dois problemas de dado, não de layout,
apareceram ao testar contra os dados reais (nunca por inspeção de código):

1. **Responsável "a definir"** (todos os 28 temas novos): o pontinho
   colorido por agente (`.k-ag-dot`) não tinha nenhuma regra para um valor
   fora do catálogo de 5 agentes — ficava invisível, não neutro. Decisão:
   pontinho **oco** (contorno, sem preenchimento) + texto em itálico
   opacidade reduzida para qualquer responsável não reconhecido, não só
   "a definir" — trata a ausência de atribuição como informação visível
   ("ninguém assumiu ainda"), nunca como um buraco no layout.
2. **Nome de campo divergente**: Cap.2 usa `citacoes`, Caps.3-6 usam
   `citacoes_chaves` — mesmo dado, chave diferente entre capítulos no
   próprio plano. Sem o fallback (`t.citacoes ?? t.citacoes_chaves`), as
   dimensões de todos os 28 temas novos mostravam "undefined citações".
   Achado rodando contra o JSON real, não em teste inventado.

## 4. Aproveitado de graça: nota por tema (dado já existia, nunca renderizado)

O tema `c2.t2` já carregava um campo `nota` livre (status detalhado do R3,
achados de recontagem, bloqueios) — mesmo papel que `cell.nota` já cumpre
na matriz Capítulos×Rodadas (tooltip + classe `.has-note` no pill).
Reaproveitado o mesmo padrão aqui: pill de status ganha `title` e
`.has-note` quando o tema tem nota. Não é conteúdo novo do pedido desta
rodada — é dado que já estava no plano e ficava invisível; decisão de
expor segue o mesmo princípio já aplicado a `decisoes_pendentes` no ciclo
005 (nunca deixar dado real represado sem chegar à tela).

## 5. Reuso

Tudo reaproveitado do ciclo 005 (`.quebra-cap`, `.tema-card`, `.k-ag-dot`,
`GLIFO`/`STAGE_CLASS`) e do padrão de tooltip já existente na matriz
principal (`.pill.has-note` + `title`). Papel novo pequeno: `.fila-trilha`
(seção com título+contagem dentro da fila do Controle) e a regra CSS de
pontinho oco para agente não reconhecido — ambos catalogáveis como
reutilizáveis se o site precisar do mesmo padrão em outro lugar.
