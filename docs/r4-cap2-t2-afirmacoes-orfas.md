# R4 do tema t2 do Capítulo 2 — afirmações órfãs e atribuições imprecisas

**Escopo**: `2-fundam/texto.tex`, linhas 210-471 (seção 2.2, "Aprendizado ativo").
**Rodada**: R4 — princípio III da constituição da tese ("Toda afirmação DEVE ser
fundamentada: justificada por argumento explícito, referenciada com citação que
a sustente, ou provada com dados/artefatos. Afirmação órfã — sem argumento, sem
fonte e sem dado — não permanece no texto").
**Executado por**: revisor1 · **Data**: 2026-08-17
**Natureza deste documento**: levantamento. **Nenhuma frase foi reescrita** — a
prosa é superfície do agente `principal`.

## Como li

Percorri as 41 chaves distintas citadas no bloco e cada afirmação declarativa,
classificando em quatro estados:

| Estado | Critério |
|---|---|
| **OK** | tem citação que sustenta, ou argumento explícito, ou dado nosso |
| **A — atribuição imprecisa** | tem citação, mas a fonte não sustenta o que lhe é atribuído |
| **B — órfã** | não tem fonte, não tem argumento explícito e não tem dado |
| **C — a qualificar** | tem fonte, mas fichamento novo da tese restringe o alcance |

O bloco está, no geral, **bem fundamentado**: a formalização (232-254), o
catálogo de cenários (312-330) e as três primeiras famílias de estratégias
carregam citação pertinente em quase toda afirmação. Os problemas abaixo são
pontuais, e quatro deles têm conserto já disponível nos fichamentos entregues
nesta madrugada.

---

## A — Atribuição imprecisa (a fonte não sustenta o que lhe é atribuído)

### A1. Linha 222 — número citado de uma fonte que a própria tese proíbe usar para números
> "transcrições cuja anotação custa dez vezes a duração do áudio `\cite{Settles2012}`"

O fichamento `fichamentos/Settles2012.md`, na seção "Números que posso citar",
diz textualmente: *"(Livro conceitual; usar como fonte de definições, não de
números.)"*

A tese extrai um número quantitativo de uma obra que o seu próprio registro de
leitura declara imprópria para isso. É violação simultânea do princípio II
(referência validada contra fichamento) e do princípio V (nenhum número sem
artefato rastreável).

**Conserto possível**: (a) localizar o número no livro e registrar página no
fichamento, corrigindo a nota; ou (b) trocar por fonte primária que meça custo
de transcrição; ou (c) remover o número e manter o argumento qualitativo
("anotação cujo custo é múltiplo da duração do material").

### A2. Linha 319 — prevalência atribuída a uma fonte que estabelece origem
> "o **aprendizado ativo com acervo fixo** (*pool-based*), o cenário desta tese
> e **o mais comum na prática** `\cite{Lewis1994}`"

O fichamento `Lewis1994.md` registra a obra como *"Origem do uncertainty
sampling E do cenário pool-based"*. Origem não é prevalência, e um artigo de
1994 não pode atestar o que é mais comum na prática hoje.

**Conserto possível**: mover a citação de prevalência para `Settles2012`
(survey, que caracteriza a distribuição de uso na área) e manter `Lewis1994`
para a origem do cenário — as duas citações na mesma frase, com papéis
distintos.

### A3. Linha 461 — critério de parada atribuído à versão errada da obra
> "critérios baseados na estagnação do desempenho […] ou em **razões de
> custo-benefício** `\cite{Rouzegar2024}` evitam pagar rótulos que só compram
> ruído"

`Rouzegar2024` é o artigo de 6 páginas do arXiv (2406.12114). Li o PDF inteiro
ao fichá-lo: ele **não propõe critério de parada**. Analisa custo por ponto de
F1 (Figura 2), o que é outra coisa. O critério de parada custo-consciente é o
**PICR**, e o PICR só aparece em `Rouzegar2024Thesis`, a dissertação de 99
páginas que estende o artigo.

**Conserto possível**: trocar a chave para `Rouzegar2024Thesis`, ou reformular
para "análises de custo por ponto de desempenho `\cite{Rouzegar2024}`", que é
o que o artigo de fato faz.

### A4. Linhas 440-442 — metade da frase fica sem cobertura da citação
> "o problema se agrava **em texto curto, onde cada instância carrega pouca
> informação**, e com classificadores profundos, cujo re-treinamento frequente
> é caro `\cite{Fromme2022}`"

