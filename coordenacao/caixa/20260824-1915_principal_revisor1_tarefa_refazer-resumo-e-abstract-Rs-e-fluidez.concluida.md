---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
assunto: CORREÇÃO — a tarefa é o RESUMO (não a introdução): refazer resumo + abstract com o estado atual, R's e fluidez
prioridade: alta
nao_atrapalhar: FREEZE do autor — NÃO altere número/resultado. A introdução JÁ foi validada pelo autor; a tarefa da intro (1850) está CANCELADA.
referencia: 0-iniciais/resumo.tex (PT) e abstract.tex (EN); plano marca R1/R2 pendentes, R6 feito
---

# Correção da tarefa

A tarefa anterior (refazer a introdução, 1850) está **CANCELADA** — o autor **já
validou a introdução**. A tarefa correta é o **RESUMO**.

Confirme identidade pelo título (ADR 0011). Ritual v1.8: `git fetch origin main
"+refs/heads/mensageria:refs/remotes/origin/mensageria"`, trabalhe sobre a main atual.

# Objetivo (ordem do autor)

Refazer o **resumo** (`0-iniciais/resumo.tex`) e o **abstract** (`abstract.tex`)
"com o que temos no momento": coerentes com a tese como está hoje (v1 congelada),
passar os R's e avaliar/melhorar a **fluidez**.

## O que fazer

1. **Coerência com a v1 (freeze):** o resumo/abstract devem bater com os números e
   conclusões que já estão na tese. Se algum número do resumo **divergir** do corpo,
   **REPORTE** (não conserte número, não invente — freeze). Alinhar prosa ao que já
   existe é ok; mudar resultado não.
2. **R's de forma:** R1 (travessões de prosa → pontuação), R2 (siglas na 1ª
   ocorrência — FALCO/LLM já abrem; audite o resto), + humanize completo.
3. **Fluidez:** encadeamento claro, sem densidade excessiva; PT e EN espelhados.

## Restrições

- **FREEZE:** nenhum número/resultado muda. Só forma, fluidez, coerência.
- É **sugestão** para o gate do autor — **não mergeie na main**.

## Entrega

Na **sua branch** + caixa (§2-ter): diff antes/depois (resumo e abstract) + laudo
curto de fluidez + qualquer divergência de número que você tenha achado (para o
autor decidir). **Poke o principal** (session_01JWRRPCroKSVBbRpCGBwpLG) com o
código (branch@sha:caminho). Um tick.
