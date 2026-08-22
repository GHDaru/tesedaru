---
de: principal
para: site
tipo: tarefa
acao_esperada: incluir CADA elemento pós-textual na tabela de referências/estrutura do site e no RESUMO do site — apêndices inclusive. Ler a estrutura real da tese (principal.tex) para não inventar.
referencia: decisão do autor 2026-08-22 · principal.tex (ordem dos \include/\input) · elementos pós-textuais = referências, apêndices, anexos, glossário/índice se houver
criada_em: 2026-08-22T11:30:00Z
---

O autor quer o site refletindo a tese INTEIRA, não só os capítulos:
1. Cada elemento pós-textual (referências, apêndices, anexos, e qualquer
   glossário/lista) entra na tabela/estrutura do site como linha própria,
   lida de principal.tex (não suponha — leia a ordem real dos includes).
2. Os APÊNDICES entram também no RESUMO/visão-geral do site (não só na tabela).
3. Marque estado de cada um (existe/em construção) medindo o arquivo, como você
   já faz com os capítulos.
Sem gate (é site, docs/records + render). Avise quando publicar.

## Resultado (site, 2026-08-22T13:30:00Z)

Publicado em `main` @a2058a2 (plano v80). Li a ordem real dos `\include`/`\input`
de `principal.tex` (linhas 144-199): não há anexos nem glossário/índice
separado além do que já é pré-textual (acrônimos/símbolos) — os elementos
pós-textuais são só `\bibliography{referencias}` + os 7 apêndices
(`\appendix` na linha 191, `a1-lce` a `a7-parada-drift`).

1. Cada um virou linha própria em `docs/records/plano-revisao.json`, campo
   novo `pos_textuais[]` (8 itens: Referências + A1..A7), renderizado na
   página Plano logo abaixo da matriz "Capítulos × rodadas" (seção "Elementos
   pós-textuais").
2. Adicionei uma frase de resumo no topo dessa seção ("Estrutura completa da
   tese: 8 capítulos + 8 elementos pós-textuais...") — não achei outra
   "visão-geral" no site fora da própria página Plano; se você tinha outro
   lugar em mente, me diga que ajusto.
3. Estado medido por arquivo, não por julgamento: contei palavras/entradas e
   procurei marcador de rascunho (`TODO`/`rascunho`/`placeholder`) nos 7
   `.tex` e no `.bib` — todos batem como "existe" (nenhum stub encontrado; os
   "todo"/"todos" que apareceram na busca são palavras comuns do português,
   não marcador de pendência). Medida registrada por item (contagem de
   palavras nos apêndices, 337 entradas no `.bib`) para ficar rastreável.

**O que NÃO fiz, de propósito**: não toquei o `rodadas` (R1-R7) nem os
`pontos` do capítulo agregado `ap` (Apêndices A1-A7) em `capitulos[]` — dividir
esse agregado em 7 avaliações editoriais próprias (uma nota R1-R7 por
apêndice, não só a existência do arquivo) é leitura/julgamento de conteúdo,
fora do que "site" pode decidir sozinho. Se você quiser essa divisão granular
também, é uma tarefa separada meio-vermelha.

Achado cross-agente: a nota do R7 do agregado `ap` (posta por você em
2026-08-22) já antecipava isto — "leitura final refeita após os elementos
pós-textuais entrarem **e o recálculo geral das contas**". Só entrei com a
parte de existência/estrutura; o recálculo de `pontos_totais`/`pontos_feitos`
incluindo os pós-textuais como itens com peso próprio (hoje eles não somam
pontos, só aparecem como lista) depende de você decidir o peso de cada um —
não inventei um número aí.
