# Laudo: dry run LIDO do Cap.3 — metadiscurso encenado e registro acadêmico

- **Autor do laudo**: revisor1 · **Data**: 2026-08-24
- **Alvo**: `3-metodo/texto.tex` na main `@7974563`
- **Regra**: `docs/criterio-humanizacao.md`, seção "Metadiscurso: sóbrio sim, encenado não"
- **Natureza**: LAUDO. Nenhuma edição de `.tex`. Congelamento respeitado.

## Ponto de partida medido

`python3 scripts/checa-metadiscurso.py 3-metodo/texto.tex` → **saída vazia, exit 0**.
O capítulo **passa no verificador regex**. Tudo o que segue é, portanto, o que o
regex não alcança. Todas as reescritas sugeridas foram testadas e **passam** no
próprio `checa-metadiscurso.py`.

Cobertura: as dez seções foram lidas. Seções sem achado estão declaradas.

---

## 3.0 Abertura do capítulo

**A-01 · linha 13 · prioridade 1 (drama de necessidade)**
> "O custo de rotulagem que se quer reduzir **não chega de uma vez**: primeiro
> não há rótulo algum, depois cada rótulo consultado tem preço, e por fim as
> peças precisam funcionar juntas sob o mesmo orçamento."

Fere a forma 1 (drama). "não chega de uma vez" encena um enredo; "as peças"
é metáfora de quebra-cabeça. Teste (b): anuncia conteúdo, então vira forma sóbria.
**Sugestão**: "O custo de rotulagem tem três momentos: no início não há rótulo
algum; em seguida cada rótulo consultado tem preço; e por fim os componentes
operam juntos sob o mesmo orçamento."

**A-02 · linha 32 · prioridade 1 (apelo ao leitor / suspense)**
> "Definido o começo, cada rótulo passa a ter preço, e **a pergunta muda: quem
> fornece os rótulos, a que custo e com que perfil de erro?**"

Pergunta retórica dirigida ao leitor, respondida na frase seguinte. É a forma 2
em formulação nova; o regex não tem padrão para interrogação retórica.
**Sugestão**: "Definido o conjunto inicial, cada rótulo passa a ter preço. A
seção seguinte examina quem fornece os rótulos, a que custo e com que perfil de
erro."

**A-03 · linha 37 · prioridade 1 e 2**
> "**A pergunta final é o que o custo total compra**"

Pergunta encenada, e "o que o custo total compra" é registro comercial.
**Sugestão**: "O quarto pilar avalia o framework contra métodos de referência
sob o mesmo orçamento de rotulagem."

**A-04 · linha 43 · prioridade 2 (redundância com legenda)**
> "A Figura~\ref{fig:metodo-sequencia} **é o mapa dessa sequência, e cada seta
> se lê como uma dependência**: o que precisa estar resolvido antes do passo
> seguinte."

