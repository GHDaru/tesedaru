# QA Report 003 — Página Referências

- **Lane**: light — spec é a tarefa do `principal` (`coordenacao/caixa/
  20260816-2110_principal_site_tarefa_pagina-tabela-de-referencias.aberta.md`),
  já completamente especificada; `ux-design.md` deste ciclo cobre o porquê
  das decisões de tela. Sem plan.md/tasks.md separados — rastreados nesta
  sessão via lista de tarefas, não como artefato do repositório.

## Três bugs reais encontrados e corrigidos durante o próprio desenvolvimento

1. **Hang total do build**: `markdown_to_html()` entrava em loop infinito
   sempre que um parágrafo de fichamento começava com `**negrito**` (ex.:
   `fichamentos/Bengar2022ClassBalanced.md`, linha 47) — o critério de
   parada do parágrafo usava `startswith(("#","|","-","*"))` (sem exigir
   espaço depois), diferente do critério de despacho que exigia espaço
   (`^[-*]\s+`), então uma linha começando com `**` nunca avançava o
   índice. Corrigido com uma única função `_is_block_start()` usada nos
   dois lugares — nunca mais podem divergir. Adicionada também uma trava de
   segurança genérica (se nenhum ramo avançar `i`, força +1) para qualquer
   caso futuro do mesmo tipo não travar o build inteiro de novo.
2. **Acentos não convertidos**: cedilha (`\c c`, com espaço — este .bib usa
   essa forma) não batia com o regex, que só previa `\c{c}`/`\c c` sem
   espaço variável; e 4 diacríticos raros (caron `\v`, ogonek `\k`, e os
   símbolos sem argumento `\l`/`\L` do polonês) não tinham conversão
   nenhuma, deixando barras invertidas literais no nome de autores (ex.:
   "Dem\vsar" em vez de "Demšar"). Corrigido: regex de acento aceita espaço
   opcional, e as três famílias que faltavam foram adicionadas.
3. **Parser de BibTeX quebrava campos com vírgula dentro de aspas**: o
   divisor de campos só respeitava `{}` aninhado, não aspas — um campo
   como `author = "Zhang, Zhisong and Strubell, Emma and Hovy, Eduard"`
   (chave `zhang2022surveyAL`) tem vírgulas DENTRO da string, e cada uma
   virava (erradamente) um separador de campo, produzindo autores como
   `"Zhang` com aspas soltas. Corrigido: `_split_top_level` agora rastreia
   estado "dentro de aspas" e ignora vírgulas nesse estado.

Nenhum dos três foi encontrado por inspeção de código — todos apareceram
rodando o script contra os dados REAIS (378 entradas do bib, 152
fichamentos) e olhando o resultado, não só testando com exemplos
inventados pequenos.

## Verificação (Playwright/Chromium, dados reais)

- **0 erros de console** nas 5 páginas do site (Controle, Plano,
  Coordenação, Resultados, Referências).
- **378 referências, 152 citadas** — contagem confere com
  `grep -c "^@" referencias.bib` (378) e a distinção citada/órfã é real
  (verificado: `Aggarwal2012` citado mas não fichado vs.
  `Aggarwal2012MiningText` fichado mas não citado sob essa chave — duas
  entradas BibTeX genuinamente diferentes, não um bug).
- **Ordenação**: clique em "Título" ordena asc (A→Z) e desc (Z→A)
  corretamente; terceiro clique volta à ordem padrão (# crescente),
  confirmado via `aria-sort`.
- **Busca**: filtro por texto ("active learning") retorna exatamente as
  108 linhas que de fato contêm o termo (conferido contra o JSON bruto via
  Python, não só confiando na tela).
- **Detalhes**: expande com o fichamento renderizado (título, resumo,
  tabela de claims, listas) — testado com `alsmadi2019shorttext`;
  chave sem fichamento mostra "Ainda não fichada." (testado com
  `Aggarwal2012`, que é citada mas não fichada).
- **Tamanho**: 527KB de `referencias.json` (todos os corpos de fichamento
  já em HTML) — muito abaixo do teto de 8MB que a tarefa citou como
  gatilho para carregamento sob demanda; decisão de não implementar
  lazy-load registrada em `ux-design.md` §5.
- **Responsividade**: tema claro/escuro corretos; mobile (390px) — tabela
  rola horizontalmente dentro do próprio container (`.scroll`), o `body`
  nunca rola lateralmente (confirmado: `scrollWidth <= innerWidth`).
- **Regressão**: as outras 4 páginas (Controle/Plano/Coordenação/
  Resultados) seguem funcionando sem mudança de comportamento — só a
  sidebar (novo item "Referências") e o `main()` mudaram fora da nova
  função `build_referencias()`.

## Closing tail

- `TAIL:review` — n/a nesta rodada: lane light, mudança aditiva (função
  nova + item de sidebar), sem alterar nenhuma função existente das outras
  4 páginas; verificação própria com evidência acima substitui a revisão
  formal em contexto fresco para este ciclo leve. Registrado no aviso ao
  `principal` para que ele decida se quer pedir revisão adicional.
- `TAIL:security` — o parser de BibTeX/Markdown/LaTeX é só leitura de
  arquivos do próprio repositório (sem entrada de usuário, sem rede); todo
  texto passa por `esc()` antes de entrar no HTML da tabela, e o Markdown
  dos fichamentos vira HTML pelo conversor próprio (sem `eval`/execução).
  n/a como risco de segurança real.
- `TAIL:gate` — n/a: site/painel dispensa gate de merge humano (ADR 0010).
