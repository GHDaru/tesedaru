# Diário de Bordo — Jornada Autônoma (tese FALCO)

Registro operacional contínuo. Horários em GMT-3 (São Paulo).
Decisões formais com racional completo: `docs/decisoes.md`.

---

## 16/07/2026 23:17 — Preparação da jornada
- Missão recebida e reescrita para aprovação do autor; aguardando OK para iniciar.
- Inclusões do autor aceitas: (1) este diário com horário GMT-3; (2) experimento
  E0-P de ablação de prompt — modelo fraco (gpt-4o-mini) × prompts {v3, v4a
  regras de fronteira, v4b few-shot com pares confundidos}, pareado, McNemar.
  Racional: anatomia dos erros mostrou ~48% de erros de convenção de catálogo,
  atacáveis por prompt; mini custa ~US$0,05/1k com cache.
- Estado herdado: E0 oficial parcial commitado (OpenAI completo; v4-pro completo;
  glm-5.2 e 4 free do OpenRouter retomados em 2º plano). Revisão R1 da banca
  simulada com 4 bloqueantes mapeados. 122 fichamentos. FlowBuilder v0 no ar.

## 16/07/2026 23:22 — Checklist criado
- checklist.md com 8 blocos (A-H), ~45 tarefas; blocos A-G devem fechar na
  jornada; bloco H (GPU/BERTimbau + rotação de chaves) fica aberto por design.

## 16/07/2026 23:24 — OK recebido. Jornada iniciada.
- Ordem de ataque: A (correções R1) → B (biblioteca) → C (replays) → D
  (experimentos) → E (FlowBuilder) → F (escrita) → G (revisão R2).
- Runs em 2º plano herdados: MaaS (glm-5.2) e OpenRouter free — monitorados.

## 16/07/2026 23:27 — Bloco A concluído (10/10 correções da R1)
- A1: transição de fase agora usa V (vazamento de T eliminado no texto).
- A2: 8 sementes + IC bootstrap no E3 (Wilcoxon com n<6 era infalseável).
- A3: fitness do AG em partição de aferição; envelope reavaliado em T intocado.
- A4: LCE agora cita ALC (Guyon 2011) e demarca os dois deltas.
- A5: nova seção "Ameaças à validade" (externa/interna/constructo).
- A6: literatura de noisy labels no Cap.2 (Frénay 2014, Natarajan 2013, Song 2023).
- A7: constantes justificadas (85% ancorado no teto supervisionado 89,56%).
- A8: L_ideal,0 definido inline; procedimento da subamostra 50k declarado.
- A9: 5º braço do E3 (oráculo-total) separa ruído × parcimônia.
- A10: seção esparsa condensada citando a dissertação; figura ActiveLLM em TikZ real.
- Verificação estática: 0 citações órfãs, 0 refs quebradas.
- Próximo: Bloco B (portar PVBin do legado).

## 16/07/2026 23:40 — Bloco B em andamento; MaaS completo
- B1 PVBin portado: escores IDÊNTICOS ao legado (dif 0,0); divergências = 100%
  empates; decisão D-001 (desempate determinístico). 8 testes.
- B3 laço RunActiveLearning: 5 estratégias, L0 injetável, teste fora do laço.
  9 testes.
- B2 DRI-SL portado com porta de encoder (SBERT baixado e validado; TF-IDF+SVD
  p/ testes). 6 testes. Suíte: 58 verdes.
- E0: MaaS terminou — glm-5.2 (77,3% rand / 80,9% strat) e v4-pro completo
  (82,1% / 82,6%). Falta só OpenRouter free (rodando).
- Próximo: B4 runner FALCO; depois C (replays P1/AG).

## 17/07/2026 00:16 — Cap. 4 escrito (F1+F2); replays C1/C2 concluídos
- P1-replay: convergência com o original ≤0,7 p.p. em TODOS os tamanhos —
  validação independente forte (tabela no Cap.4).
