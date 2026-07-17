# Revisão por Pares Simulada — Rodada 1 (academic-paper-reviewer v1.9.0)

**Manuscrito**: "Aprendizado Ativo com Modelos de Linguagem para Textos Curtos em
Português" — Capítulos 1 (Introdução), 2 (Fundamentação) e 3 (Metodologia).
**Estado do manuscrito**: PARCIAL — capítulos de resultados (4–5) e conclusão (6)
ainda não escritos; a revisão avalia o que existe e a *avaliabilidade* do que está
prometido.
**Data**: 17/07/2026 · **Modo**: full · Escores de rubrica são ordinais
(comparáveis entre rodadas), não garantia de aceitação em veículo real.

---

## Fase 0 — Configuração da banca (field_analyst)

| Papel | Persona configurada | Foco |
|---|---|---|
| EIC | Editor de periódico de PLN aplicado (ex.: *LREV/Information Processing & Management*) | Adequação, originalidade, significância |
| R1 Metodologia | Especialista em avaliação experimental de AL e estatística aplicada | Desenho, validade, reprodutibilidade |
| R2 Domínio | Pesquisador de AL para PLN (linha Settles→Zhang et al. 2022) | Cobertura da literatura, contribuição incremental |
| R3 Perspectiva | Engenheiro de ML industrial (MLOps/FinOps de anotação) | Impacto prático, custo, transferibilidade |
| Advogado do Diabo | Cético de "LLM resolve tudo" com formação em aprendizado com ruído | Ataque ao argumento central |

Classificação: pesquisa quantitativa experimental; PLN aplicado; maturidade =
proposta metodológica com infraestrutura pronta e resultados parciais (piloto).

---

## Parecer 1 — Editor-Chefe

**Pontos fortes.** Posicionamento da contribuição exemplar: a Seção 1.5 delimita
explicitamente que a originalidade está no *processo de rotulagem*, não no modelo —
isso desarma a objeção mais comum a teses aplicadas de PLN. Hipótese falseável com
critério quantitativo (≤30% dos rótulos → ≥95% do Macro-F1 de supervisão completa,
com significância vs RS/US) é raro e louvável. A continuidade dissertação→tese
(Daru 2022/2024 → FALCO) constrói narrativa de programa de pesquisa.

**Preocupações.** (i) **Tese de dataset único**, e criado pelo próprio autor: a
generalização das conclusões além do *Retail Product Description-Ptbr* não é
discutida — ao menos uma seção de ameaças à validade externa é necessária. (ii) A
significância para além do caso (varejo/PT-BR) precisa ser argumentada na
introdução: o que o leitor de AL geral aprende com o FALCO? (iii) Manuscrito
incompleto: a decisão editorial final dependerá inteiramente de E0–E3 entregarem o
que o Cap. 3 promete.

**Nota EIC (originalidade/significância)**: 78/100.

---

## Parecer 2 — R1 Metodologia (o mais crítico)

**Pontos fortes.** Programa E0–E4 com desenho fatorial, amostras pareadas,
IC de Wilson + McNemar (com binomial exato para <25 discordâncias) — acima do
padrão da área, que raramente reporta IC de acurácia de oráculo. Instrumentação de
3 modos (enum/json-prompt/free) com RQ4 dedicado ao efeito do instrumento é uma
contribuição metodológica em si. Auditoria do gold com teto de 99,3% explicitado.
Reprodutibilidade (config versionada, sementes, JSONL retomável) exemplar.

**Problemas que EXIGEM correção:**

1. **[GRAVE] Vazamento do conjunto de teste no critério de transição de fase.**
   A Fase 2 do FALCO transiciona "quando o Macro F1 em $T$ estagna por $p=5$
   iterações" (Seção 3.8.1). Usar $T$ — reservado "exclusivamente à avaliação
   final" (Seção 3.3.4) — para decidir a política DURANTE o processo contamina a
   avaliação: o procedimento passa a otimizar contra o teste. **Correção
   obrigatória**: o critério de estagnação deve usar $V$ (validação), nunca $T$.
   Uma linha de correção, mas indispensável à validade.

2. **[GRAVE] Wilcoxon com 3–5 sementes não pode atingir significância.** Com $n$
   pares, o menor p-valor bicaudal do teste de postos sinalizados é $2/2^n$: para
   $n=5$, p mínimo $= 0{,}0625 > 0{,}05$; para $n=3$, $0{,}25$. Tal como escrito
   ("3 a 5 sementes; Wilcoxon pareado"), o E3 é estatisticamente incapaz de
   rejeitar $H_0$ — a hipótese central fica infalseável pelo próprio desenho.
   **Correções possíveis**: (a) ≥6 sementes (mínimo aritmético) e idealmente ≥8;
   (b) trocar por teste que agregue por iteração; (c) reformular a inferência
   (IC bootstrap sobre diferença de LCE). Recomendo (a)+(c).

