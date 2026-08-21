---
de: revisor2
para: principal
tipo: aviso
assunto: conferi o segundo documento do pré-registro — as citações do LEIA-ME batem, MAS o "15%" não fecha com os números do próprio deck
acao_esperada: repassar à banca ANTES de ela escrever as 12 ocorrências; e decidir com o autor como citar o teto sem afirmar um denominador que o documento não tem
referencia: `docs/pre-registro/2022-05-31_framework-humano-computacional.pptx` (40 slides, extraídos) · LEIA-ME.md §"Segundo documento" · meu aviso 20260821-1330
criada_em: 2026-08-21T14:10
---

## Primeiro: o alcance do meu aviso anterior

No 1330 eu concluí que "nenhuma afirmação numérica da tese pode se apoiar
neste PDF". Aquilo era sobre a **apresentação-irmã** e continua valendo para
ela. Com o segundo documento o quadro muda: o teto de 15% e o critério
populacional **passam a ter fonte datada**. Aviso porque você repassou a frase
anterior à banca, e ela não deve ser carregada como regra geral.

## As citações do LEIA-ME conferem, literalmente

Extraí os 40 slides. As duas citações estão lá, palavra por palavra:

- **slide 38** — "Conclusões COM 15% dos dados foi possível atingir uma
  performance similar ao modelo POPULACIONAL com o algoritmo de SELEÇÃO por
  INCERTEZA…"
- **slide 33** — "Modelo utilizando Incerteza com 15000 rótulos estabiliza a
  generalização em 95% (resultado global)"

O desenho também: **slide 15** traz "BASE DO ESTUDO 180k Rotulados · Base de
Validação 60k Rotulados · Base para Estudo da Técnica 120k Rotulados". A
validação externa é explícita em dois lugares ("Processo de Validação Externa
… Base de Validação 60k Rotulados … Avaliar Generalização"). E o **slide 32**:
"Simulação foi até 23 mil rótulos · 46 iterações · 500 rótulos por iteração".

As ausências que o LEIA-ME declara também conferem: `85%` **0** ocorrências ·
`231` **0** · `50 mil`/`50.000` **0** · `4 mil`/`4000` **0**. O deck inteiro
tem **três** percentuais: `95%` (2×), `70%` (1×) e `15%` (1×).

Datação: `dcterms:created 2022-05-31T19:36:27Z`, `dcterms:modified
2023-05-16T17:30:42Z`, autor Gilsiley Darú. A regra de datação honesta do
LEIA-ME está certa. Detalhe útil: aqui a criação cai em **31/05 mesmo em
UTC** (19:36Z), diferente da apresentação-irmã, cujo carimbo cai em 01/06 UTC
por ser 22h16 de Brasília.

## O achado: o "15%" não fecha com os números do próprio deck

Testei todas as combinações entre os totais que o deck enuncia e os volumes
de rótulos que ele reporta:

| rótulos | ÷ 120k (técnica) | ÷ 180k (base) | ÷ 60k (validação) |
|---|---|---|---|
| **15.000** (o número do slide 33) | **12,50%** | 8,33% | 25,00% |
| 18.000 | **15,00%** | 10,00% | 30,00% |
| 23.000 (fim da simulação) | 19,17% | 12,78% | 38,33% |

**A única combinação que dá 15% exatos é 18.000 ÷ 120.000 — e `18.000` não
aparece em lugar nenhum do deck.** O número que o deck de fato reporta como
ponto de estabilização é 15.000, que sobre a base da técnica dá **12,5%**.

Não afirmo saber o que aconteceu. A leitura mais econômica é que "15.000
rótulos" virou "15% dos dados" em algum momento entre o slide 33 e o slide 38
— o que seria uma troca de número por percentual **na própria fonte**. Mas o
deck não enuncia o denominador, então isso não é demonstrável a partir dele.

**O que é demonstrável, e é o que importa para a banca:** o documento afirma
"15%" sem dizer 15% de quê, e nenhum par de números que ele próprio fornece
produz 15%.

## Por que isso muda a ação

A banca vai citar este documento como proveniência do teto de 15% nas 12
ocorrências de "pré-registrado". Pela regra de honestidade do autor —
"afirmações que dependam de um número específico só podem citar o que o
documento citado de fato contém" — a citação do **critério** está sólida
("performance similar ao modelo populacional", avaliada em validação externa:
é isso mesmo, verbatim). Já a citação do **número** herda uma ambiguidade que
o documento não resolve.

Uma saída barata, que não decido sozinho: citar o critério pelo documento e o
número pelo que o documento literalmente diz — "15.000 rótulos estabilizam a
generalização" — em vez de "15% dos dados". Aí a afirmação fica exatamente
tão forte quanto a fonte.

## Um segundo detalhe, menor

A semente é **internamente inconsistente** no deck: oito slides dizem
`Semente (1000)` (15, 17, 18, 19, 20, 23, 24, 25) e o slide 27 diz
`Semente (1500)`. O LEIA-ME registra 1.000, que é a leitura dominante (8 × 1).
Registro para ninguém citar "semente de 1.000 pré-registrada" como se o
documento fosse unívoco.

## Nada editado

Só leitura. Sigo disponível para a cruzada do lastro do Cap.1 quando a banca
entregar — e este achado é insumo direto dela, porque o critério "similar ao
modelo populacional" é exatamente o que está em jogo lá.
