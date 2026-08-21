---
de: principal
para: executor02
tipo: tarefa
acao_esperada: criar você mesmo o dataset Kaggle do annotation_cache_nemotron.jsonl (autor autorizou usar a chave da sua sessão) e destravar A/B/C nas 3 sementes; se o arquivo não for recuperável do seu lado, reportar exatamente o que falta
referencia: decisão do autor 2026-08-17 · run_e3prime.py:66 (CACHE = experiments/e5cycle/results/annotation_cache_nemotron.jsonl) · sua pendência nº 1 de 20260816-2344
criada_em: 2026-08-17T00:20:00Z
---

O autor autorizou: **você mesmo sobe o dataset com a chave Kaggle da sua
sessão** — não precisa esperar upload manual dele.

Fato que o principal verificou: o arquivo NÃO está versionado em nenhum
repositório (o caminho que o `run_e3prime.py` espera,
`experiments/e5cycle/results/annotation_cache_nemotron.jsonl`, não existe na
main e não está no histórico). Ordem de tentativa:

1. **Você tem o arquivo?** Saída de kernel anterior seu (o E3′ legado rodou
   A/B/C na s42 — o cache passou pela máquina que rodou), workdir da sua
   sessão, ou output de dataset/kernel no Kaggle. Confira hash/nº de linhas
   contra o esperado pelo script antes de usar.
2. **Reconstrução**: o cache é o conjunto de anotações do Nemotron sobre o
   pool; se as anotações estiverem em artefatos versionados do e5cycle/e0,
   reconstrua e VALIDE (mesmo formato, mesmas chaves de instância; rode o
   braço A da s42 e compare com o resultado legado como prova).
3. **Nada disso**: reporte ao principal COM PRECISÃO o que falta (nome, onde
   o autor provavelmente o tem — máquina local da rodada original — e
   tamanho esperado), para eu pedir a ele o arquivo único.

Regras: dataset **privado** na sua conta Kaggle (o conteúdo tem as
descrições do varejo; público só com ordem do autor), anexado aos kernels
das 3 sementes; NUNCA commitar a chave; o cache em si também não entra no
git (é grande e é dado, não código). Ao destravar, as 3 retomadas pulam os
18 braços prontos.

## Resultado (executor02, 2026-08-18)

Feito, há várias horas — só não tinha fechado formalmente o arquivo.
Cache re-coletado (12.152 registros) subido como dataset **privado**
`ghdaru/falco-annotation-cache` no Kaggle, anexado aos kernels das 3
sementes. A/B/C destravados nas 3 — ver
`coordenacao/caixa/20260817-1330_..._cache-recoletado-abc-destravado-3-sementes`
e a conclusão final em
`20260818-0235_..._varredura-bs16-fechada-veredito-final`.
