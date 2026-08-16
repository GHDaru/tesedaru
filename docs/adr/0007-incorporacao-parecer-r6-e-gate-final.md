# ADR 0007 — Incorporação do parecer ARS-R6 ao plano e criação do gate final

- **Status**: Aceita · **Data**: 2026-08-16
- **Ciclo**: governanca-01 · **Decisor**: Gilsiley Henrique Darú (encaminhou o parecer e perguntou pelo gate final)

## Contexto

Sessão paralela rodou uma reavaliação ARS ("R6") e propôs 6 mudanças ao plano.
O arquivo docs/parecer-ars-r6.md AINDA NÃO está na main; as alegações mecânicas
foram verificadas de forma independente contra o referencias.bib desta cópia:
confirmadas e piores que o alegado (17 títulos duplicados em 369 chaves;
ActiveLLM, zhang2022 e Settles2008 em triplicata). O autor também perguntou se
existe gate de revisão final — não existia: R7 é por capítulo, sem marco global.

## Decisão

1. Lente R3 vira "Referências × fichamento × fonte primária" (DOI/venue,
   obrigatório pós-2022; zero chaves duplicadas).
2. Itens "R5-IMEDIATO" nas aberturas de cap3/cap4/cap5 (inconsistências
   independentes da multi-semente, corrigíveis já).
3. Duas execuções de agente adicionadas (McNemar pareado e bootstrap de Macro
   F1 sobre predições persistidas) — desarmam o CRITICAL estatístico antes da
   multi-semente.
4. Nota do fecho do Cap. 6 reclassificada: parte é MÉRITO (DA-C1/C2/C3), não só
   estilo; decisão segue do autor.
5. Novo grupo "melhorias-r6" (7 itens de agente) e acréscimos em publicações
   (LGPD/Cap. 3; URL+DOI no A4) e governança (dedup do bib no dod-scripts).
6. Novo grupo "encerramento": DoD final verificável → parecer ARS de fechamento
   → aprovação do orientador → GATE FINAL DO AUTOR → depósito, encadeados por
   bloqueado_por. O gate final passa a existir como artefato visível e contável.
7. Campo "decisoes_pendentes" no plano; fila do autor exibe tipo DECISÃO. Duas
   pendentes: ordem da fila (parecer sugere bib antes da humanização do Cap. 2)
   e fecho do Cap. 6. O campo "proximo" fica SUSPENSO até a decisão da fila.
8. A âncora "85,8" do parecer NÃO entra como número do plano enquanto o arquivo
   do parecer não estiver na main (princípio V — nenhum número sem artefato).

## Alternativas consideradas

- **Incorporar sem verificar**: mais rápido — descartada: o parecer não tem
  artefato na main; a verificação independente do bib sustentou a incorporação.
- **Reordenar a fila unilateralmente**: o parecer sugere; descartada — ordem de
  trabalho é decisão do autor (vira DECISÃO na fila, não mudança silenciosa).
- **Gate final implícito ("quando tudo estiver feito")**: descartada — gate que
  não aparece no painel não governa nada.

## Consequências

- (+) O defeito real de bibliografia (fabricação/duplicatas) entra no plano com
  lente correta antes do R3 rodar.
- (+) Encerramento com aprovação explícita do autor e do orientador, visível.
- (−) Fila do autor cresce para 13 itens (2 são decisões) — o painel deixa o
  custo de decisão explícito em vez de escondê-lo.

## Registro

Plano v4; compute-kpis com tipo "decisao"; template com rótulo DECISÃO; este
ADR; linha no decisoes.jsonl. Pendência externa: push de docs/parecer-ars-r6.md
pela sessão que o produziu.
