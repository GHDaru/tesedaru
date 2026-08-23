---
de: revisor2
para: principal
tipo: entrega
acao_esperada: §6 sobre o adiantamento do revisor1 (`cruzada/a2-config-canonica` @91a2be0). REEXECUTEI o script dele: exit 0, PASS, mesmos numeros. CONFIRMO a ressalva (b) dele — ha uma TERCEIRA configuracao. E fecho uma ponta que eu mesmo tinha deixado aberta na minha primeira cruzada do dia. Um alerta de nomenclatura para quem reescrever o A2.
referencia: branch @91a2be0 e `scripts/confere-config-ag.py` · entrega do revisor1 · meus 1930 (a excecao do 250old) e 2000 · lote @24b09f7 ja entregue
criada_em: 2026-08-24T07:00:00Z
---

# Papel e regra

Titulo da sessao (ADR 0011): **"Revisor 02"**. **v1.5 §2-ter cumprida**:
setima entrega seguida na branch; nao toquei a main.

# 1. §6 no script do revisor1 — reexecutei, e passa

Ele executou; quem verifica sou eu. Rodei `scripts/confere-config-ag.py` da
branch dele, em worktree destacada, contra o `activetextclassification`:

```
     L0    tese g1/g100    _old (pop 20)  _oldold (pop 50)  veredito
     10     13.06/18.82      13.06/18.82       12.90/19.45  pop 20
     50     22.12/33.83      22.12/33.83       21.01/33.21  pop 20
    100     26.65/36.71      26.65/36.71       28.22/38.76  pop 20
  30000     85.07/85.88      85.07/85.88      (nao existe)  pop 20
PASS — exit 0
```

**Confirmo o veredito dele**: a tabela do Cap. 4 vem das corridas de populacao
20, entao o defeito esta **confinado a descricao do A2** e nao toca resultado
nenhum. Isso bate com o que eu ja tinha medido de outro jeito na auditoria do
Cap. 4 (as 38 celulas da `tab:ag-evolucao` conferidas contra `_old` na geracao
100); o contraste contra `_oldold` nos tamanhos 10 e 50 e dele, e e o que
transforma "bate com `_old`" em "**nao** bate com `_oldold`". Complementar,
nao redundante.

Uma nota de uso: o script recebe `--repo`, nao `--activetextclassification`.
Errei o flag na primeira tentativa; registro para o proximo nao perder o
minuto.

# 2. A ressalva (b) dele — CONFIRMADA, e maior do que uma dicotomia

Ele avisou que ha uma terceira configuracao. Medi todas as pastas restantes:

| pasta | linhas | ger. max | populacao | avaliacoes |
|---|---|---|---|---|
| `_30000v1` | 20.000 | **200** | **100** | **20.000** |
| `_30000old` | 2.000 | 100 | 20 | 2.000 |
| `_20000old` | 2.000 | 100 | 20 | 2.000 |
| `_10000old` | 2.000 | 100 | 20 | 2.000 |
| `_100000v2` | 2.000 | 100 | **20** | 2.000 |
| `_250old` | **4** | **2** | **2** | 4 |

**Ele esta certo**: o `30000v1` e uma terceira configuracao, com populacao
100 e 200 geracoes. E o `250old` e mesmo corrida abortada — quatro linhas,
duas geracoes, dois individuos.

# 3. Isso FECHA uma ponta que eu tinha deixado aberta hoje de manha

Na minha primeira cruzada do dia (entrega 1930, a do $L_0=100$), eu disse que
a evidencia do "cabecalho do CSV" era **mais fraca do que enunciada**, porque
o `250old` aparecia do lado "errado": tinha BOM, coluna
`metric_value_on_eval_set` e `experiment_params.json`, como as `_oldold`,
apesar do sufixo `_old`. Deixei como anomalia sem explicacao.

**Agora tem explicacao**: o `250old` e uma **corrida abortada da geracao
`_oldold`** — parou na 2ª geracao com 2 individuos. Por isso carrega o
cabecalho e o arquivo de parametros daquela geracao. **Nao e excecao a regra;
e uma corrida que nao chegou a existir.**

Consequencia: a evidencia do cabecalho do CSV, que eu tinha enfraquecido, na
verdade **se sustenta** — o corte `_old` × `_oldold` e limpo depois que se
remove uma corrida abortada. Corrijo a minha propria ressalva.

# 4. Alerta de nomenclatura, para quem reescrever o A2

O sufixo do diretorio **nao e marcador confiavel de geracao**:

- `_100000v2` tem **populacao 20** — pertence a familia **canonica**, apesar
  do `v2`;
- `_30000v1` tem **populacao 100** — nao pertence a nenhuma das duas;
- `_250old` tem sufixo `_old` e e da geracao `_oldold`.

Quem for reescrever o A2 nao pode inferir configuracao pelo nome da pasta. O
que discrimina e o `individual_id` do `detailed_fitness`, que e o que o script
do revisor1 usa. **Sugiro que essa frase entre na instrucao a banca**, junto
com a dele.

E, pelo mesmo motivo, o A2 nao deveria dizer "**a** configuracao" no singular
sem qualificar: ha **tres** no repositorio e so uma alimenta a tese. Nem o
$L_0=250$ nem o $L_0=100.000$ aparecem em tabela alguma do Cap. 4, entao a
abortada e a de populacao 100 nao contaminam nada — mas quem le o apendice
para reproduzir precisa saber qual e qual.

# 5. A ressalva (a) dele ja esta resolvida

A excecao do $L_0=10$ (200 geracoes, e a leitura da 100ª geracao no Cap. 4)
**ja foi aplicada** no lote que a banca entregou em `@24b09f7`: o texto la ja
diz "200 geracoes no caso $|L_0|=10$, o unico que difere" e a contagem ja
carrega os 4.000. Era o mesmo ponto que eu tinha registrado como armadilha na
auditoria do Cap. 4. **Fechado, nao pendente** — vale ele saber para nao
recruzar.

# Estado

- **Prontidao**: o critério do A2 refinado esta pronto, e agora com **duas
  ferramentas**: o meu criterio do Cap. 3 (as duas trocas de numero e a queda
  do "identica em todas as execucoes") e o script do revisor1, que eu ja
  reexecutei e sei rodar. A re-cruzada sai em minutos.
- **Bloqueio**: braco E, no executor02. Reconferi: `activelearning` main sem
  nenhum `bs16v2`; `E_s123_bs16v2` inexistente em ref alguma.
- **Erros de ano da bib**: nao reabro.
- **Nao compilei** — sem LaTeX neste conteiner.
