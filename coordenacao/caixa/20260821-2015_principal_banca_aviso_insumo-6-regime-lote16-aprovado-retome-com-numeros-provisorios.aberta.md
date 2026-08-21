---
de: principal
para: banca
tipo: aviso
acao_esperada: RETOME a redação das 4 superfícies (tarefa 1600): o autor decidiu — a tese reporta o REGIME LOTE 16 corrigido. Use os números da entrega 20260818-0235 do executor02 como PROVISÓRIOS: os 25 braços pré-correção serão regerados (aprovado), e os valores finais trocam quando a varredura 27/27 homogênea fechar. Estruture para a troca ser barata.
referencia: decisão do autor 2026-08-21 (dec-regime-lote16-aprovado, dec-regerar-25-bracos-aprovado) · insumo 5 · quadros lote16
criada_em: 2026-08-21T20:15:00Z
---

Diretrizes de montagem:

1. O eixo conceitual não mudou: critério pré-registrado em acurácia
   (qualificação junho/2023), operacionalizado como 0,95×régua (decisão
   declarada da tese); Macro F1 como robustez — só que agora o F1 TAMBÉM
   fecha dentro do teto (piso provisório 25 mil), então a seção de robustez
   ganha tom de reforço, não de ressalva.
2. O sub-treino do lote 128 entra como achado metodológico diagnosticado
   (com o teste de controle do executor02) — é a justificativa do regime
   reportado, não uma nota de rodapé.
3. Braço A: não atinge o critério (gap 28%) com 5,2% da base — a espinha
   "atingível dentro do teto vs configuração executada que parou cedo"
   continua. A>B merece uma frase (oráculo LLM bate gabarito nos mesmos
   itens).
4. NÚMEROS PROVISÓRIOS: concentre menções numéricas nas tabelas e em poucas
   frases marcadas (comentário LaTeX % PROVISORIO-ate-regeracao), para a
   troca final ser mecânica. O E25 cruza o F1 por 0,0041 — margem fina que
   PODE mudar com a regeração: não escreva nenhuma frase que quebre se o
   piso do F1 deslizar para 30 mil.
5. Cruzada do revisor2 como sempre; gate do autor no merge.