- AG-replay: mecanismo reproduzido; QUANTIFICADA a inflação de circularidade
  (max_f1 I=500: aptidão 19,4% vs teste 13,1% = −6,3 p.p.) — vira achado
  metodológico da tese (Seção 4.4).
- Cap.4 completo: sensibilidade (com figuras do draft), AG (tabela original
  condensada 575→~30 linhas), DRI-SL vs envelope (resultado central P2:
  DRI-SL supera o MELHOR indivíduo do AG em 100..5000), reexecução+circularidade.
- E1/E4 sweeps rodando; E0 free rodando (nemotron 675/1000).

## 17/07/2026 02:30 — FlowBuilder E2E; Caps. 5 e 6; apêndices
- Bloco E: upload CSV → saneamento censitário (relatório + download da base
  saneada) → execução parametrizada (semente, lote, estratégia, oráculo,
  orçamento) → curva SVG na UI. 67 testes verdes (8 de API).
- E5 parcial: E2E com SimulatedOracle OK; oráculo LLM free adiado (D-003,
  contenção de cota com o E0 em 2º plano).
- Cap.5 núcleo E0 (RQ1-4 + gate), Cap.6 completo, apêndices a1-a6 escritos.

## 17/07/2026 09:15 — Compilação LaTeX limpa (F8)
- Cadeia pdflatex+bibtex funcionando após 8 iterações de correção (pacotes
  texlive, algorithm/algpseudocode, travessões corrompendo o .toc, \& no bib).
- principal.pdf: 0 erros. Restava 1 ref quebrada (sssec:consideracoes_praticas).

## 17/07/2026 09:55 — E0-P/E1/E4 analisados, persistidos e NA TESE (F4)
- Contêiner reiniciou durante a pausa: scipy/openai reinstalados; run free do
  OpenRouter retomado (resumível; nemotron-ultra rand 725/1000).
- Análises agora são artefatos: experiments/e0p/results/analysis.json e
  experiments/e1e4/results/analysis.json (antes só impressas).
- E0-P (n=500 pareado, McNemar exato): S-rand 60,4%→64,2% (v4a, p=0,045) →
  65,0% (v4b, p=0,012); S-strat 51,8%→44,8%/41,0% (p<0,001). Regras de
  fronteira ajudam a distribuição de produção e DESTROEM as classes raras —
  "faca de dois gumes" escrita na Seção E0-P do Cap.5.
- E1 (8 sementes, teto supervisionado 0,540): menor margem lidera LCE
  (0,528±0,013), menor confiança lidera F1 final (0,421±0,009); todas as
  incertezas > aleatória com p=0,0078 (máximo com n=8). Lote: 50≈100 > 200.
- E4: vantagem da entropia sobrevive a TODO ε (p=0,0078); retenção 87/74/54%
  em ε=0,1/0,2/0,4 — faixa dos LLMs reais (0,17-0,23) é tolerável; ruído
  uniforme = limite inferior vs erro estruturado do RQ3.
- Ref quebrada corrigida (seção comentada na condensação → citação inline).
- F7: resumo/abstract com números reais; siglas e símbolos reais; dedicatória/
  agradecimentos como placeholders explícitos do autor (não invento texto
  pessoal). Compilação: 89 páginas, 0 erros, 0 refs não definidas.
- Próximo: commit+push, depois Bloco G (revisão R2 com academic-paper-reviewer).

## 17/07/2026 10:50 — Bloco G: revisão R2 concluída (Minor Revision, 83,3)
- Re-review com matriz R&R: 10/10 itens do roteiro R1 verificados no texto;
  4/4 ataques do Advogado do Diabo endereçados. docs/revisao-pares-simulada-r2.md.
