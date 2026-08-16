# Protocolo de coordenação — 4 agentes + autor (v1.1)

> Regra única de mensageria, locks e processo multiagente da tese FALCO.
> Todo agente LÊ este arquivo ao iniciar a sessão e segue o ritual de entrada.
> Fonte: especialistas de mensageria e de processo (ADR 0008). Emendas por ADR.
>
> **Agentes registrados**: `principal` (prosa da tese) · `banca` (revisão
> crítica, read-only sobre o texto) · `revisor1` · `revisor2` (rodadas
> paralelas: fichamentos, dados, análises, normas) · `autor` (humano; único que
> mergeia na main e arbitra).
>
> A frase que resume tudo: **"Escreva só na sua superfície, verifique só o que
> não fez, poste só o que muda a ação de outro, e nunca espere parado — a main
> é do autor."**

## 0. Ritual de entrada (toda sessão, antes de qualquer trabalho)

1. `git pull --rebase origin main` — nenhuma leitura da caixa e nenhum claim
   vale sem pull no mesmo turno (a raiz de quase toda falha é pular isto).
2. Ler a caixa SÓ por glob: `ls coordenacao/caixa/*_<eu>_*` + `*_todos_*`.
   Nunca "ler tudo".
3. Arquivar (dever de quem chega): mover para `coordenacao/arquivo/AAAA-MM/`
   toda `.concluida` com >48 h e todo aviso com >7 dias; push.
4. Postar o aviso de início do próprio ciclo (§3, evento "claim").

## 1. Mensagens — nome de arquivo é a caixa de entrada

```
coordenacao/caixa/AAAAMMDD-HHMM_<de>_<para>_<tipo>_<slug>.<estado>.md
```

- `de`/`para`: `principal|banca|revisor1|revisor2|autor|todos` · hora em UTC
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
