---
de: revisor2
para: principal
tipo: aviso
assunto: a descrição nova do ALPS (R7-t5) descreve um mecanismo que o artigo RECUSA explicitamente - e a ficha do acervo atribui ao ALPS o algoritmo do concorrente
estado: aberta
---

O `693f672` (6 edições do R7-t5, aplicadas pela banca sob a exceção do
congelamento) acrescentou uma **descrição técnica** do ALPS na 2.5.2. Fui ao
PDF conferir, porque descrição técnica nova é afirmação nova. Achei dois
problemas — um no texto, outro no acervo. **Não editei nada**: a faixa do t5
está congelada e a ficha não é minha superfície.

# 1. O texto novo descreve um ALPS que o artigo diz não ser

A frase hoje (2.5.2, "Partida a frio informada"):

> "ALPS \cite{Yuan2020} seleciona pela surpresa (\textit{surprisal}) que a
> instância causa ao modelo de linguagem, **medida como a perda de modelagem
> mascarada do próprio BERT: quanto pior o modelo prevê os tokens escondidos da
> instância, mais informativa ela é**, sem exigir nenhum rótulo."

A **primeira metade está certa e é uma boa melhoria** — a perda de modelagem
mascarada é mesmo o sinal, e o "sem exigir nenhum rótulo" é exatamente o que
resolve a partida a frio.

O problema é a segunda metade. "Quanto pior prevê, mais informativa" descreve
uma **ordenação monótona pela perda** — e o artigo antecipa essa leitura e a
**recusa**, com a justificativa explicitada:

> "we may sample several atypical sentences that are similar to each other,
> which is often an issue for uncertainty-based methods. **Therefore, we
> incorporate clustering in ALPS to maintain diversity.**" (p. 5)

> "**Thus, we combine uncertainty and diversity sampling for cold-start AL.**"
> (p. 4)

Ou seja: o ALPS calcula as *surprisal embeddings* e depois **agrupa** para
não sacar várias frases surpreendentes pelo mesmo motivo. Sem o agrupamento,
seria a estratégia que o próprio artigo aponta como defeituosa.

**Por que isso importa para a tese, e não é preciosismo.** A ficha do acervo
registra o ALPS como "o **antecessor conceitual direto da Fase 1 do FALCO**".
O DRI-SL é justamente uma **composição** — densidade semântica mais variedade
lexical, com agrupamento. Descrever o ALPS como ordenação pura apaga o traço em
que ele mais se parece com a nossa fase 1, e deixa o parágrafo sugerindo que a
combinação com diversidade só chega depois, no DEUCE. A banca que abrir o
Yuan2020 vai ver a frase da p. 4.

**Conserto sugerido (uma oração, sem mexer no resto):** depois de "sem exigir
nenhum rótulo", acrescentar algo como "*e agrupa as instâncias antes de
escolher, para não sacar várias frases surpreendentes pelo mesmo motivo*".
Fica fiel e ainda **fortalece** a linhagem da Fase 1. Vai como sugestão ao
autor pela fila, já que a faixa está congelada.

# 2. Erro no acervo: a ficha atribui ao ALPS o algoritmo do BADGE

`fichamentos/Yuan2020.md`, claim C4:

> "O ALPS combina surpresa com diversidade, agrupando os *surprisal embeddings*
> por **k-MEANS++**" — evidência: "§3, Algoritmo 2"

**Medido no PDF: é k-MEANS, não k-MEANS++.** E o artigo não só usa outro
algoritmo como conta que **testou o k-MEANS++ e o descartou**:

> "The state-of-the-art baseline BADGE applies k-MEANS++ on gradient
> embeddings... Initially, we also use k-MEANS++ on the surprisal embeddings but
> validation accuracy is **only slightly higher than random sampling**. Since
> k-MEANS++ is originally an algorithm for robust initialization of k-MEANS, we
> instead apply **k-MEANS** on the surprisal embeddings." (Apêndice A.3, p. 13;
> comparação na Figura 5)

O k-MEANS++ é do **BADGE**, a linha de base contra a qual o ALPS compete
(p. 3). A ficha trocou o algoritmo do concorrente pelo do artigo — e a
evidência aponta "§3, Algoritmo 2", que é a seção onde o artigo descreve o
**BADGE**, não o ALPS. É consistente com o erro ter nascido aí.

Não é fatal (a tese não cita esse número), mas é o tipo de coisa que a ficha
existe para impedir. **A ficha não é minha** (commit `82806f9`, lote das
05h27), então levo o achado em vez de consertar — regra §6 do protocolo. Se
quiser que eu conserte, é uma linha e eu abro branch.

# 3. De brinde, a prova viva do defeito que reportei às 1935

A mesma ficha ancora sua evidência em **`2-fundam:768`**. Conferi na main de
agora: a linha 768 é `\subsection{Representação e classificadores}` — outra
subseção, outro assunto. A frase do ALPS está hoje na **linha 859**. É o
apodrecimento por número de linha que levantei nas 36 fichas, agora com um
caso concreto e datado. Segue de pé a oferta da checagem executável (meia
hora, minha superfície) — só com despacho.

# 4. Gatilho 6 cumprido contra `693f672`

- Merge simulado das **6** branches da fila, worktree recriada a cada
  iteração: **todas limpas**.
- As 7 passagens que reproduzo nos meus artefatos: **todas batem**.
