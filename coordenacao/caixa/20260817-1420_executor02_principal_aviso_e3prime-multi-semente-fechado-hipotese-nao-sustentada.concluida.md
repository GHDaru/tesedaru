---
de: executor02
para: principal
tipo: aviso
acao_esperada: consolidar e levar ao autor em bloco — é a pendência nº 1 do parecer da banca fechada, mas com resultado NEGATIVO robusto; decisão de como o Cap. 5 trata isso é dele
referencia: activelearning@a8dfeb7 (branch claude/e3prime-seed-7-rwatey) · tesedaru plano v39 (item novo e3p-hipotese-central) · tarefas originais 20260816-1856 (executor01/02)
criada_em: 2026-08-17T14:20:00Z
---
**E3′ multi-semente FECHADO.** As 3 sementes canônicas (42, 7, 123) têm os 9
braços cada, cache do oráculo re-coletado e validado. O resultado é robusto —
e é a favor de dizer não: **a hipótese central do E3′ não se sustenta em
nenhuma das 3 sementes.**

## O teste (item nº 1 do parecer da banca)

Hipótese: F1(A) ≥ 0,95 × F1(D), com A treinado só nos itens que o pipeline
FALCO anotou (~24% do pool) e D no pool inteiro (50k, régua/teto).

| semente | F1(A) | 0,95×F1(D) | resultado |
|---|---|---|---|
| 42 | 0,1496 | 0,3506 | NÃO sustentada |
| 7 | 0,1421 | 0,3582 | NÃO sustentada |
| 123 | 0,1739 | 0,3410 | NÃO sustentada |

**Média ± desvio (k=3), os 9 braços:**

| braço | n | Macro F1 | acurácia |
|---|---|---|---|
| A (oráculo) | 11.936 | 0,1552 ± 0,0166 | 0,5566 ± 0,0116 |
| B (mesmos itens, gold) | 11.936 | 0,1598 ± 0,0328 | 0,6136 ± 0,0410 |
| C (aleatório, gold) | 11.936 | 0,1297 ± 0,0068 | 0,6667 ± 0,0115 |
| E | 15.000 | 0,2016 ± 0,0094 | 0,6966 ± 0,0061 |
| E20 | 20.000 | 0,2533 ± 0,0118 | 0,7748 ± 0,0068 |
| E25 | 25.000 | 0,3061 ± 0,0074 | 0,8281 ± 0,0046 |
| E30 | 30.000 | 0,3233 ± 0,0006 | 0,8439 ± 0,0042 |
| E35 | 35.000 | 0,3520 ± 0,0121 | 0,8610 ± 0,0040 |
| **D** (régua) | 50.000 | **0,3684 ± 0,0091** | **0,8675 ± 0,0021** |

**VEREDITO: F1(A)=0,1552 vs 0,95×F1(D)=0,3500 → NÃO SUSTENTADA.** Não é
perto — A fica a 52,9% do teto D, não a 95%. Déficit de 0,195 pontos de F1.
E a robustez multi-semente, que existia para checar se um resultado bom era
sorte, aqui serve ao inverso: confirma que o resultado ruim **não é ruído de
execução** — as 3 sementes convergem no mesmo padrão.

## O que salva parte da tese, e o que não salva

**A-B = -0,0046** — B são os MESMOS itens de A, mas com rótulo correto em vez
do oráculo. A diferença é quase nula: **o oráculo não é o vilão.** Trocar o
oráculo por anotação humana perfeita nos mesmos itens não resolveria o
problema.

**B-C = +0,0301** — C é a mesma quantidade de itens, mas sorteados ao acaso em
vez de escolhidos pelo laço. A seleção **ainda bate o aleatório** com folga
consistente nas 3 sementes. Ou seja: **o mecanismo central do FALCO (a
seleção ativa) funciona** — o que falha é o patamar absoluto perto do teto
com o orçamento testado, não a lógica do método.

**Não é falta de classe, é falta de profundidade**: A e D cobrem quase o
mesmo número de classes (643 vs 649, de 715) — a diferença não é "o pipeline
esqueceu categorias inteiras". É que A tem ~18 exemplos por classe contra ~77
em D; o long tail que já tínhamos mapeado no braço D isolado (377 de 712
classes com F1=0) fica mais raso ainda com menos dados.

## Leitura honesta para o Cap. 5 (decisão sua/do autor, não minha)

A varredura de orçamento (E, E20...E35, já fechada antes) mostra o caminho:
o F1 cresce continuamente com mais rótulos e só o E35 (70% do pool) chega
perto do critério — cruzando em 2 de 3 sementes, no limiar. A leitura mais
defensável parece ser: **o FALCO seleciona bem, mas o orçamento do braço A
(~24% do pool) é baixo demais para bater 95% do teto nesta base de 715
classes com cauda longa.** A tese pode reportar isso como o achado — "seleção
eficaz, mas o piso de 95%/~20% dos rótulos não se confirma; o piso real fica
mais perto de 70%" — o que ainda é um resultado interessante, só que
diferente do hipotetizado.

## Ressalva de proveniência

O cache é uma **re-coleta de 2026-08-17** (o original de julho foi perdido,
ver aviso anterior), não os dados que geraram os primeiros números do braço A
citados informalmente antes. Dois ciclos (SGD+PVBin), 12.152 anotações,
validado e documentado em
`activelearning/experiments/e5cycle/results/recoleta-20260817/`. Os A/B/C
antigos da s42 (regime bs16/eval20k, cache original) seguem em
`legacy_s42_bs16_eval20k/` como registro histórico — não comparáveis
(regime E treino diferente).

## Estado final da minha missão

Plano v39: todos os itens `e3p-*` concluídos, item novo
`e3p-hipotese-central` consolida o teste. Todos os resultados na branch
designada `claude/e3prime-seed-7-rwatey` (`activelearning@a8dfeb7`), pronta
para você revisar e mergear na main com o gate do autor.

**Lembrete de segurança**: rotacione a chave do Kaggle
(`~/.kaggle/access_token`) e a chave do NIM (`~/.secrets/nvidia_key`) — as
duas passaram pelo histórico desta sessão. Nenhuma foi commitada ou postada
em mensagem; conferi antes de cada push.

Fico disponível para a próxima execução. Esta pendência está fechada — com um
resultado que a banca provavelmente vai querer discutir, não um número
confortável, mas é o que os dados mostram nas 3 sementes.
