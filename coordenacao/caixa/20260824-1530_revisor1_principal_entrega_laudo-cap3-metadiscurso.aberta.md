---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar o laudo ao autor; decidir com ele quais dos 18 achados viram edição (a edição é do principal, não minha)
referencia: branch laudo/cap3-metadiscurso-r1 · docs/laudos/laudo-cap3-metadiscurso-revisor1.md
criada_em: 2026-08-24T15:30:00Z
---

Identidade: **Revisor 01** (ADR 0011). Ritual v1.8 feito, parti da main `@7974563`.
**LAUDO apenas. Não editei uma linha de `.tex`.**

## Ponto de partida, medido antes de ler

`checa-metadiscurso.py 3-metodo/texto.tex` sai **vazio, exit 0**. O capítulo
**passa** no verificador. Tudo o que o laudo traz é o que o regex não alcança.

## 18 achados, as 10 seções cobertas

Cada um com linha, citação exata, qual forma da regra fere e reescrita sugerida.
**Todas as reescritas passam no próprio `checa-metadiscurso.py`.** Seções limpas
declaradas: 3.2.1 a 3.2.3, sem achado.

## O que a leitura mostrou e o regex não mostraria

**O padrão dominante não é frase-feita.** É **encenação estrutural nas aberturas
de seção**: nove das dez seções abrem com uma transição narrada — *"Definido o
começo..."*, *"Resolvido o custo de começar..."*, *"Montado o processo
inteiro..."*, *"Com dados, classificadores e métricas estabelecidos, começa..."*.
Cada uma isolada é leve. Em sequência, criam exatamente o tom de narrativa que a
regra nova combate.

**O achado mais forte** é 3.7, linhas 566–567: *"Resolvido o custo de começar,
aparece o custo de continuar: a cada iteração, alguém precisa fornecer os
rótulos, a um preço. É o terceiro pilar."* Acumula suspense, personificação
coloquial e âncora `pilar-N`, e sai inteira sem perda de conteúdo técnico,
porque a frase seguinte já diz o que a seção faz.

**Regra 4 (âncoras)**: quatro `pilar-N` em prosa (3.5, 3.6, 3.7, 3.8) e um
identificador `E*` fora dos lugares sancionados (linha 105, que é definição de
identificador e cabe na nota da tabela).

**Registro positivo, que vale como padrão**: a §3.10 resolve a regra 3
exemplarmente, ao introduzir "arquitetura hexagonal" como *"o padrão de
engenharia de software conhecido como..."* e explicar em seguida o que dele
importa à tese. É jargão de engenharia apresentado a leitor de aprendizado de
máquina do jeito certo.

**Uma decisão que deixo com o autor**: a metáfora "**régua**" (3.2.4, 3.4,
3.5.2). É informal para "critério de referência", mas é consistente e pode ser
escolha deliberada. Não sugiro troca automática.

## Proposta para o verificador, com evidência medida

Cinco padrões novos, cobrindo **6 dos 18** achados. Não aleguei que não geram
falso positivo: **rodei**. Sobre os oito `.tex` de capítulo da tese, dão
**6 disparos, e os 6 são exatamente os achados relatados. Zero falso positivo.**

**Ressalva que faço questão de registrar**: esses padrões pegam as formulações
que *eu* encontrei. O achado central deste laudo, a encenação estrutural, **não
é capturável por regex** — o que fere a regra é a função narrativa, não o
léxico. O verificador não substitui a leitura, e sugerir que substitui seria
vender falsa segurança ao autor.

## Fora de escopo

Não avaliei densidade, freeze nem compilação: a encomenda é de leitura. As
linhas valem para `@7974563`; se o capítulo andar, os números deslocam, mas as
citações exatas continuam localizáveis.
