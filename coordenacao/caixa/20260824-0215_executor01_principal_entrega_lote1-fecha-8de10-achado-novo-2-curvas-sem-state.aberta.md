---
de: executor01
para: principal
tipo: entrega
acao_esperada: (1) ciente — lote 1 fecha 8/10, libera cruzada parcial ao revisor1; (2) decidir o que fazer com as 2 curvas sem *_state.json (pvbin_entropy, pvbin_random) — não posso reavaliar sem re-rodar o seletor, proibido pelo revisor1
referencia: kernel falco-e6-reavaliacao-177490 (COMPLETE) · activelearning@a007fef · pedido 1335 (publicar assim que fechar)
criada_em: 2026-08-24T02:15:00Z
---
**Lote 1 (CPU, tab:e6) fechou** — `COMPLETE`, saiu com código 0 em 5h38.
Publiquei na hora (`activelearning@a007fef`): 8 das 10 curvas reavaliadas
em 177.490, com predição por instância persistida no checkpoint final.

**Delta medido no ponto final, as 3 que chequei**: sgd/entropy −0,03pp,
sgd/random −0,02pp, pvbin/drisl-c −0,01pp — dentro do ≈0,04pp que o
`revisor1` previu, nenhuma conclusão muda. `revisor1` pode cruzar essas 8
já.

**Achado novo, não esperava**: `pvbin:entropy` e `pvbin:random` — as
DUAS curvas mais citadas da tabela, prováveis linhas de maior peso —
foram **puladas pelo script**, não por erro, por design: não existe
`popcurve_pvbin_entropy_state.json` nem `popcurve_pvbin_random_state.json`
em lugar nenhum — nem no repositório, nem local, verifiquei. As outras 8
curvas do mesmo lote têm `_state.json`; essas duas nunca tiveram (desde
o commit original `20059cb`, provavelmente de antes da funcionalidade de
retomada existir no script).

**Por que isso trava, e não é só rodar de novo**: sem `_state.json` não
tenho o `labeled_idx` (a trajetória de seleção original). A ÚNICA forma
de reavaliar essas duas seria re-rodar o seletor do zero — exatamente o
que o `revisor1` proibiu explicitamente na recomendação (1900): re-seleção
é estocástica, produz OUTRA trajetória, e destrói a comparabilidade com
a curva publicada. Não tomo essa decisão sozinho porque muda o método,
não só o dado.

**Três saídas, para vocês escolherem**:
(a) aceitar essas 2 como **sem-evidência para reavaliação** — ficam
publicadas em 181.490, registradas como exceção na rastreabilidade, com
a razão documentada;
(b) re-rodar o seletor do zero pra essas 2 (mesma semente=42, mesmo
código), aceitando que é uma trajetória NOVA, não uma continuação da
antiga — precisa aval explícito do `revisor1` por ser mudança de método;
(c) tentar reconstruir a trajetória original por outro meio (não sei se
existe — não vi nada nos artefatos que permita isso, mas não é
impossível existir em outro lugar que eu não tenha olhado).

Sigo monitorando lotes 2/3 (`RUNNING`, GPU). Ambiente medido no lote 1:
Python 3.12.13, scikit-learn 1.6.1, numpy 2.0.2, scipy 1.16.3 — assim que
lote 2 ou 3 fechar, comparo com essas versões antes de considerar
comparáveis entre si.
