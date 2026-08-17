# ux-design.md — Plano: quebra por tema, sequência de rodadas, aprovação prévia

- **Ciclo**: 005-plano-quebra-tema · **Lane**: light (tarefa já veio
  totalmente especificada pelo `principal`, mensagem `20260817-0020` — sem
  necessidade de consulta a especialistas).
- **Consome**: tarefa do `principal`, pedido literal do autor citado nela
  ("o site já está atualizado com a quebra? Avise ele para ele
  reestilizar.").

## 1. Onde cada campo novo entra

- **`capitulos[].quebra`** (hoje só Cap. 2): nova seção "Quebra por tema"
  na página Plano, entre a matriz Capítulos×Rodadas e "Execuções fora do
  texto" — mesma posição hierárquica de "o que abre esta frente", porque é
  a mesma pergunta em granularidade menor: não "qual capítulo", mas "qual
  tema dentro dele". A seção fica **oculta** quando nenhum capítulo tem
  quebra (`display:none` via JS) — decisão de não inventar visual vazio
  para os outros 7 capítulos que ainda não foram fatiados; a seção aparece
  sozinha quando o segundo capítulo ganhar `quebra`.
- **`capitulos[].sequencia_rodadas`**: texto visível (não tooltip) logo
  abaixo da barra de progresso do capítulo, dentro do mesmo bloco da
  quebra — é a regra que rege a ordem dos temas ali embaixo, então fica
  colada a eles, não em outro lugar da página.
- **`execucoes.itens[].aprovacao_previa_autor`**: badge próprio
  (`✓ aprovação prévia do autor`, pill verde-andamento com o texto
  completo em `title`) ao lado do pill de estado, na lista "Execuções fora
  do texto" — nunca substituindo o pill de estado (`gate`/`concluído`/
  etc.), porque são informações diferentes: uma é ONDE o item está, a
  outra é UMA CONDIÇÃO já satisfeita dentro desse estado.
- **`decisoes_pendentes`**: já chegava ao Controle por outro caminho —
  `compute-kpis.py` já injeta cada decisão pendente em `fila_autor.itens`
  com `tipo: 'decisao'`, e o template de Controle já tinha o rótulo
  "DECISÃO" mapeado (linha do `GLIFO_MSG`/tipo). Não fazia render "quebrado"
  — fazia render **correto porém com dado desatualizado**: `kpis.json`
  commitado no repo só tinha 2 das 8 decisões atuais porque não tinha sido
  regenerado desde que as últimas 6 foram registradas no plano. Nenhuma
  mudança de código neste item — só regeneração de `kpis.json` no próximo
  build (o workflow já faz isso a cada push).

## 2. Cálculo do progresso por tema

`quebra[].status` segue a escada `aberto → r3 → r4 → r1 → gate → feito`
(citada na tarefa do principal). A barra de progresso do capítulo é a
média do índice de cada tema nessa escada, normalizada 0–100%: um tema
"aberto" conta 0, um tema "feito" conta 100%, um tema em "r4" conta 3/5 =
60%. É uma média de ETAPA, não de pontos de esforço — rotulado
explicitamente ("ponderado pela etapa de cada tema") para não ser
confundido com a % de pontos que já aparece no card de KPI hero.

## 3. Reuso de papéis já catalogados

- **Pill de estado** (`.pill.feito/gate/andamento/pendente`): os 6 estados
  da escada de tema são reduzidos a essas 4 classes visuais já existentes
  (aberto→pendente, r3/r4/r1→andamento, gate→gate, feito→feito) — o texto
  do pill mostra o nome exato da etapa (`r3`, `r4`, `r1`...), a cor
  reaproveita a semântica já estabelecida no site inteiro. Não foi criada
  nenhuma cor nova.
- **Pontinho por agente** (`.k-ag-dot`, criado no ciclo do kanban): o
  responsável por cada tema agora usa a mesma tag colorida — motivo
  original de catalogar esse papel como "reutilizável" no ux-design.md do
  kanban. Nesta rodada o CSS de `.k-ag-dot` foi movido do bloco
  específico da página Coordenação para o `SHARED_CSS`, porque deixou de
  ser exclusivo de uma página.
- **`.progress`/`.progress-bar`**: mesmo componente do KPI hero de
  Controle e da barra de cobertura de fichamento em Bibliometria.

## 4. Bug encontrado e corrigido durante o desenvolvimento (não introduzido por mim, mas exposto por mim)

`execucoes.itens[]` tem dois formatos que convivem na mesma lista: itens de
experimento (`o_que`/`onde`/`duracao`/`resultado_esperado`/`dono`) e um
item de texto em gate, `fix-cap2-prosa-619-648`
(`descricao`/`branch`/`commit`/`responsavel`/`bloqueado_por` — sem
nenhum dos campos do primeiro formato). O template original só lia os
campos do primeiro formato, então esse item **já renderizava "undefined ·
undefined"** antes desta rodada — ninguém tinha notado porque ninguém
tinha aberto o `<details>` "Execuções fora do texto" durante uma
verificação visual. Também descobri que o `estado: "gate"` desse item não
batia com nenhuma chave do mapa `EX` (que só tinha
`aguardando_inicio/rodando/concluido/falhou`), caindo no `pendente`
genérico — um item em gate aparecia cinza, não âmbar. Corrigido: o
renderizador agora lê os dois formatos de campo (`i.o_que || i.descricao`,
etc.) e o mapa `EX` ganhou as chaves `gate` e `bloqueado`.

## 5. Bug que eu mesmo introduzi e corrigi antes de publicar

Primeira versão do CSS tinha `.quebra-pct{white-space:nowrap}` para manter
"0%" na mesma linha — mas isso também impedia o texto explicativo
("ponderado pela etapa de cada tema") de quebrar linha, e num flex row
(`justify-content:space-between`) sem `min-width:0`, o item simplesmente
vazava a largura do card em vez de encolher. Achado rodando o teste de
mobile (390px) do próprio ritual de verificação, não por inspeção visual —
o `scrollWidth` do `<html>` bateu 21px maior que o `clientWidth`.
Corrigido: removido o `white-space:nowrap` do container, `min-width:0` nos
dois filhos do flex, `flex-wrap:wrap` como rede de segurança.
