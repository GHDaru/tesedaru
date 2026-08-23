---
de: banca
para: principal
tipo: tarefa
acao_esperada: (1) integrar em bloco os SETE apêndices desta branch (B, A, C, D, E, F, G) + correções 12pt, com compilação completa (DoD IX); (2) adicionar PSI à lista de siglas (0-iniciais/acronimos.tex, sua superfície): "PSI & \textit{Population Stability Index} (índice de estabilidade populacional)"; (3) repassar ao revisor1 a conferência do CV do Apêndice F
referencia: a7-parada-drift/texto.tex + esq-ciclo-vida-modelo.tex · branch banca/esquemas-tikz-metodo · ordem do autor (2026-08-23)
criada_em: 2026-08-23T23:55:00Z
---
Conclusão do passe no Apêndice G (claim 2340) — e FECHAMENTO DA SÉRIE dos
sete apêndices, toda por ordem direta do autor na conversa da banca. Ele
recebeu as páginas de cada um.

Apêndice G:
1. Gatilhos de parada em lista numerada; racional estatístico intacto.
2. Autocontenção: sem \ref{ch:metodo}, sem símbolo V solto, sem "E0".
3. Siglas: NIM e SGD abertos conforme a lista; PSI aberto em linha — MAS
   PSI NÃO ESTÁ NA LISTA (pedido acima, superfície sua).
4. Números reconferidos: 0,0224 ✓; 22,4x ✓; 31,6/40,1% → "32–40%" ✓;
   991/982/6.009/4.742 (laudo) ✓; Wilson n=1.000 ≈ 2,5 p.p. ✓.
5. Figura NOVA do ciclo de vida (esq-ciclo-vida-modelo, corpo 12; requer
   amsmath, que a tese carrega). Achado: vãos de 1,2–1,4cm entre colunas
   não comportam rótulos de seta em corpo 12 — semântica nas caixas/nota.
6. 0 erros / 0 overfull nas medidas reais.

BALANÇO DA SÉRIE (tudo nesta branch, nada na main):
- 7 apêndices com passe de excelência, autocontidos, 0 erros/0 overfull;
- 6 figuras de apêndice calibradas em corpo 12 (F sem figura, por decisão
  fundamentada no princípio V) + os 5 esquemas do Cap. 3 ainda propostos
  (estes seguem em corpo 10 — recalibrar SE o autor decidir inseri-los);
- verificação executável dos 94 valores do Apêndice F;
- NOTA-esquemas.md com o registro completo de todos os loops.
