---
de: banca
para: principal
tipo: entrega
acao_esperada: consolidar o gate do R2+R6 do Cap. 3 (commit 9470c1f, bloco único como você pediu); enfileirar os 4 achados que NÃO toquei (lista no §2, cada um com dono ou decisão pendente); levar ao autor o achado de figuras do §3, que é decisão dele e excede o Cap. 3
referencia: tarefas 20260817-1940 e 20260817-2250 (em-andamento, fecho ambas) · exceção nominal de aplicação vigente · lock de 3-metodo liberado neste commit
criada_em: 2026-08-18T00:35:00Z
---

# 1. Aplicado (commit 9470c1f)

R2 (siglas), varredura do capítulo inteiro contra a lista de acrônimos:
- **AG** era usada em `3-metodo:530` sem nunca ter sido apresentada; passa a
  nascer em `:303` ("um algoritmo genético (AG)");
- **MaaS** aparecia só em itálico, sem expansão em nenhum ponto da tese;
  agora "plataformas de modelo como serviço (\textit{Model-as-a-Service},
  MaaS)";
- **IC** era usada em `:395` e `:486`; a forma longa em `:272` não
  apresentava a sigla. Agora "intervalo de confiança (IC) de Wilson";
- **RS e US** (`:504`) nunca foram expandidas em lugar nenhum: viram
  "seleção aleatória e seleção por incerteza", em português, coerente com a
  decisão AA×AL do autor;
- **SGD**: o capítulo batizava o classificador com o nome do OTIMIZADOR, e a
  lista expande SGD como \textit{Stochastic Gradient Descent}. Não renomeei
  (12 ocorrências no Cap. 5); glosei a origem do apelido em `:223`;
- **GPU** entrou na lista (usada 2x, ausente da lista).

R6 (terminologia em camadas), termo usado antes de existir:
- **E3$'$**: a linha nunca era explicada. A explicação entra na PRIMEIRA
  aparição, logo abaixo da tabela-mapa: variante executada do E3
  pré-registrado, com \ref para a seção que detalha. (Fecha a nota antiga do
  plano que você apontou na tarefa 1940.)
- **"régua"**: usada em `:196`, explicada só em `:476`. Agora a primeira
  ocorrência diz o que é ("a referência de comparação contra a qual os
  braços são medidos") e aponta a seção;
- **"gate"**: jargão usado em `:397` antes de qualquer definição. Agora o
  critério de aprovação é nomeado em `:397` e o apelido \emph{gate} passa a
  ter ponto formal de definição na abertura da
  Seção~\ref{sec:metodo-oraculo-decisao};
- **"Fase 1"** citada em `:332` antes da máquina de fases existir (`:430`):
  ganhou referência cruzada;
- **simbolos.tex** tinha 7 símbolos para um texto que usa mais de 20:
  entram $L$/$L_t$, $T$, $V$, $\theta$, $S$, $O$, $Q_t$, $B$, $b_0$, $I$,
  $N_c$.

Achado de forma, fora de escopo mas indefensável deixar passar: `:241` lia
"A métrica primária é o \textbf{Macro F1-Score} **é** a média aritmética" —
verbo duplicado, frase quebrada. Corrigido.

Códigos de experimento: conferidos, NÃO expurgados, conforme a sua
instrução (as 44 ocorrências em prosa dependem de decisão do autor).

# 2. Achados que NÃO toquei (enfileirar)

1. **Colisão de $\epsilon$**: o texto usa `\epsilon` para a tolerância de
   estagnação (`:441`, `:455`) e `\varepsilon` para o ruído do oráculo
   (`:510`); a lista de símbolos declara $\varepsilon$ como ruído e
   $\varepsilon_{\max}$ como limiar de estagnação. Ou seja: três grafias
   para dois conceitos. NÃO consertei de propósito — a seção do critério de
   parada e o Apêndice A7 vão ser reescritos pela decisão do autor (curva
   completa sem critério de parada, tarefa 1905); consertar agora seria
   trabalho jogado fora e risco de conflito. Amarrar os dois consertos.
2. **"decisão D-005"** (`:390`): a tese cita um identificador de decisão que
   não é explicado em lugar nenhum do texto e não tem apêndice de decisões.
   O leitor não consegue resolver a referência. Decisão editorial: ou
   explica-se a notação, ou substitui-se pela descrição.
3. **RQ1--RQ4**: notação em inglês (\textit{Research Question}) num texto
   que acabou de decidir preferir o português (AA×AL). Não é defeito
   isolado, é coerência de régua, e o revisor1 já inventariou os títulos.
   Decisão do autor.
4. **DRI-SL** é usada no resumo do capítulo (`:8`) e formalizada em `:322`.
   No Cap. 3 as criações NASCEM, então a regra é definição antes do uso;
   aqui a abertura do capítulo antecipa o nome. É defensável (abertura é
   sumário e o Cap. 1 já define), por isso não mexi, mas registro.

# 3. ACHADO PARA O AUTOR: a tese tem duas figuras

Medido no repositório inteiro (`begin{figure}` em todos os `.tex`):

| Capítulo | Figuras | Tabelas |
|---|---|---|
| 1 Introdução | 0 | 0 |
| 2 Fundamentação | 1 | 4 |
| **3 Metodologia** | **0** | 1 |
| 4 Resultados L0 | 1 | 3 |
| **5 Resultados FALCO** | **0** | 8 |
| 6 Conclusão | 0 | 0 |
| 7 apêndices (a1--a7) | **0** | -- |

A tese inteira tem duas figuras. A única figura conceitual é a 2.1, que é o
diagrama do **ActiveLLM**, adaptado de Bayer (2024): está desenhado o
trabalho do concorrente e não está desenhado o FALCO. O Cap. 3 propõe um
framework de três fases com laço, transição por estagnação e progressão de
oráculo, e descreve tudo em prosa. O Cap. 5 reporta oito tabelas e nenhum
gráfico, numa tese cuja métrica central (LCE) é razão de áreas sob curvas
de aprendizado: as curvas nunca são mostradas.

Não é matéria da minha rodada e a decisão é do autor. Levei a ele.
