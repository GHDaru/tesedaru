---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
assunto: LOOP DE EXCELÊNCIA no Cap.5 (resultados-FALCO) — mesmo padrão do Cap.3
prioridade: alta
nao_atrapalhar: FREEZE — capítulo de RESULTADOS: nenhum número/veredito/achado muda; divergência factual REPORTA, não corrige. Sem executar código.
referencia: 5-resultados-falco/texto.tex na main ATUAL (@12194fe+); modelo: o loop que fechou o Cap.3 (seu humanizer+auto-contenção alinhados na main)
---

# Objetivo (ordem do autor)

Entrar em **loop de melhoria no Cap.5 inteiro** até a **excelência acadêmica**,
no MESMO padrão do Cap.3: medir → piorar-passagens → melhorar → re-medir →
até você julgar excelente; o principal cruza e o autor gateia.

Confirme identidade (ADR 0011). Ritual v1.8: `git fetch origin main
"+refs/heads/mensageria:refs/remotes/origin/mensageria"`; trabalhe sobre a
main ATUAL (seu delta do Cap.3 já foi alinhado e comitado @12194fe — parta dela,
não do seu fork antigo).

# GOAL (critérios de parada)

(a) R1–R6 limpos + humanizer completo. (b) Densidade ~20–26 p/f; frase >50 só
enumeração legítima. (c) Frase-tópico em seção/parágrafo-chave. (d) Zero
caminhos/códigos internos; ancoragem de artefato/software pela rota
bibliográfica: \cite{DaruActiveLearning} / \cite{DaruActiveTextClassification}
(chaves já no bib). (e) Terminologia/refs consistentes com Cap.3 alinhado.
(f) Zero travessões novos na prosa (aparte → vírgula/dois-pontos/parênteses);
travessões de TABELA ficam.

# Instrumentos

`scripts/mede-fluidez-prosa.py` e `scripts/mede-freeze-tex.py` (seus, agora na
main). Prove o freeze a cada iteração (números, \label, \ref, \cite, \emph,
\textbf idênticos; exceção declarada só para chaves de citação novas).

# Avisos ESPECÍFICOS do Cap.5 (críticos)

- **P-01 CONGELADA**: a seção do gate cita "p<0,001" que um achado (não
  cruzado) contesta. NÃO toque nos números do gate nem "conserte" o p-valor —
  é pendência da matriz, decisão do autor. Reescrever FORMA da seção pode,
  números não.
- **tab:e3p / tab:e6**: legendas recém-gateadas (braço E = 2 sementes 0,822/
  0,351; receita `_bs16v2`; denominadores mistos declarados). `_bs16v2` é
  identificador científico de regime — fica. Não reagregue nada.
- Títulos RQ1–RQ4 já estão "RQ1: assertividade" (R1 gateado) — mantenha o padrão.
- O autor está corrigindo conteúdo dos capítulos de resultados: descompasso
  factual REPORTA, não corrige.
- Cuidado com $-$ (menos matemático), \% escapado, ambientes; declare o que não
  compilou.

# Entrega e recibos (FORMATO CURTO)

SUA branch + caixa (§2-ter) por iteração, com antes/depois + métricas. Poke ao
principal em 1 linha: `de:revisor1 para:principal | resumo 1 linha |
branch@sha:caminho-da-caixa`. Um tick por iteração; o principal re-kicka até o
goal. NÃO mergeie na main (gate do autor).
