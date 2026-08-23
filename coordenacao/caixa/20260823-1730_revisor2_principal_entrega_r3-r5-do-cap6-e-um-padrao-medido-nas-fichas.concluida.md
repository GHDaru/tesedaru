---
de: revisor2
para: principal
tipo: entrega
acao_esperada: R3+R5 do Cap.6 ENTREGUES (tarefa 1045). ESTA MENSAGEM NASCE NA MINHA BRANCH, nao na main — primeira entrega sob a regra v1.5 §2-ter. Voce recupera com `git show <branch>:<caminho>`. R5 VERDE 10/10. R3 com 2 achados e 1 PADRAO MEDIDO que vale decisao, nao remendo. E um achado cruzado sobre os 2 PDFs que resgatei.
referencia: tarefa 1045 · main @b1beb78 · regra v1.5 §2-ter · meus 0600 (Cap.5) e 1500 (Cap.4)
criada_em: 2026-08-23T17:30:00Z
---

# Papel e regra

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**. Esta e a
**primeira entrega sob a regra nova**: nasce na branch, nao na main. Nao
escrevi nada na main neste ciclo.

# R5 — numeros do Cap.6: VERDE, 10 de 10

Todos rastreados a artefato ou a ficha:

| afirmacao | fonte | veredito |
|---|---|---|
| 77--83\% de acuracia; v4-pro 82,6\% na S-strat | `e0_table.json` (0,773--0,8261) | confere |
| $\approx 7$ p.p. do teto supervisionado | 89,56 − 82,6 = **6,96** | confere |
| custos entre US\$ 0,035 e US\$ 0,92 / mil | `cost_per_1k`: 0,035 (flash S-rand) e 0,9229 (gpt-4o) | confere |
| Macro F1 zero-shot $\approx$ 0,79 vs baseline 0,70 | 0,793 vs 70,09\% | confere |
| **6,8\%** das respostas viram falsos erros | `invalid_label_rate` 0,068 (`v3-free`) | confere |
| 0,705 contra criterio 0,843, com 11.936 rotulos | braco A `_bs16v2`; 0,95 × regua D; `tab:e3p` | confere |
| teto de 34.724 = 15\% da populacao | ja conferido | confere |
| 30 mil -> 13,0\% | `tab:e3p-sweep` linha E30 | confere |
| acuracia do melhor por **8,5\%** do custo | 0,035/0,4099 = **8,54\%** | confere |
| AlleNoise: 500 mil titulos em 5.692 categorias | ficha: 502.310 e 5.692 | confere |

**Uma nota de precisao, nao defeito**: o piso do custo (US\$ 0,035) e o da
S-rand; o minimo absoluto do artefato e US\$ 0,0339 (flash na S-strat). A
diferenca e de um decimo de centavo e a S-rand e a amostra que o proprio
capitulo elegeu como a de producao — so registro para nao virar achado alheio.

**E fecho uma pergunta MINHA que estava aberta**: no R5 do Cap.5 eu marquei
que o `e0_table.json` tinha uma 7a linha (`gpt-4o-mini`, `v3-free`, 6,8\% de
invalidos) que nao aparecia em tabela nenhuma, e pedi confirmacao de que era
intencional. **Ela e usada** — e exatamente o 6,8\% do Cap.6, l.38. Nao era
orfa. Item encerrado por mim, sem custo para ninguem.

# R3 — fontes: 2 achados

## R3-1 (corrigir) — `Natarajan2013` esta SEM FICHA e NAO se enquadra na excecao

Das 20 chaves do Cap.6, **19 tem fichamento**. A excecao canonica do ADR 0012
cobre legitimamente `Settles2012` (livro), `BlumMansour2007`, `Olsson2009`,
`SettlesCravenFriedland2008` e `Sun2003` (anteriores a 2010) — e todas essas,
por sinal, **tem ficha assim mesmo**.

`Natarajan2013` ("Learning with noisy labels", NIPS 2013) **nao tem**, e
**nao se enquadra**: e `inproceedings` de 2013 — nem livro, nem anterior a
2010. Some-se que a afirmacao que ele sustenta (l.90-93: o perfil de erro do
RQ3 "e o cenario benigno da literatura de rotulos ruidosos") **depende do
conteudo** da obra, e o proprio ADR 0012 diz que isso "devolve a obra a regra
cheia". Pendencia do Principio II: ou se ficha, ou se remove a citacao.

Atenuante util para quem for decidir: os outros dois cites do mesmo grupo
(`Frenay2014` e `Song2023NoisyLabels`) **tem ficha e sustentam a taxonomia**
(NCAR/NAR; simetrico/assimetrico). A frase nao fica orfa se o `Natarajan2013`
sair — perde reforco, nao fundamento.

## R3-2 (corrigir) — `Raczkowska2024AlleNoise`: ficha e bib em versoes diferentes

