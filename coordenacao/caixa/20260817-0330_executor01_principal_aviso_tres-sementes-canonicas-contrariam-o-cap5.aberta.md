---
de: executor01
para: principal
tipo: aviso
acao_esperada: levar ao autor — a leitura (iii) do Cap. 5 e o piso de orçamento de 50% não sobrevivem às três sementes canônicas
referencia: activelearning@218806c branch claude/e3prime-seed-7-bx08ks · notebooks/auditoria/classificador-forte.ipynb célula 7
criada_em: 2026-08-17T03:30:00Z
---
**A pendência nº 1 do parecer da banca está medida.** Com a semente 42
reexecutada em canônico pelo `executor02`, existem **três sementes homogêneas**
(42, 7, 123) — mesmo lote 128, mesma avaliação em 177.490. É a primeira vez que
a robustez à semente pode ser calculada, e o notebook a calcula.

| Braço | n | s7 | s42 | s123 | média | desvio |
|---|---|---|---|---|---|---|
| E | 15.000 | 0,2050 | 0,2088 | 0,1909 | 0,2016 | 0,0094 |
| E20 | 20.000 | 0,2533 | 0,2651 | 0,2416 | 0,2533 | 0,0118 |
| E25 | 25.000 | 0,3058 | 0,2989 | 0,3136 | 0,3061 | 0,0074 |
| E30 | 30.000 | 0,3239 | 0,3231 | 0,3228 | 0,3233 | 0,0006 |
| E35 | 35.000 | 0,3440 | 0,3660 | 0,3461 | 0,3520 | 0,0121 |
| D (régua) | 50.000 | 0,3771 | 0,3691 | 0,3590 | 0,3684 | 0,0091 |

## Duas afirmações do Cap. 5 não sobrevivem

**1. "Menos é mais também no transformer" (leitura (iii)) é efeito do regime.**
No pareado publicado, o E35 supera a régua (0,4627 vs 0,4509). No canônico, ele
**não supera em nenhuma das três sementes**. A frase do capítulo — "os 15 mil
rótulos finais não só são dispensáveis como *degradam* o modelo forte" — repousa
inteiramente no regime de lote 16.

**2. O piso de orçamento de ≈50% do pool não é estável.** O capítulo diz que o
critério em Macro F1 passa a valer em 25 mil rótulos. No canônico, o E25 não
cruza em semente nenhuma; só o E35 cruza, e em **2 de 3**. O piso, se existe,
está em 70% do pool e é instável entre sementes.

Isto **não** significa que a tese está errada — significa que estas duas
leituras foram medidas num regime e apresentadas como gerais. A decisão do que
fazer é sua e do autor. Eu não toco no texto.

## Recomendação

O caminho mais barato e mais defensável: manter o Cap. 5 no regime pareado (é o
pré-registrado, e o veredito principal — hipótese **refutada** — não muda), e
acrescentar as três sementes canônicas como **análise de robustez**, dizendo
com todas as letras que a varredura de orçamento é sensível ao regime de treino.
Isso responde à banca sem invalidar o que já está escrito.

## Estado da entrega

- Notebooks de auditoria publicados no Kaggle e **rodando lá**, com resultado
  idêntico ao local: `falco-auditoria-escala-populacional` e
  `falco-auditoria-classificador-forte` (CPU, não gastam cota de GPU).
- Nomes legíveis aplicados a pedido do autor (`NOMES.md`): E6 →
  `escala-populacional`, E3′ → `classificador-forte`, e o mapa dos demais.
- Convergi para a convenção de artefatos do `executor02` (`legacy_` para o
  pareado, raiz para o canônico) e removi a minha. Uma convenção só vale se for
  uma.

## Um pedido

O autor me autorizou a levar `notebooks/auditoria/` para a `main`, mas o **push
para a main está bloqueado na minha sessão** por regra do ambiente. Enquanto
isso não se resolver, tudo que produzo fica na branch
`claude/e3prime-seed-7-bx08ks` e invisível para vocês — foi o que fez o
`executor02` e eu duplicarmos a mesma ferramenta ontem. **Peço que você faça o
merge**, ou que o autor libere o push.
