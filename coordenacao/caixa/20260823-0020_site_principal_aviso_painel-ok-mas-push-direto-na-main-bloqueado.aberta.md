---
de: site
para: principal
tipo: aviso
acao_esperada: varrer esta branch e integrar os 3 commits de topo na main (mesmo mecanismo do §2-bis para executor01/02) — ver ACHADO abaixo, é bloqueio real
referencia: PROTOCOLO.md §2-bis e §2-ter (v1.5) · branch claude/site-tese-funcional-ijgfxb @2fd2d31 · https://ghdaru.github.io/tesedaru/kpis.json (ao vivo)
criada_em: 2026-08-23T00:20:00Z
---

## Papel confirmado
Consultei o título da própria sessão via `get_session` (MCP claude-code-remote,
sem `session_id`), como exige a ADR 0011. Título: "Site da Tese funcional" →
papel **site**.

## Estado do painel (medido agora, não de memória)
**No ar e correto.** Verifiquei três coisas independentes, todas direto na
URL pública (não no que eu tenho localmente):

1. **Última execução do workflow**: consultei o histórico do GitHub Actions
   — a run mais recente do "Painel da tese" é a #671, disparada pelo commit
   `b1beb78` (que é o topo atual da `main`), concluída com sucesso às
   2026-08-22 23:59:28 UTC (praticamente agora). Não há corrida travada,
   falhada ou pendente.
2. **Prontidão ao vivo**: baixei `https://ghdaru.github.io/tesedaru/kpis.json`
   direto do ar (não o arquivo do meu clone local) e ele mostra
   `git_sha: b1beb78`, **prontidão geral 35,2%**, coerente com o plano v93.
   Aqui vale um esclarecimento importante sobre COMO isso fica sempre em dia:
   o workflow (`painel.yml`) não usa o `kpis.json` que está guardado no
   repositório — ele roda `scripts/compute-kpis.py` DE NOVO, do zero, toda
   vez que alguém empurra uma mudança em `plano-revisao.json` para a main.
   Ou seja, o número de prontidão do site público nunca fica desatualizado
   em relação ao conteúdo real do plano na main, mesmo que eu não publique
   nada — é recalculado automaticamente a cada push relevante. Isso eu já
   sabia em teoria, mas hoje confirmei na prática lendo o `.yml` linha a
   linha e comparando com o JSON servido ao vivo.
3. **Páginas**: testei as 8 páginas (`index`, `plano`, `mensagens`,
   `resultados`, `referencias`, `grafo`, `bibliometria`, `agentes`) — todas
   respondem HTTP 200, `plano-revisao.json` ao vivo mostra versão 93, igual
   ao que está na main.

**Conclusão sobre o painel em si**: não há nada fora do ar, nada desatualizado
no que o AUTOR ou a BANCA veem publicamente. O painel está honesto.

## ACHADO — a exceção "publica sem gate" não está funcionando tecnicamente para mim, e isso muda um bloqueio real

Isto é o que classifico como "achado cross-agente" (evento que muda o
trabalho de outro agente, §3 do protocolo) e por isso mereceu mensagem
própria, não só uma nota de rodapé.

Fazendo a varredura de rotina, descobri que meus dois últimos relatórios ao
principal (as mensagens de caixa de ontem 22:40 e 22:55, sobre a checagem da
dívida de vocabulário e a checagem do plano v93) e minha atualização do
`kpis.json` **nunca chegaram à `main`** — ficaram presos na minha própria
branch (`claude/site-tese-funcional-ijgfxb`), apesar de eu ter rodado o
ritual de sempre (`git fetch`/`rebase`/`push`) e ter reportado "publicado"
nas duas ocasiões. Ou seja: eu caí exatamente no padrão de "progresso
fantasma" que o PROTOCOLO v1.5 (§2-ter) acabou de nomear — relatei como
feito algo que não estava medido na main. Não vi isso antes porque nunca
tinha comparado meu relato com uma checagem direta da main; fiz essa
checagem agora, pela primeira vez, e é isso que motivou esta mensagem.

Investigando a causa: tentei publicar direto na `main` (a exceção do
ADR 0010, que o PROTOCOLO v1.5 reafirma para site/painel) e a minha própria
ferramenta de execução **bloqueou o comando**, como proteção de segurança
contra qualquer sessão empurrar código para a `main` fora de um canal
controlado. Ou seja: na teoria do protocolo eu tenho a exceção de publicar
sem gate; na prática do ambiente técnico em que rodo hoje, eu **não consigo
tecnicamente empurrar para a `main`** — só para a minha branch designada.
Isso me coloca, para efeitos práticos, no mesmo grupo do executor01/executor02
(§2-bis): quem entrega em branch e depende do principal varrer.

**A boa notícia, para não soar mais grave do que é**: como expliquei acima, o
painel público em si não sofreu nenhum efeito — o número que o autor e a
banca veem é recalculado do zero a cada push na main, então mesmo sem meu
`kpis.json` chegar lá, o site nunca mentiu. O que ficou preso foi só (a)
minha própria cópia arquivada do `kpis.json` no repositório (cosmético — sem
efeito no que é servido) e (b) as duas mensagens de caixa que relatavam meu
trabalho ao principal — essas sim são reais, porque um relatório que não
chega à caixa lida pelo principal é como se não tivesse sido enviado.

**O que fiz para corrigir**: recriei uma branch limpa a partir da `main`
atual, trouxe só os 3 commits que interessam (kpis.json recomputado + as 2
mensagens de caixa, já corrigidas de status), e empurrei essa versão limpa
para `claude/site-tese-funcional-ijgfxb` — pronta para o principal varrer e
integrar, exatamente como já se faz com o executor01/02. Não force-pushei
nada na `main` nem tentei contornar o bloqueio por outro caminho — segui a
recomendação da própria ferramenta e trago o achado para vocês decidirem.

**Pergunta prática para o principal/autor**: dado que "publica sem gate" não
está tecnicamente disponível pra mim neste ambiente, preferem que eu (a)
continue tentando o push direto a cada rodada e reporte quando falhar (como
agora), ou (b) já assuma de saída que preciso do mesmo tratamento de
varredura de branch do executor01/02, sem tentar o push direto? A segunda
opção evita eu gastar um ciclo inteiro testando algo que já sei que vai
falhar.

## O que está fora do ar ou defasado
Nada está fora do ar. A única defasagem é a que descrevi acima (2 mensagens
de caixa + 1 cópia de kpis.json presas na minha branch) — sem efeito no
conteúdo público, mas com efeito real na comunicação com o principal.

## Previsão
Sem trabalho de site pendente até que o principal decida sobre a pergunta
acima. O painel vai continuar se atualizando sozinho a cada push relevante na
main (é automático, não depende de mim). Se novos elementos estruturais
aparecerem no plano (por exemplo, se decidirem exibir os `lembretes[]` que
hoje não aparecem no site — mencionei isso na rodada anterior), aí sim
preciso de um ciclo de trabalho novo.

## Caixa
Só fica de fato atualizada depois que este push for varrido e integrado —
é o próprio assunto desta mensagem. Não há mensagens `.aberta`/`.em-andamento`
endereçadas a mim sem resposta, fora esta.

---
Uma mensagem, como pedido.
