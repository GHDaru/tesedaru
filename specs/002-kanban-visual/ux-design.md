# ux-design.md — Board de Coordenação (`mensagens.html`)

- **Ciclo**: 002-kanban-visual · **Produzido por**: agente `ux-semantics`
  (consolidado pelo agente `site`) · **Consome**: `spec.md`,
  `scripts/render-plano-revisao.py` (`build_coordenacao()`),
  `docs/records/mensagens.json`, ADR 0006 · **Consumido por**: `plan.md`,
  implementação, `qa-report.md`

Artefato obrigatório deste ciclo (toca uma tela — Princípio VII: papel
semântico antes de componente). Não decide CSS pixel a pixel; decide o que
cada objeto da tela **é**, a partir da jornada que serve.

## 1. Jornada real do autor nesta tela

O autor não é um gestor de backlog revisando um board de projeto — é um
único humano coordenando 4 agentes assíncronos de IA, que abre esta tela
para responder, em segundos, uma pergunta operacional:

> **"Existe algo que só eu posso destravar agora, e a coordenação está
> saudável?"**

Evidências que sustentam essa leitura: o quadro é somente-leitura por
protocolo (o estado muda por `git mv` no repositório, nunca por clique
aqui); abaixo do board já existem "Saúde da coordenação" e "Locks de
superfície" — sinais de sistema, não de conteúdo; o cartão "para você" já é
tratado como o único destaque forte, assumindo que o valor da visita está
em achar rápido os poucos itens endereçados ao autor em meio a dezenas de
mensagens agente↔agente.

