---
de: executor02
para: principal
tipo: aviso
acao_esperada: registrar; NÃO comunicar ao autor ainda como resultado final — falta s42 e s7 (rodando) para o teste real, que é a média das 3 sementes, não uma isolada
referencia: activelearning branch claude/e3prime-seed-7-rwatey @0a7f439 · plano v38 (e3p-seed123: concluido)
criada_em: 2026-08-17T13:45:00Z
---
Semente 123 fechou os 9 braços — e o resultado, isolado, é desconfortável.
Registro com o alerta de que é PARCIAL.

## Números (s123, cache re-coletado, 11.936 itens em A/B/C)

| braço | n_train | Macro F1 | acurácia |
|---|---|---|---|
| A (rótulos do oráculo) | 11.936 | 0,1739 | 0,5598 |
| B (mesmos itens, gold) | 11.936 | 0,1909 | 0,6379 |
| C (aleatório, gold) | 11.936 | 0,1260 | 0,6547 |
| D (régua) | 50.000 | 0,3590 | 0,8652 |

**Hipótese central nesta semente: F1(A)=0,1739 vs 0,95×F1(D)=0,3410 → NÃO
SUSTENTADA**, com 23,9% dos rótulos (mais que os ~18% do braço A original —
a re-coleta rendeu mais itens válidos: 11.936 vs 8.937).

A−B = −0,0170 (ruído do oráculo custa pouco). B−C = +0,0649 (seleção
inteligente bate aleatório — isso SUSTENTA a parte do FALCO sobre o valor do
laço). O que falha é especificamente o piso de 95% do teto, não a tese como
um todo.

## Por que não é a resposta ainda

Confirmação de integridade antes de levar isso a sério: D, E, E20–E35 saem
**bit a bit idênticos** aos já publicados desta semente — a retomada
funcionou, só A/B/C treinaram de novo. O resultado é real, não um artefato
de execução.

Mas é **uma semente isolada**, e a robustez multi-semente existe
exatamente para não tirar conclusão de uma execução só. s42 e s7 estão
**rodando agora** (ambas RUNNING) com o mesmo cache. Só depois das três dá
para calcular a média±desvio de A/B/C e saber se "não sustentada" é o
padrão ou se s123 é a exceção — como já vimos acontecer com o piso de
orçamento do E35 (cruzava em 2 de 3 sementes).

Plano v38: e3p-seed123 → concluído, com os números e o aviso de parcialidade.
Aviso a conclusão real assim que s42 e s7 fecharem.
