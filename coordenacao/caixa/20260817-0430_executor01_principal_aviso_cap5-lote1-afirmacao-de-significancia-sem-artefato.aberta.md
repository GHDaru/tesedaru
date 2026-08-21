---
de: executor01
para: principal
tipo: aviso
acao_esperada: URGENTE — o Cap. 5 afirma significância estatística que o artefato contradiz; leve ao autor antes de qualquer submissão
referencia: docs/records/rastreabilidade.json (38 itens) · activelearning notebooks/auditoria/build_rastreabilidade.py · experiments/e0/results/e0_mcnemar.json
criada_em: 2026-08-17T04:30:00Z
---
**Etapa 2, lote 1** (Cap. 5: E0, E6, E3′ + Cap. 4). `rastreabilidade.json`
gerado: **38 números**, sendo **28 rastreados, 9 divergentes, 1 em legado**.

## O achado grave: uma significância que o artefato não sustenta

O Cap. 5, RQ1 do E0, afirma:

> "o teste pareado (RQ1, McNemar) na S-strat mostra deepseek-v4-pro
> **significativamente superior** ao v4-flash (**b=43, c=16, p<0,001**)"

O `e0_mcnemar.json`, para esse par nessa amostra, dá **b=73, c=91,
p=0,184** — **não significativo**. E procurei `b=43 / c=16` nos **43 pares**
do artefato, nas duas amostras: **não existe em nenhum**.

Na mesma frase, "estatisticamente empatado com o gpt-4o (**p=0,061**)": o
artefato dá **p=0,525**, e nenhum par tem p próximo de 0,061. Aqui o
*veredito* (empate) se sustenta; o número, não.

Isto é diferente de tudo que reportei até agora. As outras divergências eram
arredondamento ou escopo. Esta é uma **afirmação de significância estatística
que o artefato contradiz** — e a leitura (i) do capítulo se apoia nela para
dizer que há hierarquia dentro do platô de oráculos. Se o artefato estiver
certo, os quatro melhores estão empatados e a frase muda.

Duas explicações possíveis, e não sei qual é: (a) os números vêm de uma
execução que não está no repositório; (b) estão errados. Nos dois casos é
`divergente` e precisa do autor. **Não toquei no texto.**

## As outras oito divergências

| Número | Tese | Artefato |
|---|---|---|
| inválidos glm-5.2 S-rand | 0,0% | **0,7%** |
| inválidos v4-pro S-strat | 0,0% | **0,2%** |
| gpt-4o-mini S-rand | uma linha | o artefato tem **duas execuções**; a tese usa uma sem dizer qual |
| população do E6 | ≈140 mil | **181.490** |
| ganho C sobre B (E3′) | +3,0 p.p. | 2,93 |
| E35 supera a régua | sim | só no regime pareado; em **0 de 3** canônicas |
| piso de orçamento em 25 mil | sim | no canônico, **nenhuma** semente |

## O que confere (a maior parte)

Custo e cache do E0 inteiros, incluindo o "26× mais barato" (26,4) e a faixa
de cache 88–95% (88,3–94,8 no artefato). Toda a campanha multi-semente do E6.
A Tabela e3p com IC de Wilson, o McNemar e o bootstrap do E3′ — estes últimos
**recomputados do zero**, com b/c exatos e os três IC idênticos.

## Cap. 4

Entra como **`legado`**: a evidência existe no `activetextclassification`
(`L0_experimento.ipynb` com 0.891 na saída gravada + o xlsx da sensibilidade),
mas em repositório somente leitura e sem referência cruzada.

## Próximo lote

Faltam no Cap. 5: **E0-P, E1, E4 e a seção do gate**. Sigo por eles agora e
mando o lote 2. Depois Caps. 4, 3, 6, apêndices e pré-textuais, nessa ordem.
