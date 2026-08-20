---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir a correção do número da população reservada do E6 no Cap. 5 — eu não edito texto da tese
referencia: activelearning@24b00ab notebooks/auditoria/e6-populacao.ipynb · 5-resultados-falco/texto.tex seção "E6" · artefato popcurve_*_summary.json
criada_em: 2026-08-17T01:30:00Z
---
Primeiro notebook da Onda 1 entregue (E6). **13 das 14 afirmações do Cap. 5
conferem exatamente** contra os artefatos. Uma diverge, e é de fato.

## A divergência

O Cap. 5, na abertura da seção do E6, diz que a base é dividida em pool de
50.000 e "uma **população reservada** com todo o restante (**≈140 mil
instâncias**)".

O artefato registra **`population: 181490`**
(`popcurve_pvbin_entropy_summary.json`), e o runner é explícito:
`population = dedup[args.pool_size:]`, ou seja 231.490 − 50.000 = **181.490**.
O notebook recalcula a partição do zero, a partir do CSV, e chega no mesmo
181.490 — com o md5 do arquivo impresso na tela.

Não é arredondamento: **≈140 mil subestima em cerca de 23%**.

Repare que o próprio texto se contradiz internamente: "todo o restante" de
231.490 menos 50.000 não pode ser 140 mil. O número correto está a uma
subtração de distância do que a frase já afirma.

## Provável origem (hipótese, não conclusão)

Não confundir com a população do **E3′**, que é **177.490** — ali se excluem
também os 4.000 do *holdout* do ciclo real. Nenhum dos dois dá 140 mil. Pode
ser resíduo de uma versão anterior do particionamento; o `principal` ou o autor
saberão dizer. Não fui atrás porque a decisão não é minha.

## O que NÃO diverge (para não assustar)

Tudo o mais bate: as saturações de semente única nos 8 braços, a campanha
multi-semente inteira (SGD entropia 9.062 ± 563; aleatório 15.500 ± 1.102;
PVBin 19.312 ± 704 e 40.625 ± 1.408), o Wilcoxon (8/8 no SGD, 6/8 no PVBin,
p = 0,0078) e o viés de autoavaliação de −17,1 ± 1,0 p.p. em |L| = 10k. A
observação do capítulo de que os 8.000 da Tabela e6 ficam na "borda otimista"
da faixa multi-semente também confere: o mínimo da campanha é 8.500.

**Detalhe metodológico que vale registrar em ADR**: a campanha multi-semente é
`s43..s50` e **não inclui a semente 42**. Está correto — a 42 é a descritiva da
Tabela e6 e a campanha são 8 execuções independentes —, mas em lugar nenhum
isso está escrito. Eu mesmo errei na primeira tentativa, incluí a 42, vi as
quatro médias divergirem e quase acusei a tese por erro meu. Um leitor de banca
que tente reproduzir vai cair no mesmo buraco.

## Próximo

Sigo para o notebook do E3′, o segundo da Onda 1. Lá a divergência já é
conhecida e maior (a inversão da varredura de orçamento, mensagem das 21:30).
