# Plano de reestruturação do Capítulo 2 — v2 detalhada (para aprovação)

Revisão de 18/07/2026 após feedback do autor: títulos sóbrios (sem retórica)
e conteúdo detalhado por subseção. Diagnóstico que motiva o plano: 70 blocos
de título para ~12,9 mil palavras, 4 níveis de numeração, 13 blocos com menos
de um parágrafo, três seções top-level para o mesmo assunto e
avaliação/validação duplicada em dois lugares.

Regras de fluidez: máximo 2 níveis numerados; `\paragraph` apenas no catálogo
de estratégias; todo título abre com texto-ponte; nenhum bloco menor que ~60
palavras; alvo ~9,5–10 mil palavras (corte líquido ≈25%).

---

## 2.1 Aprendizado supervisionado: conceitos, métricas e validação (~1.400 palavras)

*Função: dar ao leitor exatamente o instrumental usado nos Caps. 3–5 — nada além.*

- **2.1.1 Regimes de supervisão e a tarefa de classificação multiclasse.**
  Definição formal breve (Mitchell); supervisionado/não/semi como contexto do
  AA; a tarefa multiclasse com $K=621$ e desbalanceamento severo como caso da
  tese. *(condensa as atuais 2.2.1+2.2.2; ~350 palavras)*
- **2.1.2 Métricas para classes desbalanceadas.** Acurácia global; precisão/
  revocação/F1 por classe; agregações micro×macro e por que o Macro F1 é a
  métrica primária sob cauda longa (Sokolova); matriz de confusão como
  instrumento de diagnóstico (usada no perfil de erro do E0). *(funde 2.2.3 com
  a duplicata 2.6.6.1; ~450 palavras)*
- **2.1.3 Validação e particionamento.** Hold-out, validação cruzada
  estratificada, conjunto de validação separado do teste; a exigência
  específica da tese: deduplicação por texto normalizado ANTES do
  particionamento (vazamento por duplicatas em dados de varejo). *(funde 2.2.4
  com 2.6.6.2; ~350 palavras)*
- Fecho-ponte (~100 palavras): estas escolhas reaparecem como decisões
  auditáveis no Cap. 3.

**Sai:** algoritmos clássicos em catálogo (SVM/NB/KNN/árvores) — reduzidos a
uma frase com citações-síntese; descrição enciclopédica de conceitos que
nenhum capítulo posterior usa.

## 2.2 Aprendizado ativo (~2.600 palavras)

*Função: formalizar o laço, apresentar as estratégias que a tese usa e
estabelecer as duas limitações que motivam o FALCO.*

- **2.2.1 Formalização e cenários.** Origens (Angluin; Cohn; Lewis & Gale;
  Settles); o laço pool-based formal (U, L, θ, S, O, B) com a notação que o
  Cap. 3 reutiliza; cenários stream-based e por síntese em um parágrafo de
  panorama. *(funde as atuais seções 2.3+2.4+2.5.1, com 2.5.2 reduzida;
  ~600 palavras)*
- **2.2.2 Estratégias de seleção de instâncias.** Catálogo compacto em
  `\paragraph`: incerteza (menor confiança, menor margem, entropia — COM as
  fórmulas, pois o Cap. 5 as referencia); comitê/desacordo, redução de erro
  esperado e densidade/representatividade em um parágrafo-síntese cada (hoje
  são subsubseções de um parágrafo); densidade/cluster com meia página a mais
  por ancorar o DRI-SL (Nguyen & Smeulders; Dasgupta; Settles 2008). Fecho:
  tabela comparativa custo×hipóteses das famílias. *(reorganiza 2.5.3;
  ~1.000 palavras)*
- **2.2.3 Limitações do laço clássico.** As duas fraturas: (i) *cold start* —
  estratégias dependem de um modelo que ainda não existe (Bayer & Reuter;
  Yuan et al.); (ii) suposição de oráculo perfeito — anotadores reais erram
  (Snow; Sheng; Donmez) e viés de amostragem ativa: o conjunto rotulado deixa
  de ser i.i.d., afetando o treino e a própria avaliação (Settles;
  Santos & Carvalho) — preparando E6. Inclui critérios de parada do laço em
  um parágrafo (literatura + remissão ao Apêndice A7). *(novo, absorvendo
  material disperso; ~800 palavras)*
- Fecho-ponte (~200 palavras): as duas fraturas definem as Fases 1 e 3 do
  FALCO.

**Sai:** subsubseções de um parágrafo (espaço de versão, variância);
"cenários emergentes" pouco usados; o sumário comparativo redundante.

## 2.3 Modelos de linguagem como oráculos de rotulagem (~2.300 palavras)

*Função: estabelecer o estado do conhecimento sobre LLM-como-anotador — o
terreno do E0/E0-P — incluindo custo, ruído e instrumentação.*

