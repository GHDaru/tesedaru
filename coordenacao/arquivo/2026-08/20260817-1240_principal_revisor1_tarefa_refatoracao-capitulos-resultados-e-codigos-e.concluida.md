---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: TRABALHO GRANDE, em 2 fases — FASE 1 (agora): diagnóstico + proposta de refatoração, SEM editar prosa, entregue ao principal para decisão do autor; FASE 2 (só após o gate): execução, com exceção nominal de superfície concedida pelo autor
referencia: ordem do autor 2026-08-17 ("tenho dois capítulos de resultados? a notação EXXX é controle interno, não importa ao leitor; precisamos refatorar") · seu docs/uso-declarado-vs-citacao-real.md · check-uso-declarado.py
criada_em: 2026-08-17T12:40:00Z
---

# Refatoração: dois capítulos de resultados + expurgo da notação de experimento

Ordem direta do autor. Você foi escolhido por já ter a ferramenta e o mapa
(a varredura uso-declarado × citação real e o `check-uso-declarado.py`).
Esta tarefa tem prioridade sobre o R4 de t4/t5, que fica para depois.

## O diagnóstico que o principal já mediu (ponto de partida, confirme)

| Fato | Número |
|---|---|
| Cap. 4 (L0, pilares P1-P2) | 207 linhas · **1.442 palavras** · 5 seções · **zero códigos E** · zero citações |
| Cap. 5 (oráculos + FALCO, P3-P4) | 619 linhas · **4.973 palavras** · 7 seções · 61 códigos E |
| Códigos de experimento na tese inteira | **224 ocorrências** (Cap.3: 63 · Cap.5: 61 · Cap.6: 22 · declaração de IA: 7 · Cap.2: 2) |

Dois problemas distintos, que a proposta deve tratar separados:

**(A) Assimetria dos capítulos de resultados.** Um tem 1/3 do tamanho do
outro e nenhuma citação. Ou os dois viram um capítulo único de resultados
organizado por pilar (P1-P2 / P3-P4), ou o Cap. 4 é reforçado para justificar
existir sozinho. Não decida: MEÇA e apresente as opções com consequências
(estrutura de sumário, remissões cruzadas afetadas, impacto nos apêndices).

**(B) Notação EXXX é controle interno.** O leitor não precisa saber que a
avaliação de oráculos se chama "E0". A regra que o autor quer: o texto fala
o que foi feito, não o código do experimento. Mas ATENÇÃO — a proposta
precisa resolver como preservar a rastreabilidade que os códigos dão hoje.
Sugestão de partida (avalie e melhore): os códigos migram para UMA tabela do
Cap. 3 (mapa experimento → seção de resultados → artefato) + o apêndice de
reprodutibilidade, e somem da prosa corrente; a tabela é a ponte para os
notebooks auditáveis do executor01.

## Fase 1 — o que entregar (nenhuma linha de prosa editada)

`docs/plano-refatoracao-resultados.md` com:
1. inventário completo das 224 ocorrências, classificadas em: prosa
   corrente (some) · tabela/legenda (migra) · rastreabilidade legítima (fica,
   com justificativa);
2. as 2 ou 3 opções de estrutura para (A), com prós, contras e custo em
   número de remissões a ajustar (`\ref`, `\label`, sumário, apêndices);
3. sua recomendação, explícita, com o porquê;
4. lista de efeitos colaterais: o que quebra (labels, referências cruzadas,
   o kanban do plano, o site) e como o plano previne cada um;
5. estimativa de esforço por fatia, para o autor decidir se vai de uma vez
   ou por partes.

## Fase 2 — execução (só depois do gate do autor)

Exceção nominal de superfície: você edita prosa nesta refatoração (como a
banca fez no Cap. 1), em branch própria, por fatias pequenas, com
verificação cruzada do revisor2 e gate do principal a cada fatia. O
`check-uso-declarado.py` vira o DoD: zero código E fora dos lugares
autorizados pelo plano aprovado.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
