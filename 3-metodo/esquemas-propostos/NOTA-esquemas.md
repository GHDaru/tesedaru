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

## Esquema 7 — `esq-lce.tex` (pedido do autor: Seção 3.4; revisado por ele)

**O que esclarece**: a LCE é uma métrica de ÁREA — a figura desenha a
geometria dela em vez de reexplicá-la em texto: a curva de aprendizado com
os pontos observados marcados (é sobre eles que a regra de Simpson integra),
a $\mathrm{AUC}_{real}$ sombreada, o retângulo
$\mathrm{Perf}_{baseline}\times(L_{final}-L_{ideal,0})$ apontado como
$\mathrm{AUC}_{ideal}$, a fórmula com remissão à Equação 3.1 e ao Apêndice
A, e a leitura ("$\approx 1$ = aproxima-se rápido do teto com poucos
rótulos"). **Cuidado com o princípio V, declarado no próprio desenho**: o
título interno diz "curva ilustrativa, sem dados medidos" — é a definição
da métrica desenhada, não um resultado; citações ficam na prosa/legenda.
**Onde entra**: Seção `sec:metodo-metricas`, ao lado da Equação 3.1.

**Loop**: render 1 reprovado (rótulo do eixo x colidia com $L_{final}$ —
centralizado sob o eixo; o rótulo da AUC_ideal espremido dentro da fatia
clara cruzava a borda e a curva — virou ponteiro tracejado de fora;
"pon-tos" re-quebrado — linhas recalibradas); render 2 + zoom: aprovado.
**Revisão do autor (2026-08-23, aplicada)**: (a) a faixa da análise
estatística saiu da figura (fica só na prosa); (b) a precedência da ALC
saiu da figura (fica só na prosa); (c) o estouro do texto da fórmula na
borda direita da caixa foi corrigido (caixa alargada para 58mm, conferido
por zoom). O arquivo foi renomeado de `esq-lce-e-estatistica.tex` para
`esq-lce.tex` porque a estatística deixou de fazer parte do desenho.

**Inserção ordenada pelo autor (2026-08-23)**: este é o PRIMEIRO esquema da
série promovido de sugestão a texto — o autor mandou inseri-lo no
**Apêndice A** (`a1-lce/texto.tex`): ambiente `figure` com
`\input{3-metodo/esquemas-propostos/esq-lce}`, legenda com a ponte de
notação ($L_{ideal,0}=n_1$, $L_{final}=n_K$), rótulo
`fig:ap-lce-geometria` e uma frase de remissão no fim da Definição. A
remissão interna da caixa de fórmula passou de "(Equação 3.1; Apêndice A)"
para "(Equação A.1)" — apontar para o próprio apêndice seria
autorreferência. O bloco foi test-compilado dentro de `figure` (0 erros).
A edição vive nesta branch; a integração na main é do principal (§2-ter),
avisado por tarefa na caixa. O DoD completo (tese inteira compilando com a
figura) fica com a cruzada/principal — este contêiner não tem a toolchain
completa do ppginf.

## Passe de excelência no Apêndice B (ordem do autor, 2026-08-23)

O autor ordenou um passe completo no Apêndice B (`a2-ag/texto.tex`) — as
rodadas de forma, humanização, fluidez, AUTOCONTENÇÃO ("tire as referências
de coisas da tese se tiver e arquivos"), verificação dos números e a
inserção da figura do laço — em LOOP até a excelência acadêmica (figura +
conteúdo + fluidez + compreensão + rigor).

**Texto** (base: a versão da main, que já continha o lote A2 ratificado):
- Autocontenção: removidos `\ref{sec:res-l0-replay}` e
  `\ref{ch:resultados-l0}` (substituídos por explicação em linha e "nos
  resultados"), o campo de artefato `individual_id 0..19`, o código de
  governança "decisão D-002" e o nome de formato "JSON" ("a configuração
  versionada"). A anti-circularidade agora é EXPLICADA onde aparece, não
  referenciada.
- Humanização/fluidez: a Formulação telegráfica ("Indivíduo: ...
  Aptidão: ...") virou prosa contínua; a repetição de "definido no
  notebook" (4 ocorrências) foi consolidada em um preâmbulo único de
  proveniência que preserva a tripartição do laudo ratificado (notebook
  define; população e gerações conferidas contra artefatos; população sem
  fonte de configuração); título do capítulo com $L_0$ em matemática
  (`\texorpdfstring`); um par de travessões convertido em parênteses (R1).
- Números conferidos contra o canônico da Seção 3.5.2 e o laudo:
  20×100=2.000, 20×200=4.000, k=3, 0,8 (padrão 0,7 sobrescrito), 0,1,
  m_s, 10% (N_elite=2), 18,82%/19,20%, reexecução 30×40, 4 cenários ×
  10 tamanhos (10 a 30.000). Nenhum número novo.
- Figura inserida no fim (fig:ap-ag-laco), com legenda amarrando aptidão →
  aferição → reavaliação no teste intocado.

**ACHADO SISTÊMICO — corpo 12**: as prévias da série foram feitas em corpo
10; ao compilar o apêndice inteiro no corpo REAL da tese (ppginf = book
12pt), o `esq-ag-envelope` quebrou (caixas transbordando, rótulo colidindo
com a caixa final). Foi REDESENHADO para corpo 12 (larguras +25%,
espaçamentos maiores, rótulo de saída realocado; 0 erros, overfull 0,7pt =
imperceptível). O `esq-lce`, JÁ INTEGRADO ao Apêndice A na main, tinha o
mesmo defeito em grau menor (a fórmula transbordava a caixa em ~4mm) —
corrigido nesta branch (caixa 58→64mm; o principal deve integrar).
**Pendência para a cruzada**: os esquemas 1, 2, 4 e 5 (gate-e-régua, mapa
experimental, preproc, l0-três-origens) e o esq-drisl continuam calibrados
em corpo 10 — re-verificar em corpo 12 ANTES de qualquer inserção na tese.
As prévias `preview-esq-ag-envelope.png` e `preview-esq-lce.png` agora são
renders em corpo 12.

## Passe de excelência no Apêndice A (ordem do autor, 2026-08-23)

Extensão do passe do Apêndice B ao `a1-lce/texto.tex` (mesmo goal: figura +
conteúdo + fluidez + compreensão + rigor):
- **Forma/humanização**: título com o estrangeirismo em itálico
  (`\textit{Learning Curve Efficiency}` via `\texorpdfstring`); "MESMO
  classificador" em caixa alta virou ênfase acadêmica (`\emph{mesmo}`); a
  Definição agora ABRE dizendo para que a métrica serve (um escalar para
  comparar e ordenar estratégias) antes do "Seja uma execução...".
- **Compreensão**: as quatro propriedades, antes espremidas num parágrafo
  "(i)...(iv)", viraram lista com nomes (Imagem; Invariância de escala;
  Comparabilidade entre tetos distintos; Dependência do intervalo); a
  invariância ganhou a justificativa de uma linha (numerador e denominador
  escalam pelo mesmo fator).
- **Autocontenção**: o símbolo $T$ (notação do Cap. 3) saiu da Definição
  ("conjunto de teste, fixo ao longo das iterações").
- **Legenda da figura**: repetia a fórmula da AUC_ideal (que já está na
  caixa da figura e na Equação A.1) — virou prosa ("de altura Perf, base
  L_final − L_ideal,0"), removendo a redundância e um overfull de legenda.
- **Medidas reais confirmadas**: o ppginf tem textwidth de 16cm (a4,
  margens 2+2cm + lombada 1cm) — os invólucros de prévia foram ajustados
  de 15cm para 16cm. Com isso, Apêndices A e B compilam com **0 erros e
  0 overfull**. O último overfull (1,89pt) estava DENTRO do nó da fórmula
  do esq-lce (o `\mbox` mede ~64,7mm): caixa alargada para 66mm.
- Sem mudança de conteúdo técnico: equação, propriedades (afirmações),
  relação com a ALC e a frase da implementação de referência intactas.

## Passe de excelência no Apêndice C (ordem do autor, 2026-08-23)

Extensão da série ao `a3-drisl/texto.tex` (DRI-SL), mesmo goal:
- **Forma/fluidez**: a abertura telegráfica ("Construir $L_0$...
  Entradas: ...") virou prosa, com a sigla DRI-SL expandida no próprio
  apêndice (autocontenção + princípio I) e as quatro entradas enumeradas
  em frase corrida.
- **Autocontenção**: removido o `\ref{ch:resultados-l0}` da Intuição
  ("experimentos de composição do conjunto inicial", sem \ref); as Etapas
  e a Intuição já eram autocontidas.
- **Número verificado e tornado mais preciso**: "7,7% de duplicatas
  exatas" conferido contra a Seção 3.2.2 (19.356 linhas = 7,7%) e
  reescrito como "7,7% das linhas repetem descrição e rótulo" (o que a
  fonte de fato mede).
- **Figura**: `esq-drisl.tex` RECALIBRADO PARA CORPO 12 e adaptado ao novo
  lar — notação do apêndice (grupo $c$, cota $q_c$, mínimo 1 por grupo não
  vazio; $U$ em vez de $U_0$), citação na prosa, e a antiga faixa de
  avaliação REMOVIDA (a avaliação pertence ao método — Cap. 3 e
  esq-l0-tres-origens — não ao algoritmo). Inserida como
  `fig:ap-drisl-fases` após as Etapas.
- **Loop visual (3 renders + zoom)**: "es-paço" re-hifenizado (quebra
  forçada recalibrada); o título da Fase (ii) raspava a caixa de cotas
  (descido para junto da linha) e depois a linha cortava os descendentes
  do rótulo (subido 1,5mm — conferido por zoom). Final: 0 erros,
  0 overfull nas medidas reais (corpo 12, textwidth 16cm).

## Passe de excelência no Apêndice D (ordem do autor, 2026-08-23)

Extensão ao `a4-biblioteca/texto.tex` (a biblioteca `activelearning`):
- **Fluidez**: o parágrafo único e denso da Arquitetura (núcleo, adapters e
  casos de uso espremidos) virou lista nomeada de três camadas; título do
  capítulo com `\texttt{activelearning}` (via `\texorpdfstring`).
- **Siglas/estrangeirismos**: MaaS expandido (*Model as a Service*) e SBERT
  expandido (*Sentence-BERT*) na primeira ocorrência; JSONL glosado ("um
  registro JSON por linha").
- **Autocontenção**: os códigos internos de experimento (E0, E0-P, P1/AG,
  E1/E4, E2/E3) saíram da seção de Reprodução — a frase fala em "cada
  experimento" e "identificador de experimento" sem o jargão de controle;
  os caminhos de arquivo já haviam sido removidos pelo principal.
- **Figura NOVA**: `esq-biblioteca-arquitetura.tex` (nascida em corpo 12) —
  a arquitetura hexagonal em 4 camadas: FlowBuilder (borda) → casos de uso
  → domínio (núcleo, cinza escuro) ← adapters (base, 4 caixas), com a nota
  "toda dependência aponta para dentro". Inserida como
  `fig:ap-biblioteca-arq`.
- **Loop (2 renders)**: overfull de 36pt no item dos adapters
  ("OpenAI-compatível/MaaS" inquebrável — reescrito com pontos de quebra);
  na figura, a nota dos adapters era atravessada pelas setas diagonais
  (movida para baixo da fileira) e três hifenizações ("prove-dores",
  "e da-dos", "SQ-Lite") corrigidas com quebras forçadas. Final: 0 erros /
  0 overfull nas medidas reais.
- Conteúdo técnico intacto (arquitetura, diferencial vs small-text,
  reprodução, FlowBuilder dizem o mesmo).

## Passe de excelência no Apêndice E (ordem do autor, 2026-08-23)

Extensão ao `a5-prompts/texto.tex` (prompts e esquemas do oráculo):
- **FREEZE do instrumento**: o texto do prompt v3 (a citação) permaneceu
  intocado palavra por palavra; a única intervenção foi TIPOGRÁFICA
  (`\sloppy` no ambiente quote, com comentário explicando), porque as
  abreviações "X=y" inquebráveis estouravam a linha.
- **Autocontenção**: removidos os códigos internos "medido no E0" (→ "na
  avaliação de oráculos"), "(somente RQ4)" (→ "usada somente para
  quantificar o efeito do instrumento sobre a acurácia medida"),
  "decisão D-004" (→ "para não contaminar a medição") e o título de seção
  "Variantes do E0-P" (→ "Variantes do prompt").
- **Número verificado**: "88--95% de acerto" de cache confere com o
  Cap. 5 (l.106: "atinge 88--95% de acerto nos provedores que o
  suportam").
- **Fluidez**: o parágrafo único dos três modos de instrumentação virou
  lista (enum / json-prompt / free), com o parágrafo do lote separado.
- **Figura NOVA**: `esq-prompt-anatomia.tex` (nascida em corpo 12) — a
  chamada em lote: contêiner tracejado (prefixo estático cacheável +
  itens numerados) → oráculo → resposta como vetor indexado, com a nota
  do cache. Inserida como `fig:ap-prompts-anatomia`.
- **Loop (3 renders)**: estouro no quote (resolvido com \sloppy), figura
  1cm mais larga que o textwidth (coluna direita comprimida),
  `expanded_description` inquebrável pendurado no fim da linha (frase
  reordenada para a quebra cair antes dele), contêiner com vão vertical
  excessivo (apertado). Final: 0 erros / 0 overfull nas medidas reais.

## Passe de excelência no Apêndice F (ordem do autor, 2026-08-23)

Extensão ao `a6-tabelas/texto.tex` (estatísticas completas da
sensibilidade do $L_0$):
- **Verificação EXECUTÁVEL dos 94 valores** (47 tamanhos × 2 métricas):
  script conferiu, linha a linha, mín ≤ P25 ≤ mediana ≤ P75 ≤ máx,
  mín ≤ média ≤ máx, IQR = P75−P25 e CV = DP/mediana. Resultado: ordem,
  média e IQR exatos em 94/94; o CV é consistente com a fonte NÃO
  arredondada (as discrepâncias de 3ª casa são arredondamento composto —
  confirmado por checagem de intervalos). A conferência contra o artefato
  bruto fica para quem tem o repositório de dados.
- **Consistência com a tese**: a tabela usava PONTO decimal (0.067) contra
  a convenção de vírgula do resto da tese — convertidas as 94 linhas
  (846 valores) por script, sem tocar nos dígitos.
- **Limpeza de fonte**: removido o comentário-cicatriz "% DADOS DA TABELA
  AQUI (COPIADOS DO SEU <DADOS>)" (assinatura de máquina no fonte) e o
  vestígio "Base" no cabeçalho de duas linhas (virou cabeçalho de uma
  linha, nas duas ocorrências do longtable).
- **Prosa/autocontenção**: `\ref{sec:res-l0-sens}` e o símbolo $T$
  removidos; a abertura agora define DP, P25/P75, IQR e CV (= DP/mediana,
  conferido pelo script antes de afirmar); caption sem o anglicismo
  "Performance" e com $L_0$ em matemática.
- **Sem figura, por decisão**: a única figura natural seria a curva dos
  próprios dados — gráfico de dados exige pipeline de artefato (princípio
  V); um esquema decorativo não acrescentaria nada a uma tabela.
- 0 erros / 0 overfull nas medidas reais (3 páginas de longtable).

## Passe de excelência no Apêndice G (ordem do autor, 2026-08-23) — SÉRIE COMPLETA

Extensão final ao `a7-parada-drift/texto.tex` (parada, liberação, deriva):
- **Fluidez**: os três gatilhos de parada saíram do parágrafo-monólito
  para lista numerada; o excelente parágrafo do racional estatístico
  (tolerância vs. limite amostral) ficou como estava.
- **Autocontenção**: removidos `\ref{ch:metodo}` (o racional já é
  explicado em linha), o símbolo solto $V$ ("no conjunto de validação"),
  e "medidos no E0" ("na avaliação de oráculos").
- **Siglas** (princípio I): NIM e SGD abertos conforme a lista oficial
  (*NVIDIA Inference Microservice*; *Stochastic Gradient Descent*); PSI
  aberto em linha (*Population Stability Index*) — **PSI NÃO está na
  lista de siglas** (`0-iniciais/acronimos.tex`, superfície do principal):
  pedido de inclusão na entrega.
- **Números reconferidos**: 1/√2000 = 0,0224 ✓; tolerância 22,4× menor
  ("cerca de vinte e duas vezes") ✓; 4.742/15.000 = 31,6% e 6.009/15.000 =
  40,1% → "32–40%" ✓; 991/982/6.009/4.742 = laudo ratificado ✓; meia
  largura de Wilson com n=1.000 ≈ 2,5 p.p. → "2–3 pontos" ✓.
- **Figura NOVA**: `esq-ciclo-vida-modelo.tex` (nascida em corpo 12) — o
  ciclo de vida completo: laço ativo → parada → liberação → produção →
  retreino → volta, com a nota das camadas de deriva. Requer amsmath
  (\text), que a tese já carrega. Achado do loop: os vãos de 1,2–1,4cm
  entre colunas NÃO comportam rótulos de seta em corpo 12 — a semântica
  foi para as caixas e para a nota (2 colisões corrigidas), mais um
  "gati-lhos" re-hifenizado (quebras recalibradas).
- 0 erros / 0 overfull nas medidas reais (3 páginas).

**Balanço da série (7 apêndices, A–G)**: todos com passe de excelência,
todos autocontidos, 6 com figura (F sem, por decisão fundamentada), todas
as figuras calibradas em corpo 12 nas medidas reais do ppginf, tudo
compilando com 0 erros / 0 overfull. Pendências de terceiros: PSI na lista
de siglas (principal); CV do Apêndice F contra o artefato bruto
(revisor1); compilação completa da tese na integração (principal).

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

## Adendo 0143 (2026-08-24) — esq-preproc-espacos-rotulos v3 "explica as classes"

A figura 2 da tarefa 0138 foi refeita por adendo do principal (encomenda do
autor): ela deve EXPLICAR AS CLASSES — o caminho das contagens pelas visões
da base, respondendo "por que 621 num experimento e 714 no outro?" — com
EXCEÇÃO CONTROLADA à regra "zero números": entram somente os números já
impressos no §3.2 (250.221, ≥5, 621, 620, ≥2, 715, 710, 231.490, 714), nada
recomputado; qualquer mudança na prosa deve refletir aqui (checagem de
espelho manual no gate).

- **v3, iteração 1**: duas vias a partir da base corrigida (linhas cruas →
  CategorySchema fechado; filtro brando → deduplicação → visão populacional),
  nota da "pomada massageadora" no vão entre as vias, seta anotada
  "715 − 1 = 714", e nota-resposta didática ao pé. Compilou 0/0, mas o render
  achou: rewraps no meio de palavra na caixa do filtro ≥2 ("li-nhas",
  "tex-tos") e a nota da pomada colidindo com a caixa do CategorySchema.
- **Iterações 2–4**: quebras da caixa ≥2 redistribuídas em 4 linhas curtas
  (paralela à caixa ≥5); hífen manual "popu-lacional" removido (linhas
  naturais); nota da pomada estreitada (28 mm) e movida para o corredor livre
  entre as vias (x≈5,55), seta tracejada até dedup.west sem cruzar nada.
  Render final: nenhuma quebra intra-palavra, nenhuma colisão, rótulo da
  aritmética com folga. 0 erros, 0 overfull (corpo 12, textwidth 16 cm).
  Prévia regenerada (`preview-esq-preproc-espacos-rotulos.png`).
