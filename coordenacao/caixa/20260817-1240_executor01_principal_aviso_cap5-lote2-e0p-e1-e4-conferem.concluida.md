---
de: executor01
para: principal
tipo: aviso
acao_esperada: nenhuma decisão nova — registro do lote 2; sigo para a Onda 2 (P1/P2) conforme a ordem "todas as ondas"
referencia: docs/records/rastreabilidade.json (65 itens) · activelearning@d1a798b notebooks/auditoria/build_rastreabilidade.py
criada_em: 2026-08-17T12:40:00Z
---
**Lote 2 do Cap. 5 fechado** (E0-P, E1, E1b, E4). Tarefa 1210 reivindicada; o
check-in automático da minha sessão está armado — eu não tinha nenhum, e era
por isso que eu parava entre uma ordem e outra.

## Nenhuma divergência nova de número

**E0-P confere inteiro** — seis células de acurácia, seis pares de
discordantes, os p do McNemar e o p=0,0013 do v4b contra v4a.
**E1 confere inteiro** — cinco estratégias em LCE e F1 final com desvios, o
teto de 0,540, os 78% recuperados e a ablação de lote b50/b100/b200.
**E4 confere inteiro** — os seis pares ε × estratégia com retenção, e o
p=0,0078 em todos os níveis.

Placar do Cap. 5: **65 números · 52 rastreados · 9 divergentes · 3 sem
evidência · 1 legado**. As 9 divergências continuam sendo as já reportadas.

## Três dados brutos que faltam (novos)

1. **`sweeps.jsonl` das 104 células do E1/E1b/E4** não está no repositório —
   só o `analysis.json` e o `baseline.json`. Conclusão versionada, dado por
   célula não.
2. **`experiments/plots/` tem o gerador e nenhuma figura.** As publicadas
   vivem em `tesedaru/N-*/imagens/`, desacopladas do script — nada garante que
   a figura da tese corresponda ao artefato atual.
3. Os **replays de P1/P2** que sustentam o "execuções já auditadas" do Cap. 3.

Os três casam com a linha 7 do `.gitignore`. Verifiquei o mecanismo com
`git check-ignore --no-index`: a regra barra **tudo** que casa, e os 42 JSONL
do E6 estão versionados porque alguém os forçou com `add -f` no commit
`20059cb`. Não é falha de configuração — é ausência de critério. **Proposta**:
JSONL que sustenta número publicado entra sempre, mesmo grande. Decisão sua.

## Defeito meu, corrigido antes de reportar

Minha comparação numérica não tinha folga de ponto flutuante e marcava três
números do E1/E4 como divergentes: `0,006 − 0,0055` dá
`0,0005000000000000004`, que estoura uma tolerância de exatamente `0,0005`.
Teriam chegado a você como divergências da tese, e eram erro meu. Corrigido,
com o motivo no código — auditoria que inventa divergência é pior que
auditoria nenhuma.

## Próximo

**Onda 2: P1/P2 (Cap. 4)** — reexecutar os dois replays, que é o caminho para
transformar o `sem-evidencia` do "auditadas" em artefato de verdade. Lembrete
para quem revisar: os `.jsonl` precisam entrar com `git add -f`, senão a
regra 7 os engole outra vez.
