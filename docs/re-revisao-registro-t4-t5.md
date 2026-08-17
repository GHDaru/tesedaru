# Re-revisão de registro — t4 e t5 do Capítulo 2

**Ordem**: do autor, transmitida pela banca (checklist de 9 itens) e despachada
na tarefa `20260817-1420`.
**Lente**: registro de escrita — **não** é R1 (travessões) nem R4 (afirmação
fundamentada). É o que a leitura do autor pegou em t1/t2 e nós não pegávamos.
**Executado por**: revisor1 · **Data**: 2026-08-17
**Natureza**: levantamento. **Nenhuma linha de prosa foi editada.**

Faixas medidas na `main` de 2026-08-17T15:30Z: **t4 = linhas 715-810**,
**t5 = linhas 811-938**. Cada item traz o trecho citado, porque a faixa desliza.

---

## Antes da lista: um item (c) que é meu, e está fora de t4/t5

> **FECHADO em 2026-08-17T16:01Z — não precisa de ação.** Verifiquei na `main`
> depois do gate do t2 (`00baaed`, as 14 edições da leitura do autor): o autor
> **já resolveu**, e pela segunda alternativa sugerida abaixo. A evocação saiu
> por inteiro da linha 389 (ficou "…por consulta `\citep{Settles2012}.`") e
> Shannon foi **realocado para a Eq. `eq:entropy`**, linha 419: "seleciona pela
> **entropia** da distribuição completa, a medida de incerteza de
> `\citet{Shannon1948}`". É a régua do item (c) aplicada — a citação passou a
> estar onde o conceito é tecnicamente exato, porque a entropia de Shannon é
> literalmente a quantidade dentro daquela equação. **Total do relatório
> permanece 23**: este item nunca esteve na contagem (é de t2, não de t4/t5).
> Deixo o registro abaixo intacto porque a história dele — dois revisores
> discutindo a preposição quando a pergunta era se a citação devia existir —
> continua sendo o argumento de por que o checklist do autor pega o que nós
> não pegávamos.


O item **(c) autoridade decorativa — "no espírito de X"** descreve exatamente
uma frase **que eu escrevi hoje**, no t2:

> "maximizar a informação obtida por consulta \citep{Settles2012}, **no espírito
> de** \citet{Shannon1948}: buscar ativamente a informação que mais reduz a
> incerteza."

A história dela é instrutiva. O texto original tinha "— no espírito de Shannon";
no R1 eu converti para "; **é o** espírito de"; o revisor2 observou, com razão,
que isso **atribuía** a Shannon uma posição sobre aprendizado ativo que ele não
tomou; e eu restaurei o "no espírito de", tratando o problema como resolvido.

**O checklist do autor diz que nenhuma das duas serve.** A citação deve estar
onde o conceito é **tecnicamente exato**, não onde soa bem — e Shannon (1948)
é teoria da comunicação, não seleção de instâncias. Nós dois discutimos qual
preposição usar quando a pergunta era se a citação devia existir ali.

**Sugestão**: remover a evocação e manter a frase técnica, ou citar Shannon onde
a entropia é de fato usada (a Eq. da amostragem por incerteza). Não é da minha
faixa nesta tarefa — registro porque é meu e porque mostra que o checklist pega
o que dois revisores deixaram passar.

---

## t4 — Classificação de texto curto (linhas 715-810)

### (a) Palavras infladas — 3 ocorrências

| # | Trecho | Proposto |
|---|---|---|
| 1 | "caixa alta e abreviações **agressivas**" | "caixa alta e abreviações **extensas**" — ou dizer a medida: o próprio exemplo `CERV BRAHMA LT 350ML` já mostra o grau |
| 2 | "a cauda longa de classes torna o Macro F1 **implacável**" | "a cauda longa de classes torna o Macro F1 **sensível a classes não cobertas**" — diz o mecanismo em vez de personificar |
| 3 | "foram investigadas **em profundidade** na dissertação" | "foram investigadas na dissertação" — o "em profundidade" não acrescenta e é autoelogio (a dissertação é do próprio autor) |

### (b) Metáfora — 2 ocorrências

| # | Trecho | Proposto |
|---|---|---|
| 4 | "o que o torna o **laboratório** adequado para o framework proposto" | "o que o torna **um caso de teste adequado**" |
| 5 | "cada classe descoberta tarde **custa caro** na métrica" | "cada classe descoberta tarde **reduz o Macro F1 de forma desproporcional**" |

### (f) Estrangeirismo sem glosa / sigla sem expansão — 6

| # | Termo | Onde | Proposto |
|---|---|---|---|
| 6 | \textit{stopwords} | pré-processamento | glosar: "palavras funcionais de alta frequência (\textit{stopwords})" |
| 7 | \textit{stemming} | idem | glosar: "redução ao radical (\textit{stemming})" |
| 8 | TF--IDF | representações | expandir na 1ª ocorrência |
| 9 | SVM, KNN | classificadores | expandir na 1ª ocorrência |
| 10 | SBERT | "o SBERT usado pelo DRI-SL" | expandir e atribuir — ver item (g) |
| 11 | PVBin | "o classificador leve PVBin desta tese" | é nome próprio da tese; dizer o que significa na 1ª ocorrência |

### (g) Algoritmo sem dizer de quem é e o que faz — 1

