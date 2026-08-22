---
de: banca
para: principal
tipo: entrega
acao_esperada: despachar a CRUZADA do revisor2 sobre banca/veredito-lote16 @ 0bfa5e1 (os quadros e a distinção média×3-de-3 são dele; a aritmética nova precisa da regra 3); depois gate do autor. ATENÇÃO à ordem de merge no §4: a branch está EMPILHADA sobre a 1210
referencia: aprovação do mapa pelo autor ("aprovo o mapa, pode redigir") · tarefa 1600 + insumos 1-6 · medição dos pisos do revisor2 (0110) · entrega 0235 do executor02
criada_em: 2026-08-22T02:30:00Z
---

# 1. O que a branch contém (0bfa5e1, 6 arquivos)

- **Cap. 1**: o critério muda para a métrica do pré-registro — "pelo menos
  95% da ACURÁCIA que o mesmo classificador obtém com o pool de referência"
  — com a frase que explica: acurácia é a métrica do critério porque é a do
  pré-registro; o Macro F1 acompanha como análise de robustez para o espaço
  de centenas de classes.
- **Cap. 3** (uma frase, o critério de aceitação): acc(A) >= 0,95·acc(D), F1
  como robustez, |A| limitado ao teto — sem isso o Cap. 3 contradiria o
  Cap. 1 dentro do mesmo gate.
- **Cap. 5** (seção E3' inteira): regime declarado (lote 16 com clipping,
  3 sementes, avaliação nos 177.490) com o sub-treino do lote 128 como
  achado metodológico; tabela principal com média±desvio; decomposição
  (i)/(ii)/(iii) reescrita nos números novos SEM os números órfãos do cache
  antigo (concordância 71,6% e contagens de cobertura saíram — comentário
  PROVISORIO pede os valores do cache canônico à regeração); varredura com
  a tabela nova (colunas % base e contagem de sementes que cruzam) e as
  três leituras.
- **Cap. 6**: os dois vereditos e a extensão prioritária (piso agora por
  \ref, sem número — não quebra se deslizar).
- **Resumo/abstract**: item (v) reescrito espelhado; item (iv) ganhou o
  denominador ("15% do pool desse experimento") para não colidir com o teto.

# 2. As três regras duras da redação, cumpridas

1. **Média × 3-de-3 declarada** (medição do revisor2): o veredito apoia-se
   na ACURÁCIA, que cruza em 20 mil nas TRÊS sementes; o F1 é reportado com
   a gradação ("na média, dentro do teto; em todas as sementes, apenas no
   braço de 35 mil, fração de ponto ACIMA do teto") — e a frase registra
   que o teto não acomodar o melhor braço afasta a suspeita de critério
   ajustado. Critério de robustez ÚNICO em toda a redação.
2. **Margem fina protegida**: nenhuma frase de prosa quebra se o piso do F1
   deslizar de 25 para 30 mil na regeração — os pontos de cruzamento vivem
   nas tabelas e nas frases marcadas.
3. **9 marcas `% PROVISORIO-ate-regeracao`** nos valores que a regeração
   pode mover; a troca final é mecânica (grep pelo marcador).

# 3. O que a redação NÃO afirma (guardas)

- Nunca "sustentada com oráculo LLM": o braço A não atinge e isso está
  escrito (gap em acurácia e F1, 5,2% da população); a espinha é "atingível
  dentro do teto (gabarito) × execução que parou aquém do piso".
- Nenhum número do regime legado sobreviveu (grep: 32--40%, 20.092, 8.937,
  refutad*, refuted = zero nos seis arquivos).
- A>B em F1 dito como "na média das sementes" (desvios se sobrepõem; sem IC
  novo não afirmo significância — a regeração fecha).

# 4. ORDEM DE MERGE (importante)

A branch está EMPILHADA sobre banca/pre-registro-e-lastro (1210, cruzada já
aprovada): o gate da 1210 mergeia PRIMEIRO, o desta em seguida (ou os dois
no mesmo bloco, na ordem). Mergear só a veredito-lote16 arrastaria a 1210
junto sem o registro de gate dela.

# 5. Fora desta branch (fila combinada)

Trem da higiene do Cap. 3 (pool-referência, percurso, semente-única->3,
parágrafo do sub-treino em detalhe) — por cima do Cap. 3 pós-merge; e a
troca mecânica dos PROVISORIO quando a regeração 27/27 fechar.
