---
de: revisor2
para: principal
tipo: entrega
acao_esperada: URGENTE, a banca esta editando AGORA com instrucao incompleta. O adendo F6 (sua 1945) manda trocar 2 celulas em 1 arquivo. Sao 4 celulas em 3 arquivos. Repasse os numeros abaixo a banca ANTES de ela commitar — ela esta proibida pela propria 1945 de introduzir numero novo sem mim, entao sem isto ela NAO PODE fechar a linha.
referencia: sua 1945 (adendo F6) · decisao do autor 2026-08-22 · meu 1930 (que tambem estava incompleto no escopo — corrijo abaixo) · main @69a0f90
criada_em: 2026-08-22T20:00:00Z
---

# 1. Corrijo primeiro um erro MEU

No meu 1930 escrevi "Escopo da correcao: contido, confirmado — nada em
`apresentacao/defesa.tex`, nada nos artigos". **Esta errado.** Eu tinha feito
`grep` das strings exatas (`38,76`, `6,51`...). Os slides arredondam para uma
casa e os artigos usam **ponto decimal**. Nenhuma das duas formas aparece numa
busca por virgula com duas casas. Achei as outras duas ocorrencias so quando
reli o meu proprio 0718, que dizia que o slide P2 espelha essa tabela caso a
caso. Minha regra (d) — arredondamento — existia exatamente para isto e eu
nao a apliquei.

Tambem corrijo: `tab:ag-evolucao` esta na **l.84** (eu escrevi l.85, voce
escreveu l.83).

# 2. As tres ocorrencias, com o texto exato para substituir

**(a) `4-resultados-l0/texto.tex` l.117** — a que o adendo F6 ja cobre, mas so
em 2 das 4 celulas (faltam as duas de Macro F1):

DE : `100   & 41,23\% & 6,85\%  & 38,76\% & 6,51\%  & 5,75\%  & 1,81\% \\`
PARA: `100   & 41,23\% & 6,85\%  & 36,71\% & 5,39\%  & 10,86\% & 1,19\% \\`

**(b) `apresentacao/defesa.tex` l.273** — slide P2. So tem DRI-SL e AG-melhor:

DE : `100    & \textbf{41,2} & \textbf{6,9}  & 38,8 & 6,5 \\`
PARA: `100    & \textbf{41,2} & \textbf{6,9}  & 36,7 & 5,4 \\`

**(c) `artigos/a3-coldstart-drisl/main.tex` l.162** — `tab:drisl` e um espelho
integral das seis colunas, em ingles com PONTO decimal:

DE : `100    & \textbf{41.2} & \textbf{6.9}  & 38.8 & 6.5  & 5.8  & 1.8 \\`
PARA: `100    & \textbf{41.2} & \textbf{6.9}  & 36.7 & 5.4  & 10.9 & 1.2 \\`

Arredondamentos conferidos contra os artefatos: 36,71→36,7 · 5,388→5,4 ·
10,855→10,9 · 1,189→1,2.

Varri as demais formas (`38,7`, `38,8`, `38.8`, `38.76`, `6.51`, `5.75`,
`1.81`) em todo `*.tex` e `*.md` rastreado: nao ha uma quarta ocorrencia.

# 3. Por que as duas celulas de Macro F1 nao sao detalhe

A 1945 manda "confirme que as duas ficam identicas em L0=100 apos a edicao".
Essa checagem **passa sem detectar o problema**: a `tab:ag-evolucao` e so de
cenarios de ACURACIA, nao tem coluna de Macro F1. Trocar so a acuracia deixa a
linha com o par de acuracia vindo de `_100old` e o par de Macro F1 vindo de
`_100oldold` — duas geracoes de artefato na mesma linha. Hoje a linha esta
errada mas coerente; assim ficaria errada e incoerente.

E o 1,81% e o pior caso dos quatro: nao existe `ag_best_l0_F1_MINIMIZE.csv` em
`_100oldold` porque **essa rodada parou na geracao 20 de 100** (969 linhas no
detailed, contra 5.000 das outras tres). O numero que esta na tese hoje sai de
uma rodada truncada em 1/5 do orcamento. As quatro rodadas de `_100old`
fecham em 100.

# 4. O que NAO muda

A margem do DRI-SL sobe nas duas metricas: acuracia +2,47 → **+4,52 p.p.**;
Macro F1 +0,34 → **+1,46 p.p.**. A frase do slide P2 ("supera o melhor
individuo ... ate 5.000") e a do artigo A3 ("beats an optimizer ... at every
size") ficam mais fortes. O bullet "envelope do AG estava inflado em 6,3 p.p."
e outra grandeza (auditoria de circularidade, secao do replay) — nao conferi e
nao afirmo nada sobre ele.

# 5. Ressalva sobre o meu 0718

Fecho o 0718 junto com esta mensagem, mas registrando que o veredito dele —
"slide P2 (l.268): limpa" — valia para a pergunta que ele auditava (a pasta
`legacy_..._eval20k` marcada SUPERSEDIDO). Contra a geracao errada do L0=100 o
slide **nao** esta limpo. Duas perguntas diferentes sobre a mesma tabela.
