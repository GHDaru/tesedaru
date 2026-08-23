---
de: revisor1
para: principal
tipo: entrega
acao_esperada: CRUZADA DO E6 CONCLUÍDA — BATE. O executor01 fez exatamente o que a recomendação pedia. 4 das 8 células da tab:e6 têm valor a atualizar (todos de 0,001, mais DUAS saturações que andam um passo da grade). UM ponto exige decisão sua: a tabela vai passar a MISTURAR denominadores (8 células em 177.490, 2 PVBin em 181.490) e isso precisa ser declarado na legenda.
referencia: activelearning@264818c · scripts/cruza-e6-177490.py (exit 0) · minha recomendação da tarefa 1720 · tab:e6 do Cap.5
criada_em: 2026-08-24T00:30:00Z
---

# 1. Bate. E bate pelo motivo certo.

Conferi as três precisões que eu tinha pedido na recomendação, e **as três
foram cumpridas**:

| o que eu pedi | o que foi feito |
|---|---|
| curva INTEIRA, não só o ponto final | **100 pontos** em cada uma das 8 |
| re-avaliação, **não** re-seleção | a trajetória é a mesma; só o conjunto de avaliação mudou |
| métricas INTERNAS transportadas sem recálculo | **`acc_int` idêntico bit a bit nas 8** |

E o executor01 fez algo melhor do que eu pedi: **guardou o valor original de
181.490 ao lado do novo em cada linha**. É o que torna esta cruzada
verificável ponto a ponto em vez de agregado contra agregado.

# 2. O tamanho do efeito: menor ainda do que eu previa

Em **801 pontos** comparados:

- Δ acurácia: média **−0,014 p.p.** (máx |Δ| 0,140)
- Δ Macro F1: média **−0,015 p.p.** (máx |Δ| 0,080)

Eu havia previsto ≈0,04 p.p. É **três vezes menor**. Contra a dispersão entre
sementes que medi antes (0,075 p.p. em acurácia, 0,354 p.p. em F1), o efeito da
troca de denominador é **19% do desvio em acurácia e 4% em F1**. **Nenhum
veredito da tese se move.** A correção era certa por princípio — um único
denominador — e é imaterial em magnitude, como se esperava.

# 3. O que a banca precisa mudar na `tab:e6`: 4 células de 8

| célula | teto | saturação | F1@10k | F1@20k |
|---|---|---|---|---|
| sgd\_entropy | **0,591 → 0,590** | 8.000 = | 0,565 = | **0,574 → 0,573** |
| sgd\_random | **0,459 → 0,458** | **16.500 → 15.500** | 0,391 = | **0,449 → 0,448** |
| sgd\_drisl-cs | 0,555 = | **10.000 → 9.500** | 0,533 = | 0,543 = |
| pvbin\_drisl-c | 0,525 = | 39.500 = | 0,349 = | **0,453 → 0,452** |
| (as outras 4) | — sem alteração — | | | |

Todas as mudanças de F1 são de **0,001**. As duas saturações que andam são
**efeito de discretização**, não de comportamento: saturação é o primeiro ponto
que atinge 95% do teto, então um teto 0,001 menor baixa o limiar e um ponto
anterior da grade passa a qualificar. Um passo de grade em `drisl-cs`, dois em
`random`.

**Verifiquei a frase do texto que depende disso** e ela sobrevive: "a entropia
satura com 8.000 rótulos no SGD, metade do que a aleatória exige" — com a
aleatória em 15.500, a razão vai de 2,06× para 1,94×, e "metade" continua
honesto.

# 4. O ponto que exige DECISÃO sua

Com 8 curvas em 177.490 e as **2 PVBin travadas em 181.490**, a `tab:e6`
**passa a misturar denominadores entre linhas**. Numericamente é irrelevante
(0,02 p.p.), mas é exatamente a mistura que a uniformização existia para
eliminar — só que agora entre linhas da mesma tabela, em vez de dentro da
curva. Foi o risco que apontei na recomendação: *"se a tabela migrar e a faixa
das sementes ficar para trás, recriamos entre parágrafos a mistura que estamos
eliminando dentro da curva."*

**Não é impeditivo, e não recomendo segurar a tabela por isso.** Recomendo
**declarar na legenda**: dizer que as células de PVBin Entropia e PVBin
Aleatório são avaliadas em 181.490, com a razão (execuções travadas) e a
magnitude da diferença (0,02 p.p.). Uma linha na legenda transforma uma
inconsistência silenciosa em limitação declarada — princípio VI.

# 5. Um defeito HERDADO, que não é do executor01

A curva `sgd_drisl-c` tem **101 pontos**: o `n_labels=2000` aparece duas vezes.
Fui à curva original e **a duplicação já estava lá**, com dois valores
diferentes para o mesmo ponto (0,7015 e 0,7006 de acurácia). O executor01
reproduziu fielmente as duas linhas, cada uma com o seu original.

Curiosamente, **a reavaliação resolve a inconsistência**: como ela é
determinística dado o `labeled_idx`, as duas linhas agora dão o **mesmo** valor
novo (0,7006). O defeito é do artefato original — provavelmente um reinício de
execução — e não afeta nenhum dos quatro números reportados. Registro para não
virar susto de quem reconferir.

# 6. Artefato

`scripts/cruza-e6-177490.py`, **exit 0**. Reexecutável; falha se alguma métrica
interna tiver sido alterada, e imprime as quatro grandezas da tabela lado a
lado com as publicadas. Nenhum número desta entrega existe sem ele.

# 7. Prontidão para o A2 refinado

Pronto e testado: `scripts/confere-config-ag.py` (exit 0) já confirma o
critério e delimita o estrago. Quando a branch da banca chegar, rodo contra ela
e devolvo em **minutos**. Lembro as duas ressalvas que o critério não cobre e
que a reescrita precisa absorver: o **$L_0=10$ fez 200 gerações e 4.000
avaliações** (a regra única "100 gerações / 2.000" mentiria para um dos oito
tamanhos), e existe uma **terceira configuração** no repositório (pop 100),
que não alimenta a tese mas desfaz a dicotomia.
