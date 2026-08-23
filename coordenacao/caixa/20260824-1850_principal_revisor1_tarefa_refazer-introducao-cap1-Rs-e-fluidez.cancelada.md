---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
assunto: Refazer a Introdução (Cap.1) com o estado ATUAL — passar os R's e avaliar fluidez
prioridade: alta
nao_atrapalhar: FREEZE do autor — não altere número, artefato nem conclusão; é trabalho de forma, fluidez e coerência narrativa. Se algo do texto parecer factualmente desatualizado, REPORTE, não corrija número.
referencia: 1-intro/texto.tex na main ATUAL (inclui o §1.3 já reescrito @4a84cb9); padrão dos R's do Cap.3/Cap.5
---

# Objetivo (ordem do autor)

Refazer a **Introdução (Cap.1)** "com o que temos no momento": deixá-la coerente
com o estado atual da tese, **passar os R's** e **avaliar a fluidez**.

Confirme sua identidade pelo título da sessão (ADR 0011). Ritual v1.8: rode
`git fetch origin main "+refs/heads/mensageria:refs/remotes/origin/mensageria"`
e trabalhe sobre a **main atual** (o §1.3 já foi aliviado no @4a84cb9 — não desfaça).

## O que fazer

1. **Coerência com o estado atual:** leia o Cap.1 inteiro e verifique se a
   narrativa bate com a tese como está hoje (v1 congelada). Onde houver
   descompasso factual, **reporte** (não conserte número — freeze).
2. **R's de forma:** R1 (travessões de prosa → pontuação; deixe travessões de
   tabela), R2 (siglas glosadas na 1ª ocorrência), R6 (jargão). Rode o humanize
   (todos os tells: paralelismo negativo, filler, vocabulário-IA, regra de três,
   gerúndio superficial, negrito mecânico).
3. **Fluidez:** avalie e melhore o encadeamento de raciocínio (o autor achou o
   §1.3 antigo "denso e difícil de acompanhar"). Frases mais curtas onde ajudar,
   transições claras, sem perder conteúdo nem número.

## Restrições

- **FREEZE:** nenhum número/resultado/afirmação científica muda. Só forma,
  fluidez, ordem e clareza.
- É **sugestão** para o gate do autor — **não mergeie na main**.

## Entrega

Na **sua branch** + caixa (§2-ter): o diff (antes/depois) **e** um laudo curto de
fluidez (o que travava, o que melhorou). Depois **poke o principal**
(session_01JWRRPCroKSVBbRpCGBwpLG) com o código (branch@sha:caminho). Um tick.
