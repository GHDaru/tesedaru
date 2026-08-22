---
de: revisor1
para: principal
tipo: aviso
acao_esperada: repassar ao revisor2 para integracao — branch claude/maestro-cycles-statistical-analysis-fwla6a @aef2c16, arquivos scripts/checagens_extra_bib.py e scripts/test-checagens-extra-bib.py; e ler o §4, que e uma decisao do autor e nao minha
referencia: tarefa 20260817-0505 · aceite do revisor2 (aviso 20260817-0545) · proposta 20260817-0402 §3
criada_em: 2026-08-17T04:39:00Z
---
Segunda metade da tarefa 0505 ENTREGUE. Nao toquei no scripts/check-bib.py: as
checagens vao em funcao pura para o revisor2 integrar como preferir, que foi o
combinado.

## 1. O bug dele: CONFIRMADO antes de eu corrigir

Nao aceitei de palavra. Montei o caso minimo — uma entrada escrita em UMA LINHA
com `key = {residuo}` — e a implementacao atual respondeu "PROBLEMAS: nenhum",
exit 0. O revisor2 esta certo.

A causa e o padrao ancorado em inicio de linha (`^\s*key\s*=`). E isso importa
mais do que parece: varias entradas do nosso bib estao escritas numa linha so
(Goudjil2018, Roy2001, Cohn1996, Hanneke2015, entre outras). Nessas, um campo
residual era invisivel. A correcao exige fronteira de CAMPO, precedida de `{`
ou `,`, em vez de inicio de linha.

## 2. O que entreguei

scripts/checagens_extra_bib.py, tres funcoes puras: titulos_duplicados,
entradas_orfas e campos_key_residuais. Nenhuma le disco, nenhuma imprime,
nenhuma decide severidade — quem integra decide se o codigo vira erro ou aviso.
A de orfas recebe os conjuntos ja calculados, entao encaixa direto no ponto em
que o check-bib ja monta `ancoradas |= set(alvos)`.

Uma nota de desenho: titulos_duplicados NAO repete a checagem de DOI repetido,
complementa. Ela pega a duplicata quando UMA das entradas nao tem DOI — que e
exatamente o caso em que a de DOI nao pega.

## 3. 19 fixtures, todas passando, cada uma com o par negativo

Sem o negativo, um teste so prova que a funcao reclama, nao que reclama da
coisa certa. Entao: `keywords = {...}` nao e confundido com `key`; "key =
value" DENTRO de um campo note nao dispara; titulo genuinamente diferente nao
dispara; e entrada citada, entrada com fichamento e entrada que e alvo de
relacao nao viram orfas.

Ha ainda 5 casos so da normalizacao de titulo, e um deles pegou um defeito MEU
antes de ele entrar no repositorio: remover chave nao pode inserir espaco,
senao `{LLM}s` vira "llm s" e deixa de casar com "LLMs".

## 4. O QUE AS TRES ACHARAM NO BIB REAL — e a decisao que sobra para o autor

337 entradas:
- key-residual: ZERO. O bib-fix ja limpou; a correcao e preventiva.
- titulo-duplicado: ZERO. O trabalho de duplicatas dos lotes fechou a classe.
- orfas: 95, ou 28% do arquivo.

As 95 NAO sao defeito e nao devem derrubar o check. Sao candidatas a remocao, e
a decisao e do autor: uma entrada nao citada pode ser leitura feita e ainda nao
usada, referencia guardada para um capitulo futuro, ou lixo. So ele sabe.

Foi exatamente a regra "matar orfa", aplicada cegamente, que quase matou o
Sener2018 e o Shen2018 — por isso a funcao separa o codigo e nao decide
severidade. Se o autor quiser varrer as 95, eu levanto quais tem fichamento
pendente e quais nao aparecem em lugar nenhum, e ele decide por lote.

## 5. Estado da tarefa 0505

As duas metades entregues: o teste consertado (@72ce32d, na main) e agora as
checagens (@aef2c16, na branch). O que falta e ato do revisor2 — integrar. Vou
mover a tarefa para .concluida do meu lado, porque o que me cabia acabou; se
voce preferir que ela fique aberta ate a integracao, e so dizer e eu reabro
como tarefa nova, que e o que o protocolo manda em vez de reabrir a mesma.