- Dois residuais achados e corrigidos NA RODADA: (1) ablações do FALCO
  adicionadas ao desenho do E3 (sem DRI-SL / sem troca de oráculo — responde
  DA-4); (2) Cap.1 agora conecta o gate ao destino da hipótese (refutação
  honesta condicional ao cardápio de oráculos — responde DA-1).
- Varredura dos capítulos novos: resumo/abstract diziam 259.464; N real é
  250.365 (Cap.3) — corrigido. Ablação de lote agora declara entropia
  (pré-registro) em vez de "melhor estratégia". Frase de vazão/latência no RQ2.
- G3: poda — 14/14 candidatos sem citação (Bhavani2021 removida do cluster).
- G4: KG regenerado (356 nós, 720 arestas).
- Suíte reinstalada pós-reinício do contêiner: 67 testes verdes.
- Compilação final da rodada: 89 páginas, 0 erros, 0 refs não definidas.
- PENDENTE (aguardando o run free do OpenRouter, retomado e rodando):
  D1 (anotações free), D2 (reconsolidação analyze_e0), E5 (E2E com LLM free,
  D-003), G5 final e G6 (push final). Check-in agendado.

## 17/07/2026 11:35 — BERTimbau em CPU: smoke test executado (pedido do autor)
- Escrito o adapter BertimbauClassifier (porta TaskClassifier, lazy imports,
  determinismo por semente) + experiments/e2e3/run_smoke_cpu.py.
- torch 2.13 CPU + transformers 5.14 instalados; modelo neuralmind (440MB) baixado.
- SEM erros bloqueantes na cadeia download→tokenização→fine-tune→predição.
- Resultados (CPU, max_len=32, b=16): 100 docs/10cls/1ép: acc 10% (subtreinado,
  como esperado); 3ép: 34%; 900 docs/30cls/3ép: acc 86,3% / Macro-F1 0,859 em
  235s de treino. Aprendizado converge corretamente.
- Custo medido: ~0,087 s/doc/época em CPU (competindo com o run free).
  Extrapolação honesta: E3 completo (150 retreinos/braço × 7 braços × 8
  sementes) é INVIÁVEL em CPU (ordem de anos); um único treino de 15k docs
  (~65 min) é viável — GPU segue necessária para E2/E3 (bloco H confirmado).
- Avisos não bloqueantes: cabeçalho de classificação inicializado do zero
  (esperado em fine-tune) e relatório verboso de carga do transformers v5.
- Run free OpenRouter: vivo, 775 anotações (~100/h — fortemente estrangulado).

## 17/07/2026 12:20 — D-005: escopo do braço free reduzido
- Vazão real do plano gratuito: ~75 rótulos/h (429s) → plano completo ≈ 6 dias.
- Decisão registrada (docs/decisoes.md): free = só nemotron-ultra × S-rand
  (150 itens restantes, ~2h); demais 3 modelos free abandonados no E0.
- Cap.3 corrigido: lista de candidatos agora reflete o executado (sai o
  Gemini 2.0 Flash, que nunca rodou; braço free com a redução declarada).
- Run reduzido relançado rastreado; ao concluir: D2 (analyze_e0), linha free
  no Cap.5, E5 (cota liberada), G5/G6.

## 17/07/2026 12:45 — D1 pausado: cota diária do free esgotada (diagnóstico)
- Sonda direta na API confirmou: 429 "free-models-per-day", limite de 50
  requisições/dia sem créditos; reset à 00:00 UTC (21:00 GMT-3).
- Isso explica a vazão de ~75 rótulos/h e as "mortes" aparentes: o run ficava
  em backoff longo. Run pausado; retomada agendada para 21:02 (faltam 150
  itens = 15 requisições — fecha em minutos após o reset).
- E5 (E2E com LLM free) idem: agendado para depois do reset.
- Opção nas mãos do autor: adicionar US$10 de créditos no OpenRouter libera
  1.000 req/dia free — fecharia D1+E5 imediatamente.

