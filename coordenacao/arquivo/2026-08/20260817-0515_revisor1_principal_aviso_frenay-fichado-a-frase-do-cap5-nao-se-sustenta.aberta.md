---
de: revisor1
para: principal
tipo: aviso
acao_esperada: LEVAR AO AUTOR — a frase de 5-resultados-falco:143 esta verificada contra as DUAS fontes que ela cita, e nenhuma a sustenta; o conserto e uma reformulacao que FORTALECE a tese, descrita no §3
referencia: fichamentos/Frenay2014.md e fichamentos/Song2023NoisyLabels.md · branch @1a00d6d
criada_em: 2026-08-17T05:15:00Z
---
O autor subiu o PDF do Frenay2014 em a_sanear/ — copia do repositorio
institucional da Universite de Namur. Conferido e arquivado. Com ele fecha a
verificacao que eu abri as 02:56.

## 1. VEREDITO: as duas fontes lidas, nenhuma sustenta a frase

5-resultados-falco/texto.tex:143 afirma que o ruido estruturado, concentrado em
pares vizinhos, e "cenario menos danoso ao classificador treinado que ruido
uniforme", citando Frenay2014 e Song2023NoisyLabels.

Song2023NoisyLabels (fichado as 03:00): na dimensao que mede — detectabilidade
— diz o CONTRARIO, e as Figuras 5 e 7 fazem a comparacao na mesma taxa.

Frenay2014 (fichado agora), secao II-B-2: "In the case of NAR label noise, it
is no longer trivial to decide whether the labels are helpful or not". Sob
ruido dependente de classe o problema fica MAIS dificil de analisar, nao menos
danoso.

Busquei o contrario antes de concluir, nos dois. A unica ocorrencia de "less
harmful" no Frenay compara ruido de ATRIBUTO com ruido de ROTULO — comparacao
diferente — e na mesma secao ele registra que o de rotulo e potencialmente MAIS
danoso.

## 2. O AGRAVANTE, e ele e especifico das nossas 621 classes

Mesmo paragrafo do Frenay: a condicao de erro esperado menor que 1/2 "does not
prevent the occurrence of very small correct labelling probabilities for some
class y, in particular if the prior probability of this class is small".

Traduzindo para o nosso caso: a taxa de erro GLOBAL do oraculo pode parecer
aceitavel e, ao mesmo tempo, uma classe rara ter probabilidade de rotulagem
correta quase nula. Com 621 classes e cauda longa, e exatamente a nossa
situacao — e e a situacao que o Macro F1 penaliza com forca.

O survey nao diz que o ruido estruturado e mais brando. Diz que ele pode
ESCONDER dano concentrado nas classes raras.

## 3. O CONSERTO FORTALECE A TESE — e e por isso que eu levaria ao autor

Nao e so tirar uma citacao que nao serve. As duas fontes passam a sustentar
coisas melhores:

(a) TERMO TECNICO NO LUGAR DA PARAFRASE. O Frenay da nome formal ao que a tese
    descreve: "pairwise label noise" — duas classes escolhidas, cada instancia
    de uma com probabilidade de virar a outra, so duas entradas nao nulas fora
    da diagonal da matriz de rotulagem. Caso particular do NAR. Trocar "ruido
    estruturado, concentrado em pares vizinhos" por "ruido de par" ancora a
    frase numa fonte que sustenta exatamente o que esta sendo dito.

(b) O AGRAVANTE VIRA ARGUMENTO A FAVOR. Uma hipotese que a literatura declara
    NAO TRIVIAL de decidir e, por definicao, hipotese que merece experimento.
    O E4 e esse experimento. A tese deixa de herdar uma conclusao da literatura
    e passa a responder uma pergunta que a literatura deixou em aberto — o que
    e posicao mais forte, nao mais fraca.

(c) O PAR FICA COERENTE. O Frenay da a algebra (matriz de rotulagem, tres
    regimes NCAR/NAR/NNAR); o Song2023 da a evidencia empirica moderna
    (sobreposicao das distribuicoes de perda, dificuldade de deteccao). Citados
    juntos cobrem formalizacao e pratica sem que nenhum precise sustentar o que
    nao diz.

A reformulacao e a mesma que o Cap. 2 ja usa corretamente nas linhas 585-590:
o dano do nosso caso "nao se deduz da regra geral — e examinado empiricamente
nesta tese".

## 4. Estado

Branch @1a00d6d. KG em 594 nos e 1215 arestas; check-bib exit 0.
Pendencia do Frenay2014 fechada — era a ultima da R4 do t5 que dependia de PDF
externo. Restam os tres classicos (Yuan2020, EinDor2020, Griesshaber2020), cujos
PDFs eu re-baixo no proximo ciclo.
