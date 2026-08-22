# ux-design.md — Resultados: link do notebook Kaggle por experimento

- **Ciclo**: 012-resultados-notebook-kaggle · **Lane**: light — pedido direto
  do autor ("Coloque no site os experimentos e o link do notebook do Kaggle
  correspondente ao experimento"). A tabela "Experimentos executados" já
  existe (`resultados.html`); o pedido é uma coluna nova.

## 1. O problema real: o dado quase não existe no repositório versionado

Busquei "kaggle.com" em todo o `tesedaru` (mensagens, `.bib`, tudo) antes de
escrever qualquer link. Achado: só **duas** URLs de kernel Kaggle aparecem
documentadas com confiança, e nenhuma delas está num arquivo estruturado —
estão em prosa dentro de mensagens de `coordenacao/`. Fui atrás da fonte
primária que os avisos citavam (`docs/records/rastreabilidade.json`, 74
itens, gerado por `notebooks/auditoria/build_rastreabilidade.py`) e descobri
que esse arquivo nunca foi mergeado na `main` — vive só na branch do
`executor01` `origin/claude/e3prime-seed-7-bx08ks`, buscável por
`git show <branch>:<caminho>` (não aparece em `git log` da main porque nunca
foi commitado lá).

Nessa branch, dos 6 notebooks de auditoria que o `executor01` publicou e
verificou rodando de verdade no Kaggle ("Missão concluída — todas as ondas",
17/08), só **2 têm o slug do Kaggle registrado** no JSON; os outros 4 têm
só o caminho do arquivo local (`notebooks/auditoria/*.ipynb`, no repositório
`activelearning`, não uma URL pública). Os 2 confirmados batem
exatamente com os experimentos E6 e E3′ desta tese (conferi cruzando os
números — "saturação SGD/PVBin", "viés de autoavaliação" no notebook
`escala-populacional` são os mesmos números do achado E6 aqui; "Tabela e3p
A/B/C/E/D", "McNemar" no `classificador-forte` são os mesmos do E3′ aqui).

## 2. Por que não completei os outros 5 experimentos

Existe uma convenção de nome documentada (`falco-auditoria-<experimento>`,
numa mensagem do `executor01` de 17/08) que tornaria trivial "adivinhar" os
outros 4 slugs (`falco-auditoria-escolha-do-oraculo`, `-efeito-do-prompt`,
`-estrategias-e-robustez`, `-conjunto-inicial`). Não fiz isso. Tentei
verificar por rede (`curl` contra `kaggle.com`) mas o proxy deste ambiente
devolve 404 genérico para QUALQUER caminho em `kaggle.com` — inclusive para
o slug que eu já sabia, por prosa confirmada, que existe e roda (`falco-e3-
semente-7`) — então uma checagem de rede aqui não distingue "existe" de
"não existe"; teria sido um sinal falso, não uma confirmação. Sem fonte no
repositório e sem forma de verificar por rede, adivinhar o slug seria
inventar um link — exatamente o que a constituição da tese proíbe
("nenhuma afirmação sem fundamento", princípio III) e o que o próprio schema
de `resultados.json` já institui para o campo `resultado`: **null é a
resposta honesta até então**. Estendi essa mesma regra ao novo campo.

## 3. O que foi implementado

- `docs/records/resultados.json`: cada item de `experimentos[]` ganha
  `notebook_kaggle` (URL ou `null`). E6 → `falco-auditoria-escala-
  populacional`; E3′ → `falco-auditoria-classificador-forte`; E0, E0-P, E1,
  E4, E5 → `null`. `schema_doc.experimentos` documenta a regra de não
  adivinhar. `atualizado_por` registra a autoria do campo separadamente
  (site) e a fonte (branch não mergeada), para não passar como se fosse
  conteúdo verificado pelo `principal`.
- `build_resultados()` (`scripts/render-plano-revisao.py`): 5ª coluna
  "Notebook Kaggle" na tabela de experimentos — link "abrir ↗" quando
  existe, "—" com `title` explicando que ausência de link não é ausência de
  execução (mesmo padrão já usado no selo de "parte detectada" do ciclo 008
  e no `link_s2` de Referências do ciclo 006: nunca esconder a lacuna atrás
  de um traço mudo).

## 4. Achado para o principal (fora do escopo do site, registrado aqui)

`docs/records/rastreabilidade.json` (74 itens, script gerador versionado)
parece ser exatamente o artefato que o princípio V da constituição pede
("nenhum número sem artefato rastreável") — e está pronto, verificado pelo
próprio `executor01` linha a linha, preso numa branch há 5 dias. Decisão de
merge, e de completar os 4 slugs Kaggle que faltam nele, é do `principal`
(planejamento) — não é decisão do site, só o aviso.

## 5. Reuso

Nenhum componente novo; só uma coluna a mais na tabela `<table id=
"experimentos">` já existente, mesma convenção de link externo (`target=
"_blank" rel="noopener"`) usada em Referências e Entregas.
