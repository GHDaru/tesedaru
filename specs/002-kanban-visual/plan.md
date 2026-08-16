# Plan 002 — Board kanban da Coordenação: caber na tela

- **Spec**: `spec.md` · **UX**: `ux-design.md` · **Lane**: light · **Date**: 2026-08-16

## Constitution Check (docs/governance/principles.md)

| Principle | Compliance |
|---|---|
| I. Spec-driven | ✅ `spec.md` nasce do relato do autor + achados independentes de 3 especialistas, e fixa FR1–FR8 antes de qualquer CSS/JS ser tocado. |
| II. Human-governed orchestration | ✅ autor pediu o ciclo e decide o resultado; agente `site` executa; achados fora do escopo visual (ex.: se "para você" deveria cobrir `para:"todos"`) são explicitamente NÃO decididos aqui — vão para `principal`/autor. |
| III. Reversibility / risk gates | ✅ mudança é só CSS/JS de uma função de um script gerador estático — reversível por `git revert`; nenhum dado é alterado; sem gate humano de merge (ADR 0010, site/painel). |
| IV. Test-first / verifiable DoD | ✅ AC1–AC5 em `spec.md` são executáveis via Playwright (altura medida, scroll testado, ordem do DOM verificada, atributos ARIA verificados) — evidência em `qa-report.md`, não julgamento. |
| V. Context economy / boundary | ✅ 3 especialistas em paralelo, cada um cego aos outros dois, cortados por fronteira de expertise (semântica / mecânica kanban / acessibilidade) — não por arquivo, porque os três precisavam ler o MESMO código para diagnosticar; consolidação single-threaded (eu) depois. |
| VI. Living artifacts | ✅ `ux-design.md` é o artefato consumido pela implementação e citado nela; achados fora de escopo (título/referência inacessível por teclado, estado de dados ausente, semântica de "para você") registrados em `spec.md` §Out of scope, não perdidos. |
| VII. Light governance / YAGNI | ✅ mecanismo de corte por DOM quebrado é removido, não "consertado com mais uma condição"; nenhum token novo de design; container queries citadas e descartadas como base (enhancement futuro, não obrigatório). |
| VIII. Intelligible communication | ✅ "raia limitada" (bounded lane), único termo novo introduzido pelos especialistas, é definido na primeira ocorrência em `ux-design.md` §2. |

**No violations.**

## Artifacts of this cycle (declare all five)

| Artifact | Declaration | Why |
|---|---|---|
| `research.md` | `ART:research=no` | não há incógnita técnica a resolver antes de decidir — `overflow-y:auto` é CSS padrão, sem escolha de biblioteca/protocolo em jogo. |
| `data-model.md` | `ART:data-model=no` | nenhuma entidade nova; `mensagens.json` não muda de forma. |
| `contracts/` | `ART:contracts=no` | nenhuma interface nova entre partes — o board continua consumindo o mesmo JSON injetado inline. |
| `checklist.md` | `ART:checklist=no` | os 5 critérios de aceite executáveis em `spec.md` cobrem a qualidade deste ciclo; não há checklist adicional além do DoD. |
| `ux-design.md` | `ART:ux-design=yes` | toca uma tela — não é opcional (Princípio VII). Produzido pelo agente `ux-semantics`, consolidado neste ciclo. |

## How

### Diagnóstico consolidado (convergência dos 3 especialistas, independente)

Causa raiz dupla, confirmada de forma independente pelos três: (1)
`.k-cards` não tem `max-height`/`overflow`, cresce linearmente com N
cartões; (2) `CAP_ENABLED = ativas.length > 50` mede o total do board
inteiro, não o tamanho de cada coluna — uma coluna isolada com 38 cartões
nunca aciona o corte se a soma das 3 colunas ficar abaixo de 50, e mesmo
quando aciona, só limita nós do DOM, não a altura visual.

### Decisão de implementação

