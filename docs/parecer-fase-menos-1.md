# Parecer Crítico — Fase −1
## Avaliação da tese como orientador e banca simulada, com plano de reescrita capítulo a capítulo

**Objeto:** `GHDaru/Tese-Vers-o-Draft` (texto) + `GHDaru/activetextclassification` (código/experimentos)
**Destino:** `GHDaru/tesedaru` (texto, template PPGINF/Maziero) + `GHDaru/activelearning` (código, DDD+Hexagonal)
**Data:** julho/2026

---

## 1. Sumário executivo

A tese tem **quatro contribuições com dados reais e defensáveis hoje** e **uma contribuição central anunciada mas não implementada**. O texto atual promete um framework (FALCO com BERTimbau e oráculo LLM progressivo GPT-4o mini→GPT-4o) que não existe em código; o que existe de verdade é: (a) um estudo de sensibilidade do L0 grande e bem executado; (b) uma otimização de composição de L0 via AG completa; (c) um algoritmo de cold start (DRI-SL) implementado e com logs reais; (d) uma avaliação multi-modelo do oráculo LLM com defeito de instrumentação conhecido e corrigível; e (e) a métrica LCE formalizada.

**Veredito como banca:** no estado atual, a tese seria **reprovada ou devolvida para correções maiores**, por dois motivos fatais: resultados centrais marcados como `[Suposição:]` e um capítulo de metodologia que descreve um sistema diferente do que foi executado. **Veredito como orientador:** o material real existente cobre ~70% de uma tese defensável; o caminho mínimo exige (i) uma execução real, mesmo que em escala reduzida, do FALCO com BERTimbau; (ii) a repetição da avaliação do oráculo com instrumentação corrigida; e (iii) uma reescrita que alinhe as promessas do texto ao que foi de fato feito — cortando o que não foi.

---

## 2. Inventário: o que é real vs. o que é promessa

| # | Item | Estado no código | Estado no texto | Aproveitável? |
|---|------|------------------|------------------|----------------|
| 1 | Sensibilidade do L0 (47 tamanhos × 30 repetições, PVBin) | ✅ Completo, logs reais | ✅ Cap. 4 escrito com números reais | **Sim, quase pronto** |
| 2 | Otimização de L0 via AG (10 tamanhos × 4 cenários × 100 gerações) | ✅ Completo, logs + figuras | ✅ Cap. 4 escrito (longo demais) | **Sim, condensar** |
| 3 | Cold start DRI-SL (cluster semântico + variedade lexical) | ✅ Implementado, logs reais | ⚠️ Cap. 4 com tabela parcial e 4 figuras placeholder | **Sim, gerar figuras** |
| 4 | Avaliação do oráculo LLM (4 modelos, N=1000-2000 cada) | ⚠️ Real, mas schema sem `enum` contamina a medida (acc 21–58%) | ❌ Duas seções conflitantes (GPT template vs. Gemini parcial N=10) | **Refazer com correção** |
| 5 | Métrica LCE | ✅ Implementada (`calculate_lce`) | ✅ Formalizada (apêndice v5) — mas Cap. 3 diz trapézio e apêndice diz Simpson | **Sim, unificar definição** |
| 6 | ActiveLearner loop (PVBin + estratégias ENT/LC/SM/HYB + oráculo simulado) | ✅ Implementado | ⚠️ Cap. 4 `analise_aprendizado.tex` 100% template sem números | **Rodar e preencher OU cortar** |
| 7 | FALCO completo (BERTimbau θ + oráculo LLM progressivo + 3 fases) | ❌ **Não existe** | ❌ Cap. 3 descreve em detalhe; Cap. 4 `falco.tex` 100% template | **Implementar (mínimo viável)** |
| 8 | Algoritmo IPR (incerteza × representatividade) | ❌ Não existe | ⚠️ Proposto formalmente no Cap. 3, nunca avaliado | **Cortar ou rebaixar a trabalho futuro** |
| 9 | Baselines RS/US com BERTimbau | ❌ Não existe | Descritos no Cap. 3 | **Implementar junto com o item 7** |
| 10 | Análise de custo financeiro do oráculo | ⚠️ Tokens registrados em `api_calls.csv` | ❌ Ausente | **Sim, barato — dados já existem** |

---

## 3. Parecer como banca simulada — perguntas que você levaria na defesa

Estas são as perguntas que eu, como membro de banca, faria com o texto atual — e que a reescrita precisa tornar respondíveis:

