---
de: revisor1
para: principal
tipo: aviso
acao_esperada: branch atualizada para @f069543 — o autor mandou passar as diretrizes de tom JÁ, e apliquei antes do gate; peça ao revisor2 a reconfirmação (3 títulos + 2 propagações) e leve ao gate
referencia: ordem direta do autor 2026-08-17 · edições dele no pacote t2 (tarefa 1005 da banca) · branch refatora/resultados-f1-f2 @f069543
criada_em: 2026-08-17T15:30:43Z
---

# Diretrizes de tom aplicadas ANTES do gate, por ordem do autor

Ele foi direto: *"nos seus gates de retrabalho do Capítulo 5, já pode passar as
diretrizes já, pois senão terá retrabalho depois."* Apliquei na branch em vez de
deixar para a próxima leitura.

## Os três títulos que não passavam na régua

| Antes | Agora |
|---|---|
| O *prompt* é parte do instrumento, **não um detalhe de implementação** | O *prompt* como variável do instrumento de medição |
| Seleção sob oráculo perfeito: **o teto do que o método pode render** | Seleção sob oráculo perfeito: limite superior do método |
| **O veredito** do classificador forte sobre a hipótese central | Avaliação da hipótese central com o classificador forte |

Os outros quatro já estavam conformes.

## Duas propagações que a varredura revelou

Aplicar a régua **aos dois arquivos**, e não só onde eu esperava, encontrou o
que uma troca de títulos isolada teria deixado para trás:

1. **A linha do E3' na tabela-mapa do Cap. 3** repetia "veredito" — teria ficado
   inconsistente com o título que acabei de limpar.
2. **A frase de abertura do resultado do E3', no Cap. 5**: *"O **veredito** da
   hipótese central é negativo"* → *"A hipótese central **não se confirma** na
   configuração executada"*. Estava a dois parágrafos do título; deixá-la seria
   **mudar a metáfora de lugar, não removê-la**.

## A régua virou critério vinculante no plano (§7)

Derivada das quatro edições do autor, com a regra que cada uma fixa:

| Ele trocou | Regra |
|---|---|
| "poderoso" → "funciona **quando** o espaço tem estrutura conhecida" | adjetivo avaliativo → **condição em que vale** |
| "inevitável" → "necessário na prática" | absoluto → qualificado |
| "cardápio" → "oferta" | metáfora → termo literal |
| "eventualmente" → "possivelmente" | falso amigo (em português é *de vez em quando*) |

**Vale para F3, F4, F5 e F7**, e a mensagem de entrega de cada fatia declarará
quais regras foram acionadas.

## A distinção que eu quase errei, e que vale mais que a regra

Ao varrer as metáforas, encontrei **"teto" 11 vezes** e ia proibi-lo. Fui olhar
antes: **todas são termo técnico** — "teto supervisionado", "teto de medição
($\approx 99{,}3\%$)", "teto de significância". Limite superior de uma medida
**se chama teto** em português técnico.

Então o critério não é a palavra, é a função: **figura que substitui o termo
próprio sai; termo consagrado do campo fica.** Uma lista de palavras proibidas
aplicada sem esse filtro produziria exatamente a classe de falso positivo que
venho perseguindo nos checadores — e por isso o item 1 da régua diz "metáfora
**decorativa**", com a distinção escrita por extenso. Registrei também que os
itens 2 a 4 **não são automatizáveis**: checagem que promete julgar tom mente.

## DoD sobre TODOS os arquivos do diff

| Checagem | Resultado |
|---|---|
| `\label` idênticos (Cap. 3 e Cap. 5) | **sim, nos dois** |
| citações idênticas | **sim, nos dois** |
| `\ref` perdidas | **nenhuma** |
| `\ref` sem `\label` (viraria `??`) | **nenhuma** |
| metáforas decorativas (cardápio / veredito / espinha) | **0, 0, 0** |
| "teto" técnico preservado | **11 intactas** |
| travessão Unicode em título | **nenhum** |

**Um item que reporto como escopo, não como defeito**: 4 títulos do Cap. 3 ainda
têm código E (`Pilar P3: … (experimento E0)`, `Desenho fatorial do E0`, …). São
da **fatia F4** e estão fora desta entrega. Aparecem porque rodei a checagem no
arquivo inteiro, e prefiro relatá-los a deixar que pareçam esquecidos.

## Estado

Branch em **`@f069543`**. Hash mudou depois da aprovação do revisor2 — peço que
ele **reconfirme os três títulos e as duas propagações**; é um `git diff
d14e55e f069543`.
