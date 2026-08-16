---
de: principal
para: executor01
tipo: tarefa
acao_esperada: assumir como DONO a rastreabilidade número→experimento→código→evidência da tese e a organização/padronização de TODOS os notebooks; esta tarefa ABSORVE a 20260816-2026 (notebooks auditáveis)
referencia: decisão do autor 2026-08-16 · tese em tesedaru (Caps. 3-6 + apêndices) · resultados em activelearning/experiments e results/ · kernels Kaggle ghdaru/*
criada_em: 2026-08-16T22:05:00Z
---

# Rastreabilidade total: cada número da tese aponta para sua evidência

Pedido literal do autor: "vasculhe toda a dissertação em relação aos números
e procurar o experimento que a suporta, ou aonde está o código e as
evidências da rodada para termos rastreabilidade de tudo que foi feito e
inclusive, colocar para rodar em um jupyter no kaggle. De forma a ficar
organizado. Inclusive ele será responsável pela organização e padronização
dos nomes dos notebooks, pois já está cheio, ele deve auditar o que tem
inclusive."

## Etapa 1 — Auditoria do que existe (começar por aqui)

Inventário de TODOS os notebooks: kernels no Kaggle (ghdaru/*), notebooks
nos repositórios (activelearning, tesedaru, legados). Para cada um: nome
atual, o que roda, de qual experimento, estado (roda? desatualizado?
duplicado?). Proponha e aplique o padrão de nomes (sugestão de partida:
`falco-<exp>-<descricao-curta>[-s<seed>]`, ex.: `falco-e3prime-s42` já
segue). Duplicados/mortos: listar para o principal antes de apagar qualquer
coisa — nada some sem registro.

## Etapa 2 — Varredura dos números da tese

Percorrer capítulo a capítulo (ordem: 5-resultados, 4-resultados-l0,
3-metodo, 6-conclusao, apêndices, pré-textuais) e, para CADA número
reportado (tabelas e inline): de qual experimento vem, qual artefato o
contém (arquivo JSON/CSV + repositório + commit), qual código o produziu
(script/notebook), e se a rodada tem evidência recuperável.

Saída versionada: `docs/records/rastreabilidade.json` no tesedaru —
lista de itens `{numero, onde (arquivo:linha), experimento, artefato,
codigo, notebook_kaggle, status}` com status em
`rastreado | sem-evidencia | divergente`. Esse arquivo vai alimentar uma
página do site depois — capriche na estrutura, não no visual.

**Os `sem-evidencia` e `divergente` são o produto principal**: reporte ao
principal por lote (um aviso por capítulo), não no final de tudo.

## Etapa 3 — Notebooks reprodutores no Kaggle

Para cada experimento citado na tese, um notebook Kaggle padronizado e
VISUAL (o autor vai auditar olhando, não lendo código): células com
markdown explicando o que se espera, execução, e no fim a comparação
número-do-notebook × número-da-tese. Aproveite os que já existem
renomeando; crie os que faltarem.

## Regras

- Você NÃO edita texto da tese nem o bib: divergência achada → aviso ao
  principal, que trata a prosa.
- Trabalhe em lotes com conclusão por capítulo (cadência §3); claim no
  início de cada lote.
- A recomendação de regime da sua mensagem 2130 foi superada pela decisão
  do autor (s42 canônica, executando); a hipótese de sub-treino segue viva
  como decisão pendente do autor — não a execute sem ordem.
