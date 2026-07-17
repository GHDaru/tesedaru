# Revisão por Pares Simulada — Rodada 2 (academic-paper-reviewer v1.9.0, modo re-review)

**Manuscrito**: tese completa — Caps. 1–6, apêndices a1–a6, pré-textuais
(89 páginas, compilação limpa, 0 refs quebradas).
**Insumos**: Roteiro de revisão da R1 (`revisao-pares-simulada-r1.md`) +
manuscrito revisado + artefatos de resultados (`activelearning/experiments/*/results`).
**Data**: 17/07/2026 · **Modo**: re-review (verificação) + varredura de conteúdo
novo (Caps. 4–6). Notas ordinais, sem calibração com gold set.

---

## Matriz de rastreabilidade R&R (Roteiro R1 → manuscrito atual)

| # | Comentário R1 | Alegação do autor | Verificado? | Evidência no manuscrito |
|---|---|---|---|---|
| 1 | Vazamento de T no critério de transição | Corrigido: estagnação em V | **SIM** | 3-metodo §3.8.1 ("Macro F1 no conjunto de *validação* V estagna por p=5") |
| 2 | Wilcoxon com n<6 infalseável | 8 sementes + IC bootstrap | **SIM** | 3-metodo §E3 ("8 sementes — mínimo necessário…2/2^n"); IC percentil 10^4 |
| 3 | Fitness do AG / circularidade | Partição de aferição + reavaliação em teste | **SIM** | 3-metodo (aptidão em partição de aferição disjunta); Cap.4 §4.4 quantifica a inflação: −6,3 p.p. |
| 4 | Precedente ALC (Guyon 2011) | Citado com delta demarcado | **SIM** | 3-metodo §LCE + apêndice a1 (\citep{Guyon2011ALC}, "difere dela em dois…") |
| 5 | Baseline "100% rotulado pelo oráculo" | 5º braço do E3 | **SIM** | 3-metodo §E3 braço (v) oráculo-total, com racional da decomposição ruído × parcimônia |
| 6 | Ablações do FALCO (sem DRI-SL; sem troca) | **Pendente na 1ª verificação** → adicionadas ao desenho do E3 nesta rodada | **SIM (desenho)** | 3-metodo §E3: ablações (a) L0 aleatório e (b) sem troca de oráculo. Execução é dependente de GPU (bloco H) |
| 7 | Constantes não justificadas | Racional para 85%, p=5, ε, b0 | **SIM** | 3-metodo (85% ancorado no teto supervisionado; janela de estagnação justificada) |
| 8 | Ameaças à validade | Nova seção | **SIM** | 3-metodo §"Ameaças à validade" (externa/interna/constructo); ecoada no Cap.6 §Limitações |
| 9 | Literatura de noisy labels | Adicionada no Cap.2 | **SIM** | 2-fundam §desafios (Frénay 2014, Natarajan 2013, Song 2023); usada na leitura do E4 |
| 10 | L_ideal,0 inline; subamostra 50k; pendências Cap.2 | Corrigidos | **SIM** | Eq. LCE com definição inline; §dados (subconjunto estratificado ~50k); figura ActiveLLM em TikZ real; seção esparsa condensada |

### Ataques do Advogado do Diabo (R1)

| Ataque | Alegação do autor | Verificado? |
|---|---|---|
| DA-1: hipótese aritmeticamente inalcançável; intro não conecta gate→hipótese | **Pendente na 1ª verificação** → Cap.1 agora declara a hipótese condicional ao gate e define refutação honesta ("refutada para o cardápio de oráculos avaliado") com ponteiro para a decomposição do 5º braço | **SIM** |
| DA-2: "95% do baseline" esconde o denominador | 5º braço (oráculo-total) separa custo do ruído × custo da parcimônia | **SIM** (desenho; execução no bloco H) |
| DA-3: dataset único do próprio autor | Ameaças à validade + Limitações + réplica STOPS em trabalhos futuros | **SIM** (mitigação declarada, não resolvida — aceitável para tese) |
| DA-4: FALCO como "teste ônibus" sem ablação | Ablações (a)/(b) no desenho do E3 | **SIM** (desenho) |

