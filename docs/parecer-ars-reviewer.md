# Parecer — Academic Paper Reviewer (ARS v3.6.5) aplicado à tese FALCO

> Simulação de revisão por pares multi-perspectiva (skill `academic-paper-reviewer`,
> modo **full**): 5 revisores independentes (EIC + Metodologia + Domínio +
> Perspectiva + Advogado do Diabo) + síntese editorial. **Read-only**: este é um
> documento à parte; a tese não foi editada por esta revisão. Objeto: tese de
> doutorado (88 p., PPGMNE/UFPR), commit atual da `main` do `tesedaru`.

---

## Fase 0 — Análise de campo e configuração do painel

| Dimensão | Diagnóstico |
|----------|-------------|
| Disciplina primária | Processamento de Linguagem Natural / Aprendizado de Máquina (classificação de texto) |
| Disciplinas secundárias | Aprendizado ativo; LLMs como anotadores; estatística aplicada |
| Paradigma | Quantitativo — modelagem estatística e experimentação controlada |
| Tipo de método | *Statistical modeling / Machine Learning* + experimentos pareados pré-registrados |
| "Venue" de referência | Tese de doutorado; artigos derivados mirando Q1–Q2 de NLP/AL (TACL, ACL Findings, EMNLP-industry) |
| Maturidade | *Pre-submission* — estrutura completa, compila limpo, prosa polida |

**Painel configurado (personas):**
- **EIC** — editor de revista de NLP aplicado, sensível a reprodutibilidade e a contribuições de método (não de modelo); calibra originalidade e ajuste ao escopo.
- **R1 (Metodologia)** — especialista em desenho experimental e inferência estatística para comparação de classificadores/anotadores; foco em validade, poder e reprodutibilidade.
- **R2 (Domínio)** — pesquisador de aprendizado ativo e cold start para texto; foco em cobertura de literatura, posicionamento e contribuição incremental.
- **R3 (Perspectiva)** — pesquisador de LLM-como-oráculo e MLOps; foco em impacto prático, custo, *serving* e transferência para outros domínios.
- **DA (Advogado do Diabo)** — desafia o argumento central: a hipótese pré-registrada e o veredito de P4.

---

## Fase 1 — Cinco relatórios independentes

### R-EIC — Editor-chefe (tom e ajuste)
**Avaliação global.** Tese madura, de contribuição clara e incomum: não propõe um modelo novo, mas uma **disciplina de medição** para reduzir o custo de rotulagem em texto curto de português com cauda longa (621 classes). Os diferenciais que sustentam a publicação dos derivados: pré-registro do critério, rastreabilidade "nenhum número sem artefato", e a honestidade do veredito de P4 (refutado no orçamento fixado, sustentado a partir de ~50%). O escopo é bem delimitado (Seção de delimitação da contribuição).
- **Força:** originalidade de processo + rigor declarado; três achados de *instrumento* (enum, *serving*, circularidade) que transcendem o dataset.
- **Fraqueza:** um único conjunto de dados (do próprio autor) limita a generalização externa das afirmações — precisa estar explícito no *abstract* como ameaça, não só no Cap. 6.
- **Recomendação:** Minor Revision.

### R1 — Metodologia / Estatística
Escores (rubrica 0–100):

| Dimensão | Escore | Justificativa (com localização) |
|----------|:---:|-------------|
| Originalidade | 82 | DRI-SL (cold start sem rótulos) + LCE + auditoria de circularidade (Cap. 4). |
| **Rigor metodológico** | **85** | Critérios pré-registrados, IC de Wilson em toda proporção, McNemar exato, Wilcoxon com n=8 (p mínimo 0,0078), *bootstrap*; deduplicação **antes** do particionamento; auditoria de gabarito. |
| Evidência | 83 | Programa amplo (E0/E0-P/E1/E4/E5/E6/E3′ + replays P1/P2) com artefatos versionados. |
| Coerência | 84 | Encadeamento problema→lacuna→método→resultado sólido. |
| Escrita | 85 | Prosa técnica precisa; compila 0 erros/0 refs indefinidas. |

- **MAJOR — semente única em braços decisivos.** O E3′ (veredito da hipótese) roda em **semente única**, 3 épocas, contexto de 32 *tokens*, e várias células do E6 também. O texto declara isso e trata os números como descritivos, mas a comparação que sustenta a manchete (E35 supera a supervisão completa) merece ≥3 sementes ou um IC por reamostragem. Localização: Cap. 5, `sec:res-e3p` e `sec:res-e6`.
- **MINOR — teto absoluto do BERTimbau.** A configuração econômica do classificador forte (3 épocas/32 *tokens*) pode subestimar seu teto; o texto argumenta que isso tornaria o critério *mais* exigente (a favor da conclusão), o que é aceitável, mas convém quantificar a sensibilidade a épocas em ao menos um ponto.
- **Recomendação:** Minor→Major Revision (condicionada ao ponto das sementes).

### R2 — Domínio (aprendizado ativo / cold start)
- **Força:** posicionamento preciso na literatura — a tabela de lacunas (Cap. 2) e a comparação com DEUCE, ActiveLLM, surveys de AL+LLM; granularidade de 621 classes muito acima da usual (dezenas a ~370) em LLM-como-anotador.
- **Literature Integration (opcional): 84** — cobertura boa de seminais + recentes (2024–2026). Sugestão: garantir que os trabalhos 2026 de *mixture/roteamento de oráculos* (Qi, Rouzegar) apareçam também na discussão de trabalhos futuros, não só na fundamentação.
- **MINOR — DRI-SL vs. estado da arte de cold-start informado.** A comparação principal é contra AG supervisionado e aleatório; um revisor de domínio pediria uma linha de base adicional de cold start moderno (ex.: ALPS/coreset) ao menos discutida, para reforçar o "supera o envelope".
- **Recomendação:** Minor Revision.

