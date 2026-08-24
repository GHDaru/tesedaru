---
de: local
para: principal
tipo: entrega
acao_esperada: usar a tabela para redigir o 3.10 final com o autor e corrigir o 6.4; decidir o que fazer com as duas linhas sem evidência (máquina dos `_bs16v2` e RTX 3090)
referencia: tarefa 20260824-0226 (mensageria@f66b62c) · branch `local/ambientes-por-experimento` · `docs/ambientes-por-experimento.md`@6d8d3dc
criada_em: 2026-08-24T03:11:00Z
---
Mapeamento execução para ambiente levantado só por leitura de artefato, em
`docs/ambientes-por-experimento.md`@6d8d3dc (branch `local/ambientes-por-experimento`),
com evidência por linha e "sem evidência" declarado onde não há registro.

O que o principal precisa saber antes de abrir o arquivo, em quatro pontos:

1. O 6.4 e o 3.10 estão errados em direções opostas. "Semente única e CPU" era verdade
   da corrida ORIGINAL de julho (semente 42, lote 16, avaliação em 20.092 itens, CPU do
   sandbox, 4 vCPU), e é falso do regime `_bs16v2` que a tese imprime hoje, que tem três
   sementes e rodou em GPU. Do outro lado, nenhum artefato registra corrida em RTX 3090:
   toda menção a 3090 no repositório é plano ou estimativa.
2. Nenhum JSON de braço do E3' registra ambiente, e isso é do código, não da corrida:
   o dicionário serializado em `run_e3prime.py`@13ff0d1:225-235 não tem `device`, `gpu`,
   hostname nem versão de biblioteca. O ambiente só se declara pela receita commitada e
   pela coordenação.
3. A máquina exata dos 25 braços `_bs16v2` é sem evidência direta. O que há é indício
   forte de GPU e de três sessões distintas: braço D em 1199,2 s contra 10593,3 s no
   mesmo lote 16 em CPU (fator 8,8), e `predict_seconds` agrupado em três patamares
   estreitos por semente. Dizer "T4 do Kaggle" para elas seria inferência.
4. Três armadilhas registradas no arquivo: o `resultados.json` dá `notebook_kaggle` para
   E6, mas os notebooks do E6 são auditoria em CPU; os três regimes do E3' não podem ser
   misturados; e o legado citado como @b540533 não existe no clone local, que está em
   26d7c4e.

Risco: baixo, nada foi executado nem alterado fora desta branch. O único risco é de
leitura, se alguém tomar o indício de tempo do ponto 3 como registro de máquina.
