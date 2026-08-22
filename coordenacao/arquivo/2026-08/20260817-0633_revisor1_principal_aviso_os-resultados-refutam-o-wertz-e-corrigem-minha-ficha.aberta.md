---
de: revisor1
para: principal
tipo: aviso
acao_esperada: levar ao autor — (1) o E6 CONTRARIA o Wertz2022 e a tese não diz isso, o que é contribuição sendo desperdiçada; (2) correção de um claim MEU, que estava errado; (3) o Cap.4 segue com ZERO citações apresentando como novo um mecanismo que tem literatura
referencia: 5-resultados-falco/texto.tex §E6 (Tab. tab:e6) · 4-resultados-l0/texto.tex L49-53 · fichamentos/Griesshaber2020.md · docs/uso-declarado-vs-citacao-real.md
criada_em: 2026-08-17T06:33:28Z
---

# Fui aos resultados conferir os meus próprios achados. Um deles estava errado.

O autor pediu para verificar se os achados da varredura tinham ido para algum
lugar. Abri o Capítulo 4 e o E6 do Capítulo 5. Três conclusões, e começo pela
que me desabona.

## 1. CORREÇÃO — o meu claim de "ameaça" no `Griesshaber2020` está errado

Hoje de manhã fichei o `Griesshaber2020` e registrei, com destaque, um
`falco_relation: ameaca`: a seleção por incerteza desequilibra as classes, foi
medido com 2-3 classes, o FALCO tem 621, **logo seria ameaça**.

**Os resultados da tese dizem o contrário, e já diziam antes de eu escrever.**

O achado (ii) do E6: o Macro F1 populacional chega a $0{,}59$ com ~15 mil
rótulos selecionados por entropia e **cai para $0{,}44$ quando o pool inteiro é
rotulado** — *"porque a amostra ativa é mais balanceada por classe que a
distribuição natural"*. O achado (iv): estratificar pelas classes previstas
captura quase todo o ganho, porque *"o que a métrica macro paga é cobertura
balanceada de classes"*.

Ou seja: o desbalanceamento induzido pela seleção ativa **não é a ameaça, é a
fonte do ganho**. Eu escrevi uma ameaça sobre um capítulo que não tinha aberto.

É o anti-padrão nº 23 que eu mesmo propus — diagnosticar contra a cópia
desatualizada — na versão mais constrangedora: a cópia desatualizada era a
minha ignorância do próprio repositório. Vou corrigir a ficha.

## 2. Mas a correção revela um achado melhor: o SINAL do efeito depende do pool

As duas evidências não se contradizem. Elas se reconciliam pela distribuição
do pool, e é isso que vale escrever na tese:

| | `Griesshaber2020` | FALCO (E6) |
|---|---|---|
| Classes | 2 a 3 | 621 |
| Pool de origem | GLUE, aproximadamente balanceado | natural, fortemente enviesado |
| Efeito da seleção ativa | **desequilibra** (4 a 10× o aleatório) | **equilibra** (mais que a natural) |
| Consequência | prejudicial | **é o ganho** |

**O sinal do efeito de viés de classe depende de o pool ser balanceado ou
torto.** Num pool balanceado, a seleção por incerteza afasta do equilíbrio;
num pool torto, puxa para ele. É uma condição de contorno que explica as duas
literaturas de uma vez, e a tese tem as duas pontas na mão sem ter escrito a
ligação. Material de Cap. 5 (discussão) e Cap. 6.

## 3. O `Wertz2022` continua fora do Cap. 5 — e agora o argumento é muito mais forte

No aviso das 0630 eu disse que ele deveria ser citado. Agora sei **por quê**, e
é mais do que eu supunha: **a tese tem a medição que responde à alegação dele.**

O `Wertz2022` afirma que, em classificação com rótulo extremo (centenas de
classes), nenhuma estratégia de seleção supera a aleatória de forma
consistente. O E6 mede exatamente isso, em 621 classes:

| Classificador | Entropia (teto / saturação) | Aleatório (teto / saturação) | Veredito |
|---|---|---|---|
| SGD | **0,591** / 8.000 | 0,459 / 16.500 | **contraria o Wertz** — 8/8 sementes, Wilcoxon $p=0{,}0078$ |
| PVBin | 0,529 / 19.000 | 0,530 / 40.000 | **teto empata** (6/8, não significativo) — concorda em parte |

É uma **refutação parcial e dependente do classificador** — que é exatamente o
tipo de resultado que uma tese quer ter, e é mais forte do que a redação atual,
que diz apenas *"a entropia domina em escala"*. Dominar em escala é uma
observação sobre o próprio experimento. **Contrariar um resultado publicado sob
condição declarada é contribuição.** E o empate no PVBin, longe de enfraquecer,
mostra que o autor sabe onde a própria vantagem não vale — o que a banca lê
como maturidade, não como fraqueza.

Repare ainda que a saturação do PVBin (19 mil contra 40 mil) **contraria o
Wertz por outro eixo** mesmo com o teto empatado: mesma qualidade final por
menos da metade do rótulo. O `Wertz2022` mede teto; a tese mede teto **e**
custo até o teto. Isso é uma distinção metodológica que vale explicitar.

## 4. Confirmado: o Capítulo 4 segue com ZERO citações

Recontei: **0**. E ele apresenta como observação própria o mecanismo
*"Cobertura de classes como mecanismo: em $I=10$ o $L_0$ típico cobre 9 das 621
classes; em $I=1.000$, cerca de 255; a curva de Macro F1 segue de perto a curva
de cobertura"* (L49-53).

Esse mecanismo **tem literatura**, e ela está fichada e não citada em lugar
nenhum: o `Bengar2022ClassBalanced` é aprendizado ativo balanceado por classe,
tem ficha, e não aparece em nenhum capítulo. O `Griesshaber2020` mede a mesma
coisa pelo outro lado.

Não é que a observação da tese esteja errada — ela está certa e é bem medida.
É que apresentá-la sem interlocutor a faz parecer menor do que é, e deixa a
banca perguntar "isso não é conhecido?" quando a resposta boa seria "é, e nós
medimos em 621 classes, onde não havia medida".

## 5. O que JÁ chegou, e eu registro para dar crédito

`Farquhar2021Bias` e `Kossen2021ActiveTesting` **estão no lugar certo**: o E6
os cita para o viés de autoavaliação, e o achado (v) credita o mecanismo ao
Kossen nominalmente. Minha varredura os acusou porque prometiam **também** os
Caps. 2, 3 e 6 — a promessa do Cap. 5 foi cumprida. Bom exemplo de que a
varredura aponta candidatos, não defeitos.

## O que peço

Levar ao autor os itens 2, 3 e 4. São decisões de conteúdo e nenhuma é minha.
O item 3 é o de maior retorno: **um parágrafo no E6 dizendo contra quem o
resultado está** transforma uma observação em contribuição, e o material já
está todo medido.

Vou corrigir a ficha do `Griesshaber2020` por conta própria — o claim errado é
meu e está na minha superfície.
