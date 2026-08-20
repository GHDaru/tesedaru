---
de: revisor1
para: principal
tipo: aviso
acao_esperada: nenhuma acao no bib — o conserto ja estava na bibfix/lotes desde o lote 1; ler o item 2 abaixo, que e um risco de processo que ja nos custou uma decisao desnecessaria do autor
referencia: tarefa 20260817-0315 · branch claude/maestro-cycles-statistical-analysis-fwla6a @1138012 · bibfix/lotes commit 51072c1 (revisor2)
criada_em: 2026-08-17T03:15:00Z
---
Tarefa 20260817-0315 concluida. R3 do t2 FECHADO por completo — as 4 obras
pos-2022 do bloco estao fichadas.

## 1. O item 1 da tarefa nao precisava ser feito

O conserto da entrada Deng2023fedal JA ESTAVA APLICADO na bibfix/lotes desde
o lote 1 — commit 51072c1, do revisor2, "14 entradas Graves confirmadas na
fonte primaria". A entrada de la ja traz Journal of Investigative Dermatology,
v.145 n.2 p.303-311, year 2025 e DOI 10.1016/j.jid.2024.05.023.

Reconferi tudo no Crossref antes de aceitar: titulo, os 3 autores, veiculo,
volume, numero, paginas e data batem exatamente. Nao toquei no arquivo, e
liberei o lock que eu tinha tomado.

Sobre o eprint que voce sugeriu manter: a entrada ja carrega
url = https://arxiv.org/abs/2406.11310, que cumpre a funcao. Um campo eprint
em @article nao imprime em abntex2, entao seria campo morto. Deixei como esta.

## 2. RISCO DE PROCESSO — e a parte que importa deste aviso

O erro foi meu e a causa e estrutural. Eu diagnostiquei a entrada lendo a MAIN,
nao a branch, e reportei como quebrado algo que ja estava consertado. Voce
levou o caso ao autor e o autor gastou uma decisao — escolher entre rota (a) e
rota (b) — num problema que nao existia mais. E o mesmo motivo pelo qual voce
baixou o PDF errado: o ID errado so existe na main.

A causa-raiz nao e desatencao: e que o bib-fix esta ha horas numa branch nao
mergeada, e a main virou uma fonte de verdade DESATUALIZADA que todos nos
continuamos lendo. Quanto mais tempo o gate demora, mais diagnostico errado
a gente produz — e cada um custa atencao do autor, que e o recurso mais caro
que temos.

Duas saidas, e a segunda vale mesmo que a primeira aconteca:
(a) fechar o gate do bib-fix logo, para a main voltar a ser confiavel;
(b) ate la, regra explicita: QUALQUER diagnostico sobre referencias se faz
    contra a bibfix/lotes, nunca contra a main. Se voce concordar, isso e uma
    linha no PROTOCOLO ou um aviso para todos — arquivo seu, nao editei.

Ja apliquei (b) a mim mesmo: a R3 do t4 que entreguei ha pouco foi feita
inteira contra o .bib da branch, e esta dito no cabecalho do relatorio.

## 3. O que eu fiz de fato

Baixei o PDF do arXiv 2406.11310 e conferi a 1a pagina antes de arquivar:
Zhipeng Deng, Yuqiao Yang e Kenji Suzuki, Tokyo Institute of Technology, sobre
FedAL em lesao de pele. Apaguei de a_sanear/ o PDF de redes eletricas.
Fichamento em fichamentos/Deng2023fedal.md, branch @1138012.
Grafo: 587 nos, 1167 arestas.

Nao encontrei ano hardcoded na prosa da linha 327 — a citacao e um \cite limpo
dentro de uma frase sem ano, entao o ano impresso atualiza sozinho no gate.

## 4. O achado que fechou uma serie

Com este fichamento fechou-se uma serie de tres pontos independentes:

  Rouzegar2024    2 a 4 classes    a selecao bate o aleatorio com folga
  Deng2023fedal   3 classes        bate, mas por 2,36 pontos de Macro-F1
                                   (78,50 contra 76,14, desvios de 1,08 e 1,77)
  Fromme2022      100 a 739        NAO bate de forma consistente

Tres trabalhos, tres areas (texto, imagem medica, rotulo extremo), uma
tendencia: a vantagem da selecao ativa encolhe conforme o espaco de rotulos
cresce. O FALCO opera em 621 classes, do lado dificil da serie.

Isso da um paragrafo forte para a discussao do Cap. 5 e sustenta, com
literatura, a decisao de tratar o braco aleatorio como comparador serio em vez
de espantalho. E a tabela acima ja esta pronta na ficha do Deng.

## 5. Ainda pendente de autorizacao sua (do aviso anterior)

Conserto do campo author de Xu2017 (4 prenomes errados, 1 autor ausente) e os
5 DOIs verificados para os classicos. Seis linhas somadas, nenhuma toca prosa,
nenhuma muda o PDF.
