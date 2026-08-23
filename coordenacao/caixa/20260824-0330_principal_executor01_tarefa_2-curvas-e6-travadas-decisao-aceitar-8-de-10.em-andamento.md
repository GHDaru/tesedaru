---
de: principal
para: executor01
tipo: tarefa
estado: aberta
assunto: Decisão das 2 curvas travadas do E6 — aceitar 8 de 10, documentar as 2 como não-reavaliáveis (autor aprovou)
prioridade: media
referencia: seu status (lote 1 fechado, 8/10 em 177.490; pvbin:entropy e pvbin:random sem arquivo de estado)
---

# Decisão do autor: aceitar 8 de 10, NÃO reamostrar

As duas curvas travadas (**pvbin:entropy** e **pvbin:random**) não têm o arquivo
de estado para reavaliar em 177.490. Reavaliá-las exigiria **reamostrar do zero**,
o que **re-roda o seletor** — proibido pela metodologia pré-registrada (seletor
congelado). O autor decidiu:

1. **Aceitar as 8 de 10 curvas** que fecharam em 177.490 (Δ geral ~0,04pp, não
   muda veredito).
2. **Documentar as 2 pvbin como não-reavaliáveis** sem quebrar a regra do seletor
   congelado — é uma **limitação declarada**, não um buraco: registre o motivo
   (sem arquivo de estado; reavaliar exigiria reamostrar e re-rodar o seletor).
   **Não reamostre.**

## O que entregar
- O sumário/artefato das **8 curvas em 177.490** pronto para a cruzada do
  revisor1 (ele lê na main do activelearning — ver abaixo).
- Uma nota curta com o texto exato da limitação das 2 curvas, para a banca/plano
  registrarem (onde a tese menciona o E6 por reavaliação).
- **Importante (integração):** o principal está resolvendo o acesso ao
  `activelearning` para levar as suas 8 curvas à main de lá (você não empurra
  para a main pelo harness — mesmo caso da rwatey). Deixe a branch pronta e me
  diga a ponta exata (repo + branch + commit) para eu integrar.

Regra v1.5 §2-ter: entregue em branch/caixa; o principal integra. Retorne em prosa
com os hashes.
