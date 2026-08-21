---
de: principal
para: executor02
tipo: tarefa
acao_esperada: sua fila é a mais crítica do projeto e não mudou: (1) re-coleta E5 → cache; (2) braços A/B/C × 3 sementes; (3) McNemar/bootstrap canônicos + parecer da anomalia dos IC; (4) sub-treino D/lote16. Reporte por etapa concluída
criada_em: 2026-08-17T22:55:00Z
referencia: tarefas 20260817-1210 e 20260816-2152 · achado da população divergente (aviso 2215)
---
CONTEXTO: com os Caps. 1 e 2 encerrados, **a sua fila virou o caminho
crítico da tese**. Nada do texto avança as três leituras do Cap. 5 que
dependem dos seus números — e o gargalo é a re-coleta.

ATENÇÃO ao aviso 2215 (população divergente E3' × E6): se a decisão do autor
for reexecutar o E6 com 177.490, isso entra na SUA fila; não comece sem
ordem, mas já dimensione o custo de GPU e me diga, porque o autor vai
perguntar.

NO LOOP: você ficou 12 h sem reportar durante a re-coleta e eu tive que
cobrar. Numa rodada longa, um aviso de "em curso, previsão X" a cada ~4 h
basta — não é progresso parcial proibido pelo §3, é sinal de vida em job
longo, e evita que eu ou o autor gastemos tempo investigando.

## Resultado (executor02, 2026-08-18)

Os 4 itens da fila estão concluídos: (1) re-coleta E5 → cache — feito;
(2) A/B/C × 3 sementes — feito; (3) McNemar/bootstrap canônicos + parecer
da anomalia dos IC — feito (não se reproduz no canônico); (4) sub-treino
D/lote16 — feito, e expandido (com autorização do autor) numa varredura
completa de 9×3 em lote 16, com um colapso de treino corrigido no meio do
caminho. Veredito final consolidado em
`coordenacao/caixa/20260818-0235_..._varredura-bs16-fechada-veredito-final.aberta.md`.
Nota sobre o feedback de cadência: aplicado a partir da mensagem 20260818-0045
em diante (status a cada job longo, não só no início/fim).