1. **"O senhor apresenta LCE de 0,88 e economia de 80% de rótulos. Onde estão as tabelas com desvio padrão e os testes de significância?"** — Hoje: não existem. Fatal.
2. **"A metodologia descreve GPT-4o como oráculo; os resultados mostram Gemini com N=10. Qual foi o experimento?"** — Inconsistência interna grave. O leitor não consegue saber o que foi feito.
3. **"Com um oráculo de ~58% de acurácia, como o senhor sustenta a premissa de que o LLM substitui a rotulagem humana?"** — A medida real está contaminada pelo schema sem `enum` (variações de fraseado contadas como erro: 'ovos de pascoa' ≠ 'ovo de pascoa'). Precisa ser re-medida com saída restrita e, se ainda ficar baixa, a narrativa do FALCO precisa mudar (ex.: oráculo com validação humana amostral).
4. **"O senhor propõe três algoritmos (DRI-Cluster, DRI-SL, IPR). Qual é O algoritmo da tese? Onde está a avaliação do IPR?"** — O Cap. 3 propõe DRI-Cluster (framework.tex) E DRI-SL (cold_start.tex) — que são a mesma ideia com formalizações diferentes — e o IPR, que nunca foi avaliado. Consolidar em UM algoritmo (o implementado: DRI-SL) e cortar o IPR.
5. **"Por que 2 épocas de fine-tuning? Por que b=64? Por que 5 repetições?"** — Sem justificativa hoje (recomendações 10 e 11 do orientador).
6. **"O Capítulo 2 gasta 15 páginas em conceitos de livro-texto (tipos de ML, k-fold, softmax). O que disso é necessário para entender a contribuição?"** — A seção `aprendizado_maquina` é enciclopédica; nível de mestrado introdutório, não de tese. Condensar agressivamente (de ~15 para ~4 páginas), mantendo apenas métricas multiclasse (macro-F1) e validação, que são usadas de fato.
7. **"O dataset é o mesmo da sua dissertação de mestrado. Qual é exatamente a fronteira entre os dois trabalhos?"** — O Cap. 1 novo já trata bem disso; manter e reforçar.
8. **"A hipótese fala em 'redução substancial de rótulos (15–25%)'. Qual é o critério quantitativo de aceitação da hipótese?"** — Precisa de um critério falseável definido ANTES do experimento (ex.: "atingir ≥95% do macro-F1 da supervisão completa com ≤30% dos rótulos").

---

## 4. Parecer como orientador — decisões estruturais para a reescrita

### 4.1 A tese precisa mudar de promessa
O texto atual vende "FALCO, framework completo em 3 fases validado em 175k instâncias". O mínimo defensável honesto é reposicionar a narrativa sobre **quatro pilares já reais + um experimento integrador novo em escala controlada**:

> **Nova espinha dorsal da tese:** "Como montar, com evidência empírica em cada componente, um processo de aprendizado ativo com oráculo LLM para texto curto em português?" — respondida por: (P1) quanto importa o L0 (sensibilidade + AG); (P2) como construir um L0 melhor sem rótulos (DRI-SL); (P3) o LLM serve como oráculo? A que custo e com que ruído? (avaliação corrigida + custo); (P4) o processo integrado (FALCO) supera RS/US sob o mesmo orçamento? (experimento novo, escala controlada); medido transversalmente por (P5) LCE.

Isso preserva o nome FALCO e a hipótese, mas faz cada capítulo de resultados corresponder a um experimento que existe.

### 4.2 Cortes recomendados
- **IPR**: cortar do Cap. 3; mover 1 parágrafo para trabalhos futuros.
- **DRI-Cluster vs. DRI-SL**: unificar sob um único nome (sugestão: manter **DRI-SL**, que é o implementado) com uma única formalização (a do apêndice, que é a mais precisa).
- **Seção `aprendizado_maquina` do Cap. 2**: reduzir a ~1/4, mantendo métricas multiclasse e validação.
- **Arquivos `genspark.tex`, `gemini.tex`, `novaescrita.tex`, `bibsold/`**: lixo de processo; não migram.
- **Seção duplicada de avaliação do oráculo no Cap. 4**: as duas versões morrem; nasce uma única, escrita a partir do experimento re-executado.
- **`analise_aprendizado.tex` (estratégias com PVBin + oráculo simulado)**: decidir — ou rodar (é barato, o código existe) ou cortar. Recomendo **rodar**: dá um capítulo inteiro de resultados por custo computacional baixo e fundamenta a escolha da estratégia de incerteza do FALCO.
- **Duas épocas/b=64**: transformar em experimento auxiliar pequeno (curvas de loss para 2-3 tamanhos de L) ou justificar por literatura com citação direta.

