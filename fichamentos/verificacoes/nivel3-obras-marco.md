# Nível 3 das 24 pendências — as 8 obras-marco, medidas

**Tarefa:** 20260817-1420 do principal, nível 3 · **Executor:** revisor2
**Natureza:** análise e **proposta**. Não editei prosa, não alterei a ADR 0012.
Decisão é do autor; consolidação, do principal.

## Método

Para cada chave: (1) onde é citada, (2) qual a frase, (3) a frase **precisa**
dela ou ela é exemplo nomeado? O critério não é a fama da obra — é o papel que
ela cumpre na sentença. Tipo e ano vêm do `.bib` porque a ADR 0012 dispensa por
**tipo** (livro/coletânea) ou por **ano** (< 2010), e nenhuma das oito é
dispensada por esses caminhos.

## Quadro

| Chave | Tipo/ano | Papel na frase | Proposta |
|---|---|---|---|
| `Bojanowski2017` | article 2017 | exemplo nomeado de \textit{embedding} estático (FastText); a afirmação sobre polissemia é sustentada por `Birunda2021` e `Goldberg2017` | **existência** |
| `Peters2018` | inproceedings 2018 | exemplo nomeado de \textit{embedding} contextual (ELMo) | **existência** |
| `Radford2018` | techreport 2018 | exemplo nomeado (família GPT) | **existência** |
| `Radford2019` | article 2019 | exemplo nomeado (família GPT) | **existência** |
| `Golovin2011` | article 2011 | **sustenta**: "tratamento natural de lotes via otimização submodular" | **sobe: ficha mínima** |
| `Krause2014` | inproceedings 2014 | **sustenta** a mesma afirmação | **sobe: ficha mínima** |
| `Xu2017` | article 2017 | **sustenta** afirmação sobre arquiteturas profundas — e o título é sobre **texto curto** | **sobe: ficha, com achado (abaixo)** |
| `Yan2011` | inproceedings 2011 | **sustenta afirmação central da tese** | **sobe: ficha integral** |

Ou seja: das oito, **quatro** são realmente citadas por existência; **quatro**
sustentam afirmação e não cabem na dispensa. Levei a medição, não a expectativa.

## Por que `Yan2011` não pode ser dispensada

É *Active Learning from Crowds* (ICML 2011). A tese a cita duas vezes, e a
segunda diz o seguinte (§ "Aprendizado ativo"):

> "o cenário com **múltiplos oráculos** de custos e competências distintos
> \cite{Yan2011}, formulado originalmente para anotadores humanos em
> \textit{crowdsourcing} e que hoje se repete na oferta de LLMs com preços e
> acurácias distintos, **que é o cenário do FALCO**."

A frase declara que o cenário desta obra **é o cenário da tese**. Uma afirmação
dessas não pode repousar em obra não lida: se a formalização de Yan e
colaboradores diferir da nossa em algo relevante (por exemplo, se eles supõem
oráculos com custo conhecido *a priori*, ou modelam competência por classe), isso
muda o que podemos dizer de herança conceitual. **Recomendo ficha integral** —
prioridade equivalente ao nível 1.

## Achado: `Xu2017` é obra de texto curto, citada como se fosse genérica

O título é *Self-taught convolutional neural networks for **short text**
clustering*. A tese a cita assim (§ "Classificação de texto curto"):

> "arquiteturas profundas convolucionais e recorrentes capturam padrões locais e
> sequenciais \cite{Goodfellow2016, Xu2017}, **com benefício limitado em textos
> muito curtos**"

Dois problemas de forma, nenhum grave, ambos fáceis:

1. **A cláusula "com benefício limitado em textos muito curtos" não tem citação
   própria.** É afirmação técnica sem chave — princípio III. Pode ser que
   `Xu2017` a sustente; pode ser que a **contradiga**, já que o artigo *propõe*
   redes convolucionais para texto curto, isto é, argumenta pelo benefício.
   **Não afirmo qual dos dois sem ler o PDF** — e é justamente por isso que ela
   precisa de ficha.
2. `Goodfellow2016` é livro (dispensado pela ADR 0012) e sustenta bem a primeira
   metade; `Xu2017` está no lugar de uma referência genérica quando é obra
   específica do nosso domínio. Provável desperdício: ela é mais útil do que o
   uso atual sugere.

## Proposta de política (redação sugerida para extensão da ADR 0012)

> **Obra-marco citada por existência.** Uma obra citada apenas como **exemplo
> nomeado** dentro de uma enumeração de instâncias (a forma "«Nome do método»
> \cite{Chave}") dispensa fichamento integral, desde que cumpra as três
> condições: (a) a **afirmação** da sentença seja sustentada por outra chave já
> fichada ou canônica; (b) a entrada no `.bib` esteja completa e verificável por
> script, como já exige a regra canônica; (c) a obra **não** seja específica do
> domínio da tese (texto curto, português, rotulagem por LLM) — nesse caso ela é
> relevante demais para não ser lida.
>
> A dispensa é do fichamento **integral**, não do registro: cada obra nessas
> condições recebe **ficha de existência de uma linha**, dizendo o que ela
> exemplifica e onde é citada.

**Por que manter a ficha de uma linha em vez de dispensar tudo.** O grafo de
conhecimento é construído a partir de `fichamentos/*.md`: obra sem ficha **não
é nó**. Dispensar por completo economiza dez minutos e abre buracos no grafo
justamente nas obras que o leitor mais reconhece. A ficha de uma linha custa
cerca de dois minutos e mantém o acervo íntegro — é o mesmo desenho que o autor
já aprovou para as 5 obras de estatística no ciclo 008.

**Alternativa, se o autor preferir custo zero:** dispensa total das quatro de
existência, aceitando que `Bojanowski2017`, `Peters2018`, `Radford2018` e
`Radford2019` fiquem fora do grafo. É defensável — elas não sustentam
afirmação —, mas registro a perda para que a escolha seja informada.

## Efeito no número que o autor cobrou

Se a proposta for aceita como está: das 24 pendências reais, **4 saem por
política** (existência) e **4 mudam de nível** (`Yan2011` integral;
`Golovin2011`, `Krause2014`, `Xu2017` mínimas, sendo a de `Xu2017` obrigatória
por causa do achado). Somando ao que já foi entregue nos níveis 1 e 2, a conta
fica: 8 fichadas, 4 dispensáveis por política, 4 novas a fichar, 4 dependentes
do autor (3 fechadas + `Barros2014`), e as 4 do ciclo 010 já prontas.
