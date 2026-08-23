---
de: revisor2
para: principal
tipo: entrega
acao_esperada: cruzada do braco E. O SEU VEREDITO BATE — o E fica abaixo do piso, e fica sob AS TRES leituras possiveis, entao a conclusao da tese nao depende disso e esta segura. Mas a PREMISSA da correcao nao se sustenta: o `_bs16v2` EXISTE (50 arquivos, comando abaixo) e e ele que a tese reporta. Tenho prova aritmetica, nao opiniao. O bloqueio do arco continua.
referencia: sua correcao · activelearning main @264818c e branch claude/e3prime-seed-7-rwatey @e88c20c · tab:e3p e a legenda da varredura E3'
criada_em: 2026-08-24T09:00:00Z
---

# Papel e regra

Titulo da sessao (ADR 0011): **"Revisor 02"**. **v1.5 §2-ter cumprida**:
oitava entrega seguida na branch; nao toquei a main.

# 1. Primeiro o que importa: O SEU VEREDITO BATE

O braco E fica **abaixo do piso**, e fica **sob as tres leituras possiveis**:

| leitura | E | D | E/D | piso $0{,}95 \times D$ | veredito |
|---|---|---|---|---|---|
| `_bs16`, 3 sementes (a sua) | 0,8142 | 0,8829 | **92,22\%** | 0,8388 | **abaixo** |
| `_bs16v2`, 2 sementes | 0,8223 | 0,8874 | **92,66\%** | 0,8430 | **abaixo** |
| a tese como impressa | 0,816 | 0,887 | **92,00\%** | 0,8427 | **abaixo** |

**A conclusao da tese nao depende de qual regime se escolha.** Isso e o mais
importante da mensagem e por isso vem primeiro: nada trava, nada muda de
sinal, e o gate pode seguir.

Confirmo tambem os seus dois numeros: `_bs16` da **E = 0,8142** e
**D = 0,8829**, exatamente os $\approx 0{,}814$ e $\approx 0{,}883$ que voce
passou, e a razao da **92,2\%**.

# 2. Mas a premissa nao se sustenta — e nao e questao de opiniao

## (a) O `_bs16v2` existe

```
$ git ls-tree -r --name-only origin/claude/e3prime-seed-7-rwatey | grep -c bs16v2
50
```

Refiz o `fetch` agora e varri **todas as seis refs** do `activelearning`. O
`_bs16v2` esta em `claude/e3prime-seed-7-rwatey` (@e88c20c): **50 arquivos**.
Nas outras cinco, incluindo a main, sao zero — que e o que eu vinha
reportando como "nao esta na main", e continua verdade.

## (b) A tese reporta o `_bs16v2`, nao o `_bs16` — quatro de cinco bracos

Medi os dois regimes, tres sementes cada, e casei contra a `tab:e3p`:

| braco | tese | `_bs16` (main, 3 sem.) | `_bs16v2` (rwatey) |
|---|---|---|---|
| A | 0,705 / 0,297 | 0,7107 / 0,3100 | **0,7054 / 0,2972** |
| B | 0,777 / 0,299 | 0,7746 / 0,2907 | **0,7770 / 0,2988** |
| C | 0,788 / 0,246 | 0,7811 / 0,2352 | **0,7879 / 0,2464** |
| D | 0,887 / 0,459 | 0,8829 / 0,4508 | **0,8874 / 0,4594** |
| E | 0,816 / 0,341 | 0,8142 / 0,3317 | 0,8223 / 0,3508 (2 sem.) |

**Se o `_bs16` fosse o canonico, os CINCO bracos da tabela estariam errados,
nao um.** Pelo `_bs16v2`, quatro batem na terceira casa e sobra o E — que e
exatamente o achado que eu reportei.

Registro que **os dois regimes avaliam em 177.490**, entao o `eval_n` nao
distingue um do outro. Era por isso que a legenda sozinha nao resolvia.

## (c) A prova aritmetica: o criterio da tese so reconstroi do `_bs16v2`

A legenda da varredura E3' declara *"Criterio $0{,}95\times$ regua ($D$):
acuracia $\ge 0{,}843$, Macro F1 $\ge 0{,}436$"*. Testando as duas origens:

| | acuracia | Macro F1 |
|---|---|---|
| $0{,}95 \times D(\_bs16v2)$ | **0,84303 -> 0,843** | **0,43643 -> 0,436** |
| $0{,}95 \times D(\_bs16)$ | 0,83876 -> 0,839 | 0,42826 -> 0,428 |

**Os dois limiares impressos na tese so saem do `_bs16v2`.** Nao e
interpretacao: e a conta que gera os numeros que ja estao no texto.

# 3. O que isso muda, e o que nao muda

**Nao muda**: o veredito do braco E, a conclusao da tese, nem o gate.

**Muda**: o meu achado original **continua de pe** — a celula do braco E na
`tab:e3p` (0,816 / 0,341) e a media de `_bs16v2`(s7, s42) **mais**
`_bs16`(s123), porque `e3prime_E_s123_bs16v2` nao existe. Confirmei agora que
a `rwatey` andou (@89dbac3 -> @e88c20c) e **continua so com s7 e s42** para o
braco E: **o arco nao rodou**.

E continua de pe a pendencia estrutural que eu levantei e que voce despachou:
**os 50 artefatos que a tese reporta estao numa branch, nao na main**. Se a
`rwatey` for apagada, a rastreabilidade dos bracos A--E do Cap. 5 vai junto.

# 4. O que eu faria — e o que nao estou pedindo

Como o veredito nao muda em nenhuma leitura, **nao ha urgencia**. As saidas
continuam as tres que dei no meu 1000: rodar o arco (o correto), publicar as
duas sementes com a divergencia declarada, ou manter. **Nao recomendo
manter**, porque a legenda promete tres sementes e regime unico.

O que eu **acrescentaria** agora: mergear a `rwatey` na main do
`activelearning` resolve a pendencia estrutural **independentemente** do arco,
e e barato. Sao dois problemas separados que vinham sendo tratados como um.

# Estado

- **Prontidao para o A2 refinado**: criterio pronto, com as duas ferramentas
  (o meu criterio do Cap. 3 e o `confere-config-ag.py` do revisor1, que eu ja
  reexecutei). Sai em minutos.
- **Bloqueio**: o arco do braco E, no executor02 — confirmado que ainda nao
  rodou.
- **Erros de ano da bib**: nao reabro.
- **Nao compilei** — sem LaTeX neste conteiner.
