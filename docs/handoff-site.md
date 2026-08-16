# Repasse — sistema do site da tese (para o agente de site)

> Documento de transferência escrito pelo agente `principal` a pedido do autor
> (2026-08-16). A partir daqui, **o site é sua superfície**: você é o dono dos
> arquivos listados em §2. O restante do repositório pertence a outros agentes
> (§6). Leia também `coordenacao/PROTOCOLO.md` e
> `docs/governance/constituicao-tese.md` antes de começar.

## 1. O que existe hoje, e por quê

O site nasceu de uma necessidade concreta: o trabalho da tese acontece em
várias sessões de IA paralelas mais o autor, e ninguém sabia "onde estamos".
A solução: um **plano em JSON versionado no git** é a fonte de verdade, e o
site é a **visualização** desse plano, re-renderizada automaticamente a cada
push. Nenhum estado vive no site; ele é sempre derivado de arquivos.

No ar hoje (GitHub Pages do repositório `GHDaru/tesedaru`, Source = GitHub
Actions):

| URL | O que é | Situação |
|---|---|---|
| `https://ghdaru.github.io/tesedaru/` | Painel de gestão (KPIs, fila do autor, burn-up, matriz capítulos × rodadas, coordenação, artefatos) | Funciona, mas **empilhado numa página só** — é o problema a resolver |
| `.../mensagens.html` | Caixa de mensagens entre agentes (tabelas Ativas/Concluídas/Arquivadas + locks) | Funciona; deve virar **kanban** |
| `.../plano-revisao.json`, `.../kpis.json`, `.../mensagens.json` | Dados brutos expostos | OK |

## 2. Sua superfície (arquivos que você passa a possuir)

```
docs/records/plano-artefato-template.html   # template do painel (JS vanilla inline)
docs/records/mensagens-template.html        # template da caixa de mensagens
scripts/render-plano-revisao.py             # injeta os 3 JSONs nos templates -> HTML
scripts/compute-kpis.py                     # calcula os 6 indicadores -> kpis.json
scripts/compute-mensagens.py                # varre coordenacao/ -> mensagens.json
.github/workflows/painel.yml                # CI: computa + renderiza + publica no Pages
```

**Você NÃO edita** (dono é outro agente): texto da tese (`N-*/texto.tex`,
`0-iniciais/`), `docs/records/plano-revisao.json` (conteúdo do plano — só o
`principal`), fichamentos, bibliografia, pareceres.

## 3. Como o sistema funciona (pipeline completo)

```
coordenacao/caixa/*.md ──► compute-mensagens.py ──► docs/records/mensagens.json ─┐
docs/records/plano-revisao.json ─► compute-kpis.py ─► docs/records/kpis.json ────┤
                                                                                  ▼
                                          render-plano-revisao.py (injeta JSONs nos templates)
                                                                                  │
                                                    ┌─────────────────────────────┴───────────┐
                                                    ▼                                         ▼
                                              _site/index.html                       _site/mensagens.html
                                                    └──────────► GitHub Pages (workflow painel.yml)
```

Gatilho do workflow: qualquer push na `main` que toque
`docs/records/plano-revisao.json`, os templates, os scripts, `coordenacao/**`
ou o próprio workflow. O checkout usa `fetch-depth: 0` porque a série temporal
do burn-up é reconstruída do histórico git do plano.

Testar localmente antes de publicar:
```bash
python3 scripts/compute-kpis.py && python3 scripts/compute-mensagens.py \
  && python3 scripts/render-plano-revisao.py /tmp/painel.html
# gera /tmp/painel.html e /tmp/mensagens.html
```

## 4. Restrições técnicas duras (não negociáveis)

- **Sem rede externa**: o Artifact do Claude (espelho do painel) roda sob CSP
  que bloqueia CDN, fontes web e ícones remotos. Tudo inline: CSS, JS vanilla,
  SVG. Nada de framework nem build.
- **Sem estado no site**: ele é derivado dos JSONs. Interação é leitura,
  filtro e navegação; nunca escrita (o estado real muda por commits no git).
- **Temas claro e escuro** obrigatórios, com a regra dos três estados: tokens
  completos em `:root`; redefinição em `@media (prefers-color-scheme: dark)`
  guardada por `:root:not([data-theme="light"])`; e de novo em
  `:root[data-theme="dark"]`. Nunca declarar uma cor só dentro de bloco de
  tema. `body` sempre com `background` explícito.
- **Repositório público**: nada de segredo, chave ou dado pessoal nas páginas.

## 5. O trabalho que o autor pediu (o encargo)

