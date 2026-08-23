---
de: principal
para: banca
tipo: tarefa
estado: aberta
assunto: Propor e CONSTRUIR esquemas em TikZ que melhorem o entendimento do processo metodológico (Cap.3) — loop de melhoria com goal
prioridade: alta
nao_atrapalhar: NÃO toca números/artefatos (freeze do autor) — é ilustração de processo. GRÁFICOS DE DADOS ficam para depois; agora é esquema/diagrama.
referencia: 3-metodo/texto.tex; figuras TikZ já aceitas no Cap.3
---

# Objetivo (ordem direta do autor)

Propor e **construir, em TikZ (TeX)**, esquemas que melhorem o **entendimento e a
explicação do processo metodológico** do FALCO (Cap.3). São **sugestões** para o
autor aprovar — **NÃO mergeia na main**.

Confirme sua identidade pelo título da sessão (ADR 0011) antes de agir.

## Candidatos de esquema (escolha os que mais esclarecem; pode propor outros)

- O **laço FALCO em 3 fases**: Fase 1 (*cold start* informado) → Fase 2 (seleção
  por incerteza com LLM Inicial) → Fase 3 (refinamento com LLM Avançado), com os
  pontos de decisão (gate/régua) e o critério de parada.
- O **mapa do programa experimental** (E0–E6 e o E3) e como se encadeiam / o que
  cada um responde (RQ1–RQ4).
- O **pipeline de dados / rastreabilidade** (do conjunto inicial $L_0$ ao artefato
  de execução versionado).
- A **decisão de gate e da régua** ($0{,}95\times D$) como fluxo.

## Loop de melhoria COM GOAL (ordem do autor)

Entre em **loop de melhoria**: rascunhe o TikZ, **autoavalie contra o goal** — "a
figura ficou **muito boa e ilustrativa**?" (fluxo inequívoco, rótulos claros,
coerente com o texto, sem poluição visual, legível em P&B) — melhore, repita,
**até você mesma julgar que ficou muito boa e ilustrativa**. Você decide quando
parou. Se não tiver LaTeX no contêiner para renderizar, itere no código e no
desenho raciocinando o render; registre que não compilou.

## Restrições

- **TeX/TikZ puro**, compilável e autocontido (standalone OU pronto para `\input`
  no Cap.3). **Sem gráfico de dados** (fica para depois).
- **Freeze:** não altere números, artefatos nem conclusões — é ilustração do
  processo, não resultado.

## Entrega

Na **sua branch** + caixa (v1.5 §2-ter): os arquivos `.tex` das figuras + uma nota
curta por esquema (o que esclarece, onde entra no Cap.3, e por que você a considerou
"muito boa e ilustrativa"). Depois **poke o principal** com o código
(`branch@sha:caminho`). Um tick; se precisar de mais iterações, o principal re-kicka.
