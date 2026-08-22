---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) §6 das duas branches de harness: APROVO as duas, pode mergeiar. (2) R4 do Cap.5 entregue em modo auditoria: 8 achados em docs/r4-cap5-achados.md, para a banca aplicar no lote único. DOIS são de nível ALTO, e um deles é o MESMO gate da divergência nº1 da minha R4 do Cap.3 — peça à banca que trate os dois na mesma passada, senão conserta metade.
referencia: tarefas 0050 e 0330 · branches fcb2b21 e 7814389 · docs/r4-cap5-achados.md
criada_em: 2026-08-23T05:20:00Z
---

# 1. §6 — as duas branches de harness passam

Verifiquei como quem não executou, e não me contentei com "os testes passam".

| branch | DoD | exit REAL | merge |
|---|---|---|---|
| `harness/check-largura-tabela` @`fcb2b21` | `testa-largura-tabela.sh`, 14 casos | **0** | limpo |
| `harness/check-numero-sem-ficha` @`7814389` | `testa-numero-sem-ficha.sh`, 17 casos | **0** | limpo |

Não se sobrepõem em nenhum arquivo, então a ordem de merge é indiferente.
Merge conferido com `git merge --no-commit` real contra a `origin/main` em
worktree descartável, não `merge-tree`.

**Correção minha, antes que vire relato errado:** na primeira medição eu li
`exit 0` para o verificador do número-sem-ficha e quase reportei que ele não
bloqueia. Estava medindo o status do `tail` por causa do pipe. O verificador
sai **1** quando acha algo, que é o comportamento certo de um guarda. Terceira
vez hoje que um pipe me engana; passei a medir sem pipe.

**A parte que interessa, além do verde:** confirmei de forma independente as
duas afirmações centrais.

- **`check-largura-tabela`**: ele trocou os dois casos de dado real, que
  estavam amarrados ao estado do dia, por **revisões congeladas da história**.
  Fui conferir e as duas são exatamente o que ele diz — `01b78fd` é a minha
  Fase 2, com a tabela em `{llll}` (todas as colunas livres, o caso que
  estourava), e `96a28b2` é o meu conserto, com `p{63mm}`/`p{34mm}`. Testa os
  dois lados e vale para sempre. O diagnóstico dele é o certo: teste amarrado
  ao estado do momento mede circunstância, não comportamento.
- **`check-numero-sem-ficha`**: rodei o verificador contra a árvore real e
  confirmei a afirmação dele — **as superfícies novas (`apresentacao/`,
  `artigos/*/main.tex`) estão limpas** e o único achado do repositório segue
  sendo o do Cap. 1 (`Settles2009`/10%).

**Uma consequência do merge que você precisa saber:** por causa desse achado
do Cap. 1, o verificador sai **1 na árvore de hoje**. Se ele estiver ligado em
hook ou CI, **passa a bloquear** até que o 10% do Cap. 1 seja resolvido — de um
dos dois lados que a própria mensagem de erro oferece. Não é defeito da branch;
é o efeito de mergeiá-la. Melhor decidir isso antes do que descobrir depois.

# 2. R4 do Cap. 5 — 8 achados, modo auditoria

Lista completa em `docs/r4-cap5-achados.md`. **Não editei uma linha do
capítulo**, como você pediu. Método idêntico ao do Cap. 3: varri 15 gatilhos
(7 conectivos causais, 3 generalizações, 5 verbos fortes), li cada um em
contexto e confrontei com a tabela ou o artefato.

**Nenhuma afirmação órfã.** O capítulo é disciplinado, e o fecho da varredura
de orçamento tem hedging exemplar. Os achados são de **força excessiva** e de
**mecanismo afirmado sem medição**.

## Os dois ALTOS

**(1) A conclusão do pilar é provada com gabarito e atribuída ao FALCO.** O
texto conclui que *"o FALCO atinge o critério dentro do teto de rotulagem"*.
Mas os braços que cruzam (E20–E35) usam **gabarito** — o próprio texto declara
— e o FALCO usa **oráculo LLM**, cujo custo está medido no mesmo capítulo em
**7,2 p.p.** (A vs.\ B). Aplicada ao braço que cruza (E20, 0,858), essa
penalidade dá ≈0,786, **abaixo** do critério de 0,843. O dado sustenta que *o
critério é atingível naquele volume com rótulos perfeitos* — não que o FALCO o
atinja. O texto reconhece a pendência na oração seguinte, mas a frase-conclusão
já afirmou o que a ressalva relativiza, e é ela que a banca lê em voz alta.

**(2) O gate atribui um papel por um critério cuja restrição falhou.** O
critério pré-registrado define *LLM Inicial* como melhor razão acurácia/custo
**sujeito a acurácia mínima de 85%**. O Cap. 5 diz *"nenhum oráculo atinge
≥ 85%"* e, três linhas abaixo, nomeia *LLM Inicial = deepseek-v4-flash
(78–82%)*. A restrição que define o papel não foi satisfeita, e o papel foi
atribuído assim mesmo, sem a declaração de divergência do princípio VI. Não é
preciso mudar a decisão: é preciso dizer que a regra foi relaxada.

**Este é o MESMO gate da divergência nº 1 da minha R4 do Cap. 3** (onde o
racional está invertido: 85% está 4,56 p.p. *abaixo* do baseline de 89,56%, não
acima). Some ainda o achado do revisor2 de que esse baseline foi medido em
**795 categorias** e a tese opera com 621. **São três defeitos no mesmo
critério, em dois capítulos.** Peça à banca que trate o conjunto numa passada
só; consertar um de cada vez produz três idas ao gate.

## Um atalho para os achados 6 e 7

Dois achados de mecanismo ("rotular tudo pode piorar" e o viés do Macro F1
interno) apoiam-se na **mesma** proposição não medida: a amostra ativa seria
mais balanceada / sobre-representaria classes raras. Os efeitos estão medidos;
a proposição, não. **Uma única medida fecha os dois**, e é barata — os
`labeled_idx` já estão salvos nos `*_state.json` do E6, então a distribuição de
classes da amostra ativa sai sem re-executar nada. Vale pedir o número antes de
a banca reescrever qualquer um dos dois.

## O que verifiquei e NÃO é achado

Registro para ninguém "consertar" o que está certo: a frase *"nenhum oráculo
sustentaria o critério sob a política de parada executada"* **se sustenta** — B
(gabarito, mesmo *n*) dá 0,777 e E dá 0,816, ambos abaixo de 0,843, e gabarito
é o teto de qualquer oráculo. Um parecer anterior a listou como excedida;
pelos números de hoje, não está. A qualificação final é o que a torna correta.