3. **[MODERADO] Fitness do AG e circularidade do envelope (P1).** Se o algoritmo
   genético otimiza a composição de $L_0$ usando desempenho medido no MESMO
   conjunto em que o envelope é reportado, o "limite empírico" está superajustado
   ao conjunto de avaliação. O texto não especifica o conjunto usado como fitness.
   **Correção**: declarar explicitamente; se fitness = teste, reavaliar os
   indivíduos finais em partição intocada e reportar o envelope nela.

4. **[MODERADO] Constantes não justificadas**: $b_0 = 1\%B$, estagnação com
   $p=5$ e $\epsilon=10^{-3}$, limiar de acurácia de 85% no gate do oráculo.
   Nenhuma precisa ser ótima, mas cada uma precisa de uma frase de justificativa
   ou análise de sensibilidade (ao menos para o 85%, que decide a arquitetura do
   framework).

5. **[MENOR] LCE**: $L_{\mathrm{ideal},0}$ aparece na Eq. (3.1) sem definição no
   corpo (só no apêndice). Definir inline.

6. **[MENOR] Subamostra de ~50k no E3**: declarar o procedimento de amostragem
   (estratificada? semente?) e discutir o que se perde vs o pool completo.

**Nota R1 (rigor metodológico)**: 68/100 *(subiria para ~85 com as correções 1–3,
que são baratas)*.

---

## Parecer 3 — R2 Domínio

**Pontos fortes.** Cobertura da literatura excepcional em extensão (a cadeia
Angluin→Cohn→Lewis→Settles→Ren→Zhang 2022 está completa; a frente AL+LLM cobre
Gilardi, Bayer/ActiveLLM, Rouzegar, Zhang 2025, e a atualização 2025–2026 com
mixture-of-LLMs e barreiras práticas). A seção de ML condensada com citações-síntese
é o formato certo. A tabela de lacunas (AL × STC × LLM × PT) fecha o posicionamento.

**Correções e ausências:**

1. **[MODERADO] Precedente da LCE.** A tese apresenta a LCE como métrica "proposta
   nesta tese". Métricas de área sob a curva de aprendizado normalizada têm
   precedente direto — notadamente a **ALC (Area under the Learning Curve)** do
   Active Learning Challenge (Guyon et al., 2011). A LCE difere (normalização pelo
   baseline de supervisão completa e integração por Simpson), mas o texto precisa
   citar o precedente e demarcar o delta, sob pena de um revisor real apontar a
   omissão como falha de escolaridade.
2. **[MODERADO] Falta a literatura de aprendizado com rótulos ruidosos** para
   sustentar o E4 (ex.: survey de *learning with noisy labels*). Se o gate falhar
   (piloto sugere que falhará), essa literatura vira central — antecipe-a no Cap. 2.
3. **[MENOR] Pendências assumidas no próprio Cap. 2** (nota de cabeçalho):
   redundância STC vs dissertação e figura do ActiveLLM comentada — resolver antes
   da defesa.
4. **[MENOR] Poda de citações herdadas**: o lote de reviews periféricos
   (identificados nos fichamentos como "candidatos a poda") deve ser reduzido —
   citações fracas diluem as fortes.

**Nota R2 (suficiência de evidência bibliográfica)**: 80/100.

---

## Parecer 4 — R3 Perspectiva (impacto prático)

**Pontos fortes.** A contabilidade de custo em US$/1k rótulos com cache e lote é a
parte mais transferível da tese — nenhum trabalho citado instrumenta custo nesse
nível. O FlowBuilder + biblioteca hexagonal tornam o trabalho *usável*, não só
publicável. RQ4 (efeito do instrumento) tem relevância além da academia: equipes
industriais medem oráculos LLM com instrumentos defeituosos rotineiramente.

**Sugestões (não bloqueantes):** (i) reportar também latência/vazão como restrição
operacional (rate limits moldaram o próprio desenho — 3 rpm no MaaS — e isso é um
achado prático digno de seção); (ii) considerar DOI (Zenodo) para a biblioteca e o
dataset na versão final; (iii) o enquadramento do RQ4 ganharia força com uma frase
de teoria de medição (validade de instrumento).

**Nota R3 (impacto/aplicabilidade)**: 82/100.

---

## Parecer 5 — Advogado do Diabo