`Fromme2022` sustenta a segunda metade e mede o custo com números (Tab. 3,
p. 4602: de 3,80 s a 123 s por 1.600 textos, e o CVIRS chegando a semanas de
experimento). Mas **não estuda texto curto**: seus sete conjuntos são EurLex
(textos jurídicos), arXiv (resumos), NYT (notícias), RCV1, Yelp, AGNews e
Toxic. Em nenhum momento afirma que instância curta carrega pouca informação.

Com a citação no fim do período, o leitor a lê como cobrindo a frase toda. A
metade "texto curto" fica órfã.

**Conserto possível**: separar as duas afirmações e apoiar a de texto curto nas
fontes que a tese já usa na seção 2.4, ou deslocar a citação para logo após
"classificadores profundos".

---

## B — Afirmações órfãs (sem fonte, sem argumento explícito, sem dado)

### B1. Linha 390 — alegação absoluta sem fonte
> "**É a única família que otimiza diretamente o objetivo final**"

"Única" é quantificador universal sobre toda a literatura. Não há citação. O
resto do período traz argumento de custo, mas a alegação de unicidade fica
descoberta.

**Conserto possível**: citar uma das fontes já presentes na frase anterior
(`Roy2001`, `Cohn1996`) se alguma faz a afirmação, ou abrandar para "é a
família que se propõe explicitamente a otimizar o objetivo final".

### B2. Linhas 408-410 — dupla afirmação sem fonte, com conserto disponível
> "Sua hipótese de trabalho — estrutura dos dados correlacionada com a
> distribuição dos rótulos — **nem sempre vale**, e o **custo de computar a
> estrutura não é desprezível**."

As duas metades são exatamente o que `Fromme2022` mede, e a tese já cita essa
chave em outro ponto:
- "nem sempre vale" → §6.1, p. 4603: o AL só melhora o classificador em
  conjuntos de **baixa co-ocorrência de rótulos**; nos demais a seleção empata
  ou perde para a aleatória;
- "custo não desprezível" → Tab. 3, p. 4602, com os tempos por estratégia.

**Conserto possível**: acrescentar `\cite{Fromme2022}` ao fim do período. É o
conserto mais barato desta lista — uma chave, sem reescrita.

### B3. Linha 452 — a natureza do erro do LLM afirmada sem fonte
> "Quando o oráculo passa a ser um LLM, essa fratura muda de natureza — **o
> erro torna-se sistemático e estruturado**"