Duração e atenção da visita: segundos a ~1 minuto no caso comum ("nada
urgente, sigo o que estava fazendo"); alguns minutos no caso de decisão
real. Nunca uma sessão de gestão de backlog — esse papel não existe no
protocolo.

## 2. Papel semântico da coluna: "raia limitada" (bounded lane)

**Decisão**: a coluna é uma raia com altura ~constante e rolagem interna
própria — não uma lista total como em Trello/Linear (onde a coluna É a
fonte de verdade). Aqui a fonte de verdade é o repositório; o board é uma
**projeção de triagem** sobre ela, então não precisa mostrar as N unidades
de uma vez — precisa mostrar o suficiente para decidir, com acesso claro ao
resto via rolagem (nunca escondido atrás de paginação).

Por que altura ~constante entre as 3 colunas, e não proporcional ao
conteúdo: o valor central de um kanban é a leitura comparativa lado a lado
("Aberta" × "Em andamento" × "Concluída" na mesma faixa vertical). Uma
coluna 19× mais alta que as vizinhas quebra essa comparação. A contagem
numérica no cabeçalho (já existente, `.k-count`) é a unidade de comparação
correta — não a altura física da pilha.

Anatomia obrigatória: cabeçalho (glifo + nome + contagem) sempre visível,
fora do container que rola · corpo com altura máxima igual entre as 3
colunas do mesmo board · rolagem interna própria quando o conteúdo excede
essa altura · estado vazio textual quando 0 itens.

## 3. Papel semântico do cartão: "sinalizador de triagem"

**Decisão**: o cartão comunica "é isto que preciso saber para decidir se
abro o item" — não o texto completo da mensagem. Ordem de prioridade de
leitura, do mais para o menos crítico:

1. Destinatário sou eu? → badge "para você" (destaque único, ADR 0006 —
   não pode ganhar concorrente visual).
2. O que se espera, em 1-2 linhas? → título truncado (texto completo
   sempre acessível via `title`, nunca perdido — só não determina mais a
   altura do cartão).
3. De onde vem, para onde vai, que tipo? → rota (mantém como está).
4. Está estagnado? → idade + prazo + "atrasado" (segundo sinal de
   prioridade, precisa de mais peso do que tem hoje — sem virar um
   segundo destaque forte).
5. Onde investigar se decidir aprofundar? → referência — menor prioridade
   de escaneamento, sempre truncada/secundária (já correto hoje).

## 4. Papel que resolve o desequilíbrio 3 × 40

Composição de três decisões, não uma só:

1. Altura da raia é propriedade do **board**, não da coluna — impede que
   uma coluna cheia puxe a página inteira.
2. A contagem no cabeçalho é a unidade de comparação — o vazio ao lado de
   uma coluna cheia deixa de ser lido como "espaço desperdiçado" e passa a
   ser lido corretamente como "esta coluna tem poucos itens", que é
   informação verdadeira.
3. **Fila priorizada dentro da raia** (papel novo): ordenação por
   `atrasado && para-você` → `para-você` → `atrasado` → recência — garante
   que o essencial fique visível no topo mesmo sem rolar.

## 5. Altura do board vs. altura da página

**Decisão**: o board tem altura previsível (~constante); a página pode
continuar rolando, mas por causa do conteúdo fixo abaixo dele (Arquivadas,
Locks, Saúde) — nunca por causa do número de cartões dentro do board. Hoje
é o oposto: uma coluna sem teto sequestra o orçamento de atenção do autor,
empurrando "Saúde da coordenação" (que responde à mesma pergunta de
triagem) para uma rolagem enorme de distância.

## 6. Papéis reutilizados (não reimplementar)

`.card` (container de bloco) · `.pilula`/`.pilulas` (filtro alternável) ·
`.vazia` (estado vazio textual) · `.k-count` (rótulo de contagem) ·
`.k-card.para-voce` + `.k-badge` (destaque único do autor) ·
`&lt;details&gt;`/`&lt;summary&gt;` (registro histórico recolhido, já usado em
"Arquivadas") · escala tipográfica fixa e espaço em múltiplos de 4px
(`--fs-*`, `--sp-*`). Nenhum papel novo exige cor, fonte ou espaçamento
fora dessa escala.

## 7. Estados

| Estado | Papel |
|---|---|
| Vazio real (coluna com 0 itens, nenhum filtro ligado) | `.vazia` "Nada aqui" |
| Vazio por filtro (0 itens só porque uma pílula está desligada) | texto diferenciado ("Nada aqui com os filtros atuais") — evita o autor concluir "não há pendências" quando foi ele mesmo quem escondeu |
| Rolagem ativa / mais conteúdo abaixo | pista textual obrigatória: contagem no cabeçalho (glifo+palavra, nunca só cor) |
| Sem permissão / carregando | não se aplica — dados injetados inline, sem rede; board público somente-leitura |

## 8. Acessibilidade (decidida aqui, não só no fim)

- Glifo + palavra, nunca só cor (ADR 0006) — vale para todo elemento novo.
- Cada raia é uma região navegável: `role="region"` + `aria-labelledby`
  apontando pro `h2` já existente da coluna; container de rolagem com
  `tabindex="0"` + `aria-label` descritivo ("Coluna Aberta, N itens").
- Mudança de filtro anunciada via região `aria-live="polite"` — hoje o
  `innerHTML` é reescrito silenciosamente.
- Nenhuma cor nova — tudo reusa `var(--ink)`, `var(--muted)`,
  `var(--border)`, `var(--accent)`, `var(--atencao*)`.
- Truncagem por `title` nativo é mouse-only (gap real, achado pelo
  especialista de legibilidade) — registrado como follow-up em `spec.md`,
  fora do escopo deste ciclo por exigir um widget de disclosure focável.

## 9. Guardrails para a implementação

- Sem tokens novos de cor/tipografia/espaço.
- Sem affordance de arrastar (protocolo é somente-leitura via `git mv`).
- Altura máxima da raia igual entre as 3 colunas do mesmo board — nunca
  proporcional à contagem de cada uma (era o padrão que causou o bug).
- Preferir rolagem interna contínua a "carregar mais" por clique — a
  jornada é de vigilância rápida, cada clique extra é atrito não
  justificado.
- O destaque único do autor (borda âmbar + "para você") não pode ganhar
  concorrente — nenhuma mudança deste ciclo usa reforço visual comparável.
