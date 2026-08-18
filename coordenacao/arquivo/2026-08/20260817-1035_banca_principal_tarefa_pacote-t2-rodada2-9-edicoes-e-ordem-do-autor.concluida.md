---
de: banca
para: principal
tipo: tarefa
acao_esperada: (A) aplicar na zona t2 (2.2.2 e 2.2.3) as 9 edições aprovadas pelo autor, antes/depois abaixo, gate em bloco; (B) ORDEM DO AUTOR: dividir tarefas entre os revisores e disparar AGORA a re-revisão de t3, t4 e t5 com a lente da leitura dele (checklist no fim desta mensagem)
referencia: leitura do autor na 2.2.2/2.2.3, aprovação textual ("Todas aprovadas") em 2026-08-17 · cruzada do revisor2 (nuance Shannon, veredito R1-t2) · fichas Santos2016Vies, Rouzegar2024Thesis, Farquhar2021Bias, Kossen2021ActiveTesting conferidas pela banca
criada_em: 2026-08-17T10:35:00Z
---
PARTE A — 9 EDIÇÕES APROVADAS (zona t2, seções 2.2.2-2.2.3). Nenhuma muda
número; as de citação foram verificadas contra ficha pela banca.

1. SHANNON SAI DA ABERTURA E ENTRA NA ENTROPIA (l.392-394 e l.420-423):
   ANTES: "...maximizar a informação obtida por consulta \citep{Settles2012},
   no espírito de \citet{Shannon1948}: buscar ativamente a informação que
   mais reduz a incerteza."
   DEPOIS: "...maximizar a informação obtida por consulta \citep{Settles2012}."
   E na sequência da Eq. eq:entropy:
   ANTES: "seleciona pela \textbf{entropia} da distribuição completa."
   DEPOIS: "seleciona pela \textbf{entropia} da distribuição completa, a
   medida de incerteza de \citet{Shannon1948}."
   (Resolve também a nuance registrada pelo revisor2 na cruzada do R1-t2:
   Shannon não escreveu sobre aprendizado ativo; agora a citação está onde
   é tecnicamente exata.)

2. CORE-SET EM PORTUGUÊS + TYPICLUST NOMEADO (l.463-469):
   ANTES: "A linhagem moderna da família formaliza a seleção por cobertura
   como \textit{core-set}, cuja garantia teórica degrada à medida que cresce
   o número de classes \citep{Sener2018}, e explora a tipicidade com
   agrupamento no TypiClust, que evidencia uma transição de regime: exemplos
   representativos vencem sob orçamento baixo de rótulos, e exemplos
   incertos, sob orçamento alto \citep{Hacohen2022TypiClust}."
   DEPOIS: "Dois desenvolvimentos recentes da família importam aqui.
   \citet{Sener2018} formalizam a seleção como a busca de um conjunto-núcleo
   (\textit{core-set}), o subconjunto que melhor cobre o espaço das
   instâncias; sua garantia teórica, porém, degrada à medida que cresce o
   número de classes. E o algoritmo TypiClust, de
   \citet{Hacohen2022TypiClust}, seleciona exemplos típicos, de alta
   densidade, dentro de agrupamentos; seus experimentos evidenciam uma
   transição de regime: exemplos representativos vencem quando o orçamento
   de rótulos é baixo, e exemplos incertos, quando é alto."

3. FRASE-SÍNTESE DO COLD START GANHA CHAVES (l.507-510):
   ANTES: "As respostas da literatura passam pela exploração da estrutura
   dos dados antes de existir modelo (a família da Eq.~\eqref{eq:id}) e,
   mais recentemente, por seletores externos com conhecimento pré-treinado
   (Seção~\ref{sec:fund-llm})."
   DEPOIS: "As respostas da literatura passam pela exploração da estrutura
   dos dados antes de existir modelo (a família da Eq.~\eqref{eq:id};
   \citealp{Hacohen2022TypiClust}) e, mais recentemente, por seletores
   externos com conhecimento pré-treinado \citep{Bayer2024ActiveLLM}
   (Seção~\ref{sec:fund-llm})."

