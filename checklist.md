# Checklist da Jornada — Tese FALCO

Convenção: `[ ]` pendente · `[~]` em andamento · `[x] tarefa [início → fim]`
(horários GMT-3). Tarefas desdobradas em subtarefas quando necessário.
Meta de encerramento: **somente o bloco H (GPU/BERTimbau) e seus dependentes
podem restar abertos.**

---

## A. Correções da Revisão R1 (bloqueantes primeiro)
- [x] A1. Trocar T→V no critério de transição de fase (Cap.3 §3.8.1) [23:20 → 23:27]
- [x] A2. Corrigir inferência do E3: ≥8 sementes + IC bootstrap sobre ΔLCE (texto Cap.3) [23:20 → 23:27]
- [x] A3. Declarar fitness do AG e protocolo anticircularidade do envelope (Cap.3 P1) [23:20 → 23:27]
- [x] A4. Citar ALC (Guyon 2011) e demarcar o delta da LCE (Cap.3 + Apêndice LCE) [23:20 → 23:27]
- [x] A5. Seção de ameaças à validade (dataset único, autor-criador, instrumento) [23:20 → 23:27]
- [x] A6. Literatura de noisy labels no Cap.2 (fonte via web + bib + fichamento) [23:20 → 23:27]
- [x] A7. Justificar constantes (85%, p=5, ε=1e-3, b0=1%B) com racional/decisão [23:20 → 23:27]
- [x] A8. Definir L_ideal,0 inline; procedimento da subamostra 50k do E3 [23:20 → 23:27]
- [x] A9. Baseline extra no desenho E3: "100% rotulado pelo oráculo" (ataque DA-2) [23:20 → 23:27]
- [x] A10. Pendências Cap.2: redundância STC vs dissertação; figura ActiveLLM [23:20 → 23:27]

## B. Biblioteca activelearning (código + testes)
- [x] B1. D4: portar PVBin do legado (ProductVectorizerClassifier → adapter) [23:45 → 23:42]
  - [x] B1a. Adapter + porta TaskClassifier no domínio [23:45 → 23:42]
  - [x] B1b. Testes unitários (treino mínimo, predict_proba, reprodutibilidade por semente) [23:45 → 23:42]
  - [x] B1c. Validação contra legado (mesmos dados → mesmas predições) [23:45 → 23:42]
- [x] B2. D3: portar DRI-SL (SBERT + k-means + novidade lexical) [23:45 → 23:42]
  - [x] B2a. Implementação com embeddings CPU (sentence-transformers) [23:45 → 23:42]
  - [x] B2b. Testes unitários (determinismo por semente, cobertura de clusters) [23:45 → 23:42]
- [x] B3. Laço RunActiveLearning (iterações, curvas, LCE, retomável) [23:45 → 23:42]
- [x] B4. Runner FALCO (fases, transição por V, troca de oráculo) [23:45 → 23:42]
- [x] B5. Suíte completa verde + lint [23:45 → 23:42]

## C. Reexecução dos experimentos do autor (validação independente)
- [x] C1. P1-replay: sensibilidade de L0 (grade reduzida com racional; comparar com originais) [16/07 23:50 → 17/07 00:16]
- [x] C2. AG-replay: 2-3 tamanhos de L0, fitness em validação (anticircularidade) [16/07 23:50 → 17/07 00:16]
- [x] C3. Relatório de convergência reexecução × originais (docs/) [17/07 09:45 → 09:55]

## D. Experimentos novos (CPU/API)
- [~] D1. E0: finalizar oráculos (pagos OK; free RESTAURADO completo via NVIDIA NIM — D-006; rand+strat rodando)
- [~] D2. E0: análise consolidada final (Wilson+McNemar+gate formal+custo) — análise oficial dos pagos PRONTA e na tese; reconsolidar quando os free terminarem
- [x] D3. E0-P: ablação de prompt no modelo fraco [17/07 00:20 → 09:40]
  - [x] D3a. Prompt v4a (regras de fronteira) e v4b (few-shot pares confundidos) [17/07 00:20 → 00:35]
  - [x] D3b. Execução pareada (mini + 1 free; n=500 rand + 500 strat) [17/07 00:35 → 02:10]
  - [x] D3c. Análise McNemar v3×v4a×v4b + recomendação [17/07 09:20 → 09:40]
