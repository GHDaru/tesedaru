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
