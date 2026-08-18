---
de: revisor2
para: principal
tipo: aviso
acao_esperada: pedir a verificação cruzada do revisor1 (§6 — quem executa não verifica) e levar ao gate em bloco; lock do 2-fundam LIBERADO neste push, então o senhor pode aplicar o pacote t1 quando quiser
referencia: tarefa 20260817-0640 item 1 · skill fight-the-pile-up · specs/009-r1-t3/qa-report.md
criada_em: 2026-08-17T07:05:00Z
---

# R1 do t3 ENTREGUE — `humanize/cap2-t3` @ `1dd5776`

Lock do `2-fundam/texto.tex` **liberado neste mesmo push**. A aplicação
centralizada do pacote t1 está desimpedida.

## Números, todos medidos

| Critério | Antes | Depois |
|---|---|---|
| travessões na faixa do t3 | **22** | **1** |
| códigos de experimento (E0, E0-P, E4, RQ3) | 7 ocorrências | **0** |
| chaves de citação | 26 | **26, idênticas** (`diff` vazio) |
| números de conteúdo | 10 | **10 presentes** |
| chaves LaTeX balanceadas | — | 100 = 100 |

O único travessão que sobrou é o de `humano--LLM`, que é grafia de termo
composto, não aposto encaixado. Mantido de propósito.

## As duas maiores quebras

O trecho do Gilardi/Pangakis era **uma frase de 15 linhas com quatro travessões
aninhados**; virou três parágrafos, um assunto cada: vantagens, limitações,
ressalva de escala. E o dos sistemas compostos era **uma frase de 16 linhas com
quatro desenhos e cinco travessões**; agora os quatro são anunciados e nomeados
em ordem. Nenhum fato mudou — só a forma.

## Sobre os códigos de experimento

Apliquei a receita que o pacote t1 já autorizou para os ciclos t3/t4 ("não
precisam de aprovação item a item"): cada `E0`/`E4`/`RQ3` virou referência ao
capítulo correspondente. Foram 7 ocorrências, incluindo a da l.631 que o pacote
citava nominalmente.

## Uma diferença numérica que registro antes que alguém a encontre

Um verificador de dígitos vai acusar que sumiram quatro "0", um "3" e dois "4"
da faixa. **Não é número de conteúdo**: são os dígitos dos próprios códigos de
experimento removidos. Deixei isso explicado no `qa-report.md` para ninguém
precisar refazer a conta para descobrir.

## Uma pendência que NÃO é minha rodada

`BERT` aparece sem expansão dentro do diagrama TikZ da Figura do ActiveLLM. Não
fui eu que introduzi, e mexer em rótulo de nó é alterar figura — fora do escopo
do R1. **Fica registrado para o R2 (siglas)**, que é a rodada dona desse
critério. Prefiro deixar anotado a corrigir por conta própria numa rodada que
não é a certa.

## Verificação cruzada

Não me verifico. Peço o revisor1 no diff — o que mais interessa conferir é se
alguma quebra de frase mudou sentido, porque é exatamente onde a humanização
pode errar sem parecer que errou.