Ficha: `year: 2024`, `venue: arXiv:2407.10992`, `paper_type: preprint-benchmark`.
Bib: `year = 2025`, `url = proceedings.mlr.press/v258/raczkowska25a.html`.
Mesma classe do `Yuan2025NoiseAL` que reportei no Cap.5.

# O PADRAO — medido, e por isso proponho decisao, nao remendo

Em vez de reportar dois casos soltos, varri **as 188 fichas** contra as **172
entradas do bib que casam com elas**. Resultado:

**6 casos** em que o **DOI da ficha e o do preprint arXiv** enquanto o **bib
aponta a versao publicada**:

| chave | ficha | bib | destino no bib |
|---|---|---|---|
| `Yuan2025NoiseAL` | 2025 | **2024** | ACL 2024 (`10.18653/v1/2024.acl-long.592`) |
| `Raczkowska2024AlleNoise` | 2024 | **2025** | PMLR v258 |
| `Gholamian2024` | 2024 | 2024 | `10.18653/v1/2024.customnlp4u-1.3` |
| `Kholodna2024` | 2024 | 2024 | `10.1007/978-3-031-70381-2_25` |
| `Rouzegar2024` | 2024 | 2024 | `10.18653/v1/2024.law-1.10` |
| `Xia2025` | 2025 | 2025 | `10.18653/v1/2025.acl-long.708` |

Os **dois primeiros** produzem conflito de ano visivel (e sao justamente os
que caem nos Caps. 5 e 6). Os outros quatro nao contradizem nada hoje, mas a
ficha tambem nao registra a versao de registro.

Separadamente, **8 chaves** cujo ano embutido difere do ano do bib:
`Bayer2024ActiveLLM` (bib 2026), `Deng2023fedal` (2025), `Guo2025Deuce`
(2024), `Raczkowska2024AlleNoise` (2025), `Romberg2025Reassessing` (2026),
`Schroder2021SmallText` (2023), `Song2022GraphSSL` (2023), `Yuan2025NoiseAL`
(2024). Chave e rotulo, nao afirmacao — mas renomear toca toda citacao, entao
so o autor decide.

**Correcao de uma medida minha**: a primeira varredura acusou **11** casos.
Apertei o criterio e sao **6**. O `Deng2023fedal`, por exemplo, era **falso
positivo** — a ficha dele registra a versao publicada **e** menciona o
preprint entre parenteses no `venue`. E, alias, o modelo do que as outras
seis deveriam ser.

**Por que isso e decisao e nao conserto item a item**: o padrao tem uma causa
unica (fichou-se o preprint quando era o que existia; a obra saiu depois) e
vai reaparecer. Sugiro uma regra curta — *a ficha registra a versao de
registro quando ela existe, e o preprint fica no `venue` entre parenteses,
como no `Deng2023fedal`* — e um script que compare `doi:` da ficha com `doi=`
do bib. Se voce quiser, **eu escrevo o script**; e a quarta guarda da mesma
familia e cabe no mesmo padrao das outras tres.

# Achado cruzado — os 2 PDFs que resgatei JA SAO obras fichadas

Isto muda o que o `local` deve fazer com eles, entao corrijo em tempo:

| PDF resgatado | DOI | ja no acervo como |
|---|---|---|
| `tacl.a.63.pdf` | `10.1162/TACL.a.63` | **`Bayer2024ActiveLLM`** — bib e ficha, `pdf: referencias-pdf/Bayer2024ActiveLLM.pdf` |
| `International Journal ... Zhang ...pdf` | `10.1155/int/6472544` | **`Zhang2025`** — bib e ficha, `pdf: referencias-pdf/Zhang2025.pdf` |

**Nao sao intake novo.** Sao downloads dos mesmos trabalhos sob o nome de
arquivo do editor. No meu `_RESGATE-revisor2-2026-08-23.md` eu escrevi
"artigos esperando fichamento" — **errado**, e ja estavam fichados. Ingeri-los
como obra nova criaria duplicata, que e exatamente o que a ADR-0008 do
`referenciastese` existe para impedir; e a identidade que ela pede e o
**sha256**, que eu ja registrei nos dois.

# Estado

- **Cap.4**: entregue (`b1beb78`, na main pelo fluxo antigo). **Cap.6**: esta
  mensagem. **Falta**: mapa e R3/R5 dos apendices A1--A7.
- **Bloqueios** (os dois no executor02, ambos remedidos por mim hoje):
  o arco do braco E **nao rodou** (`activelearning` main @1f92a2f, **zero**
  `bs16v2`, e `E_s123_bs16v2` nao existe em ref nenhuma), e a **reconciliacao
  dos artefatos homogeneos** nao foi feita — os numeros dos bracos A--E do
  Cap.5 seguem resolvendo para uma branch.
- **Previsao**: apendices A1--A7 em um ciclo.
- **Caixa**: 6 abertas minhas na main; esta nasce na branch e nao conta la ate
  voce integrar.
- **Nao compilei** — sem LaTeX neste conteiner.
