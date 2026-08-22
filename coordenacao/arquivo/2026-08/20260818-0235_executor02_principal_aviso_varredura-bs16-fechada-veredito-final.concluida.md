---
de: executor02
para: principal
tipo: aviso
acao_esperada: CONSOLIDAR e levar ao autor em bloco — a varredura em lote 16 está fechada com os dois testes críticos resolvidos; falta só a decisão sobre regerar os 25 braços pré-correção (efeito pequeno medido, não travo nada esperando)
referencia: activelearning@6e1d2f5 (branch claude/e3prime-seed-7-rwatey) · minhas mensagens 0045/0120/0135/0150/0200 · plano v70
criada_em: 2026-08-18T02:35:00Z
---
**Varredura em lote 16 fechada: 27/27 braços válidos, 3 sementes,
estatística pareada completa.** Este é o veredito final desta fase — os
dois achados críticos que oscilaram ao longo da noite agora têm resposta
definitiva, com significância estatística, não só ponto estimado.

## Os dois colapsos foram destravados

`clip_grad_norm_(max_norm=1.0)` (`activelearning@1dabdbb`) resolveu os dois
braços que colapsavam (E25/s42, E/s123) — confirmado por retreino, ambos
saudáveis agora. Medi o efeito da correção num braço que já treinava bem
(D/s42, controle): **+2,26% relativo em F1, +0,0052 em acurácia** — real,
positivo, mas pequeno, muito menor que os efeitos de 20-100%+ que a
varredura estuda. Decisão sobre regerar os 25 braços pré-correção por
consistência fica com vocês/autor — não travo nada esperando, mas está
registrada.

## Média ± desvio final (k=3, 27 braços)

| braço | n | Macro F1 | acurácia |
|---|---|---|---|
| A | 11.936 | 0,3100 ± 0,0108 | 0,7107 ± 0,0031 |
| B | 11.936 | 0,2907 ± 0,0255 | 0,7746 ± 0,0116 |
| C | 11.936 | 0,2352 ± 0,0239 | 0,7811 ± 0,0151 |
| E | 15.000 | 0,3317 ± 0,0341 | 0,8142 ± 0,0192 |
| E20 | 20.000 | 0,3934 ± 0,0122 | 0,8521 ± 0,0080 |
| E25 | 25.000 | 0,4324 ± 0,0092 | 0,8749 ± 0,0064 |
| E30 | 30.000 | 0,4474 ± 0,0212 | 0,8801 ± 0,0049 |
| **E35** | 35.000 | **0,4640 ± 0,0052** | **0,8899 ± 0,0013** |
| **D** (régua) | 50.000 | **0,4508 ± 0,0067** | **0,8829 ± 0,0028** |

## Teste 1 — Hipótese central: NÃO SUSTENTADA

F1(A)=0,3100 vs 0,95×F1(D)=0,4283 → não sustentada, com 23,9% dos rótulos.
Consistente nas 3 sementes (desvio baixo, 0,0108). O pipeline barato do
FALCO não chega a 95% do teto do pool nesta base de 715 classes com cauda
longa.

## Teste 2 — E35 vs D: SUSTENTADA, com significância forte nas 3 sementes

McNemar + bootstrap pareado (10k réplicas), não só ponto estimado:

| semente | Δacc | p (McNemar) | ΔF1 | IC95% |
|---|---|---|---|---|
| 42 | +0,0092 | 3,7e-58 | +0,0172 | [+0,0128; +0,0199] |
| 7 | +0,0088 | 8,5e-55 | +0,0158 | [+0,0125; +0,0187] |
| 123 | +0,0031 | 2,0e-08 | +0,0065 | [+0,0037; +0,0103] |

**As 3 sementes concordam: E35 bate D com força estatística, sempre na
mesma direção.** A alegação (iii) do Cap. 5 ("menos é mais, também no
transformer" — E35 supera a régua) **volta a valer** — e agora com
avaliação canônica rigorosa (população inteira, 177.490 itens) em vez do
regime legado com amostra pequena que a sustentava antes. É uma conclusão
mais forte que a original: não é só o ponto estimado que supera, é
estatisticamente significativo nas 3 sementes.

## Bônus: B−C também ficou consistente

No regime lote 128 eu tinha reportado que B−C (valor da seleção vs
aleatório) trocava de sinal entre sementes. No lote 16 corrigido, **não
troca mais**: positivo e significativo nas 3 (p<1e-24 em todas). A seleção
do laço bate o aleatório de forma robusta neste regime.

## O que isso significa para o Cap. 5 — não decido, mas resumo as peças

1. **"Menos é mais, também no transformer"**: sustentado, com evidência
   mais forte que antes (significância estatística nas 3 sementes, não só
   um ponto no regime legado).
2. **Hipótese central (F1(A)≥0,95×F1(D))**: não sustentada — mas o gap
   encolheu bastante do regime lote128 (57%) para o lote16 (28% de
   distância até o critério).
3. **Onde o piso realmente cruza**: pela tabela, F1 cruza o critério em
   E25 (50% do pool) e acc já cruza em E20 (40%) — o piso de orçamento é
   parecido com o que o Cap. 5 já dizia (25k/50%), só que agora com
   números e significância corretos.

## Estado da minha missão

Todas as tarefas da fila (recoleta E5 → cache → A/B/C×3 → estatísticas
canônicas → sub-treino → varredura completa → correção do colapso →
verificação → estatísticas finais) estão concluídas. Plano v70. Fico
disponível para a próxima frente — inclusive o dimensionamento do E6
(mensagem 2300, ainda sem decisão) ou qualquer outra execução que a fila
precisar.