O autor relatou, literalmente: *"está tudo amontoado em uma página somente"*,
*"está muito empilhado, não consigo entender"*, *"estou com dificuldade em
fazer o controle e ter foco"*. Ele pediu:

1. **Páginas separadas com menu** e foco: cada página com um propósito claro.
2. **Sidebar recolhível**.
3. **Mensagens como board kanban** (colunas por estado; hoje é tabela).
4. **Página de resultados e entregas** (nova): hoje o sistema só mostra o que
   FALTA; não há vitrine do que a tese JÁ PRODUZIU. Conteúdo a abrigar:
   resultados por pilar (P1 amplitude de 6,4 p.p.; P2 DRI-SL supera o envelope
   evolutivo, correção de circularidade de −6,3 p.p.; P3 oráculos LLM com
   77–83% de acurácia a US$ 0,035–0,92 por mil rótulos, razão de custo 26×;
   P4 veredito refutado a 30% e alcançável a ~50%, com McNemar e IC bootstrap),
   artefatos entregues (tese de 90 p., 5 artigos, biblioteca Python,
   FlowBuilder, dataset público de 250 mil descrições em 621 categorias,
   métrica LCE, 142 fichamentos + grafo, ~20 relatórios) e os experimentos
   (E0, E0-P, E1, E4, E5, E6, E3′ + replays) com pergunta, resultado e
   artefato de cada um. **Outro agente preencherá o conteúdo**; você entrega a
   estrutura.
5. Padrão profissional de produto, não relatório.

**Uma especificação de UX/UI está sendo produzida** por um especialista sênior
(arquitetura de informação, sidebar, kanban, página de controle, página de
resultados, sistema visual completo, acessibilidade e armadilhas). O agente
`principal` a repassará a você assim que ficar pronta — **implemente-a linha a
linha**; ela é o contrato de design. Se ela não tiver chegado quando você
começar, peça ao `principal` antes de improvisar um layout próprio.

Decisões de design já tomadas e vinculantes (do UX anterior, ADR 0006):
- A página inicial responde, em cinco segundos: quanto falta · **o que espera
  o autor** · o que mudou.
- **Um único grito visual na interface, e ele pertence ao autor** (a fila
  "Aguardando você", em âmbar). Telemetria de agentes nunca compete com ela.
- Estados nunca por cor sozinha: glifo + palavra (○ aberta · ◐ em andamento ·
  ● concluída; ✓ feito · 🔒 em gate · ⛓ bloqueado).
- Burn-up com eixo Y fixo de 0 a 100% e eixo X em **datas reais** (semanas
  paradas devem aparecer).

## 6. Regras de convivência (protocolo multiagente)

- Ritual de entrada de toda sessão: `git pull --rebase`, ler a caixa por glob
  (`coordenacao/caixa/*_<seu-nome>_*` e `*_todos_*`), arquivar antigas, postar
  o claim do próprio ciclo.
- **Mensagens só para o `principal`** (ele roteia; ninguém fala direto com o
  autor) — constituição, princípio XII.
- **Site dispensa gate de merge** (ADR 0010): suas mudanças são reversíveis e
  não tocam o texto nem os dados, então você publica direto na `main`. Todo o
  resto do repositório exige gate do autor, consolidado pelo `principal`.
- Comunicação com o autor é sempre **didática e detalhada** (princípio XI):
  termos explicados, siglas abertas, sem telegrama.
- Push rejeitado = `pull --rebase` e tentar de novo. **Nunca** force-push.
- Decisão de arquitetura com efeito duradouro = ADR novo em `docs/adr/`
  (próximo número livre) + linha em `docs/records/decisoes.jsonl`.

## 7. Contexto que evita retrabalho

- Por que o JSON é embutido no HTML e não buscado por `fetch`: o espelho do
  painel roda em sandbox sem rede. Mantenha a injeção por marcador
  (`__PLANO_JSON__`, `__KPIS_JSON__`, `__MENSAGENS_JSON__`).
- Por que os indicadores usam "pontos de esforço" e não contagem de células:
  células têm custos muito diferentes; contagem seria métrica de vaidade
  (ADR 0006 traz a tabela de pesos e o que foi cortado).
- Por que o kanban é somente-leitura: o estado das mensagens muda por `git mv`
  (o rename é o claim atômico do protocolo). Comunique isso na interface para
  o usuário não tentar arrastar cards.
- O painel também é espelhado como Artifact do Claude; a URL fica em
  `docs/records/plano-artefato-url.txt`. O espelho é opcional e manual — o
  Pages é a cópia canônica.
