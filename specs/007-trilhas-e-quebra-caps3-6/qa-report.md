# QA Report 007 — Trilhas na fila do Controle + quebra por tema nos Caps. 3-6

- **Lane**: light — aviso do `principal` (`20260817-0215`) já
  completamente especificado; `ux-design.md` deste ciclo cobre o porquê
  das decisões e os dois bugs de dado reais encontrados no caminho.

## Verificação de dados

- **Controle — fila por trilha**: 16 itens agrupados em Texto (4),
  Experimentos (2), Processo (1), Geral (9) — soma bate com o total.
  Confirmado contra `kpis.json` fresco (`fila_autor.itens[].trilha`).
- **Gap fechado**: item de execução `fix-cap2-prosa-619-648` (`estado:
  gate`, sem `trilha`) agora aparece em "Geral" — antes desta rodada não
  aparecia em `fila_autor` de jeito nenhum (confirmado comparando o
  `kpis.json` antes/depois da mudança em `compute-kpis.py`).
- **Plano — quebra por tema**: 5 capítulos com `quebra` renderizados
  (Cap.2 a Cap.6), 33 `tema-card` no total (5 do Cap.2 + 28 dos novos).
  `Math.round` do progresso por capítulo calculado corretamente (0% para
  os 4 capítulos novos, todos os temas em `aberto`).
- **0 ocorrências de "undefined"** em `.tema-dim` após o fallback
  `citacoes ?? citacoes_chaves` (checado nos 33 cards, não só amostra).
- **Nota por tema**: pill do tema `c2.t2` carrega `title` com o texto
  completo da nota (recontagem de 41 chaves, bloqueio do Deng2023fedal
  etc.) e classe `.has-note` — mesmo padrão já usado na matriz principal.

## Verificação visual (Playwright/Chromium, dados reais)

- **0 erros de console reais** nas 7 páginas (só o 404 de favicon já
  investigado em ciclos anteriores).
- **Responsável "a definir"**: pontinho oco (contorno, sem preenchimento)
  + texto em itálico opacidade reduzida, confirmado nos 28 temas novos —
  nunca invisível.
- **Claro/escuro**: Controle (fila por trilha) e Plano (quebra Caps.3-6)
  verificados nos dois temas, sem regressão.
- **Mobile (390×844)**: `scrollWidth <= clientWidth` confirmado em
  Controle e Plano — sem rolagem horizontal do body.
- **Regressão**: as outras 5 páginas seguem com 0 erros de console; a
  mudança em `compute-kpis.py` ficou contida em `fila_e_represados()`
  (só adiciona `trilha` aos itens já existentes + um novo caso para
  execuções em gate — não altera o cálculo de pontos/represados).

## Fora de escopo, registrado para o principal

O campo `citacoes_chaves` (Caps.3-6) vs. `citacoes` (Cap.2) é uma
divergência de nome no próprio `plano-revisao.json`, não algo que o site
deveria decidir sozinho — tratei com fallback defensivo no renderizador
(nunca quebra a tela), mas a unificação do nome do campo na fonte é uma
decisão de quem mantém o plano, não do site.

## Closing tail

- `TAIL:review` — n/a nesta rodada: lane light, mudança aditiva (campo
  `trilha` propagado + fallback de nome de campo + estilo para valor não
  catalogado), sem alterar o cálculo de pontos/represados nem o
  comportamento de nenhuma outra página; verificação própria com
  evidência acima substitui a revisão formal em contexto fresco.
- `TAIL:security` — nenhuma superfície nova de rede ou entrada externa;
  todo texto (`nota`, `titulo`, `responsavel`) passa por `esc()` antes de
  entrar no HTML. n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
