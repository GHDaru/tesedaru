# Registro de Decisões — Jornada Autônoma

Formato: contexto → decisão → racional. Horários GMT-3.

---

## D-001 · 17/07 · Desempate do PVBin no porte
**Contexto**: validação B1c mostrou matrizes de escore IDÊNTICAS (dif. máx 0,0)
entre legado e porte; 100% das divergências de predição (141/1000, amostra de
treino 5k) são empates exatos no escore máximo — o legado resolve pela ordem
instável de `set()`, o porte pela ordem alfabética determinística. Com a base
de treino completa (250k), empates tornam-se raros.
**Decisão**: manter argmax com ordem de classes alfabética (determinística);
NÃO introduzir desempate por frequência de classe.
**Racional**: (i) fidelidade matemática comprovada é o critério de validação —
predição só difere onde o legado era, ele próprio, arbitrário; (ii) desempate
por prior melhoraria acurácia mas confundiria a reexecução C1 (comparação com
os números originais da dissertação); (iii) determinismo é requisito de
reprodutibilidade da constituição.

## D-002 · 17/07 · Escala dos replays P1/AG (Bloco C)
**Contexto**: o P1 original usou 47 tamanhos × 30 repetições (~1.410 execuções)
e o AG usou N_pop=50 × 100 gerações × 10 tamanhos × 4 cenários. Reexecutar na
íntegra neste ambiente (CPU compartilhada) levaria dias e não é necessário para
o objetivo da reexecução: verificar se a FORMA da curva e as CONCLUSÕES se
reproduzem de forma independente.
**Decisão**: P1-replay com 15 tamanhos log-espaçados (10→200.000) × 10
repetições; AG-replay com 2 tamanhos (50, 500) × 2 cenários (max Acc, max
MacroF1), N_pop=30, 40 gerações, aptidão em partição de aferição (5k) e
reavaliação final em teste intocado (protocolo anticircularidade A3).
**Racional**: 10 repetições dão desvio-padrão estável para comparar com as 30
originais; a grade log-espaçada preserva a resolução onde a curva muda (baixos
tamanhos); o AG reduzido verifica o MECANISMO (envelope acima do aleatório) sem
pretender reproduzir os valores extremos, que dependem do orçamento evolutivo.
Divergências serão reportadas como tais no relatório C3.

## D-003 · 17/07 · E5 (E2E com LLM free) adiado para após o E0 de fundo
**Contexto**: o teste E2E do FlowBuilder com gemma-4 :free falhou com 100% de
rótulos inválidos no L0 e chamada direta ao modelo pendurou em retries de 429 —
o run E0 de fundo consome a cota livre por conta do OpenRouter simultaneamente.
**Decisão**: manter o run E0 (prioridade: dados da tese), reexecutar o E5
quando ele terminar. O caminho E2E completo JÁ está validado com oráculo
simulado sobre dados reais; o adapter OpenRouter JÁ está validado no próprio
E0 (nemotron 675/1000 anotações em andamento). Guarda de erro clara adicionada
ao runner (L0 sem rótulo válido → mensagem acionável).

## D-004 · 17/07 · Desenho do E0-P (ablação de prompt)
**Contexto**: as regras de fronteira do prompt v4 derivam da ANÁLISE DE ERROS
feita sobre as amostras oficiais (S-rand/S-strat) — usar as mesmas instâncias
como few-shot ou avaliar só nelas contaminaria a medição.
**Decisão**: (i) exemplos few-shot do v4b são descrições INVENTADAS análogas
(nunca strings das amostras); (ii) as regras v4a derivam majoritariamente dos
erros da S-strat e o efeito é medido nas DUAS amostras, com a S-rand (instâncias
disjuntas) como leitura primária; (iii) v3 reutiliza as anotações oficiais já
existentes do gpt-4o-mini (mesmo instrumento), pareando nos mesmos 500+500 itens.
**Racional**: mede-se generalização das regras, não memorização; custo ~US$0,10.
