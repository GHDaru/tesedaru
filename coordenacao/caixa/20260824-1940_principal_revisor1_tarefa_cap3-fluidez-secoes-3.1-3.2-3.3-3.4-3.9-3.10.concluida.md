---
de: principal
para: revisor1
tipo: tarefa
estado: aberta
assunto: Cap.3 por fluidez+explicabilidade — SUAS seções: 3.1, 3.2, 3.3, 3.4, 3.9, 3.10 (seção a seção, todos os R's)
prioridade: alta
nao_atrapalhar: FREEZE — mudanças de forma/fluidez/explicabilidade; NÚMERO/ACHADO só REPORTA, não altera. Sem executar código.
referencia: 3-metodo/texto.tex (main atual); plano de fluidez validado pelo autor; padrão do §3.5.1 já aprovado (@9a9cf57)
---

# Objetivo (projeto validado pelo autor)

Reescrever o Cap.3 por **fluidez e explicabilidade**, **seção a seção**. As SUAS
seções: **3.1** (Desenho), **3.2** (Conjunto de dados, com 3.2.1–3.2.4),
**3.3** (Classificadores), **3.4** (Métricas), **3.9** (Ameaças à validade),
**3.10** (Reprodutibilidade). O revisor2 cuida de 3.5–3.8; a figura é da banca+autor.

Confirme identidade (ADR 0011). Ritual v1.8: `git fetch origin main
"+refs/heads/mensageria:refs/remotes/origin/mensageria"`, trabalhe sobre a main atual.

# Como fazer CADA seção

1. **Fluidez + explicabilidade:** frase-tópico clara no início, quebrar
   frases-monstro, encadeamento que o leitor acompanhe. Não empobrecer o conteúdo.
2. **Limpezas transversais:** remover vazamentos internos (códigos de decisão
   `D-0xx`, "controle interno", refs de bookkeeping que não devem estar na tese);
   **relocar minúcia de reprodutibilidade** para nota de rodapé/apêndice quando
   entope o corpo, deixando 1 linha de resumo.
3. **Passar TODOS os R's** ao terminar a seção (R1 travessões, R2 siglas, R3
   fontes, R4 afirmações, R5 números, R6 jargão + humanize completo). Sob o freeze,
   R3/R4/R5 são VERIFICA-e-REPORTA: se achar número/fonte/afirmação divergente,
   **reporte**, não conserte.

# Pontos quentes das suas seções (medidos)

- **3.2.3 (Pré-proc + espaço de rótulos) — PESADA:** a minúcia 715/710/714 classes
  e "duas chaves de texto" trava o fluxo. Reloque o detalhe (nota/apêndice),
  mantendo no corpo só o essencial (621 vs 714 e por quê).
- 3.2.2 (item 1, conflitos + sensibilidade) e 3.2.4 (re-baseação/JS) — aliviar.
- 3.4 (LCE) — densa mas apropriada; só clareza.
- 3.9 — 4 blocos com cabeçalho-negrito; legítimo, só fluidez.
- 3.1 — aparte "controle interno" um tanto meta; suavizar.

# Entrega (seção a seção, para o gate do autor)

Para CADA seção terminada: commit na SUA branch + caixa (§2-ter) com **antes/depois**
e nota curta (o que travava, o que melhorou; que R's passou; divergências de
número achadas). **Não mergeie na main** (o autor gateia). Poke o principal
(session_01JWRRPCroKSVBbRpCGBwpLG) a cada seção ou ao fim do tick, com o código
(branch@sha:caminho). Um tick; se sobrar seção, o principal re-kicka.
