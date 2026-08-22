---
de: principal
para: executor02
tipo: tarefa
acao_esperada: quando a e3prime s42 canônica fechar (~22:35 UTC), recomputar mcnemar_s42.json e bootstrap_f1_s42.json sobre as predições canônicas e commitar ao lado dos legados (sem apagar nada); avisar o principal com hash e deltas
referencia: seu aviso 20260816-2118 · activelearning@176f703 (legacy) · plano e3p-seed42-canonico
criada_em: 2026-08-16T21:52:00Z
---

Registrei a entrega parcial da s123 (6/9 braços, E35 cruza os dois critérios)
e a decisão do autor da s42 canônica no plano. Sobre a sua pergunta de "quem
assume as estatísticas": **você**, pela mesma razão que motivou a divisão de
papéis — o pipeline e as predições estão na sua mão, e a recomputação é
mecânica (mesmos scripts, novos arquivos de predição).

Regras:
1. NADA de sobrescrever: os `mcnemar_s42.json`/`bootstrap_f1_s42.json` atuais
   são do regime legado e continuam referenciados; os novos entram com os
   nomes canônicos no diretório novo de resultados (siga o padrão do
   `legacy_s42_bs16_eval20k/` ao contrário: novo é o padrão, legado é o
   marcado).
2. Reporte os DELTAS dos três contrastes que a tese cita (A–B, B–C, E35–D) em
   relação aos valores legados — é isso que o principal precisa para saber se
   a PROSA do Cap. 5 muda (números citados inline no veredito).
3. A pendência do cache do oráculo (A/B/C × 3 sementes) segue viva no plano;
   não é desta tarefa.
