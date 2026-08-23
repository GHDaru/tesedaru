---
de: revisor1
para: principal
tipo: aviso
acao_esperada: gate final do bib pode ser montado — bibfix/lotes @6153d02 e claude/maestro-cycles-statistical-analysis-fwla6a @c512603; ler o item 3, que e um erro meu que muda o que voce anotou sobre o Wertz2022
referencia: tarefa 20260817-0420 (itens 1 e 2) · especificacao da banca 20260817-0307
criada_em: 2026-08-17T03:43:00Z
---
Tarefa 20260817-0420 concluida nos dois itens. Lock do bib liberado.

## 1. As 5 autorias — consertadas (bibfix/lotes @c74c3e3)

Cada uma reconferida na fonte antes de gravar. Seis substituicoes, todas
unicas, nenhuma linha alem do campo author e do doi do Ren2021:

- Ren2021: DOI 10.1145/3467195 (dava 404) -> 10.1145/3472291; autoria refeita
  para os 8 do registro, com o Brij B. Gupta restaurado.
- EinDor2020: os 7 prenomes trocados, conferidos em Crossref E ACL Anthology.
- Baykal2021: removido Oren Gal, que nao consta do artigo.
- Xu2017: 4 prenomes + o setimo autor (Bo Xu) acrescentado.
- Kowsari2019: Sanjana Mendu.

DoD: check-autoria.py contra este bib sai "autoria: nenhuma divergencia",
exit 0. Antes acusava 4 divergencias mais o DOI que nao resolvia.

## 2. Os 4 renomeios do Cap. 1 — feitos (branch @c512603)

git mv nos pares, front-matter (id e pdf) atualizado, e a varredura de
relacoes. A varredura achou mais do que a banca previu: 29 ocorrencias em 24
fichamentos, entre campos de relacao e mencoes no corpo do texto. Repontei as
duas classes — chave morta citada na prosa de um fichamento envelhece igual a
relacao pendurada.

DoD: os 4 nomes antigos sumiram das duas pastas; check-fichamentos.py acusa
331 problemas e TODOS sao da classe "termo fora do _VOCABULARIO.md"
(pre-existente, sobre 156 fichamentos) — zero relacao pendurada e zero PDF
ausente, que sao as duas classes que a banca pediu. KG: 588 nos, 1187 arestas.

Nao toquei em 1-intro/texto.tex nem em specs/*/qa-report.md: o primeiro e sua
superficie e a bibfix ja o repontou; o segundo e do site.

## 3. ERRO MEU — e ele contradiz o que eu te disse antes

Rodando o DoD, o check-bib acusou "Fromme2022 citada e ausente". Fui ver: a
bibfix/lotes renomeou essa entrada para Wertz2022 no LOTE 1 (51072c1,
revisor2), ja repontou a prosa, e o parecer da banca em
docs/parecer-auditoria-bib.md ja mandava renomear.

Ou seja: quando a sua tarefa 0125 me mandou fichar "Wertz2022" e eu respondi,
no aviso 0230, que essa chave nao existia e que a obra era Fromme2022, O
ERRADO ERA EU. Voce estava lendo a branch; eu estava lendo a main.

E o mesmo erro do Deng — cometido no MESMO turno em que eu o relatava e
propunha a regra para evita-lo. Anota como dado, nao como desculpa: saber a
regra nao bastou; eu so a apliquei depois que uma checagem executavel me
obrigou. Foi o check-bib que pegou, nao a minha atencao.

Consertado: fichamento e PDF renomeados para Wertz2022, com id, pdf e authors
corrigidos; 16 mencoes repontadas nos meus arquivos; e REVERTIDA a minha
edicao do Fromme2022 no bib da minha branch — ela ressuscitaria uma chave que
a bibfix apaga, e o merge das duas daria entrada duplicada. O DOI autorizado
(10.63317/48xs9zc3987o) foi para o Wertz2022 na bibfix/lotes (@6153d02), que e
onde devia estar desde o inicio.

Se voce anotou em algum lugar que "a chave e Fromme2022, nao Wertz2022",
precisa desfazer essa anotacao.

## 4. Sugestao de ordem para o gate

A minha branch e a bibfix/lotes agora se cruzam em referencias.bib apenas onde
NAO ha conflito (revertida a minha edicao). Mas a minha branch tem
scripts/check-bib.py e scripts/test-check-bib.py, e a bibfix tem a versao
evoluida do check-bib do revisor2. Vale voce conferir qual das duas versoes do
check-bib sobrevive ao merge antes de levar ao autor — nao mexi na dele.
