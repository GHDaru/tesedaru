---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: com a prosa mergeada na main (38dbb11), remover as entradas Wu2022 e Ahmed2023 do referencias.bib na branch bibfix/lotes (com lock) — são órfãs agora; check-bib deve zerar; avisar com hash para eu montar o GATE FINAL do bib ao autor
referencia: merge da prosa na main · bibfix/lotes @ a3861ca+ · suas pendências conhecidas do check-bib
criada_em: 2026-08-17T03:05:00Z
---
A prosa do Cap. 2 está na main sem nenhum \cite de Wu2022 e Ahmed2023 (e com
Margatina2023 no lugar, fichada). As duas entradas fabricadas viraram órfãs
sem fichamento e sem relação — pelo invariante, removíveis. Remova as duas,
rode o check-bib (esperado: ZERO pendências) e me devolva o hash. Com isso eu
consolido o gate final do bib-fix inteiro para o autor: lotes 1-5 +
correções + invariantes, de 378 para ~338 entradas, tudo verificado na
fonte. Inclua no mesmo aviso o estado dos seus 2 fichamentos pendentes de
gate (Rouzegar2024 e Fromme2022) — vou levá-los no mesmo bloco.

## Resultado (revisor1, 2026-08-17T03:20Z)

bibfix/lotes @162c12b. check-bib: exit 0, "PROBLEMAS: nenhum", 337 entradas,
145 chaves citadas. As duas entradas conferidas na fonte antes da remocao e
confirmadas fabricadas (arXiv 2212.06445 e de matematica; o survey real dos
autores do Ahmed2023 e DOI 10.3390/app13010342). Precisou de um merge da main
na branch antes (edef416), senao os .tex dela ainda citavam as duas chaves.
Detalhe e ressalvas: coordenacao/caixa/20260817-0320_revisor1_principal_aviso_bib-zerado-e-estado-dos-2-fichamentos.aberta.md
