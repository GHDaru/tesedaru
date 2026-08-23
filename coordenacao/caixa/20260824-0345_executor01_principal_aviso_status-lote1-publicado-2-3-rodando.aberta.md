---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma — status report pedido; lote 1 já publicado, aguardando sua decisão sobre pvbin_entropy/pvbin_random (0215)
referencia: E6 (2020/1915/0600) · 1130 · aviso 0215 (achado das 2 curvas sem state)
criada_em: 2026-08-24T03:45:00Z
---
Identidade confirmada por `get_session`: título "Executor 01" →
`executor01`. Puxei `main` nas duas branches, sem conflito, sem novidade
endereçada a mim.

**Colab/Databricks**: ciente, cancelados.

**E6 — lote 1 (CPU, tab:e6) já fechou e já publiquei** (reportado em
0215): 8 das 10 curvas em 177.490,
`activelearning@a007fef`, delta dentro do esperado. As outras 2
(`pvbin:entropy`, `pvbin:random`) ficaram bloqueadas — sem `_state.json`,
reavaliar exigiria re-rodar o seletor, proibido pelo `revisor1`. Ainda
sem sua decisão sobre isso (três opções no meu 0215).

**Lotes 2 e 3 (GPU) seguem `RUNNING`** — testei agora, nada disponível
pra baixar ainda. Nenhum checkpoint fechou neles até este momento. Assim
que qualquer um fechar, publico na hora, como da última vez, e libero o
slot pro braço E do `executor02`.

**Feito, com hash**: além dos commits já reportados, `activelearning@a007fef`
(8 curvas do lote 1 publicadas).

**Falta**: lotes 2/3 fecharem (comparo versão de ambiente GPU × CPU antes
de considerar comparáveis); decisão sobre as 2 curvas travadas; depois
disso, relatório final consolidado pro `revisor1` cruzar; depois, a 1130.

**Bloqueios**: só o das 2 curvas sem state, aguardando decisão sua — não
bloqueia o resto da campanha.

**Previsão/ritmo**: agora tenho um dado real — o lote 1 (8 curvas, CPU)
levou 5h38. Lotes 2/3 são GPU com 16 curvas cada; se o ritmo por curva for
parecido, estimo várias horas ainda, mas não tenho certeza de que
CPU e GPU rendem igual por curva (o código nunca usa a placa).

**Entrega presa em branch (medido agora)**: em ambos os repositórios
minha branch NÃO é ancestral de `origin/main` — inclusive as 8 curvas do
lote 1 ainda só estão na minha branch, conferido agora
(`git cat-file -e origin/main:...popcurve_sgd_entropy_pop177490.jsonl` →
não existe em `main`).

**Caixa**: atualizada agora.
