# R4 do tema t5 do Capítulo 2 — a seção que sustenta a lacuna

**Escopo**: `2-fundam/texto.tex`, linhas 722-848 (seção 2.5, "Estado da arte na
interseção e lacuna de pesquisa").
**Rodada**: R4 — princípio III (afirmação fundamentada) e princípio V (nenhum
número sem artefato rastreável).
**Executado por**: revisor1 · **Data**: 2026-08-17
**Natureza**: levantamento. Nenhuma frase reescrita.

Esta é a seção mais consequente do capítulo: é dela que sai a **lacuna** que
justifica a tese inteira. Uma afirmação frouxa aqui custa mais caro na banca do
que dez afirmações frouxas numa revisão de conceitos. Revisei com esse peso.

---

## Primeiro, o que está exemplar

A subseção 2.5.1 **declara o próprio estatuto metodológico**: diz, com todas as
letras, que é *"uma revisão narrativa focada na interseção das frentes, e não
de uma revisão sistemática completa com protocolo registrado e fluxo de seleção
documentado"*, cita `Kitchenham2004` para marcar o contraste, justifica a
escolha pelo papel do capítulo e declara a contrapartida.

Isso é o oposto do que se costuma ver, que é passar uma revisão narrativa por
sistemática sem dizer. Quem lê sabe exatamente o que está recebendo. **Não
mexer.**

Falta-lhe **uma linha**: a **data da última busca**. Numa tese que cobre "até o
primeiro semestre de 2026", o leitor de 2027 precisa saber a partir de quando o
silêncio da revisão deixa de ser evidência. É a informação mais barata de
acrescentar e a que mais protege a alegação de lacuna.

---

## 1. `Machado2026RetailPt` — quatro números, dois verificados, zero fichamento

O trecho (L793-800) usa quatro números para sustentar uma escolha de projeto da
tese (BERTimbau como classificador forte):

| Número no texto | Verificação na fonte |
|---|---|
| "$\approx 100$ mil títulos" | **confere** — o resumo diz "100,000 product titles" |
| "94,0\% de Macro F1 após ajuste" | **confere** — "the transformer attains 94.00%" |
| "97,0\% de acurácia" | **não verificado** — o resumo não reporta acurácia, só macro-F1 |
| "12 mil rótulos manuais" | **não verificado** — o resumo não traz esse número |

E a obra **não tem fichamento**. Ou seja: pelo princípio II a referência não
está validada, e pelo princípio V nenhum dos quatro números resolve para
artefato do repositório — os dois que eu confirmei, confirmei agora, contra o
resumo no Crossref, e essa verificação não fica registrada em lugar nenhum
enquanto não houver ficha.

**Imprecisão de escopo, no mesmo trecho**: o texto descreve o estudo como
classificação de "títulos de supermercados portugueses nas categorias ECOICOP".
O resumo restringe: *"Portuguese **food and beverage** items"*, de seis redes.
Não é a categoria toda do supermercado — é o recorte de alimentos e bebidas.

Isso importa para a comparação, e a favor da tese: o FALCO opera sobre **621
classes de catálogo inteiro**, e o trabalho comparado resolve um recorte mais
estreito. Dizer o recorte torna o contraste mais forte, não mais fraco.

**Conserto**: fichar a obra (fica na minha fila), e enquanto isso ou localizar
os dois números não verificados no corpo do artigo, ou removê-los. O par
100 mil / 94,0% já sustenta o argumento sozinho.

## 2. A alegação de lacuna não está delimitada pela busca (L845-847)

> "A ausência combinada — partida a frio informada + oráculo LLM progressivo +
> texto curto em português + custo instrumentado — é a lacuna que o
> Capítulo~\ref{ch:metodo} ataca."

É a afirmação mais importante da tese, e é uma **afirmação de ausência**. Como
está escrita, ela diz que a combinação não existe. O que a revisão pode
sustentar é que ela **não foi encontrada na busca descrita na 2.5.1**.

A diferença não é retórica. Uma alegação de ausência sem delimitação é
refutável por **um único contraexemplo** que um membro da banca conheça — e
cai inteira. Delimitada pela busca, ela continua verdadeira mesmo que apareça o
contraexemplo, porque passa a ser afirmação sobre o que a revisão cobriu, que é
exatamente o que a subseção 2.5.1 já teve o cuidado de declarar.

**Custa uma oração subordinada.** A 2.5.1 já fez o trabalho difícil de declarar
o estatuto; a 2.5.3 não colhe o benefício.

O mesmo vale, em menor escala, para a L812: *"com avaliação rigorosa desse
trade-off, **ainda rara** mesmo nos trabalhos que tocam o custo
`\cite{Zhang2025, EinDor2020}`"*. "Rara" é afirmação sobre a distribuição de um
campo; duas citações mostram dois casos, não uma frequência.

## 3. A tabela de lacunas são 45 afirmações, e nem todas têm lastro

A Tabela~\ref{tab:lacunas} cruza **9 trabalhos × 5 dimensões**. Cada célula é
uma afirmação sobre o trabalho de outra pessoa — que ela **trata**, **não
trata** ou trata **parcialmente** de uma dimensão. São 45 afirmações, e as de
ausência (`\xmark`) são as mais arriscadas: dizer que um trabalho *não* faz
algo exige ter lido o suficiente para saber.

Cobertura de fichamento das 9 obras da tabela: **8 têm, 1 não**
(`Machado2026RetailPt`, item 1). Base boa.

Mas ter fichamento não é o mesmo que a célula estar lastreada. **Proposta de
critério executável** (skill `verifiable-dod`): cada `\xmark` e cada `$\sim$` da
tabela deve poder ser apontado para um claim do fichamento da obra, com
evidência localizável. Onde não houver, ou se completa a ficha, ou a célula
vira `$\sim$`, ou some.

Não é trabalho grande — são 8 fichas que já existem — e transforma a tabela de
juízo em registro. É a peça da tese que uma banca mais provavelmente vai atacar
célula a célula.

## 4. Claims que carregam peso e não têm ficha por trás

Cinco obras citadas nesta seção não têm fichamento: `Machado2026RetailPt`,
`Romberg2025Reassessing`, `Yuan2020`, `EinDor2020` e `Griesshaber2020`.

Três delas sustentam claims específicos, não decorativos:

- **`Romberg2025Reassessing`** (L785-789) sustenta a afirmação mais forte da
  subseção sobre o estado prático do campo: *"a viabilidade operacional, não a
  acurácia, é o obstáculo apontado"*. É a leitura de uma pesquisa de comunidade,
  e é conclusão interpretativa — precisa de evidência localizável (qual
  pergunta, qual proporção de respondentes) para não ser paráfrase otimista.
- **`Yuan2020`** (L768) sustenta a descrição mecânica do ALPS ("explora a
  'surpresa' do modelo de linguagem").
- **`EinDor2020`** aparece duas vezes, inclusive na L813 sustentando que a
  avaliação rigorosa de custo é rara.

Os dois últimos são obras clássicas da área e o risco é baixo. O
`Romberg2025Reassessing` é o que eu ficharia primeiro.

## 5. Claims negativos sobre trabalhos alheios

Dois, ambos load-bearing:

- L773-775: *"O DEUCE converge conceitualmente com a Fase 1 do FALCO, mas **não
  incorpora oráculo LLM nem é avaliado em português ou texto de e-commerce**."*
  `Guo2025Deuce` tem fichamento, então a checagem é barata: confirmar que a
  ficha registra as duas ausências com evidência.
- L798-800: *"depende de um fluxo de rotulagem humano ad-hoc […] **sem
  estratégia formal de aprendizado ativo nem oráculo automatizado**"*. O resumo
  do artigo confirma "human-in-the-loop workflow", o que sustenta a primeira
  metade. A segunda metade — ausência de estratégia formal — é o tipo de
  ausência que só a leitura do corpo sustenta, e a obra não tem ficha.

Nenhum dos dois é implausível. Os dois são exatamente o tipo de frase que uma
banca pede para justificar.

## 6. Uma órfã pequena

L725-728: *"a partida a frio é mais severa: com pouca informação por instância,
o modelo inicial precisa de mais exemplos para sustentar seleções informadas"*.
Sem fonte, sem dado. É argumento plausível e a tese tem o experimento
(Capítulo~\ref{ch:resultados-l0}) que poderia sustentá-lo — basta remeter.

---

## Resumo executável

| # | Linha | Item | Ação | Custo |
|---|---|---|---|---|
| 1 | 796-798 | 2 dos 4 números do Machado não verificados, obra sem ficha | fichar; localizar ou remover os dois | médio |
| 2 | 794-795 | escopo do Machado é alimentos e bebidas, não o catálogo | dizer o recorte — **fortalece** o contraste | **mínimo** |
| 3 | 845-847 | alegação de lacuna sem delimitação de busca | delimitar pela busca da 2.5.1 | **mínimo** |
| 4 | 812 | "ainda rara" como afirmação de frequência | abrandar ou delimitar | mínimo |
| 5 | 817-840 | 45 células, cada uma uma afirmação | critério: toda `\xmark` aponta para claim de ficha | médio |
| 6 | 785-789 | claim forte do Romberg sem ficha | fichar | médio |
| 7 | 746-762 | falta a data da última busca | uma linha | **mínimo** |
| 8 | 725-728 | órfã sobre partida a frio | remeter ao Cap. 4 | mínimo |

Quatro dos oito custam uma oração cada — e três deles (2, 3, 7) **fortalecem** a
posição da tese em vez de enfraquecê-la: dizer o recorte do trabalho comparado,
delimitar a alegação de ausência e datar a busca são movimentos que tiram do
examinador as três perguntas mais fáceis de fazer.

## Encerramento do Capítulo 2 nas rodadas que me cabem

Com esta, fecham-se: R3 e R4 do t2, R3 e R4 do t4, R3 e R4 do t5. Os temas t1 e
t3 são do revisor2. A retrospectiva do capítulo, com a skill `anti-patterns`,
vem em documento separado.
