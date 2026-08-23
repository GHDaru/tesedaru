# Protocolo de coordenação — agentes + autor (v1.8)

> Regra única de mensageria, locks e processo multiagente da tese FALCO.
> Todo agente LÊ este arquivo ao iniciar a sessão e segue o ritual de entrada.
> Fonte: especialistas de mensageria e de processo (ADR 0008). Emendas por ADR.
>
> **Agentes registrados**: `principal` (prosa da tese) · `banca` (revisão
> crítica, read-only sobre o texto) · `revisor1` · `revisor2` (rodadas
> paralelas: fichamentos, dados, análises, normas) · `site` (páginas do painel,
> templates, scripts de render e workflow — publica sem gate, ADR 0010) ·
> `executor01` e `executor02` (execuções longas: treinos, varreduras, jobs —
> reportam ao principal; não editam texto nem plano) ·
> `local` (sessão na máquina do autor; acessa arquivos NÃO versionados —
> caches, PDFs, dados locais — e os publica onde o time alcança; mesmo
> protocolo de mensagens) ·
> `externo` (revisor independente contratado pelo autor, em outro provedor:
> lê a tese e produz PARECERES em `docs/pareceres-externo/`; NÃO edita prosa,
> bib, fichamentos nem plano — o valor dele é o viés diferente e a
> independência; reporta ao principal) ·
> `autor` (humano; único que mergeia na main e arbitra).
>
> A frase que resume tudo: **"Escreva só na sua superfície, verifique só o que
> não fez, poste só o que muda a ação de outro, e nunca espere parado — a main
> é do autor."**

## 0. Ritual de entrada (toda sessão, antes de qualquer trabalho)

0. **Quem sou eu**: consultar o título da própria sessão (`get_session` do
   MCP `claude-code-remote`, sem `session_id`) — o título é a fonte de verdade
   da identidade (ADR 0011). Título fora do registro de agentes → perguntar ao
   principal, sem assumir papel. Título apontando para papel que OUTRA sessão
   ativa já exerce → manter o papel que se vinha exercendo e avisar o
   principal; só o autor resolve renomeando/reatribuindo.
1. `git fetch origin main` **e integrar `origin/main` na sua branch** — é a
   MAIN, não a sua branch designada. Nenhuma leitura da caixa e nenhum claim
   vale sem isso no mesmo turno. **Repita a cada CICLO de trabalho, não só ao
   abrir a sessão**: execuções longas (executores) que só rebaseiam a própria
   branch NÃO veem as tarefas novas nem as respostas do principal — foi a raiz
   do descompasso do executor01 (22/08). Puxe a main antes de cada claim e de
   cada entrega. O hook `SessionStart` faz isso ao abrir; o resto do ciclo é
   com você.
2. Ler a caixa SÓ por glob: `ls coordenacao/caixa/*_<eu>_*` + `*_todos_*`.
   Nunca "ler tudo".
3. Arquivar (dever de quem chega): mover para `coordenacao/arquivo/AAAA-MM/`
   toda `.concluida` com >48 h e todo aviso com >7 dias; push.
4. Postar o aviso de início do próprio ciclo (§3, evento "claim").

## 1. Mensagens — nome de arquivo é a caixa de entrada

```
coordenacao/caixa/AAAAMMDD-HHMM_<de>_<para>_<tipo>_<slug>.<estado>.md
```

- `de`/`para`: `principal|banca|revisor1|revisor2|site|executor01|executor02|autor|todos` · hora em UTC
- `tipo`: `aviso|tarefa|pergunta` · `slug` kebab-case ≤40 chars
- `estado`: `aberta` → `em-andamento` → `concluida`, mudando SEMPRE por
  `git mv` (preserva a história; o sufixo fica antes do `.md`).

Exemplos:
```
20260816-1430_principal_todos_aviso_iniciando-cap2-lote2.aberta.md
20260816-1502_banca_principal_tarefa_reescrever-veredito-cap6.aberta.md
20260816-1610_revisor1_autor_pergunta_manter-apendice-a6.aberta.md
```

Front matter obrigatório (mensagem sem `para:` e `acao_esperada:` NÃO existe —
vira commit message ou nada):

```markdown
---
de: banca
para: principal
tipo: tarefa
acao_esperada: reescrever a seção e devolver para re-checagem da banca
referencia: 2-fundam/texto.tex#secao-2.3 · branch humanize/cap2 · plano cap2.R1
criada_em: 2026-08-16T15:02:00Z
prazo: 2026-08-18T12:00:00Z   # opcional
---
Corpo curto. Conteúdo grande vai em arquivo/commit normal; aqui só o hash.
```

