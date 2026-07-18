# Plano de reestruturação do Capítulo 2 — para aprovação do autor

Motivação (diagnóstico de 18/07/2026): o Cap. 2 foi escrito antes de sabermos
onde a tese chegaria. Hoje ele tem **70 blocos de título para ~12,9 mil
palavras** (média 185 palavras/bloco), **4 níveis de numeração** (ex.:
2.5.3.2) mais 28 `\paragraph`, **13 blocos com menos de um parágrafo**, três
seções top-level fragmentadas para o mesmo assunto (AA), e **avaliação/validação
duplicadas** (uma vez na seção de ML, outra dentro de texto curto). Falta
fluidez; sobra taxonomia.

Princípio do redesenho: **cada seção existe para responder UMA pergunta e
deixar UMA mensagem que algum capítulo posterior usa**. O que não ancora
decisão dos Caps. 3–5 sai ou vira remissão (dissertação/legado).

## Regras de fluidez (valem também para o Cap. 3)

1. **Máximo 2 níveis numerados** (seção + subseção). `\subsubsection` extinto.
2. `\paragraph{}` só onde enumerar É o conteúdo (o catálogo de estratégias);
   nos demais, prosa corrida com os termos em destaque.
3. **Nenhum título seguido imediatamente de outro título** — todo título abre
   com texto-ponte que diz ao leitor por que a seção existe e o que vai
   encontrar.
4. Bloco com menos de ~60 palavras: funde-se ao vizinho ou vira meia frase.
5. Alvo de extensão: **~9,5–10 mil palavras** (corte líquido de ~25%).

## Estrutura proposta (5 seções) — pergunta · mensagem · contribuição

### 2.1 Fundamentos de aprendizado supervisionado para esta tese
- **Pergunta**: que instrumental mínimo o leitor precisa para auditar as
  decisões metodológicas dos Caps. 3–5?
- **Mensagem**: métrica e validação não são burocracia — Macro F1 (sob 621
  classes desbalanceadas) e deduplicação antes do particionamento decidem
  interpretações inteiras desta tese.
- **Muda**: FUNDE "Avaliação de Modelos" + "Estratégias de Validação" (hoje
  2.2.3/2.2.4) com a duplicata "Avaliação e Validação" que vive dentro de
  texto curto (2.6.6) — uma única passagem, dita uma vez.

### 2.2 Aprendizado ativo: o laço que compra informação
- **Pergunta**: por que selecionar bem economiza rótulos — e onde o laço
  clássico quebra?
- **Mensagem**: incerteza é o motor comprovado; as duas fraturas do laço
  clássico — *cold start* e oráculo imperfeito — são exatamente os pontos que
  o FALCO ataca.
- **Muda**: FUNDE as três seções top-level atuais (2.3 "Aprendizado Ativo" +
  2.4 "Formalização" + 2.5 "Cenários"); as estratégias de seleção sobem de
  altitude (hoje enterradas em 2.5.3) e são apresentadas como catálogo
  compacto: incerteza com fórmulas (é o que a tese usa), espaço de
  versão/EER/desacordo reduzidos a um parágrafo-síntese cada (hoje
  subsubseções de um parágrafo); densidade/representatividade ganham
  destaque (ancoram o DRI-SL). Entram DUAS adições novas exigidas pelos
  achados: parada do laço (ponte para o Apêndice A7) e **viés de amostragem
  ativa na avaliação** (Santos2016 + o achado do E6) — hoje o capítulo não
  prepara o leitor para nenhum dos dois.

### 2.3 O LLM no laço: de anotador a oráculo progressivo
- **Pergunta**: o que muda quando o oráculo é um modelo pago por token, com
  erro estruturado e servido por terceiros?
- **Mensagem**: o oráculo deixa de ser premissa (perfeito, humano) e vira
  **variável de projeto** — qualidade × custo × instrumento de medição; a
  tese inteira vive nessa mudança de regime.
- **Muda**: PROMOVE a atual subseção 2.5.4 a seção própria; absorve
  rótulos ruidosos (Frénay/NoiseBench/AlleNoise — ponte para E4), custo
  operacional (lote/cache/vazão — ponte para RQ2, com Kholodna) e a linha
  2025–2026 (DEUCE, CanDist, MoLLIA, Rouzegar) hoje espalhada entre 2.5.4 e a
  revisão. "Desafios e Direções" deixa de ser subsubseção e vira o fecho.

### 2.4 Classificação de texto curto em português: o domínio que aperta as condições
- **Pergunta**: por que descrições de varejo com 621 classes são o teste duro
  para tudo que foi dito acima?
- **Mensagem**: esparsidade + cauda longa tornam o Macro F1 implacável e o
  *cold start* crítico — e é por isso que o domínio é o laboratório certo.
- **Muda**: CORTA a vetorização enciclopédica (2.6.4, três subsubseções) para
  um resumo de meia página com remissão à dissertação \citep{Daru2024Dissertacao}
  (o próprio texto já declara essa dívida no cabeçalho W7); corta a duplicata
  de avaliação (vai para 2.1); mantém definições, desafios e algoritmos no
  essencial que o PVBin/BERTimbau exigem.

### 2.5 Estado da arte e a lacuna
- **Pergunta**: o que já foi feito nas três frentes — e o que ninguém juntou?
- **Mensagem**: as peças existem separadas (cold start informado; oráculo
  LLM; robustez a ruído; produto/e-commerce); **a integração em fases com
  instrumentação de custo é a lacuna** que o Cap. 3 ocupa.
- **Muda**: a revisão sistemática SOBE de subseção de texto curto (2.6.7)
  para seção própria de fechamento — ela cobre as três frentes, não só STC;
  termina na tabela de lacunas e na ponte explícita para o FALCO.

## O que sai do capítulo (com destino)

| Conteúdo atual | Destino |
|---|---|
| Subsubseções de 1 parágrafo (espaço de versão, EER, variância…) | síntese em prosa dentro de 2.2 |
| Vetorização enciclopédica (esparsas/densas/similaridade) | resumo + remissão à dissertação |
| "Avaliação e Validação" dentro de STC | fundido em 2.1 |
| 28 `\paragraph` | ~8 sobrevivem (catálogo de estratégias); resto vira prosa |
| Cenários emergentes de AA pouco usados | 1 parágrafo de panorama |

## Cap. 3 — correção de fluidez (mesma regra 3)

Diagnóstico: 5 pontos de "título seguido de título" (seção que abre direto em
subseção). Correção mínima e cirúrgica: um parágrafo-ponte de 2–4 linhas em
cada abertura de seção, dizendo o que a seção decide e como as subseções se
dividem. Sem mudança de estrutura ou numeração.

## Execução (após o OK)

1. Reescrita seção a seção na ordem 2.1→2.5, preservando TODAS as citações
   vivas (349 entradas; poda já feita) e as figuras (ActiveLLM permanece em 2.3).
2. Cada seção nova é validada contra a pergunta/mensagem declarada acima —
   se um parágrafo não serve à pergunta, sai.
3. Compilação + verificação de refs/citações a cada seção; commit por seção.
4. Pontes do Cap. 3 ao final.
5. Estimativa: uma sessão de trabalho; risco baixo (conteúdo preservado no
   histórico git; legado intocado como fonte).
