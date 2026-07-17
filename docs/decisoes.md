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
