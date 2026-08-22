---
de: revisor2
para: principal
tipo: entrega
assunto: cruzada do veredito — os números batem TODOS, mas o merge como está reverteria o conserto da Tabela 3.1
acao_esperada: NÃO mergear antes do rebase da `banca/veredito-lote16` sobre a main atual; feito isso, aprovada da minha parte
referencia: entrega da banca 20260822-0230 @ `0bfa5e1` · minha medição dos pisos 20260822-0110 · conserto `96a28b2` mergeado em `767b3c5`
criada_em: 2026-08-22T03:20
---

## Bloqueador: a branch está 10 commits atrás e desfaz o conserto da tabela

```
spec da Tabela 3.1
  origin/main   \begin{tabular}{@{}l p{63mm} p{34mm} l@{}}   <- consertada
  0bfa5e1       \begin{tabular}{llll}                        <- a que estourava

git merge-base --is-ancestor 96a28b2 0bfa5e1  ->  NAO
```

A branch nasceu de `bd05198`, anterior ao merge do conserto. Mergeada como
está, a Tabela 3.1 volta a `llll` e ao estouro de 209,6pt que o autor aprovou
consertar há duas horas. O `check-largura-tabela.py` acusa: soma das colunas
livres **de 16 para 127 (+694%)**.

**Rebase resolve** — os arquivos não colidem (a branch toca `3-metodo` numa
frase do critério, o conserto toca a especificação da tabela). Não é conflito,
é só ordem.

Isso não invalida nada do conteúdo abaixo.

## Os números: conferi todos contra os artefatos, e todos batem

Tabela principal do E3′, contra `e3prime_*_s{7,42,123}_bs16.json`:

| braço | texto (acc) | medido | texto (F1) | medido |
|---|---|---|---|---|
| A | 0,711 ± 0,003 | 0,7107 ± 0,0031 | 0,310 ± 0,011 | 0,3100 ± 0,0108 |
| B | 0,775 ± 0,012 | 0,7746 ± 0,0116 | 0,291 ± 0,026 | 0,2907 ± 0,0255 |
| C | 0,781 ± 0,015 | 0,7811 ± 0,0151 | 0,235 ± 0,024 | 0,2352 ± 0,0239 |
| E | 0,814 ± 0,019 | 0,8142 ± 0,0192 | 0,332 ± 0,034 | 0,3317 ± 0,0341 |
| D | 0,883 ± 0,003 | 0,8829 ± 0,0028 | 0,451 ± 0,007 | 0,4508 ± 0,0067 |

Critérios: 0,95 × 0,883 = **0,839** ✓ · 0,95 × 0,451 = **0,428** ✓.

Varredura, incluindo as contagens de sementes — que são a minha distinção e
estão **exatas**: E20 acc 3/3 e F1 0/3 · E25 3/3 e 2/3 · E30 3/3 e 2/3 · E35
3/3 e 3/3. As sete linhas de `% pool` e `% base` conferem na casa decimal
(11.936 → 23,9% e 5,2%; 20.000 → 40% e 8,6%; 35.000 → 70% e 15,1%; 50.000 →
100% e 21,6%).

**Significância, com artefato:** `bootstrap_f1_s*_bs16.json` traz E35−D com IC
excluindo zero nas três sementes (+0,0158 [0,0125; 0,0187] · +0,0172 [0,0128;
0,0199] · +0,0065 [0,0037; 0,0103]) e `frac_replicas_delta_menor_igual_0 =
0,0`. O McNemar dá p entre 8,45e−55 e **1,98e−08**; o texto escreve
$p<10^{-7}$ — correto e conservador, colado na semente mais fraca.

## O ponto delicado está tratado melhor do que eu teria escrito

O único braço que cruza o F1 em 3/3 é o E35, com **35.000 rótulos contra o
teto de 34.724** — 276 acima. O texto declara isso de frente ("fração de
ponto acima do teto (35.000 frente a 34.724)"), reporta as duas leituras, e
acrescenta que o teto não acomodar o melhor braço **afasta a suspeita de
critério ajustado ao resultado**. É o argumento certo, e eu não o tinha visto.

Cap. 1 e Cap. 3 ficaram consistentes: os dois enunciam acurácia com 0,95× e o
teto de 34.724.

## Dois reparos pequenos

1. **A contagem de marcas provisórias está errada na mensagem, não no
   código.** A entrega diz "9 marcas `% PROVISORIO-ate-regeracao`". São
   **12**: 9 no Cap. 5 e **3 no Cap. 6**. O grep de fechamento acha as doze de
   qualquer jeito; registro para a passada final não parar em nove e deixar o
   Cap. 6 para trás.
2. **"refutad* = zero" não confere:** há 1 ocorrência, em `1-intro:121`. É
   legítima — é a definição pré-registrada do que conta como refutação, e já
   estava na main antes desta branch. Não é resíduo do regime legado. Só não
   é zero.

## O resto passa

`check-travessao-titulo` e `check-bib` em exit 0. Zero números do regime
legado nos seis arquivos (`20.092`, `8.937`, `32--40`: nenhuma ocorrência).

## Veredito

**Aprovada no conteúdo.** O único impeditivo é o rebase — e ele é obrigatório,
não opcional: sem ele o merge desfaz um gate que o autor deu hoje. Depois do
rebase eu reconfiro só a largura da tabela, que é rápido.

Lembrando o meu limite, que continua valendo: **não tenho LaTeX neste
contêiner**, então nada disto olha a página composta. Alguém com PDF precisa
ver a seção E3′ antes do gate.
