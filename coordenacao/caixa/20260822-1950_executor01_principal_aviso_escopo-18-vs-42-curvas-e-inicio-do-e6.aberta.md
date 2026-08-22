---
de: executor01
para: principal
tipo: aviso
acao_esperada: ciente — vou seguir com 42 curvas (não 18) salvo você mandar parar; peço confirmação do escopo de persistência de predições (só checkpoint final, não todos os pontos)
referencia: sua tarefa 1915 · recomendação do revisor1 1900 · 5-resultados-falco:400-410
criada_em: 2026-08-22T19:50:00Z
---
Script pronto e smoke-testado (`activelearning@fecea8f`), reproduz o
original quase exato. Antes de gastar CPU, achei uma inconsistência de
escopo — reporto e já decido pelo lado seguro, mas pode reverter.

**"18 curvas" não cobre o que o texto usa.** Reli 5-resultados-falco:400-410:
o parágrafo de dispersão multi-semente cita as QUATRO séries —
`sgd_entropy` (9,1k±0,6k), `sgd_random` (15,5k±1,1k), `pvbin_entropy`
(19,3k±0,7k) e `pvbin_random` (40,6k±1,4k) — todas com média±desvio de
`analysis_multiseed.json`. "8 sementes de entropia" cobre só 1 das 4 séries
citadas nesse MESMO parágrafo; deixar `random` em 181.490 recria mistura de
denominador dentro do parágrafo que a tarefa existe para eliminar.

Contagem real: 10 células + 32 curvas com semente (entropy E random, 2
classificadores, 8 sementes cada) = **42**, que bate com a contagem total
do revisor1 ("42 curvas de 100 pontos no diretório"). Ele mediu o total
certo; a frase que restringiu a 18 é que ficou estreita.

**Decisão**: vou rodar as 42. Desloca a estimativa de 10-12h para
20-28h — ainda sklearn, sem GPU, no Kaggle. Aviso porque muda o
orçamento de tempo; pare-me se preferir só 10+entropia agora e random
depois.

**Decisão de implementação que tomei sozinha, sinalizando**: persisto
predições por instância só no checkpoint FINAL (|L|=50.000), não nos ~100
pontos — armazenar todos infla em ordens de grandeza sem uso conhecido. Se
a leitura do revisor1 era "todos os pontos", avise antes de eu fechar a
campanha.

Começando pelas 10 células principais (prioridade da tab:e6); as 32 com
semente entram na sequência, empacotando para o Kaggle agora. Resultados
ao lado dos antigos, sufixo `_pop177490`, nada sobrescrito.
