---
de: principal
para: local
tipo: aviso
acao_esperada: ADENDO à tarefa 1130 (migração das referências): o autor aprovou saldar a dívida das 342 entidades fora do vocabulário controlado nos 140 fichamentos legados. Como as fichas estão indo para o repo privado sob padrão de especialista, PADRONIZE o vocabulário na mesma passada — é o momento barato (uma mão só nas fichas). Revisor2 cruza o mapa 342->canônico.
referencia: dec-divida-vocabulario aprovada pelo autor 2026-08-22 · _VOCABULARIO.md + check-fichamentos.py (hoje no repo da tese) · tarefa 1130
criada_em: 2026-08-22T12:00:00Z
---

As 342 entidades são termos livres (ex.: "topic-models", "cnn",
"deep-active-learning") que deveriam usar os termos canônicos do
_VOCABULARIO.md. Ao reorganizar as fichas no repo privado:
- gere o mapa 342 -> termo canônico (ou proponha novos termos canônicos onde
  o vocabulário for pobre — decisão sua de especialista, o revisor2 confere);
- leve o _VOCABULARIO.md e o check-fichamentos.py para o repo privado junto
  das fichas (é lá que passam a viver), ou deixe claro no de/para o que a tese
  mantém;
- objetivo: check-fichamentos.py exit 0 no repo privado, sem as 342 pendências.
Não bloqueia a migração; é a mesma passada. Reporte o de/para ao principal.
