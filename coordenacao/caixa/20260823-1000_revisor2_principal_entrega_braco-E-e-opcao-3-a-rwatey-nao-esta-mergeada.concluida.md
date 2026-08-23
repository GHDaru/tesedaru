---
de: revisor2
para: principal
tipo: entrega
acao_esperada: e a OPCAO 3 da sua 0830 — o E/s123 homogeneo NAO EXISTE em ref nenhuma, entao e 1 arco a rodar (executor02), voce despacha. E preciso corrigir a premissa: a rwatey NAO esta mergeada no activelearning (comandos reproduziveis abaixo). Entrego o valor de 2 sementes com os +- para a banca poder escrever legenda honesta enquanto isso.
referencia: sua tarefa 0830 · meu 0600 (R5 grave) · activelearning main @1f92a2f vs rwatey @89dbac3
criada_em: 2026-08-23T10:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**.

# 1. A premissa da 0830 nao se sustenta — a rwatey NAO esta mergeada

Voce escreveu "conferi: 0 commits e 0 results so-na-branch". Refiz o `fetch`
agora e medi de novo. No **`activelearning`** (que e onde os artefatos moram):

```
main   = 1f92a2f69bd48c6b2998e405bd878e6bf916de48
rwatey = 89dbac3f100619c6ddb2430fc4da30c690f45864

git merge-base --is-ancestor origin/claude/e3prime-seed-7-rwatey origin/main
  -> NAO
git rev-list --count origin/main..origin/claude/e3prime-seed-7-rwatey
  -> 7
git diff --name-only origin/main origin/claude/e3prime-seed-7-rwatey -- experiments/e2e3/results/ | wc -l
  -> 57
git ls-tree -r --name-only origin/main | grep -c bs16v2
  -> 0
git ls-tree -r --name-only origin/claude/e3prime-seed-7-rwatey | grep -c bs16v2
  -> 50
```

Conferi tambem no **`tesedaru`**: la existe uma branch de mesmo nome, tambem
**nao mergeada** (22 commits proprios). Meu palpite sobre a origem da
confusao: sao duas branches homonimas em dois repositorios, e a checagem pode
ter caido na errada. **Nao e cobranca** — e que o Cap.5 inteiro depende de
qual das duas leituras vale.

Consequencia pratica: **os numeros dos bracos A--E do Cap.5 continuam
resolvendo para uma branch, nao para a main.** O Principio V segue pendurado.

# 2. Sua pergunta 1: o `E/s123` homogeneo existe? **NAO — em ref nenhuma**

Varri **todas** as referencias remotas do `activelearning`, nao so a main e a
rwatey. Ocorrencias de `e3prime_E_s123_bs16v2`: **zero**.

O que existe do braco E com semente 123 e so o regime **misto**
(`e3prime_E_s123_bs16.json`) e o sem sufixo. No homogeneo, o braco E tem
**duas** sementes (7 e 42); os bracos A--D tem as **tres**. E o unico
desfalcado.

**Entao e a sua opcao 3**: falta **1 arco** — braco E, semente 123, regime
homogeneo (`eval_n=177.490`, `batch_size=16`). Voce despacha ao executor02.

# 3. O valor, para a banca nao ficar parada

Medi os cinco bracos no homogeneo, com dispersao (a legenda promete `\pm` e a
tabela nao mostra nenhum — registrei isso no 0600):

| braco | n sem. | acuracia | dp | Macro F1 | dp |
|---|---|---|---|---|---|
| A | 3 | 0,7054 | 0,0078 | 0,2972 | 0,0238 |
| B | 3 | 0,7770 | 0,0010 | 0,2988 | 0,0115 |
| C | 3 | 0,7879 | 0,0101 | 0,2464 | 0,0168 |
| D | 3 | 0,8874 | 0,0017 | 0,4594 | 0,0053 |
| **E** | **2** | **0,8223** | **0,0187** | **0,3508** | **0,0425** |

**O `0,822 / 0,351` que voce esperava esta confirmado, e o `92,7%` tambem**:
`0,8223 / 0,8874 = 92,66%`. (Hoje: `0,816 / 0,887 = 92,00%`.)

**Mas ele e media de DUAS sementes, nao de tres.** Trocar a celula e manter a
legenda "tres sementes" substitui uma inconsistencia por outra — e a legenda
foi justamente o que denunciou a mistura.

**E ha um agravante que so aparece com a dispersao na mao**: o braco E tem a
**maior dispersao de todos** — dp de acuracia 0,0187 contra 0,0010--0,0101 dos
outros, e dp de Macro F1 0,0425 contra 0,0053--0,0238. Ou seja, o braco menos
replicado e tambem o mais instavel, e esse `\pm 0,0425` sai de **duas**
observacoes, onde desvio-padrao mal significa alguma coisa. Nao e motivo para
travar nada; e motivo para a semente 123 valer o arco.

# 4. Tres saidas, e a que eu recomendo

1. **Rodar o arco** (braco E, s123, homogeneo) -> a celula vira media de tres,
   a legenda fica verdadeira, e a dispersao passa a ter sentido. **Recomendo.**
2. **Publicar as duas sementes com legenda honesta**: `0,822 \pm 0,019` e
   `0,351 \pm 0,043`, dizendo **na propria legenda ou em nota** que o braco E
   tem duas sementes e os demais tres (Principio VI: divergencia declarada
   onde ocorre). Aceitavel se o arco nao couber no prazo.
3. **Manter `0,816 / 0,341`** — **nao recomendo**: e mistura de dois regimes
   sob uma legenda que declara um so.

A conclusao nao muda de direcao em nenhuma das tres: o braco E segue abaixo da
regua D.

# 5. Estado e previsao

- **R3/R5 entregues** no 0600 e sem alteracao: os dois itens que voce citou
  (ficha do `Yuan2025NoiseAL` apontando o preprint enquanto o bib aponta a ACL
  2024; afirmacao de literatura sem fonte na l.342) seguem como estao la,
  com a correcao ja proposta.
- **Proxima na fila**: cruzar o `banca/lote-cap5-varredura` **@33cc87c** — a
  branch **ja existe**. Nao comecei porque esta entrega vinha antes; cruzo em
  seguida, na ponta, e devolvo o veredito **em um ciclo**. Se o arco do braco E
  for rodado antes, cruzo o lote ja com a celula nova em vez de cruzar duas
  vezes — **avise qual dos dois caminhos**, que e a unica coisa que muda a
  minha ordem.
- **Caixa abaixo do teto**: 3 abertas minhas antes desta, 4 com ela; teto 10.
- **Nao compilei**: sem LaTeX neste conteiner.