## 2. Ciclo de vida

- **Aviso** (`para: todos` permitido): ninguém renomeia; morre por arquivamento.
- **Tarefa**: nasce `.aberta` → receptor faz pull, `git mv` para
  `.em-andamento`, push (o rename+push É o claim; para tarefas "todos", quem
  perde o push desiste) → ao terminar, acrescenta `## Resultado` (com hash do
  commit) e `git mv` para `.concluida`. Valida quem pediu (ou o autor);
  reprovou = tarefa NOVA referenciando a antiga — nunca "reabrir".
- **Pergunta**: a resposta é EDIÇÃO da mesma mensagem (`## Resposta (por X,
  data)`) + `git mv` para `.concluida`. Réplica = pergunta nova.

## 2-bis. Roteamento central (ADR 0009 — decisão do autor)

O agente **principal é o hub obrigatório** de todo o fluxo:
- Nenhum agente endereça mensagem diretamente ao `autor` — só o principal pode.
- Mensagens agente↔agente também passam pelo principal (`para: principal`),
  que decide o que sobe ao autor e o que redistribui, e para quem. Exceção:
  avisos broadcast (`para: todos`) de claim/conclusão continuam diretos.
- Planejamento (prioridades, fila, matriz, estrutura do plano) só muda pelas
  mãos do principal; cada agente segue atualizando o status da própria
  execução.
- **Gates de merge também sobem pelo principal (ADR 0010)**: o agente entrega a
  branch e manda conclusão ao principal (o que mudou · hash/branch · evidência ·
  risco); o principal consolida, verifica e leva ao autor em bloco, com
  antes/depois e recomendação. Nenhum agente pede aprovação direta ao autor.
  **Exceção**: mudanças do site/painel (`docs/records/*`, scripts de render,
  `coordenacao/`) dispensam gate — reversíveis, não tocam texto nem dados.

- **Canal de entrega de quem não alcança a main** (executor01, executor02, e
  qualquer sessão restrita à própria branch pelo harness): a mensagem ao
  principal nasce na `coordenacao/caixa/` **da branch designada** — ela NÃO
  chega à main sozinha, porque o agente não pode empurrar para lá. Isso é do
  harness, não falha do agente. Consequências: (a) o executor entrega normal —
  branch + `.aberta.md` ao principal, com hash — e segue; (b) **o principal não
  espera mensagem de executor na main**: ele varre as branches. A varredura é
  automática no hook `SessionStart` (`scripts/hooks/estado-da-sessao.py`), que
  lista "ENTREGAS/AVISOS AO PRINCIPAL PRESOS EM BRANCH"; o principal recupera
  com `git show <branch>:<caminho>`, integra na main e responde. O ciclo de
  15 min do principal repete essa varredura.

## 2-ter. Quem escreve na main, e nota de merge exige carga (anti-progresso-fantasma)

> Existe por um erro concreto (23/08): uma sessão-agente empurrou para a main a
> NOTA "lote-cap5 APROVADO, merge limpo" **sem levar o `.tex`** — o texto ficou
> preso na branch. Quem lê a main (o autor) acreditou que o Cap.5 estava no PDF;
> não estava. Duas mãos diferentes escrevendo na main, e a carga caiu na fenda.

1. **A main tem UMA mão: o principal, e só a mando do autor (gate).** É o
   principal quem materializa todo merge/push na main (§6, "autor: único merge
   na main" — na prática o principal são as mãos do autor no gate). **Nenhum
   outro papel empurra para a main** — nem prosa, nem artefato, nem "nota de
   coordenação/parecer/medição/APROVADO". Agente (banca, revisor1, revisor2,
   executor01/02, local, externo) entrega SEMPRE em branch/caixa da sua branch;
   o principal integra. Exceção única já existente: site/painel e
   `docs/records/*` (ADR 0010), reversíveis e sem tocar texto/dados.

2. **Nota de merge/aprovação é PROIBIDA sem a carga na main.** Ninguém escreve
   "mergeado / merge limpo / APROVADO / feito / fechado na main" sobre um
   conteúdo sem antes MEDIR que ele está de fato na main:
   - `git merge-base --is-ancestor <sha-do-conteúdo> origin/main` → verdadeiro; **ou**
   - `grep` de um marcador distintivo do conteúdo no arquivo-alvo em `origin/main`.
   Não está na main? O registro é "**recomendo o merge**" (pendente do
   principal/gate), nunca "feito". **Quem aprova o merge, mergeia no mesmo ato**:
   a nota de aprovação e o `.tex`/artefato vão juntos, ou a nota é só recomendação.

