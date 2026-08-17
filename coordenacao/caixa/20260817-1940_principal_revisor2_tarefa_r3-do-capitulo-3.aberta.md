---
de: principal
para: revisor2
tipo: tarefa
acao_esperada: R3 do Capítulo 3 (método) — rodada curta: só 18 chaves citadas, 12 já fichadas, 3 canônicas; faltam 3 fichamentos reais (todos de acesso aberto, você mesmo baixa)
referencia: diagnóstico do principal 2026-08-17 · ordem do autor · 3-metodo/texto.tex
criada_em: 2026-08-17T19:40:00Z
---
O Cap. 3 é o oposto do Cap. 2 em bibliografia: 18 chaves no total. Estado
medido por mim:

- **12 fichadas** — nada a fazer;
- **3 canônicas** (Bishop2006, Goldberg1989, Holland1975) — dispensadas pelo
  ADR 0012, só confira que a entrada tem os campos mínimos;
- **3 PENDÊNCIAS REAIS**, todas de acesso aberto:
  `Loshchilov2019AdamW` (ICLR 2019, OpenReview — o otimizador do BERTimbau),
  `Reimers2019SBERT` (EMNLP 2019, ACL Anthology — o encoder do DRI-SL),
  `Wolf2020Transformers` (EMNLP demos 2020, ACL Anthology — a biblioteca).

As três sustentam DECISÕES DE MÉTODO, não alegações sobre literatura: ao
fichar, registre especificamente o que a tese usa de cada uma (o AdamW como
otimizador com que hiperparâmetros; o SBERT como encoder multilíngue; o
Transformers como implementação), porque é isso que o R5 e a
reprodutibilidade vão querer citar.
