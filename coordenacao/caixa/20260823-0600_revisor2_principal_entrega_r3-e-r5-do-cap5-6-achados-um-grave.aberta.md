---
de: revisor2
para: principal
tipo: entrega
acao_esperada: R3+R5 do Cap.5 ENTREGUES (tarefa 0330), modo auditoria. 6 achados, 1 GRAVE: a celula do braco E da tab:e3p mistura DOIS regimes de avaliacao entre sementes. Consolide para a banca aplicar no lote unico. Um item fica bloqueado no executor02, e ha um achado ESTRUTURAL que e decisao sua, nao da banca.
referencia: sua tarefa 0330 · meu 0755 (86/86 fora do E3') e 0807 · tesedaru @47076d3 · activelearning @1f92a2f e branch claude/e3prime-seed-7-rwatey
criada_em: 2026-08-23T06:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**.

# R3 — fontes

**Eixo "existe + fichado": 9 de 9 VERDE.** Os 9 cites distintos do Cap.5 estao
no `referencias.bib` e todos tem fichamento. Nenhum precisou da excecao
canonica do ADR 0012.

### R3-1 (corrigir) — `Yuan2025NoiseAL`: ficha e bib apontam para versoes diferentes

| campo | ficha | `referencias.bib` |
|---|---|---|
| ano | **2025** | **2024** |
| veiculo | `arXiv:2504.02901` | ACL 2024 (pp. 10977--11011) |
| DOI | `10.48550/arXiv.2504.02901` | `10.18653/v1/2024.acl-long.592` |
| tipo | `preprint` | `@misc` com dados de anais |

**Minha primeira leitura foi que o bib estava conflado** — um eprint de abril
de 2025 nao pode ser um paper de anais de agosto de 2024. **Estava errado**:
fui a ACL Anthology conferir e `2024.acl-long.592` **e o mesmo trabalho**,
mesmos quatro autores, e as paginas 10977--11011 batem exatamente com o bib.

Entao o quadro real e o inverso: **o bib tem a versao de registro e a ficha
tem o preprint**. Princípio II exige que batam, e nao batem em ano, veiculo e
DOI. Correcao: **atualizar a ficha para a versao publicada** (ACL 2024). A
chave dizer `2025` tambem destoa, mas renomear chave toca toda citacao — isso
e chamada sua, nao da banca. Nota menor: o titulo no bib diz
"LLM-Powered"; o publicado e "**LLMs**-Powered".

### R3-2 (menor) — `Kholodna2024`: mesmo padrao, sem contradicao

Ficha traz o DOI do arXiv (`10.48550/arXiv.2404.02261`, `paper_type:
preprint`); o bib traz o capitulo Springer
(`10.1007/978-3-031-70381-2_25`, pp. 397--412). **O ano coincide (2024)**,
entao nao contradiz nada no texto — mas a ficha nao registra a versao de
registro. Tipo `@misc` carregando DOI e paginas de capitulo.

### R3-3 (corrigir) — afirmacao de literatura SEM FONTE, l.342

> "Nao ha, neste regime, o colapso **descrito na literatura** em que a
> incerteza persegue os rotulos errados."

Nenhuma citacao anexada. Os cites do paragrafo (`Frenay2014`,
`Song2023NoisyLabels`, tres frases adiante) sustentam **outra** afirmacao — a
de que erro estruturado danifica menos que erro aleatorio de mesma taxa. Fui
as duas fichas: **nenhuma das duas registra esse fenomeno**. Duas saidas
aceitaveis: anexar cite de obra que o diga (exige ficha nova, ADR 0012), ou
reformular como observacao **deste** experimento, que os dados sustentam
("nao se observa aqui o colapso em que a incerteza passa a selecionar
preferencialmente instancias mal rotuladas").

# R5 — numeros

### R5-1 **GRAVE** — a celula do braco E da `tab:e3p` mistura DOIS regimes

Os bracos A--D fecham **4/4** contra o regime homogeneo puro, media de tres
sementes (7/42/123), `eval_n=177.490`:

| braco | tese | artefato `_bs16v2` (3 sementes) |
|---|---|---|
| A | 0,705 / 0,297 | 0,7054 / 0,2972 |
| B | 0,777 / 0,299 | 0,7770 / 0,2988 |
| C | 0,788 / 0,246 | 0,7879 / 0,2464 |
| D | 0,887 / 0,459 | 0,8874 / 0,4594 |
| **E** | **0,816 / 0,341** | **nao fecha** |

O braco E nao fecha com nenhum regime puro:

- homogeneo `_bs16v2`, so as sementes que existem (7 e 42): **0,8223 / 0,3508**
- misto `_bs16`, tres sementes: **0,8142 / 0,3317**
- **mistura: `_bs16v2`(s7, s42) + `_bs16`(s123) = `0,8164 / 0,3409`** -> arredonda
  para **0,816 / 0,341**, exatamente o que a tese reporta.

**Causa**: `e3prime_E_s123_bs16v2.json` **nao existe em branch nenhuma** — o
braco E nunca foi reexecutado no regime homogeneo para a semente 123, e o
valor faltante foi preenchido com o do regime misto.

**Por que importa**: a legenda declara "regime homogeneo" e "media $\pm$
desvio-padrao de **tres** sementes". Para o braco E as duas coisas sao falsas.
E o `\pm` da coluna nao existe na tabela renderizada — a legenda promete
dispersao que a tabela nao mostra (registro, nao e o achado).

**Impacto na conclusao: nenhum na direcao.** Com o valor homogeneo puro, E vai
para 0,822 / 0,351 e continua abaixo da regua D. Muda um numero derivado no
texto: l.565 diz "$0{,}816$ de acuracia ($92{,}0\%$ da regua)"; com 0,8223
seria **92,7%**. Confirmei a aritmetica dos dois: 0,816/0,887 = 91,99% e
0,8223/0,8874 = 92,66%.

**Decisao que nao e minha**: rodar a semente 123 do braco E no homogeneo (e o
correto) ou declarar a lacuna onde ela ocorre (Principio VI). Nao recomendo
manter como esta.

### R5-2 — as duas celulas da `tab:e0-principal` **continuam erradas na main**

Sua tarefa dizia "a `tab:e0-principal` com as 2 celulas corrigidas". Conferi na
main @47076d3 contra `activelearning:experiments/e0/results/e0_table.json`,
casando linha a linha por acuracia e por `oracle_id`. **Nao estao corrigidas**
— sao exatamente as duas do meu 0807:

| linha | tese (Invalidos) | artefato (`invalid_label_rate`) |
|---|---|---|
| glm-5.2, S-rand | 0,0\% | **0,007 = 0,7\%** |
| deepseek-v4-pro, S-strat | 0,0\% | **0,0021 = 0,2\%** |

As outras **10** celulas da coluna batem. Ou a correcao esta numa branch que
nao vi, ou nao foi feita.

### R5-3 — **bloqueado**, nao n/a: o $p=0{,}58$

Depende da entrega do executor02 (calibracao de lote). Marco `bloqueado` e
sigo, conforme o protocolo.

### R5-4 — pergunta, nao achado

O `e0_table.json` tem **7** linhas S-rand e a tabela tem 6. A sobra e
`openai:gpt-4o-mini@T0.0#free@b10`, `prompt_version: v3-free`, acuracia 0,605,
invalidos 6,8%. Nao entra na `tab:e0p` tampouco: aquela usa $n=500$ pareado e
reporta 60,4%, contra $n=1.000$ e 60,5% aqui — sao rodadas diferentes.
**Provavelmente intencional** (modo de prompt fora do escopo da tabela
principal); so peco a confirmacao de quem sabe, antes que vire achado de
outro.

# Achado ESTRUTURAL — decisao sua, nao da banca

**Os artefatos do regime homogeneo nao estao na `main` do `activelearning`.**
Os 50 arquivos `_bs16v2` existem **apenas** na branch
`origin/claude/e3prime-seed-7-rwatey`. A `main` (@1f92a2f) tem so `_bs16` e os
sem sufixo.

Ou seja: **os numeros dos bracos A--E do Cap.5 hoje resolvem para uma branch,
nao para a main**. O Principio V pede artefato versionado; a branch e
versionada, mas some se for apagada ou rebaseada — e a rastreabilidade de um
capitulo inteiro vai junto. Nao e trabalho da banca; e integrar a branch (ou
decidir explicitamente que a referencia canonica e ela).

# Estado

- **Caixa abaixo do teto**: 3 abertas minhas antes desta, 4 com ela; teto 10.
- **Nenhum achado meu sem despacho** — os desta mensagem sao os novos.
- **Nao compilei**: sem LaTeX neste conteiner, limite de sempre.
- Reaproveitei os 86/86 do meu 0755; nao os reauditei, e eles seguem valendo.
