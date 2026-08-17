---
de: revisor1
para: principal
tipo: aviso
acao_esperada: afiar a frase da L813 do Cap. 2 conforme o §2 — o conserto torna a lacuna MAIS nitida; e considerar a ressalva do §4, que a tese deveria herdar
referencia: fichamentos/EinDor2020.md na branch @85ff31b · docs/r4-cap2-t5-afirmacoes.md
criada_em: 2026-08-17T05:37:00Z
---
EinDor2020 fichado. Com ele so falta o Griesshaber2020 para fechar o t5.

Nota de passagem: a 1a pagina traz os DEZ nomes corretos — Liat Ein-Dor, Alon
Halfon, Ariel Gera, Eyal Shnarch, Lena Dankin, Leshem Choshen, Marina
Danilevsky, Ranit Aharonov, Yoav Katz e Noam Slonim. Sao os mesmos que o nosso
bib trazia errados em SETE posicoes ate o conserto de hoje. Ver o PDF ao lado
do registro antigo deixa claro o tamanho do problema que o check-autoria pega.

## 1. O que a R4 mandou verificar

A L813 diz que a avaliacao rigorosa do compromisso custo-beneficio e "ainda
rara mesmo nos trabalhos que tocam o custo", citando Zhang2025 e EinDor2020.

## 2. VERIFICADO — e o achado favorece a tese MAIS do que a frase sugere

Este trabalho NAO avalia custo. Ele mede ORCAMENTO EM NUMERO DE ROTULOS: o
desenho e "orcamento inicial de 100 anotacoes", e todas as curvas sao
desempenho por iteracao, nunca por unidade monetaria. As palavras "cost" e
"expensive" aparecem em sentido qualitativo ("rotular e caro") ou referindo-se
a custo COMPUTACIONAL de treinar rede profunda — nunca como grandeza medida.

Ou seja: um dos estudos empiricos mais completos da area sobre AL com BERT — 10
conjuntos, estrategias avancadas, arcabouco publicado — opera sob restricao de
orcamento SEM JAMAIS INSTRUMENTAR CUSTO. E exatamente o vazio que a tese alega.

SUGESTAO: "trabalhos que tocam o custo" e generoso demais com eles. O mais
forte, e mais exato, e dizer que esses trabalhos tratam orcamento como CONTAGEM
DE ROTULOS e nao como custo — e que e essa a diferenca que o FALCO instrumenta.
A frase fica mais precisa E a lacuna fica mais nitida. Prosa e sua; so proponho.

## 3. Um numero para o Cap. 5

No cenario desbalanceado-pratico, as estrategias superam a aleatoria por 4 a 8
pontos de F1 em media. E a referencia externa mais proxima do que o FALCO mede.
Ressalva obrigatoria ao usar: la sao 2 classes, aqui sao 621.

## 4. UMA RESSALVA QUE A TESE DEVERIA HERDAR

Os autores registram, na secao 3.5, que sob orcamento limitado um conjunto de
validacao pode simplesmente NAO EXISTIR na pratica — e verificam que ignora-lo
da resultado qualitativamente igual, porem mais ruidoso.

O criterio de parada do FALCO se apoia em estagnacao de desempenho em conjunto
de validacao. Herdamos a fragilidade. Nao e defeito — e ressalva honesta que
vale uma linha no Cap. 6, e citar o EinDor2020 nela e melhor do que descobri-la
na arguicao.

## 5. Quinto ponto da serie

  Rouzegar2024    2 a 4 classes     selecao ganha
  Deng2023fedal   3 classes         ganha, por 2,36 pontos de Macro F1
  Yuan2020        2 a 5 classes     ganha
  EinDor2020      2 classes         ganha, por 4 a 8 pontos de F1
  Wertz2022       100 a 739         NAO ganha de forma consistente

Cinco trabalhos independentes. A fronteira continua exatamente onde estava.

## 6. Estado

KG em 597 nos e 1251 arestas; check-bib exit 0. Falta o Griesshaber2020 — e
nele esta a 6a autoria corrompida (Julia -> Johannes Maucher), ainda sem
autorizacao para corrigir.
