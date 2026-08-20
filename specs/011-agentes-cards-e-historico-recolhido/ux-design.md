# ux-design.md — Agentes: cards para o "agora", grafo redesenhado no "histórico"

- **Ciclo**: 011-agentes-cards-e-historico-recolhido · **Lane**: light — feedback
  direto do autor sobre a página publicada no ciclo 010 (mapa de nós/arcos).
  Envolveu consulta a 3 especialistas independentes antes de decidir; por
  isso este documento cobre também a consolidação, não só o resultado.

## 0. O pedido e por que consultar 3 especialistas

O autor viu o mapa de nós/arcos do ciclo 010 e relatou "visualmente
carregado e congestionado". Propôs duas direções concorrentes sem decidir
entre elas — (A) simplificar para "big numbers" (hipótese dele: os arcos
talvez não carreguem informação suficiente para justificar a complexidade
visual) ou (B) manter grafo, mas com um arco por par (não dois), sem seta,
rotulado `[in]`/`[out]` — e pediu que 3 especialistas avaliassem e
decidissem, "aqui os especialistas sugerirem". Convoquei 3 pareceres
independentes (agentes em background, sem se verem uns aos outros, mesmos
dados reais e o mesmo screenshot da versão publicada): um especialista em
visualização de redes/grafos, um em dashboards/big numbers, um em UX
operacional de baixa cardinalidade.

## 1. O que os três pareceres disseram (resumo, não a íntegra)

Convergência forte nos três, por caminhos diferentes:

- **Grafos/redes**: a topologia real (10 nós, 23 arestas) colapsa em 17
  pares distintos, mas o nó `todos` (que nem é um agente — é o destinatário
  de mensagens em difusão) concentra 8 arestas e continuaria sendo o maior
  polo de congestão mesmo depois de aplicar a opção B do autor. Causa raiz
  real: arcos bidirecionais do mesmo par viram uma "gota" de cor misturada
  nos 3 pares de maior volume (exatamente os mais importantes), e `todos`
  foi modelado como nó de primeira classe sem ser um agente. Recomendação:
  abandonar o grafo como visão principal — a topologia é imposta pelo
  protocolo (hub obrigatório), não é uma descoberta que valha o custo
  visual.
- **Dashboards/big numbers**: confirma com números — 90,6% do tráfego
  histórico passa pelo `principal`; só 1,05% (3 mensagens em 287) é troca
  direta fora do hub. Recomendação: cards por agente, número grande =
  tarefas abertas agora (o dado acionável) em destaque, histórico
  (enviado/recebido) em texto pequeno subordinado; `principal` extraído do
  grid para uma faixa-resumo própria (não é comparável aos satélites);
  cards satélites devem reportar "enviado ao principal / recebido do
  principal" (é 97%+ do que já é o total de cada um) em vez de totais
  globais soltos.
- **UX operacional**: a causa raiz não é geometria, é hierarquia de
  informação — a página tratava "tarefas abertas agora" (acionável, muda a
  cada hora) e "histórico de mensagens" (contexto, quase não muda) no mesmo
  plano visual, quebrando o padrão que o resto do site já segue (Plano tem
  KPI "Aguardando você" em destaque; Coordenação tem "para você" + arquivo
  recolhido em `<details>`). Recomendação: "agora" sempre visível no topo
  (cards só para quem tem pendência — 5 de 10 nós tinham em zero, e um grid
  homogêneo de "big numbers" reproduziria o mesmo ruído de zeros do grafo
  atual), "histórico" — grafo ou tabela — recolhido por padrão.

## 2. Decisão consolidada

Nenhum dos três recomendou implementar a opção B do autor (grafo com um
arco por par) como visão PRINCIPAL — mas o próprio autor já havia
enquadrado essa opção como "para este 'histórico'" nas palavras dele, o que
bate exatamente com o diagnóstico dos 3 pareceres. Decisão: os dois não são
mutuamente exclusivos, são a mesma resposta em dois planos:

1. **"Agora" (sempre visível, topo da página)**: KPI agregado (tarefas
   abertas agora + quantos nós têm pendência) → faixa-resumo do `principal`
   (hub, à parte do grid) → cards, um por agente com tarefa aberta agora,
   ordenados por volume desc, número grande em destaque, "enviado/recebido
   do principal" em texto pequeno subordinado, sinal de vida quando
   disponível (reaproveita `atividade` do ciclo 009). Agentes sem pendência
   viram uma linha de texto ("Sem pendências agora: ..."), não cards vazios
   — evita o ruído de zeros que o parecer de UX identificou.
2. **"Histórico" (dentro de `<details>` fechado por padrão)**: aqui sim, a
   opção B do autor, implementada ao pé da letra — um arco por par
   (`agente ⇄ principal`), sem seta, rótulo `[in N] [out M]`. Redesenhado
   como leque reto (não anel): `principal` fixo à esquerda, satélites em
   coluna à direita ordenados por volume do par, linhas retas (sem curva —
   como a origem é sempre o mesmo ponto, retas não se cruzam). O nó `todos`
   sai do desenho (não é agente); vira uma frase ("Mensagens em difusão:
   N"). As 3 trocas peer-to-peer fora do hub (1 mensagem cada) também saem
   do desenho e viram uma frase de exceção, em vez de 3 arestas cobrando
   espaço geométrico por um dado tão raro. Agentes sem troca direta com o
   principal (`local`, `autor`) também viram frase, não nó vazio no leque.
   A tabela de dados exatos, que já existia e os pareceres validaram como
   "honestamente mais legível que qualquer grafo para consulta pontual",
   continua abaixo, inalterada.

## 3. Por que isso resolve o "carregado e congestionado"

Porque o problema nunca foi só a geometria — era tratar dado volátil
(tarefas agora) e dado quase-estático (287 mensagens desde o início) como
se tivessem a mesma urgência visual. Separar em dois planos (sempre visível
× recolhido) é o mesmo princípio que Plano e Coordenação já usam; a página
Agentes, isoladamente, tinha se desviado dele. A geometria do histórico
também melhorou (leque reto sem cruzamento, resolvendo o problema real de
sobreposição nos 3 pares de maior volume identificado pelo parecer de
grafos), mas é a hierarquia que faz a página parecer "limpa" ao abrir.

## 4. Reuso

`.kpis`/`.kpi`/`.kpi.hero` (já usado no Plano) para o KPI agregado —
nenhum componente novo de KPI. `.k-ag-dot[data-ag=...]` e os tokens
`--ag-*` (já existentes desde os ciclos 009/010, incluindo os 4 agentes
adicionados no ciclo 010) para toda cor de identidade — nenhuma cor nova.
`atividade`/sinal de vida (ciclo 009, `compute-mensagens.py`) reaproveitado
nos cards sempre que o agente tem esse dado computado (só os 4 agentes de
coordenação — os demais não mostram a linha, não fabricam "sem sinal" para
quem nunca teve o dado calculado). O padrão `<details>` fechado por padrão
para histórico (já usado em Coordenação para "Arquivadas") é reaplicado
aqui pela primeira vez fora daquela página. Nenhum script novo — tudo segue
vindo de `mensagens.json`, já carregado.

## 5. O que foi descartado e por quê (registro para o autor)

O SVG em anel com curvas e setas do ciclo 010 foi removido por inteiro —
não é uma correção incremental, é substituição. Justificativa dos 3
pareceres: a topologia é 100% imposta pelo protocolo de coordenação (hub
obrigatório), então desenhar o grafo inteiro não revela um achado, só
reafirma visualmente uma regra que já está escrita em prosa no CLAUDE.md.
O único dado genuinamente topológico (as 3 trocas peer-to-peer fora do hub)
sobrevive como texto, não como desenho.