### 4.3 Riscos que a reescrita deve mitigar
- **Risco 1 — oráculo fraco:** se após corrigir o schema a acurácia do melhor LLM ficar < ~80%, a Fase 3 do FALCO ("LLM avançado refina") vira o argumento central: mostrar que o processo é robusto a ruído do oráculo passa a ser A contribuição. Planejar o texto para os dois desfechos.
- **Risco 2 — BERTimbau caro demais:** fine-tuning iterativo em pool de 175k pode ser inviável na RTX 3090. Mitigação: pool subamostrado estratificado (ex.: 50k), batch de consulta maior (ex.: 512–1000), 3–5 sementes + teste de Wilcoxon (responde recomendação 11 com rigor, não com força bruta).
- **Risco 3 — template:** o template novo (`ppginf.cls`, Maziero) é do PPGINF/UFPR; a tese é do PPGMNE. **Confirmar com a secretaria do programa que o formato é aceito** antes de migrar tudo (ou confirmar que a intenção é mesmo usar esse formato).

---

## 5. Plano de reescrita capítulo a capítulo (draft → tesedaru)

Estrutura de destino no template: `0-iniciais/`, `1-intro/`, `2-fundam/`, `3-metodo/`, `4-resultados/` (possivelmente dividido), `5-conclusao/`, apêndices `a1-`, `a2-`... Bibliografia migra de biblatex/biber para BibTeX (`apalike-ptbr.bst`) — todas as citações `\textcite`/`\citep` precisam ser revisadas na migração.

| Destino (tesedaru) | Fonte (draft) | Ação | Prioridade |
|---|---|---|---|
| `0-iniciais/resumo.tex` + `abstract.tex` | `00-dados.tex` (Resumo/Abstract) | **Reescrever ao final** com números reais; corrigir sigla LCE (já feito no draft) | Última |
| `0-iniciais/acronimos.tex` | lista de siglas criada no draft | Migrar direto | Baixa |
| `1-intro/texto.tex` | `nova_introducao.tex` | **Reaproveitar ~80%**. Ajustes: (i) reescrever "Organização do trabalho" para a nova estrutura; (ii) adicionar critério quantitativo falseável à hipótese; (iii) já apontar os 4 pilares | Alta |
| `2-fundam/texto.tex` §ML | `aprendizado_maquina.tex` | **Condensar 75%** → só métricas multiclasse + validação | Média |
| `2-fundam/texto.tex` §AL | `_0` a `_4` de `aprendizado_ativo/` | **Reaproveitar ~90%** (formalismo, cenários, estratégias, LLM-oráculo são bons) | Média |
| `2-fundam/texto.tex` §STC | `texto_curto/0..5` | **Reaproveitar ~85%**; cortar redundâncias com a dissertação de mestrado (citar em vez de reexplicar) | Média |
| `2-fundam/texto.tex` §Revisão | `revisao_aprendizado_classificacao.tex` | **Reaproveitar ~95%** (já atualizada até 2026 nesta sessão) | Baixa |
| `3-metodo/texto.tex` | `metodologia_main` + módulos | **Reescrever ~60%**: unificar DRI, cortar IPR, alinhar oráculo ao decidido na Fase 0, parâmetros AG reais (já preenchidos), UMA definição de LCE (Simpson), justificar épocas/batch/repetições, desenho experimental dos 4 pilares | **Crítica** |
| `4a-resultados/` P1 (L0+AG) | `introducao.tex` + `lote_genetico.tex` do cap. 4 | **Reaproveitar ~80% / condensar**: L0 sensitivity está pronto; AG reduzir de 575 linhas para ~1/3 (mover figuras de correlação em massa para apêndice) | Alta |
| `4a-resultados/` P2 (DRI-SL) | `cold_start.tex` do cap. 4 | **Completar**: gerar as 4 figuras reais a partir de `dri_vs_random_final_log_results.csv`; validar tabela | Alta |
| `4b-resultados/` P3 (oráculo) | `oraculo.tex` do cap. 4 | **Reescrever do zero** após experimento corrigido (Fase 0): tabela multi-modelo, matriz de confusão/análise de erros, custo por 1k rótulos vs. rotulagem humana | **Crítica** |
| `4b-resultados/` P4 (FALCO vs RS/US) | `falco.tex` + `analise_aprendizado.tex` | **Escrever do zero** com o experimento novo (Fase 2); curvas de aprendizado, LCE, Wilcoxon | **Crítica** |
| `5-conclusao/` | `discussao.tex` + `conclusao.tex` | **Reescrever ~70%**: estrutura aproveita (limitações/futuros bons); todo bloco `[Suposição:]` substituído por números reais; comparação com trabalhos relacionados (reescrita nesta sessão) migra ~90% | Alta |
| `a1-` LCE | `learning_curve.tex` (v5) | Migrar direto (já deduplicado) | Baixa |
| `a2-` AG | `algoritmos_geneticos.tex` | Migrar direto | Baixa |
| `a3-` DRI-SL | `cold_start.tex` (apêndice) | Migrar; virar A formalização única do DRI-SL | Baixa |
| `a4-` Biblioteca | `biblioteca_falco.tex` | **Reescrever** descrevendo a `activelearning` nova (arquitetura DDD+Hexagonal, como instalar, como reproduzir cada experimento) | Média |
| `a5-` Prompts do oráculo | — (não existe) | **Escrever**: prompt final + schema JSON com `enum` — é referenciado 2× no texto e nunca existiu | Média |
| `a6-` Tabela stats L0 | `tabela_resultado_stats_l0.tex` | Migrar direto | Baixa |

