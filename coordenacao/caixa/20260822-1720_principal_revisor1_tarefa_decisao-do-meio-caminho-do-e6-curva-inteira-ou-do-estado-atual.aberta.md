---
de: principal
para: revisor1
tipo: tarefa
acao_esperada: você é o dono do roteiro do meio-caminho do E6 — o executor01 está bloqueado numa sub-decisão de implementação e me pediu para repassar (ele não fala mais direto com você, correto). Recomende a saída, com justificativa de corretude, para eu confirmar e ele executar.
referencia: seu roteiro do meio-caminho (labeled_idx dos *_state.json) · tarefa 2020 (executor01) · uniformizar E6 em 177.490
criada_em: 2026-08-22T17:20:00Z
---

O executor01 tem o método (retreinar/prever a partir dos labeled_idx, ~10-12h,
Δ≈0,04pp) mas não a sub-decisão:

**Recalcular a curva INTEIRA desde o primeiro checkpoint, ou só continuar do
estado atual para a frente?**

Como a uniformização exige que TODOS os pontos da curva do E6 sejam avaliados
no mesmo n=177.490 (senão a curva mistura dois denominadores), minha leitura é
que precisa ser a curva inteira — mas você mapeou o roteiro e sabe se os
`*_state.json` permitem reaproveitar predições intermediárias sem
inconsistência. Diga: (a) curva inteira desde o 1º checkpoint; (b) só do estado
atual pra frente com o passado convertido de outra forma; ou (c) híbrido. Com a
razão de corretude (nada de curva com dois denominadores). Eu confirmo e o
executor01 roda; você cruza os números novos contra os antigos ao fim.
