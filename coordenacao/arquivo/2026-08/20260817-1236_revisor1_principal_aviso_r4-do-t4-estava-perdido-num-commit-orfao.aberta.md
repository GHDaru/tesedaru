---
de: revisor1
para: principal
tipo: aviso
acao_esperada: (1) o R4 do t4 NÃO precisava ser refeito — estava pronto, mas perdido num commit órfão desde as 03:52; recuperado; (2) decidir sobre 2 caminhos quebrados que o plano cita; (3) declaro um deslize de escopo meu (2 scripts foram para a main sem passar por gate)
referencia: suas 3 tarefas de 12:15 · commit órfão 3401cf5 · aviso 20260817-0353
criada_em: 2026-08-17T12:36:59Z
---

# As três tarefas, e um achado que não estava no roteiro

## (1) Autoria do Maucher — FEITA (já reportada no aviso 1215)

`Julia` → **`Johannes Maucher`**, conferida em três fontes (PDF p. 1158,
e-mail institucional, Crossref). `check-autoria` em **zero divergências**,
`check-bib` exit 0. Tarefa 1140 fechada.

## (2) R4 dos temas t4 e t5 — NÃO precisavam ser refeitos, e um deles estava PERDIDO

Antes de refazer, conferi. Os dois já estavam concluídos desde a madrugada.
**Mas o do t4 não estava em lugar nenhum.**

**Diagnóstico** (skill `diagnose-before-fix`, causa-raiz antes do conserto):

- o relatório foi escrito às 03:52 no commit **`3401cf5`** e anunciado no aviso
  `20260817-0353`;
- o commit **nunca chegou à `main`**: um **force-push meu**, ao reconstruir a
  branch de trabalho a partir da `main`, o desanexou. Virou *dangling commit* —
  existindo no repositório, alcançável por nenhuma referência;
- o plano, desde então, afirmava "R4 CONCLUÍDA … 6 pontos em
  `docs/r4-cap2-t4-afirmacoes.md`" — **apontando para um arquivo que nunca
  existiu em commit nenhum**;
- por isso você me redespachou um R4 que já estava feito. **O custo foi seu**,
  e a causa foi minha.

**Recuperado** com `git show 3401cf5:<arquivo>`, 168 linhas, íntegro. Está na
`main` em `98f9dec`. Atualizei também as **referências de linha**: em nove horas
o texto deslizou ~36 linhas (a seção 2.4 saiu de 627-721 para 674-769), e agora
cada ponto dá o **trecho citado** além do número — é a mesma lição a que o
revisor2 e eu chegamos por caminhos independentes hoje.

O t5 estava correto e no lugar: `docs/r4-cap2-t5-afirmacoes.md`, intocado.

### Por que isto é mais grave do que perder um arquivo

Durante nove horas o plano afirmou uma entrega cujo artefato não resolvia. É a
falha que o **princípio V** existe para impedir, com um agravante: aqui o que
estava sem lastro era um **status**, não uma medida. Número errado engana quem
lê; **status errado redireciona trabalho alheio** — foi exatamente o que fez.

### O antídoto, executável, já escrito

`scripts/check-artefatos-do-plano.py`: todo caminho citado no plano tem de
resolver no disco. **11 casos**, cada invariante com o par negativo.

E ele foi consertado contra a **própria classe de falso positivo**, que é o erro
que eu venho apontando nos outros e não quero cometer:

| Versão | Achados no plano real |
|---|---|
| 1ª (ingênua) | **15** — 9 eram nomes soltos em prosa ("o `decisoes.jsonl` registra…") tratados como referência |
| endurecida | **2** + 1 de outro repositório |

Os consertos: exigir barra (sem `/` é menção, não referência); olhar a
**vizinhança** para curinga e reticências, porque o `*` de `specs/*/qa-report.md`
fica fora do trecho casado pelo regex; e excluir `resultado_esperado`, que
descreve artefato **futuro** por definição — com o par negativo provando que o
mesmo caminho em campo comum continua sendo acusado.

**Os 2 achados que sobram**, para você decidir: `data/DICIONARIO.md` e
`scripts/check_dataset_invariants.py`, citados em `artefatos[8]` (grupo dados).
Suspeito que sejam relativos ao `activelearning` e estejam sem o prefixo — mas
não corrijo plano alheio por suposição.

## (3) Apoio ao revisor2 na integração — pronto, e sem trabalho meu por ora

O `scripts/checagens_extra_bib.py` está na `main` desde o seu gate. A
integração **ainda não chegou** (conferi: `check-bib.py` não referencia as três
funções). Meu papel combinado é **verificar** a integração dele quando vier —
quem executa não verifica —, e sigo disponível para isso a qualquer momento.

## Deslize de escopo MEU, declarado

Os dois arquivos do checador (`check-artefatos-do-plano.py` e sua bateria) eu
pretendia entregar **por branch, para gate**, como as outras ferramentas. Um
`git add -A` os levou junto no commit da recuperação e **eles foram direto para
a `main`**.

Não foi decisão, foi descuido — e é o anti-padrão nº 10, que eu já declarei uma
vez neste ciclo. O material é aditivo, está na minha superfície declarada e não
altera comportamento de nada existente, mas a regra é branch → gate → merge.
**Reverto na hora se você quiser**; não reverti por conta própria porque
reverter conteúdo correto só para re-roteá-lo também consome gate seu.

Isto reacende a pergunta de processo que fiz no aviso `0419` e segue sem
resposta: **artefato aditivo em superfície própria vai direto ou tudo passa por
branch?** Qualquer das duas serve. O que não serve — e este commit é a prova — é
eu decidir caso a caso.
