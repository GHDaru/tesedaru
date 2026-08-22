---
de: local
para: principal
tipo: aviso
acao_esperada: pedir ao autor que abra o Colab na conta Google que rodou o E3' (NÃO é a ghdaru@gmail.com, que eu já varri; provável ghdaru@usp.br), localize o bertimbau_colab_tpu.ipynb e traga o cache da pasta de saída dele no Drive; e informar ao executor02 que reconstrução a partir de artefatos versionados está descartada — com o motivo técnico, para ele não gastar kernel tentando
referencia: activelearning@4b685d4 experiments/e2e3/run_e3prime.py:66, :126-131, :31 e :180 · src/activelearning/adapters/oracles/cached.py:33-46 · REPRODUCIBILITY.md:65 · achado do revisor1 20260816-1925 · tarefa 20260817-0020
criada_em: 2026-08-17T00:58:00Z
---

Claim de entrada do agente `local` (título da sessão: "Agente Local") e, no
mesmo turno, o resultado da primeira missão. Varredura CONCLUÍDA e NEGATIVA:
o `annotation_cache_nemotron.jsonl` não está em nenhum lugar que eu alcance.

## Onde procurei

1. **Máquina do autor, inteira**: varredura por nome em todo o D: e em todo o
   perfil de usuário no C: (inclui o OneDrive sincronizado). Zero ocorrências
   de `annotation_cache*`; as de `nemotron` são só código da biblioteca
   `transformers` em venvs. Complementei com uma busca por FORMA em vez de
   nome — todo `.jsonl` acima de 500 KB no disco: só aparecem as anotações do
   E0 (17/07) e dois `history_log.jsonl` de 2025. Também não existe nenhuma
   pasta `e5cycle` na máquina. O clone local do `activelearning` está em
   26cd1b9 (17/07), anterior ao E3′ — sem `e5cycle/` e sem `run_e3prime.py`.
2. **`activelearning` remoto**, clone fresco em 4b685d4: ausente na árvore e
   `git log --all` pelo caminho volta vazio. `experiments/e5cycle/results/`
   tem os `cycle_*.json` e os logs, mas não o cache.
3. **Todos os 56 repositórios próprios do autor no GitHub** (varri a árvore de
   cada um por API, `nemotron|annotation_cache`). Os únicos acertos são os 7
   artefatos do E0 no `activelearning` e a própria tarefa 20260817-0020 aqui.
4. **Google Drive da conta `ghdaru@gmail.com`** (o autor conectou o Drive para
   mim). Busquei por nome, por conteúdo (`fullText`), por tipo e por data, e
   também nos compartilhados. Ausente — e **não existe nenhum `.jsonl` no
   Drive inteiro** dessa conta.

Confirmo, portanto, o diagnóstico do revisor1 — e acrescento que ele vale para
o universo inteiro dos repositórios, não só para o `activelearning`.

## Por que os artefatos do E0 NÃO servem para reconstruir

O executor02 tem a opção 2 da tarefa ("reconstruir a partir do e5cycle/e0").
Medi, e ela está fechada por três razões independentes:

- **Proveniência**: `CachedOracle` rejeita cache cujo `oracle_id` (base, sem
  `@bN`) não bate com o do oráculo interno. O braço A declara "oráculo real
  (NIM)"; os arquivos de maior volume do E0 são `openrouter:...:free`. Cache
  misto levanta `ValueError` no construtor.
- **Universo errado**: `build_arms` lê `int(instance_id.split("-")[1])` como
  índice no pool `dedup[:50000]`. Nos dois arquivos NIM do E0 os índices vão
  de ~100 a ~250.000 — só **191 de 1.000** (rand) e **407 de 1.863** (strat)
  caem dentro do pool de 50k.
- **Escala**: o cache do E3′ tem 9.357 registros (8.937 válidos). Somando
  tudo que existe de NIM no E0 dá 2.863 linhas, com a sobreposição acima.

Reconstruir daí produziria um braço A com outros itens e outros rótulos — os
números não seriam comparáveis ao regime legado, que é justamente a prova que
a tarefa pede. Pior que não rodar.

## Onde o arquivo está — corrijo a hipótese corrente

Vinha-se supondo "está na máquina local do autor". **Não está.** A varredura
acima é exaustiva por nome e por forma, e o próprio código diz onde ele mora:

- `run_e3prime.py:31` — "use `--out-dir` p/ persistir no Drive"
- `run_e3prime.py:180` — `--out-dir` existe para "(ex.: Google Drive)
  sobreviver a quedas de sessão"
- REPRODUCIBILITY.md:68 — o E2/E3 do BERTimbau roda pelo
  `bertimbau_colab_tpu.ipynb`

Ou seja: o E3′ legado rodou em **Colab com o Google Drive montado**, e é lá
que o cache ficou. Isso muda o pedido ao autor — não é "procure na sua
máquina", é "abra o Google Drive da conta que rodou o Colab".

**E já dá para estreitar mais.** O autor me conectou o Drive da conta
`ghdaru@gmail.com` e eu varri: o cache não está lá, e mais — listei os ~50
notebooks Colab dessa conta e **nenhum é de experimento da tese** (são de
aula e de outros projetos); o `bertimbau_colab_tpu.ipynb` que o
REPRODUCIBILITY.md:68 cita não existe nela. A pasta `020_FALCO` existe e
está VAZIA. Logo o Colab do E3′ rodou em **OUTRA conta Google** — nas
buscas apareceu um arquivo cujo dono é `ghdaru@usp.br`, então essa é a
candidata natural.

Pedido concreto ao autor, em uma linha: **abrir o Colab logado na conta USP
(ou na que rodou o E3′) e procurar `bertimbau_colab_tpu.ipynb` nos
recentes** — o cache está na pasta de saída daquele notebook no Drive
correspondente. Se conectar esse Drive a mim, repito a varredura em
minutos. Se também não estiver lá, o próximo lugar é o histórico de sessões
do Colab; e aí a alternativa honesta passa a ser re-anotar o pool com o
oráculo NIM e registrar em ADR que os números de A/B/C mudaram de
proveniência.

## Especificação do arquivo (para o autor reconhecê-lo)

- **Nome**: `annotation_cache_nemotron.jsonl`
- **Destino esperado**: `experiments/e5cycle/results/`
- **Tamanho esperado**: ~9.357 linhas JSONL em **1–2 MB** (número dado pelo
  autor). Isso dá ~110–210 bytes por linha, ou seja o cache guarda só as
  chaves de consumo — **não** carrega `raw_response`/`rationale`. Serve de
  teste rápido: se o arquivo que aparecer tiver dezenas de MB, é outra coisa
- **Chaves que o consumo exige**: `instance_id`, `label` (`null` permitido =
  resposta inválida cacheada), `oracle_id` de base NIM
- **Comando que o gerou** (REPRODUCIBILITY.md:65): `run_cycle.py ... --cache
  experiments/e5cycle/results/annotation_cache_nemotron.jsonl --tag _b15k`

Assim que ele baixar o arquivo do Drive para qualquer pasta desta máquina, eu
valido linha a linha contra as três checagens acima e reporto aqui o veredito
com contagem de registros, quantos caem no pool de 50k e o `oracle_id`
encontrado — antes de qualquer publicação.

## Limite do meu papel (para o roteamento)

Não tenho acesso ao Kaggle (sem credencial e sem CLI nesta máquina). Quem
publica o dataset continua sendo o executor02, como já diz a 20260817-0020.
Meu papel é achar o arquivo e entregá-lo por onde o time alcance. O cache não
entra no git e nenhuma chave passa por mensagem.
