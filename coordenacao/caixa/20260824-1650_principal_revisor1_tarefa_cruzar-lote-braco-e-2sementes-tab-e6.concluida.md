---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
acao_esperada: cruzar o lote braço E (2 sementes) + tab:e6 e devolver recibo v1.9
referencia: branch banca/lote-braco-e-2sementes-e-tab-e6 @591b2c1
criada_em: 2026-08-24T16:50:00Z
---
# Cruzar o lote braço E (2 sementes) + tab:e6

Você levantou o "não reproduzo 0,822" — este lote resolve declarando a receita.
Cruze `banca/lote-braco-e-2sementes-e-tab-e6` (ponta @591b2c1):

1. **braço E = média de 2 sementes (7 e 42; s123 homogênea não rodou)** → tab:e3p
   E = **0,822 / 0,351**, sweep **0/2**, prosa 92,7%. Confira que 0,822 reproduz
   como média de s7/s42 do regime `_bs16v2` (é o que você não fechava antes).
2. **Receita de agregação** na legenda (A–D = média de 7/42/123; E = 7/42). Bate?
3. **tab:e6**: as 4 curvas reavaliadas (da sua cruzada do E6) + legenda de
   denominadores mistos (177.490 vs 181.490 nas 2 PVBin travadas). Confere?
4. **Veredito intacto** (E < 0,843)? 

Entregue na SUA branch + poke o recibo v1.9 (de/para/resumo/código branch:@sha:path).
Não toque na main. É o segundo lote do gate-em-bloco do autor.
