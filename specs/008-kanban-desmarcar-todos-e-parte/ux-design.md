# ux-design.md — Kanban: desmarcar todos + parte da tarefa

- **Ciclo**: 008-kanban-desmarcar-todos-e-parte · **Lane**: light — pedido
  direto do autor na sessão, dois pontos concretos e pequenos.

## 1. "Nenhum" / "Todos" por grupo de filtro

Problema relatado: para ver só um agente, o autor tinha que clicar em
CADA um dos outros 4 para desligar (o padrão é tudo ligado). Solução:
dois botões de texto — "nenhum" e "todos" — acima de cada linha de
pílulas (um par para Agente, outro para Tipo, porque são eixos
independentes). Isolar um valor agora é 2 cliques ("nenhum" + clicar no
valor desejado), não 4. Desenho: botões de **texto sublinhado**, não
mais uma pílula — para não serem confundidos com um valor de filtro a
mais (são AÇÃO sobre o grupo, não um VALOR do grupo).

## 2. Parte da tese detectada — honestidade sobre cobertura parcial

O autor perguntou se dá para identificar a que parte a tarefa se
refere. As mensagens de coordenação não têm um campo estruturado para
isso — só texto livre (`referencia`, `acao_esperada`, slug do arquivo).
Decisão: badge **best-effort**, calculado em `compute-mensagens.py` por
regex sobre esse texto livre (nome de diretório de capítulo/apêndice ou
"Cap. N"), aparecendo no cartão **só quando detectado** — nunca um "—"
para o resto, porque a ausência não significa "sem parte", significa
"a mensagem não citou a parte nesse texto". Medido contra os dados reais:
33 de 121 mensagens (≈27%) têm parte detectável hoje.

Registrado para o autor (não implementado, é decisão dele/do principal):
cobertura completa exigiria os 4 agentes passarem a declarar um campo
`trilha`/`parte` no front-matter de toda mensagem nova — mudança de
protocolo (`coordenacao/PROTOCOLO.md`), fora da minha superfície
(planejamento é do `principal`). O `title` do badge já deixa isso
explícito: "Parte detectada a partir do texto da mensagem — nem toda
mensagem cita a parte".

## 3. Reuso

`.pilula`/`.pilulas` inalterados; `.k-parte` reaproveita a mesma anatomia
de badge com borda já usada em `.pill`/`.k-badge` no site inteiro (glifo
opcional + texto, nunca só cor). Nenhum papel novo de vulto — os botões
"nenhum"/"todos" são infraestrutura de filtro, catalogáveis como
reutilizáveis se outra página ganhar filtro de múltiplo grupo no futuro.