- **2.3.1 Capacidades e evidência empírica.** Gilardi (LLM supera crowdworkers);
  zero/few-shot em classificação; granularidade típica dos estudos (dezenas a
  ~370 classes: Roumeliotis; Gholamian) — o contraste com 621 fica para o
  Cap. 5. *(~500 palavras)*
- **2.3.2 Arquiteturas de integração no laço.** LLM como anotador único
  (Zhang; Rouzegar com roteamento por confiança); como seletor (ActiveLLM);
  em lote com modelos menores (Kholodna — anotação em lote; CanDist — rótulos
  candidatos destilados; MoLLIA — mistura de LLMs leves); dual-expert para
  produto. Figura ActiveLLM permanece aqui. *(reorganiza 2.5.4.1–2.5.4.4 +
  material da revisão; ~700 palavras)*
- **2.3.3 Rótulos ruidosos e seu efeito no treinamento.** Taxonomia de ruído
  (Frénay & Verleysen; Natarajan; Song); ruído real × sintético (NoiseBench;
  AlleNoise) e a implicação para avaliação de robustez — base do E4.
  *(reloca o parágrafo A6 e expande ~1 parágrafo; ~450 palavras)*
- **2.3.4 Custo, instrumentação e reprodutibilidade da medição.** Estruturas
  de custo por token, lote e cache; restrição de saída ao espaço de classes
  (formato consumível ≠ semântica correta — Kholodna mede correção de
  formato); variabilidade entre provedores e versões (a medição como
  fotografia modelo-provedor-data) — base do RQ2/RQ4. *(novo — hoje a tese
  descobre isso no Cap. 5 sem preparo; ~450 palavras)*
- Fecho-ponte (~200 palavras): o oráculo passa de premissa a variável de
  projeto com três dimensões (qualidade, custo, instrumento) — é o espaço de
  decisão do FALCO.

## 2.4 Classificação de texto curto (~1.700 palavras)

*Função: caracterizar o domínio de aplicação e justificar por que ele
tensiona tudo que foi dito em 2.1–2.3.*

- **2.4.1 Definições e desafios.** O que conta como texto curto; esparsidade
  lexical, baixo contexto, informalidade/abreviação; especificidades do
  português de varejo (caixa alta, abreviações de cupom fiscal).
  *(condensa 2.6.1+2.6.2; ~600 palavras)*
- **2.4.2 Representação e classificadores.** Resumo de meia página:
  representações esparsas (TF-IDF binário — a família do PVBin) × densas
  (embeddings, SBERT — a família do DRI-SL e do BERTimbau), com remissão
  explícita à dissertação do autor para o tratamento extensivo
  (Daru 2024); classificadores usados na tese (protótipos, lineares,
  transformers) em um parágrafo cada. *(corta as 3 subsubseções de 2.6.4 e
  condensa 2.6.5; ~700 palavras)*
- **2.4.3 Implicações para aprendizado ativo no domínio.** Por que cauda
  longa torna Macro F1 implacável e cold start crítico; classes
  desbalanceadas em AL (Attenberg; Ertekin). *(novo fecho analítico;
  ~400 palavras)*

**Sai:** pré-processamento passo a passo (vira 2 frases); métricas de
similaridade; a subseção duplicada de avaliação.

## 2.5 Estado da arte na interseção e lacuna de pesquisa (~1.600 palavras)

*Função: revisão focada 2020–2026 nas três frentes combinadas; terminar na
lacuna que o Cap. 3 ocupa.*

- **2.5.1 Escopo e método da revisão.** Mantém a subseção atual (bases,
  período, termos, critérios). *(~250 palavras)*
- **2.5.2 Síntese por frente.** Cold start informado (DEUCE; ALPS/TypiClust
  em uma frase); LLM no laço (consolida referências de 2.3 sem repetir —
  aqui entra a LEITURA comparativa, não a descrição); robustez a ruído;
  produto/e-commerce (AlleNoise; dual-expert; zero-shot). *(reescreve
  2.6.7.2–2.6.7.4; ~700 palavras)*
- **2.5.3 Lacuna de pesquisa.** A tabela de lacunas (AL × STC × LLM × PT ×
  custo instrumentado) — preservada integralmente — e o parágrafo-ponte para
  o Cap. 3. *(~400 palavras + tabela)*
- **2.5.4 Conclusão do capítulo.** Meia página amarrando 2.1→2.5 na cadeia:
  métricas → laço → oráculo → domínio → lacuna. *(~250 palavras)*

---

## Correção de fluidez no Cap. 3 (sem mudança estrutural)

Parágrafo-ponte de 2–4 linhas nos 5 pontos onde uma seção abre diretamente
em subseção, declarando o que a seção decide e como se divide.

## Execução (após o OK)

Reescrita seção a seção (2.1→2.5) preservando todas as citações vivas e a
figura ActiveLLM; validação de cada seção contra a função declarada;
compilação + verificação de refs a cada seção; commit por seção; pontes do
Cap. 3 ao final. Conteúdo cortado permanece recuperável no histórico git e
no repositório legado.