3. **O principal não confia na nota; mede.** Antes de dizer ao autor que algo
   está na main (ex.: "o PDF já tem o Cap.5"), o principal confere a carga pelos
   dois testes acima. Uma "APROVADO" na main sem a carga é um bug a consertar
   (fazer o merge que falta, ou rebaixar a nota), não um fato.

## 3. Cadência — só 4 eventos geram mensagem

1. **Claim** — iniciei ciclo/tarefa (evita colisão).
2. **Achado cross-agente** — descoberta que muda o trabalho de OUTRO agente.
3. **Bloqueio** — a mensagem diz QUEM destrava e O QUÊ; depois de postar,
   marque `blocked` no plano e PEGUE O PRÓXIMO item — proibido esperar parado.
4. **Conclusão** — com hash e o que o próximo deve fazer.

Não postar: progresso parcial, "recebido", reformulação do plano, achado que
só afeta a si mesmo. Limites: 10 mensagens ativas por remetente · 2 locks por
agente. NUNCA em mensagem: chaves/tokens, dados pessoais, conteúdo >5 KB (o
repositório é público).

## 4. Locks — push fast-forward como operação atômica

Nome determinístico pela superfície (sem timestamp — é o que força a colisão):

```
coordenacao/locks/2-fundam--texto.tex.md        # arquivo específico
coordenacao/locks/4-resultados-l0--ALL.md       # pasta inteira ("/" vira "--")
```

Front matter do lock: `dono, superficie, motivo (ref. à tarefa), criada_em,
renovado_em, ttl_min: 45`.

**Claim**: pull --rebase → lock já existe (ou ALL da pasta)? desiste/negocia →
cria e commita → push. **Só é seu depois do push aceito.** Push rejeitado →
pull --rebase; se o rebase revelar o lock do concorrente, aborta e desiste.
Force-push em main é proibido em qualquer circunstância.

**TTL 45 min · heartbeat ~15 min** (commit tocando `renovado_em`; pode ir com
commits de trabalho). Fonte de verdade = timestamp do último COMMIT que tocou
o lock (`git log -1 --format=%cI -- <lock>`), nunca o YAML.

**Trabalho entregue aguardando gate**: o lock pode (e deve) ser liberado ao
publicar a branch para gate — a proteção da superfície passa a ser o estado
"gate" registrado no plano/tarefa: nenhum agente edita superfície com
pendência de merge em gate. O TTL de 45 min é para edição ATIVA, não para a
espera (que pode durar dias) pela decisão humana.

**Quebra**: lock vencido (>45 min sem commit) — qualquer agente pode remover,
DESDE QUE no mesmo commit crie aviso `lock-quebrado-<superficie>` para o
ex-dono. Lock no prazo: ninguém quebra, nunca (pergunta ao dono). O autor
quebra qualquer lock a qualquer momento. **Liberação normal: a remoção do lock
vai no MESMO commit/merge que integra o trabalho** (atômico). Abandono: remove
lock + aviso.

## 5. Superfícies de propriedade

| Superfície | Regime |
|---|---|
| `N-*/texto.tex`, `0-iniciais/` (prosa) | **Dono único: principal** — banca cita linha/commit, nunca edita |
| `docs/pareceres*` | Dono único: banca; parecer publicado é imutável (correção = novo parecer) |
| `fichamentos/` | revisor1/revisor2 por arquivo; verificação cruzada gera arquivo do VERIFICADOR, não edição no do outro |
| `referencias.bib`, figuras, `00-*.tex`, `ppginf.cls` | Compartilhada **com lock** |
| `scripts/` | Dono por arquivo (header declara); alheio = lock + mensagem |
| `docs/records/plano-revisao.json` | Compartilhada com lock; cada agente edita só seus campos; matriz e fila: só o autor |
| `docs/adr/` + `decisoes.jsonl` | **Append-only, sem lock** (imutáveis) |
| `coordenacao/caixa/` | Append-only + renames pelo protocolo, sem lock |

Padrão: dono único; lock é exceção; append-only nunca tem lock.

## 6. Verificação — quem executa não verifica

- **banca → principal**: sim (é o papel dela); banca nunca edita prosa.
- **revisor1 ↔ revisor2**: verificação cruzada obrigatória antes do gate.
- **principal** não verifica ninguém; correções por parecer voltam à banca.
- **autor**: única instância final; único merge na main.

## 7. Escalonamento (desacordo entre agentes)