1. **Altura**: `.k-cards` ganha `max-height:clamp(320px,58vh,640px)` +
   `overflow-y:auto` + `overscroll-behavior:contain`. Teto vai na LISTA
   (`.k-cards`), não na coluna (`.k-col`) — senão colunas curtas
   ("Concluída", 1 item) esticariam até o teto artificialmente, invertendo
   o comportamento correto atual (coluna curta = caixa curta). Cabeçalho
   da coluna (`.k-col-h`) fica fora do container que rola — sempre
   visível, sem precisar de `position:sticky`.
2. **Remoção do corte quebrado**: `CAP_ENABLED`/`CAP`/lógica de
   `mostrar`/`resto`/botão "+N mais" (linhas ~662-663, 705-706, 712,
   715-721 da função atual) são removidos. A rolagem interna resolve
   exibição sem esconder cartões reais atrás de clique — cumpre "sem
   paginação nem rolagem infinita" com mais fidelidade do que o mecanismo
   anterior, que era paginação disfarçada e estava quebrado.
3. **Ordenação por prioridade**: nova função de comparação aplicada antes
   de renderizar cada coluna — `(atrasado && paraVoce) > paraVoce >
   atrasado > recência (ordem atual por `ts` desc)`.
4. **Densidade do cartão**: `.k-titulo` ganha `-webkit-line-clamp:2` +
   `overflow:hidden` + atributo `title` com o texto completo (mesmo padrão
   já usado em `.k-ref`); `.k-card` ganha `line-height:1.3` (em vez do
   1.55 herdado do body, pensado para prosa) e padding/gap reduzidos
   dentro da escala existente (`--sp-2`/`--sp-1`). "Atrasado" ganha `⚠` +
   negrito, mantendo-se inline no rodapé — sem virar um segundo destaque
   forte (ADR 0006).
5. **Breakpoint intermediário**: entre 601–1099px, `.k-board` vira
   `display:flex; overflow-x:auto` com `.k-col{min-width:260px}` em vez de
   espremer 3 colunas fixas. ≥1100px mantém grid de 3 colunas; ≤600px
   mantém empilhamento vertical (ajustado de 900px para 600px, coerente
   com o novo comportamento intermediário).
6. **Acessibilidade barata**: `role="region"` + `aria-labelledby` em cada
   `.k-col` (apontando pro `id` do `.k-col-h` correspondente,
   gerado dinamicamente); `tabindex="0"` + `aria-label` no container
   `.k-cards`; região `aria-live="polite"` anunciando a contagem
   filtrada após cada mudança de pílula.
7. **Estado vazio por filtro**: `passaFiltro` já existe; ao renderizar
   coluna vazia, checar se `itens.length === 0` mas a coluna TINHA
   mensagens antes do filtro — se sim, texto "Nada aqui com os filtros
   atuais" em vez de "Nada aqui".

### O que NÃO fazemos neste ciclo (com razão registrada)

- Tipo do cartão como borda colorida (risco de competir com a borda âmbar
  de "para você" — ADR 0006).
- Virtualização de lista / infinite scroll / paginação de página — volume
  real atual (dezenas) não justifica a complexidade, e o produto já proíbe
  paginação e rolagem infinita explicitamente.
- Alargar `.wrap` para o board — o gargalo é altura, não largura; alargar
  quebraria a consistência de todas as páginas do site sem necessidade.
- Corrigir a truncagem por `title` (mouse-only) para um widget acessível —
  registrado em `spec.md` §Out of scope, ciclo futuro.
- Container queries como base — citado como enhancement futuro opcional,
  não dependência da correção.
- Repensar se "para você" deveria cobrir `para:"todos"` — pergunta de
  modelo de dados/regra de negócio, não de layout; registrada para o
  `principal`/autor decidir fora deste ciclo.

## Verification (DoD)

Ver `qa-report.md`: cada AC de `spec.md` com comando Playwright, esperado e
resultado real; screenshots antes/depois; tails de revisão independente e
segurança.
