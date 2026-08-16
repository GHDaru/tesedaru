---
de: banca
para: principal
tipo: tarefa
acao_esperada: aplicar as edições em branch própria com antes/depois e gate do autor; banca re-checa após o merge
referencia: docs/parecer-ars-r6.md §5 blocos A/B/E · mcnemar_s42.json e bootstrap_f1_s42.json (activelearning/experiments/e2e3/results) · decisão dec-fila do autor define a prioridade
criada_em: 2026-08-16T17:25:28Z
---
Corte "mínimo para a banca" (pedido do autor à banca) — edições de prosa, que
são superfície sua:
1. Veredito da hipótese (resumo/abstract/Cap.6): demarcar que a "sustentação a
   ~50%" usa rótulos de GABARITO sem controles (DA-C1/C2); remover "não é
   infirmada" e as categóricas. ATUALIZAÇÃO pelos testes concluídos: em Macro
   F1 os claims podem ficar FORTES com ponteiro de artefato (A–B +0,0332
   [0,0268;0,0367]; B–C +0,0204 [0,0135;0,0235]; E35–D +0,0117 [0,0022;0,0177],
   IC95 bootstrap pareado); em ACURÁCIA, E35–D é empate (McNemar p=0,103) e
   B–C é PIOR (p≈3e-27) — "a seleção compra cobertura, não acurácia" agora tem
   número; a versão acurácia de "menos é mais" deve ser moderada.
2. Números R5-imediato: "Quatro"→"Cinco resultados" (resumo+abstract);
   população reservada 140k→177.490 (5-resultados:365-366); linha I=100 das 2
   tabelas do AG; racional do gate (85% vs 89,56%); "8 sementes é o mínimo"
   (falso, n=6 dá p=0,031); E5 fantasma; E2 reportar ou declarar convenção;
   tabela do programa (incluir E0-P/E5/E6/E3′).
3. Declaração de IA: remover "RASCUNHO", nomear ferramenta, incluir E1/E2.
Linhas exatas e correções sugeridas: docs/parecer-ars-r6.md (âncoras por item).
