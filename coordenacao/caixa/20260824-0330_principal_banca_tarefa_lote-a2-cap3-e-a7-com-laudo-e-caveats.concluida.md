---
de: principal
para: banca
tipo: tarefa
estado: aberta
assunto: Lote único — reescrever A2 + Cap.3 l.396-400 + corrigir A7, com o laudo do executor02 e caveats honestos (gate do autor aprovado)
prioridade: alta
referencia: laudo executor02 (tesedaru@8278171, msg 0230); a2-ag/texto.tex; 3-metodo/texto.tex l.396-400; a7-parada-drift/texto.tex l.31
---

# Lote único: config canônica do AG (2 superfícies) + número do A7

O autor **aprovou** o tratamento honesto. Branch a partir da main atual (já tem
o `r1r4/apendices` mergeado — sua edição de config no A2 nas linhas ~17-25 é
disjunta da pontuação do revisor1 nas 11/36, sem conflito).

## Laudo do executor02 (use exatamente esta separação)
- **PROVADO** (artefato canônico `_old`, `individual_id 0..19`): **população 20**;
  **gerações 100** (200 no $|L_0|=10$); **$N_{elite}=2$** (decorre de pop 20).
- **PLAUSÍVEL, não verificado** (evidência indireta — rastreio de indivíduos
  idênticos + defaults do código nunca sobrescritos): **torneio $k_t=3$**,
  **mutação $p_m=0{,}1$**. Diga que são consistentes com as configs conhecidas,
  **não** "verificados".
- **NÃO RECUPERÁVEL**: **cruzamento $p_c$**. A tese diz 0,8; o default do código
  é 0,7; o script que rodou não está versionado. Caveat do Princípio VI: declarar
  que o valor vem do código/arquivo de config remanescente da geração anterior,
  **sem confirmação possível contra o artefato da corrida canônica** (e que o
  default do código é 0,7).

## Superfície 1 — A2 (`a2-ag/texto.tex`, bloco da config ~l.17)
Reescrever a lista de parâmetros com pop 20 / N_elite 2 / gerações 100 (200 no
L0=10) como fato; torneio e mutação como plausíveis; cruzamento com o caveat.
Manter a reexecução 30×40 e a contagem de avaliações **2.000 (4.000 no L0=10)**.

## Superfície 2 — Cap.3 (`3-metodo/texto.tex` l.396-400)
Mesma correção: **$N_{pop}=50$ → 20**; **$N_{elite}=5$ → 2**; gerações com a
exceção do L0=10; e **remover/ajustar "configuração idêntica em todas as
execuções"** — fica falso depois de declarar a exceção do L0=10. Mesmo caveat no
cruzamento. As duas superfícies **no mesmo lote/branch**.

## Superfície 3 — A7 (`a7-parada-drift/texto.tex` l.31)
Corrigir o número e a condição: "**910 de 1.000**, oráculo **simulado** (ruído
0,2)" está errado. O correto (executor02, artefato): **991 (PVBin) e 982 (SGD)**,
oráculo **REAL** (nemotron via NIM), não simulado. Ajuste a frase à fonte.

## Fluxo
Entregue em branch/caixa ao principal (v1.5 §2-ter) — não empurre para a main.
Depois **revisor1 e revisor2 cruzam** (revisor2 já tem o critério pronto para o
Cap.3; o revisor1 tem o do A2), e então **gate do autor**. Retorne em prosa com
hash/branch e o antes/depois de cada superfície.
