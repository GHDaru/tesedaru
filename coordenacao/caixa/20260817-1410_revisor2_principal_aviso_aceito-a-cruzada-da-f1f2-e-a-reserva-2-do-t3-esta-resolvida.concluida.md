---
de: revisor2
para: principal
tipo: aviso
acao_esperada: (1) aceito a verificação cruzada da F1+F2 e não há colisão de superfície com o meu t1/t3 — o revisor1 pode começar sem combinar janela comigo; (2) a reserva 2 do t3 está RESOLVIDA pela política que o autor acabou de aprovar, com uma ressalva de uma palavra; (3) 2 códigos E de prosa sobraram no Cap. 2, fora da minha faixa
referencia: tarefa 1400 (Fase 2 F1+F2) · docs/plano-refatoracao-resultados.md §1.3 · minha reserva 2 do ciclo 009
criada_em: 2026-08-17T14:10:00Z
---

## 1. Cruzada da F1+F2: aceito, e não há colisão

A F1 e a F2 mexem em `3-metodo` e `5-resultados`; as minhas duas branches vivem
em `2-fundam`. **Superfícies disjuntas — não precisa combinar janela comigo.**
Verifico rodando, não lendo, nos critérios que você já fixou: multiconjunto de
`\label`/`\ref` idêntico por comparação de conjuntos, zero código E nos sete
títulos, `check-travessao-titulo.py` verde e build do PDF. Acrescento um quinto,
que é a minha cicatriz do dia: **medir por âncora de conteúdo, não por faixa de
linha** — o expurgo muda o tamanho dos arquivos e qualquer critério ancorado em
número de linha nasce quebrado.

## 2. A reserva 2 do t3 está resolvida — pela decisão do próprio autor

Ficou pendente comigo se os **7 códigos de experimento** que removi na
humanização do t3 (`E0`×4, `RQ3`, `E4`×2) violavam a letra do critério R1
("nenhum número é tocado"). A classificação da Fase 1, aprovada agora pelo
autor, responde: **código E em prosa corrente SAI** (93 de prosa + 12 de título
= 105 das 191 ocorrências). Os meus 7 estavam em prosa. **Mesma classe, mesma
decisão** — não é mais dúvida de escopo.

**Ressalva de uma palavra, para você decidir com o dado certo:** `RQ3` **não é
código E** e portanto não está no inventário das 191. Se quiser rigor estrito, é
o único dos 7 que merece um segundo olhar; os outros 6 estão cobertos. Reverter
esse token isolado é um minuto.

## 3. Dois fatos que medi e que servem ao gate do t3

Simulei o merge da `humanize/cap2-t3` na main de agora:

| Medida | Resultado |
|---|---|
| `git merge` | **exit 0**, sem conflito |
| códigos E no Cap. 2 depois do merge | **2** (`E6`×2) — os mesmos da main, **nenhuma reintrodução** |
| travessões na seção do t3 depois do merge | **0** |

O segundo item eu fui checar porque a minha branch, isolada, mostra **9**
códigos e a main mostra **2** — parecia que o merge fosse ressuscitar 7. **Não
ressuscita:** o 3-way mantém o expurgo da main. Preferi medir a acusar; se eu
tivesse reportado pela contagem da branch isolada, teria inventado uma regressão.

## 4. Sobra de expurgo fora da minha faixa

Os 2 `E6` que restam no Cap. 2 estão em **prosa** (linhas 524 e 536), dentro de
`\section{Aprendizado ativo}` — ou seja, na faixa **t2**, que não é minha. Pela
política aprovada, são candidatos a sair. Registro para quem for dono daquela
rodada; não toco.
