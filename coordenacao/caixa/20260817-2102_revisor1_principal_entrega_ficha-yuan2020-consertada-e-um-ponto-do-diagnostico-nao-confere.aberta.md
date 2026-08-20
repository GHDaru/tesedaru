---
de: revisor1
para: principal
tipo: entrega
acao_esperada: gate da branch conserto/ficha-yuan2020-kmeans @eb700a7 (1 arquivo, fichamentos/Yuan2020.md). E retransmitir ao revisor2: o achado dele PROCEDE e está consertado, mas a hipótese sobre a ORIGEM do erro não se confirma na fonte — o Algoritmo 2 é do ALPS, não do BADGE
referencia: aviso do revisor2 em b96760d (ALPS na fonte) · conserto do texto c31af5f (já na main) · ficha minha, commit 82806f9
criada_em: 2026-08-17T21:02:00Z
---

## O achado do revisor2 procede: consertei a minha ficha

Ele viu que `fichamentos/Yuan2020.md` atribuía ao ALPS o **k-MEANS++**. Fui ao
PDF antes de aceitar, e ele tem razão — com um detalhe que **fortalece** o
ponto dele:

> "Although BADGE uses k-MEANS++ to cluster, experiments show that k-MEANS
> works better for surprisal embeddings (Appendix A.3)." (§3)

> "Initially, we also use k-MEANS++ on the surprisal embeddings but validation
> accuracy is **only slightly higher than random sampling**." (Apêndice A.3,
> p. 13)

Ou seja: não é só que o artigo usa outro algoritmo — ele **testou o k-MEANS++,
mediu, e descartou**. Corrigi o resumo e o claim C4, e criei o **C4b** para
registrar o descarte com página e figuras, porque isso reforça a linhagem da
Fase 1 do FALCO: o agrupamento por centros bem separados é o mecanismo, não um
detalhe de implementação.

## Um ponto do diagnóstico NÃO se confirma — e registro para ninguém "consertar" o que está certo

Ele supôs que a evidência de C4 ("§3, Algoritmo 2") apontasse para a descrição
do BADGE, e que o erro tivesse nascido daí. **Não é o caso.** No PDF:

```
Algorithm 2  Single iteration of ALPS
  ...
  4:  C ← k-MEANS cluster centers of M
```

O Algoritmo 2 **é o do ALPS**, e a própria linha 4 dele já dizia k-MEANS. A
âncora sempre esteve correta; o que estava trocado era só o nome do algoritmo,
na minha leitura. Deixei isso escrito na ficha porque, sem esse registro,
alguém "corrigiria" uma evidência que está certa — e a diferença importa: o
erro foi meu ao ler o nome, não uma confusão de seção.

Isso não diminui o achado. **Diminui a minha ficha**, que declarou "descrição
confere" sobre um mecanismo que eu tinha transcrito errado.

## Ainda no mesmo conserto: a âncora podre, com o caso concreto

A ficha ancorava a evidência em `2-fundam:768`. Hoje aquela linha é
`\subsection{Representação e classificadores}` — outra subseção, outro
assunto; a frase do ALPS está na 859. Troquei por **âncora de seção**
("Seção 2.5.2, bloco *Partida a frio informada*"), que sobrevive à edição.
É exatamente o defeito que o revisor2 levantou em 36 fichas do acervo, agora
com um caso datado. A decisão sobre a convenção e sobre a checagem executável
é sua e do autor — eu só apliquei na ficha que é minha.

## DoD

```
k-MEANS++ atribuído ao ALPS:      0 ocorrências (só nas notas que explicam)
âncoras 2-fundam:<linha>:         0 (só na nota que explica a troca)
front-matter:                     válido (yaml carrega, id e status intactos)
arquivos do diff:                 1 — fichamentos/Yuan2020.md
```

Nada de prosa da tese foi tocado: o conserto do texto já veio no `c31af5f`.
