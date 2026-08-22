---
de: revisor2
para: principal
tipo: aviso
acao_esperada: LEVAR AO AUTOR — achei DOIS valores errados na coluna "Inválidos" da Tabela~\ref{tab:e0-principal} (Cap.5). Não é arredondamento: as outras dez células da mesma coluna batem exatamente com o artefato. Uma delas contradiz a prosa da própria tese duas páginas adiante. Correção pronta, duas células
referencia: 5-resultados-falco/texto.tex tab:e0-principal (l.28-56) e RQ3 (l.127) · experiments/e0/results/e0_table.json e ANALISE_ERROS.md na MAIN do activelearning · continua a auditoria dos avisos 0744 e 0755
criada_em: 2026-08-22T08:07:00Z
---

# O achado

Na coluna **Inválidos** da `tab:e0-principal`, duas células não correspondem
ao artefato:

| linha | tese diz | artefato (`e0_table.json`) | correção |
|---|---|---|---|
| glm-5.2, **S-rand** | 0,0\% | `invalid_label_rate` = 0,0070 | **0,7\%** |
| deepseek-v4-pro, **S-strat** | 0,0\% | `invalid_label_rate` = 0,0021 | **0,2\%** |

**As outras dez células da mesma coluna batem na casa publicada** (flash
0,7 e 0,9; nemotron 1,2 e 2,6; v4-pro S-rand 0,1; os quatro zeros do gpt-4o
e do gpt-4o-mini; glm S-strat 0). Isso é o que descarta convenção de
arredondamento ou definição diferente de "inválido": a coluna segue
fielmente `taxa × 100` com uma casa em dez de doze lugares. Nesses dois, não.

# Por que o segundo é mais do que cosmético

A tese **conta esses inválidos duas páginas adiante**. Na RQ3 (l.127), sobre
os erros do v4-pro na S-strat: *"$\approx 2\%$ envolvem `_rare_` ou rótulo
inválido"*. E o artefato de análise de erro (`ANALISE_ERROS.md`) detalha:
*"Rótulo inválido (fora do schema) — ~1% — **4 casos em 1.863**"*.

Ou seja: a tabela declara **zero** inválidos para exatamente o oráculo e a
amostra em que a prosa, logo depois, **conta quatro**. Um leitor atento — e
banca é isso — encontra a contradição sem sair do capítulo. Com 0,2\% na
célula, os dois trechos passam a dizer a mesma coisa (0,0021 × 1.863 =
3,91 $\to$ 4 casos).

O caso do glm-5.2 é mais simples: parece transcrição. Vale notar que 0,7\% é
exatamente o valor da linha do flash, logo acima na mesma amostra — o tipo de
vizinhança que produz esse erro.

# Uma segunda coisa, menor, que é de precisão e não de erro

Na RQ2 (l.117): *"o nemotron \ldots\ empata com o deepseek-v4-flash na
S-rand ($p=0{,}76$) e com o glm-5.2 na S-strat ($p=0{,}078$), ficando abaixo
**apenas** do v4-pro ($p<0{,}001$)"*.

Os três números batem exatamente (0,764177 · 0,077729 · 0,000107). O
"apenas", porém, depende do limiar que se lê:

| comparação com o nemotron | S-rand | S-strat |
|---|---|---|
| v4-pro | 0,000107 | 0,000055 |
| gpt-4o | **0,0034** | **0,0015** |
| deepseek-v4-flash | 0,76 | **0,0048** |

Ao limiar que a própria frase enuncia ($p<0{,}001$), o "apenas" está
**correto** nas duas amostras. Ao limiar convencional de $0{,}05$, o nemotron
também fica significativamente abaixo do gpt-4o nas duas, e do flash na
S-strat. Não é erro; é uma frase que fica frágil se alguém abrir o artefato
com $\alpha=0{,}05$ na cabeça. Bastaria explicitar: *"o único a superá-lo com
$p<0{,}001$"*.

# O que conferi nesta rodada e bate

Para o achado não parecer maior do que é, o resto das seções RQ2–RQ4 está
verificado contra artefato:

- **`tab:e0-custo`** — 15 valores (custo, cache, acurácia dos 6 oráculos):
  todos exatos, inclusive o gpt-4o-mini pago (0,0507 $\to$ 0,051) separado da
  variante gratuita.
- **"26 vezes mais barato"** — 0,9229 / 0,0350 = **26,4**. Confere.
- **"cache atinge 88--95\%"** — conferi nas DUAS amostras antes de julgar: o
  mínimo é 0,883 (gpt-4o, S-rand) e o máximo 0,9475 (gpt-4o-mini, S-strat).
  A faixa está certa; se eu tivesse olhado só a S-rand teria acusado o 95\%
  indevidamente.
- **"$p<0{,}001$ no subconjunto pareado de 850 itens"** (o mesmo modelo
  servido por dois provedores diverge de si mesmo) — existe no artefato,
  com `n_paired` = 850. Confere.
- **"os 324 erros do melhor oráculo"** — 1.863 × (1 − 0,8261) = **324,0**.
- **O perfil de erro (31\% / 17\% / 7\% / $\approx$2\%)** — bate linha por
  linha com o `ANALISE_ERROS.md`. O "$\approx$2\%" é a soma de duas linhas do
  artefato (`_rare_` 1\% + inválido ~1\%); quase o acusei de errado por ter
  lido só a primeira.
- **RQ4** — 61,3\% (enum) contra 60,5\% (free) e inválidos 0,0\% contra
  6,8\%: os quatro exatos.

**Ainda não rastreado** neste capítulo: a `tab:e0p` (ablação de prompt) e as
duas verificações de instrumentação (ruído do gabarito; calibração de lote,
o $p=0{,}58$). Ficam para o próximo ciclo vazio.

**Meu limite, sempre:** sem LaTeX neste contêiner — nada disto olha a página
composta. Não editei capítulo nenhum.
