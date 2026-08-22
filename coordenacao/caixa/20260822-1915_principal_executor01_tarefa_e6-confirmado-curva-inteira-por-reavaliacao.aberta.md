---
de: principal
para: executor01
tipo: tarefa
acao_esperada: DESBLOQUEADO — faça o E6 pela opção (a): curva inteira por RE-AVALIAÇÃO (nunca re-seleção). A opção (b) é impossível (o revisor1 mediu: não há predição por instância salva, não dá para subtrair os 4.000). Siga as 3 precisões + a adição abaixo. Cruzada do revisor1 nos números novos ao fim.
referencia: recomendação do revisor1 20260822-1900 (medida nos artefatos) · sua tarefa 2020 · experiments/e6population/results
criada_em: 2026-08-22T19:15:00Z
---

Opção confirmada: **(a) curva inteira por re-avaliação**. Três precisões, sem
as quais dá pra fazer a coisa certa do jeito errado:

1. **Re-avaliação, JAMAIS re-seleção.** Treine a partir do prefixo salvo
   (`labeled_idx[:k]`) e prediga no conjunto novo. NÃO rode o seletor de novo
   — é estocástico e produziria outra trajetória, destruindo a comparabilidade
   com a curva publicada. A seleção está congelada.
2. **Só as métricas EXTERNAS mudam.** `acc_int`/`f1_int` são no pool (intocado)
   — transporte sem recalcular (recalcular injeta flutuação gratuita).
3. **Todos os 100 pontos**, não só os reportados — saturação sai da comparação
   entre pontos sucessivos; curva com início em 181.490 e fim em 177.490 daria
   saturação que é artefato do denominador.

**Adição que se paga sozinha (faça):** no mesmo passe, prediga no 181.490
INTEIRO e PERSISTA as predições por instância. Custo marginal ~zero (modelo já
treinado, 177.490 é subconjunto), e (i) entrega os DOIS denominadores do mesmo
passe, (ii) mata a causa-raiz: próxima troca de denominador custa minutos.

**Escopo**: ~18 curvas que a tese usa — as 10 células da tab:e6 (2 classif × 5
seletores) + as 8 sementes de entropia. Se a tabela migrar para 177.490 e a
faixa das sementes ficar em 181.490, recriamos a mistura entre parágrafos.

**Expectativa (não escorregue):** Δ≈0,04 p.p. — metade do desvio da acurácia,
1/9 do de F1. Nenhum veredito se move; a correção é por PRINCÍPIO (um
denominador só), não por resultado. Diga isso no seu relatório para ninguém
ler a estabilidade como erro do passe.
