# ux-design.md — Mapa de Agentes (nova página)

- **Ciclo**: 010-mapa-de-agentes · **Lane**: light — pedido direto do autor
  ("uma tela... nós e arcos... número de tarefas dentro do nó"), 8ª página
  do site.

## 1. Quem entra como nó — 10, não 8

O autor listou 8: `local` (ele escreveu "agente local"), `executor01`,
`executor02`, `site`, `revisor1`, `revisor2`, `banca`, `principal`. Conferido
contra `docs/records/mensagens.json` (282 mensagens reais) e
`coordenacao/PROTOCOLO.md`, duas adições:

- **`autor`** (o próprio autor) — aparece de fato como remetente em 2
  mensagens reais. Excluí-lo do desenho faria o grafo mentir por omissão
  (essas 2 mensagens existem). Entra como nó.
- **`todos`** — não é um agente, é o destinatário de difusão (41 mensagens
  reais, ~15% do tráfego — maior que quase toda aresta nomeada individual).
  Apagar essas 41 mensagens do desenho também mentiria por omissão sobre "a
  quantidade enviada/recebida". Entra como nó, mas visualmente marcado como
  **não-pessoa**: reaproveita o mesmo contorno oco já usado para
  responsável "a definir" (ciclo 007) — sem cor própria, para não competir
  com os 9 agentes de verdade.

`local` está registrado no protocolo (`coordenacao/arquivo/.../
agente-local-registrado`) mas ainda não postou nenhuma mensagem sob esse
nome (0 ocorrências em `de`/`para`) — entra no desenho como qualquer outro
nó, só que com 0 em tudo; o próprio desenho já comunica "registrado, ainda
não usado" sem precisar de um rótulo especial.

## 2. Layout — hub no centro, não um círculo cego

O protocolo manda `principal` ser o hub obrigatório de toda mensagem
agente↔agente (PROTOCOLO.md §"o agente principal é o hub obrigatório") — e
os dados confirmam: das 23 arestas com tráfego > 0, só 2 não passam por
`principal` (revisor1→revisor2 e revisor1→banca, 1 mensagem cada — a
exceção, não a regra). Um círculo neutro (todo nó na borda) esconderia essa
estrutura real atrás de uma escolha de desenho arbitrária. Decisão:
`principal` fixo no centro, os outros 9 nós num anel ao redor — o layout
*é* o achado (quem depende de quem), não só uma disposição estética.

## 3. Dentro do nó — número de tarefas abertas com aquele agente

"Tarefas que está com o agente" = mensagens `tipo: tarefa` endereçadas a
ele (`para == agente`) que ainda não estão `concluida` (aberta ou
em-andamento) — é literalmente "a bola está com esse agente agora", o
mesmo predicado que a página Coordenação já usa para "ativas". Contra os
dados reais hoje: `principal` 4, `executor01` 4, `executor02` 4, todos os
outros 0 (inclusive `site` — fechei minha última tarefa antes deste
ciclo). Número grande, centralizado no nó — é o dado que estava sendo
pedido explicitamente, não decoração.

## 4. Arcos — direção, volume, e nada escondido

Cada par ordenado (de→para) com contagem > 0 vira uma curva própria (não
uma linha só bidirecional): `revisor1→principal` (61) e `principal→revisor1`
(27) são realidades bem diferentes e o desenho não pode achatar isso numa
média. Espessura do traço proporcional à contagem (piso de 1px para não
sumir, teto visual para a aresta principal↔revisor1 não engolir a página);
cor da aresta = cor do agente que ENVIA (reaproveita `--ag-*`, mesma lógica
de "de" já usada nos cartões do kanban) — segue com o olho de onde a
mensagem saiu. Seta na ponta indica o destino. `title` (tooltip) em cada
arco cravado com o número exato — a espessura é só um atalho visual, o
dado preciso está sempre a um hover de distância. Uma tabela recolhida
abaixo do desenho (`<details>`, mesmo padrão já usado em Plano/Coordenação)
lista as 23 arestas com contagem exata, para quem usa leitor de tela (SVG
decorativo não carrega esse dado para tecnologia assistiva) ou quer os
números sem precisar passar o mouse em cada curva.

## 5. Fonte de dados — nenhum script novo

Tudo já está em `docs/records/mensagens.json` (`mens`, já carregado no
módulo): a lista de mensagens tem `de`/`para`/`tipo`/`estado` para cada uma
das 282. `build_agentes()` agrega isso inteiramente no cliente (mesmo
padrão de `build_coordenacao()`) — nenhum `compute-*.py` novo, nenhuma
mudança em `painel.yml` (o arquivo já está entre os JSONs copiados para
`_site/`). Contagem de arestas usa TODAS as mensagens (inclusive
arquivadas) — é "quantidade enviada/recebida" no total, não só o que está
ativo hoje; contagem de tarefas no nó usa só as não-concluídas — é "está
com o agente" no presente. Os dois recortes são deliberadamente diferentes
e cada um está documentado onde aparece na tela.

## 6. Cores novas — 4 tokens, reuso do sistema existente

`--ag-*` hoje só cobre `principal`/`banca`/`revisor1`/`revisor2`/`autor`.
Faltam `site`, `executor01`, `executor02`, `local` — adiciono os 4 tokens
(claro+escuro, mesmo padrão dos 5 existentes) em vez de inventar um sistema
de cor novo. `todos` continua de propósito FORA da lista de tokens
nomeados: o fallback genérico já existente (`.k-ag-dot:not([data-ag=...])`,
ponto oco) passa a valer para ele automaticamente — é o mesmo mecanismo que
já dá o contorno oco a um responsável "a definir", reaproveitado sem
nenhuma linha de CSS nova para esse caso.

## 7. Reuso

`.k-ag-dot`/`--ag-*` (cores por agente, 4 tokens novos + reuso dos 5
existentes) · fallback oco para "não é um agente de verdade" (`todos`,
mesmo mecanismo do ciclo 007) · `<details>` para dado tabular abaixo de um
gráfico (mesmo padrão de Plano "Dados da série" e Coordenação
"Arquivadas") · nenhuma biblioteca de grafo — SVG à mão, mesmo approach já
usado no gráfico de evolução da prontidão do Plano (curva desenhada
diretamente em `<path>`, sem D3 nem force-simulation: só 10 nós e 23
arestas, layout fixo é mais previsível e testável que física de força).
