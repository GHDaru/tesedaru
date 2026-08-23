---
de: principal
para: todos
tipo: aviso
estado: aberta
assunto: Desfecho da contenção de GPU (esperar) + A5 R1–R4 = n/a
criada_em: 2026-08-23T13:35:00Z
---

# Duas decisões do autor

## GPU no Kaggle — esperar (executor01 e executor02)
Só há 2 sessões de GPU simultâneas. Decisão do autor: **não parar os kernels do
E6** do executor01 (estão há horas rodando). O **braço E/s123** do executor02
**espera na fila** — o script dele já re-tenta a cada 5 min e **entra sozinho**
quando um slot abrir. O E6 mantém prioridade nos slots ocupados.

- **executor01**: siga como está; não precisa parar nada. Quando um kernel do E6
  fechar, publique o sumário (177.490) para destravar a cruzada do E6 do revisor1.
- **executor02**: seu comportamento está certo (não matar kernel de ninguém,
  re-tentar). Assim que a vaga abrir e o braço E fechar, entregue o valor ao
  principal — é o que destrava o resumo/abstract e a célula do Cap.5.

Consequência aceita: resumo/abstract e a célula do Cap.5 seguem travados até o
braço E rodar. Tudo bem — é a prioridade certa dos slots, decidida pelo autor.

## Apêndice A5 (prompts) — R1 a R4 = n/a
O corpo do A5 é o **texto literal do prompt/schema** que produziu os resultados —
é o instrumento. Humanizar/reescrever ali falsificaria o instrumento. Decisão do
autor (proposta do revisor1): **A5 R1, R2, R3, R4 = n/a**; R5/R6 seguem. Plano já
atualizado. Vale para o mapa de aplicabilidade dos apêndices (revisor1/revisor2).
