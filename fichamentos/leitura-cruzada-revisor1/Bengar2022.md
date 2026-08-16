---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Bengar2022
title: "Class-Balanced Active Learning for Image Classification"
authors: ["Zolfaghari Bengar, Javad", "van de Weijer, Joost", "Lopez Fuentes, Laura", "Raducanu, Bogdan"]
year: 2022
venue: "IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)"
doi: "10.1109/WACV51458.2022.00376"
pdf: referencias-pdf/Bengar2022.pdf

# ===== CLASSIFICAÇÃO (arestas de tipo) =====
paper_type: metodo
pillars: [P1, P4]
status: fichado

# ===== ENTIDADES (nós Método/Dataset/Métrica/Tarefa; usar nomes canônicos) =====
proposes: [balanceamento-de-classes-na-selecao]   # CBAL: otimização entropia + termo de balanceamento
uses_methods: [aprendizado-ativo, pool-based, amostragem-por-incerteza, entropia,
               core-set, rotulagem-em-lote]
datasets: [cifar-10, cifar-100, tinyimagenet]
metrics: [acuracia]
tasks: [classificacao-de-imagens]
models: [resnet-18]

# ===== RELAÇÕES COM OUTROS PAPERS (arestas tipadas; alvo = chave bibtex) =====
extends: []
compares_with: [Sener2018, Kirsch2019]
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE (arestas para nós do FALCO) =====
falco_relation:
  - type: motiva
    target: FALCO
    note: "Demonstra que o desbalanceamento — vindo do pool (cauda longa) OU do viés
           de amostragem do próprio AL — degrada o classificador final quando o teste
           cobre todas as classes; é exatamente o risco central do FALCO com 714
           classes fortemente desbalanceadas e classes raras."
  - type: ameaca
    target: FALCO
    note: "Mostra que seleção por incerteza pura piora o perfil de classes ao longo
           dos ciclos; a fase de incerteza do FALCO precisa monitorar/discutir esse
           viés de amostragem sob cauda longa (Cap. 5)."
  - type: complementa
    target: DRI-SL
    note: "CBAL corrige o desbalanceamento DEPOIS, via termo explícito de
           balanceamento com pseudo-rótulos na aquisição; o DRI-SL age ANTES,
           buscando cobertura de classes por diversidade sem rótulos — mecanismos
           complementares contra o mesmo problema."
---

# Class-Balanced Active Learning for Image Classification (CBAL)

## Resumo (5-8 linhas, com as MINHAS palavras)

Investiga aprendizado ativo quando o pool não rotulado é desbalanceado (cauda longa)
e o teste é balanceado — cenário realista ignorado pela literatura que avalia AL em
datasets curados e uniformes. Propõe o CBAL: um problema de programação binária que
seleciona o lote maximizando a entropia (informatividade) menos λ vezes a norma L1
entre a distribuição de classes estimada (pseudo-rótulos via softmax do pool) e a
cota de amostras por classe necessária para atingir balanceamento no ciclo, com
salvaguarda contra sobreamostragem. O termo é geral: acopla-se a métodos informativos
(entropia, BALD) e representativos (k-Center-Greedy, VAAL). Em CIFAR-10/100 e Tiny
ImageNet com fatores de desbalanceamento 0,1/0,3/1, a versão -CB melhora quase
sempre os baselines, com ganhos maiores quanto mais classes e mais desbalanceamento;
mesmo em pools balanceados há ganho, por corrigir o viés de amostragem do AL.