"cada seta se lê" instrui o leitor, e a oração final **repete quase literalmente
a legenda da própria figura** ("cada seta indica o que precisa estar resolvido
antes do passo seguinte"). Duplicação prosa/legenda.
**Sugestão**: "A Figura~\ref{fig:metodo-sequencia} apresenta essa sequência."
(a legenda já carrega a leitura das setas).

## 3.1 Desenho da pesquisa

**A-05 · linha 105 · prioridade 4 (âncora de identificador na prosa)**
> "**O E3 designa**, em toda a tese, a avaliação da hipótese central efetivamente
> executada."

A regra reserva identificadores `E*` para onde a função é localizar: tabela,
nota da tabela, §3.10. Esta frase é definição de identificador e cabe **na nota
da Tabela~\ref{tab:metodo-experimentos}**, que já define os demais.
**Sugestão**: mover a frase para a nota da tabela, sem alterar o texto.

## 3.2 Conjunto de dados

**Nada encontrado.** 3.2.1, 3.2.2 e 3.2.3 estão sóbrias. Registro positivo: o
jargão *multi-gold* é definido na própria nota de rodapé em que aparece, e
*CategorySchema* é definido na primeira ocorrência. É o padrão que a regra 3 pede.

**A-06 · linha 321 (3.2.4) · prioridade 1 (drama de necessidade)**
> "Uma consequência dessa escolha **deve ser registrada**: ..."

É a mesma manobra de "precisa ser dita", que o regex JÁ pega, em formulação
nova com "registrar". Passa incólume.
**Sugestão**: "Essa escolha tem uma consequência: ..." ou "Uma consequência
dessa escolha é registrada a seguir: ...".

## 3.3 Classificadores da tarefa

**A-07 · linha 379 · prioridade 1 e 2 (palco + personificação)**
> "Definido o material, **a peça seguinte é quem aprende com ele**."

"a peça seguinte" é metáfora de palco/quebra-cabeça (forma 3) e "quem aprende"
personifica o classificador. Teste (a): sai sem perda de conteúdo técnico.
**Sugestão**: "Esta seção define os classificadores da tarefa." — ou suprimir,
já que a seção seguinte é autoexplicativa.

## 3.4 Métricas de avaliação e análise estatística

**A-08 · linha 419 · prioridade 2 (metáfora recorrente)**
> "Esta seção **completa o terreno comum**"

Forma sóbria correta (sujeito + verbo), mas "terreno comum" é metáfora espacial
que reaparece da abertura. Severidade baixa.
**Sugestão**: "Esta seção define as métricas de avaliação e os instrumentos de
análise estatística."

**A-09 · linha 464 · prioridade 1 (título interrogativo)**
> "**\textbf{Em que fase cada métrica entra.}**"

Título em forma de pergunta encenada, no meio de uma série de títulos nominais
("Desempenho do classificador", "Análise estatística").
**Sugestão**: "\textbf{Uso das métricas por fase.}"

**A-10 · transversal · prioridade 2 (registro): a metáfora "régua"**
Ocorre em 3.2.4, 3.4 e 3.5.2 ("a régua é o Macro F1", "a régua muda de
natureza", "com a mudança de régua"). É informal para "critério de referência".
**Não sugiro troca automática**: pode ser escolha deliberada do autor, e é
consistente. Registro para decisão dele; se mantida, mantenha-se em todas as
ocorrências.

## 3.5 Composição do conjunto inicial

**A-11 · linhas 483--485 · prioridade 1 e 4**
> "Com dados, classificadores e métricas estabelecidos, **começa o processo de
> rotulagem, e ele começa pelo seu primeiro custo**: o conjunto inicial. **O
> primeiro pilar** responde a duas perguntas em sequência"

Encenação de início ("começa... e ele começa"), com repetição, mais âncora
`pilar-N` na prosa.
**Sugestão**: "Esta seção mede o primeiro custo do processo de rotulagem: o
conjunto inicial. Ela responde a duas perguntas em sequência: ..."

## 3.6 Partida a frio: DRI-SL

**A-12 · linha 541 · prioridade 4** — "esta, **o segundo pilar**, responde como
construir". Âncora `pilar-N` na prosa.
**Sugestão**: "esta seção responde como construir".

**A-13 · linha 546 · prioridade 2 (coloquialismo)** — "porque nenhum dos dois
isolado **dá conta**".
**Sugestão**: "porque nenhum dos dois espaços isolado é suficiente".

**A-14 · linhas 549 e 552 · prioridade 2 (personificação)** — "A densidade
semântica **cuida do primeiro**"; "A variedade lexical intragrupo **cuida do
segundo**".
**Sugestão**: "atende ao primeiro requisito" / "atende ao segundo".

## 3.7 LLMs como oráculo

**A-15 · linhas 566--567 · prioridade 1, 2 e 4 — o achado mais forte do capítulo**
> "Resolvido o custo de começar, **aparece o custo de continuar**: a cada
> iteração, **alguém precisa fornecer os rótulos**, a um preço. **É o terceiro
> pilar.**"

Acumula três violações: suspense ("aparece o custo"), personificação coloquial
("alguém precisa fornecer") e âncora `pilar-N`. Teste (a): sai inteira sem
perda de conteúdo técnico, porque a frase seguinte já diz o que a seção faz.
**Sugestão**: suprimir e começar em "A avaliação de oráculos exige, antes de
qualquer comparação, um instrumento de medição confiável."

## 3.8 O framework FALCO

**A-16 · linhas 673--674 · prioridade 1, 2 e 4**
> "O **quarto pilar** integra os anteriores no framework proposto e **pergunta o
> que o custo total compra**."

Pilar não pergunta (personificação); "o que o custo total compra" é registro
comercial e repete A-03.
**Sugestão**: "Esta seção integra os componentes anteriores no framework
proposto e descreve sua avaliação."

## 3.9 Ameaças à validade

**A-17 · linha 859 · prioridade 1 (drama de falta)**
> "Montado o processo inteiro, do dado ao veredito, **resta declarar** onde ele
> pode falhar"

"resta declarar" é primo direto de "falta a última peça", que o regex pega.
**Sugestão**: "Esta seção declara onde o processo pode falhar e o que foi feito
a respeito de cada risco."

## 3.10 Reprodutibilidade e ambiente

**A-18 · linha 919 · prioridade 2 (personificação leve)** — "a lógica científica
dos experimentos ... **vive** em um núcleo isolado".
**Sugestão**: "concentra-se em um núcleo isolado".

**Registro positivo, e vale ao autor como padrão**: esta seção resolve
exemplarmente a regra 3 (jargão). Ela introduz "arquitetura hexagonal" como
"o padrão de engenharia de software conhecido como...", e em seguida explica
"o que importa a esta tese é uma garantia: ...". É jargão de engenharia de
software apresentado a leitor de aprendizado de máquina do jeito certo.

---

## Resumo por seção

| Seção | Achados |
|---|---|
| 3.0 abertura | A-01, A-02, A-03, A-04 |
| 3.1 Desenho | A-05 |
| 3.2 Dados | **nada encontrado** (3.2.1–3.2.3); A-06 em 3.2.4 |
| 3.3 Classificadores | A-07 |
| 3.4 Métricas | A-08, A-09, A-10 (transversal) |
| 3.5 Composição de L0 | A-11 |
| 3.6 DRI-SL | A-12, A-13, A-14 |
| 3.7 Oráculo | A-15 |
| 3.8 FALCO | A-16 |
| 3.9 Validade | A-17 |
| 3.10 Reprodutibilidade | A-18 + registro positivo |

**18 achados.** Nenhum é pego pelo verificador atual. O padrão dominante não é
frase-feita, e sim **encenação estrutural nas aberturas de seção**: nove das dez
seções abrem com uma transição narrada ("Definido o começo...", "Resolvido o
custo de começar...", "Montado o processo inteiro..."). Individualmente cada uma
é leve; em sequência, criam o tom de narrativa que a regra combate.

## Proposta de padrões novos para `scripts/checa-metadiscurso.py`

Cobrem **6 dos 18** achados (A-02, A-03, A-06, A-07, A-15, A-17).

**Medido, não alegado**: rodei os cinco padrões sobre os oito arquivos `.tex` de
capítulo da tese (1-intro, 2-fundam, 3-metodo, 4-resultados-l0,
5-resultados-falco, 6-conclusao, resumo, abstract). Resultado: **6 disparos, e
os 6 são exatamente os achados acima. Zero falso positivo.**

```python
r"[Rr]esta (declarar|dizer|registrar|notar|mencionar)",          # A-17
r"deve(m)? ser (registrad|dit|mencionad|notad)[ao]s?\b",         # A-06
r"[Aa] (pergunta|questão) (muda|final é|seguinte é|agora é)",    # A-02, A-03
r"(a peça|o passo) seguinte é",                                  # A-07
r"[Aa]parece o custo|[Rr]esolvido o custo",                      # A-15
```

**Ressalva honesta sobre o alcance disso**: os cinco padrões pegam as
formulações que EU encontrei. O achado central deste laudo (a encenação
estrutural das aberturas) **não é capturável por regex**, porque não há frase
fixa: o que fere a regra é a função narrativa, não o léxico. Um verificador
regex não substitui a leitura, e sugerir o contrário seria vender falsa
segurança.

## Fora de escopo, e por quê

Não avaliei densidade, freeze nem compilação: a encomenda é de leitura. Não
editei `.tex`. As linhas citadas valem para a main `@7974563`; se o capítulo
andar, os números deslocam, mas as citações exatas continuam localizáveis.
