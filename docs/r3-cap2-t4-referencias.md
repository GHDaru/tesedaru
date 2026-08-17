# R3 do tema t4 do Capítulo 2 — referências × fichamento × fonte primária

**Escopo**: `2-fundam/texto.tex`, linhas 627-721 (seção 2.4, "Classificação de
texto curto").
**Rodada**: R3 — princípio II da constituição da tese ("referência validada
contra fichamento"), estendido pela lente adotada nesta madrugada: **validar
também contra a FONTE PRIMÁRIA** (DOI, veículo, autoria), que foi o que expôs
as seis fabricações de metadados do Capítulo 1 e do t2.
**Executado por**: revisor1 · **Data**: 2026-08-17
**Base**: o `.bib` da branch `bibfix/lotes @162c12b` (estado pós-correções), não
o da `main`, porque é ele que vai ao gate.

## Números do bloco

| Medida | Valor |
|---|---|
| Chaves distintas citadas em 627-721 | **28** |
| Com fichamento | 10 |
| **Sem fichamento** (pendência do princípio II) | **18** |
| Verificadas na fonte primária nesta rodada | 10 |
| **Divergências encontradas** | **1 grave, 1 cosmética** |
| Fabricações de obra | **0** |

O bloco é o mais limpo revisado até agora. Escolhi as 10 a verificar pela regra
de risco que a rodada anterior estabeleceu — obra pouco conhecida, veículo de
baixa circulação, ou entrada sem identificador — e deixei de fora os clássicos
de identidade inequívoca cuja checagem eu faria só para confirmar o óbvio.

---

## 1. Divergência grave: `Xu2017` tem a lista de autores corrompida

**Obra**: "Self-Taught Convolutional Neural Networks for Short Text
Clustering", *Neural Networks*, v. 88, p. 22-31, 2017.
**DOI declarado**: `10.1016/j.neunet.2016.12.008` — **resolve para a obra
certa**. Não é sequestro de identificador.

O problema é a autoria. Comparação com o registro do Crossref:

| # | Nosso `.bib` | Fonte primária |
|---|---|---|
| 1 | Xu, **Jun** | Xu, **Jiaming** |
| 2 | Xu, **Bin** | Xu, **Bo** |
| 3 | Wang, Peng | Wang, Peng |
| 4 | Zheng, **Shuang** | Zheng, **Suncong** |
| 5 | Tian, **Guang** | Tian, **Guanhua** |
| 6 | Zhao, Jun | Zhao, Jun |
| 7 | *(ausente)* | **Xu, Bo** (segundo homônimo) |

**Quatro prenomes trocados por formas plausíveis mas erradas, e um autor a
menos.** O padrão é o mesmo das fabricações já encontradas: sobrenomes
preservados, prenomes preenchidos por plausibilidade. A diferença é que aqui a
obra é real e o identificador está certo — o dano é ao registro, não à
verificabilidade.

**Efeito na saída impressa: nenhum.** Em ABNT os prenomes viram iniciais, e
`Jiaming → J.`, `Bo → B.`, `Suncong → S.`, `Guanhua → G.` coincidem com
`Jun → J.`, `Bin → B.`, `Shuang → S.`, `Guang → G.`. Com mais de três autores
imprime-se "et al." de todo modo. **A correção é invisível ao leitor** — e é
por isso mesmo que ela não pode ser adiada por "não muda nada": muda o
registro, que é o que a tese promete ser auditável.

**Conserto** (uma linha, sem efeito no PDF):
```bibtex
author = {Xu, Jiaming and Xu, Bo and Wang, Peng and Zheng, Suncong and
          Tian, Guanhua and Zhao, Jun and Xu, Bo},
```

## 2. Divergência cosmética: `Ahmed2022` com chave e ano em desacordo

A entrada corrigida pelo bib-fix está certa quanto à obra — "Short Text
Clustering Algorithms, Application and Challenges: A Survey", *Applied
Sciences*, v. 13, n. 1, art. 342, DOI `10.3390/app13010342`, quatro autores
conferidos. Mas a **chave diz `Ahmed2022` e o campo `year` diz `2023`**.

Não é erro: o Crossref registra `issued` em **2022-12-27** e o fascículo é o
de **janeiro de 2023**. As duas datas são defensáveis, e `year = {2023}` é a
escolha certa para ABNT (segue o fascículo). O que incomoda é a chave sugerir
outra coisa: a citação imprime "(AHMED et al., 2023)" enquanto o identificador
interno diz 2022.

**Conserto**: renomear para `Ahmed2023` — mas isso colide com a chave que
acabamos de remover por fabricação (a antiga `Ahmed2023`, cujo título e veículo
eram inventados). Renomear agora reintroduziria um nome com histórico sujo.
**Recomendo deixar como está** e registrar aqui o porquê, para ninguém
"consertar" no futuro sem saber. É decisão de nomenclatura, não de conteúdo.

## 3. Verificadas e corretas na fonte primária

| Chave | Fonte primária conferida | Veredito |
|---|---|---|
| `Aliero2023` | *Int. J. of Computer Applications*, v. 185, n. 33, p. 44-55, 2023; 6 autores; DOI `10.5120/ijca2023923106` | confere |
| `Alsmadi2019` | *Int. J. of Web Information Systems*, v. 15, n. 2, p. 155-182, 2019; Alsmadi e Gan; DOI `10.1108/IJWIS-12-2017-0083` | confere |
| `Song2014` | *Journal of Multimedia*, v. 9, n. 5, 2014; 5 autores; DOI `10.4304/jmm.9.5.635-643` | confere |
| `Li2020` | arXiv:2008.00364, 8 autores, título exato | confere |
| `Ahmed2022` | *Applied Sciences* 13(1):342; 4 autores | confere (ver §2) |
| `Bojanowski2017` | *TACL*, v. 5, p. 135-146; 4 autores | confere |
| `Pennington2014` | EMNLP 2014, p. 1532-1543; 3 autores | confere |
| `Cortes1995` | *Machine Learning*, v. 20, n. 3, p. 273-297 | confere |
| `Cover1967` | *IEEE Trans. Information Theory*, v. 13, n. 1, p. 21-27 | confere |
| `Salton1988` | *Information Processing & Management*, v. 24, n. 5, p. 513-523 | confere |

A duplicata `Alsmadi2019` / `alsmadi2019shorttext`, que o `check-bib` acusava
na `main` por DOI repetido, **já está resolvida** na `bibfix/lotes`.

## 4. Nove chaves citadas sem identificador — e cinco DOIs prontos

O `check-bib` só cobra `doi` ou `url` de entradas citadas com `year >= 2020`,
por decisão do parecer. Nove chaves deste bloco ficam abaixo desse corte e
seguem sem identificador:

`Baeza2013`, `Bojanowski2017`, `Cortes1995`, `Cover1967`, `Goldberg2017`,
`Pennington2014`, `Radford2018`, `Radford2019`, `Salton1988`.

São todas obras clássicas de identidade inequívoca — **não há suspeita**. Mas
sem identificador o leitor não tem caminho de um clique, e a tese perde
rastreabilidade barata.

**Cinco delas eu já verifiquei no Crossref**, com título, autoria e veículo
batendo exatamente com a nossa entrada. Ficam prontos para aplicar, se
autorizado:

```bibtex
Bojanowski2017  doi = {10.1162/tacl_a_00051}
Pennington2014  doi = {10.3115/v1/D14-1162}
Cortes1995      doi = {10.1007/BF00994018}
Cover1967       doi = {10.1109/TIT.1967.1053964}
Salton1988      doi = {10.1016/0306-4573(88)90021-0}
```

As quatro restantes não têm DOI a acrescentar: `Goldberg2017` e `Goodfellow2016`
são livros (cabe `isbn`), e `Radford2018` e `Radford2019` são relatórios
técnicos da OpenAI que nunca receberam DOI — nesses dois o correto é `url` para
a página oficial.

## 5. Duas chaves mortas ainda citadas na `main` — confirmação, não achado

As linhas 657 e 683 deste bloco citam `Naseem2021` e `Selva2021`, que o bib-fix
removeu (em favor de `Naseem2021HateSpeech` e `Birunda2021`, as entradas
ancoradas em fichamento). Na `main` as citações antigas continuam; na
`bibfix/lotes` já foram repontadas por mim nas rodadas anteriores.

Registro aqui só para deixar explícito: **quem ler a `main` isolada vê duas
citações que o gate resolve.** Não é pendência nova.

## 6. Pendência do princípio II: 18 das 28 sem fichamento

| Sem fichamento (18) |
|---|
| `Aggarwal2012`, `Ahmed2022`, `Aliero2023`, `Alsmadi2019`, `Baeza2013`, `Bojanowski2017`, `Cortes1995`, `Cover1967`, `Devlin2019`, `Goldberg2017`, `Goodfellow2016`, `Murphy2012`, `Naseem2021`†, `Peters2018`, `Radford2018`, `Radford2019`, `Selva2021`†, `Xu2017` |

† chaves mortas, resolvidas pelo gate do bib-fix.

Descontando as duas mortas, **16 chaves vivas sem fichamento**. Como no t2, a
maioria é clássico anterior a 2015 (Cover 1967, Salton 1988, Cortes 1995) ou
livro-texto (Goodfellow, Goldberg, Murphy, Aggarwal, Baeza-Yates), e cai na
mesma decisão de princípio que o principal já subiu ao autor: emenda que
dispense fichamento para clássicos e livros de referência, ou fichamento em
massa.

As que **não** caem nessa categoria e mereceriam ficha própria, por serem
método diretamente empregado ou survey do assunto central do capítulo:
`Xu2017`, `Ahmed2022`, `Aliero2023`, `Alsmadi2019`, `Devlin2019`, `Peters2018`.

---

## Resumo executável

| # | Item | Ação | Custo |
|---|------|------|-------|
| 1 | `Xu2017` com 4 prenomes errados e 1 autor ausente | substituir o campo `author` (sem efeito no PDF) | **mínimo** |
| 2 | `Ahmed2022` com chave e ano em desacordo | **não mexer**; motivo registrado aqui | zero |
| 3 | 5 DOIs verificados prontos para clássicos | aplicar sob lock, se autorizado | baixo |
| 4 | `Radford2018`/`Radford2019` sem DOI | acrescentar `url` oficial | baixo |
| 5 | `Goldberg2017`/`Goodfellow2016` sem identificador | acrescentar `isbn` | baixo |
| 6 | 16 chaves vivas sem fichamento | depende da decisão de princípio pendente com o autor | — |

Nenhuma fabricação de obra neste bloco. Depois de seis fabricações confirmadas
nos blocos anteriores, um bloco limpo é informação: sugere que o problema se
concentrou nas seções escritas com apoio de geração automática de referências,
e não no capítulo inteiro.