- [x] D4. E1: estratégias × lote (PVBin + oráculo simulado, multi-semente) [17/07 00:10 → 09:40]
- [x] D5. E4: robustez a ruído ε∈{0, .1, .2, .4} (PVBin; BERTimbau fica p/ H) [17/07 00:10 → 09:40]
- [x] D6. Artefatos e análises commitados (results/ + tabelas prontas p/ tese) [17/07 09:40 → 10:00]

## E. FlowBuilder ponta a ponta
- [x] E1. Upload de CSV pela UI → persistido na base (SQLite/Neon) [17/07 01:00 → 02:30]
- [x] E2. Saneamento automático (inativo/conflitos/duplicatas) + relatório + download da base saneada [17/07 01:00 → 02:30]
- [x] E3. Execução parametrizada pela UI (semente, lote, estratégia, oráculo, orçamento, amostras) [17/07 01:00 → 02:30]
- [x] E4. Fluxo de AL completo pela UI (curva de aprendizado visível) [17/07 01:00 → 02:30]
- [~] E5. Teste E2E com LLM free como oráculo + SimulatedOracle offline (SimulatedOracle OK; free adiado por contenção de cota — D-003; retomar após D1)
- [x] E6. Testes de API para upload/saneamento/parâmetros [17/07 01:00 → 02:30]

## F. Escrita da tese (com dados reais das seções C/D)
- [x] F1. Cap.4: resultados P1 (sensibilidade + AG) — original + replay [17/07 00:00 → 00:16]
- [x] F2. Cap.4: resultados P2 (DRI-SL vs aleatório vs envelope AG) [17/07 00:00 → 00:16]
- [x] F3. Cap.5: resultados E0 completos (RQ1-4, gate, custo, anatomia de erros, sensibilidade a ruído de gabarito) [17/07 02:30 → 04:00]
- [x] F4. Cap.5: E0-P (prompt como instrumento) + E1 + E4 [17/07 09:20 → 09:50]
- [x] F5. Cap.6: discussão e conclusão (sem placeholders; lacunas GPU explícitas) [17/07 04:00 → 04:30]
- [x] F6. Apêndices a1-a6 (LCE+ALC, AG, DRI-SL, biblioteca, prompts v3/v4, tabelas) [17/07 04:30 → 05:30]
- [x] F7. Pré-textuais: resumo/abstract com números reais, siglas, listas [17/07 09:50 → 10:00]
- [x] F8. Compilação LaTeX limpa (instalar TeX ou validação estática rigorosa + CI) [17/07 05:30 → 09:15]

## G. Revisão e refinamento final
- [x] G1. Re-rodar academic-paper-reviewer (R2) na tese completa [17/07 10:05 → 10:40]
- [x] G2. Aplicar correções da R2; iterar até sem bloqueantes solucionáveis [17/07 10:20 → 10:45] (ablação E3, gate→hipótese no Cap.1, N=250.365, entropia pré-registrada, vazão/latência)
- [x] G3. Poda de citações fracas (14/14 candidatos não citados; Bhavani2021 removida) [17/07 10:40 → 10:45]
- [x] G4. KG e fichamentos atualizados (356 nós, 720 arestas) [17/07 10:45 → 10:47]
- [~] G5. Verificação por amostragem OK (E0-P/E1/E4 conferidos contra analysis.json; N corrigido no resumo); re-verificar consolidado do E0 após D2
- [ ] G6. Diário e decisões atualizados; push final de tudo

## H. Dependentes de GPU (ficam abertos para a estação RTX 3090)
- [ ] H1. E2: épocas de fine-tuning BERTimbau por |L| (adapter + smoke CPU validados 17/07 11:35 — 86,3% acc em 900 docs/30cls/3ép; cadeia sem erros; falta só a grade completa na GPU)
- [ ] H2. E3: FALCO vs RS vs US + ablações (L0 aleatório; sem troca de oráculo) com BERTimbau, ≥8 sementes (script pronto-para-rodar)
- [ ] H3. E4-BERTimbau: repetição do E4 com classificador forte (condicional)
- [ ] H4. F-gpu: inserir números E2/E3 nos Caps. 5-6 + fechar hipótese central
- [ ] H5. Rotação das 5 credenciais pelo autor após conclusão dos runs de API (OpenAI, OpenRouter, MaaS, Neon, NVIDIA NIM)
