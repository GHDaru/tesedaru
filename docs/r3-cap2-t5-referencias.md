# R3 do tema t5 do Capítulo 2 — e uma varredura de autoria em todo o `.bib`

**Escopo declarado**: `2-fundam/texto.tex`, linhas 722-848 (seção 2.5, "Estado
da arte e lacuna").
**Escopo real**: o bloco t5 mais uma varredura que ele obrigou — ver §2.
**Rodada**: R3 (princípio II, referência validada contra fichamento) com a lente
de fonte primária.
**Executado por**: revisor1 · **Data**: 2026-08-17
**Base**: o `.bib` da branch `bibfix/lotes`, **não** o da `main`.

## 1. O bloco t5

17 chaves distintas. Nove têm fichamento; oito não. Verifiquei **doze** na fonte
primária — proporção alta porque este é o bloco mais recente da tese: sete
entradas são de 2024 a 2026, exatamente a faixa em que as fabricações
apareceram antes.

**Verificadas e corretas** (título, autoria, veículo, volume e páginas batendo
com Crossref ou arXiv): `Cheng2024DualExpert`, `Guo2025Deuce`,
`Machado2026RetailPt`, `Romberg2025Reassessing`, `Yuan2020`, `Griesshaber2020`,
`Xia2025`, `Xia2025CanDist`, `Kholodna2024`, `Zhang2025`, `Qi2026MixtureLLMs`,
`Daru2022`.

Três observações menores, nenhuma delas erro:

- **`Xia2025` e `Xia2025CanDist` não são duplicata.** São dois Xia diferentes —
  Yu Xia (survey de AL com LLM, ACL 2025 p. 14552-14569) e Mingxuan Xia
  (framework professor-aluno, ACL 2025 p. 2750-2770). Registro para ninguém
  "unificar" as duas num futuro lote.
- **`Xia2025` usa `and others`**, que é o `et al.` do BibTeX. Os três autores
  nomeados conferem; a lista completa tem oito. Não é erro, é truncamento
  deliberado.
- **Chave e ano em desacordo** em `Guo2025Deuce` (chave 2025, `year` 2024, TACL
  v. 12) e `Romberg2025Reassessing` (chave 2025, `year` 2026, EACL 2026). Nos
  dois casos o `year` está certo e a chave é só rótulo interno. Mesmo caso do
  `Ahmed2022` do t4: **não mexer**.

**Faltam páginas** em duas entradas verificadas: `Cheng2024DualExpert`
(p. 294-304) e `Machado2026RetailPt` (p. 122-136). Campos ausentes, não errados.

**`Bayer2024`** aparece citada aqui na `main`; é chave morta, já repontada na
`bibfix/lotes`. Confirmação, não achado.

**`Kitchenham2004`** não tem identificador — é relatório técnico de 2004 e
nunca teve DOI. Correto como está.

---

## 2. O que o bloco obrigou: a falha não era do bloco

A R3 do t4 encontrou o `Xu2017` com quatro prenomes inventados. Este bloco
trouxe o `EinDor2020` com **sete de dez**. Dois blocos seguidos com o mesmo
defeito deixaram de ser coincidência, então parei a revisão por bloco e fui
medir a extensão.

**Hipótese**: o defeito se concentra em entradas com muitos autores — o
gerador preserva os sobrenomes e preenche os prenomes por plausibilidade.

**Classe de risco definida**: entrada citada, com identificador, e **cinco ou
mais autores**. São **21 entradas** no `.bib` inteiro.

**Resultado da varredura**: **cinco defeituosas em vinte conferidas — 25%.**

### 2.1 `Ren2021` — o pior caso: o DOI não existe

Citada em `2-fundam:223` para sustentar que o aprendizado ativo "ganhou novas
camadas com o aprendizado profundo".

- **`doi.org/10.1145/3467195` devolve 404.** O identificador não resolve para
  nada. O DOI correto de *A Survey of Deep Active Learning* (ACM Computing
  Surveys, v. 54, n. 9) é **`10.1145/3472291`**.
- Contra o registro real, sete dos oito prenomes estão alterados e **um autor
  inteiro falta**:

| # | Nosso `.bib` | Fonte primária |
|---|---|---|
| 1 | **Peng** Ren | **Pengzhen** Ren |
| 2 | **Yuqing** Xiao | **Yun** Xiao |
| 3 | **Xuemin** Chang | **Xiaojun** Chang |
| 4 | **Pei-Yuan** Huang | **Po-Yao** Huang |
| 5 | **Zhen** Li | **Zhihui** Li |
| 6 | *(ausente)* | **Brij B. Gupta** |
| 7 | **Xiangyu** Chen | **Xiaojiang** Chen |
| 8 | Xin Wang | Xin Wang |

### 2.2 `EinDor2020` — sete de dez prenomes trocados

Conferido em **duas** fontes independentes, Crossref e ACL Anthology, que
concordam entre si e discordam de nós:

| # | Nosso `.bib` | Fonte primária |
|---|---|---|
| 1 | **Lior** Ein-Dor | **Liat** Ein-Dor |
| 3 | **Avi** Gera | **Ariel** Gera |
| 4 | **Ehud** Shnarch | **Eyal** Shnarch |
| 5 | **Leonard E.** Dankin | **Lena** Dankin |
| 6 | **Liat** Choshen | **Leshem** Choshen |
| 7 | **Matan** Danilevsky | **Marina** Danilevsky |
| 10 | **Nadav** Slonim | **Noam** Slonim |

Repare no detalhe que denuncia o mecanismo: **"Liat" existe na lista real — na
posição 1 — e no nosso registro reapareceu na posição 6.** O gerador reciclou
um nome verdadeiro para o lugar errado. Não é erro de digitação.

Vale dizer o que isso significa fora do arquivo: são pessoas identificáveis. A
primeira autora chama-se Liat Ein-Dor, e o nosso registro a chama de "Lior";
Lena Dankin virou "Leonard E."; Marina Danilevsky virou "Matan". Não é só
metadado sujo — é atribuir a obra de alguém a nomes que não são os dela.

### 2.3 `Baykal2021` — um autor que não existe no artigo

Nosso registro traz cinco autores: Baykal, Liebenwein, **Gal, Oren**, Feldman,
Rus. O arXiv 2104.02822 lista **quatro**: Cenk Baykal, Lucas Liebenwein, Dan
Feldman, Daniela Rus. Conferi a v1 e a versão corrente — as três versões têm os
mesmos quatro nomes.

**"Oren Gal" é um autor inserido.** É o caso mais claro da varredura: não é
prenome alterado, é uma pessoa acrescentada a um trabalho de que não participou.

### 2.4 `Xu2017` — já relatado na R3 do t4

Quatro prenomes trocados e o sétimo autor ausente. Detalhe em
`docs/r3-cap2-t4-referencias.md`.

### 2.5 `Kowsari2019` — um prenome

`Sanjeet Mendu` contra `Sanjana Mendu`. Isolado, e o único da varredura que
poderia passar por erro de digitação.

### 2.6 As que passaram

`Aliero2023`, `Cheng2024DualExpert`, `Diao2023`, `Goudjil2018`, `Kholodna2024`,
`Li2020`, `Peters2018`, `Qi2026MixtureLLMs`, `Reusens2024`,
`Romberg2025Reassessing`, `Song2014`, `Song2023NoisyLabels`, `Tian2023`,
`Xia2025CanDist`, `Zhang2023LLMaAA`.

`Peters2018` apareceu como suspeita e **não é**: nosso "Matthew E. Peters"
contra "Matthew Peters" do Crossref é só a inicial do nome do meio, que o
Crossref não registra. O nosso está mais completo.

---

## 3. Por que o `check-bib` não pega nada disso

Todas as cinco entradas **passam** no `check-bib` atual: a chave existe, é
citada, não é duplicata, tem identificador, o título está certo e a obra é real.
O que está errado só aparece comparando com a fonte.

E em ABNT quase nada disso chega ao PDF, porque os prenomes viram iniciais.
`Pengzhen` e `Peng` imprimem os dois "REN, P.". É precisamente por ser
invisível que precisa de checagem mecânica: o que está corrompido é o
**registro**, que é o que a tese promete ser auditável (princípios II e IX).

## 4. A checagem virou script — `scripts/check-autoria.py`

Seguindo a skill `verifiable-dod` (critério vira checagem executável, não
juízo), a varredura desta rodada está encapsulada em `scripts/check-autoria.py`.
Ele lê o `.bib`, pega as entradas citadas com identificador e cinco ou mais
autores, consulta o Crossref e compara autor a autor.

```
python3 scripts/check-autoria.py --bib <caminho>   # classe de risco
python3 scripts/check-autoria.py --todas           # tudo o que tem DOI
python3 scripts/check-autoria.py --chave Ren2021   # uma entrada
```

Saída atual contra a `bibfix/lotes`: **16 entradas conferidas, 4 divergências**
(`EinDor2020`, `Kowsari2019`, `Ren2021`, `Xu2017`), 3 não-verificáveis por
terem DOI de arXiv.

Três decisões de desenho que valem registro:

- **DOI de prefixo depositável que devolve 404 é DEFEITO, não falta de
  cobertura.** Foi assim que o `Ren2021` apareceu. DOI de arXiv (`10.48550/*`)
  não é depositado no Crossref e sai como não-verificável, sem acusar.
- **Sem rede, o script sai com 0 e avisa.** Ausência de verificação não é
  reprovação; do contrário ele viraria um bloqueio aleatório.
- **Não é para CI**, porque depende de rede e de um serviço externo. É
  verificação sob demanda: ao mexer no `.bib` e ao abrir uma R3.

**Limite conhecido, declarado no cabeçalho do script**: para não acusar "J."
contra "Jiaming", o comparador aceita prenome abreviado de até dois caracteres
com a mesma inicial. Isso deixa passar prenomes curtos e reais trocados por
outros de mesma inicial — o "Bin" contra "Bo" do `Xu2017` **não** é acusado. O
script reduz o trabalho manual; não o substitui.

E ele **não** teria pegado o `Baykal2021`, cujo DOI é de arXiv. Esse achei à
mão. Fica como limite honesto da cobertura: a classe de risco tem 21 entradas,
o script cobre 16.

---

## Resumo executável

| # | Entrada | Defeito | Gravidade |
|---|---|---|---|
| 1 | `Ren2021` | DOI não resolve + 1 autor ausente + 7 de 8 prenomes | **alta** |
| 2 | `EinDor2020` | 7 de 10 prenomes trocados | **alta** |
| 3 | `Baykal2021` | autor inserido que não consta do artigo | **alta** |
| 4 | `Xu2017` | 4 prenomes + 1 autor ausente (relatado no t4) | média |
| 5 | `Kowsari2019` | 1 prenome | baixa |
| 6 | `Cheng2024DualExpert`, `Machado2026RetailPt` | falta `pages` | baixa |
| 7 | `Guo2025Deuce`, `Romberg2025Reassessing` | chave × ano | não mexer |

Nenhuma fabricação de OBRA no t5 — as 17 obras existem e são as citadas. O que
há é corrupção de AUTORIA, e ela não respeita fronteira de bloco: está
espalhada pela classe "muitos autores", em 25% dela.

**Nenhuma entrada foi editada.** Correção de `referencias.bib` depende de
autorização, e as cinco somadas são um único commit de poucas linhas.