**Ataque 1 — A hipótese pode ser aritmeticamente inalcançável com o oráculo
disponível.** O piloto do E0 indica melhor acurácia de oráculo ~84% (v4-pro,
S-strat) e nenhum modelo ≥85% na S-rand. Treinar com 30% de rótulos dos quais
~16–22% estão errados e atingir 95% do Macro-F1 de supervisão LIMPA completa é uma
alegação forte: o ruído de rótulo impõe teto ao classificador (literatura de noisy
labels). Se E4 mostrar que ε≈0,2 degrada além de 5%, a hipótese central é refutada
*pela escolha do oráculo*, não pelo framework. **Exigência**: ou (a) a hipótese
declara explicitamente que vale sob o melhor oráculo aprovado no gate, ou (b) o
texto define de antemão o que conta como refutação honesta vs recalibração — o
critério de decisão existe (Seção 3.7.3), mas a introdução não conecta o fracasso
do gate ao destino da hipótese.

**Ataque 2 — "95% do baseline" esconde o denominador.** O baseline de supervisão
completa herda o teto de 99,3% do gold E treina com rótulos limpos. A comparação
justa seria também reportar o baseline treinado com rótulos do MESMO oráculo em
100% do pool — separando "custo do AL" de "custo do ruído". Sem isso, um resultado
negativo é ambíguo entre estratégia ruim e oráculo ruim.

**Ataque 3 — Generalização de dataset único do próprio autor.** Todo o edifício
empírico repousa numa base construída pelo autor. Não há réplica em segunda base
(ex.: STOPS/NICE de Karl 2023, mesmo em inglês, como sanity check barato). Uma
tese pode viver com isso — mas precisa confessá-lo em limitações com mais ênfase.

**Ataque 4 — O FALCO tem muitas peças móveis para o orçamento de evidência.**
DRI-SL + fases + troca de oráculo + transição por estagnação: no E3 com poucas
sementes, será impossível atribuir ganho a cada peça. Sem ablação (FALCO sem
DRI-SL; FALCO sem troca de oráculo), o claim "o framework integrado funciona" é
um teste ônibus. **Exigência**: ao menos uma ablação de cada componente principal,
ou rebaixar o claim.

**Nota DA (robustez do argumento)**: 65/100.

---

## Síntese Editorial (Fase 2)

**Consensos**: infraestrutura metodológica e reprodutibilidade acima do padrão;
posicionamento honesto; instrumentação do oráculo é contribuição própria;
literatura abrangente. **Divergências**: R3 aceita as constantes de projeto como
engenharia; R1 exige justificativa; DA considera a hipótese em risco aritmético —
R1 responde que o desenho já prevê E4 e o gate.

### Decisão: **MAJOR REVISION** (esperada para manuscrito parcial)

| Dimensão (peso) | Nota |
|---|---|
| Originalidade (20%) | 78 |
| Rigor metodológico (25%) | 68 |
| Suficiência de evidência (25%) | 70* |
| Coerência argumentativa (15%) | 80 |
| Apresentação (15%) | 76 |
| **Média ponderada** | **73,6** → Minor/Major na fronteira; *Major* pela ausência dos capítulos de resultados |

\* Evidência bibliográfica forte (80), evidência empírica ainda parcial (piloto).

### Roteiro de revisão (ordem de prioridade)

| # | Ação | Esforço | Bloqueante p/ defesa? |
|---|---|---|---|
| 1 | Trocar $T$ por $V$ no critério de transição de fase (Seção 3.8.1) | 1 linha + ajuste no código | SIM |
| 2 | Sementes ≥6 (ideal 8) no E3 OU reformular inferência; corrigir texto da Seção 3.4 | médio (custo GPU) | SIM |
| 3 | Declarar fitness do AG e sanear circularidade do envelope (P1) | baixo | SIM |
| 4 | Citar ALC (Guyon 2011) e demarcar o delta da LCE | baixo | SIM |
| 5 | Adicionar baseline "100% rotulado pelo oráculo" no E3 (ataque 2 do DA) | médio | recomendado |
| 6 | Ablações do FALCO (sem DRI-SL; sem troca de oráculo) | médio | recomendado |
| 7 | Justificar constantes (85%, p=5, ε, b₀) com 1 frase/análise cada | baixo | recomendado |
| 8 | Seção de ameaças à validade (dataset único, autor como criador da base) | baixo | SIM |
| 9 | Literatura de noisy labels no Cap. 2 (antecipa E4) | baixo | recomendado |
| 10 | Definir $L_{\mathrm{ideal},0}$ inline; procedimento da subamostra 50k; pendências do Cap. 2 | baixo | não |

**Observação de calibração** (exigida pela skill): estas notas não passaram por
modo de calibração com gold set; trate-as como ordinais. A revisão é *read-only* —
nenhuma alteração foi feita nos capítulos.
