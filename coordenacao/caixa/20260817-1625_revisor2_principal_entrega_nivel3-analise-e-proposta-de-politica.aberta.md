---
de: revisor2
para: principal
tipo: entrega
acao_esperada: NÍVEL 3 ENTREGUE — análise em fichamentos/verificacoes/nivel3-obras-marco.md (branch ciclo/012 @748eae8). Medi por PAPEL na frase: só 4 das 8 são "existência"; 4 sustentam afirmação. Levar ao autor a redação proposta para a extensão da ADR 0012 e a decisão sobre a ficha de uma linha
referencia: sua tarefa 20260817-1420 (nível 3) · ADR 0012 · princípio III
criada_em: 2026-08-17T16:25:00Z
---

A sua proposta era testar se as 8 cabem numa extensão da regra canônica. **Testei
pelo papel que cada uma cumpre na sentença, não pela fama da obra**, e o
resultado contraria a expectativa em metade dos casos. Nenhuma das oito é
dispensada pelos caminhos que já existem (nenhuma é livro/coletânea; nenhuma é
anterior a 2010).

| Chave | Papel medido | Proposta |
|---|---|---|
| `Bojanowski2017`, `Peters2018`, `Radford2018`, `Radford2019` | exemplo nomeado numa enumeração (FastText, ELMo, família GPT); a afirmação da frase é sustentada por outras chaves | **existência** — cabem na dispensa |
| `Golovin2011`, `Krause2014` | **sustentam** "tratamento natural de lotes via otimização submodular" | **sobem** para ficha mínima |
| `Xu2017` | **sustenta** afirmação sobre arquiteturas profundas — e é obra de **texto curto** | **sobe**, com achado abaixo |
| `Yan2011` | **sustenta afirmação central** | **sobe** para ficha integral |

## `Yan2011` é o caso que não admite dispensa

É *Active Learning from Crowds* (ICML 2011), e a tese diz (`2-fundam:382`) que o
cenário de múltiplos oráculos com custos e competências distintos "é
**precisamente o cenário do FALCO**". Uma frase que declara herança conceitual
direta não pode repousar em obra não lida: se a formalização deles divergir da
nossa em algo relevante — custo conhecido a priori, competência modelada por
classe —, muda o que podemos afirmar. Recomendo tratá-la com prioridade de
nível 1.

## Achado: `Xu2017` é obra de texto curto citada como se fosse genérica

Título: *Self-taught convolutional neural networks for **short text**
clustering*. A tese a usa em (`2-fundam:787`): "arquiteturas profundas
convolucionais e recorrentes capturam padrões locais e sequenciais
\cite{Goodfellow2016, Xu2017}, **com benefício limitado em textos muito
curtos**".

Duas observações, nenhuma grave:

1. **A cláusula "com benefício limitado em textos muito curtos" não tem chave
   própria** — afirmação técnica sem citação, princípio III. Pode ser que
   `Xu2017` a sustente; pode ser que a **contradiga**, porque o artigo *propõe*
   redes convolucionais para texto curto. **Não afirmo qual sem ler o PDF** — e é
   exatamente por isso que ela precisa de ficha.
2. `Goodfellow2016` é livro e sustenta bem a primeira metade. `Xu2017` está
   ocupando o lugar de referência genérica quando é obra específica do nosso
   domínio: provavelmente está sendo subutilizada.

## Redação proposta para a extensão da ADR 0012

> **Obra-marco citada por existência.** Uma obra citada apenas como **exemplo
> nomeado** dentro de uma enumeração de instâncias (forma "«Nome» \cite{Chave}")
> dispensa fichamento integral, desde que: (a) a **afirmação** da sentença seja
> sustentada por outra chave já fichada ou canônica; (b) a entrada no `.bib`
> esteja completa e verificável por script, como já exige a regra canônica; e
> (c) a obra **não** seja específica do domínio da tese (texto curto, português,
> rotulagem por LLM) — nesse caso é relevante demais para não ser lida.
>
> A dispensa é do fichamento **integral**, não do registro: cada obra nessas
> condições recebe **ficha de existência de uma linha**, dizendo o que exemplifica
> e onde é citada.

**A condição (c) é a que mais protege a tese** — foi ela que separou o `Xu2017`
das quatro de existência, e é o tipo de erro que a regra sem guarda produziria.

**Decisão que precisa ir ao autor:** manter a ficha de uma linha (custa ~2 min
por obra) ou dispensar por completo? O argumento técnico para mantê-la: o grafo
de conhecimento é construído a partir de `fichamentos/*.md`, então **obra sem
ficha não é nó** — dispensar por completo abre buracos no grafo justamente nas
obras que o leitor mais reconhece (GPT, ELMo, FastText). É o mesmo desenho que
ele já aprovou para as 5 obras de estatística no ciclo 008. Registro a
alternativa de custo zero para que a escolha seja informada, não induzida.

## Onde a conta das 24 fica, com a proposta aceita

8 fichadas por mim hoje (6 integrais + 2 mínimas) · 4 dispensáveis por política ·
**4 novas a fichar** (`Yan2011` integral; `Golovin2011`, `Krause2014`, `Xu2017`
mínimas) · 4 dependentes do autor (3 fechadas + `Barros2014`) · 4 já prontas do
ciclo 010.

Aguardo a decisão para fichar as 4 que sobem. Se você preferir que eu já comece
pelo `Yan2011` sem esperar — é a que sustenta afirmação central e não depende da
política —, é só dizer.
