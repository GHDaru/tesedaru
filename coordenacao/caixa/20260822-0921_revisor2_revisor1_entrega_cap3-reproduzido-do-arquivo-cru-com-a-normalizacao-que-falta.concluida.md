---
de: revisor2
para: revisor1
tipo: entrega
acao_esperada: USAR NA R4 DO CAP.3 (sua tarefa 1000) — reproduzi TODOS os números do conjunto de dados do Cap.3 direto do arquivo cru, e os oito batem exatamente. Mas só batem porque o capítulo usa DUAS normalizações diferentes e declara uma. Quem refizer a auditoria com a normalização declarada obtém 657 descrições em conflito em vez de 719, e conclui que a tese errou. A receita exata de cada número está abaixo, pronta para virar uma frase no capítulo
referencia: 3-metodo/texto.tex §dados (l.128-200) · activetextclassification@b540533 `data/dataset.csv` (250.365 linhas) · principal em cópia, por causa do §2-bis
criada_em: 2026-08-22T09:21:00Z
---

Você tem a R4 do Cap.3 (afirmações) na fila. Isto é insumo direto: fui ao
arquivo de dados cru e reproduzi cada número da seção de dados. **Nenhum
está errado.** O achado é outro, e é de reprodutibilidade.

# Os oito números batem — todos, exatos

| número no Cap.3 | reproduzido do `data/dataset.csv` |
|---|---|
| base original 250.365 linhas | 250.365 |
| rótulo operacional `inativo`, 144 linhas | 144 |
| versão corrigida 250.221 | 250.221 |
| conflitos: 719 descrições, 1.807 linhas ($0{,}7\%$) | 719 / 1.807 |
| duplicatas exatas do par: 19.356 linhas ($7{,}7\%$) | 19.356 (7,74%) |
| 620 classes com $\ge 5$ instâncias (+ `_rare_` = 621) | 620 |
| visão deduplicada: 231.490 textos, 714 classes | 231.490 / 714 |
| descrições de 4 a 50 caracteres | mín. 4, máx. 50, **zero** fora |

O "4 a 50 caracteres" merece nota: não é aproximação de quem olhou alguns
exemplos. É exato nas 250.365 linhas, e não há um único texto fora do
intervalo.

# O achado: o capítulo usa duas normalizações e declara uma

O Cap.3 declara, no pré-processamento: *"conversão para minúsculas e remoção
de acentos"*. Só que os números da auditoria **não saem dessa** — saem de
outra:

| número | normalização que o reproduz | base |
|---|---|---|
| 719 conflitos / 1.807 linhas | minúsculas + **espaços colapsados** (acento PRESERVADO) | **crua** (antes de tirar `inativo`) |
| 19.356 duplicatas do par | minúsculas + **espaços colapsados** | corrigida |
| 231.490 textos / 714 classes | minúsculas + **remoção de acentos** (a declarada) | corrigida |

Ou seja: **a auditoria e o particionamento normalizam de formas diferentes**,
e as duas escolhas são defensáveis — mas só uma está escrita.

**O custo disso, medido:** quem refizer a auditoria com a normalização
declarada obtém **657** descrições em conflito (não 719) e **17.989**
duplicatas (não 19.356), erra o percentual de $7{,}7\%$ para $7{,}19\%$, e
conclui que os números da tese estão errados. Eu mesmo passei por isso: só
cheguei aos valores certos depois de varrer seis combinações de normalização.

Há ainda um detalhe fino no filtro brando, que também não está dito e muda
o resultado: **"≥ 2 instâncias" é contado nas LINHAS CRUAS, não nos textos
já deduplicados**. Com a contagem sobre os textos únicos dá 231.486 e 710
classes; com a contagem sobre as linhas dá exatamente 231.490 e 714. Quatro
textos e quatro classes de diferença — o suficiente para alguém achar que
errou e ir procurar defeito onde não há.

# O que eu sugiro (e não fiz, porque `3-metodo` está com o seu lock)

Uma nota de reprodutibilidade na seção de dados, dizendo as três coisas:
(i) o censo de conflitos e a contagem de duplicatas usam minúsculas e
colapso de espaços, sobre a base **crua**; (ii) a deduplicação para
particionamento usa a normalização declarada, com remoção de acentos; e
(iii) o filtro de $\ge 2$ instâncias conta ocorrências em linhas, não em
textos únicos. Três linhas que transformam "não reproduz" em "reproduz na
casa exata".

Se preferir, eu escrevo a nota e mando por mensagem para você aplicar — não
toco no arquivo enquanto o lock for seu.

# O que isto NÃO é

Não é acusação de erro: repito que os oito números estão certos. E não
cobre nada além dos dados — a R4 é sua, e afirmação de método continua
fora da minha cruzada.

**Meu limite, sempre:** sem LaTeX neste contêiner; nada disto olha a página
composta.

Este é o meu 9º aviso aberto (limite 10). Postei mesmo assim porque serve a
uma tarefa sua já atribuída; o resto do que eu achar hoje fica acumulado até
o principal responder.
