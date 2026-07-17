# Checklist da Jornada — Tese FALCO

Convenção: `[ ]` pendente · `[~]` em andamento · `[x] tarefa [início → fim]`
(horários GMT-3). Tarefas desdobradas em subtarefas quando necessário.
Meta de encerramento: **somente o bloco H (GPU/BERTimbau) e seus dependentes
podem restar abertos.**

---

## A. Correções da Revisão R1 (bloqueantes primeiro)
- [ ] A1. Trocar T→V no critério de transição de fase (Cap.3 §3.8.1)
- [ ] A2. Corrigir inferência do E3: ≥8 sementes + IC bootstrap sobre ΔLCE (texto Cap.3)
- [ ] A3. Declarar fitness do AG e protocolo anticircularidade do envelope (Cap.3 P1)
- [ ] A4. Citar ALC (Guyon 2011) e demarcar o delta da LCE (Cap.3 + Apêndice LCE)
- [ ] A5. Seção de ameaças à validade (dataset único, autor-criador, instrumento)
- [ ] A6. Literatura de noisy labels no Cap.2 (fonte via web + bib + fichamento)
- [ ] A7. Justificar constantes (85%, p=5, ε=1e-3, b0=1%B) com racional/decisão
- [ ] A8. Definir L_ideal,0 inline; procedimento da subamostra 50k do E3
- [ ] A9. Baseline extra no desenho E3: "100% rotulado pelo oráculo" (ataque DA-2)
- [ ] A10. Pendências Cap.2: redundância STC vs dissertação; figura ActiveLLM

## B. Biblioteca activelearning (código + testes)
- [ ] B1. D4: portar PVBin do legado (ProductVectorizerClassifier → adapter)
  - [ ] B1a. Adapter + porta TaskClassifier no domínio
  - [ ] B1b. Testes unitários (treino mínimo, predict_proba, reprodutibilidade por semente)
  - [ ] B1c. Validação contra legado (mesmos dados → mesmas predições)
- [ ] B2. D3: portar DRI-SL (SBERT + k-means + novidade lexical)
  - [ ] B2a. Implementação com embeddings CPU (sentence-transformers)
  - [ ] B2b. Testes unitários (determinismo por semente, cobertura de clusters)
- [ ] B3. Laço RunActiveLearning (iterações, curvas, LCE, retomável)
- [ ] B4. Runner FALCO (fases, transição por V, troca de oráculo)
- [ ] B5. Suíte completa verde + lint

## C. Reexecução dos experimentos do autor (validação independente)
- [ ] C1. P1-replay: sensibilidade de L0 (grade reduzida com racional; comparar com originais)
- [ ] C2. AG-replay: 2-3 tamanhos de L0, fitness em validação (anticircularidade)
- [ ] C3. Relatório de convergência reexecução × originais (docs/)

## D. Experimentos novos (CPU/API)
- [ ] D1. E0: finalizar glm-5.2 + 4 free OpenRouter (runs em andamento)
- [ ] D2. E0: análise consolidada final (Wilson+McNemar+gate formal+custo)
- [ ] D3. E0-P: ablação de prompt no modelo fraco
  - [ ] D3a. Prompt v4a (regras de fronteira) e v4b (few-shot pares confundidos)
  - [ ] D3b. Execução pareada (mini + 1 free; n=500 rand + 500 strat)
  - [ ] D3c. Análise McNemar v3×v4a×v4b + recomendação
- [ ] D4. E1: estratégias × lote (PVBin + oráculo simulado, multi-semente)
- [ ] D5. E4: robustez a ruído ε∈{0, .1, .2, .4} (PVBin; BERTimbau fica p/ H)
- [ ] D6. Artefatos e análises commitados (results/ + tabelas prontas p/ tese)

## E. FlowBuilder ponta a ponta
- [ ] E1. Upload de CSV pela UI → persistido na base (SQLite/Neon)
- [ ] E2. Saneamento automático (inativo/conflitos/duplicatas) + relatório + download da base saneada
- [ ] E3. Execução parametrizada pela UI (semente, lote, estratégia, oráculo, orçamento, amostras)
- [ ] E4. Fluxo de AL completo pela UI (curva de aprendizado visível)
- [ ] E5. Teste E2E com LLM free como oráculo + SimulatedOracle offline
- [ ] E6. Testes de API para upload/saneamento/parâmetros

## F. Escrita da tese (com dados reais das seções C/D)
- [ ] F1. Cap.4: resultados P1 (sensibilidade + AG) — original + replay
- [ ] F2. Cap.4: resultados P2 (DRI-SL vs aleatório vs envelope AG)
- [ ] F3. Cap.5: resultados E0 completos (RQ1-4, gate, custo, anatomia de erros, sensibilidade a ruído de gabarito)
- [ ] F4. Cap.5: E0-P (prompt como instrumento) + E1 + E4
- [ ] F5. Cap.6: discussão e conclusão (sem placeholders; lacunas GPU explícitas)
- [ ] F6. Apêndices a1-a6 (LCE+ALC, AG, DRI-SL, biblioteca, prompts v3/v4, tabelas)
- [ ] F7. Pré-textuais: resumo/abstract com números reais, siglas, listas
- [ ] F8. Compilação LaTeX limpa (instalar TeX ou validação estática rigorosa + CI)

## G. Revisão e refinamento final
- [ ] G1. Re-rodar academic-paper-reviewer (R2) na tese completa
- [ ] G2. Aplicar correções da R2; iterar até sem bloqueantes solucionáveis
- [ ] G3. Poda de citações fracas (candidatos marcados nos fichamentos)
- [ ] G4. KG e fichamentos atualizados com novas fontes
- [ ] G5. Verificação final: números da tese ⇄ artefatos (rastreabilidade 100%)
- [ ] G6. Diário e decisões atualizados; push final de tudo

## H. Dependentes de GPU (ficam abertos para a estação RTX 3090)
- [ ] H1. E2: épocas de fine-tuning BERTimbau por |L| (script pronto-para-rodar)
- [ ] H2. E3: FALCO vs RS vs US com BERTimbau, ≥8 sementes (script pronto-para-rodar)
- [ ] H3. E4-BERTimbau: repetição do E4 com classificador forte (condicional)
- [ ] H4. F-gpu: inserir números E2/E3 nos Caps. 5-6 + fechar hipótese central
- [ ] H5. Rotação das 4 credenciais pelo autor após conclusão dos runs de API
