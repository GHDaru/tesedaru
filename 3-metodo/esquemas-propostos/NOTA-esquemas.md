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

## Esquema 3 — `esq-drisl.tex` (pedido direto do autor, 2026-08-23)

**Origem**: o autor apresentou um infográfico gerado por ferramenta de imagem
para o DRI-SL e pediu a versão TikZ sóbria para a tese ("faça a versão TikZ
sóbria para a tese em loop"). O parecer da banca sobre o infográfico:
conteúdo correto (conferido linha a linha contra a Seção `sec:metodo-drisl`),
mas inadequado ao PDF por assinatura visual de máquina (princípio X), por ser
raster não reproduzível, e pelos mini-gráficos decorativos que parecem dado
(risco frente ao princípio V). O infográfico serve aos slides da defesa.

**O que a versão TikZ preserva do infográfico**: a decomposição didática em
Fase (i) densidade semântica e Fase (ii) variedade lexical intragrupo, o laço
de seleção iterativa com o escore de novidade ponderado pelo perfil TF--IDF,
as cotas proporcionais com o somatório, e a faixa de avaliação (aleatório +
envelope do AG). **O que ela corrige**: sem ícones, sem cores, sem curvas
decorativas; a citação do codificador de sentenças vai na LEGENDA como
`\citep{Reimers2019SBERT}` (o check-bib a enxerga); a avaliação vira texto
com remissão à Seção `sec:res-l0-drisl` sem afirmar o resultado (terminologia
em camadas: o veredito da comparação é do Capítulo 4).

**Onde entra**: Seção `sec:metodo-drisl` (fim), com a citação na legenda.

**Loop (5 iterações, todas com compilação e inspeção visual)**: (1) rascunho
— referência-adiante do nó `cand` achada e corrigida antes de compilar;
(2) render 1 reprovado: a descida da seta em L atravessava o título da
Fase (ii), o rótulo "fechados os $N_c$ grupos" colidia com as duas caixas do
vão curto, e havia hifenizações por quebra forçada — o título da fase virou o
próprio rótulo da seta em L (um elemento, zero cruzamentos) e o rótulo do vão
foi removido (o laço já diz "repete até $n_i$"); (3) zoom reprovou: o rótulo
em uma linha ainda alcançava a descida vertical — dividido em duas linhas
centradas; (4) a caixa do $L_0$ quebrava a matemática no "=" — blindada com
`\mbox{}`; (5) alargar a caixa para 46mm piorou (duas hifenizações) —
revertido para 44mm com quebras forçadas curtas. Render final: 0 erros,
0 overfull, nenhuma sobreposição. **Julgo "muito boa e ilustrativa".**
Evidência: `preview-esq-drisl.png`.

## Esquema 4 — `esq-preproc-espacos-rotulos.tex` (pedido do autor, 2026-08-23)

**O que esclarece**: a Seção 3.2.3 é a mais densa em contagens do capítulo de
dados; a figura mostra a estrutura que as organiza — a MESMA base normalizada
bifurca em dois espaços de rótulos com papéis distintos: o `CategorySchema`
de 621 categorias (contado sobre as linhas, com a sentinela `_rare_`), que
governa os oráculos, e a visão populacional deduplicada (231.490 textos
únicos, 714 classes presentes, sem `_rare_`), que governa os experimentos do
Capítulo 5. A nota de rodapé da figura carrega as duas chaves de texto e a
receita executável (`scripts/check_dataset.py`). Todos os números são os da
própria seção. **Onde entra**: fim da Seção `sec:metodo-dados-preproc`.

**Loop**: referência-adiante das setas da bifurcação pega antes de compilar;
render 1 reprovado (setas atravessavam os títulos das colunas — os títulos
viraram a 1ª linha das próprias caixas; hifenizações); render 2 reprovado
(quebra forçada mais larga que a caixa re-quebrou "catego-rias" — linhas
recalibradas); render 3 aprovado.

## Esquema 5 — `esq-l0-tres-origens.tex` (pedido do autor: "um do P2")

**Interpretação de "P2"** (registrada porque o termo não aparece no Cap. 3):
no vocabulário da defesa (`apresentacao/defesa.tex`) e do `principal.tex`,
P1 = sensibilidade do conjunto inicial + envelope do AG e P2 = partida a
frio DRI-SL. Como o ALGORITMO do DRI-SL já tem o `esq-drisl.tex`, o que
faltava é o DESENHO DA AVALIAÇÃO do pilar: três origens para o mesmo
$L_0$-alvo (aleatória com 47 tamanhos × 30 repetições; AG com 4 cenários
em 10 tamanhos; DRI-SL determinístico) medidas pelo MESMO protocolo (PVBin
treinado no $L_0$, Acurácia e Macro F1 no teste), com a nota de
anti-circularidade do envelope (aptidão em partição de aferição disjunta;
reavaliação no teste intocado) e a leitura remetida às quatro seções do
Cap. 4 — sem afirmar resultado. **Onde entra**: Seção `sec:metodo-l0`
(abertura do pilar), casando com o `esq-drisl` da Seção 3.6.

**Loop**: render 1 reprovado (a seta tracejada da anti-circularidade
atravessava a caixa do DRI-SL — o AG desceu para a linha de baixo, vizinho
da sua nota; hifenizações); render 2 reprovado (quebras forçadas largas
demais re-quebraram "DRI-SL" no próprio hífen — linhas recalibradas e
`\mbox{DRI-SL}`); render 3 aprovado.

## Esquema 6 — `esq-ag-envelope.tex` (pedido do autor: Seção 3.5.2)

**O que esclarece**: a Seção 3.5.2 carrega o laço evolutivo inteiro em um
único parágrafo denso. A figura o desdobra: população ($N_{pop}=20$,
indivíduo = $I$ índices únicos) → torneio ($k_t=3$) → cruzamento de um ponto
($p_c=0{,}8$, reparo de unicidade) → mutação ($p_m=0{,}1$, $m_s$ genes) →
aptidão na partição de aferição **disjunta** → elitismo 10% ($N_{elite}=2$)
→ repete; saída após 100 gerações (200 só no $|L_0|=10$) para a
**reavaliação no teste intocado** (o envelope reportado), com a razão da
anti-circularidade em nota tracejada. A figura também carrega a proveniência
da configuração (notebook define; JSON fixa só $|L_0|$; população é o único
valor lido do artefato) — a tripartição honesta que o autor ratificou no
lote A2. Todos os números são os da própria seção. **Onde entra**: fim da
Seção `sec:metodo-l0-ag`, casando com o Apêndice B (`ap:ag`).

**Loop**: render 1 reprovado (a seta curva da nota de proveniência
atravessava o próprio texto da nota — virou seta reta curta; a caixa da
mutação quebrava a matemática no "=" — `\mbox{}`; hifenizações erradas tipo
"ex-ecutou" porque o invólucro não tinha os padrões do português — pacote
`texlive-lang-portuguese` instalado e `babel brazilian` adicionado aos
invólucros, tornando o teste de hifenização realista); render 2 aprovado.

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
