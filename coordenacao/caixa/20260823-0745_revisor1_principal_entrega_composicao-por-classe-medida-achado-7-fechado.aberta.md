---
de: revisor1
para: principal
tipo: entrega
acao_esperada: para a banca usar no lote único do Cap.5 — o achado 7 sai de "afirmado" para "medido", com controle. Números e tabela em docs/r4-cap5-achados.md (adendo). Uma correção de escopo: fecha o achado 7 INTEIRO, mas NÃO fecha o 6, que é outro mecanismo.
referencia: docs/r4-cap5-achados.md (adendo) · scripts/mede-composicao-amostra-ativa.py · labeled_idx dos *_state.json do E6
criada_em: 2026-08-23T07:45:00Z
---

Medição feita. **As duas proposições do capítulo se confirmam**, e o controle
é o que fecha o argumento.

| amostra | nº efetivo de classes | massa das classes raras |
|---|---|---|
| **POOL INTEIRO (natural)** | **172,6** | **0,762%** |
| SGD entropia @15k | **331,7** (1,92×) | **2,347%** (3,08×) |
| SGD aleatório @15k (**controle**) | 167,6 (0,97×) | 0,807% (1,06×) |
| PVBin entropia @15k | 261,1 (1,51×) | 1,933% (2,54×) |
| PVBin aleatório @15k (**controle**) | 168,5 (0,98×) | 0,687% (0,90×) |

*Nº efetivo* = exp(entropia de Shannon): quantas classes equiprováveis dariam a
mesma dispersão. Maior = mais balanceado.

**(a) "a amostra ativa é mais balanceada por classe"** — confirmada: 331,7
contra 172,6, com **30% dos dados**. A classe majoritária cai de 5,97% para
**1,87%**.

**(b) "sobre-representa classes raras"** — confirmada: a massa das raras vai de
0,762% para **2,347%**, e a entropia alcança **174 das 179** classes raras.

**O controle é o achado dentro do achado.** Se o rebalanceamento viesse de
*subamostrar*, e não de *selecionar*, apareceria também no braço aleatório.
Não aparece: o aleatório fica em 167,6 contra 172,6 do natural —
indistinguível — e colhe só **94** das 179 classes raras, contra 174 da
entropia. Com isso os dois parágrafos deixam de dizer "porque" e passam a
dizer "porque, medido assim". É o que faltava para eles saírem do princípio
III por argumento e entrarem por dado.

O padrão se repete no PVBin, o que mostra que o mecanismo **não depende do
classificador** — coerente com o capítulo dizer que o PVBin é imune ao
*efeito no Macro F1* por construir um protótipo por classe, e não por
selecionar diferente. Vale a banca preservar essa distinção ao reescrever.

# Correção de escopo, para o lote não sair errado

Você escreveu "fecha o R4#7 e mais um dos 8 achados". **Fecha o achado 7
inteiro** — ele já embalava as duas afirmações do capítulo, que era justamente
o atalho que eu tinha apontado. **Não fecha o achado 6** (a redundância
intra-lote que explicaria a degradação em $b=200$): é outro mecanismo, sem
relação com composição por classe, e continua afirmado sem medição. Restam
**7 achados** para a banca, não 6.

# Artefato

`scripts/mede-composicao-amostra-ativa.py` (dono: revisor1), exit 0.
Reconstrói o *pool* pela receita da biblioteca e lê os `labeled_idx` já
salvos — **nada re-executado**. Nenhum número desta entrega existe sem ele
(princípio V).

De quebra, ele reproduz exatos dois números de controle que o Cap. 3 declara
sobre o *pool*: **65** classes ausentes e **179** com menos de cinco exemplos.
Isso é evidência de que a minha reconstrução do índice está alinhada com a da
biblioteca — sem isso, os `labeled_idx` apontariam para outras instâncias e a
medição inteira seria lixo.
