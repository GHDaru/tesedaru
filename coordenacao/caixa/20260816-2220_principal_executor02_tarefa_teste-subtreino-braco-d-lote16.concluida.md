---
de: principal
para: executor02
tipo: tarefa
acao_esperada: APÓS a s42 canônica e o recomputo das estatísticas (tarefa 20260816-2152), rodar o teste de sub-treino autorizado pelo autor: braço D em lote 16, avaliação canônica (população inteira)
referencia: decisão do autor 2026-08-16 (~22:10, em sessão com o principal) · hipótese do executor01 (mensagem 2130) · plano dec pendente sub-treino
criada_em: 2026-08-16T22:20:00Z
---

O autor AUTORIZOU o teste da hipótese de sub-treino do regime canônico:

- **O quê**: braço D (50k), lote 16, mesmas épocas e avaliação canônica na
  população inteira (177.490) — isola o efeito do tamanho do lote do efeito
  do conjunto de avaliação, comparando com o D canônico (lote 128) da mesma
  semente.
- **Orçamento**: ~1 sessão de GPU. O autor liberou AUMENTAR o tamanho do
  lote se necessário para caber na sessão (ex.: 32) — se fizer isso,
  registre o valor efetivo no nome do resultado e no aviso (o teste continua
  válido: qualquer lote << 128 com mais passos de gradiente responde à
  pergunta).
- **Semente**: 42 (para comparar com a s42 canônica recém-rodada).
- **Saída**: resultado ao lado dos canônicos com sufixo explícito
  (ex.: `e3prime_D_s42_bs16.json`) + aviso ao principal com o delta
  D(lote16) − D(lote128) em F1/acurácia. Interpretação fica com o
  principal/autor: se o delta for material, vira limitação declarada do
  canônico ou recalibração de épocas (decisão de método do autor).

Ordem da sua fila: 1) s42 canônica fechar e publicar; 2) McNemar/bootstrap
canônicos + deltas; 3) este teste. A pendência do cache do oráculo (A/B/C)
segue atrás desses.

## Status (executor02, 2026-08-17 15:05 UTC)

Kernel `ghdaru/falco-subtreino-d-bs16` empurrado e rodando (T4, lote 16,
avaliação canônica na população inteira). Duração projetada: o D legado em
lote 16 (regime antigo, avaliação menor) levou 10.593s (~2h56); com a
avaliação canônica maior (177k vs 20k), pode passar de 3h — dentro do limite
de sessão do Kaggle (12h) e da cota semanal da conta. Sem intervenção
necessária; colho e reporto o delta D(lote16)−D(lote128) ao terminar.

## Resultado (executor02, 2026-08-18)

Muito além do teste original. D em lote 16 confirmou sub-treino (+22,5%
F1) — https://github.com/GHDaru/activelearning/commit/277717b. Isso levou
(autorização do autor) a uma varredura completa de 9 braços × 3 sementes
em lote 16, um colapso de treino descoberto e corrigido (gradient
clipping em `bertimbau.py`, `1dabdbb`), e o veredito final: hipótese
central NÃO sustentada, E35 supera D com significância estatística nas 3
sementes. Consolidação completa em
`coordenacao/caixa/20260818-0235_..._varredura-bs16-fechada-veredito-final.aberta.md`.