**Balanço da verificação: 10/10 itens do roteiro + 4/4 ataques endereçados.**
Dois itens (6 e DA-1) estavam pendentes no início desta rodada e foram
corrigidos pelo autor durante ela; re-verificados no texto final. Itens 2, 5,
6 e DA-2 têm o *desenho* completo no manuscrito, mas a *execução* aguarda a
estação GPU (bloco H do checklist) — limitação declarada explicitamente no
Cap. 6.

---

## Varredura do conteúdo novo (Caps. 4–6, apêndices, pré-textuais)

Problemas encontrados nesta rodada (todos corrigidos pelo autor e re-verificados):

1. **[CORRIGIDO] Inconsistência numérica no resumo/abstract**: afirmavam
   259.464 instâncias; o Cap. 3 (auditoria, fonte autoritativa) reporta
   N=250.365. Corrigido para 250.365 em ambos.
2. **[CORRIGIDO] Desenho × execução da ablação de lote (E1b)**: o texto do
   desenho dizia "repete a melhor estratégia", mas a execução usou a entropia
   (estratégia pré-registrada da Fase 2/E4). Texto corrigido para declarar a
   entropia e o racional — evita a aparência de escolha post-hoc.
3. **[CORRIGIDO] Referência quebrada** `sssec:consideracoes_praticas`
   (seção comentada na condensação do Cap. 2) → substituída por citação inline.

Pontos fortes do conteúdo novo (consenso dos revisores):

- **Cap. 4**: a reexecução independente (≤0,7 p.p. em todos os tamanhos) e a
  quantificação da inflação de circularidade (−6,3 p.p.) transformam uma
  fraqueza apontada na R1 em achado metodológico. O DRI-SL vencer o envelope
  do AG *corrigido e o inflacionado* em 100..5000 é o resultado central de P2
  bem sustentado.
- **Cap. 5**: cadeia RQ1→RQ4 com IC de Wilson e McNemar exato; anatomia de
  erros (~48% convenção de catálogo) alimenta diretamente o E0-P; gate
  aplicado como pré-registrado. O E0-P com resultado *negativo na S-strat* é
  reportado com o mesmo destaque do positivo — exatamente o padrão de
  honestidade que a R1 pediu.
- **Cap. 6**: limitações explícitas (P4 parcial, GPU pendente) e hipótese
  central declarada "formalmente aberta" — sem overclaim.
- **Rastreabilidade**: cada tabela nova cita o artefato JSON de origem
  (analysis.json de e0p e e1e4); verificação por amostragem confirmou
  60,4/64,2/65,0%, 51,8/44,8/41,0%, LCE 0,528/0,518/0,493/0,476/0,444,
  retenções 87/74/54% contra os artefatos.

Observações não bloqueantes (para a versão de defesa):

- (i) Latência/vazão dos oráculos como restrição operacional (sugestão R3 da
  R1) segue apenas implícita nos artefatos; uma frase no Cap. 5 bastaria.
- (ii) DOI (Zenodo) para biblioteca + dataset na versão final.
- (iii) Agradecimentos/dedicatória são placeholders do autor (correto não
  inventá-los; preencher antes do depósito).

---

## Decisão editorial (síntese)

| Dimensão (peso) | R1 | R2 |
|---|---|---|
| Originalidade (20%) | 78 | 80 |
| Rigor metodológico (25%) | 68 | **85** |
| Suficiência de evidência (25%) | 70 | **82** |
| Coerência argumentativa (15%) | 80 | 85 |
| Apresentação (15%) | 76 | 84 |
| **Média ponderada** | 73,6 | **83,3** |

### Decisão: **MINOR REVISION (condicional ao bloco H)**

O manuscrito resolveu todos os bloqueantes da R1. O que separa a tese da
versão de defesa não é revisão de texto, e sim a **execução dos experimentos
E2/E3 (+ ablações) na estação GPU** e a inserção dos seus números nos Caps.
5–6 (tarefas H1–H4 do checklist) — exatamente a lacuna que o próprio texto
declara. Recomendações menores: itens (i)–(iii) acima.

Revisão *read-only* sobre o manuscrito verificado; as correções listadas
foram ações do autor dentro da rodada, re-verificadas antes desta síntese.
