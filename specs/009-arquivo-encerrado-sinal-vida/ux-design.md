# ux-design.md — regime de loop: arquivo no kanban, capítulo encerrado, sinal de vida

- **Ciclo**: 009-arquivo-encerrado-sinal-vida · **Lane**: light — tarefa direta
  do `principal` (`20260817-2255_principal_site_tarefa_sua-frente-painel-em-regime-de-loop`),
  três ajustes pequenos e independentes para o novo regime (todos os agentes
  em loop, caixa limpa de 287→21 e depois arquivo com 266 mensagens).

## 1. Arquivo no kanban — já resolvido, não é regressão

O pedido presumia que `compute-mensagens.py` só varria `caixa/`, e que a
limpeza (287→21, 266 arquivadas em `coordenacao/arquivo/2026-08/`) teria
esvaziado o histórico do painel. Investigação: isso já não é verdade desde o
primeiro ciclo da página Coordenação (commit `ec2bf01`) — o script já lê
`coordenacao/arquivo/*/` além de `caixa/` e marca cada mensagem com
`arquivada: true/false`; o front-end já renderiza um `<details>` recolhido
"Arquivadas (N)" abaixo do quadro. Regenerando os dados reais: 281 mensagens
totais, 252 arquivadas, 29 ativas — o histórico não sumiu. Nenhuma mudança de
código foi necessária aqui; o item foi verificado com dados reais e a
resposta vai para o `principal` explicando o que já existe (evita
reimplementar algo que já funciona).

## 2. Capítulo encerrado — destaque na linha, não só um texto a mais

`capitulos[].encerrado` no plano é uma string (data + justificativa) quando o
autor declarou o capítulo fechado — hoje Cap.1 e Cap.2. É "o marco que o
autor mais olha" (palavras do `principal`), e a tabela "Capítulos × rodadas"
é a visão mais olhada da página mais olhada do site. Decisão: selo
`✓ encerrado` (mesma classe `.pill.feito` já usada em todo o site — reuso, não
uma cor nova) ao lado do título do capítulo, mais um leve tingimento de fundo
na linha inteira (`--st-feito-bg`, o mesmo tom do selo) para que o encerramento
salte aos olhos até em rolagem rápida, sem competir visualmente com as
pílulas de rodada (que continuam sendo o dado principal da linha). O `title`
do selo carrega a justificativa completa registrada no plano — nada de
esconder o "porquê" atrás de um ícone.

## 3. Sinal de vida — diagnóstico primeiro (o pedido literal não funciona)

O `principal` sugeriu derivar de "último commit por autor nas últimas 2h".
Verificação antes de implementar (`diagnose-before-fix`): nos últimos 300
commits do repositório, 295 têm autor git `Claude` e só 4 têm `revisor2` — ou
seja, o autor do commit git **não distingue quem é quem** na prática (quase
todo agente commita como `Claude`, independente de qual papel está
assumindo). Implementar literalmente "por autor git" produziria um painel
que mostra sempre o mesmo (ou nenhum) agente ativo — pior que não ter o
recurso.

Sinal real disponível e já commitado a cada ação do protocolo:
- o timestamp da própria mensagem que o agente posta em `coordenacao/`
  (campo `de`, já no `mensagens.json`);
- a renovação do lock que o agente segura (`locks/*.md`, já rastreada como
  `renovado_ha_min` no mesmo JSON).

`compute-mensagens.py` agora calcula, para os 4 agentes de coordenação
(`principal`, `banca`, `revisor1`, `revisor2` — os mesmos do filtro
`AGENTES` já existente na página), o mais recente entre os dois sinais;
`ativo` = essa marca ficou dentro de uma janela de 2h (o número que o
`principal` pediu), exposta como `ativo_janela_min` no JSON para não haver
mágica escondida no front-end. Indicador discreto: uma linha fina acima dos
filtros, um `k-ag-dot` (mesma cor por agente já usada no site inteiro) por
agente com o rótulo "há Xmin"/"há Xh"; inativos ficam com opacidade reduzida
em vez de sumir — "sem sinal recente" também é informação. `title` explica a
metodologia por extenso, para não passar a falsa impressão de ser um sinal
de infraestrutura (heartbeat de verdade) quando é, na origem, atividade de
protocolo.

## 4. Reuso

`.pill.feito`/`--st-feito-bg` (já existente, usado em toda pílula "feito" do
site) para o selo de capítulo encerrado — nenhuma cor nova. `.k-ag-dot`
(já existente, cores por agente) para o sinal de vida — só uma variante de
opacidade nova (`.vida-inativo`) para o estado "sem sinal recente", que seguia
o mesmo padrão do `.tema-resp-indef` do ciclo 007 (opacidade reduzida para
"sem dado", não uma cor de alerta).
