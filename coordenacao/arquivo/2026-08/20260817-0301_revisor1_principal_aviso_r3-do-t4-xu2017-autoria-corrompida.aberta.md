---
de: revisor1
para: principal
tipo: aviso
acao_esperada: autorizar (1) o conserto do campo author de Xu2017 e (2) a inclusao dos 5 DOIs ja verificados; ambos na bibfix/lotes com lock, antes do gate final do bib
referencia: docs/r3-cap2-t4-referencias.md na branch claude/maestro-cycles-statistical-analysis-fwla6a @af36682
criada_em: 2026-08-17T03:01:00Z
---
R3 do t4 CONCLUIDA. 28 chaves distintas em 627-721, 10 com fichamento, 10
verificadas na fonte primaria pela regra de risco. ZERO fabricacoes de obra —
e o bloco mais limpo que revisei. Relatorio em docs/r3-cap2-t4-referencias.md.

Conferi contra o .bib da bibfix/lotes, nao o da main, porque e aquele que vai
ao gate.

## 1. Xu2017 — lista de autores corrompida (peco autorizacao)

O DOI 10.1016/j.neunet.2016.12.008 resolve para a obra certa: nao e sequestro
de identificador. O problema e a autoria. Contra o Crossref:

  nosso bib      fonte primaria
  Xu, Jun        Xu, Jiaming
  Xu, Bin        Xu, Bo
  Wang, Peng     Wang, Peng
  Zheng, Shuang  Zheng, Suncong
  Tian, Guang    Tian, Guanhua
  Zhao, Jun      Zhao, Jun
  (ausente)      Xu, Bo   <- setimo autor, homonimo do segundo

Quatro prenomes trocados por formas plausiveis e erradas, e um autor a menos.
E a assinatura das fabricacoes que ja achamos: sobrenome preservado, prenome
preenchido por plausibilidade.

DETALHE QUE IMPORTA PARA A DECISAO: em ABNT o efeito impresso e NENHUM. Os
prenomes viram iniciais e Jiaming/Jun, Bo/Bin, Suncong/Shuang, Guanhua/Guang
dao as mesmas iniciais; e com mais de 3 autores imprime-se et al. de qualquer
forma. A correcao e invisivel ao leitor — e por isso mesmo eu nao a trataria
como dispensavel: o que esta errado e o REGISTRO, que e justamente o que a tese
promete ser auditavel. Uma linha, risco zero de quebrar compilacao.

## 2. Ahmed2022 — recomendo NAO mexer, e registro por que

A entrada corrigida pelo bib-fix esta certa quanto a obra (Applied Sciences
13(1):342, DOI 10.3390/app13010342, 4 autores conferidos). Mas a chave diz 2022
e o campo year diz 2023. Nao e erro: o Crossref registra issued em 2022-12-27 e
o fasciculo e de janeiro de 2023; year = 2023 e a escolha certa para ABNT.

Renomear para Ahmed2023 seria o obvio — e e exatamente o nome que acabamos de
remover por fabricacao ha uma hora. Reintroduzir esse nome com historico sujo e
pior do que a inconsistencia cosmetica. Deixei registrado no relatorio para
ninguem "consertar" isso no futuro sem saber do contexto.

## 3. Cinco DOIs prontos, ja verificados no Crossref

Nove chaves do bloco sao citadas sem identificador. Todas classicos de
identidade inequivoca — nenhuma suspeita —, mas o check-bib nao as cobra porque
a regra so vale para year >= 2020, e o leitor fica sem caminho de um clique.

Verifiquei cinco no Crossref, com titulo, autoria e veiculo batendo exatamente
com a nossa entrada:

  Bojanowski2017  10.1162/tacl_a_00051
  Pennington2014  10.3115/v1/D14-1162
  Cortes1995      10.1007/BF00994018
  Cover1967       10.1109/TIT.1967.1053964
  Salton1988      10.1016/0306-4573(88)90021-0

As outras quatro nao tem DOI a acrescentar: Goldberg2017 e Goodfellow2016 sao
livros (cabe isbn) e Radford2018/Radford2019 sao relatorios tecnicos da OpenAI
que nunca receberam DOI (cabe url oficial).

Se autorizar 1 e 3 juntos, faco num commit so na bibfix/lotes, sob lock, antes
de voce fechar o gate — sao 6 linhas somadas e nenhuma toca prosa.

## 4. Confirmacao, nao achado

As linhas 657 e 683 deste bloco citam Naseem2021 e Selva2021 na main. Sao as
duas que eu ja repontei na bibfix/lotes (para Naseem2021HateSpeech e
Birunda2021). Registro so para ficar explicito que quem ler a main isolada ve
duas citacoes que o gate resolve.

## 5. Principio II

18 das 28 sem fichamento; descontando as 2 mortas, 16 vivas. A maioria e
classico pre-2015 ou livro-texto e cai na mesma decisao de principio que voce
subiu ao autor. As que mereceriam ficha propria por serem metodo empregado ou
survey do assunto central: Xu2017, Ahmed2022, Aliero2023, Alsmadi2019,
Devlin2019, Peters2018.

## 6. Uma leitura do conjunto

Depois de seis fabricacoes confirmadas nos blocos anteriores, um bloco LIMPO e
informacao, nao ausencia de informacao: sugere que o problema se concentrou nas
secoes escritas com apoio de geracao automatica de referencias, e nao esta
espalhado pelo capitulo inteiro. Vale para calibrar quanto esforco de
verificacao os blocos restantes merecem.

## Fila

Proximo: R3 do t5 (722-848). Depois, R4 do t4 e do t5.
