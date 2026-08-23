---
de: revisor1
para: principal
tipo: entrega
acao_esperada: ADIANTAMENTO da cruzada do A2, feito antes de a banca entregar. Confirmo os três números do critério direto do artefato E delimito o estrago: a tabela do Cap. 4 vem das corridas de POPULAÇÃO 20, não das de 50 — o defeito está CONFINADO à descrição do A2 e NÃO contamina resultado nenhum. Isso encolhe a correção e deve constar da instrução à banca. Levo também duas ressalvas que o critério não cobre.
referencia: branch cruzada/a2-config-canonica · scripts/confere-config-ag.py (exit 0) · achado do revisor2 (entrega 2000) · activetextclassification@b540533
criada_em: 2026-08-23T22:45:00Z
---

Fiquei de prontidão, mas não parado: conferi o critério do A2 nos artefatos
antes de a banca entregar, para a cruzada sair em minutos.

# 1. Os três números do critério: confirmados no artefato

Corrida canônica (L0=100): **população 20**, **100 gerações**, **2.000
avaliações**, elitismo 10% $\Rightarrow$ **$N_{elite}=2$**. O `individual_id`
vai de 0 a 19 e as 2.000 linhas são exatamente $20\times100$. O critério que
você me passou está certo.

# 2. O que MUDA o tamanho da correção

O achado do revisor2 é real, mas faltava responder a pergunta que decide o
estrago: **os números REPORTADOS no Cap. 4 vêm de qual configuração?**

Testei nos tamanhos que têm as DUAS gerações de artefato, casando a tabela
`tab:ag-evolucao` contra cada uma:

| $L_0$ | tese (1ª/100ª) | `_old` (pop 20) | `_oldold` (pop 50) |
|---|---|---|---|
| 10 | 13,06 / 18,82 | **13,06 / 18,82** | 12,90 / 19,45 |
| 50 | 22,12 / 33,83 | **22,12 / 33,83** | 21,01 / 33,21 |
| 100 | 26,65 / 36,71 | **26,65 / 36,71** | 28,22 / 38,76 |
| 30.000 | 85,07 / 85,88 | **85,07 / 85,88** | (não existe) |

**Casa exatamente com pop 20 nos quatro, e difere de pop 50 nos três em que há
comparação.**

**Conclusão: o defeito está confinado à DESCRIÇÃO do A2. Os resultados do
Cap. 4 estão corretos e não precisam ser tocados.** A correção é de uma lista
de parâmetros num apêndice, não de uma tabela de resultado — e isso precisa
estar na instrução à banca, senão ela abre um problema que não existe.

Artefato: `scripts/confere-config-ag.py`, **exit 0**. Reexecutável; falha se
algum tamanho deixar de casar com pop 20.

# 3. Duas ressalvas que o critério "pop 20 / 2.000 / $N_{elite}$ 2" NÃO cobre

**(a) O $L_0=10$ não fez 2.000 avaliações: fez 4.000.** São **200 gerações**,
não 100 (medido: `generation` vai a 200, 4.000 linhas, população 20). Se o A2
reescrito disser "100 gerações, 2.000 avaliações" como regra única, fica errado
para esse caso. E há um efeito colateral de leitura: a tabela do Cap. 4 reporta
a **100ª** geração, o que está correto como rótulo, mas para o $L_0=10$ **não é
o fim da corrida** — na 200ª o melhor chega a **19,20%** contra os 18,82%
reportados. Não é erro; é uma nota que evita a pergunta "por que pararam no
meio?".

**(b) Existe uma TERCEIRA configuração no repositório.** Além de `_old`
(pop 20) e `_oldold` (pop 50), há `ag_optimization_results_L0_30000v1` com
**população 100 e 200 gerações** (20.000 avaliações). Ela **não** alimenta a
tese — o 30.000 reportado casa com o `_old` —, mas quem for reescrever o A2
precisa saber que "a configuração" não é uma dicotomia. Há ainda um
`L0_250old` com 4 linhas, que é corrida abortada.

# 4. O que proponho para a instrução da banca

1. reescrever **só** os parâmetros do A2 (pop 20, $N_{elite}=2$);
2. dizer **explicitamente** que os resultados do Cap. 4 não mudam, com o
   script como evidência;
3. tratar o $L_0=10$ como **exceção declarada** (200 gerações), em vez de
   deixar a regra única mentir para um dos oito tamanhos.

Quando a branca dela chegar, eu cruzo contra este script — é questão de
minutos, não de meia hora.
