# QA — ciclo 009: R1 (humanização) do tema t3 do Capítulo 2

**Tarefa:** 20260817-0640 item 1 · **Executor:** revisor2 · **Branch:** `humanize/cap2-t3`
**Superfície travada:** `2-fundam/texto.tex`, APENAS a faixa do t3 (§2.3, "Modelos
de linguagem como oráculos de rotulagem").
**NÃO tocado:** a zona do t1 — por ordem da tarefa, o pacote t1 é aplicado pelo
principal de forma centralizada.
**Skill aplicada:** `fight-the-pile-up` (mapa skill→rodada do CLAUDE.md).

## Lei de ferro da skill, e o que ela proíbe aqui

> "Fix form, order and glossary; do **not** invent or remove facts."

Todo item abaixo é medição, não julgamento.

| # | Critério | Comando | Antes | Depois |
|---|---|---|---|---|
| 1 | Travessões na faixa (densidade de aposto encaixado) | `grep -o '—' \| wc -l` | **22** | **1** |
| 2 | Códigos de experimento no Cap. 2 (receita do pacote t1, item 4) | `grep -oE '\b(E0-P\|E0\|E1\|E4\|RQ[0-9])\b'` | 7 ocorrências | **0** |
| 3 | Chaves de citação | `grep -oE '\\cite[a-z]*\{...\}' \| sort -u` | 26 | **26, idênticas** (`diff` vazio) |
| 4 | Balanceamento de chaves LaTeX | contagem `{` vs `}` | — | **100 = 100** |
| 5 | `\citet`/`\citep` abertos sem fechar | regex multiline | — | **0** |
| 6 | Números de conteúdo preservados | busca item a item | — | **10 de 10 presentes** |

O critério 6 lista os números que a seção afirma: 25 pontos percentuais, 30
vezes menor, 27 tarefas, 0,5 de precisão/revocação, 248 categorias, 370 folhas,
42 vezes, 5.692 categorias, 15\% de ruído, meio milhão de títulos. **Todos
sobreviveram.**

## A única diferença numérica, explicada

O `diff` das contagens de dígitos acusa três mudanças: sumiram quatro "0", um
"3" e dois "4". **Não é número de conteúdo:** são os dígitos dos códigos de
experimento removidos pelo critério 2 — `E0` (quatro ocorrências), `RQ3` (uma) e
`E4` (duas). Registro aqui porque um verificador de números veria a diferença e
merece a explicação junto.

## O que mudou de forma (sem mudar o fato)

1. **Abertura da seção**: a lista dos quatro aspectos estava interrompida por um
   aposto entre travessões. Virou lista corrida + uma frase curta para o aspecto
   que a tese instrumenta.
2. **Parágrafo do Gilardi/Pangakis**: era UMA frase de 15 linhas com quatro
   travessões aninhados. Virou três parágrafos — vantagens, limitações,
   ressalva de escala — cada um com um assunto (item 1 da checklist).
3. **Roteamento do Rouzegar2024**: aposto entre travessões virou oração
   explicativa.
4. **Sistemas compostos**: era UMA frase de 16 linhas com quatro desenhos e
   cinco travessões. Virou "quatro desenhos" anunciados e depois nomeados —
   *o primeiro… o segundo… o terceiro… o quarto* (item 4: ordem que conta uma
   história).
5. **Ruído de rótulos**: quebra da frase do perfil de erro e da cautela do
   NoiseBench em períodos independentes.
6. **Custo e medição**: o aposto sobre erro de formato foi reposicionado para
   que a oposição "formato, não semântica" apareça antes do exemplo.
7. **Legenda da Figura ActiveLLM**: travessões → vírgulas.

## Sobre siglas (lei de ferro da skill)

`LLM` está expandida na primeira ocorrência da seção ("\textit{Large Language
Models} (LLMs)", l.483) e permanece. Não introduzi sigla nova. `BERT` aparece
apenas dentro do diagrama TikZ, como no original — não foi introduzida por mim,
e mexer no rótulo do nó é alterar figura, fora do escopo do R1; **fica
registrado para o R2 (siglas)**, que é a rodada dona desse critério.

## Pendência declarada

O único travessão remanescente é o de `humano--LLM` (composto com travessão
duplo do LaTeX), que é grafia de termo, não aposto encaixado. Mantido de
propósito.
