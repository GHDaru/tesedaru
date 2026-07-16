# Vocabulário controlado do grafo de conhecimento

IDs de paper = chave BibTeX. Entidades abaixo usam SEMPRE o nome canônico.

## Métodos/conceitos canônicos
aprendizado-ativo, pool-based, cold-start, amostragem-por-incerteza, entropia,
menor-confianca, menor-margem, query-by-committee, llm-como-oraculo,
llm-como-seletor, saida-estruturada, prompt-caching, rotulagem-em-lote,
destilacao-ativa, fine-tuning, DRI-SL, FALCO, LCE, algoritmo-genetico,
mixture-of-llms, few-shot, zero-shot

## Datasets canônicos
retail-product-description-ptbr, agnews, trec, imdb, ...

## Métricas canônicas
acuracia, macro-f1, lce, custo-por-rotulo, ic-wilson, mcnemar, wilcoxon

## Relações (arestas)
| Aresta | Semântica |
|---|---|
| proposes | paper → método/métrica que introduz |
| uses_methods / datasets / metrics / models | paper → entidade empregada |
| extends | paper → paper que ele estende |
| compares_with | paper ↔ paper comparado empiricamente |
| contradicts | paper → paper/claim que contesta |
| builds_on | paper → fundamento conceitual |
| falco_relation.compara/fundamenta/motiva/ameaca/complementa | paper → nó da tese |

## Pipeline para o KG
fichamentos/*.md → (script: front-matter → triplas) → JSON-LD/CSV de arestas →
Neo4j ou RDF. O corpo markdown NÃO entra no grafo; claims da tabela entram como
nós `Claim` ligados por `asserts` (paper→claim) e `evidences` (claim→localização).
