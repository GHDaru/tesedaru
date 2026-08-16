# QA Report 002 — Board kanban da Coordenação: caber na tela

- **Spec**: `spec.md` · **Plan**: `plan.md` · **Date**: 2026-08-16
- **Ferramenta**: Playwright/Chromium local, dados sintéticos (59-72
  mensagens, distribuição desequilibrada: 38 na coluna "Aberta") + dados
  reais do repositório.

## AC1 — altura de `.k-cards` não excede o teto

Comando: `page.locator('.k-cards').evaluateAll(els => els.map(el =>
el.getBoundingClientRect().height))` com 59 mensagens sintéticas (38/6/5).

**Resultado**: `[522, 522, 522]` px — as 3 colunas com a MESMA altura
(igual entre si, como decidido em `ux-design.md` §2), abaixo do teto de
640px (`clamp(320px,58vh,640px)` a 900px de altura de viewport). ✅ PASS

## AC2 — rolagem interna própria, página não escala com N

Comando: medir `scrollTop` de `.k-cards` antes/depois de
`el.scrollTop = 300`, e `document.body.scrollHeight`.

**Resultado**: `scrollTop` 0 → 300 (rolou de fato) · altura da página
1208px com 59 cartões sintéticos (comparável à altura da página com os
~11-26 dados reais — não proporcional a N, que era o defeito relatado).
✅ PASS

## AC3 — ordenação por prioridade no DOM

Comando: ler `className` dos 6 primeiros `.k-card` da coluna "Aberta"
(mistura de para-você/atrasado/comum nos dados sintéticos).

**Resultado**:
```
k-card para-voce atrasado
k-card para-voce
k-card para-voce
k-card para-voce
k-card atrasado
k-card atrasado
```
Ordem exata prevista em `ux-design.md` §4: `atrasado&&para-você` primeiro,
depois `para-você`, depois `atrasado`, depois recência. ✅ PASS

## AC4 — 0 erros de console, temas, breakpoints

- **Console**: 0 erros em todas as verificações (dados sintéticos e reais,
  claro e escuro, desktop/médio/mobile).
- **Breakpoint ≥1100px** (grid 3 colunas): screenshot confirma 3 colunas
  de mesma largura e altura — ver `shot-kanban-v2.png` (após correção do
  bug de overflow, ver "Achado durante o QA" abaixo).
- **Breakpoint 601-1099px** (950px testado): `getComputedStyle(#board)`
  → `display:flex; overflow-x:auto` — confirma o modo de rolagem
  horizontal em vez de colunas espremidas.
- **Breakpoint ≤600px** (500px testado): `grid-template-columns` retorna
  1 valor (`468px`, largura cheia) — confirma empilhamento; screenshot
  `shot-kanban-v2-mobile.png` confirma visualmente.
- **Tema escuro**: `shot-kanban-v2-dark.png` — cores corretas, badges
  âmbar e bordas mantêm contraste.
- **Regressão nas 4 páginas** (dados reais, não sintéticos): `index.html`,
  `plano.html`, `mensagens.html`, `resultados.html` — 0 erros de console
  em todas. ✅ PASS

## AC5 — acessibilidade mínima

Comando: contar `.k-col[role="region"]`, ler `aria-labelledby`,
`tabindex` de `.k-cards`, `aria-live` de `#board-status`; testar foco
programático.

**Resultado**: 3 regiões (`role="region"`) · `aria-labelledby="k-col-h-
aberta"` (aponta corretamente pro `id` do `h2` da coluna) · `tabindex="0"`
em `.k-cards` · `aria-live="polite"` em `#board-status` · elemento
focado após `.focus()` é de fato `.k-cards` (alcançável por teclado).
✅ PASS

## FR8 — estado vazio diferenciado

Teste: desligar todas as pílulas de tipo (zera as 3 colunas via filtro).

**Resultado**: as 3 colunas mostram "Nada aqui com os filtros atuais"
(não "Nada aqui" — que ficaria reservado para quando a coluna está
realmente vazia antes de qualquer filtro); `#board-status` anuncia
"Aberta: 0 · Em andamento: 0 · Concluída: 0". ✅ PASS

## Achado durante o QA (fora do escopo das 3 análises dos especialistas, corrigido antes de publicar)

O primeiro teste visual (`shot-kanban-v2.png`, primeira rodada) revelou um
bug real de layout não previsto por nenhum dos 3 especialistas: o texto
sem quebra de `.k-ref` (`white-space:nowrap`) tem um `min-content width`
igual ao texto inteiro sem quebrar; como nenhum elemento na cadeia
`.k-board → .k-col → .k-cards → .k-card` tinha `min-width:0` explícito, o
comportamento padrão (`min-width:auto`) de itens flex/grid propagou essa
largura mínima para cima, esticando a coluna e o board inteiro além da
largura pretendida — column comment lida como "1 coluna gigante" em vez de
3 colunas iguais. Clássico bug de overflow em flex/grid aninhado.

**Correção**: `grid-template-columns:repeat(3,minmax(0,1fr))` em
`.k-board` (em vez de `repeat(3,1fr)`) + `min-width:0` em `.k-col`,
`.k-cards` e `.k-card`. Reverificado com o mesmo dado sintético — AC1-AC5
voltaram a passar, agora com largura correta (ver screenshots
pré/pós-correção nas evidências abaixo).

## Evidências (screenshots)

- `shot-kanban-v2.png` (pós-correção) — desktop, claro, 59 cartões sintéticos,
  3 colunas iguais.
- `shot-kanban-v2-dark.png` — mesmo cenário, tema escuro.
- `shot-kanban-v2-mobile.png` — 390px, empilhado.

(Arquivos gerados durante a sessão em `/tmp/`, não versionados — evidência
descrita textualmente acima com os valores medidos.)

## Closing tail

- `TAIL:review` — ver seção abaixo (revisão independente em contexto
  fresco, agente `review`).
- `TAIL:security` — mudança é só CSS/JS de apresentação num script
  gerador estático (`build_coordenacao()`); sem entrada de usuário nova,
  sem rede, sem segredo tocado. Diff revisado manualmente: nenhuma
  interpolação de string insegura nova (todo texto de `mensagens.json`
  continua passando por `esc()` antes de entrar no HTML — inclusive o
  `title` do `.k-titulo`, adicionado neste ciclo). n/a como risco de
  segurança real; verificado por hábito.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).

---

## Revisão independente (TAIL:review)

_(preenchido após o agente `review` avaliar o diff em contexto fresco)_