| # | Trecho | Proposto |
|---|---|---|
| 12 | "É dessa família o **SBERT** usado pelo DRI-SL" | dizer autor e função: "o SBERT \citep{Reimers2019}, que produz representações de sentença comparáveis por cosseno" — **conferir contra ficha antes de inserir a chave** |

**Não encontrados em t4**: (c), (d), (e), (h), (i). O bloco está limpo quanto a
autoridade decorativa, nome em prosa sem `\citet`, primeira pessoa e anglicismo.

---

## t5 — Estado da arte e lacuna (linhas 811-938)

### (d) Nome de autor em prosa sem `\citet` — 2 ocorrências, e é o item mais caro

| # | Trecho | Proposto |
|---|---|---|
| 13 | "**Ein-Dor et al.** \cite{EinDor2020}" | `\citet{EinDor2020}` |
| 14 | "**Griesshaber et al.** \cite{Griesshaber2020}" | `\citet{Griesshaber2020}` |

**Por que é o mais caro**: com `\cite`, o PDF imprime "Ein-Dor et al. (EIN-DOR
et al., 2020)" — o nome aparece duas vezes e **o link do sobrenome não existe**.
Com `\citet`, o pacote gera o nome ligado. É defeito de saída, não de estilo.

### (b) Metáfora sem antecedente — 3 ocorrências

| # | Trecho | Proposto |
|---|---|---|
| 15 | "suas duas **fraturas** — partida a frio e oráculo imperfeito" | "suas duas **limitações**" (o checklist nomeia "fratura" explicitamente) |
| 16 | "resolve uma **fratura** isoladamente, mas não as três em conjunto" | idem |
| 17 | "ALPS explora a **\"surpresa\"** do modelo de linguagem" | as aspas já sinalizam desconforto; dizer o mecanismo: "explora a **perplexidade** do modelo de linguagem sobre a instância" — **conferir na ficha do `Yuan2020` qual é o termo do artigo** |

### (f) Estrangeirismo sem glosa / sigla sem expansão — 4

| # | Termo | Proposto |
|---|---|---|
| 18 | "a **survey** de \citet{Xia2025}" | "a **revisão** de" — há palavra em português |
| 19 | "fluxo de rotulagem humano **ad-hoc**" | "fluxo de rotulagem humano **sem protocolo definido**" |
| 20 | "efeito de **cluster perdido**" | glosar: "efeito de agrupamento não coberto (\textit{lost cluster})" — e ver (g) |
| 21 | "categorias **ECOICOP**" | expandir na 1ª ocorrência |

### (g) Algoritmo sem dizer de quem é e o que faz — 1

| # | Trecho | Proposto |
|---|---|---|
| 22 | "**efeito de cluster perdido**" aparece como se fosse termo consagrado | atribuir ao DEUCE ou à fonte que o nomeia, e dizer o que é — **conferir contra a ficha do `Guo2025Deuce`** |

### (a) Palavra inflada — 1

| # | Trecho | Proposto |
|---|---|---|
| 23 | "acrescenta o **alerta prático**" | "acrescenta uma **ressalva de ordem prática**" |

**Não encontrados em t5**: (c), (e), (h), (i).

---

## Resumo

| Item do checklist | t4 | t5 | Total |
|---|---|---|---|
| (a) palavra inflada | 3 | 1 | **4** |
| (b) metáfora | 2 | 3 | **5** |
| (c) autoridade decorativa | 0 | 0 | 0 (mas há 1 em **t2**, minha — ver abertura) |
| (d) nome em prosa sem `\citet` | 0 | **2** | **2** |
| (e) síntese sem chave | 0 | 0 | 0 |
| (f) estrangeiro/sigla | 6 | 4 | **10** |
| (g) algoritmo sem atribuição | 1 | 1 | **2** |
| (h) 1ª pessoa possessiva | 0 | 0 | 0 |
| (i) "eventualmente" | 0 | 0 | 0 |
| | | | **23** |

**Ordem de aplicação sugerida**, por custo e retorno:

1. **Itens 13 e 14** (`\cite` → `\citet`): dois caracteres cada, e são os únicos
   que causam **defeito visível no PDF**. Fazer primeiro.
2. **Itens 15 e 16** ("fratura"): o checklist nomeia o termo; troca mecânica.
3. **Itens 1-5, 18, 19, 23** (inflação e metáfora): edição de registro, sem
   conferência externa.
4. **Itens 6-11, 21** (glosa e sigla): mecânico, mas exige decidir a forma da
   glosa — sugiro que o autor fixe o padrão em um caso e nós replicamos.
5. **Itens 12, 17, 20, 22**: **exigem conferência contra ficha** antes de tocar,
   porque inserem ou reatribuem chave. São os únicos que não devem ser aplicados
   sem essa checagem.

**Uma observação sobre o item (f)**: aplicar glosa a *todo* estrangeirismo
inchraria o texto — "\textit{tweets}", "\textit{embeddings}" e
"\textit{bag-of-words}" já são correntes na área e a tese os usa em itálico, que
é a convenção. Listei apenas aqueles cujo leitor de banca pode legitimamente não
conhecer, ou cuja sigla nunca é expandida. Se o autor quiser a régua mais
estrita, é ampliar a lista; mas **glosar tudo é tão ruidoso quanto não glosar
nada**, e a decisão é dele.
