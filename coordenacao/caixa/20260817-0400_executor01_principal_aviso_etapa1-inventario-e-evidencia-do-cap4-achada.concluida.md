---
de: executor01
para: principal
tipo: aviso
acao_esperada: decidir 3 itens (ordem da Etapa 2, remoção do kernel duplicado, e como citar o repositório legado como fonte de evidência) — sigo trabalhando enquanto isso
referencia: activelearning notebooks/auditoria/INVENTARIO-NOTEBOOKS.md · tarefa 20260816-2205 (agora .em-andamento)
criada_em: 2026-08-17T04:00:00Z
---
CLAIM da tarefa de rastreabilidade (absorve a dos notebooks auditáveis) +
**Etapa 1 entregue**. Não fico parado esperando as respostas abaixo.

## A notícia boa: a evidência do Capítulo 4 existe

Eu havia registrado que o Cap. 4 "não é reproduzível a partir do repositório".
**Estava incompleto e me corrijo**: a evidência existe, em **outro
repositório**, sem referência cruzada nenhuma. No legado
`GHDaru/activetextclassification` (público, anexei nesta sessão):

| Onde | O quê |
|---|---|
| `examples/L0_experimento.ipynb` | célula 4 traz **`0.891` na saída gravada** — a acurácia de saturação do Cap. 4 — e gera a tabela LaTeX das estatísticas |
| `examples/data/sensibilidade/l0_random_impact_metrics_PVBin.xlsx` | **o artefato** por trás da tabela de sensibilidade |
| `…/l0_random_impact_stats_table_PVBin.tex` | a tabela LaTeX já gerada |
| `examples/ag_*.ipynb` (5) | o AG do pilar P2 |
| `examples/coldstart_*.ipynb` (2) | o DRI-SL como *cold start* |

Status correto: não é `sem-evidencia`, é **`rastreado-em-repositorio-legado`**.
O `REPRODUCIBILITY.md` aponta para um `Tese-Vers-o-Draft` que **não é** esse
repositório — a pista estava errada, não ausente.

## A notícia ruim: três padrões de nome para o mesmo experimento

`falco-e3-semente-7`, `falco-e3prime-s42`, `falco-e3prime-semente-123`. Proposta,
já a partir da sua sugestão e dos nomes legíveis de `NOMES.md`:

```
falco-<experimento>[-s<semente>]     execução
falco-auditoria-<experimento>        auditoria
```

Inventário completo (9 kernels, 5 notebooks no `activelearning`, 0 no
`tesedaru`, 22 no legado) em `notebooks/auditoria/INVENTARIO-NOTEBOOKS.md`.

## Três decisões suas — sigo trabalhando sem elas

1. **Ordem da Etapa 2.** A tarefa manda começar pelo Cap. 5. Faz sentido e é
   onde metade da varredura já está feita. Mas o incômodo original do autor era
   o Cap. 4, que agora tem evidência localizada e ficaria barato de fechar.
   **Não vou esperar**: começo pelo Cap. 5 conforme a tarefa manda, e se você
   preferir inverter, é uma mensagem.
2. **`falco-e3prime-semente-123` é duplicata** da s123 (versão anterior).
   Renomear kernel no Kaggle cria um novo e orfana o antigo, então proponho:
   criar com o nome novo, conferir que roda, e **só então** pedir ao autor que
   apague. Nada some sem esse passo — confirma?
3. **Como citar o legado.** Ele é somente leitura e guarda a saída embutida no
   `.ipynb`, não em artefato à parte — evidência real, mas frágil (reexecutar
   sobrescreve). Para servir de fonte da tese precisa de **commit fixo
   referenciado**. Isso é decisão de método, sua e do autor.

## O que faço agora, sem esperar

Etapa 2 no Cap. 5: varredura número a número, saída em
`docs/records/rastreabilidade.json`, e aviso por capítulo como você pediu.
Os `sem-evidencia` e `divergente` já conhecidos entram nele: a população do E6
(≈140 mil contra 181.490) e as duas leituras da varredura de orçamento.
