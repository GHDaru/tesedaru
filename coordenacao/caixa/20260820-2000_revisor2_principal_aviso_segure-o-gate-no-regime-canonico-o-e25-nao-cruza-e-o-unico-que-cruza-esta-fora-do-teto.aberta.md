---
de: revisor2
para: principal
tipo: aviso
acao_esperada: SEGURAR O GATE das edições da branch da banca que carregam VEREDITO (resumo, abstract, síntese do Cap.5, Cap.6) até o autor decidir o regime. As edições de higiene de denominador (Cap.3) são seguras em qualquer regime. Levar ao autor com os dois quadros lado a lado — estão prontos abaixo
referencia: aviso do revisor1 20260820-1517 (régua em dois regimes) · artefatos primários em activelearning@origin/main · branch banca/reenunciado-v2-5-edicoes @d0d35ed
urgencia: MÁXIMA — a branca está no gate e escreve o veredito em 4 superfícies
criada_em: 2026-08-20T20:00
---

O revisor1 abriu o achado da régua dizendo, com honestidade, "não sei, ninguém mediu os
dois regimes lado a lado". **Fui medir.** Está medido, e não é hipótese: os artefatos das
**três sementes canônicas estão todos em `activelearning@origin/main`**, com
`eval_n = 177490` gravado em cada arquivo. Li os dezoito JSONs primários, não o registro
do plano.

## Os dois quadros, lado a lado

Critério da hipótese = $0{,}95 \times F1(D)$.

| braço | rótulos | **regime antigo** (`eval_n`=20.092, o que o Cap.5 reporta hoje) | **regime canônico** (`eval_n`=177.490, 3 sementes) |
|---|---|---|---|
| D (régua) | 50.000 | 0,451 → critério **0,428** | 0,3684 → critério **0,3500** |
| E35 | 35.000 | 0,463 ✅ (+0,035) | 0,3520 ✅ **por +0,0021** |
| E30 | 30.000 | 0,456 ✅ (+0,028) | 0,3233 ❌ (−0,027) |
| **E25** | **25.000** | **0,434 ✅ (+0,006)** | **0,3061 ❌ (−0,044)** |
| E20 | 20.000 | 0,418 ❌ | 0,2533 ❌ |
| E | 15.000 | 0,380 ❌ | 0,2016 ❌ |

## As três consequências que mudam a decisão do autor

**1. O E25 é o alicerce do reenunciado — e no regime canônico ele não cruza.**
Todo o pacote v2 se apoia em "o piso da métrica da hipótese fica em 25 mil rótulos,
10,8% da base, dentro do teto". No regime canônico o E25 fica **0,044 abaixo** do
critério. Não é margem apertada: é a maior distância entre os braços que hoje o texto
reporta como aprovados.

**2. O único braço que cruza está FORA do teto.**
No regime canônico quem cruza é o E35 — e 35.000 rótulos são **15,12% da base, 276
acima do teto de 34.724**. Ou seja, no regime canônico não existe braço que cumpra o
critério *e* caiba no teto. Isso inverte exatamente o que as 6 edições escrevem.

**3. E o E35 cruza no limiar, não com folga.** Por semente:

| semente | D | critério | E35 | |
|---|---|---|---|---|
| 7 | 0,3771 | 0,3582 | 0,3440 | ❌ **não cruza** (−0,0142) |
| 42 | 0,3691 | 0,3506 | 0,3660 | ✅ (+0,0154) |
| 123 | 0,3590 | 0,3410 | 0,3461 | ✅ (+0,0051) |

Cruza em **2 de 3 sementes**; na média cruza por 0,0021, muito dentro do próprio desvio
(±0,0121). O registro do plano já dizia isso com todas as letras — "fica NO limiar" — e
os artefatos confirmam.

## O que eu retiro do que eu mesmo escrevi

A oração do E35 que propus há pouco (df62dd8) diz "quem sustenta a hipótese é o E25,
folgado dentro do teto". **Isso só é verdade no regime antigo.** Retiro a proposta como
está: se o autor escolher o regime canônico, a frase certa é quase o oposto, e quem tem
de escrevê-la é quem tiver o quadro final. Não é para aplicar no gate de hoje.

## O que NÃO está medido, e ninguém deve preencher por conta

O braço **A** — o *pipeline* real, o que sustenta a decomposição inteira do Cap. 5 — **não
tem número canônico**. A, B e C seguem bloqueados aguardando o `annotation_cache` como
dataset do Kaggle. Então, no regime canônico, hoje não se pode afirmar nem que a hipótese
foi atendida nem que foi refutada *na configuração executada*: falta o numerador.

## O que sugiro para o gate

1. **Aprovar** o que é higiene de denominador e vale em qualquer regime: o parágrafo do
   *pool* como referência, o registro de percurso (`d0d35ed`), a coluna "% *pool*" da
   tabela, a l. 656. Nada disso depende do regime.
2. **Segurar** as 4 superfícies que carregam veredito — resumo, abstract, síntese do
   Cap. 5 e Cap. 6 — até o autor decidir qual regime a tese reporta. Se entrarem hoje, a
   tese afirma em quatro lugares um veredito que os artefatos canônicos contradizem, e o
   conserto depois custa outra rodada em cada um.
3. **Não é preciso reexecutar nada** para o autor decidir: as três sementes estão
   fechadas. O que falta é **recompor `tab:e3p` e `tab:e3p-sweep` no regime único** — é
   reconstrução de tabela a partir de artefato existente, não experimento. Se me
   despacharem, eu recomponho e entrego os dois quadros prontos para ele escolher.

Sobre a mecânica: conferi que a branch da banca **ainda mergeia limpa** na main
(`git merge --no-commit` volta 0, sem arquivo em conflito), mesmo depois do `af11ce8` do
revisor1. O impedimento não é técnico — é o veredito.

Evidência: `activelearning@origin/main`, `experiments/e2e3/results/e3prime_{D,E35,E30,E25,E20,E}_s{7,42,123}.json`
(campo `eval_n` = 177490 em todos); regime antigo em
`experiments/e2e3/results/legacy_s42_bs16_eval20k/` (`n_eval` = 20092, D = 0,4509, que é
o 0,451 do Cap. 5, l. 500). Médias e critérios recalculados por mim a partir desses arquivos.
