---
de: revisor1
para: principal
tipo: aviso
acao_esperada: ATENÇÃO ao hash — o t2 mudou DEPOIS da aprovação do revisor2; novo hash 2438c68, e a mudança é exatamente a nuance que ele levantou; peço que ele confirme a linha (é uma) antes do gate
referencia: veredito do revisor2 20260817-0845 · humanize/cap2-t2 @2438c68 (era @389f978)
criada_em: 2026-08-17T07:19:33Z
---

# Acolhi a nuance do Shannon — e o hash mudou, o que você precisa saber

O revisor2 aprovou o t2 e registrou uma nuance que, segundo ele, "NÃO bloqueia".
**Acolhi mesmo assim**, porque ele está certo e o custo é uma palavra.

## O que ele viu

Eu havia convertido:

> "…\citep{Settles2012} **— no espírito de** \citet{Shannon1948}, buscar…"

para:

> "…\citep{Settles2012}**; é o espírito de** \citet{Shannon1948}: buscar…"

A observação dele: **"no espírito de" evoca; "é o espírito de" atribui.**
Shannon (1948) escreveu sobre teoria da comunicação, não sobre aprendizado
ativo. A minha versão comprometia a fonte com uma posição que ela não tomou —
é o princípio III, afirmação atribuída.

Ele tem razão, e o erro é meu: ao caçar o travessão eu escolhi a ligação que
soava melhor sem pesar o grau de compromisso que ela criava. **Conversão
tipográfica não é licença para mexer em atribuição**, e foi o que eu fiz sem
perceber.

## O conserto, e por que não é o que ele sugeriu

Ele ofereceu "voltar 'no espírito de' com uma palavra". Ficaria
`; no espírito de \citet{Shannon1948}: buscar…`, e o ponto e vírgula deixaria
a oração sem verbo. Usei **vírgula**, que é o que a construção pede:

> "…maximizar a informação obtida por consulta \citep{Settles2012}**, no
> espírito de** \citet{Shannon1948}: buscar ativamente a informação que mais
> reduz a incerteza."

Grau de atribuição idêntico ao original, zero travessão, e a frase respira.

## DoD reexecutado (não confiei em que "uma palavra não muda nada")

| Checagem | Resultado |
|---|---|
| travessões na seção t2 | **28 → 0** (objetivo do R1 mantido) |
| multiconjunto de citações | **IDÊNTICO** (44/44) |
| multiconjunto de números | **IDÊNTICO** (99/99) |
| travessão em título ou `\caption` | **0** |
| `é o espírito` / `no espírito` | 0 / 1 |

## O pedido, e é o motivo desta mensagem

**O hash mudou: `389f978` → `2438c68`.** A aprovação do revisor2 foi dada para
o hash antigo. Não quero que um gate suba com uma aprovação que, na letra, é de
outro objeto — mesmo sendo uma linha e sendo exatamente o que ele pediu.

Peço que ele **confirme essa única linha**. É `git diff 389f978 2438c68`, um
hunk. Se preferir, considere isto uma proposta de conserto e não uma alteração
consumada: reverter é trivial e o `389f978` já estava aprovado.

## Sobre a outra observação dele, que eu subscrevo

Ele descobriu que o próprio falso positivo ("um número perdido") veio de
**comparar janelas de linhas fixas** enquanto a branch crescia 3 linhas. É o
mesmo tipo de erro que eu cometi no t3 dele, com quebra de linha no meio da
frase procurada. **Dois verificadores, o mesmo erro de instrumento no mesmo
dia.**

Subscrevo a proposta dele de o critério exigir recorte por
`\section`/`\subsection` em vez de faixa numérica — e registro que as minhas
checagens já fazem assim desde o t3, justamente por isso. Se você quiser, eu
extraio o recorte por seção como função única para os dois usarem, em vez de
cada um ter a sua. É pequeno e evita a terceira ocorrência.
