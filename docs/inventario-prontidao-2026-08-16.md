# Inventário de prontidão — Tese FALCO (Rodada 1)

Data: 2026-08-16 · Branch: `claude/critical-review-thesis-submission-f5hjgx`
Propósito: base factual para a sessão de revisão crítica pré-banca (ciclo de
prontidão em 5 rodadas). Rodadas seguintes: avaliação de escrita (anti-AI-slop),
varredura de skills/normas UFPR-PPGMNE, proposta e aplicação de análise de
prontidão.

## Tabela resumo

| Bloco | Item | Estado | Métrica |
|---|---|---|---|
| Corpo | Cap. 1 Introdução | ✅ escrito + **humanizado com gate humano** (ADR 0001, merge 2effcfc) | 1.309 palavras |
| Corpo | Cap. 2 Fundamentação | ✅ reestruturado (5 seções, 2 níveis) · ⬜ humanização pendente | 6.194 palavras |
| Corpo | Cap. 3 Método | ✅ escrito (R1 A1–A10 aplicados) · ⬜ humanização pendente | 4.640 palavras |
| Corpo | Cap. 4 Resultados L0 | ✅ escrito · ⬜ humanização pendente | 1.435 palavras |
| Corpo | Cap. 5 Resultados FALCO | ✅ escrito (E6 incluído) · ⬜ humanização pendente | 4.895 palavras |
| Corpo | Cap. 6 Conclusão | ✅ escrito (DRI-SL-C, "menos é mais") · ⬜ humanização pendente | 1.714 palavras |
| Pré-textuais | Resumo/Abstract, catalográfica, aprovação, dedicatória, agradecimentos, siglas, símbolos, **declaração de uso de IA** | ✅ presentes (10 arquivos em `0-iniciais/`) | resumo 729 palavras |
| Apêndices | A1 LCE · A2 AG · A3 DRI-SL · A4 biblioteca · A5 prompts · A6 tabelas · A7 parada/drift | ✅ presentes | 217–2.275 palavras cada |
| Bibliografia | `referencias.bib` (chave = ID universal) | ✅ | 369 entradas |
| Fichamentos | `fichamentos/` (skill `fichamento`, KG-ready) | ✅ | 146 fichamentos · 140 PDFs em `referencias-pdf/` |
| Saneamento | `a_sanear/` | ⚠️ 6 arquivos pendentes de triagem (5 já marcados `_TRIAGEM_*`, 1 `tesedaru.pdf` deslocado) | 6 arquivos |
| Compilação | `principal.pdf` commitado | ✅ 0 erros / 0 refs / 0 warnings BibTeX (diário 17-18/07) | ~84 pp. (ref. R5) |
| Artigos satélites | A1 oráculo · A2 viés · A3 cold-start · A4 framework · A5 recurso-base | ✅ rascunhos em `artigos/` · ⬜ autoria/ordem indefinida · ⬜ revisão de inglês | 5 artigos |
| Defesa | `apresentacao/defesa.tex` + arguição + notas | ✅ material existente | — |
| Governança | Plano mestre (W1–W9), checklist, diário, ADR 0001, records JSONL | ✅ ativos | — |
| Avaliação externa simulada | Pareceres R1→R5 (`academic-paper-reviewer`) | ✅ trajetória 84,5 → 85,7 → **88,4** · veredito R5: **aprovação com revisões menores (defensável)** | 5 rodadas |

## Estado científico (fechado)

- Hipótese central testada e respondida (E3′ com varredura de orçamento):
  "refutada em 30%, sustentada em 50%, causa identificada".
- Programa experimental completo: E0, E0-P, E1, E4, E6 (8 sementes, Wilcoxon),
  replays de validação (C1–C3), auditoria de proveniência dupla.
- Nenhum achado científico fora do texto (auditoria de 18/07).
- Regra de ouro respeitada: números rastreáveis a artefatos em
  `GHDaru/activelearning`.

## Mapa dos repositórios da tese (fornecido pelo autor, 2026-08-16)

| Repositório | Papel | Estado |
|---|---|---|
| `GHDaru/tesedaru` | A tese (LaTeX, ~90 p.) + 5 artigos + fichamentos/KG + slides de defesa + ADRs | **Ativo — fonte de verdade do texto** |
| `GHDaru/activelearning` | Biblioteca `falco-active-learning` + FlowBuilder (front/back em `apps/web`) + experimentos E0–E6/E3′ + dataset CSV + docs MkDocs | **Ativo — fonte de verdade do código** |
| `GHDaru/activetextclassification` | Programa experimental legado (P1/P2, AG, notebooks originais) | Congelado — só rastreabilidade |
| `GHDaru/Tese-Vers-o-Draft` | Rascunho antigo da tese | Superado pelo `tesedaru` |
| `GHDaru/FlowBuilder` | FlowBuilder antigo | Superado pelo `apps/web` do `activelearning` |
| `GHDaru/maestro` | Metodologia de governança (mapa de gates, ciclos) | **Adotada a partir de agora** |
| Kaggle (não-git) | Dataset publicado, DOI 10.34740/kaggle/dsv/4265348 | Pendente: definir licença (CC BY 4.0) |

