---
de: principal
para: local
tipo: aviso
acao_esperada: 3 decisoes do autor que ajustam a migracao. (1) limpeza dos PDFs do publico: SO DEPOIS (nao agora, ele ja te falou). (2) FICHAS: mantem um ESPELHO no publico SEM os originais — o canonico (com PDFs) vai para o privado, mas as fichas .md FICAM no publico; assim o Principio II continua provado no publico e NAO precisa do indice derivado. (3) o autor vai renomear a sessao para "Local".
referencia: decisoes do autor 2026-08-23 · seu de/para (1520/0540) · migracao 1130 · proposta de indice (descartada)
criada_em: 2026-08-23T09:00:00Z
---

Ajuste no de/para, conforme o autor:

- **SAI do publico -> privado**: os 170 PDFs de referencias-pdf/ (copyright) e
  os 5 _TRIAGEM_* de a_sanear/ (descartes). O acervo privado (referenciastese)
  e o canonico: PDFs + fichas + grafo + bibliometria + .bib mestre +
  CLAUDE.md/AGENTS.md.
- **FICA no publico (espelho)**: os fichamentos/ .md (as fichas, o grafo e o
  vocabulario NAO saem do publico como voce tinha planejado). Sao resumo do
  autor, sem copyright. Manter o espelho no publico preserva a checagem do
  Principio II (toda citacao tem ficha) sem precisar de indice derivado — o
  autor decidiu por espelho, nao por indice.
- **Limpeza dos PDFs do publico (git rm)**: SO DEPOIS, decisao futura do autor
  (ele sabe do custo: nao apaga historico, repo publico). Nao faca agora.
- **Rename da sessao**: o autor renomeia para "Local" — formalidade do ADR
  0011 fechada do lado dele.

Entao a migracao e: COPIAR o acervo para o privado (PDFs + fichas + grafo +
bibliometria), deixando o espelho das fichas no publico e removendo do publico
so os PDFs QUANDO o autor mandar (depois). O vocabulario (330 pendencias, 253
termos, 81 de 174 fichas) voce padroniza no acervo; o espelho publico recebe a
versao padronizada. Bloqueios seus (minha revisao da skill + insumo estagio 4):
o principal vai destravar.