**Não migram:** `bibsold/`, `padraoufpr-master/`, `capitulo_01_introducao/introducao.tex` (versão velha), `genspark*/gemini*/novaescrita*`, `capitulo_02_fundamentos/revisao/revisao_main.tex` (rascunho standalone), `code/` (scripts de join).

---

## 6. Experimentos mínimos para a defesa (em ordem)

| # | Experimento | Código necessário | Custo estimado | Preenche |
|---|---|---|---|---|
| E0 | Re-avaliação do oráculo com schema `enum` (4 modelos × N≥1000, temperatura fixa 0.0) + análise de erros + custo | Porta do oráculo na lib nova + correção do schema | Horas (APIs) / dias | Pilar P3; recomendações 12, 13 |
| E1 | Curvas de estratégia com PVBin + oráculo simulado (RND/ENT/LC/SM, b ∈ {64, 256, 1000}) | Já existe no legado; portar | ~1 dia de CPU | `analise_aprendizado`; justifica ENT e b |
| E2 | Justificativa de épocas: loss/val por época (1–4) para |L| ∈ {1k, 10k, 50k} com BERTimbau | Classificador BERTimbau novo | ~horas de GPU | Recomendação 10 |
| E3 | **FALCO vs RS vs US** (BERTimbau, oráculo decidido em E0, pool estratificado ~50k, B=30%, b a definir por E1, 3–5 sementes) + Wilcoxon + LCE | Lib nova completa | Dias de GPU | Pilar P4 — `falco.tex`, Discussão, Conclusão |
| E4 | (Se E0 der acurácia baixa) FALCO com oráculo simulado com ruído controlado {0%, 10%, 20%, 40%} | Trivial na lib nova | ~1 dia GPU | Robustez ao ruído (recomendação 14) |

O DRI-SL não precisa ser re-executado — só gerar as figuras a partir dos logs existentes (validando antes que o log corresponde à formalização final).

---

## 7. Sequência recomendada

1. **Fase 0** — E0 (oráculo corrigido) — desbloqueia a decisão de narrativa.
2. **Fase 1** — Constituição spec-kit + arquitetura DDD/Hexagonal da `activelearning`; portar domínio + adapters mínimos para E0/E1.
3. **Fase 2** — E1, E2, E3 (e E4 se necessário).
4. **Fase 3** — Reescrita no `tesedaru` conforme §5, capítulos na ordem: 3 → 4a → 4b → 5 → 1 → 2 → pré-textuais.
5. **Flowbuilder** — nasce como *driving adapter* da lib (API REST) depois que E3 estiver rodando; a UI vem por último.

**Regra de ouro para todo o processo:** nenhum número entra no `tesedaru` sem um artefato rastreável (CSV/JSON de execução) no `activelearning`. A lib nova deve ter um comando `reproduce e3` (ou similar) por experimento — isso vira, inclusive, argumento de replicabilidade na defesa.
