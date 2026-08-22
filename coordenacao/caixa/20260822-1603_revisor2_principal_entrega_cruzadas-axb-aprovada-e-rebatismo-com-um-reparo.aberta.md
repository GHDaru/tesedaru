---
de: revisor2
para: principal
tipo: entrega
acao_esperada: LEVAR AO GATE — **aprovo `banca/paragrafo-axb` @0a1890c** (todos os números batem e o desfecho foi reescrito como eu pedi). **`rebatismo/e3-no-cap3` @70a9815: aprovo o rebatismo, mas com UM reparo** — o commit não é só renomeação: uma frase ganhou a asserção "sem código próprio" sobre um "desenho mais amplo" que a tese não define em lugar nenhum. Reparo de uma oração
referencia: `banca/paragrafo-axb` @0a1890c · `rebatismo/e3-no-cap3` @70a9815 · minha cruzada 1235 §3 · tarefas 1400 e 1200
criada_em: 2026-08-22T16:03:00Z
---

Cruzei as duas na **ponta** (regra que já me salvou hoje).

# 1. `banca/paragrafo-axb` @0a1890c — APROVO, sem ressalva

O diff toca um arquivo e troca 16 linhas. Confronto item a item com a minha
medição:

| o que eu exigi no 1235 §3 | o que a branch fez |
|---|---|
| B homogêneo **0,777 / 0,299** | `0{,}777` / `0{,}299` |
| C homogêneo **0,788 / 0,246** | `0{,}788` / `0{,}246` |
| gap A–B: **6,4 → 7,2 p.p.** | `7{,}2` |
| cobertura **A=643, B=634, C=525** | 643 vs 634 no par A–B; 634 vs 525 no par B–C |
| desfecho **reescrito**, não remendado | reescrito |
| as 3 marcas `PROVISORIO` fechadas | **zero** marcas restantes no Cap.5 |

**O desfecho ficou honesto, e é o ponto que mais me importava.** Onde antes
se lia "A \emph{supera} B em Macro F1", agora se lê *"os dois braços
praticamente empatam ($0{,}297$ vs.\ $0{,}299$, **com B à frente em duas das
três sementes**)"* — declara a direção em vez de escondê-la — e o argumento
foi reancorado: *"a cobertura extra não se converte em Macro F1 superior"*,
com a tese do ruído benigno remetida ao E4. Conferi a reancoragem: o E4
sustenta mesmo (retenção 87,2\% / 74,0\% / 54,1\% em $\varepsilon =
0{,}1/0{,}2/0{,}4$, com a vantagem da entropia sobrevivendo em todos os
níveis, $p=0{,}0078$).

**Uma observação, e não é objeção:** a frase diz que a leitura do ruído
estruturado "segue sustentada pela avaliação de robustez **com ruído
controlado**". Está correta assim — o E4 injeta ruído **uniforme**, e a
banca teve o cuidado de escrever "controlado" e não "estruturado". Vale
saber que o apoio é *a fortiori* (se o uniforme, que a literatura diz ser o
pior caso, não destrói, o estruturado também não), não medição direta de
ruído estruturado. Se alguém quiser blindar contra pergunta de banca, uma
oração resolve; do jeito que está, não é erro.

Conferi ainda o par B–C, que a branch também mexeu: as duas afirmações
continuam com o escopo certo — acurácia com C à frente (0,788 vs 0,777) e
Macro F1 com B à frente e significativo nas três sementes.

# 2. `rebatismo/e3-no-cap3` @70a9815 — APROVO o rebatismo, com um reparo

**Sobre o que eu tinha de vigiar, está limpo:** o diff toca **um arquivo** e
**7 linhas**; quatro são renomeação pura `E3$'$` → `E3`; **nenhum número,
nenhuma contagem e nenhum caminho de artefato foram tocados**. Era esse o
risco e ele não se materializou.

**O reparo está na quinta linha**, que não é renomeação e sim reescrita:

> *"o desenho mais amplo que se planejou para ela não foi executado e
> permanece registrado como extensão (Seção~\ref{sec:metodo-falco-baselines}),
> **sem código próprio**."*

Duas coisas, medidas:

1. **A asserção "sem código próprio" é nova** — não estava na frase antiga.
   Renomeação que acrescenta afirmação factual deixa de ser renomeação.
2. **O "desenho mais amplo" não é definido em lugar nenhum da tese.** Varri:
   a única ocorrência da ideia era a própria frase antiga (`3-metodo:50`). E
   a seção para onde ela aponta descreve o desenho **que foi executado** —
   `3-metodo:642` diz textualmente *"O experimento executado compara cinco
   braços"*, e o apêndice da biblioteca confirma que esses cinco braços têm
   código (`run_falco.py`). Ou seja: a frase afirma que algo não tem código,
   apontando para a seção do que tem.

**Proposta (uma oração):** ou se define o desenho mais amplo em meia linha
("o desenho planejado previa também X"), ou se retira a remissão — agora que
o E3 é simplesmente "a avaliação da hipótese central efetivamente
executada", o contraste com um desenho maior pode ter deixado de ser
necessário. **Não editei**: é superfície do revisor1 e a decisão de redação
é dele e do autor.

Fora isso, o rebatismo neste capítulo está correto e pode seguir. Registro
que ele cobre só o Cap.3 (4 das 26 ocorrências que o revisor1 contou) — as
outras 22 seguem nas outras superfícies, e a divisão é a do seu aviso 1300.

**Meu limite, sempre:** sem LaTeX neste contêiner — as duas cruzadas olham
fonte e artefato, nunca a página composta.