## 17/07/2026 13:15 — D-006: NVIDIA NIM destrava o braço free; notebook Colab/TPU
- Chave NIM do autor testada: 200 OK, temperatura 0, thinking desligável,
  sem cota diária aparente. Docs lidas (build.nvidia.com): structured output
  NÃO suportado (json-prompt mantido), contexto 1M, licença OpenMDW.
- NvidiaNimOracle + ramo "nvidia" na factory; config_full_nvidia.json.
- Braço free RESTAURADO ao desenho original: rand+strat completos rodando
  via NIM (D-006 desfaz a redução D-005; 850 anotações OpenRouter preservadas
  fora da análise oficial). Retomada agendada das 21:02 será cancelada se o
  NIM terminar antes.
- Notebook Colab/TPU criado: experiments/e2e3/bertimbau_colab_tpu.ipynb —
  autocontido, detecta TPU (torch_xla, bf16) > GPU > CPU, instruções de dados
  (upload/Drive), smoke 20k + base cheia, relatório JSON baixável.
- 5ª credencial (NVIDIA) adicionada ao .env local (gitignored) e ao H5.

## 17/07/2026 13:50 — Documentação completa da biblioteca/FlowBuilder + figuras
- 4 guias novos em activelearning/docs: biblioteca.md (uso com exemplos
  executáveis), flowbuilder.md (front+back+API curl), experimentos.md
  (execução/parametrização de tudo), avaliacao-e-graficos.md (rotinas de
  análise + convenções estatísticas). README com índice e estado real.
- Rotina nova experiments/plots/make_figures.py: curvas E1, degradação E4
  (com faixa dos LLMs reais) e custo×acurácia E0 — paleta categórica validada
  (colorblind-safe), rótulos diretos, PDF+PNG; inspeção visual feita e duas
  colisões de rótulo corrigidas.
- Run NVIDIA: 925/1000 na S-rand ao commitar.

## 17/07/2026 16:55 — Ciclo E2E real concluído; blocos A-G FECHADOS
- Ciclo FALCO completo com oráculo REAL e gratuito (nemotron/NIM), pedido do
  autor: PVBin (F1 teste 0,283; LCE 0,622; 991 rótulos; 23 min) e SGD
  logístico novo adapter (F1 0,358; LCE 0,605; 982 rótulos; 31 min).
  Curvas interna (validação) × externa (teste) registradas e plotadas
  (fig_ciclo_curvas) — coladas, sem superajuste à validação; SGD > PVBin
  neste regime de poucos rótulos com ruído de oráculo.
- Inválidos do oráculo: 1,9-2,9% — tratados pelo laço (instância pulada).
- E5 fechado (E2E com LLM free real); D1/D2 fechados; G5/G6 fechados.
- Contêiner reiniciou mais uma vez no meio do primeiro ciclo — sem perda
  (tudo commitado antes); run relançado e concluído.
- PERGUNTA DA JORNADA — "está tudo pronto?": SIM para os blocos A-G
  (meta de encerramento atingida). Aberto por design: bloco H — E2/E3/E4
  com BERTimbau na GPU do autor (adapter, scripts, notebook Colab e guia
  prontos) e H5 (rotação das 5 credenciais pelo autor).

## 17/07/2026 17:40 — R3 + parecer orientador/banca; ciclo 30k em execução
- Pedido do autor: orçamento 30.000 → CachedOracle novo (anotação nunca é
  re-consultada; 2º ciclo reaproveita interseções — validado: 1.920 hits,
  0 chamadas no smoke), runner parametrizado por CLI, execução lançada
  (pool 50k, val/test 2k, lote 100, nemotron/NIM; estimativa 8-12h + reuso).
- R3 (full, 5 personas): 84,5/100, Minor Revision inalterada — gap é o bloco
  H. Novos apontamentos aplicados NA HORA: fotografia (modelo, provedor,
  data) nas ameaças à validade; contingência do ranking E1→BERTimbau; achado
  de serving no resumo/abstract; APÊNDICE A7 novo (parada/liberação/drift).
