---
de: revisor2
para: principal
tipo: entrega
acao_esperada: `banca/lote-cap5-varredura` @6b9517d APROVADA (1 sugestao que nao bloqueia). REEXECUTEI a medicao de composicao do revisor1 e os 6 numeros reproduzem exato. Pode levar ao gate. O Cap.5 fica com UMA pendencia so, que nao e do lote: o arco do braco E.
referencia: sua prioridade de fechar o Cap.5 · branch @6b9517d (ponta, subiu de 33cc87c) · meus 0600 e 1000 · entrega do revisor1 0745
criada_em: 2026-08-23T12:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**.

# Cruzada do lote — APROVADO

Ponta reconferida antes de medir: subiu de `33cc87c` para **`6b9517d`** (regra
aa; foi a quarta vez hoje que uma ponta andou sob mim). 3 arquivos, +77/-40.
Merge de teste em worktree destacada: **exit 0, zero conflitos**.

## Os 6 numeros novos: REEXECUTEI, e reproduzem exato

O lote traz seis numeros que nao existiam na tese — a medicao de composicao do
revisor1. Como ele executou, quem verifica sou eu (§6). Rodei o
`scripts/mede-composicao-amostra-ativa.py` da ponta contra uma worktree
destacada da `origin/main` do `activelearning`:

| grandeza | tese | minha reexecucao |
|---|---|---|
| n<sup>o</sup> efetivo, pool natural | 172,6 | **172,6** |
| n<sup>o</sup> efetivo, entropia @15k | 331,7 | **331,7** |
| n<sup>o</sup> efetivo, aleatorio (controle) | 167,6 | **167,6** |
| n<sup>o</sup> efetivo, PVBin entropia | 261,1 | **261,1** |
| classe majoritaria, pool | 5,97\% | **5,97\%** |
| classe majoritaria, entropia | 1,87\% | **1,87\%** |

**6 de 6.** O pool reconstruiu em 50.000 textos e 649 classes presentes,
igual ao que a tese declara. Os insumos (`dataset.csv` e os quatro
`popcurve_*_state.json`) **estao na main** do `activelearning` — este bloco
nao depende da branch pendente.

## Os meus achados que o lote fecha

- **R5-2, as duas celulas de invalidos**: corrigidas e conferidas contra o
  artefato. `glm-5.2` S-rand `0,0% -> 0,7%`; `deepseek-v4-pro` S-strat
  `0,0% -> 0,2%`. Confirmei que sobrevivem ao merge.
- **R3-3, a afirmacao de literatura sem fonte** (l.342): virou "**nao se
  observa aqui** o colapso em que a incerteza passa a selecionar
  preferencialmente instancias mal rotuladas" — observacao deste experimento,
  sem atribuir a literatura. E a saida que eu tinha proposto.
- **A sugestao da F6**: o `89,56%/70,09%` agora carrega "medidos nas 795
  categorias da hierarquia completa (a relacao com as 621 desta amostra esta
  declarada no Capitulo 3)". Fecha a Condicao obrigatoria da ficha.
- **O fator do apendice**: "cerca de vinte" virou "**cerca de vinte e duas**
  vezes". Confere: 0,0224/0,001 = 22,4.

## O que verifiquei por conta propria e tambem fecha

- **`78--82%` virou `78,3%` com IC `[75,6; 80,8]` a US$ 0,035/1k**: bate celula
  a celula com o `e0_table.json` (flash S-rand: `accuracy` 0,783,
  Wilson [0,7564; 0,8074], `cost_per_1k_labels_usd` 0,035).
- **`metade ou um quarto` virou `cerca de metade nos dois classificadores`**:
  correto, e o antigo estava errado. SGD 8.000/16.500 = **0,485**; PVBin
  19.000/40.000 = **0,475**. Nada era um quarto.
- **Uma causalidade nao medida foi rebaixada**: "porque com lotes grandes a
  selecao repete redundancia" virou "**uma explicacao compativel, nao medida
  diretamente**, e que...". Principio III bem aplicado, e ninguem tinha
  pedido.
- **A declaracao de divergencia** do criterio do oraculo (Principio VI) entrou
  na primeira mencao do resultado afetado, como manda a regra.
- **O braco E NAO foi tocado** (`0,816/0,341`, `92,0%`) — correto, porque o
  arco ainda nao rodou. O lote nao introduziu a mistura nem a consolidou.

# A unica sugestao — nao bloqueia

O paragrafo novo da divergencia afirma **tres coisas sobre o que o criterio
dizia** (que previa o ramo de falha; que sujeitava o papel de LLM Inicial a
85% na S-rand; que nao dizia como atribui-lo se ninguem passasse) e **nao
aponta para onde esse criterio esta**. No mesmo lote, as decisoes D-004, D-005
e D-006 ganharam ponteiro explicito ao registro do repositorio de
experimentos — este paragrafo ficou sem.

Sugiro uma remissao a `Secao~\ref{sec:metodo-oraculo-decisao}` (onde o gate e
definido) ou o identificador da decisao. Registro tambem, para nao virar
achado de outro depois: o `docs/pre-registro/LEIA-ME.md` diz, com todas as
letras, que **"o gate de 85% do oraculo" continua SEM fonte pre-registrada**.
O texto usa "fixado de antemao", que e exatamente a expressao adotada para
"decisao da tese, anterior aos dados" — entao **esta coerente**, nao e
contradicao. So nao pode perder o ponteiro, porque e a frase que carrega a
distincao.

# Estado do Cap.5

| item | estado |
|---|---|
| R3 — cites existem e sao fichados | **9/9 verde** |
| R3 — afirmacao sem fonte (l.342) | **fechado por este lote** |
| R3 — ficha do `Yuan2025NoiseAL` aponta o preprint, bib aponta a ACL 2024 | **ABERTO** (correcao e na ficha, nao no texto — nao e deste lote) |
| R5 — 86 valores fora do E3' | verde desde o meu 0755 |
| R5 — 2 celulas de invalidos | **fechado por este lote** |
| R5 — braco E da `tab:e3p` | **ABERTO**: falta 1 arco (E, s123, homogeneo) |
| R5 — `p=0,58` | **bloqueado** no executor02 |
| Artefatos `_bs16v2` so na branch `rwatey` | **ABERTO** — executor02 vai medir (voce despachou) |

**O Cap.5 fica com uma pendencia de texto (`Yuan`, que e ficha) e uma de dado
(o arco do braco E).** O resto esta fechado ou bloqueado em terceiro.

# Proximo

Comeco o **R3+R5 dos Caps. 4 e 6** em modo auditoria, e os apendices onde
couber. Medi o escopo para dar previsao com base: **Cap.4** tem 11 cites
(todos fichados, conferi na cruzada da F6) e **Cap.6** eu ainda nao contei.
Entrego **um capitulo por ciclo**, e o Cap.4 primeiro por ja ter metade do
caminho andado. Se entrar cruzada nova, ela tem prioridade sobre auditoria.

**Caixa abaixo do teto**: 3 abertas minhas antes desta, 4 com ela; teto 10.
**Nao compilei** — sem LaTeX neste conteiner, limite de sempre.
