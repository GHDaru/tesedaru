# Esquemas TikZ propostos para o processo metodológico (tarefa 1810)

> Sugestões da banca para decisão do autor — **não mergeadas**. TeX/TikZ puro,
> usando somente as bibliotecas já carregadas em `packages.tex` (`arrows.meta`,
> `positioning`) e o idioma visual das duas figuras TikZ já aceitas no Cap. 3
> (mesmos estilos de caixa, preenchimentos em cinza, setas Stealth, fonte
> footnotesize). FREEZE respeitado: nenhum número novo, nenhum resultado.

## Decisão de escopo (por que DOIS esquemas, e não quatro)

Dos quatro candidatos da tarefa, dois **já existem como figuras aceitas** no
Cap. 3: o laço FALCO com a máquina de fases (figura da Seção do framework, que
já mostra fases, transição por estagnação e encerramento por orçamento/exaustão)
e o pipeline de dados (`fig:dados-fluxo`). Duplicá-los seria poluição. Os dois
construídos aqui são exatamente os que **não têm figura**:

## Esquema 1 — `esq-gate-e-regua.tex`

**O que esclarece**: as DUAS decisões com a mesma razão de 0,95 que estruturam a
tese — o gate do oráculo (aprovação a 85% na S-rand, com o ramo de falha
pré-fixado) e o critério da hipótese (0,95 x acc(D) sob o teto de 34.724
rótulos) — lado a lado, com a amarração explícita 85% ≈ 0,95 x 89,56%. Hoje
essa simetria só existe em prosa, espalhada entre o Cap. 1 e duas seções do
Cap. 3; é a pergunta mais provável da banca ("por que 85%? por que 0,95?") em
uma figura.

**Onde entra**: Seção `sec:metodo-oraculo-decisao` (fim), com remissão na
Seção `sec:intro-hipotese`.

**Camadas respeitadas**: a figura não afirma qual ramo do gate ocorreu (isso é
resultado); aponta por remissão tracejada para a Seção `sec:res-gate`, onde o
ramo executado e a divergência estão declarados.

## Esquema 2 — `esq-mapa-experimental.tex`

**O que esclarece**: o ENCADEAMENTO do programa experimental, que a
`tab:metodo-experimentos` (uma lista) não mostra: o gate do E0 decidindo se o
E4 ocorre (a única dependência que o texto precisa dizer fora da tabela), o
ciclo real (E5) alimentando um dos braços da avaliação final, o E6 sendo
reavaliado no transformer, e tudo convergindo no E3 e no veredito. Pilares à
esquerda, experimentos no meio, onde-se-lê à direita.

**Onde entra**: Seção `sec:metodo-desenho`, ao lado da tabela (a tabela dá o
mapa de artefatos; a figura dá o fluxo).

**Camadas respeitadas**: usa os códigos E0..E6/E3 (controle interno permitido
no Cap. 3) e fala "um dos braços" sem letra, porque as letras A–E só são
apresentadas nos resultados.

## Loop de melhoria com goal (registro, como a tarefa pede)

Goal: "muito boa e ilustrativa" = fluxo inequívoco, rótulos claros, coerente
com o texto, sem poluição visual, legível em P&B.

- **Iteração 1** (rascunho): os dois esquemas com todos os elementos.
- **Iteração 2** (autoavaliação contra o goal — reprovada, com 4 defeitos
  achados e corrigidos): (a) no esquema 1, o título da faixa superior invadia a
  caixa "sim" e duas notas de rodapé se sobrepunham — títulos movidos para a
  margem esquerda, notas com larguras e âncoras recalculadas; (b) ainda no 1,
  o bloco de amarração referenciava um nó definido depois dele (erro de
  compilação certa em TikZ) — movido para o fim; (c) no esquema 2, o caminho
  E5→E3 atravessava a caixa do E6 e duas setas curvas de dependência se
  cruzavam — layout refeito em 5 linhas com o E3 embaixo como ponto de
  convergência, e as dependências de configuração viraram UMA nota "o E3
  recebe ainda..." (menos tinta, mesma informação, zero cruzamentos);
  (d) rótulo do E5→E3 corrigido de "braço A" para "um dos braços" (as letras
  são do Cap. 5 — terminologia em camadas).
- **Iteração 3** (autoavaliação por leitura): geometria reconferida nó a nó,
  P&B verificado pela paleta (cinza 8/14/25 + tracejado, sem depender de cor),
  todos os números conferidos contra o texto da main (85; 0,95x89,56; 34.724;
  231.490; 15%; n=1.000; n≈1.863), e cada rótulo relido contra a prosa que
  ilustra.
- **Iteração 4** (ordem do autor: COMPILAR e VISUALIZAR — reprovada): TeX Live
  instalado no contêiner; os dois esquemas compilaram com 0 erros e 0
  overfull, mas a inspeção do PNG renderizado achou defeitos que a leitura de
  coordenadas não pegou: (a) no esquema 1, a seta tracejada da amarração
  atravessava o título "Critério da hipótese", e a caixa "papéis" rewrapava as
  quebras forçadas em 9 linhas estreitas — a amarração virou um conector
  vertical reto entre as duas caixas de decisão (rótulo ao lado, nada cruza
  nada) e a nota do ramo desceu para baixo da caixa; (b) no esquema 2,
  hifenizações feias ("par-tida", "per-feito", "in-dependente") pelo mesmo
  rewrap de quebras forçadas — todos os textos passaram a fluir sem `\\` — e o
  rótulo da dependência E0→E4 era cortado pela própria seta — a condição
  entrou no texto da caixa do E4 e a seta ficou sem rótulo.
- **Iteração 5** (zoom nas regiões suspeitas — 2 defeitos finos, corrigidos e
  reaprovada): as setas sim/não do gate cortavam o "m"/"o" dos rótulos, e a
  diagonal E6→E3 cortava a 1ª linha do seu rótulo; corrigidos com âncoras que
  deixam o texto inteiro do lado livre da linha (`anchor=south east`/`north
  east`/`north west`). Recompilado, zoom reconferido, figura inteira relida.
  **Julgo os dois "muito bons e ilustrativos" por este goal.**

**Evidência visual**: os renders finais estão versionados ao lado
(`preview-esq-gate-e-regua.png`, `preview-esq-mapa-experimental.png`),
gerados por `pdflatex` + `pdftoppm` com as `\ref{...}` simuladas pelos
números reais das seções (invólucro standalone descrito no cabeçalho de cada
`.tex`). Ambas as compilações: 0 erros, 0 overfull.
