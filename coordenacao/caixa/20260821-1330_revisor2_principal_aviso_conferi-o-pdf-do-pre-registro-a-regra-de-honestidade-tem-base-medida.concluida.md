---
de: revisor2
para: principal
tipo: aviso
assunto: conferi o PDF do pré-registro na fonte — a regra de honestidade do autor tem base medida, e há um detalhe de data
acao_esperada: repassar à banca ANTES de ela escrever as 12 ocorrências (é insumo da tarefa 20260821-1210); nenhuma ação minha pendente
referencia: `docs/pre-registro/` (LEIA-ME.md + 2022-05-31_apresentacao-aprendizado-ativo.pdf) · tarefa 20260821-1210 à banca · meu 20260820-2115, item "pré-registrado sem artefato"
criada_em: 2026-08-21T13:30
---

Este era o meu item (c) em aberto desde ontem — "12 ocorrências de
*pré-registrado* nos `.tex`, zero registro, nenhum documento". O autor
resolveu. Fui ao PDF antes que a banca escreva em cima dele, porque a regra
de honestidade que ele enunciou depende de um fato verificável, e vale
verificar em vez de repetir.

## A regra de honestidade se sustenta — medido

O LEIA-ME diz que a apresentação **não enuncia números específicos** (teto de
15%, gate de 85%, partições). Extraí o texto das 32 páginas e contei:

| termo | ocorrências |
|---|---|
| `15%` | **0** |
| `85%` | **0** |
| `partição`/`particao` | **0** |
| `teto` | **0** |
| `gate` | **0** |

E o que o LEIA-ME afirma que o documento **contém** também confere: `130`
(mil itens) 1× · `6 meses` 1× · `Settles` **9×** · `Fake` 4× · `SVC` 2× ·
`7.200` 2×.

**Um único percentual aparece no deck inteiro: `+70%`**, e é decorativo — está
num diagrama de fluxo (`OBTER → +70% → LIMPAR → VISUALIZAR`), a figura batida
de "a maior parte do trabalho é preparar dado". Registro para que ninguém o
encontre daqui a um mês e o tome por limiar pré-registrado.

Conclusão prática para a banca: **nenhuma afirmação numérica da tese pode se
apoiar neste PDF**. Ele sustenta a proveniência do *desenho* (laço de
aprendizado ativo, estratégias de seleção, lotes pequenos, Settles 2009) e a
*data*. Números continuam tendo de vir da qualificação ou do artefato de
experimento.

## O detalhe de data — para ninguém "corrigir" errado depois

O LEIA-ME diz "metadado do PDF: criado em 31/05/2022". Quem rodar `pdfinfo`
vai ler outra coisa:

```
CreationDate:  Wed Jun  1 01:16:57 2022 UTC
Title:         Microsoft PowerPoint - Aprendizado Ativo.pptx
Author:        ghdaru
Pages:         32
```

**As duas estão certas.** `2022-06-01 01:16 UTC` é `2022-05-31 22:16` no
horário de Brasília (UTC−3). O nome do arquivo e o LEIA-ME usam a data local,
que é a data do evento; o metadado bruto está em UTC e cai no dia seguinte por
uma hora e quinze minutos.

Digo isso porque é o tipo de discrepância que alguém encontra, acha que é erro
e "conserta" — renomeando o arquivo ou trocando a data no texto. **Não é
erro.** Se a tese citar a data, sugiro citar "31 de maio de 2022" e, se algum
lugar precisar do metadado, dizer que ele está em UTC.

## Nada pendente comigo aqui

Não editei nada. O item (c) sai da minha lista de espera do autor. Sigo
disponível para a cruzada do lastro do Cap.1 quando a banca entregar — é a
verificação que o autor já me atribuiu na mesma decisão.
