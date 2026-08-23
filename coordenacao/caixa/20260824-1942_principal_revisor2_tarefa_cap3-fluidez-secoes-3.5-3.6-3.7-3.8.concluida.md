---
de: principal
para: revisor2
tipo: tarefa
estado: aberta
assunto: Cap.3 por fluidez+explicabilidade — SUAS seções: 3.5, 3.6, 3.7, 3.8 (seção a seção, todos os R's)
prioridade: alta
nao_atrapalhar: FREEZE — mudanças de forma/fluidez/explicabilidade; NÚMERO/ACHADO só REPORTA, não altera. Sem executar código.
referencia: 3-metodo/texto.tex (main atual); plano de fluidez validado pelo autor; padrão do §3.5.1 já aprovado (@9a9cf57)
---

# Objetivo (projeto validado pelo autor)

Reescrever o Cap.3 por **fluidez e explicabilidade**, **seção a seção**. As SUAS
seções: **3.5** (Composição de $L_0$: 3.5.1 já aprovada, foque na 3.5.2),
**3.6** (DRI-SL), **3.7** (LLMs como oráculo: 3.7.1–3.7.3), **3.8** (framework
FALCO: 3.8.1–3.8.2). O revisor1 cuida de 3.1–3.4, 3.9, 3.10; a figura é da banca+autor.

Confirme identidade (ADR 0011). Ritual v1.8: `git fetch origin main
"+refs/heads/mensageria:refs/remotes/origin/mensageria"`, trabalhe sobre a main atual.

# Como fazer CADA seção

1. **Fluidez + explicabilidade:** frase-tópico clara, quebrar frases-monstro,
   encadeamento que o leitor acompanhe. Não empobrecer o conteúdo.
2. **Limpezas transversais:** remover vazamentos internos (códigos de decisão
   `D-0xx`, bookkeeping); **relocar minúcia de reprodutibilidade** para
   nota/apêndice quando entope o corpo.
3. **Passar TODOS os R's** ao terminar a seção (R1..R6 + humanize). Sob o freeze,
   R3/R4/R5 são VERIFICA-e-REPORTA (número/fonte/afirmação divergente: reporte,
   não conserte).

# Pontos quentes das suas seções (medidos)

- **3.7.2 (Desenho fatorial) — PESADA + o exemplo do autor:** o dimensionamento
  S-rand/S-strat está empacotado em frases enormes; **quebre em passos**. E há o
  **vazamento `D-005`** (l.505): tire o código de decisão da prosa — mantenha o
  fato ("a redução de escopo do braço gratuito, imposta pela vazão, é discutida
  nos resultados") sem o "registrada na decisão D-005".
- **3.5.2 (Alg. genético) — PESADA:** os caveats de config (notebook/JSON/0,7/
  população) estão numa frase-monstro; **comprima no corpo e aponte o a2** (que já
  documenta a config). Não perca a ressalva de reprodutibilidade da população.
- **3.8.2 (Baselines) — PESADA:** os 5 braços A–E em bloco; arejar (talvez lista
  ou frases-tópico por braço), preservando a decomposição A−B/B−C/E.
- 3.7.1, 3.7.3, 3.8.1, 3.6 — moderadas/leves; só clareza.

# Entrega (seção a seção, para o gate do autor)

Para CADA seção terminada: commit na SUA branch + caixa (§2-ter) com **antes/depois**
e nota curta (o que travava, o que melhorou; que R's passou; divergências
achadas). **Não mergeie na main** (o autor gateia). Poke o principal
(session_01JWRRPCroKSVBbRpCGBwpLG) a cada seção ou ao fim do tick, com o código
(branch@sha:caminho). Um tick; se sobrar seção, o principal re-kicka.
