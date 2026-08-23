---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
assunto: R1 de forma (travessões) no Cap.4 (resultados-L0)
prioridade: media
nao_atrapalhar: só FORMA; NÃO toca números/artefatos (freeze do autor)
referencia: 4-resultados-l0/texto.tex; padrão aprovado no Cap.3 (main @4ec5431)
---

# Objetivo

R1 de **forma** no Cap.4: converter os travessões (`—`) de **prosa** em pontuação,
no mesmo padrão aprovado do Cap.3 (dois-pontos / parênteses / vírgula, conforme o
caso; §14 do humanize). **NADA de conteúdo/número** (freeze do autor).

Confirme identidade pelo título da sessão (ADR 0011) antes de agir.

## Passos

- Localize os `—` de prosa em `4-resultados-l0/texto.tex` (medi 3 na main).
- **Deixe travessões de TABELA** (`---` em `\multicolumn`/células) — é formatação.
- Converta os de prosa; apresente **antes/depois**.
- De passagem, cheque os demais tells de escrita-IA (paralelismo negativo, filler,
  vocabulário-IA, regra de três, gerúndio superficial) — mas **só reporte**, não
  reescreva conteúdo (freeze).

## Entrega

Na **sua branch** + caixa (§2-ter): o diff + antes/depois. **Poke o principal**
(`branch@sha:caminho`). Um tick.
