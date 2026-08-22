---
de: banca
para: principal
tipo: entrega
acao_esperada: pedir a cruzada do revisor2 sobre `banca/f6-cap4-literatura` @aacdbbf (checar que todo cite novo existe e e fichado, ADR 0012) e, aprovada, levar ao gate do autor. Ordem de merge: `banca/cap4-linha117` primeiro (cruzada ja aprovada as 2300) ou direto a F6, que a contem como base.
referencia: tarefa 20260822-1200 (F6) · dec-reforco-cap4-aprovado · branch banca/f6-cap4-literatura @aacdbbf · 4-resultados-l0/texto.tex
criada_em: 2026-08-22T23:45:00Z
---

# F6 entregue: o Cap. 4 deixou de discutir contra o nada

**O que mudou** (1 arquivo, +71/-3 linhas, so `4-resultados-l0/texto.tex`):
o capitulo sai de **0 para 11 citacoes**. Quatro insercoes de escrita nova,
nenhum numero da tese alterado, nenhuma realocacao:

1. **Abertura**: a base real de varejo como resposta a dependencia de
   benchmarks limitados (Karl2023, C3 da ficha).
2. **§4.1 (sensibilidade)**: paragrafo que ancora a saturacao no teto
   supervisionado conhecido da mesma base (Daru2024Dissertacao C1: 89,56% /
   70,09%; Daru2022), poe a amplitude de 6,4 p.p. ao lado do analogo publicado
   (Yu2023Patron C2: ate 10 p.p. com 32 rotulos) e mostra que a pratica
   corrente sorteia o L0 como detalhe (Griesshaber2020 C7).
3. **§4.3 (DRI-SL vs AG)** — a discussao nova pedida: (a) confirmacao — em
   orcamento baixo representatividade vence (Hacohen2022TypiClust C1/C2;
   Yu2023Patron C1/C5/C6: incerteza perde da aleatoria, conjunto-nucleo abaixo
   da aleatoria, k-medias vence nos conjuntos com mais classes); (b) surpresa
   delimitada — o superado e um otimizador COM acesso a rotulos, e o paralelo
   de Hacohen (C5: ate incerteza de modelo treinado no conjunto inteiro perde)
   sugere que o gargalo da partida a frio nao e falta de supervisao, e sim
   cobertura da estrutura do espaco; (c) contraste — Zhang2023LLMaAA C4
   (diversidade pura falha em extracao com poucos tipos) delimita o regime;
   (d) variancia — selecao estrategica reduz dispersao (Griesshaber2020 C2,
   Yu2023Patron C9) e o DRI-SL, deterministico, zera a do sorteio.
4. **§4.4 (replay)**: precedente publicado para reduzir malha por custo
   declarando o risco (Griesshaber2020 C8, pool de 20 mil).

**As 6 fichas que prometiam o Cap. 4 foram honradas**: Daru2022,
Daru2024Dissertacao, Griesshaber2020, Karl2023, Yu2023Patron (era ORFA — e a
primeira citacao dela na tese), Zhang2023LLMaAA. Somei Hacohen2022TypiClust,
ja interlocutora do Cap. 2, porque a transicao de regime e o eixo da discussao.

**Evidencia executavel**: `check-uso-declarado.py` nao lista mais nenhuma
promessa pendente ao Cap. 4 (eram 6); `check-bib.py`: PROBLEMAS nenhum;
`check-travessao-titulo.py`: nenhum; todas as 7 chaves conferidas no
`referencias.bib` (Yu2023Patron l.3147). Terminologia em camadas conferida:
"transicao de regime" (grafia do Cap. 2 l.463), "conjunto-nucleo" (Cap. 2
l.458), "$k$-medias" (Cap. 3 l.418).

**Riscos**: (i) sem LaTeX neste conteiner — as insercoes usam so
\citep/\citet/\textit e math ja presente, mas a compilacao precisa ser
conferida onde houver TeX; (ii) e conteudo interpretativo novo em capitulo de
resultados — exatamente o caso de gate do autor; (iii) a branch tem por base
`banca/cap4-linha117` @460a7d1: mergear a F6 traz a linha 117 junto (mesmo
commit), sem conflito em nenhuma ordem.

Sigo agora para o lote 2100 (correcoes pontuais do revisor2), ja em-andamento.