### R3 — Perspectiva (LLM-como-oráculo / prática)
- **Significance & Impact (opcional): 85** — problema real (custo de rotulagem), solução transferível, ciclo real rodado a custo zero de oráculo; a interface (FlowBuilder) e a biblioteca pip tornam o protocolo reutilizável.
- **Força:** os achados de *instrumento* (contrato de saída = 6,8% de falsos erros; o mesmo modelo diverge de si entre provedores, p<0,001; spread de custo 26× em empate estatístico) são de alto valor prático e generalizam para além do dataset.
- **MINOR — custos datados.** Preços de API (jul/2026) datam; o texto mitiga usando *razões* (26×), o que é correto — apenas reforce essa moldura no *abstract*.
- **Recomendação:** Minor Revision.

### DA — Advogado do Diabo (desafio ao argumento central)
**Contra-argumento mais forte (≈250 palavras).** A hipótese quantitativa central — atingir ≥95% do Macro F1 da supervisão completa com ≤30% dos rótulos via oráculo LLM — foi **refutada no orçamento exatamente pré-registrado (30%)**. Uma banca cética pode enquadrar assim: "a tese pré-registrou um alvo, o alvo não foi atingido, e a conclusão foi então reformulada para um orçamento maior (~50%) onde ele passa a valer." Se o pré-registro é o padrão-ouro que a própria tese invoca, mudar o orçamento *após* observar a falha é precisamente o risco que o pré-registro deveria conter. O contra-argumento é reforçado pelo fato de o braço decisivo (E3′) ser de semente única e configuração econômica: a "sustentação a partir de 50%" repousa sobre uma varredura sem repetição.

**Por que NÃO é CRITICAL (é MAJOR).** A tese não esconde nem maquia: declara a refutação em 30% no resumo, no Cap. 5 e na conclusão (após a correção de consistência), e trata a varredura como *achado medido*, não como hipótese original. A decomposição pareada (ruído/seleção/orçamento) identifica a causa (critério de parada), o que converte um "fracasso" em contribuição diagnóstica. E os pilares P1, P2 e P3 sustentam-se de forma **independente** de P4. Logo, o argumento central da tese (reduzir custo de rotulagem com disciplina de medição) sobrevive.

**Itens (severidade · dimensão · local):**
- **MAJOR · pré-registro · Cap. 5/6** — o "piso de 50%" precisa ser apresentado explicitamente como *achado post-hoc* medido, jamais como o critério original; hoje o texto já faz isso, mas a fronteira deve ser inequívoca na primeira menção.
- **MAJOR · robustez · Cap. 5** — repetir o E3′ decisivo em ≥3 sementes, ou declarar como limitação de primeira ordem no *abstract*.
- **MINOR · alternativa ignorada** — a hipótese poderia ter sido *reformulada como faixa* no pré-registro; discutir por que 30% foi escolhido a priori.

**Teste "So what?":** passa — mesmo com P4 refutado no alvo, os achados de instrumento e o DRI-SL entregam valor independente.

---

## Fase 2 — Síntese editorial e decisão

### Consenso (5/5)
- Rigor estatístico e rastreabilidade de artefatos são pontos fortes reais e acima da média da área.
- A honestidade do veredito de P4 é uma virtude, não um defeito.
- Um único dataset (do autor) é a limitação de primeira ordem.

### Divergência
- **R1 e DA** puxam para **Major** por causa da semente única nos braços decisivos; **EIC, R2, R3** ficam em **Minor**. Arbitragem: como a fragilidade é de *robustez* (não de desenho) e está declarada, a decisão fica em **Minor Revision com uma condição forte** (o item das sementes).

### Escore ponderado
`0,20·82 + 0,25·85 + 0,25·83 + 0,15·84 + 0,15·85 = ` **83,6 / 100** → faixa **Accept / Minor Revision**.
Opcionais: Literature Integration 84 · Significance & Impact 85.

### ⚖️ Decisão editorial: **MINOR REVISION** (aprovação com revisões menores)
O Advogado do Diabo levantou pontos **MAJOR**, mas **nenhum CRITICAL** (Regra de Ferro #4 satisfeita): o argumento central sobrevive à refutação de P4, que é tratada com transparência. A decisão não é *Accept* puro por causa da condição de robustez.

### Roadmap de revisão (priorizado)
1. **[ALTA · robustez]** Repetir o E3′ decisivo (pelo menos o braço E35 vs. supervisão completa) em ≥3 sementes, **ou** elevar a semente única a limitação de primeira ordem no *abstract* e na conclusão. *(endereça R1 + DA MAJOR)*
2. **[ALTA · pré-registro]** Na **primeira** menção do piso de ~50% (Cap. 5 e resumo), marcá-lo inequivocamente como *achado post-hoc medido pela varredura*, distinto do critério pré-registrado de 30%. *(endereça DA MAJOR)*
3. **[MÉDIA · generalização]** Mover a ameaça "dataset único do autor" para o *abstract*/resumo, não só o Cap. 6. *(EIC)*
4. **[MÉDIA · literatura]** Discutir uma linha de base moderna de cold-start informado (ALPS/coreset) e o roteamento/mixture de oráculos também nos trabalhos futuros. *(R2, R3)*
5. **[BAIXA · custo]** Reforçar no *abstract* que a análise de custo repousa em *razões* (26×), não em valores datados. *(R3)*

> Observação (não-defeito): a inconsistência de veredito entre *abstract*/resumo e corpo, e o furo de fundamentação do SGD, **já foram corrigidos** nas rodadas de checklist anteriores — este parecer reflete o estado atual da `main`.
