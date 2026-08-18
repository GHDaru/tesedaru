---
de: banca
para: principal
tipo: tarefa
acao_esperada: (1) tomar ciência do R6 do t3 já aplicado na main por autorização do autor (ebb1f65); (2) INCLUIR os 4 itens R6 de t4/t5 abaixo no trem de aplicação que já vai rodar DEPOIS do merge da branch 25390a3 (R1 t4+t5), junto com os 23 itens de registro — mesma superfície, mesma janela, um gate só; (3) levar ao autor a decisão AL×AA
referencia: autorização do autor em conversa com a banca ("aplicar R6, pode fazer para o que falta do capítulo 2") · branch 25390a3 aprovada na cruzada f110ee3 · relatório docs/re-revisao-registro-t4-t5.md
criada_em: 2026-08-17T13:10:00Z
---
R6 DO QUE FALTAVA DO CAP. 2 — EXECUTADO EM DUAS PARTES para não conflitar
com a branca do R1 t4+t5 que aguarda gate.

PARTE APLICADA (t3 + listas, zonas livres, commit ebb1f65):
- Glosas na 1ª ocorrência: zero-shot, cross-task, few-shot (todas nascem na
  2.3 e nenhuma tinha glosa em português);
- "o survey clássico" -> "a revisão clássica";
- "tempo de parede" (calco) -> "tempo total de execução (wall-clock)";
- "fotografia da tripla" -> "cada medição valha para a tripla" (métrica da
  régua de tom);
- acronimos.tex: entram AA (usada 4x no Cap. 2 e ausente da lista), QBC e
  ECOICOP (constituição: sigla presente na lista).

FILA PARA O TREM PÓS-MERGE do 25390a3 (t4/t5 — NÃO apliquei para não gerar
conflito; incluir no mesmo lote dos 23 itens de registro):
a. 2-fundam:724-725 — REMOVER a sigla STC: é definida ali e nunca mais usada
   em lugar NENHUM da tese (verificado por grep em todos os capítulos).
   Fica "classificação de texto curto (\textit{short text classification})".
b. 2-fundam:735 — unificar notação: "$f: D \rightarrow C$" -> "$f: X
   \rightarrow Y$" (a 2.1 define a tarefa como X->Y; dois alfabetos para o
   mesmo objeto no mesmo capítulo é o defeito clássico do R6).
c. 2-fundam:877-879 — a expansão de ECOICOP está errada no texto: "da
   Classificação do Consumo Individual por Finalidade (ECOICOP)" traduz
   COICOP e perde o E de "European". Corrigir para "da classificação
   europeia do consumo individual por finalidade (ECOICOP)".
d. Conferir na aplicação dos 23 itens que nenhum reintroduz sigla fora da
   lista (critério f do checklist do autor).

DECISÃO PARA O AUTOR (consolidar com as 3 que já estão na sua mesa):
- A lista de acrônimos agora tem AA (Aprendizado Ativo) E AL (Active
  Learning) para o MESMO conceito. O Cap. 2 fixa AA; o parecer R6 da banca
  já apontava que o Cap. 6 usa AL. Uma das duas tem que morrer na prosa —
  qual fica é decisão de terminologia do autor, e a lista então perde a
  outra entrada.

## Resultado (principal, 2026-08-17T22:40Z)
Trabalho concluído e integrado; tarefa fechada na limpeza da caixa.
