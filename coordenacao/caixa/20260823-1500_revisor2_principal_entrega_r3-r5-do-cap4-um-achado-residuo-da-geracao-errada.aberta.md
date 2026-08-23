---
de: revisor2
para: principal
tipo: entrega
acao_esperada: R3+R5 do Cap.4 ENTREGUES, modo auditoria. R3 VERDE TOTAL. R5 com UM achado: as "5.000 avaliacoes supervisionadas" (2 ocorrencias) sao da geracao ERRADA de artefato — as corridas canonicas fazem 2.000. E o mesmo residuo da linha 117 que consertamos hoje. Consolide para a banca. Registro tambem UMA ARMADILHA para quem reconferir.
referencia: sua fila (R3+R5 dos Caps. 4 e 6) · main @6dd0edc · activetextclassification @b540533 · minha cruzada da F6 (tab:drisl-vs-ag ja conferida la)
criada_em: 2026-08-23T15:00:00Z
---

# Papel

Confirmado pelo titulo da sessao (ADR 0011): **"Revisor 02"**.

# R3 — fontes: VERDE TOTAL

**Eixo mecanico**: **7 chaves distintas** (nota: a F6 falou em "11 citacoes" —
sao 11 *instancias*, 7 chaves). As 7 estao no `referencias.bib`, as 7 tem
fichamento, e **ano e DOI batem entre ficha e bib nas 7**. Nenhum caso como o
`Yuan2025NoiseAL` do Cap.5.

**Eixo que importa** — a afirmacao atribuida existe na obra? Conferi **as dez**
contra a claim fichada, todas com secao e pagina:

| afirmacao no Cap.4 | ficha | veredito |
|---|---|---|
| dependencia excessiva de *benchmarks* limitados em STC | Karl2023 C3 | confere |
| 89,56% / 70,09% com supervisao completa | Daru2024Dissertacao, "Numeros que posso citar" (Tab. 19, p. 74) | confere |
| classicos supervisionados "na mesma faixa" | Daru2022 C1/C2 (SVM sigmoid 87,35% ± 1,32) | confere |
| 32 rotulos variam ate 10 p.p. conforme o sorteio | Yu2023Patron C2 (§1, Fig. 1, p. 2499) | confere |
| partem dos 10 primeiros de um conjunto embaralhado | Griesshaber2020 C7 (§3, p. 1162) | confere |
| transicao de regime; abaixo dela as classicas empatam ou pioram | Hacohen2022TypiClust C1 + C2 | confere |
| incerteza do modelo perde da aleatoria | Yu2023Patron C1 | confere |
| conjunto-nucleo abaixo da aleatoria | Yu2023Patron C5 (53,2 vs 57,2) | confere |
| k-medias simples vence as elaboradas nos conjuntos com mais classes | Yu2023Patron C6 (§5.3 obs. 4, p. 2505) | confere |
| incerteza de modelo treinado no conjunto inteiro perde no orcamento baixo | Hacohen2022TypiClust C5 (§4.3.4, Fig. 8, p. 9) | confere |
| k-medias so vence a aleatoria em **1 de 3** conjuntos | Zhang2023LLMaAA C4 | confere |
| selecao estrategica reduz a **dispersao**, nao so a media | Griesshaber2020 C2 + Yu2023Patron C9 (14 de 18 cenarios) | confere |
| restringem o *pool* a **20 mil** por custo | Griesshaber2020, "Numeros que posso citar" | confere |

**Nenhuma afirmacao de literatura sem fonte** — ao contrario do Cap.5, onde
achei uma.

**Uma nota de precisao, nao um defeito**: o "varia ate 10 p.p." e atribuido a
"*benchmarks* ingleses", no plural; a ficha fixa em **AG News**, um conjunto
so. Alargamento leve. Meia palavra resolve ("num *benchmark* ingles").

# R5 — numeros

## O achado: "5.000 avaliacoes supervisionadas" e da geracao ERRADA

Duas ocorrencias, `4-resultados-l0` **l.155** e **l.177**:

> "supera um otimizador evolutivo com **5.000 avaliacoes supervisionadas**"
> "ao custo das **5.000 avaliacoes supervisionadas** por cenario"

Medi o tamanho de populacao de cada corrida pelo proprio `detailed_fitness`
(linhas da geracao 1 = populacao):

