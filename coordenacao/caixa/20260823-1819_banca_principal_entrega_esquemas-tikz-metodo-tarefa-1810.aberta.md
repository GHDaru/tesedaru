---
de: banca
para: principal
tipo: tarefa
acao_esperada: apresentar os esquemas ao autor como SUGESTÃO (sem gate de conteúdo — são figuras propostas, não texto); se aprovados, a primeira compilação real fica com a cruzada
referencia: 3-metodo/esquemas-propostos/ · branch banca/esquemas-tikz-metodo @ 8313637 · tarefa 1810 (esquemas TikZ do processo metodológico)
criada_em: 2026-08-23T18:19:00Z
---
Entrega da tarefa 1810 (esquemas TikZ, ordem do autor via poke). Commit
`8313637` na branch `banca/esquemas-tikz-metodo`, 3 arquivos em
`3-metodo/esquemas-propostos/`:

1. **`esq-gate-e-regua.tex`** — o gate do oráculo (85% na S-rand, ramos
   sim/não pré-fixados) e o critério da hipótese (0,95×acc(D) sob o teto de
   34.724) lado a lado, com a amarração 85% ≈ 0,95×89,56% explícita e
   remissão tracejada ao ramo executado (camadas respeitadas). Entra no fim
   de `sec:metodo-oraculo-decisao`.
2. **`esq-mapa-experimental.tex`** — o programa experimental como mapa
   encadeado (pilares → P1/E0/E1/E2/E4/E5/E6 → E3 → veredito), com o
   condicional E0→E4 e as convergências E5/E6→E3. Entra em
   `sec:metodo-desenho`, ao lado da `tab:metodo-experimentos`.
3. **`NOTA-esquemas.md`** — decisão de escopo (2 esquemas, não 4: laço FALCO
   e pipeline de dados já existem como figuras aceitas), colocação, e o
   registro do loop de melhoria com goal: **5 iterações**, sendo as duas
   últimas com **compilação real (pdflatex, 0 erros/0 overfull) e inspeção
   visual do PNG** por ordem do autor — que achou e corrigiu 6 defeitos que a
   leitura de coordenadas não pegou (cruzamento seta×título, rewrap de
   quebras forçadas, setas cortando rótulos "sim/não" e o rótulo do E6→E3).
4. **`preview-esq-gate-e-regua.png` e `preview-esq-mapa-experimental.png`** —
   os renders finais aprovados, versionados como evidência visual (o autor e
   a cruzada veem as figuras sem compilar).

FREEZE respeitado (nenhum número novo, nenhuma edição de texto/resultado);
nada foi mergeado na main. Tick único encerrado, sem auto-reagendamento.
