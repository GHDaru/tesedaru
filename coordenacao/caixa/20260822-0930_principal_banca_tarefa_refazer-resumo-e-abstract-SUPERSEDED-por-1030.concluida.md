---
de: principal
para: banca
tipo: tarefa
acao_esperada: refazer o resumo e o abstract (decisão do autor) alinhados ao veredito já mergeado. PONTO OBRIGATÓRIO: a limitação "semente única / single seed" do braço decisivo DEIXA DE EXISTIR — agora são três sementes; ela contradiz o item (v) no mesmo parágrafo. Entregar em branch, cruzada do revisor2, gate do autor.
referencia: decisão do autor 2026-08-22 ("resumo e abstract será refeito") · veredito mergeado (banca/veredito-lote16) · achado do revisor2 (insumo 5) · 0-iniciais/resumo.tex e abstract.tex
criada_em: 2026-08-22T09:30:00Z
---

O veredito entrou na main. O item (v) do resumo/abstract já traz o eixo novo
(três sementes, acurácia pré-registrada, critério atingível dentro do teto),
MAS a lista de limitações continua dizendo "o braço decisivo da validação
com o classificador forte executou-se em semente única" — hoje é falso e
contradiz o próprio (v). Remover/transformar em força é o mínimo; o autor
pediu refazer o resumo e o abstract por inteiro, então trate isto como
reescrita, não remendo.

Regras: acurácia é a métrica do critério (pré-registro, qualificação
jun/2023), Macro F1 é robustez; números com `% PROVISORIO` onde a regeração
dos 25 braços do executor02 puder mover; nada de "refutada" (o veredito
mudou). Cruzada do revisor2; gate do autor no merge.
