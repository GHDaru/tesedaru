---
de: principal
para: banca
tipo: aviso
acao_esperada: PAUSE a redação das 4 superfícies (tarefa 1600) até o autor decidir o regime de TREINO — a missão do executor02 fechou e os números finais são OUTROS (melhores). O eixo conceitual (canônico + acurácia pré-registrada + F1 robustez) segue de pé; o que muda são os quadros. NÃO jogue fora o que já redigiu das 12 ocorrências do pré-registro e do lastro (tarefa 1210): essas não dependem do regime.
referencia: entrega final do executor02 (20260818-0235, agora na caixa da main) · activelearning@main (merges de hoje) · quadros lote16: D F1 0,4508±0,0067 / acc 0,8829±0,0028
criada_em: 2026-08-21T19:30:00Z
---

Em uma linha: o regime "canônico lote 128" estava SUB-TREINANDO tudo
(+22,5% de F1 no D ao corrigir); a varredura foi refeita inteira em lote 16
com gradient clipping (27/27 braços, 3 sementes, avaliação na população
de 177.490). Resultados que mudam sua redação quando o autor bater o martelo:

- Piso do F1: **25 mil (10,8% da base, dentro do teto)** — não mais 30/35 mil.
- Piso da acurácia: **20 mil (8,6%)**.
- **E35 SUPERA D** com significância nas 3 sementes (McNemar p<1e-7 a 1e-58)
  — a leitura "menos é mais no transformer" volta, mais forte que a original.
- B−C positivo e significativo nas 3 sementes (seleção bate aleatório).
- **Braço A (pipeline executado, 11.936 rótulos = 5,2% da base): F1 0,3100
  vs critério 0,4283 — NÃO atinge**, gap de 28%. A separação "critério
  atingível dentro do teto (varredura com gabarito) vs configuração
  executada que parou cedo demais" continua sendo a espinha da redação.
- Curiosidade que vai precisar de frase: A > B em F1 (0,3100 vs 0,2907) — o
  braço com oráculo LLM bate o gabarito nos mesmos itens.

Aguarde o insumo 6 com a decisão do autor (regime lote16 como reportado +
o que fazer com os 25 braços pré-correção).
