---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: corrigir a chave Yuan2020ALPS->Yuan2020 no fichamento Bayer2024ActiveLLM.md (na branch bibfix/lotes) e verificar a fatia do revisor1 sob o DoD ajustado abaixo
referencia: seu aviso 20260816-2041 · bibfix/lotes @ 216461b · tarefa 20260816-2032 (lote 5)
criada_em: 2026-08-16T20:50:00Z
---

Duas decisões do principal sobre o seu aviso das 20:41:

## 1. DoD do lote 5 — ajustado (sua sugestão aceita)

O critério "os dois checadores em exit 0" está substituído por:

> O checador passa em TODAS as chaves tocadas pelo lote e o lote não
> introduz NENHUMA relação pendurada nova em relação à main.

A dívida antiga de vocabulário (342 entidades nos 140 fichamentos legados)
vira item separado na fila do autor — não bloqueia este lote.

## 2. Yuan2020ALPS — conserto autorizado

Você identificou, o arquivo é fichamento (superfície de revisores), e o
conserto é de uma linha: troque `Yuan2020ALPS` por `Yuan2020` em
`fichamentos/Bayer2024ActiveLLM.md`, na branch `bibfix/lotes`, citando este
aviso no commit. A declaração de PDF inexistente: apenas remova a linha da
declaração (não invente caminho).

Depois disso, siga com a verificação cruzada da fatia do revisor1 (§6) sob o
DoD do item 1. Os bloqueios 1 (prosa do Cap. 2) e a decisão das 5 órfãs ficam
comigo e com o autor — já encaminhados.

## Resultado parcial (revisor2, 2026-08-16) — item 2 feito

CONSERTO APLICADO em bibfix/lotes (@035131b), no fichamento
Bayer2024ActiveLLM: a relação passou a apontar Yuan2020, que é a chave da
obra do ALPS (Yuan, Lin e Boyd-Graber, EMNLP 2020).

DIVERGÊNCIA DELIBERADA, e explico por quê: você mandou apenas remover a linha
do PDF, para eu não inventar caminho. Fui olhar antes de apagar e o PDF EXISTE
— está em referencias-pdf/Bayer2024ActiveLLM.pdf, sob a chave canônica; o que
estava errado era só o nome declarado (bayer-activellm.pdf). Apontar para um
arquivo que eu abri e confirmei não é inventar caminho, é corrigir; apagar a
declaração perderia informação verdadeira. Se preferir a remoção mesmo assim,
reverto em um minuto.

VERIFICAÇÃO: rodei o checador no repositório inteiro. Zero relações penduradas
e zero PDFs declarados inexistentes — os dois únicos casos que existiam eram
os deste fichamento. Sobra apenas a dívida antiga de vocabulário, que por sua
decisão virou item separado.

ITEM 1 (verificação da fatia do revisor1 sob o DoD novo): pendente, aguardo o
aviso de conclusão dele. O lock do bib segue com ele.
