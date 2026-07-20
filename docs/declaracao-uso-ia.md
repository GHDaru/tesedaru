# Declaração de autoria e de uso de ferramentas de IA

> Rascunho para revisão e assinatura do autor. A divisão abaixo foi
> reconstruída do histórico real do trabalho; **ajuste qualquer item que não
> reflita a realidade antes de incorporar à tese.** Versão .tex pronta para o
> pré-textual em `0-iniciais/declaracao-ia.tex`.

## Por que declarar

O uso de assistentes de IA em pesquisa deve ser transparente. Esta declaração
separa, com honestidade, **o que foi concebido e decidido pelo autor** (que
retém integralmente a responsabilidade intelectual e científica pelo trabalho)
do que foi **produzido com auxílio de uma ferramenta de IA sob direção do
autor**. Nenhum resultado numérico foi inventado por IA: a constituição do
projeto exige *nenhum número sem artefato rastreável*, e todos os artefatos
estão versionados e são reexecutáveis.

## O que é do autor (concepção, decisão e responsabilidade)

- **A pergunta de pesquisa, a hipótese e o framework FALCO** — concepção original.
- **O algoritmo DRI-SL** e o **desenho do experimento E6** (viés de
  autoavaliação com oráculo perfeito) — concebidos pelo autor.
- **O conjunto de dados** (≈250 mil descrições, 621 categorias): coletado,
  rotulado e publicado pelo autor (Kaggle, DOI 10.34740/kaggle/dsv/4265348,
  2022), muito antes desta colaboração.
- **Os experimentos originais dos pilares P1 e P2** (sensibilidade de $L_0$,
  envelope do algoritmo genético, DRI-SL) e o **piloto de oráculo** — executados
  pelo autor no repositório \texttt{activetextclassification}.
- **Todas as decisões metodológicas e de escopo**: critérios pré-registrados,
  calibração de orçamento (15 mil rótulos), aprovação da campanha de sementes,
  desenho do E3$'$ enxuto, escolha de classificadores e métricas.
- **A expertise de domínio** (varejo, cupom fiscal, convenções do catálogo) e
  a **infraestrutura** (chaves de API, estação com GPU).
- **A revisão crítica e a aprovação de cada etapa** — inclusive a rejeição e o
  redirecionamento de sugestões da ferramenta.

## O que foi feito com auxílio de IA (sob direção e revisão do autor)

Ferramenta utilizada: assistente de IA baseado em modelo de linguagem de grande
porte (Claude, Anthropic), operando em ambiente de execução com acesso ao
código e aos dados, sob instrução e supervisão contínuas do autor.

- **Refatoração do código experimental** para a biblioteca
  \texttt{activelearning} (arquitetura DDD/hexagonal), a partir do programa
  original do autor.
- **Implementação e execução dos experimentos novos** — E0, E0-P, E4, E5
  (ciclo real), E6 (incluindo a campanha de 8 sementes) e E3$'$ (varredura de
  orçamento) — com os desenhos, parâmetros e critérios definidos pelo autor.
- **Instrumentação estatística** (intervalo de Wilson, McNemar, Wilcoxon,
  \textit{bootstrap}) e as rotinas de análise e figuras.
- **Redação e reestruturação** de capítulos e do texto, sob direção do autor,
  com revisão e aprovação deste.
- **Verificação e auditoria**: conferência dos números portados do repositório
  legado contra os artefatos originais; pareceres simulados de revisão.
- **Software de apoio**: a interface FlowBuilder e o catálogo executável de
  experimentos; os \textit{drafts} dos artigos derivados; buscas e fichamentos
  de literatura.

## Garantias

O autor leu, verificou e assume a responsabilidade por todo o conteúdo da tese.
O texto gerado com auxílio de IA foi revisado quanto a correção, adequação e
originalidade. As afirmações empíricas remetem a artefatos versionados e
reexecutáveis (repositórios \texttt{activelearning} e
\texttt{activetextclassification}; interface de reprodução/reprise).

---

*Curitiba, 2026. Gilsiley Henrique Darú.*