Sem citação no ponto. O texto remete adiante ("tratada em profundidade na
Seção 2.3"), o que atenua mas não fundamenta a afirmação onde ela é feita.

**Conserto possível**: `\cite{Song2023NoisyLabels}`, fichado hoje, dá o nome
formal ao fenômeno — ruído **assimétrico** (dependente de rótulo), em que a
classe verdadeira tende a ser trocada por uma classe específica e não por
qualquer outra (§II-A-1, p. 2). **Atenção**: citar o survey aqui é correto para
a *taxonomia*; não é correto usá-lo para afirmar que esse ruído é menos danoso
— ver o aviso sobre `5-resultados-falco/texto.tex:143`.

### B4. Linhas 457-458 — comportamento da curva afirmado sem fonte
> "o **ganho marginal por lote decresce** ao longo da curva de aprendizado"

É consenso da área, mas consenso não é fundamentação. Sem citação e sem
remissão a dado nosso.

**Conserto possível**: apontar para a própria curva do E6 (a tese já a possui)
ou para `Settles2012`.

### B5. Linhas 329-330 — afirmação de fato sobre o mercado, sem fonte
> "hoje **reencarnado no cardápio de LLMs com preços e acurácias diferentes**,
> que é precisamente o cenário do FALCO"

Afirmação factual sobre a oferta atual de modelos, sem fonte e sem remissão a
artefato.

**Conserto possível**: remeter à tabela de preços e modelos do Capítulo 3, que
é artefato próprio da tese — resolve pelo princípio III (provada com dados) sem
precisar de citação externa.

---

## C — Afirmações a qualificar (a fonte sustenta, mas fichamento novo restringe)

### C1. Linhas 348-349 — "linha de base forte" merece recorte de regime
> "permanece linha de base forte em *deep learning* `\citep{Gal2017}`"

A citação sustenta a afirmação no regime em que `Gal2017` foi feito. Mas
`Fromme2022`, agora fichado, mostra que em **rótulo extremo** (100 a 739
classes) nenhuma estratégia de seleção — a incerteza inclusive — supera a
seleção aleatória de forma consistente (§7, p. 4604).

Como o FALCO opera em 621 classes, deixar a afirmação sem recorte cria tensão
com o próprio Capítulo 5.

**Conserto possível**: acrescentar a ressalva de regime na mesma frase. Isso
**fortalece** a tese: transforma o braço aleatório de espantalho em linha de
base com respaldo publicado, e um resultado positivo passa a valer mais.

### C2. Linha 439 — a fonte existe, o fichamento existe, a evidência não
> "o modelo não sustenta seleções melhores que o acaso `\cite{Bayer2024}`"

Duas observações:

1. **Chave**: na `main` a citação ainda é `Bayer2024`, mas na branch
   `bibfix/lotes` essa chave foi unificada em `Bayer2024ActiveLLM` e o texto já
   foi repontado. Após o gate do bib-fix, esta linha citará
   `Bayer2024ActiveLLM`, cuja saída impressa muda de "(BAYER; REUTER, 2024)"
   para "(BAYER; LUTZ; REUTER, 2026)" — mudança visível ao leitor, já sinalizada
   ao autor.
2. **Evidência**: o fichamento `Bayer2024ActiveLLM.md` registra o claim C1
   ("Estratégias clássicas de AL falham no cold start few-shot") com o campo de
   evidência preenchido como **`(preencher c/ PDF final)`**. Ou seja: a
   afirmação do Capítulo 2 apoia-se num claim cuja localização no artigo nunca
   foi registrada.

Pelo princípio II a referência não está validada contra fichamento enquanto a
evidência for um marcador de pendência.

**Conserto possível**: completar a evidência no fichamento a partir do PDF
(seção/página) — trabalho de fichamento, não de prosa. Fica na minha fila.

---

## Resumo executável

| # | Linha | Estado | Conserto | Custo |
|---|-------|--------|----------|-------|
| A1 | 222 | atribuição imprecisa | número sem fonte válida: localizar, trocar ou remover | médio |
| A2 | 319 | atribuição imprecisa | separar origem (Lewis1994) de prevalência (Settles2012) | baixo |
| A3 | 461 | atribuição imprecisa | trocar para `Rouzegar2024Thesis` ou reformular | baixo |
| A4 | 440-442 | atribuição imprecisa | separar "texto curto" de "classificador profundo" | baixo |
| B1 | 390 | órfã | citar ou abrandar "única" | baixo |
| B2 | 408-410 | órfã | acrescentar `\cite{Fromme2022}` | **mínimo** |
| B3 | 452 | órfã | acrescentar `\cite{Song2023NoisyLabels}` (só taxonomia) | **mínimo** |
| B4 | 457-458 | órfã | apontar para a curva do E6 ou `Settles2012` | baixo |
| B5 | 329-330 | órfã | remeter à tabela de modelos do Cap. 3 | baixo |
| C1 | 348-349 | a qualificar | ressalva de regime com `Fromme2022` | baixo |
| C2 | 439 | evidência pendente | completar o fichamento (minha fila) | médio |

**Onze itens em 262 linhas e 41 chaves.** Nenhum é fabricação de fonte; a
maioria é citação no lugar errado ou afirmação de consenso sem âncora. Cinco
consertam-se acrescentando uma chave que a tese já possui.

## Checagem executável associada (princípio IX)

Duas das verificações acima podem virar script e deixar de depender de leitura
humana. Proponho ao dono de `scripts/` (revisor2) como extensão do `check-bib`:

```
# 1. claim ancorado em evidência-marcador de pendência
grep -l "(preencher c/ PDF final)" fichamentos/*.md \
  | xargs -n1 basename | sed 's/.md$//' \
  | while read k; do grep -l "\\\\cite[a-z]*{[^}]*$k" */texto.tex; done

# 2. número citado de fichamento que se declara impróprio para números
grep -l "não é fonte de números\|não de números" fichamentos/*.md
```

A primeira acha exatamente o caso C2; a segunda, o caso A1. Não implementei:
`scripts/` tem dono declarado por arquivo e isto é proposta, não intervenção.
