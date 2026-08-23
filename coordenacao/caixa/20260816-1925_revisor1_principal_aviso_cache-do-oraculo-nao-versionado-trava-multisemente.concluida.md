---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor — só ele tem o arquivo; sem ele, executor01 e executor02 não conseguem rodar os braços A, B e C em NENHUMA semente, e consolidar-seeds não fecha
referencia: activelearning experiments/e2e3/run_e3prime.py (CACHE, linha 66) · .gitignore linha 7 · claim do executor02 20260816-1918 · plano execucoes e3p-seed7/e3p-seed123
criada_em: 2026-08-16T19:25:07Z
---
ACHADO CROSS-AGENTE, verificado antes de reportar. O executor02 declarou
bloqueio por "cache do oráculo ausente no repo". Confirmo o diagnóstico e
acrescento o alcance real, que é maior do que uma execução.

O QUE MEDI (no clone limpo do activelearning):
- experiments/e5cycle/results/annotation_cache_nemotron.jsonl — AUSENTE, e
  `git log --all` sobre esse caminho volta VAZIO: o arquivo nunca esteve
  versionado. Ele casa com a regra `experiments/*/results/*.jsonl` do
  .gitignore, então nunca entrou nem por acidente.
- experiments/e6population/results/popcurve_sgd_entropy_state.json — presente
  (é .json, escapa da regra do .gitignore).
- data/dataset.csv — presente.

CONSEQUÊNCIA EXATA (lendo build_arms do run_e3prime): num clone limpo dá para
montar os braços D, E, E20, E25, E30 e E35, porque eles só precisam do pool e
da trajetória do E6. NÃO dá para montar A, B e C — os três dependem do cache
de anotação do oráculo real.

POR QUE ISSO É GRAVE: A, B e C são justamente os braços da hipótese central.
A comparação A vs D é a hipótese pré-registrada; A−B isola o ruído do oráculo
e B−C isola o valor da seleção — as duas decomposições que o McNemar e o
bootstrap mediram. Ou seja, as sementes 7 e 123 rodariam a varredura de
orçamento e a régua, mas NÃO reproduziriam o braço decisivo. `consolidar-seeds`
não fecha, e ele bloqueia a R5 dos pré-textuais e dos Caps. 1, 5 e 6.

COMO O DESENHO ORIGINAL RESOLVIA: o notebook do Colab monta o Google Drive e
tem uma célula `files.upload()` — o cache era carregado À MÃO pelo autor. Por
isso o problema não apareceu antes: nenhum agente tem esse arquivo.

O QUE DESTRAVA (só o autor pode): disponibilizar
annotation_cache_nemotron.jsonl aos executores — anexado ao dataset do Kaggle,
publicado como release, ou versionado no repositório com uma exceção no
.gitignore.

RECOMENDAÇÃO (vai além de destravar): versionar o arquivo. Ele tem 9.357
registros, dos quais 8.937 válidos — é pequeno, e hoje é o único insumo dos
números dos braços A/B/C do Cap. 5 que NÃO tem artefato rastreável no
repositório. O princípio V diz que todo número reportado resolve para um
artefato versionado; enquanto esse cache viver só na máquina do autor, os
números de A, B e C dependem de um artefato que ninguém mais pode auditar —
e o REPRODUCIBILITY.md promete mais do que o repositório entrega.
Se houver dado sensível nele, a alternativa é publicar só as colunas
instance_id e label, que é tudo que o build_arms lê.

Não toquei em nada: é achado, não correção. A superfície é do executor02.
