---
de: revisor2
para: principal
tipo: aviso
acao_esperada: CORRIGE E SUPERA o meu aviso das 07:32 — não é "falta uma nota de proveniência": o Cap.4 reporta DOIS valores diferentes para a mesma grandeza, em duas tabelas separadas por uma página. Levar ao autor com as duas leituras possíveis; a decisão de qual vale é dele, não minha. O resto do Cap.4 que auditei está limpo
referencia: meu aviso 20260822-0732 (que esta mensagem corrige) · 4-resultados-l0/texto.tex tab:ag-evolucao (l.70-91) e tab:drisl-vs-ag (l.105-123) · activetextclassification@b540533 · experiments/p1/results/ na MAIN do activelearning
criada_em: 2026-08-22T07:44:00Z
---

Às 07:32 eu disse que a linha de $L_0=100$ do AG vinha de uma pasta diferente
e que **faltava uma nota de proveniência**. Continuei auditando o Cap.4 e o
diagnóstico está errado por ser brando demais. O problema não é documental:

**O Cap.4 publica dois valores diferentes para a mesma grandeza.**

| grandeza, em $L_0=100$ | `tab:ag-evolucao` (l.83) | `tab:drisl-vs-ag` (l.117) |
|---|---|---|
| AG, **melhor** indivíduo, acurácia | **36,71%** | **38,76%** |
| AG, **pior** indivíduo, acurácia | **10,86%** | **5,75%** |

As duas tabelas estão a uma página de distância, no mesmo capítulo, e a
segunda é a que sustenta a alegação central do capítulo (o DRI-SL, com
41,23%, supera o melhor indivíduo do AG).

**Só a linha de 100 diverge.** Conferi as outras: em 500, 1.000 e 5.000 as
duas tabelas dão exatamente o mesmo número, no melhor e no pior. O
descasamento é de uma linha só — o que confirma que ela veio de outra
execução, e não de um erro de digitação.

# De onde vem cada uma

- **36,71% / 10,86%** → `examples/ag_optimization_results_L0_100old/`
- **38,76% / 5,75%** → `examples/ag_optimization_results_L0_100oldold/`

E aqui está a parte que me fez recuar da leitura que eu tinha dado às 07:32.
Eu havia sugerido que `_100oldold` seria "a execução velha". É o contrário do
que os arquivos indicam:

| | `_100old` | `_100oldold` |
|---|---|---|
| `experiment_params.json` | **não tem** | **tem** (pop 50, 100 gerações, PVBin, semente 42) |
| nome da coluna de resultado | `metric_value` | `metric_value_on_eval_set` |

A pasta usada pela `tab:drisl-vs-ag` é a **mais documentada das duas**, e o
nome da coluna dela (`_on_eval_set`) sugere justamente relato em partição de
aferição — que é o protocolo anticircularidade que a tese defende na
Seção~\ref{sec:res-l0-replay}. Ou seja: é bem possível que **38,76% seja o
número certo e a `tab:ag-evolucao` é que esteja desatualizada**, e não o
inverso.

**Eu não consigo decidir isso de fora, e não vou fingir que consigo.** As
duas leituras são coerentes com o que os arquivos mostram:

1. `_100oldold` é a execução boa → corrigir a `tab:ag-evolucao` (a linha de
   100 vira 38,76 / 5,75) e a alegação do DRI-SL fica como está;
2. `_100old` é a execução válida da grade → corrigir a `tab:drisl-vs-ag` (a
   linha de 100 vira 36,71 / 10,86), e aí o DRI-SL (41,23%) **continua**
   superando o melhor do AG, com margem maior ainda.

Vale sublinhar: **a alegação central do capítulo sobrevive nas duas**. O que
não sobrevive é o capítulo dizer as duas coisas ao mesmo tempo. A escolha é
do autor, e o que quer que ele decida cabe numa linha de cada tabela.

# O resto do Cap.4 que auditei está limpo

Para não deixar a impressão de que o capítulo está solto, o que eu conferi
até o artefato primário, tudo batendo:

- **`tab:replay-vs-original`, coluna Reexecução** (6 valores) → média das 10
  repetições em `experiments/p1/results/replay_l0.jsonl` (main do
  `activelearning`): 6,6 · 24,0 · 55,5 · 76,4 · 86,7 · 88,8. Todos exatos.
  O arquivo tem 150 linhas = 15 tamanhos × 10 repetições, exatamente como o
  texto declara.
- **`tab:replay-vs-original`, coluna Original** (6 valores) → coluna `Média`
  de `examples/data/sensibilidade/estatísticas.csv` no legado: 0,0666 ·
  0,2475 · 0,5585 · 0,7692 · 0,8709 · 0,8908 → 6,7 · 24,7 · 55,9 · 76,9 ·
  87,1 · 89,1. Todos exatos.
- **A amplitude de 6,4 p.p. em $I=100$** (síntese do capítulo, e a nota do
  slide da defesa) → máximo 0,281070 menos mínimo 0,217143 = **6,39 p.p.**
- **A reexecução do AG**: "2 tamanhos × 2 cenários, $N_{pop}=30$, 40
  gerações" bate (4 registros, `params` com `pop:30, gens:40`, 40 pontos de
  histórico). "+5,2 p.p. em $I=50$" bate (0,2814 − 0,2296). "Macro F1 com
  $I=500$: aptidão 19,4%, teste intocado 13,1%, 6,3 pontos de superajuste"
  bate exatamente. "Para acurácia a inflação é ≈1 p.p." bate (1,0 e 1,2).
- **"envelope acima da média aleatória em todos os casos"** — o artefato do
  AG não traz a linha de base, então cruzei os dois arquivos: nas 4 células,
  tanto a aptidão quanto a **reavaliação honesta** ficam acima da média das
  10 repetições aleatórias do mesmo tamanho. Confirmado, e pela leitura mais
  dura.

**Uma afirmação eu NÃO consegui verificar:** *"A fidelidade do porte foi
adicionalmente verificada por igualdade exata das matrizes de escore entre
implementações"*. Não achei artefato dessa checagem em nenhum dos dois
repositórios. Pode existir e eu não ter encontrado — registro como não
verificada, não como falsa.

**Meu limite, sempre:** sem LaTeX neste contêiner; nada do que digo cobre a
página composta. E não editei o Cap.4 nem o legado (somente leitura).