4. "FRATURA" SEM ANTECEDENTE (l.516-519):
   ANTES: "Quando o oráculo passa a ser um LLM, essa fratura muda de
   natureza (o erro torna-se sistemático e estruturado
   \cite{Song2023NoisyLabels}, e o custo, uma função de tokens) e é tratada
   em profundidade na Seção~\ref{sec:fund-llm}."
   DEPOIS: "Quando o oráculo passa a ser um LLM, a violação da suposição
   muda de natureza: o erro torna-se sistemático e estruturado
   \cite{Song2023NoisyLabels}, e o custo, uma função de tokens; o tratamento
   aprofundado está na Seção~\ref{sec:fund-llm}."

5. "PAGAR RÓTULOS QUE SÓ COMPRAM RUÍDO" (l.527):
   ANTES: "evitam pagar rótulos que só compram ruído."
   DEPOIS: "evitam gastar orçamento em rótulos que já não melhoram o modelo."

6. "NO NOSSO REGIME" (l.449):
   ANTES: "mas também a de custo computacional proibitivo no nosso regime"
   DEPOIS: "mas também a de custo computacional proibitivo no regime desta tese"

7. SIGLA QBC COM GLOSA (l.435):
   ANTES: "a \textbf{consulta por comitê} (QBC)"
   DEPOIS: "a \textbf{consulta por comitê} (QBC, de \textit{query-by-committee})"

8. "MENOS ATRAENTE" (l.440-441):
   ANTES: "torna a família menos atraente quando o classificador é
   re-treinado a cada lote."
   DEPOIS: "torna a família menos adequada quando o classificador é
   re-treinado a cada lote."

9. NOTA: as 2 menções a "E6" na 2.2.3 (l.524 e final do parágrafo do viés)
   ficam como estão — pertencem ao expurgo EXXX fase 2 (revisor1); não
   duplicar o conserto.

PARTE B — ORDEM DO AUTOR (transmitida textualmente à banca): "Avise também
ao principal para que divida as tarefas e peça novamente revisão de t3 a t5
com estes pontos acima para fazerem agora."

Tradução operacional: re-revisão de t3, t4 e t5 do Cap. 2, AGORA, dividida
entre os revisores, com a LENTE DA LEITURA DO AUTOR — que não é a R1 de
travessões nem a R4 de fundamentação, e sim o registro de escrita. Checklist
do que a leitura dele pegou em t1/t2 (usar como critério de varredura):
  a. palavras infladas/elogiosas: "poderoso", "inevitável", "indefensável",
     "precisamente", "atraente";
  b. metáforas coloquiais ou religiosas: "cardápio", "reencarnado",
     "comprar ruído", "fratura" (sem antecedente);
  c. invocação decorativa de autoridade: "no espírito de X" — citar onde o
     conceito é tecnicamente exato, não onde soa bem;
  d. nomes de autores em prosa sem \citet (link perdido no PDF);
  e. frase-síntese de literatura sem chave de citação;
  f. termo estrangeiro sem glosa em português na 1ª ocorrência (core-set) e
     sigla cuja expansão não bate com o nome em português (QBC);
  g. algoritmo citado sem dizer de quem é nem o que faz (TypiClust);
  h. primeira pessoa possessiva ("no nosso regime");
  i. "eventualmente" no sentido de "possivelmente" (anglicismo).
Itens (d), (e) e (g) exigem verificação contra ficha ao corrigir; o restante
é edição de registro pura. Fluxo normal: branch por tema, gate em bloco.

## Resultado (principal, 2026-08-17T14:50Z)
Aplicado e mergeado sob gate do autor. As 14 edições estão na main; a PARTE B (re-revisão t3/t4/t5 com a lente do autor) foi despachada na tarefa 20260817-1420.
