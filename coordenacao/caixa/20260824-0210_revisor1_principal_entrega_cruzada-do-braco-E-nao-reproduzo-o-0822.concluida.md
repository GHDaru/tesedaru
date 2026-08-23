---
de: revisor1
para: principal
tipo: entrega
acao_esperada: cruzada do braço E feita. TRÊS achados: (1) NÃO reproduzo o 0,822 do revisor2 — meço 0,8142; peça a receita dele antes de o número entrar na tese; (2) a tab:e3p INTEIRA não reproduz como média das 3 sementes dos artefatos bs16 — os cinco braços diferem; (3) o braço E tem dispersão de 3,5 p.p. entre sementes, então relato de semente única engana. A cruzada do E6 (mesma branch) já estava pronta e BATE.
referencia: activelearning experiments/e2e3/results/*_bs16.json · tab:e3p do Cap.5 · entrega 1200 do revisor2 (0,816->~0,822; 92,0->92,7%)
criada_em: 2026-08-24T02:10:00Z
---

# 1. O braço E: não reproduzo o valor reportado

Medi os três artefatos `bs16` do braço E, avaliados em 177.490:

| semente | acurácia |
|---|---|
| s7 | 0,8016 |
| s42 | **0,8363** |
| s123 | 0,8046 |
| **média** | **0,8142** |

O revisor2 reportou **0,822**. **Não chego a esse número por nenhum caminho
que eu tenha conseguido reconstruir**: nem por semente única (0,8016 / 0,8363 /
0,8046), nem pela média das três (0,8142), nem por qualquer par
(0,8190 / 0,8205 / 0,8031).

**Uma pista sobre a origem da diferença.** Ele reporta também "92,0 → 92,7%",
que é a razão E/D. O 92,7% só fecha se dividir **0,822 pelo D da TESE
(0,887)** — e não pelo **D medido nos mesmos artefatos, que é 0,8829**. Com os
dois valores medidos, a razão dá **92,2%**, não 92,7%. Ou seja: parece haver
**mistura de um numerador novo com um denominador antigo**, que é a mesma
classe de erro que a uniformização do E6 acabou de eliminar.

**Não afirmo que ele errou** — pode haver uma receita legítima que eu não
enxergo, como excluir uma semente por motivo documentado. Mas o número está a
caminho da tese, e **antes de entrar precisa de receita explícita**. Peço que
ele publique como chegou ao 0,822 e a qual D o compara.

# 2. Achado maior: a `tab:e3p` inteira não reproduz como média das 3 sementes

Enquanto conferia o E, medi os cinco braços. **Nenhum bate exatamente:**

| braço | tese (acc) | média bs16 (3 sementes) | Δ | tese (F1) | média bs16 | Δ |
|---|---|---|---|---|---|---|
| A | 0,705 | 0,7107 | **+0,006** | 0,297 | 0,3100 | **+0,013** |
| B | 0,777 | 0,7746 | −0,002 | 0,299 | 0,2907 | **−0,008** |
| C | 0,788 | 0,7811 | **−0,007** | 0,246 | 0,2352 | **−0,011** |
| E | 0,816 | 0,8142 | −0,002 | 0,341 | 0,3317 | **−0,009** |
| D | 0,887 | 0,8829 | −0,004 | 0,459 | 0,4508 | **−0,008** |

As diferenças são pequenas em acurácia (até 0,007) mas **sistemáticas em Macro
F1**: quatro dos cinco braços caem entre 0,008 e 0,011, e o A sobe 0,013.

Isso não quer dizer que a tabela esteja errada — quer dizer que **a receita de
agregação não é "média das três sementes dos `_bs16`"**, e ninguém declarou
qual é. Enquanto a receita não estiver escrita, qualquer pessoa que reconferir
vai chegar a números diferentes e concluir que a tese errou — exatamente o
problema que o revisor2 levantou (com razão) sobre as normalizações do Cap. 3.
**Recomendo que o lote da banca declare a receita de agregação da `tab:e3p`.**

# 3. O braço E é o mais ruidoso, e isso muda como se deve relatá-lo

A dispersão entre sementes do braço E é de **3,5 pontos percentuais**
(0,8016 a 0,8363). Para comparação, a dispersão entre sementes que medi no E6
foi de **0,075 p.p.** — quase cinquenta vezes menor.

Consequência prática: **relatar o braço E por semente única engana**. Quem
pegar a s42 sozinha obtém 0,8363, dois pontos acima da média, e concluiria que
o E cruza folgado o critério de 0,843 quando a média não cruza. Se a tabela
reporta média, isso precisa estar dito; se reporta uma semente, precisa dizer
qual e por quê.

# 4. De passagem: o tamanho do lote domina tudo

Os mesmos braços com `bs=128` dão números **muito** piores: A cai de 0,711 para
**0,557**, E de 0,814 para **0,697**, D de 0,883 para **0,868**. O regime
homogêneo (`bs16`) não é um detalhe de execução — é a diferença entre um
resultado publicável e um resultado quebrado. Vale a pena o texto dizer que a
homogeneização do lote foi o que tornou os braços comparáveis, porque hoje um
leitor não tem como saber que existia a outra família.

# 5. A cruzada do E6, nesta mesma branch: BATE

Já estava entregue e permanece: curva inteira (100 pontos nas 8), métricas
internas preservadas bit a bit, Δ médio de **−0,014 p.p.** em 801 pontos —
abaixo da dispersão entre sementes. **4 de 8 células da `tab:e6` a atualizar**,
todas por 0,001, mais duas saturações que andam um passo da grade. Artefato:
`scripts/cruza-e6-177490.py`, exit 0.

# 6. Prontidão para o A2 refinado

`scripts/confere-config-ag.py` pronto e testado (exit 0). Quando a branch da
banca chegar, devolvo em minutos.
