# Diário de Bordo — Jornada Autônoma (tese FALCO)

Registro operacional contínuo. Horários em GMT-3 (São Paulo).
Decisões formais com racional completo: `docs/decisoes.md`.

---

## 16/07/2026 23:17 — Preparação da jornada
- Missão recebida e reescrita para aprovação do autor; aguardando OK para iniciar.
- Inclusões do autor aceitas: (1) este diário com horário GMT-3; (2) experimento
  E0-P de ablação de prompt — modelo fraco (gpt-4o-mini) × prompts {v3, v4a
  regras de fronteira, v4b few-shot com pares confundidos}, pareado, McNemar.
  Racional: anatomia dos erros mostrou ~48% de erros de convenção de catálogo,
  atacáveis por prompt; mini custa ~US$0,05/1k com cache.
- Estado herdado: E0 oficial parcial commitado (OpenAI completo; v4-pro completo;
  glm-5.2 e 4 free do OpenRouter retomados em 2º plano). Revisão R1 da banca
  simulada com 4 bloqueantes mapeados. 122 fichamentos. FlowBuilder v0 no ar.

## 16/07/2026 23:22 — Checklist criado
- checklist.md com 8 blocos (A-H), ~45 tarefas; blocos A-G devem fechar na
  jornada; bloco H (GPU/BERTimbau + rotação de chaves) fica aberto por design.

## 16/07/2026 23:24 — OK recebido. Jornada iniciada.
- Ordem de ataque: A (correções R1) → B (biblioteca) → C (replays) → D
  (experimentos) → E (FlowBuilder) → F (escrita) → G (revisão R2).
- Runs em 2º plano herdados: MaaS (glm-5.2) e OpenRouter free — monitorados.

## 16/07/2026 23:27 — Bloco A concluído (10/10 correções da R1)
- A1: transição de fase agora usa V (vazamento de T eliminado no texto).
- A2: 8 sementes + IC bootstrap no E3 (Wilcoxon com n<6 era infalseável).
- A3: fitness do AG em partição de aferição; envelope reavaliado em T intocado.
- A4: LCE agora cita ALC (Guyon 2011) e demarca os dois deltas.
- A5: nova seção "Ameaças à validade" (externa/interna/constructo).
- A6: literatura de noisy labels no Cap.2 (Frénay 2014, Natarajan 2013, Song 2023).
- A7: constantes justificadas (85% ancorado no teto supervisionado 89,56%).
- A8: L_ideal,0 definido inline; procedimento da subamostra 50k declarado.
- A9: 5º braço do E3 (oráculo-total) separa ruído × parcimônia.
- A10: seção esparsa condensada citando a dissertação; figura ActiveLLM em TikZ real.
- Verificação estática: 0 citações órfãs, 0 refs quebradas.
- Próximo: Bloco B (portar PVBin do legado).
