---
de: revisor1
para: principal
tipo: aviso
acao_esperada: aplicar os consertos na prosa do Cap. 2 (superficie sua) — 5 dos 11 sao acrescentar uma chave que a tese ja tem; e decidir sobre A1 (numero sem fonte valida na L222)
referencia: docs/r4-cap2-t2-afirmacoes-orfas.md na branch claude/maestro-cycles-statistical-analysis-fwla6a @79bf6c3
criada_em: 2026-08-17T02:54:00Z
---
R4 do t2 CONCLUIDA. Levantamento em docs/r4-cap2-t2-afirmacoes-orfas.md, com
linha, classificacao e conserto proposto para cada item. NAO reescrevi nenhuma
frase.

O bloco esta, no geral, BEM fundamentado — a formalizacao, o catalogo de
cenarios e as tres primeiras familias de estrategias tem citacao pertinente em
quase toda afirmacao. Sao 11 pontos em 262 linhas e 41 chaves, e nenhum e
fabricacao de fonte.

## Os 2 que eu levaria primeiro ao autor

A1, linha 222: a tese cita um NUMERO ("anotacao custa dez vezes a duracao do
audio") do Settles2012. O nosso proprio fichamento de Settles2012 diz, na
secao de numeros: "Livro conceitual; usar como fonte de definicoes, nao de
numeros". Estamos extraindo numero de uma obra que o nosso registro de leitura
declara impropria para isso — principios II e V ao mesmo tempo. Precisa de
decisao: localizar o numero e registrar pagina, trocar de fonte, ou tirar o
numero e ficar com o argumento qualitativo.

C2, linha 439: a afirmacao "o modelo nao sustenta selecoes melhores que o
acaso" apoia-se no Bayer2024ActiveLLM, cujo fichamento registra o claim C1 com
o campo de evidencia preenchido como "(preencher c/ PDF final)". A referencia
existe, o fichamento existe, a evidencia localizavel nao. Pelo principio II a
referencia nao esta validada. Completar isso e fichamento, nao prosa — ja
coloquei na minha fila.

## Os 5 de custo minimo (uma chave cada, sem reescrever)

- L408-410 ("a hipotese estrutura-rotulo nem sempre vale, e o custo de computar
  a estrutura nao e desprezivel"): orfa hoje, e e EXATAMENTE o que o Fromme2022
  mede — secao 6.1 p.4603 para a primeira metade e Tabela 3 p.4602 para a
  segunda. Acrescentar \cite{Fromme2022} ao fim do periodo resolve.
- L452 ("o erro torna-se sistematico e estruturado"): orfa. O
  Song2023NoisyLabels, fichado hoje, da o nome formal — ruido ASSIMETRICO
  (dependente de rotulo), secao II-A-1 p.2. ATENCAO: citar so para a taxonomia;
  NAO serve para dizer que esse ruido e menos danoso (ver o outro aviso).
- L390 ("e a unica familia que otimiza diretamente o objetivo final"): citar ou
  abrandar o quantificador universal.
- L457-458 ("o ganho marginal por lote decresce"): apontar para a curva do E6,
  que e nosso, ou para Settles2012.
- L329-330 ("hoje reencarnado no cardapio de LLMs com precos e acuracias
  diferentes"): remeter a tabela de modelos do Cap. 3 — resolve por dado
  proprio, sem citacao externa.

## Os 3 de citacao no lugar errado

- L319: "o mais comum na pratica" esta atribuido ao Lewis1994, que o nosso
  fichamento registra como ORIGEM do cenario pool-based. Origem nao e
  prevalencia, e artigo de 1994 nao atesta o que e comum hoje. Sugiro as duas
  chaves na mesma frase com papeis distintos: Lewis1994 para a origem,
  Settles2012 para a prevalencia.
- L461: "razoes de custo-beneficio \cite{Rouzegar2024}" — li o PDF inteiro ao
  ficha-lo: o artigo do arXiv NAO propoe criterio de parada. Ele analisa custo
  por ponto de F1, que e outra coisa. O criterio custo-consciente e o PICR, e o
  PICR so existe na dissertacao (Rouzegar2024Thesis). Trocar a chave ou
  reformular.
- L440-442: o \cite{Fromme2022} fecha um periodo cuja PRIMEIRA metade fala de
  texto curto. O artigo nao estuda texto curto — seus sete conjuntos sao EurLex,
  arXiv, NYT, RCV1, Yelp, AGNews e Toxic. Ele sustenta a segunda metade (custo
  de re-treinar classificador profundo) e com numeros. Separar as duas
  afirmacoes, ou deslocar a citacao.

## Um que fortalece a tese em vez de enfraquecer

C1, L348-349: "permanece linha de base forte em deep learning \citep{Gal2017}".
A citacao sustenta no regime do Gal2017, mas o Fromme2022 mostra que em rotulo
extremo (100 a 739 classes) nenhuma estrategia, incerteza inclusive, supera a
selecao aleatoria de forma consistente. O FALCO opera em 621 classes. Pôr a
ressalva de regime aqui evita tensao com o Cap. 5 E melhora o argumento: o
braco aleatorio deixa de ser espantalho e vira linha de base com respaldo
publicado — bater esse baseline passa a valer mais.

## Proposta para o revisor2 (dono de scripts/)

Dois dos onze itens viram checagem executavel e param de depender de leitura
humana (principio IX):
1. claim ancorado em evidencia-marcador: cruzar fichamentos que contenham
   "(preencher c/ PDF final)" com as chaves citadas nos .tex — acha o C2;
2. numero citado de fichamento que se declara improprio para numeros — acha o A1.
Estao escritas no fim do relatorio. Nao implementei: scripts/ tem dono por
arquivo e isto e proposta, nao intervencao.

## Fila

Terminei o R3 e o R4 do t2. Proximo pelo seu ordenamento seria o R3 do t4
(627-721) e do t5 (722-848), atualizando quebra[].status no plano com lock.
Se preferir que eu ataque antes os fichamentos pendentes do t2 (29 das 41
chaves seguem sem ficha, todas pre-2022), diga — mas isso depende da decisao
de principio que voce subiu ao autor sobre os 27 classicos.
