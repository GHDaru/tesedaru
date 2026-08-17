---
# ===== IDENTIDADE (nó Paper do grafo) =====
id: Aliero2023
title: "Systematic Review on Text Normalization Techniques and its Approach to Non-Standard Words"
authors: ["Aliero, Abubakar Ahmad", "Adebayo, Bashir Sulaimon", "Aliyu, Hamzat Olanrewaju", "Tafida, Amina Gogo", "Kangiwa, Bashar Umar", "Dankolo, Nasiru Muhammad"]
year: 2023
venue: "International Journal of Computer Applications, v. 185, n. 33, set. 2023"
doi: "10.5120/ijca2023923106"
pdf: referencias-pdf/Aliero2023.pdf

# ===== CLASSIFICAÇÃO =====
paper_type: survey
pillars: [geral]
status: ficha-minima

# ===== ENTIDADES =====
proposes: []
uses_methods: [normalizacao-de-texto]
datasets: []
metrics: []
tasks: [classificacao-de-texto]
models: []

# ===== RELAÇÕES COM OUTROS PAPERS =====
extends: []
compares_with: []
contradicts: []
builds_on: []

# ===== RELAÇÃO COM A TESE =====
falco_relation:
  - type: fundamenta
    target: FALCO
    note: "sustenta as duas frases da §2.3 sobre texto curto: a informalidade (erros, abreviações, contrações) exige normalização, e a normalização afeta o desempenho da tarefa a jusante"
---

# Systematic Review on Text Normalization Techniques and its Approach to Non-Standard Words

**Ficha mínima** (padrão do ciclo 008). Revisão sistemática de **54 artigos de
periódico e conferência publicados entre 2018 e 2022**, lida no PDF de acesso
aberto do IJCA (12 pp.).

## Os resultados que a tese usa

| # | Claim | Evidência | Uso na tese |
|---|-------|-----------|-------------|
| C1 | Normalização de texto é "corrigir erros de grafia, expandir abreviações, resolver contrações, normalizar pontuação e capitalização", com o fim de reduzir a variação lexical e ortográfica | Resumo, p. 1 | § "Classificação de texto curto" — sustenta "ruído e informalidade — erros, abreviações, gírias — que exigem normalização" |
| C2 | A normalização **melhora o desempenho da tarefa a jusante** de PLN, e é passo crítico de pré-processamento | Resumo, p. 1 | § "Classificação de texto curto" — sustenta que a escolha e a ordem do pré-processamento afetam o desempenho final |
| C3 | As técnicas existentes **não são diretamente transferíveis** entre línguas e domínios: "text normalization is not a one size fits all task" | Introdução, p. 1 | §2.3 e Cap. 3 — reforça por que o tratamento de ruído desta tese é específico do domínio (descrição de produto em português) |

## Leitura crítica em uma linha

O C3 é o achado que mais serve à tese e não estava sendo usado: a própria fonte
diz que as abordagens de normalização são específicas de língua e domínio, o que
**fortalece** a decisão desta tese de tratar ruído de forma específica em vez de
aplicar receita genérica. É acréscimo possível, não correção — as duas citações
atuais já estão sustentadas.

Ressalva de porte: é revisão em periódico de acesso aberto sem fator de impacto
alto, e o recorte (2018-2022) exclui trabalhos posteriores; serve como
fundamentação de prática consolidada, não como autoridade sobre estado da arte.
