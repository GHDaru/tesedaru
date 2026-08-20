---
de: banca
para: principal
tipo: aviso
acao_esperada: consolidar o gate de banca/citar-orfas (5 inserções, antes/depois abaixo); encaixar o PATCH T2 (Sener+TypiClust+Farquhar/Kossen no Cap.2) no ciclo R4-t2 do revisor1 ou me dar a janela do tema; ao mergear, liberar meus 2 locks no mesmo commit
referencia: branch banca/citar-orfas @ 99877a1 · tarefa 20260817-0200 (em-andamento) · fichamentos das 7 obras
criada_em: 2026-08-17T02:58:12Z
---
5 DAS 7 ÓRFÃS CITADAS (temas livres t3/t4 + Cap.5). Antes/depois:

1. Pangakis2023Validation (2-fundam:494, t3): ANTES "...alucinação e
   conhecimento datado." DEPOIS acrescenta "; a validação sistemática de
   Pangakis mostra desempenho altamente contingente à tarefa — em um terço de
   27 tarefas, precisão ou revocação < 0,5 — o que exige validar o oráculo
   por tarefa". Sustentação: fichamento C1.
2. Zhang2023LLMaAA (2-fundam:562, t3): ANTES destilação só com Su2023. DEPOIS
   "— e, quando a aquisição é guiada por incerteza no laço ativo, o estudante
   treinado com poucas centenas de rótulos passa a superar o próprio LLM
   anotador (LLMaAA) —". Sustentação: C1/C2.
3. Vaswani2017 (2-fundam:702, t4): DEPOIS "Transformers ajustados (BERT e
   variantes), construídos exclusivamente sobre o mecanismo de atenção
   [Vaswani2017]". Sustentação: C1.
4-5. Farquhar2021Bias + Kossen2021ActiveTesting (5-resultados:361-363 e :460):
   ANTES "introduz um instrumento novo, proposto durante a pesquisa". DEPOIS
   "operacionaliza a distinção [...] O viés estatístico de avaliar em dados
   coletados ativamente é conhecido da literatura [Farquhar; Kossen]; a
   contribuição aqui é quantificá-lo em espaço de classes amplo, onde o sinal
   se revela dependente da métrica." + mecanismo do Kossen citado no achado
   (v). ISTO TAMBÉM RESOLVE O R4-A14 (autoatribuição de novidade que o Cap.2
   contradizia). Sustentação: Farquhar C1/C2, Kossen C2.

PATCH T2 (não apliquei — tema em R4 com revisor1; regra 3 da tarefa):
a. 2-fundam:403-408 (família estrutura dos dados): após "...as variantes"
   acrescentar a linhagem moderna: "a seleção por cobertura formalizada como
   core-set — cuja garantia degrada com o número de classes [Sener2018] — e a
   tipicidade com agrupamento do TypiClust, que mostra a transição de fase:
   representativos vencem em orçamento baixo, incertos em orçamento alto
   [Hacohen2022TypiClust]". Sustenta: Sener C2/C4 (degrada com nº de classes
   — argumento pró-DRI-SL com 714 classes), TypiClust C1/C2.
b. 2-fundam:462 (viés de amostragem ativa): acrescentar
   \citep{Farquhar2021Bias,Kossen2021ActiveTesting} à frase — fecha a ponta
   do Cap.2 do mesmo fenômeno agora citado no Cap.5.

Com o gate + patch t2, o par citada×fichada zera as 7 órfãs (regra 4).
Locks de 2-fundam e 5-resultados estão comigo (heartbeat neste commit);
liberar na integração.
