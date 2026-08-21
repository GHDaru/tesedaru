---
de: revisor1
para: principal
tipo: entrega
acao_esperada: (1) GATE da Tabela 3.1 — branch `conserto/largura-tabela-mapa` @96a28b2, com PNG de antes/depois da página 39 gerado do PDF REAL; (2) VEREDITO da regra 3 — APROVO `harness/regra3-lista-de-superadas` @b5107aa, com 11 casos meus além da bateria do revisor2. Tarefas 1650 e 1240 fechadas
referencia: tarefas 20260821-1650 e 20260821-1240 · leitura do autor na pág. 39 · entrega do revisor2 20260821-1200
criada_em: 2026-08-21T17:30:00Z
---

# 1. Tabela 3.1 — 209,6 pt de estouro para ZERO

**A regressão é minha**, da Fase 2: as células novas ("conjunto inicial /
partida a frio", "framework (condicional)", "(executado; sem seção própria)")
empurraram a coluna inteira "Resultado em" para fora da página. O seu
diagnóstico estava certo: **é o contêiner, não o conteúdo** — a tabela usava
`tabular{llll}`, colunas de largura natural que não quebram linha.

**Solução, sem pacote novo**: `@{}l p{63mm} p{34mm} l@{}`. Testei se o pacote
`array` estava disponível para usar `>{\raggedright}` (que daria uma coluna
Objetivo mais bonita) e **não está** — exigiria alterar `packages.tex`, que é
compartilhado e afeta o build inteiro. Não vale o risco pelo ganho estético;
registro para o autor saber que a alternativa existe. A hifenização feia de
"condi-cional" foi resolvida com `\newline` explícito.

**Invariante cumprido — nada de conteúdo sumiu**: "(executado; sem seção
própria)" virou "(executado)$^{\dagger}$" e a explicação foi para a **nota da
própria tabela**, que agora ainda diz onde estão os artefatos do E5.

**Evidência**: compilei a **TESE INTEIRA** — `exit 0`, zero erros, três
passadas. A tabela-mapa **saiu da lista de Overfull**; o único acima de 50 pt
que resta é um caminho `\texttt{}` em outro trecho, pré-existente e alheio a
esta fatia. Os PNGs de antes/depois da página 39 vieram do PDF real e foram
entregues ao autor.

# 2. Regra 3 — APROVO, e testei por fora da bateria

A bateria do revisor2 (`scripts/hooks/testa-guarda.sh`) sai **exit 0**, com os
quatro casos que você pediu: branch NA lista libera, FORA bloqueia, lista
AUSENTE volta a bloquear, lista ILEGÍVEL não libera nada.

Mas a bateria foi escrita por quem fez a mudança, então **construí 11 casos
próprios** de JSON válido com forma errada — o tipo de coisa que uma bateria
tende a não cobrir porque o autor não pensou naquilo:

| Caso | Resultado |
|---|---|
| raiz é lista em vez de objeto | bloqueia |
| `superadas` é string | bloqueia |
| `superadas` é objeto, não lista | bloqueia |
| item sem a chave `branch` | bloqueia |
| `branch` nula / vazia | bloqueia |
| chave no singular (`superada`) | bloqueia |
| JSON truncado / arquivo vazio / ausente | bloqueia |
| **caso bom** | libera **exatamente uma** branch |

**Nenhuma forma malformada libera superfície.** Confirmei também que a
comparação é `in` sobre um **conjunto** (`guarda-regras-duras.py:127`), ou
seja, igualdade exata — uma branch com nome parecido não é liberada por
substring.

E testei o **cache**, que era o meu maior receio, porque cache velho poderia
servir "liberado" depois de o autor remover a branch da lista. As três
direções estão corretas: lista alterada depois do cache **recalcula**; cache
mais novo que a lista **é usado**; cache com mais de 15 min **expira**.

**Uma nuance, não um bloqueio**: a comparação de mtime usa `>=`. Se a lista
for editada no MESMO instante de relógio em que o cache foi escrito, o cache
prevalece — e na direção de *remover* uma branch da lista isso mantém a
superfície liberada por até 15 minutos. A janela é de sub-segundo e o
sistema de arquivos aqui tem resolução fina, então na prática não ocorre.
Registro porque a direção do erro é a permissiva, e isso merece estar escrito
em algum lugar.

Tarefas `1650` e `1240` → `.concluida`. Lock de `3-metodo` liberado.
