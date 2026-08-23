---
de: principal
para: revisor2
tipo: tarefa
estado: aberta
assunto: R1 de forma (travessões) no Cap.5 (resultados-FALCO)
prioridade: media
nao_atrapalhar: só FORMA; NÃO toca números/artefatos/conclusões (freeze do autor). O autor pode estar reescrevendo conteúdo do Cap.5 — se houver conflito, entregue na sua branch e sinalize; o principal reconcilia no gate.
referencia: 5-resultados-falco/texto.tex; padrão aprovado no Cap.3 (main @4ec5431)
---

# Objetivo

R1 de **forma** no Cap.5: converter travessões de **prosa e de título** em pontuação,
no padrão aprovado do Cap.3 (§14 humanize: dois-pontos / parênteses / vírgula).
**NADA de conteúdo/número/conclusão** (freeze do autor).

Confirme identidade pelo título da sessão (ADR 0011) antes de agir.

# Inventário medido na main (para eficiência — reconfira)

**Títulos de subseção (converter, de forma CONSISTENTE — sugiro dois-pontos):**
- l.21 `\subsection{RQ1 --- assertividade}` → `RQ1: assertividade`
- l.77 `RQ2 --- custo e o efeito do cache`
- l.131 `RQ3 --- perfil de erro`
- l.151 `RQ4 --- efeito do instrumento de medição`

**Prosa (converter):** l.418, 571, 579, 586–587, 609, 619, 657, 673–674
(apartes com `---`; use parênteses ou dois-pontos conforme o caso).

**Tabela (DEIXAR — é formatação):** l.90–94, 212, 216, 276, 649
(`—`/`---` em células e `\multicolumn`).

**Paralelismo negativo (avaliar, não forçar):** l.128 "registrar... não só o modelo,
mas" — em PT isso costuma ser legítimo; só reescreva se soar como tell, senão reporte.

# Entrega

Na **sua branch** + caixa (§2-ter): o diff + **antes/depois**. Se colidir com reescrita
do autor no Cap.5, não resolva sozinho — entregue e sinalize. **Poke o principal**
(session_01JWRRPCroKSVBbRpCGBwpLG) com o código (`branch@sha:caminho`). Um tick.
