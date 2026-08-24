---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor junto com o laudo do Cap.3; decidir quais achados viram edição (a edição é do principal)
referencia: branch laudo/cap4-metadiscurso-r1 · docs/laudos/laudo-cap4-metadiscurso-revisor1.md
criada_em: 2026-08-24T16:00:00Z
---

Identidade: **Revisor 01** (ADR 0011). Encomenda do autor, em conversa direta:
passar o mesmo dry run no Cap.4. Mesmo protocolo do laudo do Cap.3.
**LAUDO apenas. Nenhuma edição de `.tex`.**

## Ponto de partida, medido antes de ler

`checa-metadiscurso.py 4-resultados-l0/texto.tex` sai **vazio, exit 0**. O
capítulo **passa** no verificador; tudo o que segue é o que o regex não alcança.
Todas as reescritas sugeridas passam no próprio verificador.

## O Cap.4 está sensivelmente melhor que o Cap.3

**11 achados em 307 linhas**, contra 18 em 946. E o padrão dominante é **outro**.
No Cap.3 era encenação estrutural nas aberturas de seção. Aqui é **registro de
competição e suspense na discussão do resultado central** (§4.3): o algoritmo
genético é tratado como adversário esportivo, com *"A surpresa está no
adversário"*, *"não é um competidor fraco"*, *"perde para"*, *"vence o
otimizador"*, *"desfecho"*.

**O achado mais forte** são as linhas 194–198, que acumulam encenação de surpresa
e registro esportivo. O conteúdo técnico (o AG é forte, tem acesso aos rótulos,
custa 2.000 avaliações por cenário e mesmo assim é superado) sobrevive inteiro
sem a encenação.

**O achado mais sutil** é a linha 280: *"A reavaliação **honesta**, porém, revela
a inflação da circularidade."* Qualificar a própria reavaliação de honesta é
autoelogio e, por contraste, imputa desonestidade ao protocolo anterior, que foi
apenas circular.

## Duas seções declaradas limpas

**4.2 e 4.5, sem achado.** A §4.2 vale como padrão a ser imitado: ela declara que
*"separar por completo estrutura de deriva de busca exigiria um controle de busca
aleatória de mesmo orçamento, que não foi executado"* — limitação declarada sem
drama e sem atenuar o próprio achado.

## Verificações que deram limpo, feitas e não presumidas

- **Regra 3 (jargão)**: fui conferir `conjunto-núcleo` e `envelope` antes de
  acusar. O primeiro **está** definido no Cap.2, com o inglês e a explicação
  junto; o segundo é introduzido no Cap.3. **Sem achado.**
- **Regra 4 (âncoras)**: **zero** identificadores `E*` no capítulo. Uma única
  `pilar-N`, e na função de roteiro que a regra admite.
- **Congelamento**: nenhuma sugestão toca número, tabela ou veredito.

Registrei também **um achado que recomendo NÃO mudar** (*"os achados sobrevivem
a uma reexecução"*, uso corrente em texto científico). Prefiro listar e
desaconselhar a omitir.

## Proposta para o verificador

Dois padrões novos. Não aleguei ausência de falso positivo: **rodei** sobre os
oito `.tex` de capítulo — **2 disparos, os 2 são exatamente os achados
relatados, zero falso positivo**.

Os outros **9 achados não são capturáveis por regex**. "adversário",
"competidor" e "alavanca" são palavras legítimas em outros contextos; um padrão
para elas geraria falso positivo em texto correto. O que fere a regra aqui é o
**registro**, não o léxico.
