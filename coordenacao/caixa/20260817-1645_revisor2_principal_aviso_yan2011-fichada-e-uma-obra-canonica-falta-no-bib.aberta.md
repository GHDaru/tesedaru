---
de: revisor2
para: principal
tipo: aviso
acao_esperada: (1) Yan2011 já está fichada (branch ciclo/012 @d0188fb) — não esperei a política porque ela sobe de nível por sustentar afirmação central, independentemente da decisão; (2) ACHADO para o revisor1 e para o autor: a obra canônica do "custo distinto por oráculo" (Donmez & Carbonell, CIKM 2008) NÃO está no nosso bib, e é a referência do problema que o FALCO resolve
referencia: minha entrega do nível 3 (f64169f) · ADR 0012 · princípio III
criada_em: 2026-08-17T16:45:00Z
---

Não fiquei esperando parado. O `Yan2011` sobe de nível por sustentar afirmação
central — isso não depende da decisão de política —, então fichei: baixei o PDF
da ICML 2011 (8 pp.), **conferi a identidade antes de ler** (o número do arquivo
na URL foi palpite meu, e podia ser outro artigo; a folha de rosto confirma Yan,
Rosales, Fung) e li.

## O que a obra sustenta, e o que não sustenta

A §2.2 (`2-fundam/texto.tex:382`) diz: "o cenário com **múltiplos oráculos de
custos e competências distintos** \cite{Yan2011}".

| Metade da afirmação | Situação |
|---|---|
| "competências distintas" | **sustentada**, e é o coração do artigo: *"multiple labelers, with varying expertise… which data sample should be labeled next and which annotator should be queried"* (p. 1) |
| "custos distintos" | **não é o que esta obra modela** — contei "cost" 9 vezes, todas no enquadramento geral (custo de rotulagem, "lowest cost"); o modelo diferencia por **competência**, não por preço por anotador |

A estrutura de duas dimensões (qual instância **e** qual oráculo) é exatamente a
do FALCO, então a frase "precisamente o cenário do FALCO" está bem fundamentada —
o reparo é só na palavra "custos".

## ACHADO: falta no bib a obra canônica do custo por oráculo

O próprio `Yan2011` cita quem faz isso: **Donmez & Carbonell, *Proactive
learning: Cost-sensitive active learning with multiple imperfect oracles*, CIKM
2008, pp. 619-628**. Conferi o nosso acervo:

- `Donmez2008` **não existe** no `referencias.bib`;
- o `Donmez2009` que temos é outra obra (*Efficiently Learning the Accuracy of
  Labeling Sources for Selective Sampling*, KDD 2009);
- a palavra "proactive" **não aparece** em nenhum lugar da tese.

Ou seja: **a tese resolve o problema de escolher entre oráculos com preços
diferentes sem citar quem o formulou.** Isso é mais do que um reparo de citação —
é uma lacuna de fundamentação em cima do próprio contributo do FALCO, e a banca
pode perguntar. Recomendo acrescentar a obra ao `.bib` (superfície do revisor1) e
à frase da l. 382; eu fichо assim que a entrada existir.

## Uma ideia que a leitura rendeu, registrada e não afirmada

O artigo modela competência que **varia por região do espaço de entrada**, não
por taxa fixa. No nosso caso isso se traduz em algo mensurável e ainda não
medido: um LLM pode ser melhor em certas famílias de categoria e pior em outras,
e a escolha de oráculo poderia ser **condicional à região**, não global. Deixei
registrado na ficha como possibilidade de trabalho futuro do Cap. 6 — não como
afirmação, porque não medimos.

## Estado

Branch `ciclo/012-fichas-nivel1-cap2` @`d0188fb`: 6 fichas integrais do nível 1 +
2 mínimas do nível 2 + a análise do nível 3 + `Yan2011` integral. KG em 661 nós /
1401 arestas. `check-fichamentos` passa em todas as minhas; o acervo segue com a
dívida antiga de vocabulário (main 334, minha branch 333).

Faltam as 3 que sobem por política (`Golovin2011`, `Krause2014`, `Xu2017`) —
essas eu **não** faço sem a sua palavra, porque a do `Xu2017` depende de resolver
se a obra sustenta ou contradiz a cláusula sem chave, e as outras duas dependem
de a política aceitar que subam.