## Claims relevantes
| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | AL é estudado quase só em datasets balanceados, mas dados reais seguem cauda longa; o pool desbalanceado leva a classificadores subótimos | Abstract; §1, p. 1536 | Cap. 2 fundamentação; enquadra o gap que o FALCO ocupa em varejo |
| C2 | Além do pool, o PRÓPRIO AL introduz viés de amostragem (quebra do i.i.d.) que desloca a distribuição de classes do conjunto rotulado | §1, p. 1536 | Cap. 2/5: risco da fase de incerteza do FALCO |
| C3 | Balanceamento pode ser imposto sem rótulos, confiando nos pseudo-rótulos (softmax) e minimizando entropia negativa + λ·ℓ1 até a cota Ω(c) por classe, como programação binária (relaxação LP + branch-and-bound) | §3 Eqs. (1)–(5); §4 Eq. (8), p. 1539 | Cap. 2: mecanismo alternativo ao DRI-SL contra desbalanceamento |
| C4 | O termo de balanceamento é geral: melhora métodos informativos (Entropy, BALD) e representativos (k-Center-Greedy, VAAL) | §5, Tabelas 1–3, p. 1543 | Cap. 5 discussão |
| C5 | Ganhos crescem com nº de classes (CIFAR-100 > CIFAR-10) e com o desbalanceamento (IF=0,1 e 0,3 > IF=1); mesmo com pool balanceado (IF=1) há ganho, ao conter o viés de amostragem | Tabelas 1–2, p. 1543; §5 | Cap. 5: extrapolação para 714 classes desbalanceadas |

## Números que posso citar
- Protocolo: fatores de desbalanceamento **IF ∈ {0,1; 0,3; 1}** aplicados a metade
  das classes; CIFAR-10/100 e Tiny ImageNet; 4–5 ciclos de AL (§5, p. 1542–1543).
- CIFAR-100, IF=0,1: **Entropy-CB até +2,23 p.p.** por ciclo sobre Entropy;
  **VAAL-CB até +3,29 p.p.** (IF=0,3) sobre VAAL (Tabela 2, p. 1543).
- VAAL-CB: **≈3% de melhora média** sobre o baseline VAAL em CIFAR-100 (§5, p. 1543,
  ref. Fig. 6b).
- CIFAR-10: ganhos menores (até +1,19 p.p., VAAL-CB, IF=0,1, ciclo 4; Tabela 1).
- Tiny ImageNet: Entropy-CB e BALD-CB positivos em quase todos os ciclos (até
  +1,11 p.p., BALD-CB, IF=1, ciclo 3; Tabela 3, p. 1543).
- Cota por classe: **ω_i = max((c·b + b₀)/C − n_i, 0)** (Eq. 4, p. 1539) — evita
  sobreamostragem de classe já coberta.

## Citações diretas (com página)
> "Active learning is generally studied on balanced datasets where an equal amount
> of images per class is available. However, real-world datasets suffer from severe
> imbalanced classes, the so called long-tail distribution." (Abstract, p. 1536)

> "Our results suggests that class-balancing should be an important criteria when
> selecting samples, and that it should be considered next to the long-standing
> active learning criteria of informativeness and representativeness." (§6, p. 1543)

## Crítica / limitações (minha leitura)
- O balanceamento depende de pseudo-rótulos do classificador atual: com classes
  raras e classificador fraco (início do FALCO), a estimativa P pode ser tão
  enviesada que a cota Ω mira as classes erradas — o paper não avalia esse regime.
- Alvo é distribuição UNIFORME de teste; no FALCO a distribuição de produção é a
  própria cauda longa, e a métrica é macro/por-classe — o termo ℓ1 precisaria de
  alvo diferente de uniforme.
- Escala: 100–200 classes no máximo e orçamentos pequenos; programação binária com
  N=50k e C=714 é um objeto de otimização bem maior (eles usam CVXPY+Gurobi).
- Ganhos absolutos são modestos (frações de ponto a ~3 p.p.) e nem todos os ciclos
  são positivos (alguns negativos na Tabela 1/3, IF=1 e IF=0,3).
- Só imagens; nenhuma validação em texto ou com oráculo ruidoso (rótulo vem de
  oráculo perfeito, não de LLM).

## Ideias que gera para a tese
- Usar C1–C2 no Cap. 2 para fundamentar que desbalanceamento é problema DUPLO no
  AL (pool + viés de amostragem) — enquadramento direto para as 714 classes.
- No Cap. 5, discutir a fase de incerteza do FALCO à luz de C2: medir a distância
  entre distribuição de classes adquirida e a do pool ao longo dos ciclos.
- Extensão futura: acoplar um termo de balanceamento tipo CBAL usando os RÓTULOS
  DO ORÁCULO LLM (que o FALCO já tem, ao contrário do cenário sem rótulos deles)
  na seleção progressiva — versão informada do mecanismo, citável como derivação.
