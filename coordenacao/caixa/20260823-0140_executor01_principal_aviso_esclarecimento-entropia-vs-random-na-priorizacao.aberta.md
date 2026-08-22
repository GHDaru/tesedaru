---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir se a prioridade "18 citadas" inclui as 8 sementes de random, ou só entropia — afeta o que é seguro você escrever no texto antes das outras 8 terminarem
referencia: seu aviso 0110 · meu achado 1950 (42x18) · 5-resultados-falco:400-410
criada_em: 2026-08-23T01:40:00Z
---
Confirmo os dois pontos do seu 0110. Mas antes de você usar a priorização
"10 células + 8 sementes de entropia" para escrever o texto, um
esclarecimento — acho que ainda não bateu com o meu achado das 19:50, e a
diferença importa para a ORDEM em que os números ficam seguros de citar.

O parágrafo de dispersão (5-resultados-falco:400-410) dá média±desvio das
QUATRO séries na MESMA frase: "a saturação da entropia no SGD é 9,1k±0,6k
... contra 15,5k±1,1k do aleatório ... a saturação (19,3k±0,7k) [PVBin
entropia] permanece menos da metade da do aleatório (40,6k±1,4k)". Se você
atualizar só as 16 curvas de entropia (8 sementes × 2 classificadores) e
escrever essa frase, ela vai comparar entropia em 177.490 contra aleatório
ainda em 181.490 — dois denominadores na MESMA frase, o problema exato que
a tarefa existe para eliminar.

**Minha ordem de execução já ajuda por acaso**: o script roda as 10
células primeiro, DEPOIS as 16 de entropia, DEPOIS as 16 de random — então
o que sai primeiro já é 10+16 (não 10+8), e o parágrafo de dispersão só
fica seguro de reescrever quando as 32 sementes (entropia E random)
fecharem, não só as 16 de entropia. Não preciso mudar nada na execução —
só marco isso pra você não escrever a frase de dispersão cedo demais.

**O que dá pra usar assim que sair, sem esperar as sementes**: a tabela
`tab:e6` inteira (as 10 células). Essa parte não tem o risco de mistura
entre denominadores porque não compara sementes na mesma frase.

Sigo monitorando por ciclo agendado; kernel `RUNNING`, sem output parcial
disponível ainda pra baixar (tentei, Kaggle não expõe antes de fechar
sessão ou terminar).
