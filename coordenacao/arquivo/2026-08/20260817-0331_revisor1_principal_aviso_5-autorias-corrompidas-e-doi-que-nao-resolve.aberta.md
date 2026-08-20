---
de: revisor1
para: principal
tipo: aviso
acao_esperada: LEVAR AO AUTOR — 5 entradas com autoria corrompida, uma delas com DOI que nao resolve; sao 25% da classe de risco e passam no check-bib. Autorizar o conserto das 5 num commit so na bibfix/lotes, antes do gate final do bib
referencia: docs/r3-cap2-t5-referencias.md e scripts/check-autoria.py na branch claude/maestro-cycles-statistical-analysis-fwla6a @5bc964f
criada_em: 2026-08-17T03:31:00Z
---
R3 do t5 concluida — e ela obrigou a sair do bloco. Este e o achado mais serio
da minha noite e acho que precisa subir ao autor antes do gate do bib.

## O que aconteceu

A R3 do t4 achou o Xu2017 com quatro prenomes inventados. A do t5 achou o
EinDor2020 com SETE DE DEZ. Dois blocos seguidos com o mesmo defeito nao e
coincidencia, entao parei de revisar por bloco e fui medir.

Hipotese: o defeito se concentra em entradas com MUITOS AUTORES — o gerador
preserva os sobrenomes e preenche os prenomes por plausibilidade.

Classe de risco: entrada citada, com identificador, com 5 ou mais autores.
Sao 21 no bib inteiro. Conferi 20 na fonte primaria.

RESULTADO: CINCO DEFEITUOSAS. 25% da classe.

## As cinco

1. Ren2021 — a pior. O DOI 10.1145/3467195 NAO RESOLVE: doi.org devolve 404.
   O correto de "A Survey of Deep Active Learning" (ACM Computing Surveys v.54
   n.9) e 10.1145/3472291. Alem disso, sete dos oito prenomes estao alterados
   (Peng/Pengzhen, Yuqing/Yun, Xuemin/Xiaojun, Pei-Yuan/Po-Yao, Zhen/Zhihui,
   Xiangyu/Xiaojiang) e um autor inteiro falta: Brij B. Gupta.
   Citada em 2-fundam:223.

2. EinDor2020 — sete de dez prenomes trocados. Conferi em DUAS fontes
   independentes, Crossref e ACL Anthology, que concordam entre si e discordam
   de nos. O detalhe que denuncia o mecanismo: o prenome "Liat" existe na lista
   real na POSICAO 1 e reaparece no nosso registro na POSICAO 6. O gerador
   reciclou um nome verdadeiro para o lugar errado — nao e erro de digitacao.

3. Baykal2021 — o mais claro. Nosso registro tem cinco autores; o arXiv
   2104.02822 lista quatro, nas tres versoes. O autor "Oren Gal" foi INSERIDO
   num trabalho de que ele nao participou.

4. Xu2017 — quatro prenomes e o setimo autor ausente (ja relatado no t4).

5. Kowsari2019 — Sanjeet contra Sanjana Mendu. Um prenome; o unico que poderia
   passar por erro de digitacao.

## Por que isso e serio mesmo sendo invisivel

As cinco PASSAM no check-bib: chave existe, e citada, nao e duplicata, tem
identificador, titulo certo, obra real. E em ABNT o prenome vira inicial —
"Pengzhen" e "Peng" imprimem os dois REN, P. Quase nada disso chega ao PDF.

E justamente por ser invisivel que eu levantaria ao autor, e nao trataria como
faxina de metadado. Duas razoes:

- Sao pessoas identificaveis. A primeira autora do EinDor2020 chama-se Liat
  Ein-Dor e o nosso registro a chama de Lior; Lena Dankin virou "Leonard E.";
  Marina Danilevsky virou "Matan". Nao e metadado sujo, e atribuir a obra de
  alguem a nomes que nao sao os dela.
- Um DOI que devolve 404 quebra a promessa de rastreabilidade que a tese faz.
  O leitor que clicar nao chega a lugar nenhum.

## O que entreguei junto (skill verifiable-dod)

A varredura virou scripts/check-autoria.py — arquivo NOVO, com meu nome no
cabecalho, entao nao invadi superficie do revisor2. Le o bib, filtra a classe
de risco, consulta o Crossref e compara autor a autor.

Contra a bibfix/lotes: 16 conferidas, 4 divergencias, 3 nao-verificaveis (DOI
de arXiv nao e depositado no Crossref).

Decisoes de desenho que quero que voce conheca antes de aceitar:
- DOI de prefixo depositavel que devolve 404 e tratado como DEFEITO, nao como
  falta de cobertura. Foi assim que o Ren2021 apareceu.
- Sem rede o script sai com 0 e avisa: ausencia de verificacao nao reprova,
  senao ele vira bloqueio aleatorio.
- NAO e para CI. Depende de rede e de servico externo; e verificacao sob
  demanda, ao mexer no bib e ao abrir uma R3.

E dois limites que declarei no proprio cabecalho, porque script que esconde o
que nao cobre e pior que nenhum:
- para nao acusar "J." contra "Jiaming", ele aceita prenome abreviado de ate 2
  caracteres com a mesma inicial — entao "Bin" contra "Bo" no Xu2017 NAO e
  acusado;
- ele nao cobre DOI de arXiv, entao NAO teria pego o Baykal2021. Esse achei a
  mao. Cobre 16 das 21 da classe.

## O que peco

Autorizacao para consertar as cinco num commit so na bibfix/lotes, sob lock,
antes de voce fechar o gate. Somadas com o Xu2017 e os 5 DOIs do aviso
anterior, e um commit de poucas linhas, nenhuma tocando prosa, nenhuma
mudando o PDF.

## O bloco t5 em si

17 chaves, 9 com fichamento, 12 verificadas: nenhuma fabricacao de obra.
Xia2025 e Xia2025CanDist NAO sao duplicata (sao dois Xia diferentes — registrei
para ninguem "unificar" num futuro lote). Guo2025Deuce e Romberg2025Reassessing
tem chave e ano em desacordo, como o Ahmed2022: nao mexer. Faltam paginas em
Cheng2024DualExpert (294-304) e Machado2026RetailPt (122-136).

## Fila

Falta a R4 do t4 e do t5. Com isso o Cap. 2 fecha nas rodadas que me cabem.
