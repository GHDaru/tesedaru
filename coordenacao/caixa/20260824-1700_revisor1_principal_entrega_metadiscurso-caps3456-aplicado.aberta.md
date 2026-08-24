---
de: revisor1
para: principal
tipo: aviso
acao_esperada: integrar e levar ao gate do autor; três itens ficaram por decisão dele (listados no fim)
referencia: branch edicao/metadiscurso-caps3456-r1 @ cc49df5 · base main @9bfdfe0
criada_em: 2026-08-24T17:00:00Z
---

Identidade: **Revisor 01** (ADR 0011). Ordem do autor em conversa direta: passar
o dry run pelos Caps. 3, 4, 5 e 6 **e alterar**. Feito, entregue em branch.

## Antes de tudo: a main tinha andado

Atualizei e conferi. A main foi de `@7974563` para **`@9bfdfe0`**, e o **Cap.3
mudou 48 linhas** na auditoria do autor. Caps. 4, 5 e 6 intactos.

**Re-verifiquei os 18 achados do laudo do Cap.3 contra a main nova**, em vez de
aplicar às cegas: **2 já tinham sido corrigidos pelo autor** ("Em que fase cada
métrica entra" e parte da abertura da §3.5). Os demais continuavam, com as
linhas deslocadas. Trabalhei sobre a main nova.

## 30 correções aplicadas

| capítulo | correções |
|---|---|
| 3 (Metodologia) | 16 |
| 4 (Resultados L0) | 9 |
| 5 (Resultados FALCO) | 2 |
| 6 (Conclusão) | 3 |

**Por tipo:**

- **Encenação estrutural nas aberturas** (o padrão do Cap.3): §3.3, §3.5, §3.6,
  §3.7, §3.8, §3.9 e a abertura do capítulo passam à forma sóbria. Saíram *"a
  peça seguinte é quem aprende com ele"*, *"Resolvido o custo de começar,
  aparece o custo de continuar"*, *"resta declarar"*, *"Montado o processo
  inteiro"*.
- **Perguntas retóricas ao leitor**: *"a pergunta muda: quem fornece os
  rótulos...?"* e *"A pergunta final é o que o custo total compra"*.
- **Registro esportivo** (o padrão do Cap.4): *"A surpresa está no adversário"*,
  *"não é um competidor fraco"*, *"perde para"*, *"vence o otimizador"*,
  *"desfecho"*. **O conteúdo técnico sobreviveu inteiro** — que o AG é forte,
  tem acesso aos rótulos, custa 2.000 avaliações por cenário e ainda assim é
  superado continua dito, sem a moldura de disputa.
- **Autoelogio**: *"A reavaliação **honesta** revela..."* virou *"A reavaliação
  em partição intocada quantifica..."*. E no Cap.6 saiu *"Uma tese que termina
  com um número honesto ... vale mais que uma que termina com uma promessa"*,
  que era autoelogio comparativo e não carregava conteúdo.
- **Registro de gestão e comércio**: "alavanca", "o que o custo total compra",
  "não compra nada em média".
- **Tríade retórica** do fecho do Cap.6 (*"Começar bem / Perguntar bem / E pagar
  bem"*) virou *"Na partida a frio / Na seleção / E na rotulagem"*.

## Verificação

- **FREEZE exit 0 nos QUATRO capítulos**: números, `\cite`, `\ref`, `\label`,
  `\emph` e `\textbf` idênticos à main. Cap.3 com 251 números, Cap.4 com 220,
  Cap.5 com 559, Cap.6 com 63. **Nenhum número, tabela ou veredito tocado.**
- `checa-metadiscurso.py` sai **vazio** nos quatro.
- Dos **9 padrões que eu havia proposto** nos laudos, **zero ainda dispara**.
- **pdflatex+bibtex limpos**: 0 erro, 0 citação indefinida, 0 referência
  indefinida, 112 páginas.

Os dois laudos completos vão junto na branch (`docs/laudos/`), para o autor ver
o rastro de cada correção.

## Três coisas que NÃO apliquei, de propósito

1. **Mover a definição do E3** da prosa (§3.1) para a nota da tabela. É
   relocação estrutural, não reescrita, e mexe na tabela de rastreabilidade.
2. **A metáfora "régua"** (§3.2.4, §3.4, §3.5.2). É informal, mas consistente em
   todas as ocorrências e pode ser escolha deliberada do autor.
3. **"os achados sobrevivem a uma reexecução"** (Cap.4). Uso corrente em texto
   científico; eu mesmo desaconselhei mudar no laudo, e mantive a recomendação.

## Não verificado por mim

Princípio VI: a cruzada é do revisor2. Não mergeei na main.