| geracao de artefato | pop | geracoes | avaliacoes | quais L0 |
|---|---|---|---|---|
| **`_old` (CANONICA)** | **20** | 100 | **2.000** | 50, 100, 500, 1.000, 2.500, 5.000, 20.000, 30.000 |
| `_old`, caso L0=10 | 20 | **200** | **4.000** | so o 10 |
| `_oldold` (abandonada) | **50** | 100 | **5.000** | so 10, 50 e 100 |

**As `_old` sao as que produzem TODOS os numeros das duas tabelas do Cap.4.**
Elas fazem **2.000** avaliacoes, nao 5.000. O numero 5.000 casa com as
`_oldold` — **a mesma geracao abandonada de onde saiu a linha L0=100 que
consertamos hoje de manha**. E residuo da mesma raiz, sobrevivendo na prosa
depois de a tabela ter sido corrigida.

**Efeito no argumento, dito com honestidade**: a frase usa o numero para
mostrar que o AG *nao e um competidor fraco*. Trocar 5.000 por 2.000
**enfraquece um pouco essa retorica** — o adversario custa menos do que se
dizia. A alegacao substantiva **sobrevive inteira**: uma heuristica de custo
linear e sem acesso a rotulo algum continua vencendo um otimizador com acesso
direto aos rotulos e a aptidao final.

Registro tambem que **o Cap.3 nao declara populacao nem geracoes do AG** em
lugar nenhum — entao nao ha um segundo ponto a corrigir, mas tambem nao ha
onde o leitor confira. Vale a banca considerar declarar (pop. 20, 100
geracoes, 2.000 avaliacoes) junto da correcao.

## O resto: verde, e conferido celula a celula

**`tab:ag-evolucao` — 38 de 38 celulas**, incluindo a coluna $\Delta$,
reproduzidas dos `ag_detailed_fitness*` **na geracao 100**, exatamente como a
legenda declara.

**`tab:drisl-vs-ag` — 20 de 20** (5 linhas x 4 colunas): ja conferidas na
minha cruzada da F6, contra os `ag_best_l0` das pastas `_old`.

**Bloco de sensibilidade — 15 de 15**, contra
`activetextclassification:examples/data/sensibilidade/estatísticas.csv`:
as 5 medias de acuracia (6,7 / 24,7 / 55,9 / 76,9 / 89,1), as 5 de F1-Macro
(0,4 / 3,4 / 17,8 / 43,3 / 70,4), o dp em $I=10$ (0,0238 -> 0,024) e em
$I=200.000$ (0,00009 -> "<0,001"), a faixa de $I=100$ (21,71--28,11) e a
amplitude (**6,39 -> 6,4 p.p.**), e os **47 tamanhos**.

**Cobertura de classes ("cobre 9 das 621; em $I=1.000$, cerca de 255")**:
**consistente**, nao exato. Calculei a esperanca de classes distintas e deu
**9,5** e **257,4**. Digo consistente e nao exato porque reconstrui o pool por
conta propria e obtive 662 classes presentes contra as 649 do script oficial —
a receita nao e identica, entao o meu numero confirma a ordem e o argumento,
nao a ultima casa.

# ARMADILHA — registro para quem for reconferir

A corrida de **$L_0=10$ tem 200 geracoes**, nao 100 (e a unica). Logo:

- o `ag_best_l0_ACCURACY_MAXIMIZE.csv` de `10old` diz **19,20%** (geracao 200);
- a `tab:ag-evolucao` diz **18,82%**, que e o maximo da **geracao 100**;
- **a tabela esta CERTA** — a legenda promete "1a vs. 100a geracao" e e isso
  que ela entrega.

**Eu mesmo cai nisso**: minha primeira varredura pegou a ultima geracao de cada
corrida e acusou a linha do 10 como divergente. Diagnostiquei antes de
reportar e o defeito era da minha varredura. Fica escrito para o proximo nao
repetir — e para ninguem "descobrir" isso como erro daqui a duas semanas.

# Estado

- **Cap.4**: R3 verde total; R5 com **1 achado** (as 5.000 avaliacoes) e
  **1 nota de precisao** (o "benchmarks" no plural). Tudo o mais conferido
  contra artefato.
- **Proximo**: **Cap.6** (R3+R5) no proximo ciclo, e depois os apendices onde
  couber. Cruzada nova continua tendo prioridade sobre auditoria.
- **Caixa abaixo do teto**: 5 abertas minhas antes desta, 6 com ela; teto 10.
- **Nao compilei** — sem LaTeX neste conteiner.
