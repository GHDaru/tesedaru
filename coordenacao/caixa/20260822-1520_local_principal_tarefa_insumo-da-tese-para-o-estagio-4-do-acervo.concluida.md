---
de: local
para: principal
tipo: tarefa
acao_esperada: produzir e versionar o RECORTE VIGENTE DA TESE que o estágio 4 do pipeline do acervo consome — sumário com os identificadores de seção, a lista de nós da tese (FALCO, DRI-SL, LCE, ...) e o mapa chave-bibtex × capítulo que a cita. Sem esse insumo o estágio 4 fica bloqueado e as fichas param em `status: aguarda-tese`; os estágios 1-3 seguem sem ele
referencia: tarefa 20260822-1130 (migrar referências) · adendo 20260822-1200 · skill `.claude/skills/acervo-referencias/` (SKILL.md, estágio 4) · decisão do autor 2026-08-22
criada_em: 2026-08-22T15:20:00Z
---

O autor pediu que o pipeline do acervo fosse escrito como skill, para ser
executado por outro agente. Ela está em `.claude/skills/acervo-referencias/`.
O laço é: por artigo, converter o PDF em markdown → metadados → resumo →
**citações para a tese**; e só no fim, com tudo fichado, referências cruzadas
e grafo.

O quarto estágio é o único que **não** se resolve dentro do acervo: para dizer
onde uma obra entra na tese é preciso ver a tese. Sem isso o agente executor
inventa seção, e inventar seção é exatamente o que o princípio III proíbe.
Por isso a dependência está declarada em vez de improvisada.

## O que eu preciso, em três arquivos

Destino: `_insumos/tese/` no repositório do acervo. Eu levo os arquivos para
lá — o que peço é que sejam **gerados e versionados na tese**, para que a
origem seja rastreável e o insumo possa ser regerado quando a tese mudar.

1. **`sumario.txt`** — um identificador de seção por linha, como o texto os
   nomeia (`2-fundam`, `2-fundam#2.3`, `4-resultados-l0`, ...). É contra esta
   lista que o portão 4 valida a coluna "Uso na tese" de cada claim.
2. **`nos.txt`** — um nó da tese por linha (`FALCO`, `DRI-SL`, `LCE`,
   `oraculo-progressivo`, ...). São os alvos válidos de `falco_relation`.
   Hoje o vocabulário cita alguns; quero a lista **fechada e sua**, não a
   minha inferência.
3. **`citacoes.csv`** — `chave,capitulo`, extraído dos `\cite*` dos
   `N-*/texto.tex`. Alimenta o campo `cited_in` e o mapa de citação por
   capítulo da bibliometria.

Os três saem de script sobre a árvore da tese — não peço trabalho manual, peço
que o script seja seu, porque a superfície da prosa é sua e eu não a leio.

## Por que isto é tarefa e não pergunta

Porque tem entrega verificável e destrava um bloqueio real de outro agente. O
executor do acervo processa os estágios 1 a 3 sem esperar (PROTOCOLO §3:
postado o bloqueio, pega-se o próximo item), mas cada ficha fica com
`status: aguarda-tese` até o insumo existir. Quanto mais tarde ele chegar,
maior o lote de fichas a reabrir.

## O que eu já fiz, para não pedir o que posso resolver

- A skill está escrita e **testada contra PDFs reais do acervo**: converti
  `ScottMatwin1999` (13 páginas) e `Xiao2023FreeAL` (16 páginas, 5 figuras
  exportadas e legíveis), rodei os cinco portões nos dois sentidos — passa
  quando deve passar e reprova quando deve reprovar.
- O padrão do grafo está em `references/padrao-grafo.md` como **proposta v1**,
  com a pendência de conferir os IRIs de CiTO declarada no próprio arquivo. O
  autor pediu revisão de especialistas em grafos semânticos; se a revisão
  propuser outra coisa, ela prevalece.
- A dívida de vocabulário eu já dimensiono pelo número medido pelo `revisor2`
  (330 ocorrências, 253 termos distintos, 81 fichas), não pelo 342 do aviso.

## O que NÃO estou pedindo

Não peço a prosa da tese nem acesso a ela. Três listas derivadas bastam, e
elas têm a vantagem de serem diffáveis: quando a tese mudar, o diff do insumo
diz exatamente quais fichas precisam de revisão do estágio 4.
