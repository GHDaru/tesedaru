# QA Report 005 — Plano: quebra por tema, sequência, aprovação prévia

- **Lane**: light — spec é a tarefa do `principal` (`coordenacao/caixa/
  20260817-0020_principal_site_tarefa_reestilizar-plano-com-quebra-por-tema`),
  já completamente especificada; `ux-design.md` deste ciclo cobre o porquê
  das decisões de tela. Sem plan.md/tasks.md separados.

## Dois bugs reais encontrados durante o próprio desenvolvimento

1. **`execucoes.itens[]` com formato divergente**: o item
   `fix-cap2-prosa-619-648` usa campos (`descricao`/`branch`/`commit`/
   `responsavel`) diferentes dos itens de experimento (`o_que`/`onde`/
   `dono`) — o template original só lia o segundo formato, renderizando
   "undefined · undefined" **já antes desta rodada** (bug pré-existente,
   exposto ao abrir o `<details>` para verificar o badge novo). O
   `estado:"gate"` desse item também não batia com nenhuma chave do mapa
   `EX`, caindo no estilo genérico "pendente" (cinza) em vez de "gate"
   (âmbar). Corrigido: leitura dos dois formatos de campo + chaves `gate`
   e `bloqueado` adicionadas ao mapa `EX`.
2. **Overflow horizontal no mobile, introduzido por mim**:
   `.quebra-pct{white-space:nowrap}` impedia o texto explicativo de
   quebrar linha dentro de um flex row sem `min-width:0`, vazando 21px
   além do viewport em 390px. Encontrado rodando o próprio teste de mobile
   do ritual (`scrollWidth > clientWidth`), corrigido antes de publicar.

## Verificação (Playwright/Chromium, dados reais, pipeline de build simulado)

- Pipeline completo local: `compute-kpis.py` → `compute-mensagens.py` →
  `compute-referencias.py` → `fichamentos/build_kg.py` →
  `render-plano-revisao.py` → cópia de `kg.html` para `grafo-embed.html`,
  mesma ordem do `painel.yml`.
- **0 erros de console reais** nas 7 páginas (o único "erro" reportado é
  um 404 de `favicon.ico`, já investigado e descartado em ciclos
  anteriores — não é recurso da própria página).
- **Quebra por tema**: 5 `tema-card` renderizados para o Cap. 2 (batendo
  com os 5 itens de `capitulos.cap2.quebra`), progresso do capítulo
  calculado em 0% (todos os 5 temas em `aberto`, esperado), pontinho de
  agente colorido presente nos 5 responsáveis, nota de
  `sequencia_rodadas` visível no texto (não só tooltip).
- **Aprovação prévia**: badge "✓ aprovação prévia do autor" presente e com
  o texto completo da decisão no `title`, ao lado do pill "gate" (agora
  corretamente âmbar) do item `fix-cap2-prosa-619-648`.
- **Decisões pendentes no Controle**: `kpis.json` regenerado localmente
  passou de 2 para 8 decisões em `fila_autor.itens` (batendo com as 8
  atuais em `plano-revisao.json`), rótulo "DECISÃO" e contagem "Aguardando
  você — 16 itens" corretos — nenhuma mudança de código precisou ser feita
  aqui, só a regeneração que o próprio deploy já faz a cada push.
- **Tema claro/escuro**: Plano e Controle verificados nos dois
  `colorScheme`, sem regressão visual.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` confirmado em Plano
  após a correção do item 2 acima; as outras 6 páginas seguem sem
  regressão (checadas na mesma passada).
- **Regressão**: as outras 6 páginas mantidas com 0 erros de console e
  título/h1/navegação corretos — a mudança de `.k-ag-dot` de CSS
  específico da página Coordenação para o `SHARED_CSS` foi verificada
  visualmente nas duas páginas que agora o usam (Coordenação sem mudança
  de aparência, Plano com o pontinho novo).

## Closing tail

- `TAIL:review` — n/a nesta rodada: lane light, mudança aditiva (nova
  seção + normalização de um formato de dado já existente + badge), sem
  alterar o comportamento de nenhuma outra página; verificação própria com
  evidência acima substitui a revisão formal em contexto fresco. Registrado
  no aviso ao `principal`.
- `TAIL:security` — leitura só de `docs/records/plano-revisao.json`
  (arquivo do próprio repositório), todo texto passa por `esc()` antes de
  entrar no HTML. n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