- docs/parecer-orientador-banca.md: crítica franca nos dois papéis — tese de
  MÉTODO vestida de tese de resultado (reposicionar 1 frase); data de corte
  p/ bloco H; leitura correta do ciclo 30k (saturação, não comparação no fim
  da curva); ensaio da pergunta incômoda "por que não rotular tudo com o LLM
  grátis?" (resposta: braço oráculo-total + latência + E4).
- Compilação: 93 páginas, 0 erros, 0 refs não definidas.

## 18/07/2026 00:25 — Ciclo 15k (oráculo real) concluído: a parada trabalhou
- Pedido de 30k recalibrado p/ 15k (calibração b20×b50: p=0,58, 2,14× mais
  rápido → b=50). Resultado: o critério de estagnação em validação parou
  AMBOS os ciclos muito antes do orçamento — PVBin em 6.009 rótulos
  (F1 0,457) e SGD em 4.742 (F1 0,600; LCE 0,731). Com o oráculo a ~78%,
  gastar os 15k (quanto mais 30k) seria pagar por ruído — demonstração
  empírica do racional do apêndice A7.
- Curvas interna×externa coladas nos dois (figura atualizada); SGD segue
  dominante sobre PVBin sob rótulos ruidosos (+14 p.p. de F1 final).
- Cache: 70% de reaproveitamento no ciclo SGD (3.313 hits / 1.637 chamadas).

## 18/07/2026 01:10 — Auditoria de justificativas (pedido do autor)
- Varredura Caps. 3-5: métricas OK (Macro-F1/desbalanceamento, Wilson/McNemar/
  Wilcoxon por natureza do dado, LCE+ALC), constantes OK (A7), 50k OK, lote OK
  (calibração), 3/classe OK, 8 sementes OK.
- CINCO lacunas achadas e corrigidas: (1) n=1.000 da S-rand (meia-largura de
  Wilson ≤3 p.p. separa oráculos do gate); (2) n=500 do E0-P (poder do McNemar
  p/ 4-5 p.p. a 1/5 do custo); (3) desenho do E1 (20k/3.000/lote 100 — regime
  de interesse + 104 células em CPU); (4) níveis de ε do E4 (cercam a faixa
  real: abaixo/dentro/estresse 2×); (5) grades dos replays P1 (log-espaçada,
  forma da curva, 1/9 do custo) e AG (menor config que reproduz o mecanismo).
- Compilação: 0 erros, 0 refs não definidas.

## 18/07/2026 04:30 — E6 fechado (3 seletores × 2 classificadores × 50k)
- Entropia domina os dois classificadores na região útil; saturação a 95% do
  teto: SGD 8.000 / PVBin 19.000 rótulos, vs 16.500 / 40.000 da aleatória —
  a seleção por incerteza corta o custo de rótulo pela metade ou mais.
- ACHADO INESPERADO ("menos é mais"): o SGD treinado nos ~15k selecionados
  por entropia atinge Macro-F1 0,59 na população; treinado no pool INTEIRO
  (50k) cai para 0,44 — a amostra ativa é mais balanceada por classe que a
  distribuição natural; rotular tudo não é só desperdício, PIORA o macro.
  (PVBin é imune: protótipo por classe já normaliza.)
- Viés de autoavaliação (desenho do autor): controle validado — na aleatória
  o viés de acurácia é ~0; na entropia a acc interna SUBESTIMA (−14 p.p. no
  início); o Macro-F1 interno SUPERESTIMA em todos (pior no DRI-SL, +34 p.p.
  no início) — autoavaliação em amostra ativa não estima implantação.
- DRI-SL como seletor CONTÍNUO é o mais fraco dos três — coerente com a
  tese: DRI-SL é instrumento de cold start (Fase 1), não substituto da
  incerteza no laço.