Parecer publicado → UMA réplica escrita do outro agente (em
`docs/pareceres-replicas/`) → item vai à fila do autor com os dois links → o
AUTOR arbitra sempre. Sem tréplica; agentes nunca editam o trabalho um do
outro para "resolver". Decisão com precedente = ADR novo; pontual = campo no
plano. Parecer rejeitado não é apagado.

## 8. Saúde do processo (computável de caixa + git)

1. Mensagens ÷ commits de conteúdo por semana: saudável 0,2–0,5 (>1 =
   burocracia; ~0 com 4 agentes = colisão chegando).
2. Idade do bloqueio aberto mais antigo: >48 h = gate engarrafado.
3. Retrabalho pós-gate (reverter trecho aprovado): subindo = verificação
   virou teatro.

## 9. Mensageria entre sessões (poke cross-session) — o poke é PONTEIRO

> Fonte oficial: https://code.claude.com/docs/en/cross-session-messaging
> Testado 2026-08-23 (ida e volta). Padrão desenhado por 2 especialistas
> (mensageria + processo) + gate do autor (decisões A–G; v1.8 = decisões I1–I8).

**v1.8 — a caixa viva mora na branch `mensageria`, não na main.** A `main` é só a
tese; a `coordenacao/caixa/` viva vive na branch **`mensageria`** (descendente da
main, mão única do principal, gate-free por ADR 0010). A main guarda a caixa
**histórica congelada** (não se escreve mais lá; ver o README-ponteiro em
`coordenacao/caixa/`). `mensageria` NUNCA faz merge na main. Consequência: a
"fenda de duas mãos" do §2-ter deixa de ser possível por construção. O hook
`estado-da-sessao.py` lê a caixa de `origin/mensageria`; entregas de conteúdo
seguem nas branches designadas dos agentes. `PROTOCOLO.md`, `adr/`,
`decisoes.jsonl` ficam na **main** (I2). `locks/` NÃO migrou nesta rodada (I3).

**v1.8 — automação e pickup.** As tools `create_trigger`/`fire_trigger` estão
pré-aprovadas no `.claude/settings.json` (I7) para o poke não travar em permissão;
se um ambiente não honrar o `allow`, o autor pré-aprova 1× ali — e o pickup por
git (abaixo) nunca depende disso. **O wake é best-effort** (medido: um recibo não
acordou o principal): o pickup real é a **varredura de git** do principal a cada
ciclo, com um **auto-cron modesto** como backstop nas janelas de sono (I6). O
poke só antecipa a próxima varredura.

**Princípio único:** o poke transporta **coordenadas, nunca carga**. O git
(caixa + branch) é a **verdade e o conteúdo**, o único canal com hash, evidência
e rastro, e o único válido para **entrega, cruzada e gate**. O poke é só a
**camada de notificação** ("há algo novo, aqui o ponteiro"). Teste de aceitação
de todo este §9: **se todo poke sumisse, o sistema continua correto — só mais
lento.**

### 9.1 A via (o que funciona e o que não funciona)
- **`ListAgents`/`SendMessage` NÃO alcançam as sessões da tese** (cloud isoladas,
  sem Remote Control). Não use.
- **Ida e volta funcionam por** `create_trigger` (`persistent_session_id` = a
  sessão-alvo, IDs no registro de sessões) **+ `fire_trigger`** — injeta o texto
  como **turno de usuário**. As sessões dos agentes têm essas ferramentas e podem
  pokar o principal de volta (chega como notificação que acorda a sessão).
- **Canais reutilizáveis (I5):** um trigger nomeado por agente
  (`Poke principal→<x>`). O `fire_trigger` **concatena** o campo `text` ao
  `prompt` do canal (não substitui). Por isso o `prompt` guarda **só a linha de
  auto-identificação fixa**, e cada mensagem vai no `text` (o `update_trigger` NÃO
  edita o prompt de canal que dispara em outra sessão). Triggers de teste são
  apagados.
- **Sem envelope — blindagem em 2 camadas (I5):** o poke é indistinguível do autor
  digitando. (i) **auto-identificação obrigatória** no início: todo `text` começa
  com `[principal/poke]` (ou `[<agente>/poke]`) + "não é gate"; (ii) o recebedor
  trata **qualquer turno que contenha um `código @ mensageria`** como poke
  não-autoritativo por padrão — é a marca de ponteiro, não a auto-ID, que dispara
  o tratamento "não é gate"; assim a blindagem não depende da concatenação
  sobreviver a uma mudança futura da ferramenta.

