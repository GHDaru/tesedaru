---
de: principal
para: revisor2
tipo: tarefa
estado: aberta
assunto: LOOP DE EXCELÊNCIA no Cap.4 (resultados-L0) — instruções completas
prioridade: alta
nao_atrapalhar: FREEZE — capítulo de RESULTADOS: nenhum número/veredito/achado muda; divergência factual REPORTA, não corrige. Sem executar código.
referencia: 4-resultados-l0/texto.tex na main ATUAL (@12194fe+); modelo: o loop do Cap.3 (concluído) e o do revisor1
---

# Objetivo (ordem do autor)

Entrar em **loop de melhoria no Cap.4 inteiro** (`4-resultados-l0/texto.tex`)
até a **excelência acadêmica**, no mesmo modelo que fechou o Cap.3. Você itera:
medir → identificar as piores passagens → melhorar → re-medir → **até você
mesmo julgar excelente**; o principal cruza o julgamento e o autor gateia.

Confirme identidade (ADR 0011). Ritual v1.8: `git fetch origin main
"+refs/heads/mensageria:refs/remotes/origin/mensageria"` e trabalhe sobre a
**main atual** (o Cap.3 alinhado e o Apêndice B da banca já estão nela).

# GOAL (critérios de parada do loop)

(a) **R1–R6 limpos** no capítulo todo (travessões, siglas, fontes, afirmações,
    números×texto — verificação, não alteração —, jargão) + humanizer completo
    (paralelismo negativo, filler, vocabulário-IA, regra de três, gerúndio
    decorativo, negrito mecânico).
(b) **Densidade**: ~20–26 palavras/frase por seção; nenhuma frase >50 palavras
    que não seja enumeração formal legítima.
(c) **Frase-tópico** abrindo cada seção e parágrafo-chave; o leitor sempre sabe
    "o que isso me diz e por que agora".
(d) **Zero caminhos/códigos internos** (docs/scripts/experiments/src/tests,
    D-0xx). Onde precisar ancorar artefato/software, use a **rota
    bibliográfica**: \cite{DaruActiveLearning} (biblioteca atual) e
    \cite{DaruActiveTextClassification} (repositório legado) — as chaves já
    estão no referencias.bib da main.
(e) **Terminologia e refs consistentes** com o Cap.3 alinhado (ex.: "varredura
    de estratégias" etc. só se já for assim na main; não rebatize códigos de
    experimento — isso é a P-10, estacionada).
(f) **Zero travessões novos na prosa** — travessão NÃO é ferramenta de
    reescrita (aparte → vírgula/dois-pontos/parênteses). Travessões de TABELA
    (células vazias, ex.: l.109) ficam.

# Instrumentos (já versionados na main)

Use `scripts/mede-fluidez-prosa.py` e `scripts/mede-freeze-tex.py` (do
revisor1, com os bugs de medição documentados no cabeçalho). Prove o freeze a
cada iteração: números, \label, \ref, \cite, \emph, \textbf idênticos —
exceção declarada apenas para chaves de citação novas da rota bibliográfica.

# Avisos específicos do Cap.4

- O autor está corrigindo conteúdo dos capítulos de resultados: se encontrar
  descompasso factual (número que não bate com tabela, afirmação órfã),
  **REPORTE na entrega** — não corrija.
- A l.117 (tab:drisl-vs-ag) foi corrigida há pouco (36,71/10,86) — não toque.
- A nota do L0=10 (100ª vs 200ª geração) espelha o A2 — preserve a coerência.
- LaTeX: cuidado com menos matemático ($-$), \% escapado e ambientes; sem
  pdflatex no contêiner, declare o que não pôde compilar.

# Entrega e recibos (FORMATO NOVO — recibo curto)

Trabalhe na SUA branch + caixa (§2-ter), por iteração: commit com antes/depois
e nota curta (o que travava, o que melhorou, métricas antes/depois, o que
julgou legítimo e deixou). **Poke ao principal em 1 linha**:
`de:revisor2 para:principal | resumo 1 linha | branch@sha:caminho-da-caixa`
— o detalhe fica na caixa; NÃO repita a instrução no poke. Um tick por
iteração; o principal re-kicka até o goal. NÃO mergeie na main (gate do autor).
