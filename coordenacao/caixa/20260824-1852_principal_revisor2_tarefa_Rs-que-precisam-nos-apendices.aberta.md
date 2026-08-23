---
de: principal
para: revisor2
tipo: tarefa
estado: aberta
assunto: Passar os R's que os apêndices precisam (a1–a7) — sob o freeze
prioridade: alta
nao_atrapalhar: FREEZE do autor — R3/R4/R5 (fontes/afirmações/números) NÃO entram (tocam achado). Só os R's de forma.
referencia: apêndices a1-lce, a2-ag, a3-drisl, a4-biblioteca, a5-prompts, a6-tabelas, a7-parada-drift; suas entregas anteriores (apendices-a1-a7 @20260823-2000) e a do revisor1 (r1r4-dos-apendices)
---

# Objetivo (ordem do autor)

Passar **os R's que os apêndices precisam**. Pelo plano, os apêndices estão em
R1 andamento e R2/R6 pendentes. Sob o freeze, os R's vivos são **de forma**:
**R1** (travessões de prosa → pontuação; deixe travessões de tabela), **R2**
(siglas na 1ª ocorrência), **R6** (jargão). **NÃO** rode R3/R4/R5 (tocam
fonte/afirmação/número — congelados).

Confirme identidade pelo título (ADR 0011). Ritual v1.8: `git fetch origin main
"+refs/heads/mensageria:refs/remotes/origin/mensageria"`, trabalhe sobre a main atual.

## Passos

1. Varra a1–a7 (a5-prompts já tem R5 feito; foque nos demais).
2. Aplique R1/R2/R6 por apêndice, no padrão aprovado (Cap.3/Cap.5). Rode o
   humanize (todos os tells) e **só reporte** o que for conteúdo.
3. Reaproveite/concilie com o que já existe (sua entrega `apendices-a1-a7` e a
   `r1r4-dos-apendices` do revisor1) — não retrabalhe o que já está pronto.
4. Cuidado com armadilhas de tabela e menos matemático (ex.: `$-$`), como no Cap.5.

## Restrições

- **FREEZE:** nenhum número/artefato/afirmação muda. Só forma/siglas/jargão.
- É **sugestão** para o gate do autor — **não mergeie na main**. Entregue por
  apêndice com antes/depois.

## Entrega

Na **sua branch** + caixa (§2-ter): diff antes/depois por apêndice + o que ficou
como pendência de R3/R4/R5 (para depois do freeze). **Poke o principal**
(session_01JWRRPCroKSVBbRpCGBwpLG) com o código (branch@sha:caminho). Um tick.