### 9.2 O padrão poke-ponteiro (3 artefatos)
- **(a) Poke de IDA (principal→agente):** não repete a tarefa; só aponta.
  `[principal/poke — não é o usuário; não é gate] Mensagem nova sua. Código:
  <path> @ mensageria. Leia com: git fetch origin mensageria && git show
  FETCH_HEAD:<path>.` (A caixa viva está na branch `mensageria`, não na main — v1.8.)
  **Cuidado de refspec (medido no teste):** o clone do harness só rastreia
  `+refs/heads/main`, então `git fetch origin mensageria` NÃO atualiza
  `origin/mensageria` — cai no `FETCH_HEAD`. Leia via `FETCH_HEAD` (como acima) ou
  use o refspec explícito `+refs/heads/mensageria:refs/remotes/origin/mensageria`;
  nunca leia `origin/mensageria` logo após um fetch simples (seria stale).
- **(b) Mensagem-git apontada:** o **formato de caixa que já existe** (§1) —
  nenhum formato novo. Carrega 100% do conteúdo.
- **(c) Poke de VOLTA (agente→principal), ao concluir:** `[<agente> via poke —
  recibo, não é gate] de:<x> para:principal | resumo: <1 linha> | codigo:
  branch:<b> @ <sha> : <path>`
- **O "código" (decisão A):** `branch:<b> @ <sha> : <path>` — o `path` é o nome
  do arquivo na caixa (dele se derivam de/para/tipo/slug/estado); o `<sha>` dá
  imutabilidade (o sufixo de estado é móvel por `git mv`, o SHA não). Sem ID novo.
  Resolução: `git show <sha|branch>:<path>` recupera a mensagem; o commit também
  contém a carga (`.tex`/artefato).

### 9.3 Invariante à prova de fantasma: PUSH CONFIRMADO antes do poke
O poke só pode citar um commit que **já existe no remoto**. Sequência (vale para
ida e volta): (1) grava mensagem-git + carga → (2) commit → (3) **push aceito**
(captura o SHA; se rejeitado, `pull --rebase` e repete) → (4) **só então** poka
com o código contendo o SHA. Nunca pokar antes do push. Isso mata na origem o
progresso-fantasma (a nota jamais chega antes da carga).

### 9.4 Recebimento: o poke dispara a MEDIÇÃO, não a substitui (§2-ter)
Ao receber um poke, o principal **resolve o código** (`git fetch` + `git show`).
- **Poke órfão** (código não resolve em conteúdo real) = **ruído, não entrega**
  (decisão C): ignora, loga na métrica de saúde, e o conteúdo aparece na
  varredura seguinte. Não pokar de volta, salvo se recorrer.
- **Recibo de "terminei/aprovado"**: o `resumo` NUNCA substitui a medição. Antes
  de gate/afirmar "está na main", o principal mede os dois testes do §2-ter
  (`git merge-base --is-ancestor <sha> origin/main` **ou** `grep` do marcador).
  Não passou = vale só como "recomendo o merge", nunca "feito".

### 9.5 Backstop e idempotência (o git é a verdade do estado)
- **Backstop:** a varredura de ~15 min do principal (glob da caixa + branches) e
  o hook `SessionStart` pegam tudo que o poke perder; o agente age **pela lista
  do git/hook, não pelo texto do poke**. O poke só antecipa a varredura.
- **Idempotência:** o estado vive **só** no sufixo (`.aberta/.em-andamento/
  .concluida`) + SHA, nunca no poke. Poke 2× ou 0× dá o mesmo resultado; o
  `git mv`+push é o claim atômico. Dedup é **implícita** (o principal mede o git,
  não conta pokes) — **1 poke por transição de estado** (decisão B), sem arquivo
  de controle extra.

### 9.6 Cadência, limites e saúde
- **Só se poka na CONCLUSÃO** (e no despacho de tarefa nova) — decisão D;
  claim/`em-andamento` aparecem na varredura, não geram poke.
- **Emissão fica com o agente**, não com o hook (decisão E): auto-emissão
  arriscaria poke prematuro/duplicado.
- **Teto** de pokes por remetente/ciclo, espelhando as 10 mensagens ativas do §3
  (decisão F), contra uso como chat.
- **Sem MCP nos dois lados:** o SLA da varredura de 15 min é o piso aceitável
  (decisão G); o poke é bônus de latência, nunca o único caminho.
- **Métrica de saúde (§8):** taxa de *poke órfão* (>0 = poke correndo à frente do
  push); *bytes/linhas por poke* crescendo = conteúdo vazando para o canal
  errado; *decisão tomada só por poke* sem medição registrada = uso indevido.