## Artefatos de código (repositório `GHDaru/activelearning`)

Detalhamento do repositório de código (fontes: apêndice
`a4-biblioteca/texto.tex`, plano mestre, parecer R5, diário 17/07, mapa acima):

| Artefato | Descrição | Estado |
|---|---|---|
| Biblioteca `falco-active-learning` | Arquitetura hexagonal, domínio puro (instâncias, CategorySchema, OracleUsage, estratégias, LCE/Wilson/McNemar) sem dependência de rede | ✅ validada, **pip-instalável** (R5) |
| Adapters de oráculo | OpenAI, OpenAI-compatível/MaaS, OpenRouter, Gemini, Ollama, Simulado(ε) — custo, cache, lote e latência medidos por anotação | ✅ validados ao vivo |
| Adapters de classificador | PVBin (portado do legado, validado contra ele) e BERTimbau (`transformers`); DRI-SL com SBERT | ✅ |
| Casos de uso | Avaliação de oráculo (E0, retomável), laço de AL (E1/E4), runner FALCO (fases com transição por validação), saneamento | ✅ |
| Testes | Suíte unitária cobrindo domínio, adapters e casos de uso sem rede | ✅ verde + lint |
| Reprodutibilidade | 1 ponto de entrada por experimento, config versionada, seeds + JSONL por item/iteração, retomável | ✅ (base da regra de ouro) |
| **FlowBuilder** ("o site") | Interface web FastAPI + React (`apps/web` do `activelearning`; substitui o repo antigo `GHDaru/FlowBuilder`): upload de CSV com saneamento automático, execução parametrizada de fluxos (semente, orçamento, lote, L0, estratégia, oráculo incl. custo zero), curvas de aprendizado; índice em banco, artefatos em disco | ✅ E2E com oráculo real gratuito (ciclo FALCO completo em 17/07) |
| Documentação | docs MkDocs: biblioteca.md, flowbuilder.md, experimentos.md, avaliacao-e-graficos.md + README com estado real | ✅ (17/07) |
| DOI Zenodo do código | fecha os artefatos dos artigos A1/A5 | ⬜ pendente (P8) |

O FlowBuilder é interface local (não há site público no ar); o catálogo
executável de experimentos na interface foi um dos itens que fecharam o R5.

## Pendências conhecidas (herdadas do R5 §4 + estado atual)

| # | Pendência | Tipo | Origem |
|---|---|---|---|
| P1 | **Humanização calibrada dos Caps. 2–6** (só o Cap. 1 passou pelo ciclo com gate) | escrita / anti-AI-slop | ADR 0001 |
| P2 | Frase de proveniência dupla no Cap. 3 | editorial | R5 §4 |
| P3 | Licença explícita da base no Kaggle (CC BY 4.0) | decisão do autor | R5 §4 |
| P4 | Rotação das 5 chaves de API | segurança | R5 §4 |
| P5 | Autoria/ordem dos 5 artigos | decisão autor+orientador | R5 §4 |
| P6 | Proofreading final PT + inglês dos artigos | editorial | R5 §4 |
| P7 | Figura de arquitetura do A4 (ESWA) | editorial | R5 §4 |
| P8 | DOI Zenodo do código | operacional | R5 §4 |
| P9 | Triagem final de `a_sanear/` (6 arquivos) | higiene do repo | inventário |
| P10 | Verificação de conformidade com normas UFPR/SiBi e exigências PPGMNE (ficha catalográfica, termo de aprovação, formatação) | conformidade | rodada 3 |

## Ferramentas de agente disponíveis (para as próximas rodadas)

| Ferramenta | Situação | Observação |
|---|---|---|
| "Maestro" (organizador de ciclos) | ✅ **instalado no repo** (ciclo governanca-01, ADRs 0002/0003, `check-install.sh` verde): 13 agentes em `.claude/agents/`, 6 skills em `skills/`, comandos speckit + `/dod` + `/eval`, templates `.specify/`, governança em `docs/governance/` (incl. Constituição da Tese v1.1.0) | `CLAUDE.md`/`AGENTS.md` apontam para o método; skill local separada é desnecessária (duplicaria o layout verificado pelo manifest) |
| Skill `fichamento` (local, repo) | ✅ | única skill do repositório |
| Skill `humanizer` (pessoal) | ✅ | remove sinais de escrita de IA — candidata principal para a Rodada 2 |
| Skill "academic research/reviewer" | ❌ não habilitada | pareceres anteriores citam `academic-paper-reviewer` (ARS), aplicada externamente; buscar no marketplace na Rodada 3 |
| Skills auxiliares pessoais | ✅ | `toc-prt` (planejamento TOC), `pdf-extractor`, `docx/pptx/pdf` |

## Leitura executiva

O conteúdo científico está fechado e avaliado como defensável (R5 = 88,4).
O risco dominante para a banca **não é ciência, é escrita**: 18,9 mil palavras
(Caps. 2–6) ainda não passaram pelo ciclo de humanização com gate que o Cap. 1
recebeu, e a conformidade formal UFPR/PPGMNE nunca foi verificada
sistematicamente. As rodadas 2–5 atacam exatamente esses dois eixos.
