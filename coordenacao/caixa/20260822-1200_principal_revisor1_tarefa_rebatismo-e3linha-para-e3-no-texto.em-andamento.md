---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: (autor aprovou) rebatizar E3' -> E3 em TODO o texto da tese: reescrever o desenho em 3-metodo:443 (o E3 original nunca teve resultados; agora E3 é o experimento que hoje se chama E3'), renomear as ~35 ocorrências (\ref/label/prosa/tabela-mapa) e conferir que nenhuma vira órfã. Você já segura o cap3; faça na mesma frente da R4 se ainda estiver com o lock, senão branch própria. Cruzada do revisor2; gate do autor. COORDENE com o executor01, que renomeia código/artefatos/notebooks (tarefa irmã).
referencia: dec-nome-e3 aprovada pelo autor 2026-08-22 · ~35 ocorrências (grep "E3\$'\$" e variantes) · 3-metodo:443
criada_em: 2026-08-22T12:00:00Z
---

O autor aprovou remover a plica. Regras:
- E3' passa a ser E3 no texto inteiro; o "E3 original" (que nunca produziu
  resultado) deixa de existir como rótulo separado — reescreva 3-metodo:443
  para o novo desenho não deixar dois "E3".
- labels: se hoje é \label{...e3p...}, pode MANTER o label interno (custo zero,
  como fizemos nos pilares) e mudar só o texto visível "E3'"→"E3"; ou renomear
  labels também se ficar mais limpo — sua escolha, mas conte no DoD.
- sincronize a tabela-mapa (3-metodo) e as menções em 5-resultados e 6-conclusao.
- NÃO toque nos números (regime já fechado). Antes/depois; cruzada do revisor2.
